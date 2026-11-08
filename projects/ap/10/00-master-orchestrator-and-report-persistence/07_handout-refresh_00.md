# Fresh Implementation Worker prompt — refresh the Kronika run 01 prepared handouts

You are a genuinely fresh Implementation Worker. The Cooperator has accepted
the AP update closure conditionally: the eight prepared Kronika run 01 handouts
must be refreshed to the new AP before the closure is finalized. This exchange
does that refresh. It does not start any Kronika product whole.

```text
Persistent role identity: WORKER
Worker session profile: Fresh Implementation Worker
Worker session target: fresh-worker-session
Native planning mode: not-used
Phase: Implementation
Task identity: AP-MO-07 — refresh the Kronika run 01 prepared handouts under AP d7023cf

Logical whole identity: master-orchestrator-and-report-persistence
Worker session ordinal: 07
Worker exchange ordinal: 01

Delivery route: manual Cooperator delivery
Reasoning recommendation: Medium — documentation refresh with exact state facts and AP field spellings
Recommended context capacity: approximately 250k tokens
Independence required: no (documentation refresh; non-independent)

Report persistence owner: assigned WORKER
Repository mutation: exactly the eight Kronika run 01 handouts below and the run 01 run map
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/07_report_00.md
Git authority: none; no add, commit, push, fetch, branch, tag, reset, checkout, clean, stash, amend, or remote/config write
```

## 1. Authority and boundaries

```text
Positive authority
- Read-only inspection of /Users/agile/Projects/kronika and /Users/agile/Projects/ap.
- Read-only inspection of /Users/agile/meta/AP_DESTILLED.md,
  /Users/agile/meta/AP_DEFECTS.md and /Users/agile/meta/README.md as evidence.
- Read-only inspection of the eight handouts, the closed 00 whole's handout and
  notes, the pilot report 06_report_00.md, the AP run 10 run map, and the new AP
  at d7023cf.
- Edit exactly the eight handouts and the new run 01 run map listed in section 2.
- Read-only shell and Git inspection: rg, grep, sed, tr, wc, sort, uniq, test -e,
  ls, pwd -P, git rev-parse/status/log/show/diff/ls-tree/ls-remote/cat-file.
- Exact direct-write of 07_report_00.md if and only if it is absent, followed by
  a complete readback.

Negative authority
- No edit, creation, deletion, rename, or chmod outside the eight handouts and
  the run map; the report is the only file outside them.
- Do not edit the closed 00-ux-refresh-acceptance-and-promotion handout or
  notes; they are frozen historical evidence.
- Do not edit AP_DESTILLED.md, AP_DEFECTS.md, the Meta README, the AP repository,
  Kronika product code, AGENTS.md, docs, dependencies, migrations or generated
  artifacts.
- No NUC contact, kronika-release, deployment, rollback, systemd, package
  manager, AppArmor, UFW, Tailscale, mount or storage mutation.
- No tests, product build, browser, provider, account, or secret/credential/
  token/private-key/cookie/private-host-value inspection.
- No reading of any agent or session transcript, .cursor path, or path outside
  the named roots. If the start state is lost, stop and report; do not
  reconstruct it from a transcript.
- No Git write; the Cooperator commits the Meta trace.
- No new AP rule, no second semantic owner, no product decision, no whole
  selection, no Stage 2, no Worker prompt, no 00_notes.md for a Kronika whole.
```

The report write is trace persistence, not repository mutation. If the report
path exists, including an empty file, stop `BLOCKED` without overwriting.

## 2. Exact allowlist

```text
/Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/00_handout.md
/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/00_handout.md
/Users/agile/meta/projects/kronika/01/03-companion-download-notifications/00_handout.md
/Users/agile/meta/projects/kronika/01/04-household-onboarding/00_handout.md
/Users/agile/meta/projects/kronika/01/05-humanized-error-copy/00_handout.md
/Users/agile/meta/projects/kronika/01/06-accessibility-pass/00_handout.md
/Users/agile/meta/projects/kronika/01/07-app-js-modularization-planning/00_handout.md
/Users/agile/meta/projects/kronika/01/08-product-language-decision/00_handout.md
/Users/agile/meta/projects/kronika/01/00_RUN_MAP.md  (new)
```

