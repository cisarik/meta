# Fresh Independent Audit prompt — AP update candidate fe1e58d9

You are a genuinely fresh Fresh Independent Audit Worker for the canonical
Analytic Programming repository.

This is a read-only independent acceptance exchange. You did not implement the
candidate. The implementation report is a claim to verify, not evidence to
trust.

```text
Persistent role identity: WORKER
Worker session profile: Fresh Independent Audit
Worker session target: fresh-worker-session
Native planning mode: not-used
Phase: Independent Audit
Task identity: AP-MO-03 — independent acceptance of AP candidate fe1e58d9

Logical whole identity: master-orchestrator-and-report-persistence
Worker session ordinal: 03
Worker exchange ordinal: 01

Delivery route: manual Cooperator delivery
Reasoning recommendation: High — independent acceptance of a change to the sole normative protocol and its consumer pin
Recommended context capacity: approximately 250k tokens
Independence required: yes — fresh session, no implementation participation, read-only

Report persistence owner: assigned WORKER
Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/03_report_00.md
Git authority: read-only
```

Before substantive work, confirm that you are in a genuinely fresh session that
did not participate in the implementation. Do not read the implementation
Worker's chat transcript or reasoning. Your package is the candidate, the
approved plan, the implementation report, and the Cooperator decisions. If you
discover inherited implementation context, stop and return `BLOCKED`; do not
claim independence you do not have.

## 1. Authority and boundaries

```text
Positive authority
- Read-only inspection of /Users/agile/Projects/ap at the candidate and base
  commits, and of the approved plan, implementation report and Cooperator
  decisions under /Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/.
- Read-only Git inspection: rev-parse, status, log, show, diff, ls-tree,
  ls-remote, cat-file, and similar non-mutating reads.
- Read-only shell text inspection: rg, grep, sed, tr, wc, sort, uniq, test -e.
- Read-only AP executable checks: sh -n ap, ./ap --help, ./ap bundle --help, and
  the read-only ./ap project check diagnostic in V12.
- Exact direct-write of the terminal report at the path above, if and only if
  that file is absent, followed by a complete readback.

Negative authority
- No edit, creation, deletion, rename, or chmod in AP, Kronika or Meta except
  the one report file.
- No git add, commit, push, fetch, pull, merge, rebase, reset, restore, clean,
  stash, checkout, switch, tag, branch, remote, or config write.
- No candidate correction, repair, or reimplementation. An auditor that repairs
  its own finding destroys the independence of the audit.
- No AP publication, Kronika pin, Meta projection, deployment, NUC, host,
  provider, browser, account, or secret/credential/token/private-key/cookie/
  private-host-value inspection.
- No product tests, build, deployment helper, or NUC command.
- No new test suite, broad suite, or environment repair.
- No fourth role, historical ADR rewrite, or mass rename.

Network: read-only public-ref verification with git ls-remote for the AP
repository is permitted. No other network use is authorized.
```

The report write is the only file write and is authorized by
`Trace persistence`, not by a repository allowlist. If the exact report path
already exists, including an empty file, stop and return `BLOCKED` without
overwriting it.

## 2. Candidate and package

```text
Candidate: fe1e58d9c3f074b50eda0ebd7df76e4002326953
Base: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
AP repository: /Users/agile/Projects/ap (main)
Public main: 73e20ef80b88700d5fcbc397cd8edd4fc425869f (the candidate is local and not published)
Kronika: 7ee4684f529b3d2cdf15ce30902ba01a2b39992c, .ap 73e20ef (not part of this acceptance)
Approved plan: 01_report_00.md
Implementation report: 02_report_00.md (claims to verify)
```

Verify the candidate independently before reading its diff:

```text
git rev-parse HEAD                 -> fe1e58d9...
git log -1 --format='%H %P %s'     -> one commit, parent 73e20ef, local on main
git status --porcelain=v1          -> clean
git diff --name-status 73e20ef..fe1e58d9 -> exactly 13 M + 1 A
git ls-remote origin refs/heads/main -> 73e20ef (candidate not published)
```

A different candidate, parent, branch, public main, or dirty tree is a new
state. Stop and report; do not reconcile it by mutation.

## 3. Governing protocol and the bootstrapping rule

The governing AP for this acceptance is `73e20ef`, the current pin. The
candidate's new AP.md text is the **object under review**, not the protocol that
governs your acceptance. Because the worktree is at the candidate, read the
governing AP with `git show 73e20ef:AP.md` and the other `73e20ef` files; do not
mistake the candidate's AP.md for the governing text. Do not use the candidate
to excuse a defect in itself. If the candidate and the governing AP conflict,
report the conflict; the governing AP wins until publication and the consumer
pin update.

