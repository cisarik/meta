# FrameNest Worker prompt — 04/00 session 05 exchange 04 (final freeze preparation: repository acceptance guide, script polish)

**Issuer:** the fresh Agent Orchestrator. Exchange 03 delivered the
Cooperator acceptance-test guide. The Cooperator has decided:
1. **FREEZE** all public-net / VPS / TLS deployment planning for this whole;
   any future deploy era MUST reconnect with the then-current deployment
   documentation (NUC runbook, `framenest-release` immutable contract,
   `docs/INFOSEC.md` checklist).
2. The acceptance guide must also live **in the FrameNest repository**
   (not only Meta), completed with the deploy-future annex below.
3. Close the two non-blocking script polish items you reported.

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
5. Your exchange 01–03 reports and the guide they produced
   (`13_report_00.md` in this Meta folder)

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 05
Worker exchange ordinal: 04
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Infosec Remediation Worker
Task identity: repository acceptance guide + deploy-freeze annex + script polish (executable bit, -h early exit)
Phase: implementation (freeze preparation)
Continuity anchor: your exchange 03 terminal report; HEAD be35922d223c49f3b140453e69b313c9086c3831
Authority renewal: complete new bounded grant; exchange 03 authority expired at its terminal report
Requested reasoning: Extra High
```

## Compact core

```text
Role: WORKER
Cooperator: Michal
Canonical checkout: /home/agile/Projects/framenest
Exact baseline: be35922d223c49f3b140453e69b313c9086c3831 (verify at start; worktree clean)
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head: 0033 (no migrations)
Git write authority: commits on feat/x-meme-browser-companion containing exactly allowlisted-path changes; no push
Allowlisted change scope (repository):
  scripts/operator/infosec/framenest_public_surface_check.sh (git mode +x; -h exits 0 after usage)
  scripts/operator/infosec/framenest_log_triage.sh          (-h exits 0 after usage)
  scripts/operator/infosec/framenest_socket_permissions_check.sh (-h exits 0 after usage)
  docs/ACCEPTANCE_DUAL_AUDIENCE.md (new — repository home of the guide)
  README.md (one Documentation Map pointer line only)
Allowlisted write paths (Meta):
  /home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/14_report_00.md
Validation commands: bash -n; live `-h` invocation of each script (exit code
  assertion); git read commands; ./.ap/ap project check with exact --baseline.
  NO ambient python/python3/.venv. NO network/NUC/SSH/sudo/provider/push.
```

## Task

1. **Script polish**: set the executable bit on the three infosec scripts
   (git mode change, e.g. `chmod +x` + stage so the index records 100755);
   make an explicit `-h`/`--help` print usage and `exit 0` before any other
   logic in each script. Keep every other behavior identical.
2. **Repository acceptance guide**: create `docs/ACCEPTANCE_DUAL_AUDIENCE.md`
   carrying your exchange 03 guide, professionally edited for repository
   permanence:
   - Keep the honest Part A (local MacBook) / Part B (conditional NUC/
     Tailscale, honesty banner about the older deployed release) /
     Part C (deferred to preflight) split and the report-back template.
   - Add a **Deployment-freeze annex** stating: public-net/VPS/TLS work is
     intentionally frozen for this whole; when a future era resumes it, it
     MUST begin from the then-current deployment truth
     (`docs/UBUNTU_NUC_DEPLOYMENT.md`, the `deploy/ubuntu/framenest-release`
     immutable-update contract per ADR-0060, `docs/INFOSEC.md` §4
     checklist) rather than from this document; the planned preflight shape
     is: independent posture re-verification (surface-check script against
     the real origin), proxy-owned transport limits (rate limits, body caps,
     timeouts, concurrency — audit F-8/C3), TLS/HSTS/ACME baseline,
     systemd hardening suggestions review, F-7 reader/writer atomic release
     rule exercised, Cooperator step-by-step operational authorization for
     every host mutation, and Cooperator acceptance sign-off before DNS or
     any exposure.
   - Note the two polish fixes and the executable-bit change as part of this
     freeze commit range.
3. **README**: exactly one Documentation Map line pointing to
   `docs/ACCEPTANCE_DUAL_AUDIENCE.md`.

## Validation

- Live `-h` invocation of each script prints usage and exits 0.
- `bash -n` all three; `git diff --check` clean; staged modes show 100755
  for the three scripts.
- Every command/fact in the repository guide matches source at HEAD
  (re-run your citation verification pass; line numbers may shift only in
  files you changed).
- `./.ap/ap project check --baseline be35922d223c49f3b140453e69b313c9086c3831`
  PASS (output class). Full test suite NOT required (shell/git/doc-only),
  state that honestly.
- Commits: coherent small set; suggested final message
  `docs: repository acceptance guide and infosec script polish`;
  `git log --oneline -8`; no push.

## Hard boundaries

- No product code changes; no SPEC/SERVER/SECURITY/ADR-body edits; schema
  head stays `0033`.
- No deployed-state claims anywhere; the freeze annex records intent, not
  capability.
- Do not print secrets, Tailscale hostnames, identity-map contents, cookies,
  private media filenames, tweet URLs, or the companion PEM.
- Baseline mismatch or dirty worktree → stop `BLOCKED` before writing.

## Report

Write exactly one file:

`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/14_report_00.md`

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once. Capability handshake. Start/end commits,
changed files with final git modes, `-h` exit-code evidence, terminal outcome
`PASS`/`PARTIAL`/`BLOCKED`. Quote the final full HEAD SHA exactly as
`git rev-parse HEAD` prints it. After the report: stop.

```text
#------------------------------------------------------
```
