# WORKER TASK — Implementation (isolated worktree)

Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-companion-r4-automatic-analysis-settings-mvp
Worker session ordinal: 07
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: implementation
Native planning mode: not-used
Implementation authority: explicit
Reasoning recommendation: High
Task identity: FRAMENEST-COMPANION-R4-AUTO-ANALYSIS-IMPL-01
Task type: bounded implementation
Exact baseline: 1eee09c1afcfe41b2a411784f8c43c428e610b9b
Independence required: no
Evidence posture: non-independent
Authority renewal: this is a fresh session; planning authority from session 06 expired. This prompt is the sole current grant.
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
Evidence tier: E3
Evidence tier basis: cross-cutting mutation surface (runtime server setting persistence, fifth companion_mutation route, admin-only capability gating, extension settings UI, ADR-0079). INFOSEC-adjacent.
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
Existing focused tests: tests/contract/test_x_route_policy.py; tests/contract/test_tailscale_ingress_security.py; tests/contract/test_automatic_analysis_privacy_contract.py; tests/companion_review_extension.test.js
Affected tests: the suites above plus new allowlisted tests
New causal regression: admin-only Administration section in companion Settings; runtime setting JSON persistence; dynamic scheduler flag update; 5 companion_mutation routes; capability provider.operate required; ordinary 403; confirm on enable; default in git remains false
Broad or full suite: not-used
Runtime or testbed: isolated worktree + declared AP exec deviation below
Independent acceptance: required-separate-fresh-worker
```

This prompt grants implementation only inside the isolated worktree and
allowlist. It grants no push, publication, NUC, provider calls, browser
automation, schema migration, or closure. Authority expires at your terminal
report.

## Source Precedence

1. This prompt (includes the Cooperator-accepted freeze in §Accepted Decisions).
2. Frozen planner artifact
   `/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/06_report_00.md`.
3. Repository at the exact baseline `1eee09c1afcfe41b2a411784f8c43c428e610b9b`.
4. Accepted ADRs on that baseline. You add ADR-0079; you do not edit ADR
   bodies 0020, 0023, 0044, 0062, 0065, 0066, 0067, 0072, 0073, 0075, 0076, 0077, 0078.

If the repository contradicts this grant, STOP BLOCKED with exact evidence.
Do not self-grant extra paths.

## Mandatory Reading

1. This prompt (self-contained task authority).
2. The frozen planner artifact named above.
3. `/home/agile/Projects/framenest/AGENTS.md`
4. `/home/agile/Projects/framenest/.ap/AP.md`
5. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
6. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`

Then inspect at the baseline, as data:
ADR-0066, 0044, 0075, 0067; `extension/ui/sidebar.html`, `extension/ui/sidebar.js`,
`extension/ui/sidebar.css`, `extension/background/service_worker.js`;
`src/framenest/configuration.py`, `src/framenest/application/media_analysis_lifecycle.py`,
`src/framenest/adapters/api/tailscale_ingress.py`, `src/framenest/adapters/api/application.py`.

## Repository Gate

```text
Repository checkout topology: standalone checkout with pinned submodule
Canonical root: /home/agile/Projects/framenest
Expected canonical branch: feat/x-meme-browser-companion
Expected canonical HEAD: 1eee09c1afcfe41b2a411784f8c43c428e610b9b
Expected canonical tree: bd160c2a7f9a34c689a08b0e5facff3e426f127f
Expected canonical working tree: tracked-clean
Pinned submodule: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: 1eee09c1afcfe41b2a411784f8c43c428e610b9b
Schema head: Alembic 0033; no 0034_* migration
Working-copy topology: isolated-worktree
```

Create the worktree from the exact baseline. Do not mutate the canonical checkout:

```text
git -C /home/agile/Projects/framenest worktree add -b feat/companion-r4-automatic-analysis-settings-mvp \
  /home/agile/Projects/framenest-worktrees/framenest-companion-r4-automatic-analysis-settings-mvp-w2 \
  1eee09c1afcfe41b2a411784f8c43c428e610b9b
```

If that path is taken, choose another unused sibling under
`/home/agile/Projects/framenest-worktrees/` with the same kebab and `-w2`.
Worktree HEAD must equal the baseline before your first edit.

## Accepted Decisions (implement these)

Cooperator accepted the plan on 2026-08-27:

1. **Persistence:**
   - Atomic JSON sidecar at `{database_path.parent}/runtime-settings.json` (NUC: `/var/lib/framenest/runtime-settings.json`, dev: `/tmp/framenest-development/runtime-settings.json`, test override via env `FRAMENEST_RUNTIME_SETTINGS_PATH`).
   - Atomic write via tmp + `os.replace` (mode 0o600).
   - Precedence for `automatic_media_analysis_enabled`:
     1. Valid bool in `runtime-settings.json` if file exists.
     2. Otherwise `FrameNestSettings.automatic_media_analysis_enabled` (env `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED`, default `False` in git).
   - No Alembic `0034`, no SQLite table, no `sudo`, no EnvironmentFile rewrite, no git tracked file mutation. Default in git remains `False`.
   - Backup: not included in catalog backup.

