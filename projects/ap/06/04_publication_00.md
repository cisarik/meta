# AP — Worker 04 publication: Followable Spine and restatement conversion

You are one fresh Worker instance assigned to the AP `WORKER` role.

This is a bounded publication task: exactly one ordinary non-force push of an
independently accepted candidate to the public AP `main`, then a
credential-free public readback. Native planning mode must not be used
(`Native planning mode: not-used`).

Cooperator publication authorization: granted by Michal („publikovať",
2026-08-27), held conditional on fresh independent acceptance, which completed
as `acceptance-PASS` (session 03) over candidate `86ae6e8c27d2b919d776021bee915b7292908b0e`.
This prompt executes that grant and nothing else.

Read this prompt completely before acting. Do not spawn subagents. Work as
the one accountable Worker.

---

## 1. Authoritative coordinates

```text
Persistent role identity: WORKER
Logical whole identity: ap-followable-spine-and-restatement-conversion
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Publication Worker
Phase: Publication
Task identity: AP-FOLLOWABLE-SPINE-PUB-01
Native planning mode: not-used
Candidate: 86ae6e8c27d2b919d776021bee915b7292908b0e
Expected pre-push public main: eb3507bd1753e337ca7db92bb2da6cf7ec133071
Evidence posture: non-independent implementation evidence (publication execution)
Independence required: no (acceptance already established by fresh session 03)
Sub-agents/internal delegation: not-used
Worker topology: single-active
Working-copy topology: canonical-checkout (/home/agile/Projects/ap)
Recommended reasoning: Medium
Recommendation basis: single deterministic push with hard preconditions; no design judgment
Escalation or downgrade gate: any precondition mismatch is BLOCKED, never a rebase or repair
Enhanced/maximum mode: not requested
Automatic model selection: off
Validation ladder: selected
Inspection and provenance: required (verbatim command outputs)
Existing focused tests: none (ADR-0015)
Affected tests: none
New causal regression: pushing a wrong or stale ref, force-push, or touching another ref
Broad or full suite: not-used
Runtime or testbed: not-used
Independent acceptance: not-required (publication execution of an accepted candidate; Orchestrator verifies readback independently)
Repeated-gate stop: configured; failing precondition is not-progress
External trace disposition: not-used
Authority expiry: your publication authority expires at this exchange's terminal report
```

## 2. Preconditions (all must hold before the push; else BLOCKED)

1. Workdir `/home/agile/Projects/ap`; branch `feat/subagent-lifecycle-and-intuitive-mode`;
   HEAD equals `86ae6e8c27d2b919d776021bee915b7292908b0e`; `git status
   --porcelain` empty.
2. Credential-free `git ls-remote https://github.com/cisarik/ap.git refs/heads/main`
   returns exactly `eb3507bd1753e337ca7db92bb2da6cf7ec133071`.
3. `git merge-base --is-ancestor eb3507bd1753e337ca7db92bb2da6cf7ec133071 HEAD`
   succeeds.

If any precondition fails: stop, report BLOCKED with the observed values,
change nothing, push nothing.

## 3. Authority (exactly this)

- The single command:

```sh
git push --porcelain origin 86ae6e8c27d2b919d776021bee915b7292908b0e:refs/heads/main
```

- Then the readback:

```sh
git ls-remote https://github.com/cisarik/ap.git refs/heads/main
```

## 4. Negative authority (omitted permission is not implied permission)

No force push, no second push, no other ref, no tags, no rebase/merge/amend,
no Git config change, no checkout/fetch/stash, no FrameNest or Meta access,
no file write, no publication claim beyond the readback. If the push is
rejected for any reason: stop, report the verbatim rejection, change nothing.

## 5. Report contract

Terminal report begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

with coordinates echoed (04/01), verbatim push output, verbatim readback,
`Standard terminal status: PASS`, `Phase-qualified result: publication-PASS`
only if the readback equals `86ae6e8c27d2b919d776021bee915b7292908b0e`,
`Logical-whole closure: not-closed`, `Report justification: new-mutation`,
and authority expiry. No closure claim; closure is the Orchestrator's
Cooperator-gated step.
