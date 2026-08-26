# WORKER TASK — Independent acceptance (fresh checkout)

Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-ai-suggestions-alias-edit-mvp
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Audit
Phase: Acceptance
Native planning mode: not-used
Reasoning recommendation: High
Task identity: FRAMENEST-AI-SUGGESTIONS-ALIAS-EDIT-ACC-01
Independence required: yes
Evidence posture: independent
Authority renewal: this is a fresh session. Session 02 implementation authority
  expired at `02_report_00.md`. That report is a claim, not proof. You inherit
  no mutation authority from it.
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
Acceptance candidate: 36ffdb197da9294fb1fbb06931f8169061a25c9b
Acceptance owner map: Cooperator-accepted plan 01_report_00.md plus prompt freeze (ordinary Edit GET alias if non-empty) plus candidate ADR-0077 plus implementation grant 02_implementation_00.md
Acceptance allowlist: inspection of the 15 committed paths only; no product edits
Acceptance risk claims: ordinary Edit is alias write not canonical write; ordinary cannot Analyze / Load / Apply; hosted hides Analyze+Load+dropdown+strips; dropdown GET does not call the provider; Load does not bulk-replace Current; schema head 0033; four companion_mutation unchanged; no fifth mutation; ADR-0062/0076 bodies untouched
Acceptance control matrix: see § Control matrix
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates only
```

```text
Evidence tier: E3
Evidence tier basis: access-control split on Edit/Save (ordinary alias.write vs canonical.write / analysis.run); hosted chrome hide; independent of the implementing session
Authorized implementation stages: none
Combined implementation envelope: prohibited
Implementation stage gates: not-applicable
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: canonical checkout remains 2aead540ee39a81a96425902f85e9b9a34f0d690; session-02 worktree remains untouched
Activated stricter profile: none
Terminal implementation report point: not-applicable
```

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: JS and Python matrix named below
Affected tests: same matrix re-run from a fresh checkout of 36ffdb19
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

Independence rule: you did not implement `36ffdb19…` or `6b957be…`. If this
session materially authored those commits, stop BLOCKED (independence
conflict).

This prompt grants read-only acceptance evidence only. No product edits, no
commits, no push, no NUC, no publication, no closure.

## Mission

Independently accept or reject unpublished candidate
`36ffdb197da9294fb1fbb06931f8169061a25c9b` against:

1. This prompt’s freeze and control matrix.
2. `/home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/01_report_00.md`
   except its superseded sentence that Current always seeds from canonical and
   never alias.
3. Candidate `docs/adr/0077-ordinary-alias-edit-affordance-and-per-field-ai-suggestions.md`.

Parent / public `main` / canonical HEAD:

```text
2aead540ee39a81a96425902f85e9b9a34f0d690
```

Claim to verify, not believe:
`/home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/02_report_00.md`

Do not implement. Do not replan. Do not reopen R1–R3′. Do not open R4 or VPS.

## Mandatory reading

1. This prompt.
2. `/home/agile/Projects/framenest/AGENTS.md`
3. `.ap/AP.md`, `.ap/AP_WORKER.md`
4. `docs/WORKER_EXECUTION_CONTRACT.md`
5. The plan and implementation claim named above.
6. Candidate ADR-0077. ADR-0062 / 0076 / 0023 bodies: inspect only, do not edit.

## Repository gate

```text
Repository checkout topology: standalone checkout with pinned submodule
Canonical root: /home/agile/Projects/framenest
Expected canonical branch: feat/x-meme-browser-companion
Expected canonical HEAD: 2aead540ee39a81a96425902f85e9b9a34f0d690
Expected canonical tree: 0900818f57326017712c07686c49de61d534507f
Expected canonical working tree: tracked-clean
Pinned submodule: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: 2aead540ee39a81a96425902f85e9b9a34f0d690 (re-verify ls-remote)
```

Before creating a fresh checkout, verify and record those facts. Any canonical
drift: classify RF-12 and stop; never tidy canonical.

Session-02 worktree
`/home/agile/Projects/framenest-worktrees/framenest-ai-suggestions-alias-edit-mvp-w2`
must still be at `36ffdb19…`, tracked-clean. Do **not** use it as your working
copy. Do not edit or commit in it.

Create **one** fresh detached checkout of the candidate:

```text
git -C /home/agile/Projects/framenest worktree add --detach \
  /home/agile/Projects/framenest-worktrees/framenest-ai-suggestions-alias-edit-mvp-w3 \
  36ffdb197da9294fb1fbb06931f8169061a25c9b
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
Your checkout HEAD must equal `36ffdb19…`;
`git merge-base --is-ancestor 2aead54… HEAD` must succeed;
`git rev-list --count 2aead54…..HEAD` equals 2.

