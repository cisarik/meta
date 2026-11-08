# Meta projection Worker prompt — AP_DESTILLED, AP_DEFECTS, BRAINSTORMING §7, Meta README

You are the same implementation Worker session 05. This is a complete new
bounded grant under a current-session renewal. Prior authority expired at the
pin report; retained context is convenience, not authority.

```text
Persistent role identity: WORKER
Worker session profile: Fresh Implementation Worker
Worker session target: current-worker-session
Native planning mode: not-used
Phase: Implementation
Task identity: AP-MO-05M — Meta projections for the accepted AP update

Logical whole identity: master-orchestrator-and-report-persistence
Worker session ordinal: 05
Worker exchange ordinal: 02

Delivery route: manual Cooperator delivery
Reasoning recommendation: Medium — documentation projection of an already accepted AP change
Recommended context capacity: approximately 200k tokens
Independence required: no (documentation projection; non-independent)

Report persistence owner: assigned WORKER
Repository mutation: exactly /Users/agile/meta/AP_DESTILLED.md, /Users/agile/meta/AP_DEFECTS.md, /Users/agile/meta/BRAINSTORMING.md and /Users/agile/meta/README.md
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/05_report_01.md
Git authority: none; no add, commit, push, fetch, branch, tag, reset, checkout, clean, stash, amend, or remote/config write
```

If the exact session 05 is not available or not healthy, stop and return
`BLOCKED`; the Orchestrator will reissue this projection with a fresh session
and adjusted coordinates. Do not start a fresh session under this
`current-worker-session` prompt.

## 1. Continuity anchor and re-gating

Your previous exchange 05/01 produced the Kronika pin report `05_report_00.md`
and the published pin `246c9f86b72e652cd36ed0d9f4e19e77f972df91`; the `.ap`
gitlink is `d7023cf037f6d17885c3ede5c04812c61640da50`.

Re-gate before mutation:

```text
Meta HEAD: record the actual value at exchange start; the last observed is
           5b227028f505e08fb623dba65732dbc0cf6603e3. Do not require a
           specific Meta HEAD; the Cooperator maintains and commits the trace.
AP public main: d7023cf...
Kronika HEAD and public main: 246c9f8...
Kronika .ap gitlink and .ap HEAD: d7023cf...
```

The Meta trace directory is owner state. The Cooperator maintains and commits
it. Current observed trace state may include tracked prompt/report pairs, a
tracked `00_RUN_MAP.md`, a tracked `00_master_handout.md`, an untracked
`00_notes.md`, and the untracked `05_meta-projection_01.md` (this prompt). Do
not edit any of them. Your four target files at the Meta root must be clean at
start. Stop on any conflict between retained context and current evidence.

## 2. Exact allowlist

```text
/Users/agile/meta/AP_DESTILLED.md
/Users/agile/meta/AP_DEFECTS.md
/Users/agile/meta/BRAINSTORMING.md
/Users/agile/meta/README.md
```

The report `05_report_01.md` is the only file outside these four. No other Meta
file; no AP repository file; no Kronika file; no trace `00_notes.md` or
`00_RUN_MAP.md`; no handouts.

## 3. Authority and boundaries

