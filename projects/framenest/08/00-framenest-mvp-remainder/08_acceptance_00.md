# WORKER TASK — Independent Acceptance (fresh checkout)

Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-companion-r4-automatic-analysis-settings-mvp
Worker session ordinal: 08
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Audit
Phase: Acceptance
Native planning mode: not-used
Reasoning recommendation: High
Task identity: FRAMENEST-COMPANION-R4-AUTO-ANALYSIS-ACC-01
Independence required: yes
Evidence posture: independent
Authority renewal: this is a fresh session. Session 07 implementation authority expired at `07_report_00.md`. That report is a claim, not proof. You inherit no mutation authority from it.
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
Acceptance candidate: 687b5afd933d2ffce418eb6e57f03efb3ed141bf
Acceptance owner map: Cooperator-accepted plan 06_report_00.md plus implementation grant 07_implementation_00.md plus candidate ADR-0079
Acceptance allowlist: inspection of the 27 committed paths only; no product edits
Acceptance risk claims: runtime settings store persists setting across process restarts without schema 0034; dynamic scheduler check; exactly 5 companion_mutation routes; capability provider.operate required; ordinary 403; extension Settings shows Administration for admin only; confirm on enable; default in git remains false; ADR-0079 added
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
Evidence tier basis: cross-cutting mutation surface (runtime server setting persistence, fifth companion_mutation route, admin-only capability gating, extension settings UI, ADR-0079). INFOSEC-adjacent. Independent of implementing session.
Authorized implementation stages: none
Combined implementation envelope: prohibited
Implementation stage gates: not-applicable
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: canonical checkout remains 1eee09c1afcfe41b2a411784f8c43c428e610b9b; session-07 worktree remains untouched
Activated stricter profile: none
Terminal implementation report point: not-applicable
```

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: tests/unit/test_runtime_settings_store.py; tests/contract/test_automatic_analysis_settings_api.py; tests/contract/test_x_route_policy.py; tests/contract/test_tailscale_ingress_security.py; tests/contract/test_automatic_analysis_privacy_contract.py; tests/companion_settings_automatic_analysis.test.js
Affected tests: the suites above
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
Topology rationale: candidate is unpublished; canonical must stay at public main; session-07 worktree must not be the acceptance working copy
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

Independence rule: you did not implement `687b5af…`, `f04bc23…`, or `22847b7…`. If this
session materially authored those commits, stop BLOCKED (independence
conflict).

This prompt grants read-only acceptance evidence only. No product edits, no
commits, no push, no NUC, no publication, no closure.

## Mission

Independently accept or reject unpublished candidate
`687b5afd933d2ffce418eb6e57f03efb3ed141bf` against:

1. This prompt’s freeze and control matrix.
2. `/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/06_report_00.md`.
3. Candidate `docs/adr/0079-administrator-automatic-analysis-runtime-setting.md`.

Parent / public `main` / canonical HEAD:

```text
1eee09c1afcfe41b2a411784f8c43c428e610b9b
```

Claim to verify, not believe:
`/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/07_report_00.md`

Do not implement. Do not replan. Do not open Cover Studio or VPS.

## Mandatory Reading

1. This prompt.
2. `/home/agile/Projects/framenest/AGENTS.md`
3. `.ap/AP.md`, `.ap/AP_WORKER.md`
4. `docs/WORKER_EXECUTION_CONTRACT.md`
5. The claim named above.
6. Candidate ADR-0079. ADR-0020 / 0023 / 0044 / 0062 / 0065 / 0066 / 0067 / 0072 / 0073 / 0075 / 0076 / 0077 / 0078 bodies: inspect only, do not edit.

## Repository Gate

```text
Repository checkout topology: standalone checkout with pinned submodule
Canonical root: /home/agile/Projects/framenest
Expected canonical branch: feat/x-meme-browser-companion
Expected canonical HEAD: 1eee09c1afcfe41b2a411784f8c43c428e610b9b
Expected canonical tree: bd160c2a7f9a34c689a08b0e5facff3e426f127f
Expected canonical working tree: tracked-clean
Pinned submodule: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: 1eee09c1afcfe41b2a411784f8c43c428e610b9b (re-verify ls-remote)
```

Before creating a fresh checkout, verify and record those facts. Any canonical
drift: classify RF-12 and stop; never tidy canonical.

Session-07 worktree
`/home/agile/Projects/framenest-worktrees/framenest-companion-r4-automatic-analysis-settings-mvp-w2`
must still be at `687b5af…`, tracked-clean. Do **not** use it as your working
copy. Do not edit or commit in it.

Create **one** fresh detached checkout of the candidate:

```text
git -C /home/agile/Projects/framenest worktree add --detach \
  /home/agile/Projects/framenest-worktrees/framenest-companion-r4-automatic-analysis-settings-mvp-w3 \
  687b5afd933d2ffce418eb6e57f03efb3ed141bf
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
Your checkout HEAD must equal `687b5af…`;
`git merge-base --is-ancestor 1eee09c… HEAD` must succeed;
`git rev-list --count 1eee09c…..HEAD` equals 3.

## Positive Authority

