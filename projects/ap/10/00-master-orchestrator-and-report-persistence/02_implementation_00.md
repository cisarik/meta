# Fresh Implementation Worker prompt — AP update: run-scoped orchestration, mutation axes, direct-write reports

You are a genuinely fresh Implementation Worker for the canonical Analytic
Programming repository.

This is an implementation exchange inside an approved logical whole. The plan is
approved; do not re-plan it.

```text
Persistent role identity: WORKER
Worker session profile: Fresh Implementation Worker
Worker session target: fresh-worker-session
Native planning mode: not-used
Phase: Implementation
Task identity: AP-MO-02 — implement the approved AP update (ADR-0026)

Logical whole identity: master-orchestrator-and-report-persistence
Worker session ordinal: 02
Worker exchange ordinal: 01

Delivery route: manual Cooperator delivery
Reasoning recommendation: High — the change edits the sole normative protocol and its structural projections
Recommended context capacity: approximately 300k tokens
Independence required: no (implementation evidence is non-independent; a fresh independent acceptance follows separately)

Report persistence owner: assigned WORKER
Repository mutation: exactly the 14 AP paths listed below
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/02_report_00.md
Git authority: exact git add of the 14 paths and one local commit on main; no push, fetch, branch, tag, amend, reset, checkout, clean, stash, or remote/config write
```

Before substantive work, confirm that `Native planning mode: not-used` is the
actual client state (native Plan mode OFF). If the client has native Plan mode
enabled, do not start; return `BLOCKED` naming the contradiction. This is an
implementation grant, not a planning grant.

## 1. Authority and boundaries

```text
Positive authority
- Edit exactly the 14 AP repository paths listed in section 2, within the
  approved design in 01_report_00.md.
- Read-only inspection of /Users/agile/Projects/ap and the approved plan and
  evidence under /Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/.
- Read-only Git inspection: rev-parse, status, log, show, diff, ls-tree,
  ls-remote, cat-file, and similar non-mutating reads.
- Read-only shell text inspection: rg, grep, sed, tr, wc, sort, uniq, test -e.
- Read-only AP executable checks: sh -n ap, ./ap --help, ./ap bundle --help, and
  the read-only ./ap project check diagnostic in V12.
- Exact git add of the 14 paths and one local commit on main.
- Exact direct-write of the terminal report at the path above, if and only if
  that file is absent, followed by a complete readback.

Negative authority
- No edit, creation, deletion, rename, or chmod outside the 14 paths; the
  report file is the only file outside the AP repository.
- No change to ap, ap.project.conf, INFOSEC.md, PROMPT_ENGINEERING_PATTERNS.md,
  or .gitignore.
- No change to any historical ADR body (0004–0025).
- No change to /Users/agile/meta except the report file. Do not edit
  AP_DESTILLED.md, AP_DEFECTS.md, BRAINSTORMING.md, or the Meta README in this
  exchange; those are the later Meta projection exchange.
- No change to /Users/agile/Projects/kronika or its .ap pin, test constant,
  product code, docs, or NUC state. The approved plan's CD-3 is overridden:
  the Cooperator commits and pushes the Kronika pin; that is a later exchange,
  not yours.
- No git push, fetch, pull, merge, rebase, reset, restore, clean, stash,
  checkout, switch, branch, tag, remote, or config write. Do not amend.
- No new AP command, schema, managed-block, project-contract, or test-suite
  change.
- No NUC contact, host mutation, SSH, sudo, deploy, systemd, package manager,
  AppArmor, UFW, Tailscale, mount, storage, provider, browser, account, or
  secret/credential/token/private-key/cookie/private-host-value inspection.
- No fourth persistent role, no mass rename, and no historical rewrite.

Network: read-only public-ref verification with git ls-remote for the AP
repository is permitted. No other network use is authorized.
```

The report write is the only file write outside the AP allowlist and is
authorized by `Trace persistence`, not by the AP repository allowlist. If the
exact report path already exists, including an empty file, stop and return
`BLOCKED` without overwriting it.

## 2. Exact repository allowlist

Modify exactly these 13 files:

```text
AP.md
AP_ORCHESTRATOR.md
AP_WORKER.md
PROMPT_CONTRACTS.md
ARTIFACT_LIFECYCLE.md
GLOSSARY.md
FAQ.md
README.md
INTEGRATION.md
UPDATING.md
CHANGELOG.md
INTUITION.md
docs/adr/README.md
```

