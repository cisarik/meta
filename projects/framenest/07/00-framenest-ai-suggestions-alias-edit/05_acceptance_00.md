# WORKER TASK — Independent full-fresh acceptance (correction candidate)

Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-ai-suggestions-alias-edit-mvp
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Audit
Phase: Acceptance
Native planning mode: not-used
Reasoning recommendation: High
Task identity: FRAMENEST-AI-SUGGESTIONS-ALIAS-EDIT-ACC-02
Independence required: yes
Evidence posture: independent
Authority renewal: this is a fresh session. Session 04 correction authority
  expired at `04_report_00.md`. That report is a claim, not proof. You inherit
  no mutation authority from it. Session 03 accepted parent `36ffdb19…`; this
  is full-fresh re-acceptance of the **corrected** candidate.
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
Acceptance candidate: afa0670e26d17b04570ad555ba4f922052507c6c
Acceptance owner map: Cooperator «koriguj» freeze in 04_correction_00.md plus candidate ADR-0077 as succeeded on this SHA
Acceptance allowlist: inspection of the committed path set below; no product edits
Acceptance risk claims: caller overlay is private to login_key (Alice ⊈ Bob, anonymous canonical); ordinary suggestion list is read-only; Apply/Analyze/canonical.write stay denied; hosted shows Load and hides Analyze; schema head 0033; four companion_mutation unchanged; no fifth mutation; ADR-0062/0076/0023 bodies untouched
Acceptance control matrix: see § Control matrix
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates only
```

```text
Evidence tier: E3
Evidence tier basis: identity-scoped catalog overlay merge; capability-split suggestion-list GET vs Apply/Analyze; independent of session 04
Authorized implementation stages: none
Combined implementation envelope: prohibited
Implementation stage gates: not-applicable
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: canonical checkout remains 36ffdb197da9294fb1fbb06931f8169061a25c9b; session-04 worktree remains unused as working copy
Activated stricter profile: none
Terminal implementation report point: not-applicable
```

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: JS and Python matrix named below
Affected tests: same matrix re-run from a fresh checkout of afa0670e
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
Topology rationale: candidate is unpublished; canonical must stay at public main; session-04 worktree must not be the acceptance working copy
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

Independence rule: you did not implement `85e9c04…` or `afa0670e…`. If this
session materially authored those commits, stop BLOCKED (independence
conflict). Session 03 accepted a **different** SHA (`36ffdb19…`); do not treat
that verdict as evidence for this candidate.

This prompt grants read-only acceptance evidence only. No product edits, no
commits, no push, no NUC, no publication, no closure.

## Mission

Independently accept or reject unpublished candidate
`afa0670e26d17b04570ad555ba4f922052507c6c` against:

1. This prompt’s control matrix and
   `/home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/04_correction_00.md`
   frozen correction (Cooperator «koriguj»).
2. Candidate
   `docs/adr/0077-ordinary-alias-edit-affordance-and-per-field-ai-suggestions.md`
   **as written on the candidate**, not the parent `36ffdb19…` text.

Parent / public `main` / canonical HEAD:

```text
36ffdb197da9294fb1fbb06931f8169061a25c9b
```

Claim to verify, not believe:
`/home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/04_report_00.md`

Do not implement. Do not replan. Do not reopen R1–R3′. Do not open R4 or VPS.

## Mandatory reading

1. This prompt.
2. `/home/agile/Projects/framenest/AGENTS.md`
3. `.ap/AP.md`, `.ap/AP_WORKER.md`
4. `docs/WORKER_EXECUTION_CONTRACT.md`
5. `04_correction_00.md` and `04_report_00.md` (claim).
6. Candidate ADR-0077. ADR-0062 / 0076 / 0023 bodies: inspect only, do not edit.

## Repository gate

```text
Repository checkout topology: standalone checkout with pinned submodule
Canonical root: /home/agile/Projects/framenest
Expected canonical branch: feat/x-meme-browser-companion
Expected canonical HEAD: 36ffdb197da9294fb1fbb06931f8169061a25c9b
Expected canonical tree: 301976223ce1a716fb476c70ef9d18feeff85d29
Expected canonical working tree: tracked-clean
Pinned submodule: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: 36ffdb197da9294fb1fbb06931f8169061a25c9b (re-verify ls-remote)
```

Before creating a fresh checkout, verify and record those facts. Any canonical
drift: classify RF-12 and stop; never tidy canonical.

Session-04 worktree
`/home/agile/Projects/framenest-worktrees/framenest-ai-suggestions-alias-edit-mvp-w4`
must still be at `afa0670e…`, tracked-clean. Do **not** use it as your working
copy. Do not edit or commit in it. Do not use w2 or w3 as the working copy.

Create **one** fresh detached checkout of the candidate:

```text
git -C /home/agile/Projects/framenest worktree add --detach \
  /home/agile/Projects/framenest-worktrees/framenest-ai-suggestions-alias-edit-mvp-w5 \
  afa0670e26d17b04570ad555ba4f922052507c6c
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
Your checkout HEAD must equal `afa0670e…`;
`git merge-base --is-ancestor 36ffdb19… HEAD` must succeed;
`git rev-list --count 36ffdb19…..HEAD` equals 2.

