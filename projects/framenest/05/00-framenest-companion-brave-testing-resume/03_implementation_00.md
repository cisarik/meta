# FrameNest — Implementation Worker prompt (companion history R1–R3′)

Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh implementation Worker, isolated worktree, exact-source evidence
Phase: implementation
Reasoning recommendation: High (trust-boundary edit: opened route widened to ordinary owners; cross-layer extension/API/repository/docs coherence)
Task identity: FRAMENEST-COMPANIE-HISTIMPL-01
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/05/00-framenest-companion-brave-testing-resume/
Trace project key: framenest
Trace logical-whole projection identity: framenest-companion-brave-testing-resume
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

## Mission

Implement the archived decision-ready plan **exactly as specified** in:

```text
/home/agile/meta/projects/framenest/05/00-framenest-companion-brave-testing-resume/02_report_01.md
```

That document is your normative specification (R1 click-path fix; R2 admin
analyzed-only inbox with per-actor unopened accent/badge; R3′ ordinary
requester-private own-history with analyzed-row accent/badge; same-fourth-
route opened with ownership gate; hosted-mode hides Analyze by AI + Load AI
suggestion; ADR-0076 + docs + test matrix). Where this prompt and the plan
conflict, the plan wins; where the repository contradicts both, stop and
report.

Exact baseline (= public `main`):

```text
91410fe063d9907304cff4550f61d403880a2eeb
```

## Mandatory reading

1. The archived plan above (normative).
2. `AGENTS.md`; `.ap/AP.md`, `.ap/AP_WORKER.md` (pin `9c5cc44…`);
   `docs/WORKER_EXECUTION_CONTRACT.md`.
3. `docs/adr/0073-*.md`, `docs/adr/0067-*` (bodies read-only — you supersede,
   never edit), `SECURITY.md` companion paragraphs.

## Working copy and Git authority

- Create an isolated worktree from exact baseline `91410fe…`; canonical
  checkout stays untouched.
- Git authority: local operations inside YOUR worktree only — exactly one
  normal commit at completion (no `git add .`/`-A`; stage explicit paths),
  report the commit SHA. NO push, NO publication, NO force, NO rebase of
  anything shared.

## Edit authority — exact allowlist

1. `extension/ui/sidebar.js`
2. `extension/background/service_worker.js` (only if badge/routing needs it)
3. `src/framenest/adapters/api/companion_review_api.py`
4. `src/framenest/adapters/api/tailscale_ingress.py`
5. `src/framenest/application/companion_review.py`
6. `src/framenest/infrastructure/persistence/companion_review_repository.py`
7. `src/framenest/adapters/api/web/app.js` (hosted-hide of Analyze by AI +
   Load AI suggestion only)
8. `docs/X_COMPANION.md` (history section rewrite incl. the stale sentence)
9. NEW file `docs/adr/0076-<kebab-slug>.md` + index row in `docs/adr/README.md`
10. `SPEC.md`, `PRODUCT.md`, `README.md` — ONLY present-tense sentences that
    contradict R1–R3′ (minimal, surgical)
11. Tests: `tests/companion_review_extension.test.js`,
    `tests/companion_web_bridge.test.js`,
    `tests/tailscale_identity_frontend.test.js`,
    `tests/contract/test_companion_review_api.py`,
    `tests/contract/test_adr_0073.py` (ONLY assertions encoding superseded
    mixed-inbox/pending-overlay semantics; never weaken retention tests),
    `tests/contract/test_x_route_policy.py`,
    `tests/contract/test_tailscale_ingress_security.py`,
    `tests/unit/infrastructure/persistence/test_companion_review_repository.py`

Everything else is read-only. In particular FORBIDDEN:
`docs/adr/0073-*.md` and ADR-0067 bodies, `SECURITY.md`, any file under
`alembic_environment/versions/` (**NO 0034** — head must remain `0033`),
publication/upload APIs, `deploy/ubuntu/*`, `.venv`, dependency manifests.

## Hard boundaries

- Schema head stays `0033`; no migration files added or edited.
- Exactly four `companion_mutation` routes; allowlist + header rules and
  empty-allowlist fail-closed behavior unchanged for them.
- Ordinary gains exactly: `GET /api/companion/own-history` (GET) and
  opened-POST on OWN items only (uniform 404 otherwise). Inbox list/detail/
  apply stay admin-only 403.
- Apply never publishes; administrator PUT remains sole writer incl.
  unpublish. Movie exclusion retained everywhere.
- No NUC/SSH/sudo, no providers, no browser automation, no network beyond
  loopback spawned by test suites.
- If an allowlisted change proves impossible without crossing a boundary,
  stop and request direction through your report (never self-grant).

## Execution and validation

All Python evidence ONLY through the canonical route with exact baseline;
Node suites via Node’s built-in runner from your worktree root
(`docs/WORKER_EXECUTION_CONTRACT.md`). Ambient-route encodings signature →
classify, rerun once through `ap exec`, never repair environments.

```text
./.ap/ap project check --baseline 91410fe063d9907304cff4550f61d403880a2eeb
./.ap/ap exec --root <your-worktree> --baseline 91410fe063d9907304cff4550f61d403880a2eeb --operation test-focus -- <selection> -q -p no:cacheprovider
node --test tests/x_companion_extension.test.js tests/companion_review_extension.test.js tests/companion_web_bridge.test.js tests/tailscale_identity_frontend.test.js
```

Minimum evidence (all green): the full plan test matrix (R1, R2, R3′
listing, R3′ opened+isolation Alice/Bob/admin triple, ingress, no-0034
head checks) PLUS retained suites (`test_adr_0073.py` retained parts,
`test_analysis_proposal.py`, `test_automatic_analysis_privacy_contract.py`,
`tests/integration/persistence/test_analysis_proposal_migration.py`,
`tests/integration/test_persistence_migrations.py`). First failing suite:
preserve output verbatim, classify, stop that batch.

## Output

Write exactly one file:

```text
/home/agile/meta/projects/framenest/05/00-framenest-companion-brave-testing-resume/03_report_01.md
```

Professional English, beginning exactly:

### Report for ORCHESTRATOR_CHAT

Include: coordinate echo; status PASS/PARTIAL/BLOCKED + phase-qualified
result `implementation-PASS` only when everything allowlisted is complete
and all minimum-evidence suites pass; worktree path and exact commit SHA;
changed-file list with per-file intent; test invocation lines with outcomes;
per-rule confirmation R1/R2/R3′ mapped to owning tests; security-invariant
confirmation list; sanitization compliance; Resolved Execution Issues /
Near-Misses and Pre-Existing Failure Classification (full record if any);
deviations/risks; one smallest next step; Report justification:
new-mutation; authority expiry statement. Abbreviated capability handshake
(client/surface, model requested-vs-observed class, Plan Mode observed off,
permission mode, qualitative context pressure).

## Stopping rule

Stop after the terminal report, or earlier BLOCKED on boundary conflict /
failed gate / unclassifiable failure.

## Transition owner

ORCHESTRATOR verifies claims against repository evidence, then sequences
Cooperator publication grant, routine NUC release refresh, and rendered
re-test. You have no follow-on authority.
