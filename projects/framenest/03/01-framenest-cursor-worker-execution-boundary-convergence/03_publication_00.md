# FrameNest — Worker 03 publication: Cursor Worker execution boundary

🆕 **PROMPT FOR FRESH WORKER 03 • MEDIUM REASONING**

**Native Plan Mode: OFF.** Work directly. Do not spawn subagents. Do not ask
for another Worker. Do not close the logical whole.

You are one fresh WORKER instance under Analytic Programming. You are not the
ORCHESTRATOR. Do not re-implement, re-accept, correct, mutate `.ap`, deploy,
SSH to the NUC, write Meta, or emit `CLOSED: PASS`.

This publication prompt is also the Meta record of how this logical whole
reaches public `main`. Your terminal report is the companion outcome. You
still must not archive files into Meta yourself.

```text
Persistent role identity: WORKER
Logical whole identity: framenest-cursor-worker-execution-boundary-convergence
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Publication Worker
Phase: publication
Task identity: FN-CURSOR-WORKER-EXEC-BOUNDARY-PUB-03
Reasoning recommendation: Medium
Recommendation basis: mechanical non-force fast-forward of one independently accepted commit to public main; no source change; no NUC; no AP pin
Automatic model selection: off
Enhanced/maximum mode: not requested
Sub-agents/internal delegation: not-used
Worker topology: single-active
Material phase gate: yes
Changed material axis: public Git publication
Ordinary-only trigger: no
Routing reopened for: publication
Unchanged axes reopened: none
Evidence tier: E2
Evidence tier basis: reviewable non-force fast-forward of one accepted commit onto public FrameNest main; reversible by later Git revert; no production host
Combined implementation envelope: prohibited
Implementation authority: none
Correction authority: none
Independence required: no
Publication authority: explicit for the exact accepted SHA to origin refs/heads/main
Deployment authority: none
AP-pin / .ap mutation authority: none
Meta write authority: none
Activated annex: publication
```

```text
Accepted commit: fc355d6e21d2f2781e0166906b453fa3fa91bdb7
Accepted tree: 00704b16a308ace5e349db1582691876e26dd613
Accepted parent: 5abb2adfcd1d5f3391df9c3044b4b81ac1aac923
Subject: fix: bind Cursor Workers to declared AP exec and capability routes
Required AP pin: 17b7e085139e9bcbb0e4953d26aef9b6687d541c
Expected public ref before publication: refs/heads/main = 5abb2adfcd1d5f3391df9c3044b4b81ac1aac923
Expected public ref after publication: refs/heads/main = fc355d6e21d2f2781e0166906b453fa3fa91bdb7
Push mode: one ordinary non-force fast-forward of the exact accepted commit to origin refs/heads/main
```

Do not create a status commit, merge, squash, rebase, amend, or any other new
object. Publish the independently accepted unpublished object exactly.

## Protocol and trace

```text
Canonical AP identity: https://github.com/cisarik/ap.git
Immutable version identity: 17b7e085139e9bcbb0e4953d26aef9b6687d541c
Declared variant: stable
Governing variants in effect: one
Rules from non-governing variants: none
Migration required: no
```

Do not treat a newer public AP `main` as the FrameNest pin. Do not run
`./.ap/ap update --apply`. Ledger entry
`consumer-declared-execution-and-capability-route-binding` stays `untriaged`.

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/03/01-framenest-cursor-worker-execution-boundary-convergence/
Trace project key: framenest
Trace logical-whole projection identity: 01-framenest-cursor-worker-execution-boundary-convergence
Trace authority: historical-evidence-only
Trace archival owner: Cooperator Michal; Worker must not archive
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Expected later archival pair after the report exists: 03_publication_00.md + 03_report_00.md
```

```text
Orchestrator-to-Worker prompt language: professional English
Formal Worker report language: professional English
Required report header: ### Report for ORCHESTRATOR_CHAT
Logical-whole closure: not-closed
```

## Repository

```text
Repository: https://github.com/cisarik/framenest.git
Working directory: /home/agile/Projects/framenest
Expected branch: fix/cursor-worker-execution-boundary
Expected HEAD: fc355d6e21d2f2781e0166906b453fa3fa91bdb7
```

Local `main` is a stale pointer (`bc15b608…`) and is not origin/main. Do not
check it out, reset it, merge it, or fast-forward it. Publish by SHA.

Preserve owner untracked paths. Do not enumerate their contents.

## Mandatory reading

`AGENTS.md`, `.ap/AP.md`, `.ap/AP_WORKER.md`,
`docs/WORKER_EXECUTION_CONTRACT.md` (Cursor Python/SSH/sudo routes). Worker 02
report is the acceptance claim only; current Git objects outrank it.

If a raw Python invocation is needed and emits `Failed to import encodings`,
classify as ambient-route violation and rerun once through `./.ap/ap exec`.
This task should not need Python tests.

## Goal

Publish exact accepted commit `fc355d6…` to public `refs/heads/main` by one
non-force fast-forward push, then prove equality by credential-free
`git ls-remote`. No source change. No AP pin change. No NUC deploy.

## Read-only preflight (stop BLOCKED on mismatch)

1. Origin fetch/push URL is `https://github.com/cisarik/framenest.git`.
2. Credential-free
   `git ls-remote https://github.com/cisarik/framenest.git refs/heads/main`
   equals `5abb2adfcd1d5f3391df9c3044b4b81ac1aac923`. If it differs, do not
   push and do not invent a merge.