## Positive authority

- Read candidate, canonical, plan, claim, ADR-0077.
- Diff `36ffdb19…` against `2aead54…`. Confirm the path set is exactly these
  15 files (or fail extras/missing):

  ```text
  PRODUCT.md
  SPEC.md
  docs/X_COMPANION.md
  docs/adr/0077-ordinary-alias-edit-affordance-and-per-field-ai-suggestions.md
  docs/adr/README.md
  src/framenest/adapters/api/web/app.js
  src/framenest/adapters/api/web/index.html
  src/framenest/adapters/api/web/styles.css
  tests/automatic_analysis_lifecycle.test.js
  tests/catalog_card_ai_quick_action.test.js
  tests/companion_web_bridge.test.js
  tests/contract/test_local_web_application.py
  tests/metadata_alias_edit.test.js
  tests/tailscale_identity_frontend.test.js
  tests/upload_cockpit_async_ownership.test.js
  ```

- Confirm **no** `alembic_environment/versions/0034*`, no ADR-0062/0076/0023
  **body** edits, no `SECURITY.md`, no Python API modules, no persist-join
  files, no fifth `companion_mutation`.
- Run the declared Python and Node evidence.
- Write exactly the report file below.
- Create and delete one temporary provenance probe file as specified.

## Negative authority

- No product, test, ADR-body, or docs edits (except the one Meta report).
- No Alembic 0034. No NUC, SSH, sudo, `gpgconf`, Funnel, VPS, providers,
  browser automation, secrets.
- No `.venv` reconstruction; no ambient `python` / `.venv/bin/python` /
  `poetry run`.
- No publication, push, or closure.
- No Max. No sub-agents.

## Control matrix (pass/fail)

**Positive (must hold on the candidate object + tests):**

1. Ordinary workspace Edit uses `identityAllowsMetadataEdit`
   (`alias.write` ∨ `canonical.write`); Details and Gallery card Edit follow it.
2. Ordinary `editMode === "alias"`: load canonical GET then alias GET; non-empty
   overlay becomes Current/baseline; Save is `PUT …/alias` with
   `display_title`, `description`, `tag_keys` only.
3. Admin Save remains `PUT …/metadata`. Canonical-write wins when both caps.
4. Hosted (`companionWebHosted()`): Analyze, Load, dropdown, strips hidden;
   Edit still shown per predicate.
5. Suggestions chrome: heading **AI suggestions**; dropdown + Load above Title;
   `GET /api/companion/review-inbox/{id}?limit=100`; dropdown change does not
   POST preview; Load sets revealed strips without
   `applyResolvedAiSuggestionToMetadataWorkspace`; ✅ copies one field or
   appends one mapped tag; website `app.js` contains no `/apply` substring.
6. Analyze (`analysis.run`, not hosted, not movie, not alias): confirm copy
   says strips not Current replace; success calls `presentInSessionSuggestion`;
   Analyze is not hidden after success; persist-join files unchanged vs parent.
7. Provider-miss: no “Generated automatically…” / View details essay; stale
   confirm shows the short retry message; live region uses Analyzing… / Loaded /
   `aiSuggestionErrorMessage`.
8. Schema head remains `0033`. Four `companion_mutation` routes unchanged.
9. ADR-0077 exists and index rows for 0062/0076 note succession **without**
   body edits.

