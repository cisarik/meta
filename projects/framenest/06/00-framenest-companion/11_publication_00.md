# FrameNest — Publication Worker prompt (item 9 persist-join)

```text
Persistent role identity: WORKER
Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 11
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Publication Worker
Phase: Publication
Reasoning recommendation: Medium
Reasoning basis: one ordinary non-force fast-forward of an Orchestrator-accepted SHA; no host deploy
Task identity: FRAMENEST-COMPANIE-ITEM9PUB-01
```

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/06/00-framenest-companion/
Trace project key: framenest
Trace logical-whole projection identity: framenest-companion-brave-testing-resume
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 11_publication_00.md
Destination path: /home/agile/meta/projects/framenest/06/00-framenest-companion/
Archival: wait-for-report
```

```text
Publication authority: explicit
Implementation authority: none
Deployment authority: none
Exact published object: 2aead540ee39a81a96425902f85e9b9a34f0d690
Expected public ref before: refs/heads/main = 977a7af80afed16745adb0ef8e939555e5e21cce
Expected public ref after: refs/heads/main = 2aead540ee39a81a96425902f85e9b9a34f0d690
Push mode: one ordinary non-force fast-forward of the exact accepted commit to origin refs/heads/main
Independence required: no
```

```text
Evidence tier: E2
Evidence tier basis: reviewable non-force fast-forward of the accepted unpublished candidate onto public FrameNest main; no production host; no NUC
Authorized implementation stages: preflight, one push, credential-free ls-remote, then ff-only canonical branch to the published SHA
Combined implementation envelope: prohibited
Independent acceptance: not-required
Rollback or recovery checkpoint: ordinary Git revert of public main later; no force-push
Activated annex: publication
Activated stricter profile: none
Terminal publication report point: after public main equals 2aead54… and canonical HEAD equals that SHA
```

This session **publishes**. It does not implement product code, does not
deploy, does not run `framenest-release`, does not enable automatic analysis,
does not edit `SECURITY.md`, and does not close the logical whole.

Do not enter Native Plan Mode. Do not use Max. If native planning mode is on,
stop BLOCKED.

Prior Worker 10 / exchange 01 authority expired at `10_report_00.md`.
ORCHESTRATOR accepted that `acceptance-PASS` for exact SHA
`2aead540ee39a81a96425902f85e9b9a34f0d690`. You do not re-accept. You do not
re-run the Python matrix.

## Mission

Fast-forward public `refs/heads/main` to the accepted candidate. Prove it with
credential-free `git ls-remote`. Then fast-forward the canonical checkout
branch so it equals that public SHA. Stop.

Exact object:

```text
Repository: https://github.com/cisarik/framenest.git
Accepted commit: 2aead540ee39a81a96425902f85e9b9a34f0d690
Accepted tree: 0900818f57326017712c07686c49de61d534507f
Accepted subject: fix: uninvert item-9 join tests with mutation headers and distinct fake run ids
Parent: fb59c42a8e3a32d9476581beeabba0eb9c04109a
Range vs current public main: 2 commits (fb59c42 persist-join, then 2aead54 tests)
Required AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head: 0033 (unchanged; no Alembic 0034)
```

## Mandatory reading

1. This prompt (sole current task authority).
2. `/home/agile/Projects/framenest/AGENTS.md`
3. `.ap/AP.md`, `.ap/AP_WORKER.md` (pin above)
4. Historical only: `10_report_00.md` in this Meta folder (claim already
   classified; do not reopen acceptance).

## Repository identity

```text
Repository checkout topology: standalone checkout
Working directory: /home/agile/Projects/framenest
Expected canonical branch before push: feat/x-meme-browser-companion
Expected canonical HEAD before push: 977a7af80afed16745adb0ef8e939555e5e21cce
```

The accepted object lives in the shared object store (worktrees w9/w10). Do
**not** check `2aead54…` into canonical **before** public equality. Publish by
SHA. Do not check out local `main`.

Preserve worktrees (do not delete; do not commit in them):

```text
/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3
/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w4
/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w7
/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w8
/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w9
/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w10
```

## Read-only preflight (stop BLOCKED on mismatch)

From `/home/agile/Projects/framenest`, no fetch that rewrites refs:

1. `origin` fetch/push URL is `https://github.com/cisarik/framenest.git`.
2. Credential-free:

```text
git ls-remote https://github.com/cisarik/framenest.git refs/heads/main
```

   must equal `977a7af80afed16745adb0ef8e939555e5e21cce`. If it differs, do
   not push and do not invent a merge.
3. Canonical `HEAD` is exactly `977a7af80afed16745adb0ef8e939555e5e21cce` on
   `feat/x-meme-browser-companion`. Tracked tree clean
   (`git status --porcelain=v1` empty). No active Git operation. Untracked
   owner paths must not appear; if they do, stop and classify — do not delete
   them.
