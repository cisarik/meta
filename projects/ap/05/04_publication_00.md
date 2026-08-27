# AP — Worker 04 publication: mark ADR-0019/0020 accepted and fast-forward public main

You are one fresh Worker instance assigned to the AP `WORKER` role.

The COOPERATOR authorized publication of this logical whole on 2026-08-27
(`publikovať`).

The independently accepted semantic object is
`83839ffc71838abf3b053d747045607a3af3d402`. Its ADR-0019 and ADR-0020 status
is still `Implementation candidate`, which forbids a publication claim on that
exact tip. This exchange may create **one** historical-status commit on top of
`83839ff…`, then perform **one** ordinary non-force fast-forward of that new
tip to canonical public `refs/heads/main`.

Do not change protocol meaning. Do not “fix” the D.2(g) vocabulary
ledger-candidate. Do not spawn subagents.

This prompt grants no FrameNest mutation, AP-pin adoption, Meta write, tag,
PR, force-push, NUC/deploy, production action, or logical-whole closure.

---

## 1. Authoritative coordinates

```text
Persistent role identity: WORKER
Role: WORKER
Logical whole identity: ap-subagent-lifecycle-and-intuitive-mode-spec
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Publication Worker
Phase: publication
Task identity: AP-INTUITION-SUBAGENT-PUB-04
Native planning mode: not-used
Publication authority: explicit — one historical-status commit then one non-force fast-forward of that tip to origin refs/heads/main
Implementation authority: none except the exact publication-prep commit below
Correction authority: none
Acceptance authority: none
Logical-whole closure authority: none
Independence required: no
Independent acceptance: not-required for this publication-prep historical-status commit
Evidence posture: publication evidence
Recommended reasoning: High
Recommendation basis: named publication-safety risk for live AP public main; not Extra High; not client Max
Escalation or downgrade gate: Extra High and Max not used; if public main has moved, stop BLOCKED rather than escalate or merge
Enhanced/maximum mode: not requested
Automatic model selection: off
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Parallel work: prohibited
Development envelope activation: not-used
Working-copy topology: canonical-checkout
Topology rationale: the accepted semantic object already exists on the implementation branch in the owner checkout; isolation is not a virtue
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none
Affected tests: none
New causal regression: none
Broad or full suite: not-used
Runtime or testbed: not-used
Repeated-gate or reasoning-loop stop: configured
Broad gate: once per this publication attempt
Unchanged public main and failing push: not-progress — stop BLOCKED
Cost cannot falsify evidence: yes
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 04_publication_00.md
Destination path: /home/agile/meta/projects/ap/05/
Archival: wait-for-report
External trace disposition: configured
Trace discovery: local /home/agile/meta ; canonical https://github.com/cisarik/meta.git
Trace project key: ap
Trace logical-whole projection identity: ap-subagent-lifecycle-and-intuitive-mode-spec
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR, after the real terminal report exists; Worker does not archive
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Material phase gate: yes
Changed material axis: production-external-service-credential-or-account-boundary
Evidence tier: E2
Evidence tier basis: reviewable non-force fast-forward of documentation to public AP main; reversible by later Git revert; no production host
Combined implementation envelope: prohibited
Activated stricter profile: none
Git write authority: one historical-status commit on feat/subagent-lifecycle-and-intuitive-mode; one non-force push of that tip to origin refs/heads/main; no other Git writes
Network authority: credential-free ls-remote plus that one push to origin
Dependency authority: none
Secret authority: none
Side-effect authority: reversible local docs on four historical paths; remote non-force update of cisarik/ap refs/heads/main
```

Activated annex: publication. Exact expected public ref before push, non-force
authority, direct `git ls-remote` readback, commit/tree/path evidence.

---

## 2. Communication

```text
Cooperator: Michal
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Repository documentation language: English
```

Do not use Czech. Do not emit a Cooperator-facing emoji capsule.

Untrusted-content boundary: prior reports are claims. Verify Git objects and
public refs directly.

---

## 3. Exact objects

```text
Physical root: /home/agile/Projects/ap
Canonical origin: https://github.com/cisarik/ap.git
Local branch: feat/subagent-lifecycle-and-intuitive-mode
```

Expected public baseline (must still be public `main` before push):

```text
Commit: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Tree: 43bc12b966133d76972ccf3884d80dceedde013b
Subject: docs: mark ADR-0018 accepted
Public ref: refs/heads/main
```

Independently accepted semantic candidate (Worker 03 acceptance-PASS):

