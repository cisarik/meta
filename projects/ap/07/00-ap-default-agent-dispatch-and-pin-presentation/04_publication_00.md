# WORKER TASK — Publication: Default Agent Dispatch, Companion Integrity, and Pin Presentation

You are one fresh Worker instance assigned to the AP `WORKER` role.

This is a bounded publication task: exactly one ordinary non-force push of an
independently accepted candidate to the public AP `main`, followed by a
credential-free public readback. Native Plan Mode must not be used for this
exchange (`Native planning mode: not-used`).

Cooperator publication authorization: granted explicitly by Michal
(„publikovať", 2026-08-28), held conditional on fresh independent acceptance,
which completed as `acceptance-PASS` (session 03) over candidate
`2fbf8d3fa4699d1af073dcbf135c4f11789fdcd4`. This prompt executes that grant
and nothing else.

Read this prompt completely before acting. Do not spawn subagents or delegate
internally. Work as the one accountable Worker.

---

## 1. Authoritative coordinates

```text
Persistent role identity: WORKER
Logical whole identity: ap-default-agent-dispatch-and-pin-presentation
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Publication Worker
Phase: Publication
Task identity: AP-DEFAULT-DISPATCH-AND-PIN-PRESENTATION-PUB-01
Native planning mode: not-used
Candidate: 2fbf8d3fa4699d1af073dcbf135c4f11789fdcd4
Expected pre-push public main: 86ae6e8c27d2b919d776021bee915b7292908b0e
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
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/ap/07/00-ap-default-agent-dispatch-and-pin-presentation/
Trace project key: ap
Trace logical-whole projection identity: ap-default-agent-dispatch-and-pin-presentation
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Downloadable prompt filename: 04_publication_00.md
Destination path: /home/agile/meta/projects/ap/07/00-ap-default-agent-dispatch-and-pin-presentation/
Archival: wait-for-report
Authority expiry: your publication authority expires at this exchange's terminal report
```

---

## 2. Preconditions (all must hold before the push; else BLOCKED)

1. Workdir `/home/agile/Projects/ap`; branch `feat/subagent-lifecycle-and-intuitive-mode`;
   HEAD equals `2fbf8d3fa4699d1af073dcbf135c4f11789fdcd4`; `git status --porcelain` empty.
2. Credential-free `git ls-remote https://github.com/cisarik/ap.git refs/heads/main`
   returns exactly `86ae6e8c27d2b919d776021bee915b7292908b0e`.
3. `git merge-base --is-ancestor 86ae6e8c27d2b919d776021bee915b7292908b0e HEAD`
   succeeds.

If any precondition fails: stop, report BLOCKED with the observed values,
change nothing, push nothing.

---

## 3. Authority (exactly this)

- The single push command:

```sh
git -C /home/agile/Projects/ap push --porcelain origin 2fbf8d3fa4699d1af073dcbf135c4f11789fdcd4:refs/heads/main
```

- Then the public readback:

```sh
git ls-remote https://github.com/cisarik/ap.git refs/heads/main
```

Negative: force-push, deleting refs, touching any other remote/branch/ref,
modifying any repository files, creating commits, modifying FrameNest,
modifying Meta trace files.

---

## 4. Report Contract

Terminal report begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo once, unchanged:

```text
Logical whole identity: ap-default-agent-dispatch-and-pin-presentation
Worker session ordinal: 04
Worker exchange ordinal: 01
```

Include compact core:
- `Standard terminal status: PASS` (or BLOCKED)
- `Phase-qualified result: publication-PASS`
- Start commit: `2fbf8d3fa4699d1af073dcbf135c4f11789fdcd4`
- End commit: `2fbf8d3fa4699d1af073dcbf135c4f11789fdcd4`
- Changed files: none
- Verbatim push output and public readback output
- Commit and push: push executed to `origin:refs/heads/main`
- Deviations / risks: none
- One smallest next step: Orchestrator closure of the logical whole
- Report justification: `changed-external-state`
- Authority expiry statement
- `Logical-whole closure: not-closed`

Authority expires at the terminal report.