```text
Positive authority
- Edit exactly the four Meta files above.
- Read-only inspection of /Users/agile/meta, /Users/agile/Projects/ap and
  /Users/agile/Projects/kronika.
- Read-only Git inspection: rev-parse, status, log, show, diff, ls-tree,
  ls-remote, cat-file.
- Read-only shell text inspection: rg, grep, sed, tr, wc, sort, uniq, test -e,
  ls, pwd -P.
- Exact direct-write of 05_report_01.md if and only if it is absent, followed
  by a complete readback.

Negative authority
- No edit, creation, deletion, rename, or chmod outside the four Meta files;
  the report is the only file outside them.
- No AP repository edit; no Kronika edit; no `.ap` pin change; no NUC, host,
  provider, browser, account, or secret/credential/token/private-key/cookie/
  private-host-value inspection.
- No edit to `00_notes.md`, `00_RUN_MAP.md`, a handout, a prompt, or a report
  other than your own `05_report_01.md`.
- No rewrite of the historical AP_DEFECTS defect bodies. The §0.0 standing
  instruction correction and the new §7 disposition record are prospective; the
  historical D-01..D-21 bodies stay as written.
- No change to the historical AP_DESTILLED pin note or measurement text beyond
  the planned conversion to pointers; AP_DESTILLED remains explanatory, not
  authority.
- No new semantic owner, no AP re-acceptance, no fourth role, no historical ADR
  rewrite, no mass rename.
- No git add, commit, push, fetch, pull, merge, rebase, reset, restore, clean,
  stash, checkout, switch, tag, branch, remote, or config write.
- No commit of the Meta trace; the Cooperator commits it after the report.
```

The report write is trace persistence, not repository mutation. If the report
path exists, including an empty file, stop `BLOCKED` without overwriting.

## 4. Mandatory reading

```text
Meta:
  /Users/agile/meta/AP_DESTILLED.md — full
  /Users/agile/meta/AP_DEFECTS.md — full
  /Users/agile/meta/BRAINSTORMING.md — §7 and the file's status conventions
  /Users/agile/meta/README.md — the local storage and handout/closure contract

AP at d7023cf:
  AP.md #run-level-handouts, #orchestrator-session-scope, #mutation-axes,
  #direct-write-report-persistence, #prompt-satisfiability-check,
  #consumed-coordinates, #standing-ledger-maintenance
  PROMPT_CONTRACTS.md Mutation Axes Record, Run Map Record, Provisional Handout
  Marker, Handout Revalidation Record, delivery record P1–P5
  AP_ORCHESTRATOR.md Run-Scoped Orchestration
  ADR-0026
  UPDATING.md and the AP Integration Task / AP Update Task

Trace:
  01_report_00.md — the approved plan, especially sections F, G and E.4
  03_report_00.md — the acceptance findings A-1..A-7
  02_report_01.md — the correction
  04_report_00.md — the re-audit PASS
  05_report_00.md — the pin report and the published pin
```

The approved plan's section F is the disposition table to append; section G is
the AP_DESTILLED projection. Use the current file content, not stale line
numbers. Headings are the durable keys.

## 5. Exact changes

### 5.1 AP_DESTILLED.md

Implement the approved plan's section G, adapted to the current file:

- **Header box:** add that AP `d7023cf` adopted D-17/D-17b, D-19, D-20, D-21 and
  run-scoped orchestration under ADR-0026.
- **§0:** keep the historical `9c5cc44` pin note. Add §0.1 "Measured after the
  pin" naming AP `d7023cf` and the changed AP anchors.
- **§5.4:** turn the direct-write sentence into a pointer to the RF-19
  `#direct-write-report-persistence` default.
- **§8:** add the mutation axes and pointers to the satisfiability check.
- **§14:** add pointers for the new read-only/axes/courier item and the
  pre-written-handout-without-revalidation item.
- **§16:** document `00_RUN_MAP.md` and the provisional `00_handout.md` as local
  trace names; keep the existing notes and handout/closure numbering rules.
- **§17:** retitle as adopted into AP `d7023cf`; convert §17.1–§17.8 into
  pointers that keep their measurement text. In §17.3 record that `Report
  author` and `Report persister` were not adopted (the existing
  `Report persistence owner` plus the axes are used) and that `in-session-only`
  corresponds to relay. In §17.4 correct the blocked-first-exchange rule: a new
  logical-whole identity is lawful only for a materially changed objective, not
  as a coordinate-reset mechanism. In §17.8 keep the Meta-local instruction and
  point to the AP §13 standing duty. Add a concise §18 run-scoped summary as
  pointers.