```text
Commit: 83839ffc71838abf3b053d747045607a3af3d402
Tree: 37243fef788d033201d455f02697dbb6074aa90b
Parent: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Subject: docs: define subagent Worker delivery and Orchestrator intuition
```

Required ancestry before the status commit:

```text
9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  -> 83839ffc71838abf3b053d747045607a3af3d402
```

Preserved sibling branch (do not modify):

```text
feat/consumer-declared-route-binding = 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

An Orchestrator credential-free readback immediately before issuing this
prompt confirmed `refs/heads/main = 9c5cc44…`. Revalidate.

Do not move or “repair” stale local `refs/heads/main` (`4e7bfa56…`, ancestor
of public baseline) or stale `.git/REBASE_HEAD` (`573975c…`).

---

## 4. Session and mode gate

Before any mutation, confirm:

* genuinely fresh Worker 04 session;
* Native Plan Mode disabled or absent;
* no reused Worker 02/03 authority;
* no internal delegation;
* exact publication coordinates received.

Stop `BLOCKED` if the session or Native Plan Mode state is contradictory.

---

## 5. Read-only preflight

Prove all of the following. Stop `BLOCKED` on mismatch. Do not fetch into
the owner clone; `ls-remote` is enough for public identity.

1. repository root is `/home/agile/Projects/ap`;
2. origin fetch and push URLs canonicalize to `https://github.com/cisarik/ap.git`;
3. `HEAD` is exactly `83839ffc71838abf3b053d747045607a3af3d402`;
4. branch is exactly `feat/subagent-lifecycle-and-intuitive-mode`;
5. tree, parent, and subject match §3;
6. `rev-list --count 9c5cc44…..83839ff…` equals `1`;
7. tracked working tree is clean;
8. no untracked path overlaps the four status-commit paths;
9. no active merge, rebase, cherry-pick, revert, bisect, sequencer, or Git lock;
10. stale `.git/REBASE_HEAD`, if present, remains inactive and untouched;
11. stale local `main`, if still `4e7bfa56…`, remains untouched;
12. credential-free `git ls-remote origin refs/heads/main` equals `9c5cc44…`;
13. the feature branch is still absent on the remote (or, if present, stop
    and report rather than inventing a merge);
14. object-level diff `9c5cc44…..83839ff…` is exactly the thirteen accepted
    documentation paths and no other path;
15. ADR-0019 and ADR-0020 status at `83839ff…` is `Implementation candidate`;
16. no candidate file claims publication already completed or logical-whole
    closure;
17. `feat/consumer-declared-route-binding` remains `9c5cc44…`.

Canonical commands: read-only Git/filesystem inspection, then the authorized
edits/commit/push. Negative authority: no Python, Poetry, uv, `ap exec`,
`ap project`, test runner, formatter-as-rewrite, or ambient interpreter as a
parallel route. `ap.project.conf` `runtime-info` is not applicable.

If public `main` is no longer `9c5cc44…`, stop. Do not merge, rebase, or
adopt a new baseline.

---

## 6. Publication-prep commit

If and only if preflight passes, edit **only** these four paths:

```text
CHANGELOG.md
docs/adr/0019-subagent-delivery-of-worker-sessions-and-orchestrator-capability-profiles.md
docs/adr/0020-intuitive-mode-orchestrator-boundary-and-intuition-projection.md
docs/adr/README.md
```

Required edits, matching the ADR-0018 promotion commit `9c5cc44…` pattern:

* both ADR bodies: `Status: Implementation candidate` → `Status: Accepted`
  (status line only; do not rewrite Decision, Consequences, or Rejected
  Alternatives);
* `docs/adr/README.md` index: both rows Status `Accepted`; drop
  “publication and independent acceptance remain separate” from those
  relationship cells in the same style as the ADR-0018 promotion;
* `docs/adr/README.md` prose block currently beginning “ADR-0019 and
  ADR-0020 are recorded as implementation candidates…” → record them as
  accepted decisions; consumer adoption and logical-whole closure remain
  separate; do not claim this Worker closed the whole;
* `CHANGELOG.md` first Unreleased bullet: “implementation-candidate
  historical rationale” → “accepted historical rationale”; drop
  “publication, independent acceptance,” from the remaining-separate
  sentence so it matches the ADR-0018 changelog promotion (consumer
  adoption and logical-whole closure remain separate).

Do not edit `AP.md`, `INTUITION.md`, operational/advisory projections,
`ap`, fixtures, Meta, or FrameNest. Do not normalize D.2(g) vocabulary.