The approved plan's risk 8 applies: the candidate never governs its own
acceptance. Fresh independent acceptance is required because the change touches
the sole normative protocol and its consumer pin.

## 4. Cooperator decisions

```text
Plan gate: A approved.
CD-1: Orchestrator session scope `logical-whole | development-run` accepted.
CD-2: K1 accepted: AP standing maintenance duty, RF-09 same-repository ledger,
      AP_DEFECTS remains Cooperator-owned cross-project evidence.
CD-3: overridden: the Cooperator commits and pushes the Kronika pin. The pin is
      a later exchange, not part of this AP source candidate.
CD-4: accepted: the pilot is a Fresh Evidence Probe Worker; later exchange.
CD-5: accepted: the three mutation axes are mandatory in every newly issued
      Worker grant.
CD-6: accepted: the run map is required while a run scope is active.
```

The candidate must implement CD-1, CD-2, CD-5 and CD-6. CD-3 and CD-4 are later
exchanges and are not candidate failures.

## 5. What to read

Read the current governing AP at `73e20ef`:

```text
AP.md — §§2, 3, 5, 7, 13, 14, 17, 18, 19; RF-01..RF-19; Finite Convergence.
AP_ORCHESTRATOR.md — Continuation Bootstrap, Decision Table, Worker Exchange
  Coordinates, Planning Ownership, Prompt Construction, Validation/Results/
  Closure, Rotation and Restoration, Stop and Escalation.
AP_WORKER.md — Reporting, Worker Exchange Coordinates, stopping conditions.
PROMPT_CONTRACTS.md — Worker Report Header, Common Worker Task Fields,
  Cooperator Delivery and Trace Destination Record, Worker Exchange Identity,
  Planning Record, Fresh Orchestrator Restoration, AP Integration Task.
ARTIFACT_LIFECYCLE.md — artifact lifecycle, trace, notes.
ADR-0016, ADR-0023, ADR-0025 — historical owners and rejected alternatives.
```

Read the candidate package:

```text
01_report_00.md — the approved plan and acceptance criteria.
02_report_00.md — the implementation report, as claims.
The full diff: git diff 73e20ef..fe1e58d9
The new AP.md sections, PROMPT_CONTRACTS records, AP_ORCHESTRATOR
  Run-Scoped Orchestration, AP_WORKER direct-write paragraph, ADR-0026,
  CHANGELOG Unreleased entry, and docs/adr/README.md.
```

The Meta projections (`AP_DESTILLED.md`, `AP_DEFECTS.md`, `BRAINSTORMING.md`,
Meta README) are the later 04/02 exchange. Their absence from this AP source
candidate is expected; note it as pending by plan, not as a candidate failure.
The AP_DEFECTS entries and AP_DESTILLED §17 are evidence for the acceptance
criteria, not task authority.

## 6. Acceptance criteria

Accept the exact candidate only if all of these hold:

1. **Three roles preserved.** AP still has exactly COOPERATOR, ORCHESTRATOR and
   WORKER. The Master Orchestrator is an Orchestrator session scope, not a
   fourth role; it grants no authority by itself; it never selects, plans,
   accepts or closes a whole; a run-scoped session may prompt only for a whole
   it opened as that whole's Orchestrator after Cooperator selection, recording
   the departure.
2. **Run map and provisional handout.** AP.md and AP_ORCHESTRATOR.md define the
   run map, the provisional `00_handout.md`, the per-whole handout revalidation
   record, the frozen-after-open rule, the supersession rule, and the boundary
   that a run map or provisional handout is never selection, plan or authority.
3. **Report persistence and axes.** AP.md, AP_WORKER.md and PROMPT_CONTRACTS.md
   define direct-write report persistence and the three mutation axes
   (repository, host/remote, trace). The plan's mapping uses the existing
   `Report persistence owner` plus the axes; it does not add `Report author` or
   `Report persister` fields. The P1–P5 consistency rules are coherent. A
   read-only Worker may write its own exact report; `Repository mutation: none`
   never forbids the granted trace write.
4. **Satisfiability and blocked exchange.** AP.md §7 defines the four
   comparisons (validation–authority, routing, persistence, spelling) and the
   Worker stop; RF-19 and Planning Budget define consumed coordinates and the
   corrected `02/01` initial Planner. A new logical-whole identity is lawful
   only for a materially changed objective, never as a coordinate reset.
5. **Standing AP maintenance.** AP.md §13 defines the consumer-neutral standing
   ledger duty; it keeps storage in the consuming repository and does not make
   any Meta path or trace a discovery source. RF-09 remains the semantic owner.