The closed `00-ux-refresh-acceptance-and-promotion/00_handout.md` is historical
and is not edited. The run map lists the closed 00 whole as `closed` and the
eight refreshed handouts as `provisional`.

## 3. Verified baseline — revalidate before editing

```text
AP public main and local HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
AP tree: clean
Kronika HEAD and public main: 246c9f86b72e652cd36ed0d9f4e19e77f972df91
Kronika .ap gitlink and .ap HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
Kronika tree: clean
Meta: the current trace HEAD; the eight handouts and the run map are absent or
  the handouts are present; the closed 00 handout/notes are frozen.
```

Verify the AP and Kronika state read-only. The eight handouts exist. Stop on any
mismatch.

## 4. What the pilot measured

Read the pilot report `06_report_00.md` in full. Its Handout Revalidation Record
is the correction list for handout 01; the other seven handouts were written by
the same predecessor under `73e20ef` and likely carry the same legacy metadata,
§4 operating rules and §1/§6 Stage 1 omissions. Apply the same corrections to
all eight, revalidating each handout's own state facts.

The pilot verdict is `yes-with-corrections`. The corrections include:

```text
- Restoration classification FULL -> a valid AP value. The refreshed provisional
  handout uses PARTIAL: the whole has not opened and the per-whole Orchestrator
  must revalidate it. The readiness review Overall uses PARTIAL for the same
  reason.
- Add Handout status: provisional.
- Add Orchestrator session scope: logical-whole and
  Development run identity: kronika-run-01.
- Add a reasoning recommendation or the explicit statement
  "selecting a Worker is premature". For a provisional seed the latter is
  appropriate.
- Add Refreshed: 2026-11-08; Refreshed against: AP d7023cf, Kronika 246c9f8,
  .ap d7023cf.
- Add Handout author: Master Orchestrator, AP run 10; Mechanical persister:
  Fresh Implementation Worker session 07; keep the original predecessor path.
- §1.1 HEAD/public main 7ee4684 -> 246c9f8; commit subject updated.
- §1.2 AP pin 73e20ef -> d7023cf.
- §1.3 project check baseline 7ee4684 -> 246c9f8.
- §1.4 NUC state: keep the last-observed values and mark them NOT revalidated;
  do not contact the NUC, do not run kronika-release.
- §1.5 predecessor closure: for handout 01 the predecessor 00 is closed; for
  02-08 the predecessor whole is not yet closed; state the dependency and keep
  the handout provisional. Do not invent closure evidence.
- §1 and §6 Stage 1: add upgrade-ledger revalidation and the Handout
  Revalidation Record before the first Planner prompt.
- §4.1 field block: replace Report author / Report persister / Report
  persistence / Report destination with the AP delivery record; use
  Report persistence owner: assigned WORKER, Trace persistence, and the three
  mutation axes; remove the duplicate Trace persistence line; replace
  in-session-only with the P2 relay form (another Report persistence owner,
  relay basis, Trace persistence: none).
- §4.2 AP_DESTILLED.md §17.5 pointer -> AP.md#prompt-satisfiability-check; the
  PERSISTENCE line -> owners, axes, positive authority and client completion
  route agree (P1-P5).
- §4.3 "A true restart at 01/01 requires a new logical-whole identity" -> remove;
  cite RF-19 #consumed-coordinates and the Blocked First Exchange Example.
- §4.5 AP_DEFECTS/AP_DESTILLED as rule sources -> AP §13
  #standing-ledger-maintenance; Meta files remain citable consumer evidence
  only.
- §5 renumbered residuals R1-R4 vs predecessor A6/R7/R9/R10 -> state the mapping
  once.
```

Do not copy a correction blindly if the handout's own evidence differs. Re-read
each handout and apply only what its content requires.