## Positive authority

- Read candidate, canonical, correction grant, claim, ADR-0077.
- Diff `afa0670e…` against `36ffdb19…`. Confirm the path set is **exactly**
  these 27 files (or fail extras/missing). The one named session-04 deviation
  is `companion_review_repository.py` (one constructor argument
  `suggested_filename=`; no second store). Treat that file as **expected**,
  not as a surprise extra:

  ```text
  PRODUCT.md
  SPEC.md
  docs/X_COMPANION.md
  docs/adr/0077-ordinary-alias-edit-affordance-and-per-field-ai-suggestions.md
  docs/adr/README.md
  src/framenest/adapters/api/application.py
  src/framenest/adapters/api/media_analysis_lifecycle_api.py
  src/framenest/adapters/api/media_catalog_api.py
  src/framenest/adapters/api/tailscale_ingress.py
  src/framenest/adapters/api/web/app.js
  src/framenest/adapters/api/web/index.html
  src/framenest/adapters/api/web/styles.css
  src/framenest/application/companion_review.py
  src/framenest/application/media_user_alias.py
  src/framenest/application/ports/media_user_alias_repository.py
  src/framenest/infrastructure/persistence/companion_review_repository.py
  src/framenest/infrastructure/persistence/media_user_alias_repository.py
  tests/automatic_analysis_lifecycle.test.js
  tests/companion_web_bridge.test.js
  tests/contract/test_local_web_application.py
  tests/contract/test_media_ai_suggestions_api.py
  tests/contract/test_media_catalog_api.py
  tests/contract/test_x_route_policy.py
  tests/metadata_alias_edit.test.js
  tests/tailscale_identity_frontend.test.js
  tests/unit/application/test_media_user_alias.py
  tests/upload_cockpit_async_ownership.test.js
  ```

- Confirm **no** `alembic_environment/versions/0034*`, no ADR-0062/0076/0023
  **body** edits, no `SECURITY.md`, no fifth `companion_mutation`.
- Confirm persist-join application files are unchanged vs parent
  `36ffdb19…` unless present in the 27-file set (they must not be).
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

1. Ordinary workspace Edit still uses `identityAllowsMetadataEdit`
   (`alias.write` ∨ `canonical.write`); Save split unchanged (alias PUT vs
   metadata PUT; canonical-write wins).
2. Authenticated `GET /api/media` and `GET /api/media/{id}` merge the caller's
   overlay for `(media_id, login_key)` into `display_title` / `description` /
   tags when a persisted non-empty overlay exists. Missing overlay fields keep
   canonical. No `login_key` → canonical. Alice ⊈ Bob.
3. `GET /api/media/{id}/metadata` stays canonical.
4. Load chrome: `identityAllowsAiSuggestionLoadChrome` = workspace ∧
   (`alias.write` ∨ `canonical.write`) ∧ not movie. Hosted shows Load /
   dropdown / strips. Alias-mode shows Load.
5. Analyze chrome: `identityAllowsAiAnalyze` = `analysis.run` ∧ not hosted ∧
   not movie ∧ not alias. Hosted hides Analyze.
6. Website Edit lists via `GET /api/media/{id}/ai-suggestions?limit=100`
   (ingress `metadata.alias.write`, not `companion_mutation`). Inbox detail
   stays `workflow.read`. Ordinary stays 403 on Apply. `app.js` contains no
   `/apply` substring.
