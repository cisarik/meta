# Fresh Independent Re-Audit prompt — AP update candidate d7023cf

You are a genuinely fresh Fresh Independent Re-Audit Worker for the canonical
Analytic Programming repository.

This is a full read-only independent re-acceptance of the corrected candidate.
You did not plan, implement or correct it. The implementation, acceptance and
correction reports are claims to verify, not evidence to trust.

```text
Persistent role identity: WORKER
Worker session profile: Fresh Independent Re-Audit
Worker session target: fresh-worker-session
Native planning mode: not-used
Phase: Independent Audit
Task identity: AP-MO-04 — fresh independent re-audit of AP candidate d7023cf

Logical whole identity: master-orchestrator-and-report-persistence
Worker session ordinal: 04
Worker exchange ordinal: 01

Delivery route: manual Cooperator delivery
Reasoning recommendation: High — full re-acceptance of a corrected change to the sole normative protocol and its consumer pin
Recommended context capacity: approximately 250k tokens
Independence required: yes — fresh session, no planning, implementation or correction participation

Report persistence owner: assigned WORKER
Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/04_report_00.md
Git authority: read-only; no tag, branch, remote or config mutation; read-only branch and remote inspection is allowed
```

Before substantive work, confirm that you are in a genuinely fresh session that
did not plan, implement or correct the candidate. Do not read any implementation
or correction Worker chat transcript or reasoning. Your package is the candidate,
the approved plan, the implementation report, the acceptance report, the
correction report, the two prompts and the Cooperator decisions. If you discover
inherited implementation or correction context, stop and return `BLOCKED`; do
not claim independence you do not have.

This is the one correction re-acceptance allowed by the plan. A new material
finding is escalated to the Orchestrator and Cooperator; do not start a second
correction.

## 1. Authority and boundaries

```text
Positive authority
- Read-only inspection of /Users/agile/Projects/ap at the corrected candidate,
  the correction base and the original base, and of the trace package under
  /Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/.
- Read-only Git inspection: rev-parse, status, log, show, diff, ls-tree,
  ls-remote, cat-file, branch --show-current, remote -v, and similar
  non-mutating reads.
- Read-only shell text inspection: rg, grep, sed, tr, wc, sort, uniq, test -e,
  head, dirname, test -x, test -d.
- Read-only AP executable checks: sh -n ap, ./ap --help, ./ap bundle --help, and
  the read-only ./ap project check diagnostic in V12.
- Exact direct-write of the terminal report at the path above, if and only if
  that file is absent, followed by a complete readback.

Negative authority
- No edit, creation, deletion, rename, or chmod in AP, Kronika or Meta except
  the one report file.
- No git add, commit, push, fetch, pull, merge, rebase, reset, restore, clean,
  stash, checkout, switch, tag, branch, remote, or config mutation. Read-only
  `git branch --show-current` and `git remote -v` are permitted.
- No correction, repair, or reimplementation. An auditor that repairs its own
  finding destroys the independence of the audit.
- No AP publication, Kronika pin, Meta projection, deployment, NUC, host,
  provider, browser, account, or secret/credential/token/private-key/cookie/
  private-host-value inspection.
- No product tests, build, deployment helper, or NUC command.
- No new test suite, broad suite, or environment repair.
- No fourth role, historical ADR rewrite, or mass rename.
- No reopening of A-4/A-5/A-6/A-7 unless the correction introduced a new
  material defect in them.
```

The report write is the only file write and is authorized by
`Trace persistence`, not by a repository allowlist. If the exact report path
exists, including an empty file, stop and return `BLOCKED` without overwriting.

## 2. Candidate and package

```text
Corrected candidate: d7023cf037f6d17885c3ede5c04812c61640da50
Correction base:     fe1e58d9c3f074b50eda0ebd7df76e4002326953
Original base:      73e20ef80b88700d5fcbc397cd8edd4fc425869f
AP repository:      /Users/agile/Projects/ap (main)
Public main:        73e20ef80b88700d5fcbc397cd8edd4fc425869f (the candidate is local and not published)
Kronika:            7ee4684f529b3d2cdf15ce30902ba01a2b39992c, .ap 73e20ef (not part of this re-audit)
```