## 5. Refresh rules

1. **The handouts remain seeds, not authority.** Each refreshed handout says
   it grants no authority and that the per-whole Orchestrator revalidates it in
   Stage 1. Do not claim a whole is selected, planned or closed.
2. **Preserve the product direction.** Keep each handout's recommended whole,
   scope questions, strategic continuity and risk content. The refresh updates
   state facts, metadata and AP operating rules; it does not invent product
   decisions or rewrite the product evidence.
3. **Provisional marker and dates.** Each handout carries
   `Handout status: provisional`, `Refreshed: 2026-11-08`,
   `Refreshed against: AP d7023cf; Kronika 246c9f8; .ap d7023cf`,
   `Handout author: Master Orchestrator, AP run 10`,
   `Mechanical persister: Fresh Implementation Worker session 07`, and the
   original predecessor path.
4. **AP values.** `Restoration classification: PARTIAL`, readiness review
   `Overall: PARTIAL`, `Orchestrator session scope: logical-whole`,
   `Development run identity: kronika-run-01`, and
   `Reasoning recommendation: selecting a Worker is premature` are the
   provisional values. If a handout can support a stronger value without
   claiming an unperformed revalidation, say why; otherwise keep PARTIAL.
5. **NUC.** The §1.4 NUC state is last observed, not revalidated. Keep the exact
   values and the "not revalidated" label. The NUC stays at `7ee4684` until a
   separate routine refresh.
6. **Operating rules.** The new AP is the owner of the direct-write default,
   the mutation axes, the satisfiability check, consumed coordinates and the
   standing ledger duty. The handout cites the AP owners; it does not restate a
   second rule.
7. **Run map.** Create
   `/Users/agile/meta/projects/kronika/01/00_RUN_MAP.md` with:
   - the run objective and exclusions from the handouts' product evidence;
   - the closed 00 whole and the eight provisional whole entries in order;
   - dependencies (01 precedes 02; preserve the handouts' stated dependencies;
     the Cooperator selects the final order);
   - status `closed` for 00 and `provisional` for 01-08;
   - each handout locator and one sentence of evidence;
   - `Run map authority: discovery-only`.
   The run map is a recommendation, not a selection or grant.

## 6. What not to do

- Do not edit the closed 00 handout/notes, AP_DESTILLED, AP_DEFECTS, the Meta
  README, the AP repository or Kronika product code.
- Do not start a Kronika whole, create a Kronika `00_notes.md`, issue a Worker
  prompt or plan, or claim a whole closure.
- Do not commit or push; the Cooperator commits the Meta trace.
- Do not run tests, build, browser, provider, NUC or deployment.
- Do not read a transcript or any out-of-root path.
- Do not add a new AP rule or a new semantic owner.

## 7. Validation

Run read-only checks from `/Users/agile/meta` and `/Users/agile/Projects`:

```text
V1  AP public/local HEAD d7023cf; AP clean.
V2  Kronika HEAD/public 246c9f8; .ap gitlink/HEAD d7023cf; Kronika clean.
V3  The eight handouts exist and the closed 00 handout/notes are unchanged.
V4  After edits, git diff --name-only -- the eight handouts and the run map
    shows exactly the nine paths; no AP/Kronika change.
V5  Every handout carries Handout status: provisional, the AP baseline,
    the session scope/run identity, the reasoning statement, the author and
    persister, and the predecessor.
V6  Every handout uses PARTIAL as the provisional restoration/readiness value
    and preserves its product direction.
V7  Every handout's §4 uses the AP field spellings and owners; no Report author,
    Report persister, duplicate Trace persistence, in-session-only, AP_DESTILLED
    §17.5 pointer or 01/01 restart sentence remains.
V8  Every handout's §1/§6 includes upgrade-ledger revalidation and the Handout
    Revalidation Record.
V9  The run map has the objective/exclusions, 00 closed, 01-08 provisional,
    dependencies, locators, evidence sentences, and discovery-only authority.
V10 Link/heading checks over the nine files; git diff --check; no new duplicate
    owner.
V11 AP and Kronika have no changes.
V12 Report path absent before write; complete readback after.
```