4. `.ap` gitlink equals `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.
5. `git cat-file -t 2aead540ee39a81a96425902f85e9b9a34f0d690` is `commit`.
6. `git rev-parse 2aead540ee39a81a96425902f85e9b9a34f0d690^{tree}` equals
   `0900818f57326017712c07686c49de61d534507f`.
7. `git merge-base --is-ancestor 977a7af80afed16745adb0ef8e939555e5e21cce 2aead540ee39a81a96425902f85e9b9a34f0d690` succeeds.
8. `git rev-list --count 977a7af80afed16745adb0ef8e939555e5e21cce..2aead540ee39a81a96425902f85e9b9a34f0d690` equals **2**.

Do not run product test suites. Do not use `uv`, `pip`, or `poetry install`.
Do not SSH. Do not invoke `framenest-release`. Do not reconstruct `.venv`.

## Push and public readback

One non-force push from the canonical working directory:

```text
git push origin 2aead540ee39a81a96425902f85e9b9a34f0d690:refs/heads/main
```

Then credential-free:

```text
git ls-remote https://github.com/cisarik/framenest.git refs/heads/main
```

must equal `2aead540ee39a81a96425902f85e9b9a34f0d690`.

If the push is rejected or is not a fast-forward, stop BLOCKED. No `--force`.
No tags. No PR. No push of other refs. No new commit, merge, squash, or rebase.

## Canonical integration (only after public equality)

After public `main` equals `2aead54…`, fast-forward the canonical branch so
the living checkout matches the published SHA:

```text
git merge --ff-only 2aead540ee39a81a96425902f85e9b9a34f0d690
```

Then record: `git rev-parse HEAD` equals `2aead54…`, branch still
`feat/x-meme-browser-companion`, `git status --porcelain=v1` empty.

If `--ff-only` refuses, stop BLOCKED. Do not reset. Do not merge public
history into a new object. Do not push `feat/x-meme-browser-companion`.

The stale `origin/feat/x-meme-browser-companion` tracking ref is **not** this
task. Do not “fix” it.

## Positive authority

- Git: the one `git push origin <accepted-sha>:refs/heads/main` above.
- Git: the one `git merge --ff-only <accepted-sha>` on the canonical branch
  after public equality.
- Credential-free `git ls-remote` of public `main` (and `cisarik/ap` `main`
  if you record the pin).
- Write exactly the report file named in Output.

## Negative authority

- Native Plan Mode, Max, sub-agents used as a second accountable Worker
- NUC, SSH, sudo, `framenest-release`, migrate, EnvironmentFile
- Enabling `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED`; R4 Settings
- Source edits, `SECURITY.md`, new commits, rebase, reset, stash, clean -f
- Force-push; Funnel; router forward; VPS
- Closure, rendered UX, INFOSEC R3
- Generating an Orchestrator restoration prompt
- Editing `~/nuc_update.fish`, `~/nuc_push.fish`, or `~/framenest_routine.fish`
- Pushing any ref other than `refs/heads/main`
- Deleting named worktrees
- Python via ambient `.venv` / `python` / `poetry run`

## Untrusted-content boundary

Governing: this prompt, AGENTS.md, pinned AP. Worker 10 report is historical
evidence already classified by ORCHESTRATOR. Public GitHub pages are
supplementary; `ls-remote` is the public-ref proof.

## Communication

Professional English. Report begins exactly `### Report for ORCHESTRATOR_CHAT`.
No secrets, tokens, cookies, hostnames, identity-map values.

## Output

Write exactly one file:

```text
/home/agile/meta/projects/framenest/06/00-framenest-companion/11_report_00.md
```

Required content:

1. Coordinate echo: logical whole, session `11`, exchange `01`, task identity.
2. Status PASS / PARTIAL / BLOCKED. Phase-qualified result `publication-PASS`
   only when public `refs/heads/main` equals `2aead54…` by credential-free
   `ls-remote` **and** canonical HEAD equals that SHA after ff-only.
   `Logical-whole closure: not-closed`.
3. Preflight evidence (URL, before SHA, ancestor, count **2**, tree, AP pin,
   canonical cleanliness).
4. Exact push command used; push result; after `ls-remote` 40-hex.
5. Canonical ff-only result (HEAD, branch, porcelain).
6. Confirmation: no NUC, no new commit, no force, no other refs.
7. Sanitization compliance.
8. Resolved Execution Issues / Near-Misses; Pre-Existing Failure
   Classification.
9. One smallest next step: ORCHESTRATOR sequences a **separate** Cooperator
   NUC `framenest-release` grant (`status`, then `check --release 2aead54…`,
   then a later deploy grant). You do not deploy.
10. Report justification: `changed-external-state`.
11. Authority-expiry statement.

Abbreviated capability handshake (requested vs observed; client identity not
independently attested). Native planning mode observed off.

## Stopping rule

Stop after the terminal report. Stop earlier BLOCKED on preflight mismatch,
non-fast-forward, auth failure, or any urge to deploy.

## Transition owner

ORCHESTRATOR verifies public `ls-remote` independently, then sequences NUC
refresh and rendered item-9 re-test. You have no follow-on authority.