Trace package to read:

```text
01_report_00.md          approved plan and acceptance criteria
02_implementation_00.md  implementation prompt
02_report_00.md          implementation report (claims)
03_acceptance_00.md      original acceptance prompt
03_report_00.md          original acceptance report (PARTIAL; A-1..A-7)
02_correction_01.md      bounded correction prompt
02_report_01.md          correction report (claims)
```

Cooperator decisions:

```text
Plan gate: A approved.
CD-1 session scope accepted.
CD-2 K1 standing maintenance accepted.
CD-3 overridden: the Cooperator commits and pushes the Kronika pin; later.
CD-4 accepted: the pilot is a Fresh Evidence Probe Worker; later.
CD-5 axes mandatory accepted.
CD-6 run map required accepted.
```

Verify the candidate independently before reading its diff:

```text
git rev-parse HEAD                 -> d7023cf...
git log -1 --format='%H %P %s'     -> one commit, parent fe1e58d9, local on main
git rev-list --count 73e20ef..HEAD -> 2
git status --porcelain=v1          -> clean
git branch --show-current          -> main
git ls-remote origin refs/heads/main -> 73e20ef (candidate not published)
git diff --name-status 73e20ef..d7023cf -> exactly the 13 M + 1 A cumulative paths
git diff --name-status fe1e58d9..d7023cf -> exactly the five correction paths
```

A different candidate, parent, branch, public main, or dirty tree is a new
state. Stop and report; do not reconcile it by mutation.

## 3. Governing protocol and scope

The governing AP for this re-audit is `73e20ef`, the current pin. The candidate's
AP.md text is the **object under review**, not the protocol that governs your
acceptance. Because the worktree is at the corrected candidate, read the
governing AP with `git show 73e20ef:AP.md` and the other `73e20ef` files; do not
mistake the candidate's AP.md for the governing text. Do not use the candidate
to excuse a defect in itself.

This is a **full** fresh re-acceptance, not a scoped re-acceptance: the
correction changed exact structural and persistence semantics in the sole
normative protocol. It covers the cumulative candidate against `73e20ef` and
the correction against `fe1e58d9`.

## 4. Acceptance criteria

Accept the exact corrected candidate only if all of these hold:

1. **Three roles preserved.** Exactly COOPERATOR, ORCHESTRATOR and WORKER. The
   Master Orchestrator is an Orchestrator session scope, not a fourth role; it
   grants no authority by itself; it never selects, plans, accepts or closes a
   whole; a run-scoped session may prompt only for a whole it opened as that
   whole's Orchestrator after Cooperator selection, recording the departure.
2. **Run map and provisional handout.** AP.md and AP_ORCHESTRATOR.md define the
   run map, the provisional `00_handout.md`, the per-whole handout revalidation
   record, the frozen-after-open rule, the supersession rule, and the boundary
   that a run map or provisional handout is never selection, plan or authority.
3. **Report persistence and axes.** AP.md, AP_WORKER.md and PROMPT_CONTRACTS.md
   define direct-write report persistence and the three mutation axes. The
   existing `Report persistence owner` plus the axes are used; no `Report
   author`/`Report persister` fields are added. The corrected P1/P2 scope the
   report-only restriction correctly: P1 includes the report destination and
   separately grants any other trace path; P2 names no report destination but
   does not forbid a separately granted non-report trace path. The completion
   repair, Worker handout, notes and specialist asset routes remain lawful.
4. **Satisfiability and blocked exchange.** AP.md §7 defines the four
   comparisons and the Worker stop; RF-19 and Planning Budget define consumed
   coordinates and the corrected `02/01` initial Planner. A new logical-whole
   identity is lawful only for a materially changed objective, never a
   coordinate reset.
