# Publication Exchange 01 — Session 05 — Publish the Accepted Candidate to Public `main`

Persistent role identity: WORKER
Logical whole identity: framenest-admin-openai-compatible-provider-registry-and-vision-probe
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Publication Worker
Phase: Publication
Task identity: PUBLISH-ACCEPTED-CANDIDATE-7ff6546
Implementation authority: none
Delivery route: Agent Orchestrator default dispatch (fresh session; this prompt is its initial context)
Reasoning recommendation: Medium — a deterministic, exactly specified non-force Git publication with a strict pre-push ref gate and post-push readback
Recommended context capacity: approximately 250k tokens
Independence required: no (publication is a deterministic delivery step; acceptance already passed)
Sub-agents or internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Development envelope activation: not-used

## Goal

Publish the accepted candidate commit to the public repository, non-force:
`refs/heads/main` must become exactly
`7ff6546f345827d6df20bd5b13d5e57cb4bc90db`, and
`refs/heads/feat/x-meme-browser-companion` must be advanced to the same commit
so the tracked working ref stays coherent with the published main. No other
ref, no tag, no force, no NUC, no content change.

## Authority and scope

Positive authority:

- read-only `git ls-remote origin` / `git status` / `git log` / `git show` /
  `git rev-parse`;
- exactly one non-force push of the exact accepted commit to the two named
  refs (see below);
- read-only post-push `git ls-remote` readback.

Forbidden: any other Git write (no fetch, no stage, no commit, no branch, no
tag, no remote/config change, no force, no delete); any file change; any
network beyond the Git remote operations above; any credential inspection or
printing; any provider call; NUC/SSH/sudo; ambient Python; `poetry run`;
browser/GUI. If authentication or the remote gate fails, STOP and report —
never try alternate credentials, never reprint remote output containing
secrets, never force.

## Repository gate (before any push)

Working directory `/home/agile/Projects/framenest`.

1. `git status --porcelain -b` must show branch
   `feat/x-meme-browser-companion`, no porcelain lines, and the branch ahead
   of its upstream by exactly seven commits.
2. `git rev-parse HEAD` must equal
   `7ff6546f345827d6df20bd5b13d5e57cb4bc90db`; `git log --oneline -8` must
   show the accepted chain
   `33946e0 → f41df79 → 980db7a → e6d91d1 → c66f5b6 → 810b606 → 87411e0 → 7ff6546`.
3. `git remote get-url origin` must resolve to
   `https://github.com/cisarik/framenest.git` (a `.git` suffix difference is
   cosmetic; do not modify config).
4. Pre-push public-ref gate (required): `git ls-remote origin
   refs/heads/main refs/heads/feat/x-meme-browser-companion` must show BOTH
   refs at exactly `33946e08447dc92621ed6844b4b5d13a19ec29f1`, the expected
   common ancestor being fast-forwarded. A different value, a missing ref,
   an unreachable remote, or any ambiguity is **BLOCKED** — do not push;
   report the exact observed values.

## Publication action

Exactly one command:

```text
git push origin 7ff6546f345827d6df20bd5b13d5e57cb4bc90db:refs/heads/main 7ff6546f345827d6df20bd5b13d5e57cb4bc90db:refs/heads/feat/x-meme-browser-companion
```

Non-force only. If the push is rejected as non-fast-forward or by any policy,
STOP and report the exact outcome — do not retry with force or with a
different refspec.

## Post-push readback (required)

1. `git ls-remote origin refs/heads/main refs/heads/feat/x-meme-browser-companion`
   must show both refs at `7ff6546f345827d6df20bd5b13d5e57cb4bc90db`.
2. `git status --porcelain -b` must show the local branch no longer ahead of
   its upstream (both at the accepted commit) and no porcelain lines.
3. Record the exact `ls-remote` output in the report.

## Changed-path allowlist

None — no repository files may change. The only allowed effects are the two
remote ref updates above and the single Meta report.

## Meta persistence contract (execute exactly)

```text
Meta persistence owner: this Worker, for the single report path named below.
Prompt persistence owner: ORCHESTRATOR (already written; do not rewrite it).
Exact report destination: /home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/05_report.md
Write the complete terminal report to that path after the work, then verify
byte identity. Do not create other Meta files. Do not rename. Do not commit
Meta Git. Do not commit FrameNest.
If the path already contains a terminal report, STOP (PARTIAL) — do not
overwrite.
The Cooperator must not be asked to create, paste, or rename files.
```

## Report contract

Begin exactly with `### Report for ORCHESTRATOR_CHAT`; echo these coordinates
once (`Worker session ordinal: 05`, `Worker exchange ordinal: 01`); include:

1. compact core: `status` PASS/PARTIAL/BLOCKED;
   `Phase-qualified result: publication-PASS` only when the push succeeded
   non-force and the readback proves both refs at the accepted commit;
   `not-applicable` otherwise;
2. start and end commit (both `7ff6546…` unless BLOCKED before push);
3. changed files: none in the repository; the Meta report only;
4. the pre-push observed ref values, the exact push command, its output, and
   the post-push `ls-remote` output (sanitized — no tokens, no URLs with
   credentials);
5. `Report justification: new-mutation`;
6. risks/deviations or `none`;
7. one smallest next step;
8. `Orchestration critique` (MEASURED/LEAD);
9. Resolved Execution Issues / Near-Misses and Pre-Existing Failure
   Classification;
10. `Logical-whole closure: not-closed`; authority-expiry statement.

Save, read back fully, verify first line and coordinates, then send a short
separate completion notice with status, location, and SHA-256.

## Stopping conditions

Stop and report BLOCKED when the repository gate fails, the pre-push remote
gate does not show both refs at the expected parent, the push is rejected, the
post-push readback does not prove both refs at the accepted commit, or the
Meta destination is occupied or unsafe. Do not improvise recovery; do not use
force, delete, or refspec alternatives.

Authority expiry: this terminal report ends this grant.