No Git write, commit or push.

## 8. Report contract

Write your terminal report directly to:

```text
/Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/07_report_00.md
```

The report must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

It must echo the logical-whole identity, Worker session ordinal `07`, Worker
exchange ordinal `01`, and include:

```text
1  Coordinates.
2  Status: PASS, PARTIAL, or BLOCKED.
3  Phase-qualified result: implementation-PASS for a complete refresh;
   not-applicable otherwise.
4  Start and end Meta HEAD; the Worker commits nothing.
5  Changed files and purpose: the eight handouts and the run map; the report
   outside them.
6  Tests and validation: V1-V12 exact results.
7  Commit and push result: none; the Cooperator commits the Meta trace.
8  Deviations, risks, or missing evidence.
9  Per-handout refresh table: handout, key state update, metadata, operating
   rules, residual/notes.
10 One smallest next step: the Cooperator commits the Meta trace; then the
   Orchestrator finalizes the AP update closure and the Cooperator accepts it.
11 Exactly one report justification: new-mutation.
12 Authority-expiry statement.
13 Compact critique:
   Orchestration critique:
   MEASURED: none | <verified finding; evidence; effect; smallest correction>
   LEAD: none | <unverified possibility; cheapest useful check>
14 Resolved Execution Issues / Near-Misses: none | <exact>
15 Pre-Existing Failure Classification: none | <complete if a pre-existing
   failure is found>
16 Independence statement: non-independent documentation refresh; the AP
   candidate was accepted at 04/01 and published at d7023cf.
17 Logical-whole closure: not-closed.
```

The report must state that the handouts are provisional seeds, not authority,
and that no Kronika whole was started. Read the report back completely; verify
its first line, coordinates, content and path. Then send a short terminal notice
with the status, exact report path and changed-file list. Do not paste the report
back into chat as a substitute for the file.

## 9. Stop conditions

Stop and return `BLOCKED` or `PARTIAL` without substantive mutation if:

- the AP or Kronika baseline is not the verified state;
- a handout is missing, or a path outside the nine-path allowlist would need to
  change;
- the closed 00 handout/notes, AP_DESTILLED, AP_DEFECTS, the Meta README, the
  AP repository or Kronika would need an edit;
- a product decision, a whole selection, a Stage 2 action or a Worker prompt
  would be needed;
- a NUC, test, browser, provider, secret or deployment boundary would be
  touched;
- the start state is lost and would require a transcript or out-of-root read;
- the report destination exists, its parent is not the exact verified directory,
  or the client cannot write the report;
- a material Cooperator decision is needed. Return
  `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and name the decision.

Do not repair the handouts, environment, prompt or plan. Preserve the first
causal failure and report the exact blocker.

## 10. Prompt satisfiability check

```text
VALIDATION–AUTHORITY  every required command is inside the positive authority;
                      no negative clause forbids the nine-path edit or the
                      report write.
ROUTING               one concrete value per identity route; fresh session 07;
                      Native planning mode not-used.
PERSISTENCE           report persistence owner assigned WORKER; direct-write
                      07_report_00.md; repository mutation exactly eight
                      handouts and the run map; host/remote none; trace
                      direct-write; Git none.
SPELLING              paths, SHAs, profile, status values and AP field spellings
                      come from the handouts, the pilot report, the new AP
                      owners and the published pins.
```

If you find a defect in this grant, report it under `Orchestration critique`
with MEASURED or LEAD. If it prevents a lawful refresh, stop `BLOCKED`; do not
improvise around it.

## 11. Authority expiry

This refresh grant expires at your terminal report, cancellation, or
supersession. It grants no commit, push, AP publication, pin, deployment, NUC,
acceptance or closure authority. The Cooperator commits the Meta trace. The
Cooperator is not a copy-paste courier: write the report to the exact trace
path, read it back, send only the short terminal notice, and stop.