2. **Dynamic Reading without Service Restart:**
   - `ScheduleAutomaticMediaAnalysis`: `self._enabled` can be a callable `Callable[[], bool]`; evaluated dynamically on `execute` and `notify_cataloged`.
   - `MediaAnalysisLifecycleApiDependencies.automatic_analysis_enabled` becomes `Callable[[], bool]`; `GET /api/ai/automatic-analysis-capability` reads current value per request.
   - Disabling stops queuing future events; in-flight runs complete. Enabling applies to future catalog events; no backfill.
   - YouTube remains excluded from automatic analysis (ADR-0066 §6).

3. **API and Ingress:**
   - Existing `GET /api/ai/automatic-analysis-capability`: requires `provider.operate`, reads dynamic setting.
   - New `PUT /api/admin/settings/automatic-analysis`:
     - Requires capability `provider.operate` (ordinary → 403 `CAPABILITY_DENIED`).
     - Flagged with `companion_mutation=True` (this becomes the **5th** flagged route in `tailscale_ingress.py`).
     - Audit action: `settings.automatic_analysis.put`.
     - Mandatory `X-FrameNest-Request: 1` header.
     - Body schema:
       - Enable: `{"automatic_media_analysis_enabled": true, "confirm_cloud_upload": true}` (missing confirm → 422).
       - Disable: `{"automatic_media_analysis_enabled": false}`.
     - Returns 200 `{"automatic_media_analysis_enabled": <bool>}`.

4. **Extension UI (`extension/ui/sidebar.html|js|css`):**
   - Settings dialog gains an **Administration** section below origin controls.
   - Visible ONLY when connected identity has `provider.operate` (from `GET /api/identity/me` / `service_worker.js` `capabilitiesFromBody`).
   - Hidden for ordinary users, unauthenticated, or disconnected state.
   - Checkbox: **Automatic media analysis**.
   - Checking ON: opens confirmation dialog inside settings sheet with copy:
     *"Turn on automatic media analysis? Newly captured administrator-owned X media will automatically send preview frames to the configured server-side AI provider and incur usage cost. YouTube and ordinary identities stay excluded."*
     Confirm → sends PUT with `confirm_cloud_upload: true`.
     Dismiss → reverts checkbox to OFF, no PUT.
   - Unchecking OFF: immediately sends PUT with `automatic_media_analysis_enabled: false`.
   - Error: shows localized message and reverts checkbox.
   - Communication via service worker messages (`fetchJson` + `X-FrameNest-Request: 1`).

5. **ADR & Docs:**
   - Add new `docs/adr/0079-administrator-automatic-analysis-runtime-setting.md`.
   - Update `docs/adr/README.md`.
   - Update `PRODUCT.md` (companion Settings has admin toggle; desktop Settings stays unshipped), `SPEC.md`, `SECURITY.md`, `README.md`, `docs/X_COMPANION.md`, `docs/BACKUP_AND_RECOVERY.md`, `deploy/systemd/framenest.env.example`.
   - Do NOT modify bodies of accepted ADRs 0020, 0023, 0044, 0062, 0065, 0066, 0067, 0072, 0073, 0075, 0076, 0077, 0078.

## Changed-Path Allowlist

Modify only:

1. `src/framenest/infrastructure/runtime_settings.py` (NEW)
2. `src/framenest/adapters/api/runtime_settings_api.py` (NEW)
3. `src/framenest/configuration.py`
4. `src/framenest/application/media_analysis_lifecycle.py`
5. `src/framenest/adapters/api/application.py`
6. `src/framenest/adapters/api/media_analysis_lifecycle_api.py`
7. `src/framenest/adapters/api/tailscale_ingress.py`
8. `extension/ui/sidebar.html`
9. `extension/ui/sidebar.js`
10. `extension/ui/sidebar.css`
11. `extension/shared/messages.js`
12. `extension/background/service_worker.js`
13. `tests/unit/test_runtime_settings_store.py` (NEW)
14. `tests/contract/test_automatic_analysis_settings_api.py` (NEW)
15. `tests/contract/test_x_route_policy.py`
16. `tests/contract/test_tailscale_ingress_security.py`
17. `tests/companion_review_extension.test.js`
18. `tests/contract/test_automatic_analysis_privacy_contract.py`
19. `docs/adr/0079-administrator-automatic-analysis-runtime-setting.md` (NEW)
20. `docs/adr/README.md`
21. `PRODUCT.md`
22. `SPEC.md`
23. `SECURITY.md`
24. `README.md`
25. `docs/X_COMPANION.md`
26. `docs/BACKUP_AND_RECOVERY.md`
27. `deploy/systemd/framenest.env.example`
28. Optional `tests/companion_settings_automatic_analysis.test.js` (NEW)

Everything else is read-only.

## Negative Authority

