# Bounded Correction Worker prompt — AP candidate fe1e58d9, findings A-1/A-2/A-3

You are the same implementation Worker session 02. This is a complete new
bounded grant under a current-session renewal. Prior authority expired at the
implementation report; retained context is convenience, not authority.

```text
Persistent role identity: WORKER
Worker session profile: Bounded Correction Worker
Worker session target: current-worker-session
Native planning mode: not-used
Phase: Correction
Task identity: AP-MO-02C — bounded correction of A-1/A-2/A-3

Logical whole identity: master-orchestrator-and-report-persistence
Worker session ordinal: 02
Worker exchange ordinal: 02

Delivery route: manual Cooperator delivery
Reasoning recommendation: High — exact structural and persistence wording in the sole normative protocol
Recommended context capacity: approximately 200k tokens
Independence required: no (correction evidence is non-independent; a fresh independent re-audit follows)

Report persistence owner: assigned WORKER
Repository mutation: exactly the 5 AP paths listed below
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/02_report_01.md
Git authority: exact git add of the 5 paths and one local correction commit on main; no push, fetch, branch, tag, amend, reset, checkout, clean, stash, or remote/config write
```

If the exact implementation session 02 is not available or not healthy, stop and
return `BLOCKED`; the Orchestrator will reissue this correction with a fresh
session and adjusted coordinates. Do not start a fresh session under this
`current-worker-session` prompt.

## 1. Continuity anchor and re-gating

Your previous exchange 02/01 produced:

```text
Implementation report: 02_report_00.md
Candidate: fe1e58d9c3f074b50eda0ebd7df76e4002326953
Parent: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
```

The independent acceptance report `03_report_00.md` returned `PARTIAL`:

```text
A-1  material  Direct-write default/P1/P2 over-restrict trace persistence to
                the Worker's own report and contradict lawful non-report trace
                writes.
A-2  minor     Uppercase META remains in AP_ORCHESTRATOR.md; ADR-0026 records
                "five" trace-specific passages where case-insensitive
                inspection finds six.
A-3  minor     Run-Scoped Orchestration step 6 lets the run-scoped Orchestrator
                "drop" handouts while AP.md gives dropping to the Cooperator.
A-4  info      Duplicate run-level-handouts anchor; no correction.
A-5  info      AP §1/RF-15 suffice for the consumer-file atomic-pin item.
A-6  info      MEASURED-1 is a prompt defect, not a candidate defect.
A-7  info      MEASURED-2 is verified; no correction.
```

Re-gate before mutation: verify repository identity, `main`, HEAD
`fe1e58d9...`, clean tree/index, public main `73e20ef`, and the five target
files. Stop on any conflict between retained context and current repository
evidence.

## 2. Authority and boundaries

```text
Positive authority
- Edit exactly the five AP paths in section 3.
- Read-only inspection of /Users/agile/Projects/ap and the trace package
  01_report_00.md, 02_report_00.md and 03_report_00.md.
- Read-only Git inspection: rev-parse, status, log, show, diff, ls-tree,
  ls-remote, cat-file.
- Read-only shell text inspection: rg, grep, sed, tr, wc, sort, uniq, test -e.
- Read-only AP executable checks: sh -n ap, ./ap --help, ./ap bundle --help,
  and the read-only ./ap project check diagnostic in V12.
- Exact git add of the five paths and one local correction commit on main.
- Exact direct-write of 02_report_01.md if and only if it is absent, followed
  by a complete readback.

Negative authority
- No edit, creation, deletion, rename, or chmod outside the five paths; the
  report is the only file outside AP.
- No change to `ap`, `ap.project.conf`, `INFOSEC.md`,
  `PROMPT_ENGINEERING_PATTERNS.md`, `.gitignore`, `CHANGELOG.md`,
  `docs/adr/README.md`, or any historical ADR body.
- No change to Meta, Kronika, the `.ap` pin, `tests/contract/test_ap_integration.py`,
  the NUC, a provider, a browser, or a secret/credential boundary.
- No new design decision, no change to CD-1..CD-6, no new field, no new `ap`
  command/schema/test suite, no P20, no fourth role, no historical rewrite.
- No A-4/A-5/A-6/A-7 candidate correction. A-4 is accepted info; A-5/A-6/A-7
  require no candidate change.
- No git push, fetch, pull, merge, rebase, reset, restore, clean, stash,
  checkout, switch, branch, tag, remote, or config write. Do not amend.
```

The report write is trace persistence, not repository mutation. If the exact
report path exists, including an empty file, stop `BLOCKED` without overwriting.

## 3. Exact correction allowlist

```text
AP.md
PROMPT_CONTRACTS.md
AP_WORKER.md
AP_ORCHESTRATOR.md
docs/adr/0026-run-scoped-orchestration-mutation-axes-and-direct-write-reports.md
```

Exactly five modified paths; no other path. The correction commit's parent is
`fe1e58d9...`.

## 4. The correction

