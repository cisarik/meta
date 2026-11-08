# Fresh Evidence Probe prompt — pilot dry-run of prepared Kronika handout 01

You are a genuinely fresh Fresh Evidence Probe Worker. This is a read-only pilot
of the run-level handoff model. It is not an acceptance of the AP candidate and
not the start of the Kronika product whole.

```text
Persistent role identity: WORKER
Worker session profile: Fresh Evidence Probe
Worker session target: fresh-worker-session
Native planning mode: not-used
Phase: Restoration support
Task identity: AP-MO-06 — pilot dry-run of prepared Kronika handout 01

Logical whole identity: master-orchestrator-and-report-persistence
Worker session ordinal: 06
Worker exchange ordinal: 01

Delivery route: manual Cooperator delivery
Reasoning recommendation: Medium — read-only handout revalidation and Stage 1 compatibility probe
Recommended context capacity: approximately 200k tokens
Independence required: no (pilot evidence; the AP candidate was accepted at 04/01; this is not an acceptance)

Report persistence owner: assigned WORKER
Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/06_report_00.md
Git authority: read-only
```

Before substantive work, confirm that you are a genuinely fresh session that did
not participate in the AP planning, implementation, correction, acceptance or
Meta projection. Do not read any agent or session transcript. Your inputs are
the handout, its named predecessor evidence, the new AP at the current pin, the
Kronika checkout, and this grant.

## 1. Hypothesis and scope

```text
Hypothesis: a fresh per-whole Orchestrator could lawfully start the Kronika
  logical whole `01-timeline-and-history-media-thumbnails` from the prepared
  handout `00_handout.md` under AP `d7023cf`, after revalidating its material
  facts.

Scope: the handout, the predecessor notes/reports it names, the Kronika
  checkout at the new pin, and the AP documents at `d7023cf`.

Allowed mutation domains:
  repository mutation: none
  temporary probe-state mutation: none
  durable project-state mutation: none
  external or production mutation: none
  trace persistence: direct-write this report only

Expected evidence: one Handout Revalidation Record and one verdict.

Interpretation rule:
  yes                   every material handout fact is usable as written under
                        the new AP; no correction is needed.
  yes-with-corrections  the handout is a usable seed, but the exact stale facts
                        and non-AP fields must be corrected before a per-whole
                        Orchestrator acts on it.
  no                    the handout cannot lawfully seed the whole under the
                        new AP; name the blocking fact and the smallest
                        correction.

Cleanup: none. Do not create `00_notes.md`, a handout, a prompt, a scratch file
or a temporary artifact. Write only the report.

Stop condition: the handoff compatibility fact is decision-ready. Do not expand
into Stage 2, the product whole, any Worker prompt, or any Kronika change.
```

CD-4 selected a Fresh Evidence Probe for this pilot. The probe tests the
handout's usability; it is not a full per-whole Orchestrator and does not start
the whole.

## 2. Authority and boundaries

```text
Positive authority
- Read-only inspection of /Users/agile/Projects/kronika and
  /Users/agile/Projects/ap.
- Read-only inspection of:
  /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/00_handout.md
  and the predecessor notes/reports it names under
  /Users/agile/meta/projects/kronika/01/00-ux-refresh-acceptance-and-promotion/.
- Read-only Git inspection: rev-parse, status, log, show, diff, ls-tree,
  ls-remote, cat-file, branch --show-current.
- Read-only shell text inspection: rg, grep, sed, tr, wc, sort, uniq, test -e,
  ls, pwd -P.
- Read-only Kronika checks: ./.ap/ap doctor and
  ./.ap/ap project check --root /Users/agile/Projects/kronika --baseline
  246c9f86b72e652cd36ed0d9f4e19e77f972df91.
- Exact direct-write of 06_report_00.md if and only if it is absent, followed by
  a complete readback.

Negative authority
- No edit, creation, deletion, rename, or chmod in Kronika, AP or Meta except
  the one report file.
- No `00_notes.md`, no handout, no prompt, no closure file, no scratch file.
- No Stage 2, no product whole, no Worker prompt, no plan, no implementation.
- No git add, commit, push, fetch, pull, merge, rebase, reset, restore, clean,
  stash, checkout, switch, tag, branch, remote, or config write.
- No NUC contact, `kronika-release`, deployment, rollback, systemd, package
  manager, AppArmor, UFW, Tailscale, mount or storage mutation.
- No tests, product build, browser, provider, account, or secret/credential/
  token/private-key/cookie/private-host-value inspection.
- No reading of any agent transcript, session transcript, `.cursor` path, or
  any path outside the named roots. If the start state is lost, stop and report;
  do not reconstruct it from a transcript.
- No fourth role, historical rewrite, or mass rename.
```