5. **Standing AP maintenance.** AP.md §13 defines the consumer-neutral standing
   ledger duty; storage stays in the consuming repository; no Meta path or trace
   becomes a discovery source; RF-09 remains the semantic owner.
6. **ADR and changelog.** ADR-0026 and the CHANGELOG entry exist; the ADR index
   row exists; historical ADR bodies 0004–0025 are unchanged. ADR-0026 records
   the corrected count of trace-specific passages and the AP §13 snapshot
   supersession.
7. **Compatibility.** `ap` is executable; `ap`, `ap.project.conf`, `INFOSEC.md`,
   `PROMPT_ENGINEERING_PATTERNS.md` and `.gitignore` are unchanged; schema v1,
   the managed `AGENTS.md` block, and the `init`/`doctor`/`project`/`exec`/
   `update`/`bundle` contracts are unchanged.
8. **Documentation coherence.** Links, anchors and headings resolve; no new
   duplicate heading slug; the accepted `run-level-handouts` explicit-id/slug
   overlap remains the only such case; the new rules are stated once in AP.md
   and projected as pointers plus at most one orientation sentence.
9. **Plan fidelity.** The cumulative candidate implements the approved plan's
   sections E.1–E.3, H, I, J and K, with the Orchestrator conditions and the
   A-1/A-2/A-3 corrections. It does not implement the Meta projections, the
   Kronika pin, the test-constant edit or the pilot. It does not add P20,
   `Report author`/`Report persister` fields, `correction-required` to AP enums,
   or a new `ap` command/schema/test suite.
10. **Correction fidelity.** The correction commit changes exactly five paths:
    `AP.md`, `PROMPT_CONTRACTS.md`, `AP_WORKER.md`, `AP_ORCHESTRATOR.md`, and
    ADR-0026. It does not change CD-1..CD-6, the three roles, the run map model,
    the mutation axes, the satisfiability check, the consumed-coordinate rule,
    the standing maintenance duty, or a historical ADR body.

Later exchanges remain pending by plan and are not candidate failures: the Meta
projections, AP publication, the Kronika pin (including
`tests/contract/test_ap_integration.py` line 10), and the pilot.

## 5. Findings to verify

Verify each original acceptance finding and the correction report's response:

```text
A-1  material  P1/P2/direct-write over-restriction. Verify:
               - AP.md says "does not write that report to the trace";
               - P1 includes the report destination and separately grants any
                 other trace path;
               - P2 names no report destination;
               - AP_WORKER says "no file outside the granted Trace persistence";
               - the persister routes (completion repair, Worker handout, notes,
                 specialist asset) remain lawful;
               - S15 and S16 pass.
A-2  minor     Verify "an activated trace alone" in AP_ORCHESTRATOR.md and the
               corrected "six" count in ADR-0026; case-insensitive meta check;
               the fenced meta_exchange_index example is not a defect.
A-3  minor     Verify AP_ORCHESTRATOR step 6: "refresh or supersede ... and
               record any Cooperator drop as `dropped`"; it matches AP.md.
A-4  info      Duplicate run-level-handouts anchor accepted; no correction.
A-5  info      AP §1/RF-15 suffice for the consumer-file atomic-pin item.
A-6  info      MEASURED-1 is a prompt defect, not a candidate defect.
A-7  info      ADR-0026 cites AP §13; no ADR body changed.
```

Correction report LEAD items:

```text
LEAD-1  P1 retains "; positive authority grants each write". Decide whether
        that retained clause is the intended reading.
LEAD-2  Use full-SHA two-dot ranges in this re-audit; do not read an abbreviated
        SHA plus three dots as a range accidentally.
```

The implementation and correction prompts are in the package. Use them to
verify the prompt-defect claims and the correction fidelity; do not treat them
as authority.

## 6. Validation — run and report exactly

Run from `/Users/agile/Projects/ap`. Use full-SHA two-dot ranges.

