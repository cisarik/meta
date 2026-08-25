# FrameNest Worker prompt — 04/00 session 05 exchange 02 (implementation: INFOSEC hardening manual and operator diagnostic scripts)

**Issuer:** the fresh Agent Orchestrator. Exchange 01 accepted (four commits
closing audit findings F-1..F-6; note: your report mis-transcribed the final
commit's full SHA — actual HEAD is
`3a21405e08ff30a840afe655e702d931e833acf2`; chain otherwise verified). The
Cooperator now explicitly authorizes the previously out-of-scope request:
the **INFOSEC hardening manual and administration/diagnostic tooling**,
repository-local, so he can judge public-net readiness honestly.

Deliver to the **same healthy Worker session 05** (`current-worker-session`).
Native Plan Mode **off**.

```text
#------------------------------------------------------
```

You are the same FrameNest Worker under Analytic Programming, session ordinal
05 of logical whole
`framenest-public-published-surface-and-tailscale-workspace`.

Read before action:

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/.ap/AP.md`
3. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
4. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
5. `docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md`
6. Your remediation baseline context: audit `10_report_00.md` + your
   exchange 01 report `11_report_00.md`
7. Existing operator-tool conventions:
   `deploy/ubuntu/framenest_release.py`, `scripts/operator/**`,
   `docs/UBUNTU_NUC_DEPLOYMENT.md`, `SECURITY.md`, `SERVER.md`

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 05
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Infosec Remediation Worker
Task identity: author repository-local INFOSEC hardening manual, audit record, and bash operator diagnostics
Phase: implementation (security documentation and tooling)
Continuity anchor: your session 05 exchange 01 terminal report; actual HEAD 3a21405e08ff30a840afe655e702d931e833acf2
Authority renewal: complete new bounded grant; exchange 01 authority expired at its terminal report
Requested reasoning: Extra High
```

## Compact core

```text
Role: WORKER
Cooperator: Michal
Canonical checkout: /home/agile/Projects/framenest
Exact baseline: 3a21405e08ff30a840afe655e702d931e833acf2 (verify at start; worktree clean)
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head: 0033 (no migrations authorized)
Git write authority: commits on feat/x-meme-browser-companion containing exactly allowlisted-path changes; coherent small commits permitted; no push
Allowlisted change scope (repository):
  docs/INFOSEC.md (new)
  README.md (one short pointer line to docs/INFOSEC.md, nothing else)
  scripts/operator/infosec/** (new bash-only tools)
  tests/** (only if you extract testable logic; not required)
Allowlisted write paths (Meta):
  /home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/12_report_00.md
Validation commands: git read commands; bash -n on every new script;
  shellcheck IF installed (report its absence, never install anything);
  ./.ap/ap project check with exact --baseline for repo hygiene.
  NO ambient python/python3/.venv invocation of any kind.
NUC / SSH / sudo / provider / network calls / push: none
```

## Task

### 1. `docs/INFOSEC.md` — the hardening manual (professional English)

Structure it as a senior security researcher's deployment-facing document:

1. **Scope and honesty banner**: repository-local guidance; nothing here
   claims deployed state; final public-net go/no-go belongs to the
   separately authorized TLS/reverse-proxy preflight plus Cooperator
   acceptance.
2. **Audit record (2026-08-25)**: summarize the independent audit — verdict
   yes-with-conditions; findings table F-1..F-9 with severities, one-line
   descriptions, and closure status (F-1/F-2/F-4/F-5/F-6 closed in
   `bcf5ec1..3a21405`; F-3 closed via Cooperator disposition B rate limit;
   F-7 release-ordering rule recorded; F-8 deferred to proxy ownership;
   F-9 numbering note if applicable); verified-claims inventory summarized.
3. **Threat model digest**: trust boundaries (public origin vs Tailscale
   workspace vs trusted loopback), principal assets, top abuse vectors
   (unauthenticated reads, range/stream economics, credential-free
   fingerprinting, header spoofing, alias leakage).
4. **Public-bind readiness checklist** (the core deliverable): ordered,
   checkbox-style, covering — application conditions met (C1/C2 closed);
   reverse proxy MUST own: TLS termination config baseline (modern TLS only,
   HSTS, ACME discipline), per-IP connection caps, body size limits,
   timeouts (connect/read/send), concurrency limits, rate limiting for
   content routes; OS/host: firewall default-deny inbound except proxy
   ports, SSH discipline, unattended security upgrades, time sync, disk
   full monitoring; service: dedicated non-login user, UDS directory
   permissions, systemd hardening options (ProtectSystem,
   PrivateTmp, NoNewPrivileges etc.) as suggestions for the preflight whole;
   secrets: no secrets in repo/env templates committed; log hygiene rules;
   backup/restore verification cadence reference to existing foundations;
   the F-7 reader/writer atomic-release rule.
5. **Incident response first steps**: what to pull (journal ranges, audit
   events), how to unpublish instantly (admin PUT), how to drop the public
   listener without touching workspace.
6. **Explicit non-goals**: no registration/payments/cloud SaaS; router port-
   forwarding forbidden; Funnel to workspace socket forbidden.

### 2. Bash operator tools under `scripts/operator/infosec/`

Bash only (`#!/usr/bin/env bash`, `set -euo pipefail`, shellcheck-clean where
shellcheck exists). All targets/paths from env vars with safe defaults and
clear usage output; NEVER embed real hostnames, tokens, media names, or NUC-
specific identifiers — placeholders only. Read-only diagnostics:

- `framenest_public_surface_check.sh`: given `FRAMENEST_PUBLIC_BASE_URL`,
  verify public posture — `/docs`, `/openapi.json`, an admin path, and a
  POST to `/api/media` all return the identical sanitized 404 envelope;
  `Cache-Control: no-store` and `X-Content-Type-Options: nosniff` present;
  malformed-UUID probe matches the same envelope byte-for-byte; print a
  clear PASS/FAIL table; exit non-zero on any failure. No authentication,
  no mutation attempts beyond safe GET/POST-to-denied-route probes.
- `framenest_log_triage.sh`: given a unit name (default placeholder) and
  optional since window, summarize counts of `public_unexpected_failure`,
  `public_request_validation_rejected`, `public_http_exception_rejected`,
  `ANALYSIS_PROPOSAL_RATE_LIMIT`, and audit-action lines from
  `journalctl` output; flag spikes above a configurable threshold; print
  nothing sensitive (counts and event keys only).
- `framenest_socket_permissions_check.sh`: stat the configured socket
  paths; fail if missing, world-readable/writable, or owned by an
  unexpected user pattern (env-configurable expectations).

### 3. README pointer

One line in `README.md` linking `docs/INFOSEC.md`. Nothing else changes.

## Validation (include evidence)

- `bash -n` output class for every new script; shellcheck result or its
  absence stated.
- Static self-review walk-through of each checklist claim against source
  (file:line citations for every factual security statement in INFOSEC.md).
- `./.ap/ap project check --baseline 3a21405e08ff…` PASS (output class).
- `git diff --check` clean; changed files within allowlist; coherent small
  commits; suggested final message `docs: infosec hardening manual and
  operator diagnostics`; `git log --oneline -6`; no push.

## Hard boundaries

- Documentation states repository truth only; it must NOT claim any live
  deployment, NUC state, VPS, DNS, TLS certificate, or completed preflight.
- Scripts perform strictly read-only, unauthenticated operations; no sudo,
  no service restarts, no writes outside their own temp/stdout.
- Do not print secrets, Tailscale hostnames, identity-map contents, cookies,
  private media filenames, tweet URLs, or the companion PEM anywhere.
- No ADR-body edits; SPEC/SERVER/SECURITY untouched this exchange.
- Baseline mismatch (must equal the corrected SHA above) or dirty worktree →
  stop `BLOCKED` before writing.

## Report

Write exactly one file:

`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/12_report_00.md`

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once. Full capability handshake. Start/end
commits, changed files, per-deliverable evidence (manual outline + citations
density; per-script bash -n/shellcheck results), terminal outcome `PASS` /
`PARTIAL` / `BLOCKED`. After the report: stop. No further actions.

```text
#------------------------------------------------------
```