### 4.1 A-1 — scope the persistence restriction to the report file

The candidate's direct-write paragraph, P1, P2 and AP_WORKER sentence currently
restrict a Worker's `Trace persistence` to its own report (plus an authorized
Planner's received prompt). That contradicts lawful non-report trace writes that
remain in force:

- the completion route: a named capable persister may store supplied exact
  artifacts under separate positive path authority;
- a Worker-authored handout with its own bounded grant;
- notes prepared by a named authorized persister;
- a specialist asset route that returns an asset plus the Worker's report.

Apply the smallest coherent correction:

```text
AP.md, anchor #direct-write-report-persistence:
  "The Worker then returns the complete report in the session and writes no
   trace file."
  -> "The Worker then returns the complete report in the session and does not
      write that report to the trace."

PROMPT_CONTRACTS.md, P1:
  "Trace persistence includes the report destination (plus the received prompt
   path for an authorized Planner), and any other trace path is separately
   granted."

PROMPT_CONTRACTS.md, P2:
  "Any other Report persistence owner -> Trace persistence names no report
   destination; the prompt states the relay basis; the report returns in the
   session."

AP_WORKER.md Reporting:
  "write exactly that report file (and an authorized Planner's exact prompt)
   through steps 2–4 and nothing else"
  -> "write exactly that report file (and an authorized Planner's exact
      prompt) through steps 2–4 and no file outside the granted Trace
      persistence."
```

Preserve P3–P5. Do not add a new field. Do not weaken the direct-write default:
the assigned Worker remains the default persister for its own report. The
correction only makes clear that other separately granted trace paths are not
forbidden.

Check the existing lawful routes before and after:

```text
rg -n 'persister' AP.md PROMPT_CONTRACTS.md
```

Confirm the completion-repair route, Worker handout, notes and specialist asset
route remain lawful under the corrected P1/P2. Record the exact matches that
support the conclusion.

### 4.2 A-2 — remove the sixth trace-specific reference and align the ADR count

```text
AP_ORCHESTRATOR.md, Validation, Results, and Closure:
  "not a new session-state file or META alone"
  -> "not a new session-state file or an activated trace alone."

docs/adr/0026-...:
  Align the "five live passages" / "five trace-specific passages" count with
  the actual case-insensitive count (six). Use "six" consistently, or a
  count-free formulation, in both places. Do not rewrite any historical ADR
  body.
```

`PROMPT_CONTRACTS.md`'s fenced `meta_exchange_index` example is a labelled
trace-local storage example, not a defect. Leave it.

### 4.3 A-3 — align the projection with AP.md's Cooperator drop authority

```text
AP_ORCHESTRATOR.md, Run-Scoped Orchestration step 6:
  "refresh, supersede, or drop the remaining unopened handouts"
  -> "refresh or supersede the remaining unopened handouts, and record any
      Cooperator drop as `dropped`."
```

This makes the projection match AP.md: the Cooperator may reorder, add or drop
entries; the run-scoped Orchestrator records the resulting status.

### 4.4 Do not change

Do not change A-4 (duplicate anchor), A-5 (consumer-file owner), A-6 (prompt
defect) or A-7 (verified plan correction). Do not change CD-1..CD-6, the three
roles, the run map/provisional-handout model, the mutation axes, the
satisfiability check, the consumed-coordinate rule, the standing maintenance
duty, the ADR-0026 decisions, or any historical ADR body.

## 5. Validation

Run from `/Users/agile/Projects/ap` and record exact commands and results.

```text
V1  git rev-parse HEAD; git log -1 --format='%H %P %s'; git status --porcelain=v1
    -> one correction commit whose parent is fe1e58d9...
V2  git diff --name-status fe1e58d9...HEAD
    -> exactly the five modified paths of section 3
V3  git diff --check fe1e58d9...HEAD -> clean
V4  git diff --quiet fe1e58d9...HEAD -- ap ap.project.conf INFOSEC.md PROMPT_ENGINEERING_PATTERNS.md .gitignore
    -> exit 0
V5  git diff --name-only fe1e58d9...HEAD -- docs/adr
    -> only 0026
V6  sh -n ap; ./ap --help; ./ap bundle --help -> exit 0 each
V7  Link and anchor check on the five changed files:
    relative targets; test -e; every #anchor matches an explicit <a id> or a
    heading slug. The pre-existing run-level-handouts duplicate remains
    accepted (A-4); no new unresolved link or anchor.
V8  Heading slugs per changed file; sort | uniq -d -> no duplicate.
V9  (a) each section-I definition appears once in PROMPT_CONTRACTS and verbatim
        elsewhere;
    (b) rg -n -i 'report persister|report author:' -> only ADR-0026 alternatives;
    (c) rg -n -i -w 'meta' --glob '!docs/adr/**' --glob '!CHANGELOG.md'
        -> no uppercase META and no trace-implementation name outside the
           labelled fenced Meta-local example;
    (d) rg -n 'persister' AP.md PROMPT_CONTRACTS.md -> all lawful routes are
        still permitted by the corrected P1/P2.
V10 Single-owner review:
    every new or changed normative sentence remains in AP.md with Detection;
    projections are pointers plus at most one orientation sentence; A-3 now
    matches AP.md's Cooperator drop authority.
V11 Scenario walk-through S1–S16:
    S1–S14 from the approved plan, plus
    S15 completion-repair Worker persists a predecessor artifact plus its own
        report -> lawful under the corrected P1/P2;
    S16 Worker-authored handout with its own grant and a relayed report ->
        lawful.
V12 ./ap project check --root /Users/agile/Projects/ap --baseline 73e20ef...
    -> expected trusted-baseline line then declared-CPython ERROR; record the
       limitation class, not a host path; not repaired.
```