The report write is trace persistence, not repository mutation. If the report
path exists, including an empty file, stop `BLOCKED` without overwriting.

## 3. Verified baseline — revalidate before the probe

```text
Kronika: /Users/agile/Projects/kronika
Kronika HEAD: 246c9f86b72e652cd36ed0d9f4e19e77f972df91
Kronika public main: 246c9f86b72e652cd36ed0d9f4e19e77f972df91
Kronika .ap gitlink: d7023cf037f6d17885c3ede5c04812c61640da50
Kronika .ap HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
Kronika tree: clean

AP: /Users/agile/Projects/ap
AP public main: d7023cf037f6d17885c3ede5c04812c61640da50
AP local HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
AP tree: clean

Handout:
  /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/00_handout.md

Predecessor:
  /Users/agile/meta/projects/kronika/01/00-ux-refresh-acceptance-and-promotion/
```

Verify:

```text
git -C /Users/agile/Projects/kronika rev-parse HEAD
git -C /Users/agile/Projects/kronika ls-remote origin refs/heads/main
git -C /Users/agile/Projects/kronika ls-tree HEAD .ap
git -C /Users/agile/Projects/kronika/.ap rev-parse HEAD
git -C /Users/agile/Projects/kronika status --porcelain=v1
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 246c9f8...
git -C /Users/agile/Projects/ap rev-parse HEAD
git -C /Users/agile/Projects/ap ls-remote origin refs/heads/main
git -C /Users/agile/Projects/ap status --porcelain=v1
```

A different HEAD, public main, `.ap` pin, dirty tree, or `doctor`/`project check`
failure is a new state. Stop and report; do not reconcile it by mutation.

## 4. Mandatory reading

```text
The handout at the exact path above. Read it fully.

The predecessor evidence it names, under
/Users/agile/meta/projects/kronika/01/00-ux-refresh-acceptance-and-promotion/:
  00_notes.md, 02_report_00.md, 03_report_00.md, 04_report_00.md.
The predecessor notes are frozen historical evidence; do not rewrite them.

The new AP at d7023cf:
  AP_ORCHESTRATOR.md — Continuation Bootstrap Stage 1 and Stage 2
  AP.md — §14 Run-Level Handouts; §18 Stopping Conditions;
    RF-19 and the coordination rules
  PROMPT_CONTRACTS.md — Worker Report Header; Provisional Handout Marker;
    Handout Revalidation Record; Run Map Record
  AP_WORKER.md — Reporting and stopping conditions
```

Do not read the AP update trace `00_notes.md`, the other Kronika run 01 handouts,
or any agent transcript. The pilot is independent of the AP update trace.

## 5. The handout revalidation

Read the handout's metadata and every material section. Fill this record:

```text
Handout revalidation: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/00_handout.md
Received handout status: <no provisional marker (legacy) | provisional>
Revalidated against: <Kronika 246c9f8; AP d7023cf; predecessor closure ...>
Usable facts: <list> | none
Stale facts and corrections: <fact: handout value -> measured value> | none
Not revalidated: <fact and reason> | none
Handout disposition: adopted | adopted-with-corrections | superseded-by <locator>
```

Check at least:

- **Metadata:** `Restoration classification: FULL`, `Overall: READY` and the
  absence of `Handout status: provisional`. AP §14 permits only `PASS`,
  `PARTIAL` or `BLOCKED` for restoration classification; the provisional marker
  is the new run-level marker. Record the mismatch; do not edit the handout.
- **§1.1 Canonical repository:** the handout's exact HEAD `7ee4684...`, public
  main `7ee4684...`, commit subject and clean tree. Revalidate against the
  current `246c9f8...`; record stale facts.
- **§1.2 Governing AP:** the handout's AP pin `73e20ef...`; revalidate against
  `d7023cf...`; record the stale pin.
- **§1.3 Repository gate:** the handout's `project check --baseline 7ee4684...`;
  revalidate the current baseline `246c9f8...`; record the stale baseline.
- **§1.4 NUC state:** do not contact the NUC, do not run `kronika-release`.
  Record it as **not revalidated** and name the exact last-observed values.
- **§1.5 Previous whole closure:** read the named predecessor notes/reports;
  confirm the closure, the accepted commit and the carried residuals as far as
  the evidence allows. Record what is usable and what is stale.
- **§2–§7:** the recommended whole, strategic continuity, project operating
  rules, risk register, first actions and readiness review. Distinguish
  questions/evidence/constraints from authority; the handout grants nothing.
  Record any non-AP field, missing marker, stale fact, or contradiction. The
  prepared handout is a seed, not a plan or grant.
