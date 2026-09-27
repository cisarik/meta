# Kronika one product — publication of the accepted modular-research documentation and contracts

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 30
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Publication Worker
Phase: publication
Task identity: KRONIKA-ONE-PRODUCT-S4-D-A-PUBLICATION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: public remote ref publication of the accepted documentation and provider-contract chain over the exact existing public repository; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Session declaration

This must be a genuinely fresh session. This grant authorizes exactly one
non-force fast-forward publication of the accepted chain head to public
`main`. It grants no other ref, no force, no host, no deployment and no
further publication.

## Cooperator publication authorization

Dispatching this prompt is the explicit Cooperator publication grant for this
refspec. It names one accepted chain head and one refspec only. No other ref
may move.

## Accepted artifact

```text
Accepted chain head: 40e51cb2d061ead96850c9c94aa59de54d5e1310
Tree: ec3c6c9db49ede4bfcd3616263b388bb26451834
Subject: fix(kronika): preserve research configuration in AI CLI writers
Parent: 75e9b07b2bf2269568382e28d40a8d2ff8d4bc28
Chain: fd277a9 -> 72009c3 (S4-D documentation, Orchestrator-accepted)
       -> 75e9b07 (S4-A contracts, implementation PASS)
       -> 40e51cb2 (S4-A CLI preservation correction, implementation PASS)
Acceptance evidence: 29_report_00.md (acceptance-PASS, seven of seven fixed
  claims, no findings) on candidate 40e51cb2; 26_report_00.md for the
  documentation slice
Delta over the current public main fd277a9…: 22 paths, 3277 insertions and
  341 deletions
```

## Starting state (verified at issuance, 2026-09-26)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `40e51cb2d061ead96850c9c94aa59de54d5e1310`, parent
  `75e9b07b2bf2269568382e28d40a8d2ff8d4bc28`, tree
  `ec3c6c9db49ede4bfcd3616263b388bb26451834`; clean index and worktree; the
  accepted chain is a descendant of the current public main.
- Local `main` = `origin/main` = `fd277a9a64a6965df76127dbec5b1735d2fb3cdd`.
- Public heads observed read-only at issuance:
  `refs/heads/main` = `fd277a9a64a6965df76127dbec5b1735d2fb3cdd`,
  `refs/heads/feat/chatgpt-page-ask-kernel` =
  `26d28b16c08a5e7e0179a32c16646bfdc1009c81`,
  `refs/heads/feat/x-meme-browser-companion` =
  `7ff6546f345827d6df20bd5b13d5e57cb4bc90db`.
- Remote `origin` = `https://github.com/cisarik/framenest.git`.
- Governing AP gitlink and detached `.ap` HEAD:
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- `private/**` is never read; no host or provider action.

## Goal

Publish exactly the accepted chain head to public `main` by a guarded
fast-forward and a non-force push, then prove it by direct public readback.
Nothing else changes.

## Required sequence

1. **Repository gate.** Verify the physical root and standalone Git directory,
   branch `feat/kronika-one-product`, HEAD = the accepted chain head, tree,
   parent, clean index and worktree, AP pin, local `main` = `origin/main` =
   `fd277a9…`, and that the chain head is a descendant of it. Record the
   current public heads with `git ls-remote
   https://github.com/cisarik/framenest.git` (all heads, before).
2. **Fast-forward local main.** Switch to `main`, confirm it is exactly
   `fd277a9…`, then `git merge --ff-only
   40e51cb2d061ead96850c9c94aa59de54d5e1310`. Only a fast-forward is
   acceptable; otherwise stop. Confirm local `main` = the chain head and the
   worktree is clean.
3. **Non-force push.** `git push origin refs/heads/main:refs/heads/main`. No
   force, no tags, no other refspec, no mirror, no deletion, no remote config
   change.
4. **Direct public readback.** `git ls-remote
   https://github.com/cisarik/framenest.git` (all heads, after). Confirm
   `refs/heads/main` = the chain head and that every other head is unchanged.
5. **Restore the working branch.** Switch back to `feat/kronika-one-product`;
   confirm HEAD = the chain head, clean worktree, AP pin unchanged, and
   `origin/main` updated.

## Authority and containment

Positive authority: the five steps above; read-only public `ls-remote`; local
Git branch switch, the fast-forward merge of `main`, and the single non-force
push; the terminal report write at the exact destination when absent.

Negative authority: no other ref push or move; no force, tag, deletion, remote
config change, or fetch beyond `ls-remote`; no code, test, docs, AP, packaging
or configuration edit; no host, NUC, SSH, provider or service action; no Meta
commit; no subagent. Do not read `private/**`. Do not run `sudo -v` or
`sudo -K`.

## Stopping conditions

Stop and report on: any gate mismatch; public `main` not at `fd277a9…`; a
merge that is not a fast-forward; a rejected push; a readback mismatch or
another head moved; or any instruction conflict. Preserve the first causal
failure and never force.

## Completion and report contract

`PASS` means the accepted chain head is public `main` and direct readback
matches. Use `Phase-qualified result: publication-PASS` only then.
Logical-whole closure stays `not-closed`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the before
and after public head lists; the exact push refspec and result; the readback
output; local ref states before and after; changed files (the report only);
validation; deviations/risks/missing evidence; one smallest next step (S6:
records, access and approval); `Report justification: new-mutation`; authority
expiry; and:

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
separate completion notice with status, exact report path and SHA-256.
Terminal report or cancellation expires this authority.

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
Downloadable prompt filename: 30_publication_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 30_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