Create exactly this one file:

```text
docs/adr/0026-run-scoped-orchestration-mutation-axes-and-direct-write-reports.md
```

No other path may change. The candidate commit must have exactly these 13
modified paths and 1 added path relative to `73e20ef`.

## 3. Verified baseline — revalidate before mutation

```text
Repository: https://github.com/cisarik/ap (main)
Checkout: /Users/agile/Projects/ap
HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
Public main: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
Working tree and index: clean
Highest ADR: 0025
Next free ADR number: 0026
```

Verify with `git rev-parse HEAD`, `git ls-remote origin refs/heads/main`,
`git status --porcelain=v1`, and `git log -1`. A different HEAD, a moved public
main, a dirty tree/index, or an existing ADR-0026 is a new state. Stop and
report; do not reconcile it by mutation.

The AP repository has no test suite and no consumer `.ap` submodule. Its
declared `.venv/bin/python` is absent. `./ap doctor` is not applicable. Do not
repair the environment, create a `.venv`, or substitute an ambient interpreter.

## 4. Approved plan

The approved plan is:

```text
/Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/01_report_00.md
```

Read it in full before editing. It is the approved design and the source of the
acceptance criteria. This prompt is the implementation grant; the plan is not
authority by itself. If this prompt and the plan conflict, stop and report the
conflict; the Orchestrator will reconcile it prospectively.

The plan's material corrections are already verified by the Orchestrator:

- Kronika `tests/contract/test_ap_integration.py:10` pins the AP commit and must
  move atomically with the `.ap` gitlink in the later pin exchange.
- `ap update --check` and `ap update --apply` both fetch inside `.ap`; the later
  pin grant must authorize both.
- `doctor --candidate` allows only the `.ap` gitlink to differ; the test edit
  must come after candidate doctor.
- `Report author` and `Report persister` are not added as new fields; the
  existing `Report persistence owner` plus the three mutation axes are used.
- AP_DESTILLED §17.1–§17.8 are converted, not duplicated.
- A new logical-whole identity is not a coordinate-reset mechanism; it is
  lawful only for a materially changed objective.
- The pilot handout's `FULL` / `READY` values are non-AP; the pilot measures
  them, and AP permits `PASS`, `PARTIAL` or `BLOCKED`.
- AP at `73e20ef` names Meta in five places; neutralize them.

## 5. What to implement

Implement the approved plan's sections **E.1, E.2, E.3, H, I, J and K** in the
AP source repository. Do not implement the plan's section G (AP_DESTILLED), the
AP_DEFECTS disposition record in section F, the BRAINSTORMING status line, or
the Meta README update; those are the later Meta projection exchange. Do not
implement the Kronika pin or the pilot; those are later exchanges.

The plan's drafts are the design. Use them as written where complete, and make
the final text coherent with the current files. Every new normative rule in
AP.md must state its `Detection:` surface. Every projection must be a pointer
plus at most one orientation sentence; do not create a second semantic owner.

### 5.1 AP.md

Implement the plan's section E.1:

- Per-Role Minimum-Reading Spine: add the Run-Level Handouts reference for a
  `development-run` session scope or a received provisional handout.
- RF-06 capsule: include `session scopes` among the distinct labels.
- RF-09 capsule: append the pointer to `#standing-ledger-maintenance`.
- §2 last paragraph: add Orchestrator session scopes.
- §3: add the `orchestrator-session-scope` paragraph with the exact value set
  `logical-whole | development-run`, the explanatory name "Master Orchestrator",
  the no-role/no-authority boundary, the departure-recording rule, and the
  declaration on initialization.
- §5: add the `mutation-axes` paragraph with the three axes and the read-only
  qualification rule.
- §7: add the `prompt-satisfiability-check` paragraph from plan section J.
- RF-19: add the `consumed-coordinates` paragraph from plan section J; replace
  the Meta Git phrase with the neutral trace phrase; add the direct-write
  default paragraph after the existing "Other authorized capable Workers may
  persist their own reports directly."
- Planning Budget and Expiry: add the blocked-planning sentence from section J.
- §13: add the handout revalidation record to the per-whole notes sentence; add
  the `standing-ledger-maintenance` paragraph from section K; reconcile the
  existing "bounded snapshot of the candidate observations under consideration"
  sentence with the new "every active entry of the declared ledgers available
  to it" requirement (Orchestrator condition 6). Record the partial
  supersession in ADR-0026.
