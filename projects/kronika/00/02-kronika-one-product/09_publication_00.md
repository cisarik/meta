# Kronika one product — S3 milestone publication of the accepted commit

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 09
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Publication Worker
Phase: publication
Task identity: KRONIKA-ONE-PRODUCT-S3-PUBLICATION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: public remote ref publication of the accepted S0-S3 milestone over the exact existing public repository; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Session declaration

This must be a genuinely fresh session. This grant authorizes exactly one
non-force fast-forward publication of the accepted commit to public `main`.
It grants no other ref, no force, no host, no deployment, no code change and
no further publication.

## Cooperator publication authorization

Dispatching this prompt is the explicit Cooperator publication grant for this
refspec. It names one accepted commit and one refspec only. No other ref may
move.

## Accepted artifact

```text
Accepted commit: c975aba14840b97944aecc655907e3abc370341d
Tree: a80ab53cf5ee19ffe0af46de4e015519cd97d941
Subject: feat(capture): supervise capture separately from web deploys
Acceptance evidence: S3 acceptance report 08_report_00.md (acceptance-PASS, all six
  fixed claims, no blocking finding); S0-S2 and their corrections previously accepted
  (S2 re-acceptance 03_report_00.md)
Chain over the current public main: 93e7742, 96ef426, 5259b89, 82a6a59, c975aba
Diff over 26d28b16: 80 files changed, 5411 insertions, 1493 deletions
```

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `c975aba14840b97944aecc655907e3abc370341d`, parent
  `82a6a59803ed8830c19e51cd8f9bc1665c28a975`, tree
  `a80ab53cf5ee19ffe0af46de4e015519cd97d941`; clean index and worktree.
- Local `main` = `origin/main` =
  `26d28b16c08a5e7e0179a32c16646bfdc1009c81` (fast-forward source of truth).
- Public `refs/heads/main` observed read-only at issuance:
  `26d28b16c08a5e7e0179a32c16646bfdc1009c81`.
- Remote `origin` = `https://github.com/cisarik/framenest.git`.
- Governing AP gitlink and detached `.ap` HEAD:
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- `private/**` is never read.

## Goal

Publish exactly the accepted commit to public `main` by a guarded fast-forward
and a non-force push, then prove it by direct public readback. Nothing else
changes.

## Required sequence

1. **Repository gate.** Verify the physical root and standalone Git directory,
   branch `feat/kronika-one-product`, HEAD = the accepted commit, tree, parent,
   clean index and worktree, AP pin, local `main` = `origin/main` =
   `26d28b16c08a5e7e0179a32c16646bfdc1009c81`. Record the current public heads
   with `git ls-remote https://github.com/cisarik/framenest.git` (all heads,
   before).
2. **Fast-forward local main.** Switch to `main`, confirm it is exactly
   `26d28b16…`, then `git merge --ff-only c975aba14840b97944aecc655907e3abc370341d`.
   Only a fast-forward is acceptable; if it is not a fast-forward, stop.
   Confirm local `main` = accepted commit and the worktree is clean.
3. **Non-force push.** Push exactly
   `git push origin refs/heads/main:refs/heads/main`. No force, no tags, no
   other refspec, no `--mirror`, no branch deletion, no remote config change.
4. **Direct public readback.** `git ls-remote
   https://github.com/cisarik/framenest.git` (all heads, after). Confirm
   `refs/heads/main` = the accepted commit and that every other head is
   unchanged from the before list.
5. **Restore the working branch.** Switch back to `feat/kronika-one-product`;
   confirm HEAD = accepted commit, clean worktree, AP pin unchanged, and
   `origin/main` updated by the push.

## Authority and containment

Positive authority: the five steps above; read-only public `ls-remote`; local
Git branch switch, fast-forward merge of `main`, and the single non-force push;
the terminal report write.

Commands: read-only Git identity/status/log/diff queries; `git ls-remote` for
the exact public repository; `git switch main`; `git merge --ff-only
<accepted>`; the single `git push origin refs/heads/main:refs/heads/main`;
`git switch feat/kronika-one-product`; and the native file writer for the
report only.

Negative authority: no other ref push or move; no force, no tag, no deletion,
no remote/config change, no fetch beyond `ls-remote`; no code, test, docs, AP,
packaging or configuration edit; no host, NUC, SSH, deployment or service
action; no Meta commit; no subagent. Do not read `private/**`.

## Stopping conditions

Stop and report on: any gate mismatch; public `main` not at `26d28b16…`; the
merge not being a fast-forward; a rejected push; a readback that does not match
the accepted commit or that shows another head moved; or any instruction
conflict. Preserve the first causal failure. A failed publication leaves the
feature branch and the accepted commit untouched; never force.

## Completion and report contract

`PASS` means the accepted commit is public `main` and direct readback matches.
Use `Phase-qualified result: publication-PASS` only then. `PARTIAL` or
`BLOCKED` otherwise. Logical-whole closure stays `not-closed`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the before
and after public head lists; the exact push refspec and result; the readback
command and output; local ref states before and after; changed files (the
report only); validation; deviations/risks/missing evidence; one smallest next
step; `Report justification: new-mutation`; authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

Direct communication with the Cooperator (the short completion notice) is in
Slovak, masculine address for him. This prompt and the formal report are in
English. Do not use subagents. Do not commit Meta artifacts.

Finalize the report, save it at the exact destination, read it back in full,
and verify its first line, coordinates, content and path before the short
separate completion notice with status, exact report path and SHA-256. Terminal
report or cancellation expires this authority.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 09_publication_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 09_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