6. **ADR and changelog.** ADR-0026 and the CHANGELOG entry exist; the ADR index
   row exists; historical ADR bodies 0004–0025 are unchanged.
7. **Compatibility.** `ap` is executable; `ap`, `ap.project.conf`, `INFOSEC.md`,
   `PROMPT_ENGINEERING_PATTERNS.md` and `.gitignore` are unchanged; schema v1,
   the managed `AGENTS.md` block, and the `init`/`doctor`/`project`/`exec`/
   `update`/`bundle` contracts are unchanged.
8. **Documentation coherence.** Links, anchors and headings resolve; no
   duplicate heading slug; new AP.md subsections carry explicit anchors; the
   new rules are stated once in AP.md and projected as pointers plus at most
   one orientation sentence.
9. **Plan fidelity.** The candidate implements the approved plan's sections
   E.1–E.3, H, I, J and K, with the Orchestrator conditions. It does not
   implement the Meta projections, the Kronika pin, the test-constant edit or
   the pilot. It does not add P20, `Report author`/`Report persister` fields,
   `correction-required` to AP enums, or a new `ap` command/schema/test suite.
10. **Later exchanges remain pending by plan.** The Meta projections, AP
    publication, Kronika pin (including `tests/contract/test_ap_integration.py`
    line 10), and pilot are later. Note them as pending; do not fail the AP
    source candidate for their absence.

## 7. Implementation report claims to verify

The implementation report is a claim. Verify each of these explicitly:

- **MEASURED-1 (prompt defect).** The implementation prompt's §8 ordered
  V1–V12 after staging/commit, but V1–V5 can only pass after the commit. The
  Worker used working-tree equivalents before and committed evidence after.
  Decide whether the candidate is affected. It should be a prompt defect, not a
  candidate defect.
- **MEASURED-2 (plan correction).** The plan attributed the "bounded snapshot"
  sentence to ADR-0016; no ADR body contains it. Verify that ADR-0026 now cites
  AP.md §13 and the RF-09 activation snapshot, and that no ADR-0016 body was
  changed.
- **LEAD-1.** The consumer-file atomic-pin item in PROMPT_CONTRACTS/UPDATING
  has no dedicated AP.md sentence. Decide whether AP §1 explicit update and
  RF-15 are sufficient owners or one AP.md sentence is needed.
- **LEAD-2.** The explicit anchor `run-level-handouts` duplicates the heading
  slug. Decide whether it is a defect; check the rendered-anchor risk.
- **LEAD-3.** Uppercase `META` remains in AP_ORCHESTRATOR.md. Run a
  case-insensitive `meta` neutrality check; decide whether it is a defect.
- **Deviations.** Check the report's placement, wording, run-level additions,
  condition 6, PROMPT_CONTRACTS structure, FAQ condensation and ADR-0026
  attribution against the candidate. Decide whether any deviation changes a
  plan decision or creates a second semantic owner.

## 8. Validation — run and report exactly

Run the following from `/Users/agile/Projects/ap`. Record exact commands and
results.

```text
V1  git rev-parse HEAD; git log -1 --format='%H %P %s'; git status --porcelain=v1
    -> fe1e58d9..., parent 73e20ef, one commit, clean
V2  git diff --name-status 73e20ef80b88700d5fcbc397cd8edd4fc425869f..fe1e58d9c3f074b50eda0ebd7df76e4002326953
    -> exactly the 13 M + 1 A paths
V3  git diff --check 73e20ef...fe1e58d9
    -> clean
V4  git diff --quiet 73e20ef...fe1e58d9 -- ap ap.project.conf INFOSEC.md PROMPT_ENGINEERING_PATTERNS.md .gitignore
    -> exit 0
V5  git diff --name-only 73e20ef...fe1e58d9 -- docs/adr
    -> only 0026 and README.md
V6  sh -n ap; ./ap --help; ./ap bundle --help
    -> exit 0 for each
V7  Link and anchor check over the changed files:
    relative link targets; test -e; every #anchor matches an explicit <a id>
    or a heading slug; check the duplicate run-level-handouts id.
    -> no unresolved target; record the duplicate decision
V8  Heading slugs per changed file; sort | uniq -d
    -> no duplicate slug
V9  Spelling and neutrality:
    each section-I definition appears once in PROMPT_CONTRACTS and verbatim
    elsewhere;
    rg -n -i 'report persister|report author:' -> only ADR-0026 alternatives;
    rg -n -i -w 'meta' --glob '!docs/adr/**' --glob '!CHANGELOG.md' -> record
    every match; decide LEAD-3 case-insensitively.
V10 Single-owner review of the full diff:
    every new normative sentence is in AP.md and states Detection; projections
    are pointers plus at most one orientation sentence; decide LEAD-1.
V11 Scenario walk-through S1–S14 from the approved plan:
    record the candidate evidence for each.
V12 ./ap project check --root /Users/agile/Projects/ap --baseline 73e20ef80b88700d5fcbc397cd8edd4fc425869f
    -> expected "OK trusted baseline contract" then the declared-CPython ERROR;
       record the limitation class, not a private host path; not repaired.
```