- §14: add the `### Run-Level Handouts` subsection before Continuation
  Bootstrap, with an explicit anchor and the run-map/provisional-handout/
  revalidation text from plan section E.1; add the Stage 1 and Stage 2
  sentences.
- §18: add `mutation axes or persistence fields contradict each other` to the
  stop list.
- §19: add the four anti-patterns from plan section E.1.

### 5.2 AP_ORCHESTRATOR.md

Implement the plan's section E.2:

- Continuation Bootstrap: Stage 1 provisional-handout revalidation; Stage 2
  "run map ≠ selection".
- New `## Run-Scoped Orchestration` section after Rotation and Restoration,
  with the operational checklist from the plan.
- Decision Table: one run-level handoff row.
- Worker Exchange Coordinates: one consumed-coordinates bullet.
- Prompt Construction: step 4 points to the satisfiability check; step 5
  declares the three mutation axes.
- Per-Whole Orchestrator Notes: use the activated trace's own documentation,
  not a Meta path; add the revalidation record.
- Artifact and Ledger Governance: one pointer to the standing duty.

### 5.3 AP_WORKER.md

Implement the plan's section E.2:

- Reporting: the direct-write paragraph, including the native-plan client
  completion route and the readback/no-other-file rule.
- Worker Exchange Coordinates and Trace Boundary: check that the axes agree
  before writing; contradictory axes stop under §18.

### 5.4 PROMPT_CONTRACTS.md

Implement the plan's section E.2:

- Common Worker Task Fields → Authority: the three axis rows and a
  `#### Mutation Axes Record`.
- Cooperator Delivery and Trace Destination Record: the RF-19 default sentence
  and consistency rules P1–P5.
- Source-Read-Only Review Example: the three axis lines after
  `Archival: wait-for-report`.
- Worker Exchange Identity: the Blocked First Exchange Example.
- Trace-Local Filename Mapping: the `02/01 -> 02_planning_00.md` line.
- Planning Record: the corrected-initial shape.
- Fresh Orchestrator Restoration: `Orchestrator session scope` and
  `Development run identity`.
- New `#### Run Map Record`, `#### Provisional Handout Marker` and
  `#### Handout Revalidation Record`.
- AP Integration Task: the AP Update Task bullets from the plan.
- The "Example using Meta-local storage" phrase becomes "Example using an
  activated trace's local storage grammar".

Do not add `Report author` or `Report persister` fields. Use the existing
`Report persistence owner` plus the three axes. Do not add
`correction-required` to any AP enum; it is an Orchestrator disposition, not a
Worker phase result.

### 5.5 ARTIFACT_LIFECYCLE.md

Implement the plan's section E.2/E.3:

- New `## Run Maps and Provisional Handouts` section using the lifecycle in
  plan section D.
- Two distribution-table rows.
- Neutral wording at the existing Meta references (lines 162 and 183 in the
  current file; re-measure).

### 5.6 INTEGRATION.md and UPDATING.md

Implement the plan's section E.2:

- INTEGRATION: one pointer to the standing duty; the trace-grammar paragraph
  may name run-map and handout files and default delivery to direct-write.
- UPDATING: one review-checklist item covering the mutation axes, direct-write
  default, provisional handouts, consumed coordinates, and any consumer file
  that pins the AP commit in the same pin change.

### 5.7 Explanatory and historical files

Implement the plan's section E.3:

- GLOSSARY.md: one-line rows for Orchestrator session scope, Development run,
  Run-scoped Orchestrator ("Master Orchestrator"), Run map, Provisional
  handout, Handout revalidation record, Mutation axes, Trace persistence,
  Direct-write report persistence, Prompt satisfiability check, and Consumed
  coordinates, each with a link.
- FAQ.md: update "Can a Planner or Worker save its own report?"; add "What is a
  run-scoped (Master) Orchestrator?"; add "What happens to coordinates after a
  blocked exchange?"; add the provisional-handout pointer to "Who can author a
  handout…?".
- README.md: one Reading Order row for run-level preparation.
- INTUITION.md: add `session scopes` to the no-fourth-role sentence.
- CHANGELOG.md: insert the plan's Unreleased entry at the top.
- docs/adr/README.md: one ADR-0026 row and one paragraph in the style of
  ADR-0025.
