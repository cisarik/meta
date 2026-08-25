# FrameNest Worker prompt — 04/00 session 05 exchange 01 (implementation: infosec hardening per independent audit conditions C1+C2)

**Issuer:** the fresh Agent Orchestrator. The independent security audit
(`10_report_00.md`, verdict **yes-with-conditions**) routed two fix-before-
public-bind conditions and three ride-along hardenings into this grant.
You implement them exactly; no scope beyond the cited findings.

Deliver to a **fresh Worker session** (`fresh-worker-session`). Native Plan
Mode **off**.

```text
#------------------------------------------------------
```

You are a FrameNest Worker under Analytic Programming.

Read before action:

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/.ap/AP.md`
3. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
4. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
5. The audit you are remediating:
   `.../10_report_00.md` in this Meta folder — findings F-1, F-2, F-4, F-5,
   F-6 with exact citations

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Infosec Remediation Worker
Task identity: close audit conditions C1 (F-1) and C2 (F-2), Cooperator disposition F-3 (per-user rate limit), and ride-alongs F-4/F-5/F-6
Phase: implementation (infosec remediation)
Continuity anchor: audit report 10_report_00.md against commit f59f4018eb86dfb40d339458d1d50dc208edcdd3
Authority renewal: none; single bounded remediation grant
Requested reasoning: Extra High
Cooperator delivery / trace destination: report file below
```

## Compact core

```text
Role: WORKER
Cooperator: Michal
Canonical checkout: /home/agile/Projects/framenest
Exact baseline: f59f4018eb86dfb40d339458d1d50dc208edcdd3 (verify at start; worktree clean)
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head: 0033 (no migrations authorized)
Git write authority: commits on feat/x-meme-browser-companion containing exactly allowlisted-path changes; coherent small commits permitted; no push
Allowlisted change scope (repository):
  src/framenest/adapters/api/public_published_application.py (F-1 handler, F-4 marker assert, F-5 sanitized log)
  src/framenest/adapters/api/public_published_api.py (F-4 assert support, F-5 sanitized logs on error paths)
  src/framenest/configuration.py (F-2 loopback guard for tcp mode)
  src/framenest/adapters/api/analysis_proposal_api.py and src/framenest/application/analysis_proposal.py plus the module(s) implementing the existing YouTube/X request rate-limit pattern (F-3 disposition B)
  src/framenest/infrastructure/persistence/engine.py (F-6 URI percent-encoding)
  src/framenest/server.py (only if F-2 guard requires surfacing a clear startup error)
  tests/** (focused regression tests per finding)
Allowlisted write paths (Meta):
  /home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/11_report_00.md
Python/test execution route (canonical, exclusive):
  ./.ap/ap exec runtime-info / test / test-focus with exact --baseline f59f4018eb86dfb40d339458d1d50dc208edcdd3
  NO ambient python/python3/.venv invocation of any kind.
NUC / SSH / sudo / provider / browser / external bind / push: none
```

## Task

1. **F-1 (C1)**: register a `RequestValidationError` handler on the public
   app returning the identical sanitized uniform-404 envelope used by every
   other public failure path. After the fix there must be NO reachable
   response on the public composition that reflects attacker input or
   framework/validation details. Extend the uniform-response contract tests
   to cover malformed UUID path params and out-of-range query params
   (`GET /api/media/not-a-uuid`, `GET /api/media?limit=9999`,
   negative offset, malformed location ids) asserting byte-level equality
   with the standard 404 envelope where practical.
2. **F-2 (C2)**: in ingress configuration validation, require the tcp-mode
   host to be a loopback address; settings load fails closed otherwise with
   an explicit error naming the constraint. UDS modes unchanged. Add unit
   tests in `tests/unit/test_configuration_ingress.py`: loopback tcp OK;
   non-loopback IPv4 and IPv6 rejected; UDS modes unaffected. Do NOT add any
   dev-override escape hatch in this grant.
3. **F-4**: when composing/serving public HTML, verify the companion-marker
   replacement actually occurred; if the marker is absent, fail loudly
   (startup-time check preferred) instead of silently serving companion
   references that will 404.
4. **F-5**: emit one sanitized structured-log event before uniform failure
   responses (error code/class only; never paths, queries, identity data,
   exception text). Apply to the generic handler and the broad except blocks
   in the public API module listed by the audit.
5. **F-6**: percent-encode the database path component when composing the
   read-only SQLite URI; add a focused test covering a path containing
   reserved characters.
6. **F-3 (Cooperator disposition B — per-user rate limit)**: apply a
   per-user rate limit to `POST /api/workspace/media/{media_id}/analysis-
   proposals` mirroring the existing YouTube/X request limiter pattern
   (reuse its mechanism, constants style, and test approach; do not weaken
   those existing limiters). Duplicated proposals within the window are
   rejected with an honest sanitized 429-class response consistent with the
   existing pattern; audit behavior must not regress. Add focused tests:
   limit enforcement, window reset, per-user isolation (another user is not
   blocked), and admin list unaffected.

## Validation (include evidence)

- `./.ap/ap exec test-focus --baseline f59f401…` over your focused set:
  PASS with counts.
- Full declared test operation (`./.ap/ap exec test --baseline f59f401…`):
  PASS; classify pre-existing failures honestly instead of fixing them.
- Grep proof: no `RequestValidationError` default path remains reachable on
  the public app (cite your new handler); no non-loopback acceptance in tcp
  validation (cite the guard).
- Commits: coherent small set; suggested final message
  `fix: infosec hardening per independent audit conditions`; `git log
  --oneline
  -6`; no push.

## Hard boundaries

- No migrations; schema head stays `0033`. No ADR-body edits. No capability,
  route-inventory, or publication-gate changes. Workspace composition
  behavior unchanged except the tcp host guard.
- Sanitized logging must never include request paths, query strings,
  identity data, raw exception text, secrets, Tailscale hostnames, cookies,
  private media filenames, tweet URLs, or the companion PEM.
- Baseline mismatch or dirty worktree → stop `BLOCKED` before writing.
- Scope impossible inside the allowlist → stop `PARTIAL`/`BLOCKED` with the
  exact missing piece; record necessary deviations explicitly; never expand
  scope silently.

## Report

Write exactly one file:

`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/11_report_00.md`

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once. Full capability handshake. Start/end
commits, changed files, per-finding closure evidence (F-1, F-2, F-4, F-5,
F-6), test evidence with counts, grep proofs, terminal outcome `PASS` /
`PARTIAL` / `BLOCKED`. After the report: stop. No further actions.

```text
#------------------------------------------------------
```