- Keep the historical pin note and the measurement text. AP_DESTILLED remains
  explanatory and non-authoritative.

### 5.2 AP_DEFECTS.md

- Append `## 7. Disposition record — AP d7023cf (ADR-0026)` with the approved
  plan's section F disposition for every open entry: D-01 through D-21, D-03b
  and D-17b. Each row states the disposition, owner, AP owner or reason,
  evidence at the relevant pin, and proposed change.
- Correct §0.0's restart sentence: a new logical-whole identity is lawful only
  for a materially changed objective; it is not a coordinate-reset mechanism.
  The standing instruction remains prospective.
- State explicitly that AP_DEFECTS remains evidence, not task authority, and
  that the historical defect bodies are unchanged.
- Do not silently drop an entry. Do not rewrite the D-01..D-21 bodies.

### 5.3 BRAINSTORMING.md §7

Change the §7 status line from:

```text
STATUS   proposed, 2026-11-08, by the COOPERATOR during Kronika era 01
```

to:

```text
STATUS   promoted, 2026-11-08; AP d7023cf, ADR-0026
```

One status line. Keep the rest of §7 as evidence.

### 5.4 Meta README.md

Add the local storage for the new AP model, minimally:

- `00_RUN_MAP.md` at `projects/<project>/<run>/` as the run map, with its
  discovery-only, non-authoritative status.
- `00_handout.md` may carry `Handout status: provisional`; a provisional
  handout is frozen when its whole opens and is not an exchange.
- A handout revalidation record is written in the per-whole `00_notes.md` when a
  provisional handout is received.
- Preserve the existing Worker filename grammar, handout/closure sequence,
  notes semantics, and the "storage and discovery policy only" authority
  statement.

Do not turn the Meta README into a second AP semantic owner.

## 6. What not to do

- Do not edit `00_notes.md`, `00_RUN_MAP.md`, a handout, a prompt, or any trace
  file except your report.
- Do not rewrite AP_DEFECTS D-01..D-21 bodies or the AP_DESTILLED historical pin
  note.
- Do not edit the AP repository or Kronika.
- Do not add an AP rule, a new schema, a new record, or a second semantic owner.
- Do not commit, push, stage, or otherwise touch the Meta Git index; the
  Cooperator commits the trace.
- Do not run the NUC, a provider, a browser, a deployment, or a product suite.
- Do not re-audit or re-accept the AP candidate.

## 7. Validation

Run read-only checks from `/Users/agile/meta` and record exact results.

```text
V1  Meta baseline: record git rev-parse HEAD; the four target files are clean
    at start; do not require a specific Meta HEAD. The trace directory is
    owner state; do not edit it.
V2  AP public main d7023cf; AP local clean; Kronika HEAD/public 246c9f8; .ap
    gitlink/HEAD d7023cf; Kronika clean.
V3  After edits, git diff --name-only -- AP_DESTILLED.md AP_DEFECTS.md
    BRAINSTORMING.md README.md -> exactly the four; no other new path.
V4  AP_DEFECTS §7 contains all 23 entries (21 defects plus D-03b and D-17b),
    each with a disposition; §0.0 corrected; historical bodies unchanged.
V5  AP_DESTILLED §17 pointers and measurement text present; §0.1 present;
    §17.3/§17.4/§17.8 updated; §18 present; historical pin note present.
V6  BRAINSTORMING §7 status is promoted with AP d7023cf and ADR-0026.
V7  Meta README documents 00_RUN_MAP.md, the provisional handout marker and the
    revalidation record; the existing grammar is preserved.
V8  git diff --check -- the four files -> clean.
V9  Links/headings/spellings in the four files resolve; no new duplicate owner.
V10 AP and Kronika have no changes: git -C /Users/agile/Projects/ap status
    --porcelain=v1 empty; git -C /Users/agile/Projects/kronika status
    --porcelain=v1 empty.
V11 The four-file diff stays inside the planned projection: no AP redefinition,
    no historical defect rewrite, no trace edit.
V12 Report path absent before write; readback after.
```