- docs/adr/0026-run-scoped-orchestration-mutation-axes-and-direct-write-reports.md:
  create the ADR from plan section H, including context, decision,
  semantic ownership and projections, alternatives rejected, partial
  supersession, compatibility, consequences, validation, rollback, and related
  documents. Do not rewrite any historical ADR body.

## 6. Orchestrator conditions

The following conditions are part of the approved plan envelope. Apply the ones
that belong to this exchange; the later exchanges will apply the rest.

1. Do not add `correction-required` to any AP phase-result enum. The acceptance
   Worker will use `PASS`, `PARTIAL` or `BLOCKED`; `correction-required` is an
   Orchestrator disposition.
2. The three mutation axes are mandatory in every newly issued Worker grant.
   This prompt itself carries all three.
3. The later pin grant must authorize the fetch inside `.ap` for both
   `ap update --check` and `ap update --apply`; do not add a fetch authority to
   this implementation exchange.
4. The later Meta projection exchange corrects AP_DEFECTS §0.0 and
   AP_DESTILLED §17.4 to the rule that a new logical-whole identity is lawful
   only for a materially changed objective, not as a coordinate-reset
   mechanism. In this exchange, the AP.md RF-19 text must state that rule.
5. The later Meta projection exchange uses the actual trace paths
   (`00_RUN_MAP.md`, `00_notes.md`), not the non-existent
   `00_master_handout.md`.
6. AP.md §13's "bounded snapshot of the candidate observations under
   consideration" sentence is reconciled with the new "every active entry"
   requirement. ADR-0026 records the partial supersession.
7. The later publication and pin grants state the exact `Host/remote mutation`
   or Git remote authority for the push. This implementation exchange has
   `Host/remote mutation: none` and does not push.

## 7. Validation — run and report exactly

Run the following from `/Users/agile/Projects/ap`. Record the exact commands and
results in the report.

```text
V1  git rev-parse HEAD; git log -1 --format=%P
    -> one commit whose parent is 73e20ef80b88700d5fcbc397cd8edd4fc425869f
V2  git diff --name-status 73e20ef80b88700d5fcbc397cd8edd4fc425869f..HEAD
    -> exactly the 13 M + 1 A paths of section 2
V3  git diff --check 73e20ef80b88700d5fcbc397cd8edd4fc425869f..HEAD
    -> clean
V4  git diff --quiet 73e20ef80b88700d5fcbc397cd8edd4fc425869f..HEAD -- ap ap.project.conf INFOSEC.md PROMPT_ENGINEERING_PATTERNS.md .gitignore
    -> exit 0
V5  git diff --name-only 73e20ef80b88700d5fcbc397cd8edd4fc425869f..HEAD -- docs/adr
    -> only 0026 and README.md
V6  sh -n ap; ./ap --help; ./ap bundle --help
    -> exit 0 for each
V7  Link and anchor check on the changed files:
    extract relative link targets; test -e each relative file; every #anchor
    matches an explicit <a id> or a heading slug; new AP.md subsections carry
    explicit anchors.
    -> no missing target, no unresolved anchor
V8  Heading check on the changed files:
    collect headings; derive slugs; sort | uniq -d
    -> no duplicate slug; the changed-file tree matches section 2
V9  Spelling and neutrality check:
    every section I spelling is defined once in PROMPT_CONTRACTS.md and used
    verbatim elsewhere;
    rg -n -i 'report persister|report author:' -> only the ADR-0026 alternatives;
    rg -n -w Meta --glob '!docs/adr/**' --glob '!CHANGELOG.md' -> no match.
    -> all three pass
V10 Single-owner check:
    every new normative sentence is in AP.md and states Detection;
    each projection is a pointer plus at most one orientation sentence.
    -> no second semantic owner
V11 Scenario walk-through S1–S14 from the approved plan:
    record the expected outcome and the candidate-text evidence for each.
    -> every scenario is consistent
V12 ./ap project check --root /Users/agile/Projects/ap --baseline 73e20ef80b88700d5fcbc397cd8edd4fc425869f
    -> expected "OK trusted baseline contract" followed by the declared-CPython
       ERROR; record the limitation class as a pre-existing environment
       limitation, not repaired. Do not reproduce a private host path.
```

Limitations: V7 approximates GitHub slugs with `rg`, `sed` and `tr`; headings
with punctuation are checked by hand. No Python is used. Do not invent a test
suite. Do not run a broad project suite. Do not run Kronika checks.

## 8. Git authority

After the candidate is complete and V1–V12 are recorded:

