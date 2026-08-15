You are one fresh WORKER instance under Analytic Programming.

You are not the ORCHESTRATOR. Do not re-implement, re-accept, correct the
advisory fixtures, mutate Meta or FrameNest, force-push, tag, open a pull
request, update consumer pins, deploy, or close this logical whole.

```text
Persistent role identity: WORKER
Logical whole identity: ap-cooperator-ergonomics-cost-proportional-execution-and-meta-trace-integration
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Publication Worker
Phase: publication
Task identity: AP-ERGONOMICS-PUB-04
Native planning mode: not-used

Publication authority: explicit
Implementation authority: none except the exact publication-prep commit below
Independence required: no
Accepted semantic candidate: 1cd2783838cb8cc9483792bc043010b0bbdef347
Accepted semantic tree: a68aaf200ca6d68581aa87302efa27541eb26665
Accepted semantic parent: 17b7e085139e9bcbb0e4953d26aef9b6687d541c
Expected public ref before publication: refs/heads/main = 17b7e085139e9bcbb0e4953d26aef9b6687d541c
Push mode: one ordinary non-force fast-forward push of the publication tip to refs/heads/main

Recommended reasoning: High
Recommendation basis: named publication-safety risk for the live AP public main; not Extra High; not client Max
Escalation or downgrade gate: Extra High and Max not used; if public main has moved, stop BLOCKED rather than escalate
Enhanced/maximum mode: not requested
Automatic model selection: off
Internal delegation / sub-agents: not-used
Worker topology: single-active

Material phase gate: yes
Changed material axis: production-external-service-credential-or-account-boundary
Evidence tier: E2
Evidence tier basis: reviewable non-force fast-forward of documentation to public AP main; reversible by later Git revert; no production host
Combined implementation envelope: prohibited
Independent acceptance: not-required for this publication-prep historical-status commit
Activated stricter profile: none

Development envelope activation: not-used
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none
Affected tests: none
New causal regression: none
Broad or full suite: not-used
Runtime or testbed: not-used
Independent acceptance: not-required
Repeated-gate or reasoning-loop stop: configured
Cooperator delivery / trace destination:
  filename: 04_publication_00.md
  destination: projects/ap/03/00-ap-cooperator-ergonomics-cost-proportional-execution-and-meta-trace-integration/04_publication_00.md + 04_report_00.md
  archival: wait-for-report

External trace disposition: configured
Trace discovery: local /home/agile/meta ; canonical https://github.com/cisarik/meta.git
Trace project key: ap
Trace logical-whole projection identity: ap-cooperator-ergonomics-cost-proportional-execution-and-meta-trace-integration
Trace authority: historical-evidence-only
Trace archival owner: Cooperator, manual, after this real terminal report exists
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
```

Activated annex: publication. Exact expected public ref, non-force authority,
direct `git ls-remote` readback, commit/tree/path evidence.

## 1. Goal

Publish accepted Disposition B to public AP `refs/heads/main`.

The independently accepted semantic object is `1cd27838…`. Its ADR-0017 status
is still `Implementation candidate`, which forbids a publication claim on that
exact tip. Therefore this exchange may create **one** historical-status commit
on top of `1cd27838…`, then fast-forward public `main` to that new tip.

Do not change protocol meaning. Do not “fix” the parked advisory-fixture
ledger-candidates.

## 2. Frozen facts

```text
Worktree: /home/agile/Projects/ap-worktrees/ap-cooperator-ergonomics-cost-proportional-execution-w2
Branch: docs/cooperator-ergonomics-cost-proportional-execution
Canonical repository: https://github.com/cisarik/ap.git
Owner checkout, do not switch: /home/agile/Projects/ap at 041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Acceptance-PASS for `1cd27838…` is complete. Parked non-authorizing
ledger-candidates (fixture spellings in `PROMPT_ENGINEERING_PATTERNS.md`) stay
parked.

## 3. Read-only preflight before any mutation

Prove, then stop `BLOCKED` on mismatch:

1. `origin` of the worktree is `https://github.com/cisarik/ap.git`.
2. Credential-free `git ls-remote origin refs/heads/main` equals
   `17b7e085139e9bcbb0e4953d26aef9b6687d541c`. If it differs, do not push and
   do not invent a merge.
3. Worktree HEAD is exactly `1cd27838…`, clean, parent `17b7e085…`, tree
   `a68aaf20…`.
4. Diff `17b7e085…..1cd27838…` is exactly the accepted 13 documentation paths.
5. Owner checkout was not moved.

Do not fetch into the owner clone. `ls-remote` is enough.

## 4. Publication-prep commit

If and only if preflight passes, edit only:

- `docs/adr/0017-cooperator-ergonomics-cost-proportional-execution.md`
  — `Status: Accepted`
- `docs/adr/README.md` — ADR-0017 index row Status `Accepted`; remove the
  “no public acceptance, publication, or closure claim” clause; keep AP.md as
  sole semantic owner
- `CHANGELOG.md` — first Unreleased bullet: drop “implementation candidate”
  and the sentence that independent acceptance remains future; record ADR-0017
  as accepted historical rationale; consumer adoption and logical-whole
  closure remain separate

Do not edit `AP.md`, `PROMPT_CONTRACTS.md`, operational projections, fixtures,
`ap`, Meta, or FrameNest.

One local commit, no amend. Subject: `docs: mark ADR-0017 accepted`.
Parent of that commit must be `1cd27838…`. Diff vs `1cd27838…` must be exactly
those three historical paths.

This status commit does not reopen independent acceptance: it changes no
semantic owner, authority rule, schema, validator, runtime, or security
boundary.

## 5. Push and public readback

Only after that commit exists:

```text
git push origin HEAD:refs/heads/main
```

Non-force only. No tags. No PR. No `--force-with-lease`. If the push is not a
fast-forward, stop and report; do not recover with force or rebase onto a
moved `main`.

Then credential-free `git ls-remote origin refs/heads/main` must equal the
new publication tip (the ADR-accepted commit), not `1cd27838…` and not
`17b7e085…`.

Record commit, tree, parent, subject, and the three changed paths.

## 6. Authority

```text
Git authority: one historical-status commit on the named worktree branch; one non-force fast-forward push of that tip to origin refs/heads/main; no other Git writes
Network authority: credential-free ls-remote plus that one push to origin
Dependency authority: none
Secret authority: none
Side-effect authority: reversible local docs on three historical paths; remote non-force update of cisarik/ap refs/heads/main
```

Leave the worktree in place. Do not switch `/home/agile/Projects/ap`.

## 7. Report

Professional English. Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

`Phase-qualified result: publication-PASS` only if public `refs/heads/main`
equals the new tip, the tip’s parent is `1cd27838…`, and the tip’s diff vs
`1cd27838…` is exactly the three historical paths.
`Logical-whole closure: not-closed`.
`Report justification: new-mutation`.
Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification`.

Smallest next step after PASS: Orchestrator closure of this AP whole. Do not
close it yourself. Do not start FrameNest pin adoption.

## 8. Authority expiry

All publication authority expires at the terminal report.