```text
V1  git rev-parse HEAD; git log -1 --format='%H %P %s'; git status --porcelain=v1;
    git rev-list --count 73e20ef80b88700d5fcbc397cd8edd4fc425869f..d7023cf037f6d17885c3ede5c04812c61640da50;
    git branch --show-current; git ls-remote origin refs/heads/main
    -> d7023cf..., parent fe1e58d9, count 2, main, public main 73e20ef, clean
V2  git diff --name-status 73e20ef80b88700d5fcbc397cd8edd4fc425869f..d7023cf037f6d17885c3ede5c04812c61640da50
    -> exactly the cumulative 13 M + 1 A paths
    git diff --name-status fe1e58d9c3f074b50eda0ebd7df76e4002326953..d7023cf037f6d17885c3ede5c04812c61640da50
    -> exactly the five correction M paths
V3  git diff --check 73e20ef..d7023cf; git diff --check fe1e58d9..d7023cf
    -> clean
V4  git diff --quiet 73e20ef..d7023cf -- ap ap.project.conf INFOSEC.md PROMPT_ENGINEERING_PATTERNS.md .gitignore
    -> exit 0
    git diff --quiet fe1e58d9..d7023cf -- CHANGELOG.md docs/adr/README.md
    -> exit 0
V5  git diff --name-only 73e20ef..d7023cf -- docs/adr -> 0026 and README.md
    git diff --name-only fe1e58d9..d7023cf -- docs/adr -> only 0026
    git diff --name-only 73e20ef..d7023cf -- docs/adr | grep -v '0026-' | grep -v 'README.md'
    -> empty (no historical ADR body changed)
V6  sh -n ap; ./ap --help; ./ap bundle --help; test -x ap
    -> exit 0 each
V7  Link and anchor check over the changed files in both ranges:
    relative targets; test -e; every #anchor matches an explicit <a id> or a
    heading slug. Confirm the accepted run-level-handouts overlap and no new
    unresolved link or anchor.
V8  Heading slugs per changed file; sort | uniq -d -> no new duplicate.
V9  (a) each section-I definition appears once in PROMPT_CONTRACTS and verbatim
        elsewhere;
    (b) rg -n -i 'report persister|report author:' -> only ADR-0026 alternatives;
    (c) rg -n -i -w 'meta' --glob '!docs/adr/**' --glob '!CHANGELOG.md'
        -> no trace-implementation name outside the labelled fenced
           meta_exchange_index example;
    (d) rg -n 'persister' AP.md PROMPT_CONTRACTS.md -> the nine lawful routes;
    (e) rg -n 'writes no trace file|and nothing else|Trace persistence: none;|names exactly the report destination'
        in the five corrected files -> no residual restrictive wording.
V10 Single-owner review of both diffs:
    every new or changed normative sentence remains in AP.md with Detection;
    projections are pointers plus at most one orientation sentence; A-3 matches
    AP.md's Cooperator drop authority; the correction does not create a second
    owner.
V11 Scenario walk-through S1–S16 from the original acceptance matrix:
    S1–S14 plus S15 (completion-repair Worker persists a predecessor artifact
    plus its own report) and S16 (Worker-authored handout with its own grant
    and a relayed report). Record the candidate evidence for each.
V12 ./ap project check --root /Users/agile/Projects/ap --baseline 73e20ef80b88700d5fcbc397cd8edd4fc425869f
    -> expected trusted-baseline line then declared-CPython ERROR; record the
       limitation class, not a host path; not repaired.
```

Do not run a broad suite, Kronika checks, the pin sequence, the pilot, a browser,
a provider, or a NUC command. No test suite exists.

## 7. Findings and verdict

Produce a finding table:

```text
ID | Severity | Finding | Evidence | Smallest correction | Owner
```

Severity: `blocker`, `material`, `minor`, `info`. A finding must cite the exact
file, heading, anchor or command output. Do not manufacture a finding. If a
previous finding is resolved, say `resolved` with the evidence.

Verdict:

