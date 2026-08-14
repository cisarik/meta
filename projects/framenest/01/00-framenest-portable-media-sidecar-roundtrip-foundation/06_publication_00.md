# FrameNest Portable Media Sidecar Round-Trip Foundation — Publication

Logical whole identity: `framenest-portable-media-sidecar-roundtrip-foundation`

Worker session ordinal: `06`
Worker exchange ordinal: `01`
Worker session target: `fresh-worker-session`
Worker phase: `publication`
Native planning mode: `not-used`
Maximum plan-only cycles: `0`

You are a fresh publication Worker. Publish only the exact independently accepted FrameNest candidate specified below.

Do not redesign, correct, amend, rebase, squash, merge, retest, deploy, or close the logical whole.

## Canonical repository

```text
https://github.com/cisarik/framenest.git
```

Expected current public `main` before publication:

```text
a23b4bc786357da3591a4f75087b7e8a3d50d341
```

Exact accepted candidate:

```text
commit:  230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
tree:    3d74e08f65c2d99f99c602085e6e097451a52230
parent:  87032d3826daaa217769acccc0eb37f1c1ffb1de
subject: docs: reconcile sidecar implementation status
AP pin:  041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Required ancestry:

```text
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
87032d3826daaa217769acccc0eb37f1c1ffb1de
633fa3b3884bc865dba26643034ef0c2fc12f394
96bf7df2001c38284d9aa136b56d0109f24700d5
a23b4bc786357da3591a4f75087b7e8a3d50d341
```

Independent acceptance disposition already obtained:

```text
Standard terminal status: PASS
Phase-qualified result: reacceptance-PASS
Accepted artifact: 230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
Publication eligibility: eligible-for-separate-publication
```

The accepted residuals are non-blocking:

* complete Windows `os.replace` and case-folding evidence remains incomplete;
* the trusted-library chmod/replace race remains documented;
* isolated-clone console-script failures reproduce on the exact public baseline and are not candidate-specific.

## Candidate source

Use the existing clean independent-acceptance clone:

```text
/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w5-e01
```

Do not mutate, clean, restore, reset, switch, rebase, amend, or commit in this checkout.

## Mandatory pre-publication gate

Before any push, directly verify:

* exact physical working directory;
* origin is the canonical FrameNest repository;
* detached `HEAD` is the exact accepted candidate;
* exact tree, parent, subject, ancestry, and AP pin;
* tracked worktree, index, and untracked state are clean;
* no merge, rebase, cherry-pick, revert, or bisect is active;
* the accepted candidate remains absent from public refs;
* credential-free direct `ls-remote` reports public `main` at exact `a23b4bc…`;
* the accepted candidate is a strict fast-forward descendant of that public tip;
* no other repository or host mutation is active.

Do not rely on a cached local remote-tracking ref.

If any invariant fails, stop with `BLOCKED`. Identify only the exact mismatch and the smallest safe continuation.

If public `main` is already the exact accepted candidate, perform no push. Complete direct public readback and report the already-published condition precisely.

If public `main` is neither the expected baseline nor the exact accepted candidate, stop with `BLOCKED`.

## Publication authority

When every gate passes, perform exactly one ordinary non-force push of the exact accepted commit:

```text
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb:refs/heads/main
```

Forbidden:

* force or force-with-lease;
* tag creation;
* publication of a feature branch;
* merge commit;
* commit amendment;
* rebase or squash;
* dependency installation;
* repository content mutation;
* Meta mutation;
* AP mutation or repin;
* deployment, service restart, NUC/SSH/sudo/provider/browser action;
* application or database mutation.

No deployment is required. This logical whole adds an operator-invoked portable sidecar capability but does not require production activation.

## Mandatory public readback

After the push, use credential-free direct Git evidence to verify that public `main` is exactly:

```text
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
```

Using a disposable public readback location, verify from public objects:

* exact commit, tree, parent, and subject;
* exact five-commit ancestry to `a23b4bc…`;
* exact cumulative changed-path set against `a23b4bc…`;
* AP gitlink remains `041de310…`;
* the publication is fast-forward;
* the accepted candidate content was not rewritten;
* no unexpected public branch or tag was created.

Do not substitute GitHub web rendering for direct Git evidence.

## Report contract

Return a terminal report containing:

```text
Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 06
Worker exchange ordinal: 01

Standard terminal status: PASS | BLOCKED
Phase-qualified result: publication-PASS | publication-BLOCKED
Result artifact or commit: <exact public commit or not-applicable>
Logical-whole closure: not-closed
Report justification: public-ref-mutation | invariant-failure
```

Include:

* all pre-publication gates;
* exact push command semantics and result;
* credential-free public readback;
* commit/tree/parent/subject;
* ancestry and cumulative path verification;
* final source-checkout cleanliness;
* confirmation of no force-push, deployment, Meta mutation, or AP mutation;
* deviations, residual risks, execution issues, and pre-existing failure classification;
* the smallest next step.

A publication PASS is not logical-whole closure. The ORCHESTRATOR alone performs closure after reviewing this report.

All Worker authority expires at the terminal report. Do not issue another Worker prompt.