No Git write, commit or push.

## 8. Report contract

Write your terminal report directly to:

```text
/Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/05_report_01.md
```

The report must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

It must echo the logical-whole identity, Worker session ordinal `05`, Worker
exchange ordinal `02`, and include:

```text
1  Coordinates and continuity anchor.
2  Status: PASS, PARTIAL, or BLOCKED.
3  Phase-qualified result: implementation-PASS for a complete projection;
   not-applicable otherwise.
4  Start and end Meta HEAD: record the actual value at exchange start and end;
   the Worker commits nothing.
5  Changed files and purpose: exactly the four Meta files; the report only
   outside them.
6  Tests and validation: V1–V12 exact results.
7  Commit and push result: none; the Cooperator commits the Meta trace.
8  Deviations, risks, or missing evidence.
9  One smallest next step: the Cooperator commits the Meta trace; then the
   Orchestrator verifies and issues the pilot 06/01.
10 Exactly one report justification: new-mutation.
11 Authority-expiry statement.
12 Compact critique:
   Orchestration critique:
   MEASURED: none | <verified finding; evidence; effect; smallest correction>
   LEAD: none | <unverified possibility; cheapest useful check>
13 Resolved Execution Issues / Near-Misses: none | <exact>
14 Pre-Existing Failure Classification: none | <complete if a pre-existing
   failure is found>
15 Independence statement: non-independent documentation projection; the AP
   candidate was accepted at 04/01 and published at d7023cf.
16 Logical-whole closure: not-closed.
```

The report must state that the projection is not committed or published and
that it does not close the whole. Read the report back completely; verify its
first line, coordinates, content and path. Then send a short terminal notice
with the status, exact report path and changed-file list. Do not paste the
report back into chat as a substitute for the file.

## 9. Stop conditions

Stop and return `BLOCKED` or `PARTIAL` without substantive mutation if:

- the exact session 05 is not available or not healthy;
- the four target Meta files are not clean or have unexpected changes; AP
  public main is not `d7023cf...`; Kronika HEAD/public is not `246c9f8...`; or
  `.ap` is not `d7023cf...`;
- a path outside the four Meta files would need to change;
- an AP_DEFECTS historical body or the AP_DESTILLED historical pin note would
  need a rewrite beyond the planned conversion;
- an AP or Kronika edit, a trace edit, a Git write, a commit/push, a NUC/
  provider/browser/secret boundary, or a new semantic owner would be needed;
- the report destination exists, its parent is not the exact verified directory,
  or the client cannot write the report;
- a material Cooperator decision is needed. Return
  `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and name the decision.

Do not repair the files, environment, prompt, or plan. Preserve the first causal
failure and report the exact blocker.

## 10. Prompt satisfiability check

```text
VALIDATION–AUTHORITY  every V1–V12 command is inside the positive authority;
                      no negative clause forbids the four-file edits or the
                      report write.
ROUTING               one concrete value per identity/route field; current
                      session 05 with the pin report anchor.
PERSISTENCE           report persistence owner assigned WORKER; direct-write
                      05_report_01.md; repository mutation exactly four Meta
                      files; host/remote none; trace direct-write; Git none.
SPELLING              paths, SHAs, status spelling and profile come from the
                      plan, the Meta owners and the published pin.
```

If you find a defect in this grant, report it under `Orchestration critique`
with MEASURED or LEAD. If it prevents a lawful projection, stop `BLOCKED`; do
not improvise around it.

## 11. Authority expiry

This projection grant expires at your terminal report, cancellation, or
supersession. It grants no commit, push, AP publication, pin, deployment, NUC,
acceptance or closure authority. The Cooperator commits the Meta trace. The
Cooperator is not a copy-paste courier: write the report to the exact trace
path, read it back, send only the short terminal notice, and stop.