```text
PASS      every acceptance criterion holds; no blocker or material finding.
          Phase-qualified result: acceptance-PASS.
PARTIAL   at least one material finding remains. Phase-qualified result:
          not-applicable. Escalate; this is the one correction re-acceptance.
BLOCKED   candidate identity/package unverifiable, independence compromised, or
          a blocker prevents acceptance. Phase-qualified result:
          not-applicable.
```

A second correction requires a Cooperator decision. The auditor never repairs
its own finding.

## 8. Report contract

Write your terminal report directly to:

```text
/Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/04_report_00.md
```

The report must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

It must echo the logical-whole identity, Worker session ordinal, and Worker
exchange ordinal. It must include:

```text
1  Coordinates.
2  Status: PASS, PARTIAL, or BLOCKED.
3  Phase-qualified result: acceptance-PASS for PASS; not-applicable otherwise.
4  Candidate d7023cf..., correction base fe1e58d9..., original base 73e20ef...
5  Changed files and purpose: the report only; the candidate inspected read-only.
6  Tests and validation: V1–V12 exact commands and results; S1–S16; findings.
7  Commit and push result: none.
8  Deviations, risks, or missing evidence.
9  One smallest next step: publication of the exact candidate, or escalation
   with the exact remaining finding and missing evidence.
10 Exactly one report justification: final-acceptance.
11 Authority-expiry statement.
12 Compact critique:
   Orchestration critique:
   MEASURED: none | <verified finding; evidence; effect; smallest correction>
   LEAD: none | <unverified possibility; cheapest useful check>
13 Resolved Execution Issues / Near-Misses: none | <exact>
14 Pre-Existing Failure Classification: none | <complete; V12 is pre-existing>
15 Independence statement: fresh session, no planning/implementation/correction
   participation, no inherited transcript or reasoning.
16 Logical-whole closure: not-closed.
```

The report must state that it does not publish, pin, project, deploy or close.
Read the report back completely; verify its first line, coordinates, content and
path. Then send a short terminal notice with the status, corrected candidate SHA,
exact report path, and any requested hash. Do not paste the report back into chat
as a substitute for the file.

## 9. Stop conditions

Stop and return `BLOCKED` or `PARTIAL` without substantive acceptance if:

- the candidate is not `d7023cf`, the parent is not `fe1e58d9`, the tree is
  dirty, the candidate is not on `main`, or public main is not `73e20ef`;
- you inherited implementation or correction context or cannot establish
  independence;
- a required source is missing or contradictory;
- the report destination already exists, the parent is not the exact verified
  directory, or the client cannot write the report through a permitted route;
- a finding would require an edit, correction, Git write, pin, publication,
  deployment, NUC/host/provider/browser/secret contact, or a forbidden command;
- a second correction would be needed. Return
  `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and name the finding.

Do not repair the candidate, environment, prompt, or plan. Preserve the first
causal failure and report the exact blocker.

## 10. Prompt satisfiability check

```text
VALIDATION–AUTHORITY  every V1–V12 command is inside the positive authority;
                      no negative clause forbids the report write or read-only
                      branch/remote inspection.
ROUTING               one concrete value per identity/route field; full SHAs;
                      fresh session 04.
PERSISTENCE           report persistence owner assigned WORKER; direct-write
                      exact path; repository mutation none; host/remote none;
                      trace direct-write; Git read-only.
SPELLING              paths, profile, commands and the full-SHA ranges come from
                      their durable owners and the correction report.
```

If you find a defect in this grant, report it under `Orchestration critique`
with MEASURED or LEAD. If it prevents a lawful re-audit, stop `BLOCKED`; do not
improvise around it.

## 11. Authority expiry

This re-audit grant expires at your terminal report, cancellation, or
supersession. It grants no correction, publication, pin, Meta projection,
deployment or closure authority. The Orchestrator decides the next step from
your report. The Cooperator is not a copy-paste courier: write the report to the
exact trace path, read it back, send only the short terminal notice, and stop.