- **Operating rules:** the handout's report direct-write, satisfiability,
  coordinates and AP-maintenance rules against the new AP. Record any rule that
  is now owned by AP and any stale local instruction.

The handout is legacy: it was written under `73e20ef`, before the run-level model
and the new mutation axes. Treat it as evidence and revalidate; do not trust it.

## 6. Verdict

```text
Pilot verdict: lawful start: yes | yes-with-corrections | no
```

- `yes`: every material fact is usable; no correction is needed.
- `yes-with-corrections`: the handout is a usable seed, but the exact stale
  facts and non-AP fields must be corrected before a per-whole Orchestrator acts
  on it. This is the expected outcome if the only differences are the known
  state facts and legacy metadata.
- `no`: the handout cannot lawfully seed the whole; name the blocking fact and
  the smallest correction.

Do not correct the handout. A `yes-with-corrections` verdict routes to a
run-level task that refreshes the Kronika handouts; a `no` verdict routes to a
targeted AP correction. The Orchestrator and Cooperator decide.

## 7. Report contract

Write your terminal report directly to:

```text
/Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/06_report_00.md
```

The report must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

It must echo the logical-whole identity, Worker session ordinal `06`, Worker
exchange ordinal `01`, and include:

```text
1  Coordinates.
2  Status: PASS, PARTIAL, or BLOCKED.
3  Phase-qualified result: not-applicable.
4  Start and end HEAD 246c9f8... (read-only; the probe commits nothing).
5  Changed files and purpose: the report only; no Kronika/AP/Meta edit; no
   00_notes.md.
6  Tests and validation: the baseline checks and the revalidation evidence.
7  Commit and push result: none.
8  Deviations, risks, or missing evidence.
9  Handout Revalidation Record (the exact block in section 5).
10 Pilot verdict: lawful start: yes | yes-with-corrections | no.
11 One smallest next step: refresh the handout, targeted AP correction, or
   confirm the prepared handout as a usable seed.
12 Exactly one report justification: new-evidence.
13 Authority-expiry statement.
14 Compact critique:
   Orchestration critique:
   MEASURED: none | <verified finding; evidence; effect; smallest correction>
   LEAD: none | <unverified possibility; cheapest useful check>
15 Resolved Execution Issues / Near-Misses: none | <exact>
16 Pre-Existing Failure Classification: none | <complete if a pre-existing
   failure is found>
17 Independence statement: fresh probe; not an acceptance; the AP candidate was
   accepted at 04/01.
18 Logical-whole closure: not-closed.
```

The report must state that it did not create `00_notes.md`, start the product
whole, issue a Worker prompt, edit Kronika, or contact the NUC. Read the report
back completely; verify its first line, coordinates, content and path. Then send
a short terminal notice with the status, verdict, exact report path and any
requested hash. Do not paste the report back into chat as a substitute for the
file.

## 8. Stop conditions

Stop and return `BLOCKED` or `PARTIAL` without substantive probe if:

- the handout is missing, unreadable, or not the exact path above;
- Kronika HEAD/public main is not `246c9f8...`, the `.ap` pin is not
  `d7023cf...`, or the tree/index is dirty;
- AP public main is not `d7023cf...`;
- `doctor` or `project check` fails;
- a required fact lies outside the named roots, or the probe would need an
  edit, a Git write, a NUC contact, a test, a browser, a provider or a secret;
- the start state is lost and would require a transcript or out-of-root read;
- the report destination exists, its parent is not the exact verified directory,
  or the client cannot write the report;
- a material Cooperator decision is needed. Return
  `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and name the decision.

Do not repair the handout, environment, prompt or plan. Preserve the first
causal failure and report the exact blocker.

## 9. Prompt satisfiability check

```text
VALIDATION–AUTHORITY  every required command is inside the positive authority;
                      no negative clause forbids the read-only checks or the
                      report write.
ROUTING               one concrete value per identity route; fresh session 06;
                      Native planning mode not-used.
PERSISTENCE           report persistence owner assigned WORKER; direct-write
                      06_report_00.md; repository mutation none; host/remote
                      none; trace direct-write; Git read-only.
SPELLING              paths, SHAs, profile and verdict spellings come from the
                      handout, the new AP owners and the published pins.
```

If you find a defect in this grant, report it under `Orchestration critique`
with MEASURED or LEAD. If it prevents a lawful probe, stop `BLOCKED`; do not
improvise around it.

## 10. Authority expiry

This pilot grant expires at your terminal report, cancellation, or supersession.
It grants no acceptance, publication, pin, Meta projection, deployment, NUC,
correction or closure authority. The Orchestrator and Cooperator decide the next
step from the verdict. The Cooperator is not a copy-paste courier: write the
report to the exact trace path, read it back, send only the short terminal
notice, and stop.