```text
git status --porcelain=v1      -> exactly the 14 paths; no other change
git diff --stat                -> inspect
git add <the exact 14 paths>   -> one staged change set
git diff --cached --name-status -> exactly the 13 M + 1 A paths
git commit -m "docs: add run-scoped orchestration and direct-write report persistence (ADR-0026)"
git rev-parse HEAD             -> candidate SHA
git status --porcelain=v1      -> clean
```

Do not push. Do not amend. Do not create a branch or tag. Do not fetch. The
Cooperator publishes the accepted commit in a later exchange. The commit is a
local candidate until then.

If the commit is created incorrectly, do not reset or amend; stop and report the
exact state. A correction is a later exchange with its own grant.

## 9. Report contract

Write your terminal report directly to:

```text
/Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/02_report_00.md
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
3  Phase-qualified result: implementation-PASS for a complete validated candidate; not-applicable for a BLOCKED or PARTIAL report without a phase PASS. Do not invent another value.
4  Start commit 73e20ef...; end commit <candidate SHA>.
5  Changed files and purpose: exactly the 14 paths; the report file only outside AP.
6  Tests and validation: V1–V12 exact commands and results; V12 expected error;
   no full suite; no Kronika checks.
7  Commit and push result: local commit <SHA> on main; no push.
8  Deviations, risks, or missing evidence.
9  One smallest next step: fresh independent acceptance of the exact candidate.
10 Exactly one report justification: new-mutation.
11 Authority-expiry statement.
12 Compact critique:
   Orchestration critique:
   MEASURED: none | <verified finding; evidence; effect; smallest correction>
   LEAD: none | <unverified possibility; cheapest useful check>
13 Resolved Execution Issues / Near-Misses: none | <exact>
14 Pre-Existing Failure Classification: none | <complete classification; the
   AP .venv error is pre-existing and not candidate-caused>
15 Logical-whole closure: not-closed.
```

The report must state that implementation evidence is non-independent and that
it does not certify acceptance, publication, the Kronika pin, or closure.
Read the report back completely; verify its first line, coordinates, content,
and path. Then send a short terminal notice with the status, candidate SHA,
exact report path, and any requested hash. Do not paste the report back into
chat as a substitute for the file.

## 10. Stop conditions

Stop and return `BLOCKED` or `PARTIAL` without substantive mutation if:

- native Plan mode is ON instead of `not-used`;
- the AP repository is not at `73e20ef`, public main differs, the tree/index is
  dirty, or ADR-0026 already exists;
- a path outside the exact 14-path allowlist would need to change;
- a required file is missing or the approved plan conflicts with the current AP;
- a validation command fails in a way that cannot be resolved inside this grant;
- a change would touch `ap`, `ap.project.conf`, `INFOSEC.md`,
  `PROMPT_ENGINEERING_PATTERNS.md`, `.gitignore`, a historical ADR body, Meta,
  Kronika, the NUC, a provider, a browser, or a secret/credential boundary;
- the report destination already exists, the parent is not the exact verified
  directory, or the client cannot write the report through a permitted route;
- a material Cooperator decision is needed. Return
  `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and name the decision.

Do not repair the environment, the repository, the prompt, or the plan. Preserve
the first causal failure and report the exact blocker.

## 11. Prompt satisfiability check

This grant has been checked before issue:

```text
VALIDATION–AUTHORITY  every required command is inside the positive authority;
                      no negative clause forbids V1–V12 or the report write.
ROUTING               one concrete value per identity/route field; no unresolved
                      placeholder in a routing field; the plan's future SHAs are
                      resolved by the later exchanges, not this one.
PERSISTENCE           report persistence owner `assigned WORKER`; direct-write
                      exact path; repository mutation exact 14 paths;
                      host/remote none; trace direct-write; Git add/commit exact.
SPELLING              paths, profile names, commands, and commit message are
                      copied from the approved plan and their durable owners.
```

If you find a defect in this grant, report it under `Orchestration critique`
with MEASURED or LEAD. If it prevents a lawful implementation, stop `BLOCKED`;
do not improvise around it.

## 12. Authority expiry

This implementation grant expires at your terminal report, cancellation, or
supersession. It grants no acceptance, publication, Kronika pin, Meta
projection, deployment, or closure authority. A fresh independent acceptance
Worker will receive a separate complete prompt. The Cooperator is not a
copy-paste courier: write the report to the exact trace path, read it back, and
send only the short terminal notice. Then stop.
