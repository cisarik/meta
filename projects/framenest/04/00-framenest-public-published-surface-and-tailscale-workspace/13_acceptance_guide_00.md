# FrameNest Worker prompt — 04/00 session 05 exchange 03 (Cooperator acceptance-test instruction guide)

**Issuer:** the fresh Agent Orchestrator. Exchange 02 accepted (`be35922`).
All code, audit remediation, and documentation deliverables of this logical
whole are complete. Per the Cooperator's end-of-whole flow, you now produce
the **step-by-step human test instruction guide** Michal will follow to
verify the surfaces himself before Orchestrator closure.

This is a documentation-only task. You write ONE Meta file. You do not
implement anything.

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
5. `docs/INFOSEC.md`, `docs/adr/0074-…boundary.md`, and your exchange 01–02
   reports in this Meta folder

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 05
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Infosec Remediation Worker
Task identity: author the Cooperator acceptance-test instruction guide for this whole
Phase: acceptance-support (documentation only)
Continuity anchor: your exchange 02 terminal report; HEAD be35922d223c49f3b140453e69b313c9086c3831
Authority renewal: complete new bounded grant; exchange 02 authority expired at its terminal report
Requested reasoning: Extra High
```

## Compact core

```text
Role: WORKER
Cooperator: Michal
Canonical checkout: /home/agile/Projects/framenest
Exact baseline: be35922d223c49f3b140453e69b313c9086c3831 (verify at start; worktree clean)
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head: 0033
Git write authority: none — read-only git inspection only
Repository mutation: PROHIBITED entirely
Allowlisted write paths (Meta):
  /home/agile/meta/projects/framenet/04/00-framenest-public-published-surface-and-tailscale-workspace/13_report_00.md
Python / tests / ap exec / network / NUC / SSH / sudo / provider / browser: none
```

**Path correction binding:** the allowlisted path above contains
`framenet` — that is an issuer transcription error carried from a prior tool
mishap. Write to the corrected path:
`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/13_report_00.md`

## Task

Produce the Cooperator acceptance-test guide as the main body of the report
file. Requirements:

1. **Audience**: Michal on his MacBook, fish shell, plus his NUC where
   explicitly marked. Human-facing command blocks MUST follow AGENTS.md
   conventions (`# [MacBook / fish]` or `# [NUC / bash]`, ending with
   `#------------------------------------------------------`). No mixed
   blocks.
2. **Honest environment split**, three clearly separated parts:
   - **Part A — local MacBook verification** (no NUC, no Tailscale needed):
     run the trusted-loopback dev server locally; verify workspace admin UX
     in a browser (Manage media publish/unpublish controls, contributor
     filter, team-aliases panel, analysis-proposals browser); run the public
     reader locally on its UDS/socket config and view the public page;
     exercise search on published items; run
     `scripts/operator/infosec/framenest_public_surface_check.sh` against
     the local public reader and paste its PASS table; spot-check uniform
     404s by hand.
   - **Part B — NUC/Tailscale verification steps** (only if he chooses to
     run them now): ordinary mapped user flows via Tailscale Serve (own
     gallery, propose analysis, own aliases), administrator review inbox,
     companion extension behavior unchanged. Mark every step requiring live
     identity mapping or production data clearly, with privacy reminders.
   - **Part C — deferred items** (explicitly NOT testable until later
     wholes): public TLS bind, rate limits at proxy, VPS hosting — pointer
     to `docs/INFOSEC.md` checklist.
3. Each numbered step needs: purpose, exact commands, expected observable
   result, and what a failure looks like + which report line to cite back to
   the Orchestrator.
4. Include a short "what changed in this whole" digest (commit range
   `37da5f2..be35922`, one line per rollout) so he knows what he is testing.
5. End with an explicit "report back" template: which steps passed/failed,
   screenshots optional, any deviation notes.

## Validation

- Verify every command you print exists: flags referenced against
  `--help`/source of the named scripts; startup commands against
  `README.md`/`DEVELOPMENT.md`/`pyproject.toml` entry points; script paths
  exist at HEAD.
- Re-check every file:line citation you include.
- `git status` clean before writing; no repository mutation after.

## Report

The single Meta file (corrected path) IS both your terminal report and the
guide. Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once, brief capability handshake (this exchange's
rows), then the guide itself, then terminal outcome `PASS`/`PARTIAL`/
`BLOCKED`. After writing: stop. No further actions.

```text
#------------------------------------------------------
```