**Negative (must not hold):**

- Ordinary Analyze / Load / inbox Apply.
- Ordinary canonical metadata PUT from this Edit Save.
- Alembic `0034`.
- Fifth `companion_mutation`.
- Gallery cards displaying alias (read path still canonical).
- Gallery 🧠 converted to per-field apply (parked bulk path may remain for
  admin; fail only if ordinary can see/use it).

Gallery 🧠 admin bulk canonical save is **parked debt**, not a fail.

## Execution route (RF-16)

Attempt declared isolated-worktree route first:

```text
./.ap/ap project check --root <fresh-checkout> --baseline 2aead540ee39a81a96425902f85e9b9a34f0d690
./.ap/ap exec --root <fresh-checkout> --baseline 2aead540ee39a81a96425902f85e9b9a34f0d690 --operation runtime-info
```

Expected miss: `declared CPython executable does not exist`. Classify
environment limitation. Do not repair. Do not fail the candidate solely for it.

**Task-specific deviation** after that classified miss:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 2aead540ee39a81a96425902f85e9b9a34f0d690
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 2aead540ee39a81a96425902f85e9b9a34f0d690 --operation runtime-info
```

Canonical `runtime-info` proves the envelope, not the candidate.

Provenance probe file **outside** git checkouts, e.g.
`/tmp/framenest-aliasacc-03-provenance.py`, printing `framenest.__file__` and
asserting it is under `<fresh-checkout>/src/framenest/`. Run it through
`ap exec` test-focus / `-c` only if the envelope allows trailing argv; otherwise
the test-focus invocation below must print the same path.

Python matrix (deviation: canonical `--root` + `--rootdir` / `pythonpath`
fresh-checkout):

```text
<fresh-checkout>/tests/contract/test_local_web_application.py
<fresh-checkout>/tests/contract/test_x_route_policy.py
<fresh-checkout>/tests/contract/test_media_alias_api.py
<fresh-checkout>/tests/integration/persistence/test_companion_review_migration.py::test_head_is_0033
```

Stopping condition: if `framenest.__file__` is not under the fresh checkout
`src/`, ENVIRONMENT LIMITATION for Python provenance; still run Node; do not
fail solely for the known launch-path miss; **do** fail on candidate defects.

Node from the **fresh checkout** root:

```text
node --test tests/automatic_analysis_lifecycle.test.js \
  tests/upload_cockpit_async_ownership.test.js \
  tests/tailscale_identity_frontend.test.js \
  tests/companion_web_bridge.test.js \
  tests/catalog_card_ai_quick_action.test.js \
  tests/metadata_alias_edit.test.js
```

Ambient encodings signature: rerun once through `ap exec`; never rebuild
`.venv`. First failing suite: preserve output, classify, stop that batch.

## Report contract

Write exactly:

```text
/home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/03_report_00.md
```

Begin EXACTLY:

```text
### Report for ORCHESTRATOR_CHAT
```

Professional English. Include: coordinate echo (whole, session `03`, exchange
`01`); PASS | PARTIAL | BLOCKED; `Phase-qualified result: acceptance-PASS`
only if every control-matrix row holds and minimum evidence is green,
else `not-applicable`; `Logical-whole closure: not-closed`; candidate SHA;
fresh checkout path; canonical still `2aead54…` tracked-clean; w2 untouched;
path-set vs parent; control-matrix table with evidence (`path:line` or test
id); test commands and outcomes including RF-16 deviation and
`framenest.__file__`; deviations/risks; one smallest next step (Cooperator
publication, then NUC); justification `final-acceptance`; authority expiry;
Resolved Execution Issues; Pre-Existing Failure Classification; capability
handshake (Plan Mode off; Max off or unknown).

## Human-governance routing

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
Trace discovery: /home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/
Trace project key: framenest
Trace logical-whole projection identity: framenest-ai-suggestions-alias-edit-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 03_acceptance_00.md
Destination path: /home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/03_acceptance_00.md
Archival: wait-for-report
```
