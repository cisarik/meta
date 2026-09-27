# Kronika one product — S6 candidate transport to GitHub (`feat/kronika-one-product`)

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 36
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Publication Worker
Phase: publication
Task identity: KRONIKA-ONE-PRODUCT-S6-CANDIDATE-TRANSPORT
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — one exact non-force branch push with direct readback; no tests; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Purpose and boundary

The Cooperator is switching development from the office PC to a MacBook and
needs the S6 candidate commit available on GitHub before the PC is parked.
The S6 candidate is **not accepted** (independent acceptance status PARTIAL,
finding S6-A35-F01 blocking). Therefore this grant publishes **only the
working branch** as transport. It does **not** publish `main`, does not imply
acceptance and does not authorize deployment.

## Fresh-session opening

Genuinely fresh Worker session; inherit no prior authority. Independently
verify every gate before mutation. No subagents. No tests, no host, no NUC, no
browser, no provider, no credentials, no `private/**`. Client must be
write-capable; the only mutation is the Git push below and the terminal report
write.

## Starting state (verified read-only at issuance, 2026-09-27)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `38e7beeb3921d7c0fd8e717e480754fbd18130c9` (parent
  `40e51cb2d061ead96850c9c94aa59de54d5e1310`, tree
  `d6d5d314bfaf98d968235a867004b89b3187ac68`, subject
  `feat(kronika): add private records and administrator approval`); clean index
  and worktree; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (gitlink and `.ap` HEAD).
- Local `main` = `origin/main` = `40e51cb2…`; public `refs/heads/main` of
  `https://github.com/cisarik/framenest.git` = `40e51cb2…`; public
  `feat/kronika-one-product` does not exist yet; other public heads are
  `feat/chatgpt-page-ask-kernel` `26d28b16…` and
  `feat/x-meme-browser-companion` `7ff6546f…`.
- The S6 acceptance verdict is PARTIAL with finding S6-A35-F01
  (correction-required, high); a separate correction grant and re-audit follow
  on the MacBook. This grant is transport only.

## Required sequence (ordered; fail closed)

1. Verify: physical root; branch; HEAD, parent, tree, subject; empty
   `git status --porcelain --untracked-files=no`; AP pin (gitlink and `.ap`
   HEAD); local `main` = `origin/main` = `40e51cb2…`.
2. Verify the public state with direct readback:
   `git ls-remote https://github.com/cisarik/framenest.git`; `refs/heads/main`
   must be `40e51cb2…`; `refs/heads/feat/kronika-one-product` must be absent;
   the two other heads must be unchanged. Stop on any divergence.
3. Push exactly this refspec, non-force, from the repository root:

```text
git push origin refs/heads/feat/kronika-one-product:refs/heads/feat/kronika-one-product
```

   No other ref; never `--force`; never delete or move any ref.
4. Direct readback after the push: `git ls-remote` must show
   `refs/heads/feat/kronika-one-product` = `38e7beeb…` and `refs/heads/main`
   unchanged at `40e51cb2…`; the two other heads unchanged.
5. Report. Do not push anything else; do not create tags; do not change
   repository settings; do not run tests.

## Authority and containment

Positive authority: read-only repository and remote inspection; the one exact
non-force push above; the terminal report write at the exact destination when
absent, with full readback.

Negative authority: no second ref or refspec; no force or history rewrite; no
tag; no `main` or other branch change; no remote settings; no repository file
change; no tests; no deployment or NUC contact; no host, SSH, sudo, browser,
provider, credential or `private/**` action; no subagent; no Meta commit.

## Stopping conditions

Stop with `PARTIAL`/`BLOCKED` on: repository or remote mismatch; absent
credentials or an authentication failure; a push that would require force; a
different remote state after the push; or any instruction conflict. Preserve
the first causal failure; do not improvise or retry with another ref.

## Validation

```text
Evidence tier: E1
Evidence tier basis: one bounded non-force branch push with direct readback; no product change
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none — no repository change
Affected tests: none
New causal regression: none — transport only
Broad or full suite: not-used
Runtime or testbed: not-used
Independent acceptance: not-required — transport of an explicitly unaccepted candidate branch
```

## Completion and report contract

`PASS` means the branch `feat/kronika-one-product` exists publicly at
`38e7beeb…` while `main` and the two other heads are unchanged, with direct
`git ls-remote` evidence. Use `Phase-qualified result: publication-PASS` only
for that result; otherwise `not-applicable`. `Logical-whole closure:
not-closed`. `Report justification: new-mutation`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 36, exchange 01) exactly once. Include: the
pre-push identity values; the exact push command and exit status; the
post-push `ls-remote` values (main, the new branch, the two other heads); the
statement that this is transport of an unaccepted candidate and not `main`
publication; deviations, risks and missing evidence; one smallest next step
(the S6 correction grant on the MacBook); the critique block; and the
authority-expiry statement.

The formal report is in English; the short completion notice to the Cooperator
is in Slovak, masculine address. Finalize the report, save it at the exact
destination below only if absent, read it back in full, verify its first line,
coordinates, content and path, then send the separate short completion notice
with status, path and SHA-256. Terminal report or cancellation expires this
authority.

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
Downloadable prompt filename: 36_publication_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 36_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