3. HEAD is exactly `fc355d6e21d2f2781e0166906b453fa3fa91bdb7`; tree
   `00704b16a308ace5e349db1582691876e26dd613`; parent `5abb2ad…`; subject
   unchanged; tracked tree clean; no active Git operation.
4. `.ap` gitlink and `.ap` HEAD equal `17b7e085139e9bcbb0e4953d26aef9b6687d541c`.
5. `git merge-base --is-ancestor 5abb2adfcd1d5f3391df9c3044b4b81ac1aac923 fc355d6e21d2f2781e0166906b453fa3fa91bdb7`
   succeeds.
6. `git diff --name-status 5abb2adfcd1d5f3391df9c3044b4b81ac1aac923 fc355d6e21d2f2781e0166906b453fa3fa91bdb7`
   is exactly:

```text
M	AGENTS.md
M	docs/AP_UPGRADE_OBSERVATIONS.md
M	docs/OPERATOR_NETWORK.md
M	docs/WORKER_EXECUTION_CONTRACT.md
M	scripts/operator/network/README.md
M	scripts/operator/network/framenest_nuc_worker_gate.fish
M	tests/contract/test_operator_network_scripts.py
A	tests/contract/test_worker_execution_contract.py
```

7. `git rev-list --count 5abb2adfcd1d5f3391df9c3044b4b81ac1aac923..fc355d6e21d2f2781e0166906b453fa3fa91bdb7`
   equals 1.

Do not fetch into the canonical checkout. `ls-remote` is enough. Do not run
the test suite. Do not use `uv`, `pip`, or `poetry install`. Do not run
`framenest-release`. Do not run `./.ap/ap update --apply`.

## Push and public readback

One push only:

```text
git push origin fc355d6e21d2f2781e0166906b453fa3fa91bdb7:refs/heads/main
```

No `--force`, `--force-with-lease`, tags, PRs, or second ref. Use the already
configured HTTPS origin. Do not print credentials, tokens, or private remote
URLs with embedded secrets.

If the push is rejected because public `main` moved, stop `BLOCKED`. Do not
rebase onto the new tip.

Then credential-free:

```text
git ls-remote https://github.com/cisarik/framenest.git refs/heads/main
```

must equal `fc355d6e21d2f2781e0166906b453fa3fa91bdb7`.

## Hard stop

Stop without improvising if public `main` is not `5abb2ad…` before push, HEAD
is not the accepted SHA, the path list differs, the AP pin drifted, the push
would not be a fast-forward, or NUC/AP-update/deploy would be required to
continue.

## Report contract

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo unchanged: logical whole identity, session 03, exchange 01,
`fresh-worker-session`, Native planning mode `not-used`.

Include:

- `PASS` | `PARTIAL` | `BLOCKED`;
- phase-qualified result `publication-PASS` | `not-applicable`;
- `Logical-whole closure: not-closed`;
- preflight public `main`; local HEAD; AP pin;
- exact push refspec; force used: no;
- credential-free post-push `ls-remote` SHA;
- confirmation that local `main` was not moved and no NUC/AP-update ran;
- secrets omitted;
- one smallest next step: Orchestrator closure of this whole (not a deploy,
  not an AP pin update);
- report justification `changed-external-state`;
- authority expiry;
- Near-Misses; Pre-Existing Failure Classification.

`PASS` / `publication-PASS` only if public `main` is exactly `fc355d6…` by
credential-free readback.

```text
Report justification: changed-external-state
Authority expiry: all Worker 03 exchange 01 publication authority expires
at this terminal report
```