Do not run a broad suite, Kronika checks, the pin sequence, the pilot, a browser,
a provider, or a NUC command. No test suite exists.

## 6. Git authority

```text
git status --porcelain=v1        -> exactly the five paths
git diff --stat                  -> inspect
git add <the five exact paths>
git diff --cached --name-status  -> exactly the five M paths
git commit -m "docs: correct report persistence scope and trace neutrality (A-1/A-2/A-3)"
git rev-parse HEAD               -> correction SHA
git status --porcelain=v1        -> clean
```

No push, fetch, amend, branch, tag, reset, or checkout. The correction is a
local candidate; the Cooperator publishes only after fresh independent
re-acceptance.

## 7. Report contract

Write your terminal report directly to:

```text
/Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/02_report_01.md
```

The report must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

It must echo the logical-whole identity, Worker session ordinal `02`, Worker
exchange ordinal `02`, and include:

```text
1  Coordinates and continuity anchor.
2  Status: PASS, PARTIAL, or BLOCKED.
3  Phase-qualified result: implementation-PASS for a complete validated
   correction; not-applicable otherwise.
4  Start commit fe1e58d9...; end commit <correction SHA>.
5  Changed files and purpose: exactly the five paths; the report only outside AP.
6  Tests and validation: V1–V12 and S1–S16 exact results.
7  Commit and push result: local correction commit <SHA> on main; no push.
8  Deviations, risks, or missing evidence.
9  One smallest next step: full fresh independent re-audit 04/01 of the
   correction SHA.
10 Exactly one report justification: new-mutation.
11 Authority-expiry statement.
12 Compact critique:
   Orchestration critique:
   MEASURED: none | <verified finding; evidence; effect; smallest correction>
   LEAD: none | <unverified possibility; cheapest useful check>
13 Resolved Execution Issues / Near-Misses: none | <exact>
14 Pre-Existing Failure Classification: none | <complete; V12 is pre-existing>
15 Logical-whole closure: not-closed.
```

The report must state that correction evidence is non-independent and that it
does not accept, publish, pin, project or close. Read it back completely; verify
its first line, coordinates, content and path. Then send a short terminal notice
with the status, correction SHA, exact report path, and any requested hash. Do
not paste the report back into chat as a substitute for the file.

## 8. Stop conditions

Stop and return `BLOCKED` or `PARTIAL` without substantive mutation if:

- the exact session 02 is not available or not healthy;
- AP HEAD is not `fe1e58d9...`, the tree/index is dirty, or public main is not
  `73e20ef...`;
- the correction would touch a path outside the five-path allowlist;
- a target line or anchor does not match the acceptance finding;
- the correction would change CD-1..CD-6, a plan decision, a historical ADR
  body, a semantic owner, or a new structural field;
- a required source is missing or contradictory;
- the report destination exists, the parent is not the exact verified directory,
  or the client cannot write the report;
- a material Cooperator decision is needed. Return
  `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and name the decision;
- a security, credential, NUC, provider or browser boundary would be touched.

Do not repair the candidate, environment, prompt, or plan. Preserve the first
causal failure and report the exact blocker.

## 9. Prompt satisfiability check

```text
VALIDATION–AUTHORITY  every V1–V12 command is inside the positive authority;
                      no negative clause forbids the correction or report write.
ROUTING               one concrete value per identity/route field; current
                      session 02 with the exact continuity anchor.
PERSISTENCE           report persistence owner assigned WORKER; direct-write
                      02_report_01.md; repository mutation exactly five paths;
                      host/remote none; trace direct-write; Git add/commit exact.
SPELLING              paths, profile, commands and commit message come from the
                      acceptance report, the candidate and their durable owners.
```

If you find a defect in this grant, report it under `Orchestration critique`
with MEASURED or LEAD. If it prevents a lawful correction, stop `BLOCKED`; do
not improvise around it.

## 10. Authority expiry

This correction grant expires at your terminal report, cancellation, or
supersession. It grants no acceptance, publication, pin, Meta projection,
deployment or closure authority. A fresh independent re-audit Worker will
receive a separate complete prompt. The Cooperator is not a copy-paste courier:
write the report to the exact trace path, read it back, send only the short
terminal notice, and stop.
