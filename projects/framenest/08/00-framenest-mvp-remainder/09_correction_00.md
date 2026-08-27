# WORKER TASK — Bounded Correction (checkout-independent provenance test)

Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-companion-r4-automatic-analysis-settings-mvp
Worker session ordinal: 09
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: Implementation
Native planning mode: not-used
Implementation authority: explicit
Reasoning recommendation: High
Task identity: FRAMENEST-COMPANION-R4-AUTO-ANALYSIS-CORR-01
Task type: bounded correction
Exact baseline: 687b5afd933d2ffce418eb6e57f03efb3ed141bf
Independence required: no
Evidence posture: non-independent
Authority renewal: sessions 07 and 08 expired at their reports. This prompt is the sole current grant.
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
Acceptance candidate (parent): 687b5afd933d2ffce418eb6e57f03efb3ed141bf
Acceptance owner map: Session 08 PARTIAL finding (test_candidate_source_provenance had hardcoded w2 directory name)
Acceptance allowlist: tests/unit/test_runtime_settings_store.py only
Acceptance risk claims: test_candidate_source_provenance passes across any valid worktree checkout without hardcoded directory names
Acceptance control matrix: all 112 Python tests + 32 JS tests green
Acceptance independence: not-required for this corrector; fresh independent acceptance is Worker 10
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates only
```

```text
Evidence tier: E3
Evidence tier basis: test harness provenance assertion correction; independent of implementing session
Authorized implementation stages: isolated-worktree create → implement allowlisted files → focused tests → 1 local commit → terminal report
Combined implementation envelope: allowed
Implementation stage gates: repository gate before mutation; tests green before commit; canonical checkout remains untouched
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: isolated worktree + unpushed commits; discard worktree if BLOCKED before commit
Activated stricter profile: none
Terminal implementation report point: after local commit, before any push
```

```text
Development envelope activation: activated
Development envelope identity: FrameNest isolated correction worktree (this grant)
Declared reversible class: reversible local mutation (worktree files + local commits)
Working-copy topology: isolated-worktree
Topology rationale: keep canonical public main clean; exact-source candidate parented on 687b5af
Irreversible exclusions: secrets, destruction, accounts, public exposure, unrelated owner data, publication, push, NUC, closure, schema migration, .venv reconstruction
```

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

Create the worktree from baseline `687b5afd933d2ffce418eb6e57f03efb3ed141bf`:

```text
git -C /home/agile/Projects/framenest worktree add -b feat/companion-r4-automatic-analysis-settings-corr \
  /home/agile/Projects/framenest-worktrees/framenest-companion-r4-automatic-analysis-settings-mvp-w4 \
  687b5afd933d2ffce418eb6e57f03efb3ed141bf
```

## Frozen Correction

In `tests/unit/test_runtime_settings_store.py`:
- Update `test_candidate_source_provenance` so that it asserts `framenest.__file__` resolves to the local checkout's `src/framenest/__init__.py` using relative path comparison / `Path(__file__).resolve().parents[...] / "src" / "framenest" / "__init__.py"`, rather than asserting the hardcoded string `"framenest-companion-r4-automatic-analysis-settings-mvp-w2"`.
- Run the full Python test matrix to verify 112 passed, 0 failed.

## Changed-Path Allowlist

Modify only:
1. `tests/unit/test_runtime_settings_store.py`

Everything else is read-only.

## Report Contract

Write exactly: `/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/09_report_00.md`
Begins: `### Report for ORCHESTRATOR_CHAT`
Include commit SHA, test results, and capability handshake.
