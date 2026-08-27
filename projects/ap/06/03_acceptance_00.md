# AP — Worker 03 fresh independent acceptance: Followable Spine and restatement conversion

You are one fresh Worker instance assigned to the AP `WORKER` role.

This is a read-only independent acceptance audit. You did not implement the
candidate; your independence comes from this fresh session, not from any
prior report. Native Plan Mode must not be used (`Native planning mode:
not-used`), and native planning is unnecessary for this audit.

Do not spawn subagents or delegate internally. Work as the one accountable
Worker. Read this prompt completely before acting.

**Independence discipline:** verify every control by direct repository
evidence you collect yourself. Do not read the implementation Worker's
terminal report (it is self-claims, not acceptance evidence). Do not treat
Orchestrator notes, chat narrative, or remembered conversation as evidence of
your verdict. The accepted plan is your fixed basis, not evidence of outcome.

---

## 1. Authoritative coordinates

```text
Persistent role identity: WORKER
Logical whole identity: ap-followable-spine-and-restatement-conversion
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Audit
Phase: Independent Audit
Task identity: AP-FOLLOWABLE-SPINE-ACCEPT-01
Native planning mode: not-used
Candidate under audit: 86ae6e8c27d2b919d776021bee915b7292908b0e
Baseline: eb3507bd1753e337ca7db92bb2da6cf7ec133071
Fixed review basis: /home/agile/meta/projects/ap/06/01_report_00.md (accepted plan, §1–§10, matrix P1–P7 / N1–N8)
Evidence posture: independent acceptance evidence
Independence required: yes (fresh session; did not implement the candidate)
Sub-agents/internal delegation: not-used
Worker topology: single-active
Working-copy topology: canonical-checkout (read-only inspection of /home/agile/Projects/ap)
Recommended reasoning: High
Recommendation basis: named risk — accepting a weakened or second-owned normative surface into the sole protocol; modality-preservation comparison requires sustained judgment
Escalation or downgrade gate: escalate only for a genuine unresolved contradiction; never infer Max or enhanced mode
Enhanced/maximum mode: not requested
Automatic model selection: off
Validation ladder: inspection and provenance required; existing focused tests none (ADR-0015); affected tests none; broad or full suite not-used
Repeated-gate stop: configured; unchanged failing gate is not-progress
Mutation authority: none — read-only audit; no file write, no Git write, no push, no checkout, no fetch
External trace disposition: not-used
Authority expiry: your acceptance authority expires at this exchange's terminal report
```

## 2. Gates (before the audit)

- Workdir `/home/agile/Projects/ap`; branch `feat/subagent-lifecycle-and-intuitive-mode`;
  HEAD must equal `86ae6e8c27d2b919d776021bee915b7292908b0e`; `git status
  --porcelain` empty. If HEAD differs or the tree is dirty: stop, report
  BLOCKED with observed values, audit nothing.

## 3. Audit task

Execute every control below by direct evidence (`git log`, `git diff`,
`git show eb3507bd…:<path>` for baseline comparison, file reads, seed-phrase
greps, link/anchor inspection, `wc -l`). Record observed evidence per control,
not conclusions alone.

**Positive controls (plan §9):**
- **P1** Spine subsection exists in AP.md; one row per role; every listed
  AP.md anchor resolves to a real heading.
- **P2** Detection-surface rule present in the detectability subsection; §19
  contains the new digest bullet; the emoji bullet (historical) is intact.
- **P3** Planning budget has exactly one normative home: seed grep
  ("one initial", "targeted revision", "second automatic", "plan-only cycle")
  over live `.md` surfaces returns only the owner, in-file digest, structural
  echoes, pointers with ≤1 orientation sentence, or frozen historical files
  (ADR bodies, CHANGELOG history).
- **P4** `00_notes.md` convention present in `AP_ORCHESTRATOR.md` and
  `ARTIFACT_LIFECYCLE.md`, each carrying the not-universal-grammar sentence
  ("not a universal AP field … its absence weakens no AP rule" or equivalent
  exact text).
- **P5** ADR-0021 Appendix A: coverage route stated; per-surface class
  1/2 counts; class 3 complete per-item (D-01 with disposition and reason);
  worked examples for each class present.
- **P6** ADR-0021 exists; ADR index has its row; CHANGELOG has the Unreleased
  entry; all three consistent with the actual diff.
- **P7** Appendix B conversion map covers every conversion actually present in
  `git diff eb3507bd..86ae6e8` (claimed 25 rows — verify the count yourself).

**Negative controls (plan §9):**
- **N1** No new/changed normative sentence in a non-owner file lacks an owner
  link (review the full diff normative-looking additions).
- **N2** Modality preservation: for a minimum sample — all named planning-budget
  conversion surfaces, freshness, closure-signal, omitted-permission — compare
  each converted surface against its owner (must/never/only modality, scope,
  exception carve-outs). Identical force required; any weakening is a FAIL.
- **N3** `git diff --name-only` contains only allowed paths; zero changes to
  `ap`, `ap.project.conf`, FrameNest paths, managed-block content, ADR bodies
  0004–0020.
- **N4** Diff contains only `.md` changes; no script, test, CI, or executable
  change.
- **N5** No new role, profile, phase, or universal required filename; notes
  text carries the not-universal qualifier.
- **N6** Every class-3 disposition has a recorded promotion attempt before
  demotion and a reason; no safety-adjacent rule demoted silently.
- **N7** `wc -l INTUITION.md` ≤ 200.
- **N8** No unresolved owner contradiction introduced (spot-check: spine text
  vs owner map; detectability classes vs RF capsules; conversion rule vs §19
  digest convention).

## 4. Negative authority

Omitted permission is not implied permission. No mutation of any kind: no
file write/create/delete, no Git write, no push, no fetch, no checkout, no
config change, no network call, no FrameNest or Meta access beyond the named
plan file, no subagents, no implementation, no prompt issuance, no closure
claim.

## 5. Report contract

Terminal report begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

with coordinates echoed (03/01), a per-control table (control → observed
evidence → verdict), an explicit independence statement (fresh session; did
not implement; did not reuse session-02 claims), `Standard terminal status`
PASS/PARTIAL/BLOCKED, `Phase-qualified result: acceptance-PASS` only if every
control holds, `Logical-whole closure: not-closed`,
`Report justification: new-evidence`, and authority expiry. Any FAIL or
cannot-verify is exact evidence for the Orchestrator, never a silent pass.