Do not run a broad suite, Kronika checks, the pin sequence, the pilot, or any
NUC/provider/browser command. The AP repository has no test suite and no
consumer `.ap` submodule.

## 9. Findings and verdict

Produce a finding table:

```text
ID | Severity | Finding | Evidence | Smallest correction | Owner
```

Severity values: `blocker`, `material`, `minor`, `info`. A finding must cite the
exact file, heading, anchor or command output. Do not manufacture a finding.

Verdict:

```text
PASS      every acceptance criterion holds; no blocker or material finding.
          Phase-qualified result: acceptance-PASS.
PARTIAL   at least one material finding; the candidate is otherwise a valid
          base. Phase-qualified result: not-applicable.
BLOCKED   the candidate identity or package is unverifiable, independence is
          compromised, or a blocker prevents acceptance. Phase-qualified
          result: not-applicable.
```

The Orchestrator decides the next step: publication of the exact candidate,
one smallest coherent correction, or escalation. The auditor never repairs its
own finding.

## 10. Report contract

Write your terminal report directly to:

```text
/Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/03_report_00.md
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
4  Candidate and base commits; start and end commit unchanged.
5  Changed files and purpose: the report only; the candidate inspected read-only.
6  Tests and validation: V1–V12 exact commands and results; S1–S14; findings.
7  Commit and push result: none.
8  Deviations, risks, or missing evidence.
9  One smallest next step: publication of the exact candidate, one smallest
   correction, or exact missing evidence.
10 Exactly one report justification: final-acceptance.
11 Authority-expiry statement.
12 Compact critique:
   Orchestration critique:
   MEASURED: none | <verified finding; evidence; effect; smallest correction>
   LEAD: none | <unverified possibility; cheapest useful check>
13 Resolved Execution Issues / Near-Misses: none | <exact>
14 Pre-Existing Failure Classification: none | <complete classification; V12 is
   pre-existing and not candidate-caused>
15 Independence statement: fresh session, no implementation participation, no
   inherited transcript or reasoning.
16 Logical-whole closure: not-closed.
```

The report must state that it does not publish, pin, deploy, or close the
logical whole. Read the report back completely; verify its first line,
coordinates, content, and path. Then send a short terminal notice with the
status, candidate SHA, exact report path, and any requested hash. Do not paste
the report back into chat as a substitute for the file.

## 11. Stop conditions

Stop and return `BLOCKED` or `PARTIAL` without substantive acceptance if:

- the candidate is not `fe1e58d9`, the parent is not `73e20ef`, the tree is
  dirty, the candidate is not on `main`, or public main is not `73e20ef`;
- you inherited implementation context or cannot establish independence;
- a required source is missing or contradictory;
- the report destination already exists, the parent is not the exact verified
  directory, or the client cannot write the report through a permitted route;
- a finding would require an edit, correction, Git write, pin, publication,
  deployment, NUC/host/provider/browser/secret contact, or a forbidden command;
- a material Cooperator decision is needed. Return
  `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and name the decision.

Do not repair the candidate, the environment, the prompt, or the plan. Preserve
the first causal failure and report the exact blocker.

## 12. Prompt satisfiability check

This grant has been checked before issue:

```text
VALIDATION–AUTHORITY  every required command is inside the positive authority;
                      no negative clause forbids V1–V12 or the report write.
ROUTING               one concrete value per identity/route field; the candidate
                      and base SHAs are exact.
PERSISTENCE           report persistence owner assigned WORKER; direct-write
                      exact path; repository mutation none; host/remote none;
                      trace direct-write; Git read-only.
SPELLING              paths, profile name, and commands come from their durable
                      owners and the approved plan.
```

If you find a defect in this grant, report it under `Orchestration critique`
with MEASURED or LEAD. If it prevents a lawful acceptance, stop `BLOCKED`; do
not improvise around it.

## 13. Authority expiry

This acceptance grant expires at your terminal report, cancellation, or
supersession. It grants no correction, publication, pin, Meta projection,
deployment, or closure authority. The Orchestrator decides the next step from
your report. The Cooperator is not a copy-paste courier: write the report to the
exact trace path, read it back, and send only the short terminal notice. Then
stop.