- Read candidate, canonical, claim, ADR-0079.
- Diff `687b5af…` against parent `1eee09c…`. Confirm the path set is exactly these
  27 files (or fail extras/missing):

  ```text
  PRODUCT.md
  README.md
  SECURITY.md
  SPEC.md
  deploy/systemd/framenest.env.example
  docs/BACKUP_AND_RECOVERY.md
  docs/X_COMPANION.md
  docs/adr/0079-administrator-automatic-analysis-runtime-setting.md
  docs/adr/README.md
  extension/background/service_worker.js
  extension/shared/messages.js
  extension/ui/sidebar.css
  extension/ui/sidebar.html
  extension/ui/sidebar.js
  src/framenest/adapters/api/application.py
  src/framenest/adapters/api/media_analysis_lifecycle_api.py
  src/framenest/adapters/api/runtime_settings_api.py
  src/framenest/adapters/api/tailscale_ingress.py
  src/framenest/application/media_analysis_lifecycle.py
  src/framenest/configuration.py
  src/framenest/infrastructure/runtime_settings.py
  tests/companion_settings_automatic_analysis.test.js
  tests/contract/test_automatic_analysis_privacy_contract.py
  tests/contract/test_automatic_analysis_settings_api.py
  tests/contract/test_tailscale_ingress_security.py
  tests/contract/test_x_route_policy.py
  tests/unit/test_runtime_settings_store.py
  ```

- Confirm **no** `alembic_environment/versions/0034*`, no ADR-0020/0023/0044/0062/0065/0066/0067/0072/0073/0075/0076/0077/0078
  **body** edits, no persist-join redesign, no sixth `companion_mutation`.
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

1. Runtime settings store persists atomic JSON sidecar (`runtime-settings.json`, mode `0o600`); valid bool in sidecar precedes `FrameNestSettings.automatic_media_analysis_enabled`.
2. Scheduler reads `store.is_enabled` dynamically via callable; changes take effect immediately without backend restart.
3. `PUT /api/admin/settings/automatic-analysis` requires `provider.operate`; ordinary → 403 `CAPABILITY_DENIED`.
4. Enable without `confirm_cloud_upload: true` returns 422; disable succeeds without extra confirm.
5. Exactly five `companion_mutation=True` routes in `tailscale_ingress.py` (opened, apply, requests POST, retry POST, settings PUT).
6. Companion extension Settings: Administration section visible only to connected identities with `provider.operate`; hidden for ordinary/disconnected.
7. Confirm dialog shown before enabling automatic analysis in companion Settings.
8. Git default in `configuration.py` remains `automatic_media_analysis_enabled: bool = Field(default=False)`.
9. Schema head remains Alembic `0033`; no `0034_*` migration.
10. ADR-0079 created and indexed; ADR bodies 0020/0023/0044/0062/0065/0066/0067/0072/0073/0075/0076/0077/0078 untouched.

**Negative (must not hold):**

- Ordinary access to Administration section / settings PUT.
- Sixth `companion_mutation`.
- Alembic `0034`.
- Tracked git file mutation for runtime settings.

## Execution Route (RF-16)

Attempt declared isolated-worktree route first:

```text
./.ap/ap project check --root <fresh-checkout> --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b
./.ap/ap exec --root <fresh-checkout> --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b --operation runtime-info
```

Expected miss: `declared CPython executable does not exist`. Classify
environment limitation. Do not repair. Do not fail the candidate solely for it.

**Task-specific deviation** after that classified miss:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b --operation runtime-info
```

Provenance probe file **outside** git checkouts, e.g.
`/tmp/framenest-r4acc-08-provenance.py`, printing `framenest.__file__` and
asserting it is under `<fresh-checkout>/src/framenest/`.

Python matrix (deviation: canonical `--root` + `--rootdir` / `pythonpath` fresh-checkout):

```text
<fresh-checkout>/tests/unit/test_runtime_settings_store.py
<fresh-checkout>/tests/contract/test_automatic_analysis_settings_api.py
<fresh-checkout>/tests/contract/test_x_route_policy.py
<fresh-checkout>/tests/contract/test_tailscale_ingress_security.py
<fresh-checkout>/tests/contract/test_automatic_analysis_privacy_contract.py
```

Stopping condition: if `framenest.__file__` is not under the fresh checkout
`src/`, ENVIRONMENT LIMITATION for Python provenance; still run Node; do not
fail solely for the known launch-path miss; **do** fail on candidate defects.

Node from the **fresh checkout** root:

```text
node --test tests/companion_review_extension.test.js tests/companion_settings_automatic_analysis.test.js
```

## Report Contract

Write exactly:

```text
/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/08_report_00.md
```

Begin EXACTLY:

```text
### Report for ORCHESTRATOR_CHAT
```

Professional English. Include: coordinate echo (whole, session `08`, exchange
`01`); PASS | PARTIAL | BLOCKED; `Phase-qualified result: acceptance-PASS`
only if every control-matrix row holds and minimum evidence is green,
else `not-applicable`; `Logical-whole closure: not-closed`; candidate SHA;
fresh checkout path; canonical still `1eee09c…` tracked-clean; w2 untouched;
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
Trace logical-whole projection identity: framenest-companion-r4-automatic-analysis-settings-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 08_acceptance_00.md
Destination path: /home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/08_acceptance_00.md
Archival: wait-for-report
```