- No canonical checkout mutation.
- No push, force, rebase of shared history, `git add .` / `git add -A`.
- No Alembic files; schema head stays `0033`.
- No edits to ADR **bodies** 0020, 0023, 0044, 0062, 0065, 0066, 0067, 0072, 0073, 0075, 0076, 0077, 0078.
- No sixth `companion_mutation`. No persist-join redesign. No Cover Studio. No VPS.
- No ordinary `analysis.run` / `provider.operate` / `canonical.write`.
- No NUC, SSH, sudo, `gpgconf`, Funnel, VPS, browser automation, provider calls.
- No secrets; never print hosts, IPs, Tailscale values, fingerprints, or keys.
- No `.venv` reconstruction; no `poetry env use`; no ambient
  `.venv/bin/python` / `python` / `python3` / `poetry run`.
- No Max/enhanced mode. No sub-agents. No Explore-style delegation.

## Execution Route (RF-16) and Isolated-Worktree Deviation

Declared Cursor Worker Python route:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b
./.ap/ap exec --root <WORKTREE> --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b --operation runtime-info
./.ap/ap exec --root <WORKTREE> --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b --operation test-focus -- <tests> -q -p no:cacheprovider
```

**Known miss:** `ap exec --root <WORKTREE>` fails (`declared CPython
executable does not exist`) because `ap.project.conf` uses relative
`.venv/bin/python`. Do **not** reconstruct `.venv`.

**Task-specific deviation**:

```text
Declared route that could not be used: ap exec --root <WORKTREE>
Exact alternate:
  ./.ap/ap exec --root /home/agile/Projects/framenest \
    --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b \
    --operation test-focus -- <tests> -q -p no:cacheprovider \
    --rootdir=<WORKTREE> -o pythonpath=<WORKTREE>/src
Rationale: interpreter lives in the canonical Poetry .venv; candidate source
  must still be the worktree src.
Evidence class: worker-observed limitation; ledger entry remains
  untriaged and non-authorizing.
Bounded authority: this Worker session only, Python tests for this allowlist.
Stopping condition: if provenance framenest.__file__ is not under
  <WORKTREE>/src, STOP ENVIRONMENT LIMITATION. Do not repair .venv.
```

JS tests from the **worktree** root:

```text
node --test tests/companion_review_extension.test.js tests/companion_settings_automatic_analysis.test.js
```

Minimum Python (same deviation): `tests/unit/test_runtime_settings_store.py`, `tests/contract/test_automatic_analysis_settings_api.py`, `tests/contract/test_x_route_policy.py`, `tests/contract/test_tailscale_ingress_security.py`, `tests/contract/test_automatic_analysis_privacy_contract.py`.

## Git Authority

Inside **your worktree only**: stage explicit allowlisted paths; **1–3**
normal commits (Commit 1: server store + PUT + tests; Commit 2: companion UI + tests; Commit 3: docs + ADR-0079).
Commit message style: short `fix:` / `feat:` / `docs:` subject focused on why. No push.
Report each commit SHA. Canonical checkout must remain `1eee09c1…` tracked-clean
when you stop.

## Report Contract

Write exactly:

```text
/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/07_report_00.md
```

Begin EXACTLY:

```text
### Report for ORCHESTRATOR_CHAT
```

Professional English. Include:

1. Coordinate echo: logical whole `framenest-companion-r4-automatic-analysis-settings-mvp`,
   session `07`, exchange `01`.
2. Status PASS | PARTIAL | BLOCKED.
3. `Phase-qualified result: implementation-PASS` only if the freeze is
   implemented and minimum-evidence suites pass; otherwise `not-applicable`.
   `Logical-whole closure: not-closed`.
4. Worktree path; baseline; each commit SHA; canonical checkout still
   `1eee09c1…` tracked-clean.
5. Changed files with per-file intent.
6. Exact test commands and outcomes, including the RF-16 deviation and
   `framenest.__file__` provenance.
7. Verification: runtime settings store works; scheduler reacts dynamically; exactly 5 companion_mutation routes; capability provider.operate enforced; ordinary 403; extension Settings shows Administration for admin only; confirm on enable; ADR-0079 added; no schema 0034; git default remains false.
8. Deviations, risks; empty sections say `none`.
9. One smallest next step (fresh independent acceptance Worker 08, then publication + NUC).
10. Report justification: `new-mutation`.
11. Authority-expiry statement.
12. `Resolved Execution Issues / Near-Misses:` none | details.
13. `Pre-Existing Failure Classification:` none | complete classification.
14. Brief capability handshake: Plan Mode observed off; reasoning requested
    vs observed; Max observed off or unknown; qualitative context pressure.

## Human-Governance Routing

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
Trace discovery: /home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/
Trace project key: framenest
Trace logical-whole projection identity: framenest-companion-r4-automatic-analysis-settings-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR (prompt pre-staged); Worker writes only 07_report_00.md
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 07_implementation_00.md
Destination path: /home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/07_implementation_00.md
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