7. Load does not call `applyResolvedAiSuggestionToMetadataWorkspace`.
   Dropdown change issues zero provider calls and hides strips until Load.
   Mapped suggested tags are buttons that append; unmapped are not buttons.
8. After Analyze, suggestion list dedupes on `analysis_run_id` (no in-session
   prepend of a missing-id duplicate). Custom dropdown is present (not a
   visible native `<select>` as the only control).
9. Content category and Acquisition source are hidden in this Edit dialog for
   all actors; admin Save still has the existing values to send.
10. Suggested filename is an informational note for ordinary and admin Load;
    not persisted into alias; no catalog rename.
11. Schema head remains `0033`. Exactly four `companion_mutation=True` rows.
12. ADR-0077 on the candidate records overlay display, ordinary list GET,
    hosted Load shown / Analyze hidden, filename note; index notes succession
    **without** ADR-0062/0076/0023 body edits.

**Negative (must not hold):**

- Ordinary Analyze / inbox Apply / `workflow.read` / `canonical.write`.
- Overlay leak across login_key or onto anonymous catalog.
- Overlay merge onto administrator Manage / metadata GET.
- Alembic `0034`.
- Fifth `companion_mutation`.
- Gallery 🧠 converted to per-field apply or shown to ordinary.

Gallery 🧠 admin bulk canonical save is **parked debt**, not a fail.

Session-04 named deviation (`companion_review_repository.py` +1 constructor
argument) is **not** a fail if it only passes `suggested_filename` and does
not add a second suggestion store.

## Execution route (RF-16)

Attempt declared isolated-worktree route first:

```text
./.ap/ap project check --root <fresh-checkout> --baseline 36ffdb197da9294fb1fbb06931f8169061a25c9b
./.ap/ap exec --root <fresh-checkout> --baseline 36ffdb197da9294fb1fbb06931f8169061a25c9b --operation runtime-info
```

Expected miss: `declared CPython executable does not exist`. Classify
environment limitation. Do not repair. Do not fail the candidate solely for it.

**Task-specific deviation** after that classified miss:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 36ffdb197da9294fb1fbb06931f8169061a25c9b
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 36ffdb197da9294fb1fbb06931f8169061a25c9b --operation runtime-info
```

Canonical `runtime-info` proves the envelope, not the candidate.

Provenance probe file **outside** git checkouts, e.g.
`/tmp/framenest-aliasacc-05-provenance.py`, printing `framenest.__file__` and
asserting it is under `<fresh-checkout>/src/framenest/`. Delete it after use.

Python matrix (deviation: canonical `--root` + `--rootdir` / `pythonpath`
fresh-checkout):

```text
<fresh-checkout>/tests/contract/test_local_web_application.py
<fresh-checkout>/tests/contract/test_x_route_policy.py
<fresh-checkout>/tests/contract/test_media_alias_api.py
<fresh-checkout>/tests/contract/test_media_catalog_api.py
<fresh-checkout>/tests/contract/test_media_ai_suggestions_api.py
<fresh-checkout>/tests/unit/application/test_media_user_alias.py
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
/home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/05_report_00.md
```

Begin EXACTLY:

```text
### Report for ORCHESTRATOR_CHAT
```

Professional English. Include: coordinate echo (whole, session `05`, exchange
`01`); PASS | PARTIAL | BLOCKED; `Phase-qualified result: acceptance-PASS`
only if every control-matrix row holds and minimum evidence is green,
else `not-applicable`; `Logical-whole closure: not-closed`; candidate SHA;
fresh checkout path; canonical still `36ffdb19…` tracked-clean; w4 unused as
working copy; path-set vs parent (exactly 27); control-matrix table with
evidence (`path:line` or test id); test commands and outcomes including RF-16
deviation and `framenest.__file__`; deviations/risks; one smallest next step
(Cooperator publication, then NUC); justification `final-acceptance`;
authority expiry; Resolved Execution Issues; Pre-Existing Failure
Classification; capability handshake (Plan Mode off; Max off or unknown).

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
Downloadable prompt filename: 05_acceptance_00.md
Destination path: /home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/05_acceptance_00.md
Archival: wait-for-report
```
