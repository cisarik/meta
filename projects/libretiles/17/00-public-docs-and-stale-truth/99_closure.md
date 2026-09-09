# Closure record — logical whole `public-docs-and-stale-truth` (Meta 17/00)

```text
Logical whole identity: public-docs-and-stale-truth
Logical-whole closure: closed-by-ORCHESTRATOR
Phase-qualified result: not-applicable
Result artifact or commit: f6ec9bf50e48c5b8ca97b840b019752e82b58cd6
Required preceding results: satisfied
Cooperator-owned decisions: satisfied
Residual-risk disposition: satisfied
Upgrade-ledger reconciliation: complete
Active mutation: none
Closure actor: ORCHESTRATOR
```

Closing commit: `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`  
AP pin at closure: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`  
Public `refs/heads/main` at closure: `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`  
Working tree at closure: `git status --porcelain=v1` EMPTY  
Predecessor whole `infosec-hardening-and-vps-readiness` (16/00) closed at `33ffa150fa520118e67a6670422fe7fae1c98741`  
Closed on 2026-09-09 by the Agent Orchestrator.

Artifact class: **closure record — authority for the fact of closure only.** It grants no authority to change the repository, deploy a host, or start a successor whole. Successor work takes authority from its own Orchestrator prompts.

This whole did not upgrade AP. The pin is unchanged. There is no Libre Tiles AP-upgrade ledger mutation to reconcile.

---

## 1. What this whole delivered

Public documentation now matches the live standalone-VPS product, is interviewer-legible, and is frozen against regression by ten offline static guards.

### Slice 1 — Binding Safety & Core Deployment Truth Alignment (`b45149f`)

- Replaced all six `runserver 0.0.0.0:8000` instructions with `127.0.0.1:8000` (README ×2, AGENTS, CONTRIBUTING, `scripts/start-backend.sh`, `scripts/libretiles.sh`).
- Removed four stale Vercel venue claims (AGENTS, `settings.py:295` CORS comment, PRD line 25, PRD Phase 7).
- Fixed two bare `DEBUG=true` prose sites to `DJANGO_DEBUG=true` (README throttle row, `.env.example:24`).
- Added `backend/tests/test_documentation_deployment_claims.py` (8 offline assertions, stdlib only).
- Cooperator decision A: include both dev scripts via explicit exception to documentation-only invariant; LAN tablet/phone consequence accepted.

### Slice 2 — README Streamlining & Architectural Clarity (`4a718b5`)

- README 431 → 198 lines, with `### Local development` / `### Production (VPS)` separation; deep-dive cut-with-pointer.
- CONTRIBUTING: Python 3.12 / Node 24 prerequisites, secret-key guidance, scoped mypy, `npm run typecheck`, architecture prose, catalog principles corrected.
- PRD: 29 table replacements + whole-paragraph changes — multiplayer now LIVE (not "v2 planned"), Tier 2 marked planned, reviewed Admin ordering documented, header date updated.

### Slice 3 — Documentation Quality Audit & Architecture Fixes (`f6ec9bf`)

- Fresh independent audit found five stale claims, all in `docs/architecture.md`: fallback cap 5→3, judge 5 attempts/50s→3/30s, "fixed canonical order"→reviewed-Admin ordering (×2), Tier 2 marked planned.
- All five fixed; directed grep returns zero; 10/10 guards green.

## 2. Landed commit lineage

```text
b45149f  fix(docs): eliminate wildcard Django binds and stale Vercel claims
4a718b5  docs: streamline README and align standalone product documentation
f6ec9bf  docs(architecture): align fallback, judge, and catalog ordering to live behavior
```

## 3. Closure conditions

| Condition | Status | Evidence |
|---|---|---|
| Zero product code mutation (docs + static tests only) | **MET** | all three diffs touch only docs + one new test file |
| `WordAuthority.accepts_tokens` unchanged | **MET** | no gamecore/file logic touched |
| No network exposure (no `0.0.0.0` for Django) | **MET** | directed grep zero; T1/T2/T3 guards green |
| Fast pytest (doc guards < 0.5s) | **MET** | 10 guards 0.07s isolated |
| No secret leakage | **MET** | no `.env`/`.env.local` read; credential facts reported as present+name only |
| Autonomous report delivery (D-17) | **MET** | sessions 01–06 wrote terminal reports directly to Meta |
| Fast default pytest stays SQLite | **MET** | no DB settings touched |
| AP pin unchanged | **MET** | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |

## 4. Residual-risk disposition at closure

| Finding / residual | Severity | Decision | Approver | Rationale |
|---|---|---|---|---|
| `test_word_authority_parity.py` payload-parity red (extra `inspection` block vs pinned baseline) | medium (suite-red, not a security defect) | accepted-residual, carry forward | Orchestrator + Cooperator | Pre-existed at baseline `33ffa15`; oracle must not be edited to follow implementation (AGENTS.md); owned by `codebase-hygiene-and-residual-reconciliation` |
| `judge/route.ts:10-12` docstring still lists Tier 2 as a pipeline tier | info | accepted-residual | Orchestrator | frontend source outside docs allowlist (A1) |
| `frontend/public/hu.png`, `drevo.jpeg` present; `hu` not a shipped locale | info | accepted-residual | Orchestrator | asset hygiene, future slice |
| CONTRIBUTING Node "20.19+/22.12+" support matrix | info | hypothesis-unverified | Orchestrator | no `engines` field; needs network verification in a network-capable whole |
| Whole 16 residuals (IHR-S1-F01, IHR-S2-R01, HSTS W021, billing orphan, throttle scopes, JWT storage, CSP) | info | carry unchanged | prior whole | not this whole's slices |

## 5. Logical-whole closure declaration

Logical whole `public-docs-and-stale-truth` (Meta 17/00) is **CLOSED** at `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`.

The three tactical documentation slices are accepted on public `main`. The `codebase-hygiene-and-residual-reconciliation` whole (parity oracle re-pin), the `github-actions-ci-and-sbom` whole, the `dockerized-vps-deployment` whole (Cooperator-requested, see forward handoff), and fence/host deployment remain separate future authority.