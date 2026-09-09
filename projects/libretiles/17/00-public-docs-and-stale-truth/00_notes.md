# Libre Tiles — Notes for logical whole `public-docs-and-stale-truth` (Meta 17/00)

Artifact class: **notes ledger — evidence and observation history only; grants NO authority.**

This directory and file were initialized on 2026-09-09 by Worker session 12 of closed whole 16 (`infosec-hardening-and-vps-readiness`) following the independent milestone audit at commit `33ffa150fa520118e67a6670422fe7fae1c98741`.

- Selected logical whole identity: `public-docs-and-stale-truth`
- Baseline commit: `33ffa150fa520118e67a6670422fe7fae1c98741`
- Pinned AP commit: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Predecessor whole: `16/00-infosec-hardening-and-vps-readiness` CLOSED at `33ffa150fa520118e67a6670422fe7fae1c98741` (record: `16/00-infosec-hardening-and-vps-readiness/99_closure.md`).

The successor Agent Orchestrator appends from here. No tactical slice plan is authored in this notes ledger. Task authority comes only from the current authoritative Orchestrator prompt.

---

## Slice 1 — Binding Safety & Core Deployment Truth Alignment — ACCEPTED (2026-09-09)

Independently verified by the Orchestrator against the live tree (not merely read from the Worker report):

- **Commit** `b45149fea0557ca0d87a9a7713cde80bd0fcc03b` on `origin/main`; local HEAD identical; `git status --porcelain=v1` empty. Readback holds.
- **Diff scope** = exactly the 9 allowlisted paths (8 edited + 1 new test). No product code, no gamecore, no migrations. Script shell modes preserved (`100755`).
- **New test module** `backend/tests/test_documentation_deployment_claims.py`: 8/8 pass in isolated stdlib-only run (`-c /dev/null --noconftest`, `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`) in 0.07s; `ruff check` clean; syntax `ast.parse` clean.
- **Directed grep** `0.0.0.0:8000` across the 5 documented surfaces returns ZERO. `bash -n` clean on both scripts (executed by Worker; reported).
- **makemigrations --check --dry-run**: "No changes detected".
- All 12 planned D4 replacements applied verbatim; 3 near-misses reconciled by the Worker correctly (REPL2 corruption, REPL5 filename typo, D3/D4 .env.example one-line unsatisfiable block) — none changed product code.

### Independent finding — pre-existing red test (NOT caused by this slice; carry-over)

`tests/test_word_authority_parity.py::PersistedPayloadParityTests::test_human_persisted_move_payload_matches_the_pinned_baseline` FAILS on the live tree, and I verified it independently:

- `move.words_formed` now carries an `inspection` payload (added in commit `e2c2549`, whole 15 admin-console) that the pinned baseline expectation in the parity oracle does not include.
- Confirmed at baseline `33ffa15`: `backend/game/services.py` already contains `inspection` (3 occurrences), so this failure pre-exists Whole 17. The diff proves Slice 1 touched no backend code that the test exercises.
- Per AGENTS.md the oracle must not be edited to follow the implementation — this needs a deliberate re-pin or a revert of the enrichment.

**Disposition**: out of Whole 17 scope (A1 forbids product-code mutation; this whole mutates docs + static tests only). Routed to the forward-horizon whole `codebase-hygiene-and-residual-reconciliation` as a new known defect: the parity oracle freeze is out of sync with the live `words_formed` schema. Until resolved, the default full suite is red, not green.

### Slice 1 outcome

Status: PASS (implementation-PASS). Cooperator decision A (include both dev scripts) honoured via explicit exception. LAN tablet/phone consequence accepted. Next: Slice 2 — README streamlining.

---

## Slice 2 — README Streamlining & Architectural Clarity — ACCEPTED (2026-09-09)

Independently verified by the Orchestrator against the live tree:

- **Commit** `4a718b5bcf68daed4c0b7ab43ab3261bf026fb10` on `origin/main`; local HEAD identical; porcelain empty; readback holds.
- **Diff scope** = exactly the 3 allowlisted paths (README.md, CONTRIBUTING.md, libretiles_PRD.md). No product code, no test-module mutation.
- **README.md** = 198 lines (target 170–210, no filler). Single Quick Start with `### Local development` / `### Production (VPS)` separation; deep-dive cut-with-pointer.
- **Content guards verified by Orchestrator**: 2× `manage.py runserver 127.0.0.1:8000` in README; 1× `DJANGO_DEBUG=true` boot anchor; ZERO `0.0.0.0:8000` and ZERO Vercel venue claims across the 3 files; `self-hosted VPS` present (README 1, CONTRIBUTING 1, PRD 3); `Vercel AI SDK` ×2 and Phase 7 line intact in PRD.
- **Focused documentation tests**: 10/10 passed in 0.08s (8 deployment + 2 dictionary), independently re-run by Orchestrator.
- **Standing gates** (worker-reported): mypy clean (119 files), ruff clean, makemigrations "No changes detected"; pytest `-m "not slow and not internet and not postgres"` = 1227 passed + 1 pre-existing parity failure (same as Slice 1, unchanged, out of scope), 27 deselected, 702s; frontend typecheck + lint exit 0.
- **Product-truth alignment**: multiplayer now LIVE (not "v2 planned"); Python 3.12 / Node 24 prerequisites; Tier 2 as unplanned; Playwright/CI as planned; reviewed Admin activation ordering; PRD header date → September 9 2026.

### Slice 2 outcome

Status: PASS (implementation-PASS). Zero static-test edit needed (plan D6 proved correct — no test was bent to follow documentation). Pre-existing parity failure confirmed again as baseline-red after this slice (still not caused by Whole 17). Next: Slice 3 — documentation quality audit & logical-whole closure.
