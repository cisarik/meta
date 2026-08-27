# WORKER TASK — Independent Acceptance (fresh checkout after correction)

Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-companion-r4-automatic-analysis-settings-mvp
Worker session ordinal: 10
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Audit
Phase: Acceptance
Native planning mode: not-used
Reasoning recommendation: High
Task identity: FRAMENEST-COMPANION-R4-AUTO-ANALYSIS-ACC-02
Independence required: yes
Evidence posture: independent
Authority renewal: this is a fresh session. Session 09 correction authority expired at `09_report_00.md`. That report is a claim, not proof. You inherit no mutation authority from it.
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
Acceptance candidate: 472553cadcd3d4ca87a9792a2c306bd0afeea7c1
Acceptance owner map: Cooperator-accepted plan 06_report_00.md plus implementation grant 07_implementation_00.md plus correction grant 09_correction_00.md plus candidate ADR-0079
Acceptance allowlist: inspection of the 27 committed paths only (against baseline 1eee09c1); no product edits
Acceptance risk claims: runtime settings store persists setting across process restarts without schema 0034; dynamic scheduler check; exactly 5 companion_mutation routes; capability provider.operate required; ordinary 403; extension Settings shows Administration for admin only; confirm on enable; default in git remains false; ADR-0079 added; provenance tests checkout-independent
Acceptance control matrix: see § Control Matrix
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates only
```

```text
Evidence tier: E3
Evidence tier basis: cross-cutting mutation surface (runtime server setting persistence, fifth companion_mutation route, admin-only capability gating, extension settings UI, ADR-0079). INFOSEC-adjacent. Independent of implementing/correcting session.
Authorized implementation stages: none
Combined implementation envelope: prohibited
Implementation stage gates: not-applicable
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: canonical checkout remains 1eee09c1afcfe41b2a411784f8c43c428e610b9b; session-07/08/09 worktrees remain untouched
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
Topology rationale: candidate is unpublished; canonical must stay at public main; session-09 worktree must not be the acceptance working copy
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

Independence rule: you did not implement `472553c…`, `687b5af…`, `f04bc23…`, or `22847b7…`. If this
session materially authored those commits, stop BLOCKED (independence
conflict).

This prompt grants read-only acceptance evidence only. No product edits, no
commits, no push, no NUC, no publication, no closure.

## Mission

Independently accept or reject unpublished candidate
`472553cadcd3d4ca87a9792a2c306bd0afeea7c1` against:

1. This prompt’s freeze and control matrix.
2. `/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/06_report_00.md` & `09_report_00.md`.
3. Candidate `docs/adr/0079-administrator-automatic-analysis-runtime-setting.md`.

Parent / public `main` / canonical HEAD:

```text
1eee09c1afcfe41b2a411784f8c43c428e610b9b
```

## Mandatory Reading

1. This prompt.
2. `/home/agile/Projects/framenest/AGENTS.md`
3. `.ap/AP.md`, `.ap/AP_WORKER.md`
4. `docs/WORKER_EXECUTION_CONTRACT.md`
5. Candidate ADR-0079.

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

Create **one** fresh detached checkout of the candidate:

```text
git -C /home/agile/Projects/framenest worktree add --detach \
  /home/agile/Projects/framenest-worktrees/framenest-companion-r4-automatic-analysis-settings-mvp-w5 \
  472553cadcd3d4ca87a9792a2c306bd0afeea7c1
```

Worktree-local submodule only:

```text
git -C <fresh-checkout> submodule update --init .ap
```

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

Declared Python deviation:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b \
  --operation test-focus -- \
  <fresh-checkout>/tests/unit/test_runtime_settings_store.py \
  <fresh-checkout>/tests/contract/test_automatic_analysis_settings_api.py \
  <fresh-checkout>/tests/contract/test_x_route_policy.py \
  <fresh-checkout>/tests/contract/test_tailscale_ingress_security.py \
  <fresh-checkout>/tests/contract/test_automatic_analysis_privacy_contract.py \
  -q -p no:cacheprovider -s --rootdir=<fresh-checkout> -o pythonpath=<fresh-checkout>/src
```

Node from the **fresh checkout** root:

```text
node --test tests/companion_review_extension.test.js tests/companion_settings_automatic_analysis.test.js
```

## Report Contract

Write exactly:

```text
/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/10_report_00.md
```

Begin EXACTLY:

```text
### Report for ORCHESTRATOR_CHAT
```
