# Authoritative Worker prompt — Kronika whole 09, Worker session 02, exchange 04

Activation: this file is the exact issued Worker prompt for the logical whole
`timeline-complete-chronicle`. It is stored under the Meta filename mapping
`<worker-session>_<phase>_<meta-exchange-index>.md` as
`02_correction_03.md`. The matching terminal report is `02_report_03.md`.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: timeline-complete-chronicle
Worker session ordinal: 02
Worker exchange ordinal: 04
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Correction
Task identity: KRN-TCC-CORR-03 — align the stale SERVER.md Timeline sentence with ADR-0087
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard — one documentation sentence in one durable owner
Recommended context capacity: approximately 250k tokens
Independence required: no
Continuity anchor: terminal re-acceptance report 04_report_00.md and candidate commit 1bc10a364ddf3fba15fad62e9036183ab75e1a46
Authority renewal: prior implementation/correction authority expired; this prompt grants a new bounded documentation-only correction
Evidence posture: non-independent documentation correction; the Orchestrator verifies the exact sentence and records a scoped reconciliation
```

You are continuing the healthy same Worker session that produced candidate
`1bc10a364ddf3fba15fad62e9036183ab75e1a46`. The prior authority expired. This
prompt grants a new, complete, bounded documentation correction. Retained
context is convenience, not authority; re-gate the repository and stop on any
conflict with current evidence.

Before substantive work, confirm that `Native planning mode: not-used` is the
actual client state (native Plan mode OFF). If it is enabled, stop and return
`BLOCKED` naming the contradiction.

## 1. Confirmed finding

Fresh re-acceptance `04_report_00.md` passed C01–C24 and both corrected UI
claims, but found one stale documentation sentence. `SERVER.md` lines 85–87
currently say:

```text
The shared Timeline does not receive a card until an administrator approves the
completed record.
```

That sentence equates Timeline membership with administrator approval. It
contradicts the same file's boundary paragraph at lines 115–121 and accepted
ADR-0087: the Timeline is the complete authorized read projection; the owner and
application administrators see their authorized private/unfinished work, while
another household member sees only an approved projection or unbound legacy
publication. The sentence is unchanged from the public baseline and is a
documentation contradiction, not a runtime or authorization defect.

## 2. Exact correction

Change only `SERVER.md`. Replace the stale sentence with one sentence that
matches the existing boundary paragraph and ADR-0087, for example:

```text
Another household member does not see the completed record in the shared
Timeline until an administrator approves it; the owner and application
administrators see their authorized work in the chronicle.
```

Do not change any other sentence, heading, code block, route description or
document. Do not introduce a new product rule, a new semantic owner, a capability
change or a Timeline behavior change. If the surrounding paragraph needs a
minimal wording connection to stay grammatical, make only that minimal
adjustment and report it.

## 3. Baseline and authority

```text
Repository: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Expected branch: main
Baseline commit under test: 1bc10a364ddf3fba15fad62e9036183ab75e1a46
Parent of the correction commit: 1bc10a364ddf3fba15fad62e9036183ab75e1a46
Public main: b66ec8f50860ace624f6be1fd3ad63f521edcd33
Containing-repository .ap gitlink: d7023cf037f6d17885c3ede5c04812c61640da50
Submodule HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
```

Verify `git rev-parse HEAD`, `git status --short` and `git log --oneline -2`.
Stop if the worktree is not clean or HEAD is not `1bc10a3`. The only allowed
edit is `SERVER.md`. No code, test, schema, migration, route, policy, ADR or
other documentation path may change.

## 4. Validation

Documentation-only change. Run:

```text
git diff --check
git diff --stat
git status --short
```

No product test suite is required for this one-sentence documentation
correction. If the diff touches any other path or changes more than the stale
sentence/its grammatical connection, stop and report.

## 5. Commit and report

After the diff check is clean, stage exactly `SERVER.md` and create one
corrective documentation commit:

```text
git add -- SERVER.md
git diff --cached --check
git commit -m "docs: align SERVER Timeline wording with ADR-0087"
git show --stat --oneline HEAD
```

Do not push.

Write the terminal report to:

```text
/Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_report_03.md
```

The report starts exactly with `### Report for ORCHESTRATOR_CHAT`, echoes the
coordinates and role fields, and contains:

```text
status: PASS
Phase-qualified result: implementation-PASS
Start commit: 1bc10a364ddf3fba15fad62e9036183ab75e1a46
End commit: <documentation correction SHA>
Report justification: new-mutation
Logical-whole closure: not-closed
```

Include the finding, the exact old and new sentence, the changed path and diff
stat, the diff-check result, the commit SHA, any deviation or residual risk,
`Resolved Execution Issues / Near-Misses`, `Pre-Existing Failure Classification`,
one smallest next step, and the orchestration critique. Do not claim acceptance,
publication, deployment or closure.

## 6. Delivery and trace

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/
Trace project key: kronika
Trace logical-whole projection identity: 09-timeline-complete-chronicle
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_correction_03.md
Destination path: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/
Report filename: 02_report_03.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: SERVER.md only
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_report_03.md
```

If the report path exists, including an empty file, stop `BLOCKED` without
overwriting it.

## Visible delivery capsule

```text
🟡 Ready for delivery
Recipient: Bounded Correction Worker · current-worker-session · manual
Recommendation: Standard · approximately 250k tokens
Client: Native Plan Mode OFF
Prompt: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_correction_03.md
Report: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_report_03.md
Archival: wait-for-report
```