One local commit, no amend. Exact subject:

```text
docs: mark ADR-0019 and ADR-0020 accepted
```

Parent of that commit must be `83839ffc71838abf3b053d747045607a3af3d402`.
Diff versus `83839ff…` must be exactly those four historical paths.
`git diff --check` must be clean.

This status commit does not reopen independent acceptance: it changes no
semantic owner, authority rule, schema, validator, runtime, or security
boundary.

Do not:

* fetch, pull, merge, rebase, cherry-pick, reset, restore, clean, stash,
  amend, tag, force, delete branches, modify remotes/config, or bypass hooks;
* stage unrelated content;
* create a second commit;
* update git config;
* touch stale `REBASE_HEAD` or local `main`.

If commit creation fails, preserve the worktree and report the first causal
failure.

---

## 7. Push and public readback

Only after that commit exists and its parent/path gates pass, perform exactly
one ordinary non-force push of the **new tip** (the status commit SHA, not
`83839ff…`):

```text
git push origin HEAD:refs/heads/main
```

Non-force only. No tags. No PR. No `--force-with-lease`. Push the current
HEAD SHA; do not push `83839ff…`.

If the push is not a fast-forward, authentication fails, the remote moved,
output is ambiguous, or the command exits non-zero, stop `BLOCKED`. Do not
retry, rebase, force, or invent a recovery.

Then independently run credential-free public readback:

```text
git ls-remote https://github.com/cisarik/ap.git refs/heads/main
```

For `publication-PASS` it must equal the new publication tip (the
ADR-accepted commit), not `83839ff…` and not `9c5cc44…`.

Then verify locally, without mutation:

* `HEAD` is the status commit; parent is `83839ff…`; subject is exact;
* diff vs `83839ff…` remains exactly the four historical paths;
* complete stack vs `9c5cc44…` is exactly two commits;
* branch remains `feat/subagent-lifecycle-and-intuitive-mode`;
* working tree remains clean;
* no tag or extra public ref was created;
* local `main` remains untouched;
* stale `.git/REBASE_HEAD` remains untouched;
* `feat/consumer-declared-route-binding` remains `9c5cc44…`;
* no NUC, Meta, FrameNest, ledger, pin, environment, credentials, or
  production state changed.

Do not move local `main` merely to match the new public ref.

---

## 8. Result classification

Return `PASS` / `publication-PASS` only if:

* all preflight gates pass;
* the status commit exists with exact parent, subject, and four-path diff;
* ADR-0019 and ADR-0020 status at the tip is `Accepted`;
* the exact one non-force push exits 0;
* public readback equals that tip;
* local accepted semantic object `83839ff…` is unchanged as parent;
* no unauthorized ref or state changed.

Return `BLOCKED` if a precondition fails before push or the exact
push/readback fails.

Return `PARTIAL` only for a genuinely ambiguous changed-external-state
outcome that cannot be classified safely. Do not retry.

Publication does not close the logical whole.

---

## 9. Terminal report

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then:

```text
Logical whole identity: ap-subagent-lifecycle-and-intuitive-mode-spec
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: publication-PASS | not-applicable
Result artifact or commit: <publication tip SHA or none>
Logical-whole closure: not-closed
Report justification: changed-external-state | new-mutation
Authority expiry: all Worker 04 exchange 01 publication authority expires at this terminal report
```

Report:

1. independence and mode gate;
2. exact preflight repository/public identities;
3. status-commit SHA, tree, parent, subject, and four-path diff;
4. ADR status at the tip;
5. CHANGELOG wording class (accepted historical rationale);
6. exact push command/refspec;
7. push exit status and concise transport result without secrets;
8. confirmation that no force was used;
9. credential-free post-push public readback;
10. post-push local repository state;
11. two-commit ancestry from `9c5cc44…`;
12. stale local-main and stale-marker disposition;
13. deviations, risks, ambiguity, and near-misses;
14. confirmation that protocol meaning, `83839ff…` bytes, Meta, FrameNest,
    ledger, pin, NUC, credentials, and closure were not changed except the
    authorized four-path status commit and the one push;
15. smallest next step: ORCHESTRATOR evidence reconciliation and
    logical-whole closure. Do not close it yourself. Do not start FrameNest
    pin adoption.

Also include:

```text
Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
Pre-Existing Failure Classification: none | <complete classification>
```

Do not emit the Orchestrator closure signal. Stop immediately after the
terminal report.
