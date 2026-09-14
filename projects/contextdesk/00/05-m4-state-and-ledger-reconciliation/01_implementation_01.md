Logical whole identity: m4-state-and-ledger-reconciliation
Worker session ordinal: 01
Worker exchange ordinal: 02
Persistent role identity: WORKER
Worker session target: current-worker-session
Worker session profile: Implementation Worker
Phase: implementation
Task identity: CONTEXTDECK-M4-STATE-LEDGER-RECONCILIATION-IMPLEMENTATION
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to the exact current Worker session
Continuity anchor: terminal planning report `01_report_00.md` for Worker
exchange 01/01 — the ORCHESTRATOR-accepted decision-complete plan — written in
this same session
Authority renewal: prior planning authority expired at that terminal report;
this prompt is a complete renewed implementation grant to the same session
Reasoning recommendation: Medium
Reasoning basis: bounded mechanical execution of an accepted decision-complete
plan (exact replacement texts, one small typed desktop-id predicate hardening
with an existing test target, one local commit and one normal push); no live
host mutation and no open design question remains.
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: cross-cutting reversible documentation plus one bounded
semantic-validator hardening with focused tests and ordinary revert; no live
host, device, desktop, launch, broker, packaging, or production mutation.
Fresh independent acceptance is required because a semantic validator changes.
Internal delegation: prohibited

# ContextDeck — implement the M4 state & ledger reconciliation

You are the WORKER session that produced the accepted plan. Native Plan Mode
must be OFF for this exchange. Do not use subagents.

This prompt grants one bounded repository-only implementation slice: apply the
accepted plan exactly, add the admitted typed desktop-id hardening with its
causal regression, validate, create and push one normal product commit, persist
the terminal report in META, then stop. You do not accept your own candidate and
never close the logical whole.

Continuity and renewal: prior planning authority expired at the terminal
planning report. Retained context, the plan text, and this conversation are
convenience and evidence, not authority; re-verify repository and environment
state before acting and stop on any conflict with current repository evidence.
Evidence produced in this session is non-independent.

Critical: no live host mutation, no application launch, no KWin bridge reload,
and no real KWin/OpenRGB/broker/device operation may occur during this exchange.
Those remain COOPERATOR-owned IRL operations for a later, separately authorized
run. This exchange edits, tests, commits, and pushes repository content only.

## Accepted plan and Plan-to-Execution transition

ORCHESTRATOR reconciliation: accepted
Accepted plan (frozen design):
`projects/contextdesk/00/05-m4-state-and-ledger-reconciliation/01_report_00.md`
Planning pair commit: `597d576`

ORCHESTRATOR reconciliation decisions that modify the plan's execution envelope:

1. **Ceiling widened by exactly two paths.** Add
   `docs/adr/0001-broker-suspend-resume-sleep-hook.md` and `docs/testing-m3.md`
   to the plan's allowlist, because both carry the same verified class of stale
   state inside this whole's objective. The exact replacement texts are given
   below; no other out-of-ceiling path is admitted.
2. **Access-profile policy item (plan §3.2 A3, §3.3 B1): not authorized in this
   grant.** Leave `AGENTS.md:52–55`, `AGENTS.md:95–96`, and `ROADMAP.md:7`
   byte-identical and record the open observation in the terminal report. Do not
   apply the plan's conditional access-profile text.
3. **Exact tense text for `docs/testing-m4.md`** is supplied below (the plan
   commits to the correction but did not fix its wording).
4. **One normal non-force product push is authorized** for the single commit
   (M4 precedent). META Git remains COOPERATOR-owned.
5. **The changed-path allowlist is the 14 paths below**, not the plan's 12.

The plan is decision-complete for this whole. Planning authority has expired.
This prompt is the separate Plan-to-Execution event. Do not reopen planning,
change the objective, or treat retained text as authority beyond this exact
envelope.

Implementation authority: explicit
Exact baseline: `293158887e4228a42b9c64bda7d4f0bd32fb4ec9`
Changed-path allowlist: the exact 14 paths in "Exact changed-path allowlist"
Implementation boundaries: apply the accepted plan's exact texts plus the two
widened edits and the supplied tense text, in repository content only; no live
host mutation, launch, bridge reload, or device action
Independence required: no for this implementation; yes for the required later
separate fresh acceptance

## Authoritative continuity boundary

Use this exact wording wherever M4 state is restated:

> M4 workspace session manager is code-accepted (Slice A on `aca6c68`, Slice B on
> `db9ddc1`); its live IRL run is deferred by explicit COOPERATOR decision. M4 is
> not closed, and code acceptance is not live or physical acceptance.

Use this exact wording wherever M3 state is restated:

> M3 workspace-aware lighting is code-accepted on `502ae75...`; its physical
> five-zone IRL observation is deferred by explicit COOPERATOR decision. M3 is
> not closed, and code acceptance is not physical acceptance.

For M2, preserve the substantive park claims word-for-word wherever they are
restated (the named live G4 slices are accepted; the M2 logical whole remains
open; M2 is parked with G3 host-mitigated on the authorized reference host; full
G4 remains open). The historical clause "the next bounded whole is M4 workspace
session manager" is superseded by the current whole; apply the plan's smallest
truthful replacement exactly as given in plan §3.1 and §3.3.

Do not issue, revive, or simulate `27_deployment_00.md`; do not reopen G3; do not
touch input grabbing.

## Exact repositories and immutable gates

Canonical product repository: `https://github.com/cisarik/contextdesk`
Required branch: `main`
Required product HEAD and public `main` before mutation:
`293158887e4228a42b9c64bda7d4f0bd32fb4ec9`
Required parent: `db9ddc1f923f44e26f7f1d58df7446306bbdf64a`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

Canonical META repository: `https://github.com/cisarik/meta.git`
Required public META baseline:
`597d576` (a later verified descendant is acceptable after ancestry and
changed-path review proves no artifact of this whole changed)
This whole's trace destination:
`projects/contextdesk/00/05-m4-state-and-ledger-reconciliation/`

Repository checkout topology: standalone product checkout on `main`
Working-copy topology: canonical product checkout
Topology rationale: one accountable Worker owns one coherent reconciliation
change and one commit; `build/` is git-ignored by the repository

Execution route: this repository declares no `ap.project.conf` operation; the
exact `cmake`/`ctest` commands below are the project-owned build and test
commands from `AGENTS.md` and `CMakeLists.txt`.

Before any product or META file mutation:

1. Verify the complete prompt, the exact current Worker session, Native Plan
   Mode OFF, coordinates `01/02`, the renewed authority, and no subagents.
2. Verify canonical remote, active `main`, exact HEAD, clean state, no Git lock,
   matching AP gitlink/checkout, and `./.ap/ap doctor` PASS (variant `stable`).
3. Prove public product `main` equals the exact baseline with direct
   `git ls-remote`. Do not pull, merge, rebase, switch, reset, clean, stash, or
   retarget.
4. Verify META public `main` is the baseline or a later verified descendant;
   review ancestry and changed paths.
5. Verify the trace directory is real and contains `00_handout.md`,
   `00_notes.md`, `01_planning_00.md`, and `01_report_00.md`; the report
   destination `01_report_01.md` must be absent before the write.
6. Confirm the accepted plan `01_report_00.md` is readable and unchanged.
7. Read current files before editing; every needed path must be inside the
   allowlist.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-12, RF-16, RF-18, RF-19, implementation
  authority, Git safety, validation, stopping conditions;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Implementation Authority
  Record, exchange/trace contract, validation ladder, delivery record,
  Session-and-Mode;
- the accepted plan `01_report_00.md` — all of §3;
- `AGENTS.md`, `README.md`, `ROADMAP.md`;
- `docs/specification.md`, `docs/architecture.md`, `docs/operations.md`,
  `docs/testing-m4.md`, `docs/testing-m3.md`;
- `docs/adr/0001-broker-suspend-resume-sleep-hook.md`,
  `docs/adr/0002-host-desktop-mutation-authority.md`,
  `docs/adr/0003-workspace-assignment-schema.md`,
  `docs/adr/0004-typed-application-launch.md`, `docs/adr/README.md`;
- `src/core/Types.h`, `src/workspace/ApplicationLauncher.cpp` (read-only
  reference for call sites), `tests/unit/test_application_launcher.cpp`,
  `CMakeLists.txt` (test registration only);
- the M2 record `27_report_00.md`, §2.3 and its pre-existing-classification
  paragraph, for the G4-remainder drift corroboration.

## Product invariants

- G213 only, USB `046d:c336`; five RGB zones, never per-key.
- Session app never opens raw keyboard nodes; broker stays static/inactive.
- Event-driven KWin identity; never `xdotool`/`wmctrl`/`xprop`; no title polling.
- Typed action/launch model only; no shell strings.
- Captions, titles, desktop names, and desktop UUIDs are sensitive: never
  logged, never persisted in prompts, reports, or META.
- `kwinrulesrc` is never written by M4.
- No autostart, no M5 system integration, no input-remapper operation, no
  suspend/DPMS behavior, no external source copying while licensing is
  unresolved.
- Repository documentation stays English, public-facing, readable, and scannable.

## Implementation contract

### 1. Apply the accepted plan exactly

Apply the exact texts of the accepted plan `01_report_00.md`:

- §3.1 README R1–R4 (front-door block, "Named workspace sessions" bullet,
  M4 status-table row final sentence, Hardware evidence row);
- §3.2 AGENTS.md A1–A2 (full "Current repository state" replacement; the stale
  M2 roles bullet) — **A3 is not authorized**;
- §3.3 ROADMAP B2–B12 (current-state bullets, parked-M2 paragraph, P1 row,
  G7 dependency line, G4 gate row, M3-backlog sentence, M4 backlog heading and
  classification, ledger-disposition paragraph, G4-remains-open paragraph,
  next-remaining-M2 paragraph) — **B1 is not authorized**;
- §3.4 ADR status replacement texts for 0002, 0003, and 0004;
- §3.5 strengthened `workspaceDesktopIdLooksValid` body and its causal
  regression slots in `tests/unit/test_application_launcher.cpp`;
- §3.6 QML sentence in `docs/testing-m4.md`;
- §3.7 no action for the orphaned checkpoint (recorded in the ROADMAP ledger
  paragraph only);
- §3.8 consistency fixes: architecture S1 text, operations E1–E8, specification
  KService wording, checkpoint disclosure.

Treat the plan's line numbers as locators: verify surrounding anchors before
replacing, and never replace a block whose actual content differs from the
plan's quote; if it differs materially, stop `PARTIAL` and report the exact
difference.

### 2. Supplied exact edits for the widened paths and the tense fix

**`docs/adr/0001-broker-suspend-resume-sleep-hook.md`, replace the current
Status lines (lines 3–4) with:**

```text
Status: accepted. The sleep hook is implemented and code-accepted with the M2
tree; one live suspend/resume cycle is a recorded named slice (Session 22),
while hibernate/hybrid-sleep and the production path remain open.
```

**`docs/testing-m3.md`, replace the current opening sentence (lines 3–4) with:**

```text
Numbered procedure for a **later** COOPERATOR physical run after the public
implementation candidate was separately code-accepted (`502ae75...`); code
acceptance is not physical acceptance.
```

**`docs/testing-m4.md`, replace the current opening sentence (lines 3–5) with:**

```text
Numbered procedure for a **later** COOPERATOR run after the public Slice B
implementation candidate was separately code-accepted (`db9ddc1`) and after an
explicit mutation grant.
```

**`docs/testing-m4.md`, QML sentence (plan §3.6):** after the paragraph that
ends "...automated tests alone do not establish live behavior." add exactly:

```text
QML runtime behavior has so far been validated only by build-time compilation;
these steps are its first runtime validation.
```

### 3. Access-profile policy item

Do not change `AGENTS.md:52–55`, `AGENTS.md:95–96`, or `ROADMAP.md:7`. Record in
the terminal report that the plan's conditional access-profile wording remains
an open observation requiring explicit COOPERATOR confirmation.

## Validation

Run, in order, and report counts from real output:

```sh
./.ap/ap doctor
cmake -S . -B build -G Ninja
cmake --build build

ctest --test-dir build --output-on-failure \
  -R '^(test_application_launcher|test_profile_persistence|test_profile_resolver|test_workspace_plan)$'

ctest --test-dir build --output-on-failure

git diff --check
git diff --name-only
git status --short
```

Content checks (report exact command or inspection result):

- `README.md`: no `implementation candidate` and no `not accepted and not
  live-verified`; the exact M3 and M4 wording present; no widened claim.
- `docs/adr/*`: no `accepted for the M4 tree` and no `Implementation-candidate`.
- no `KApplicationTrader` anywhere in `docs/` or `src/` after the fix.
- `AGENTS.md`: M1–M4 state present; M2/M3/M4 exact wording present; the
  access-profile lines byte-identical to the baseline.
- `ROADMAP.md`: ledger dispositions present; no remaining `M4 is now its own
  current whole`; P1 row and G7 line consistent with G1 closed and G7 pending.
- `src/core/Types.h`: the new predicate rejects `.desktop`, `..desktop`,
  `a..desktop`, `.a.desktop` and still accepts `a.desktop`,
  `org.kde.dolphin.desktop`, `org.kde.dolphin`, `kde.dolphin`.

The full registered 21-test suite is required. Do not install packages, skip a
required test, or weaken a gate.

## Exact changed-path allowlist (14 paths)

Modify only this set; the ceiling is a maximum, not a requirement:

```text
README.md
AGENTS.md
ROADMAP.md
docs/specification.md
docs/architecture.md
docs/operations.md
docs/testing-m4.md
docs/testing-m3.md
docs/adr/0001-broker-suspend-resume-sleep-hook.md
docs/adr/0002-host-desktop-mutation-authority.md
docs/adr/0003-workspace-assignment-schema.md
docs/adr/0004-typed-application-launch.md
src/core/Types.h
tests/unit/test_application_launcher.cpp
```

Do not change `.ap/`, `src/broker/`, broker IPC, `src/workspace/`, `src/context/`,
`src/app/`, `ui/`, `kwin/`, `packaging/`, `CMakeLists.txt`, license files,
dependencies, lockfiles, generated files, M1/M2 test procedures, hardware
evidence, or host configuration.

If one additional product path is genuinely required, stop `PARTIAL`, preserve
the coherent state without committing, and name the exact path and reason. Do
not silently widen the allowlist.

## Command, dependency, host, and data authority

Allowed commands: read-only source/Git inspection; `./.ap/ap doctor`; existing
CMake/Ninja build; the exact test routes above; `git diff`, `git status`,
exact-path staging, one commit, one normal push, direct public-ref readback
Forbidden commands: destructive Git recovery; force push; history rewrite;
branch/tag/remote/config changes; package manager; sudo; service/device tools;
live D-Bus calls to KWin; application launch; OpenRGB CLI; broker operations
Dependency authority: none; no package, manifest, lockfile, or toolchain change
Host authority: none
Device authority: none
Secret authority: none
Network authority: canonical product/META Git public verification and the one
authorized normal product push only; if HTTPS fails, record the bounded symptom
and retry once with `git -c http.version=HTTP/1.1`, never a mirror

No raw input, raw event lines, key names, scan values, typed content, serials,
host addresses, host keys, passwords, private paths, desktop IDs/names, window
captions, or unredacted logs may enter code logs, documentation, prompts,
reports, or META.

## Git publication authority

After all focused and full tests pass and exact-path review proves the diff is
inside the allowlist:

1. Inspect `git diff --check`, `git diff --name-only`, `git status --short`, and
   the complete diff.
2. Stage only exact changed allowlisted product paths. Never `git add .`/`-A`.
3. Create exactly one normal commit with subject:
   `Reconcile M4 state docs and dispose of carried ledger candidates`
4. Push only `main` to canonical origin with a normal non-force fast-forward.
5. Verify local HEAD, `origin/main`, and direct public `ls-remote` all equal the
   new commit; parent equals the exact baseline; changed paths are the
   authorized subset.

If commit/push is unavailable, report `PARTIAL` with exact state. Product
publication grants no host mutation, launch, deployment, acceptance, or closure.

## Validation and acceptance envelope

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: `test_application_launcher`, `test_profile_persistence`,
`test_profile_resolver`, `test_workspace_plan`
Affected tests: the new causal accept/reject regressions in
`test_application_launcher`; the full suite covers shared predicate users
New causal regression: required — the pathological desktop-id forms
(`.desktop`, `..desktop`, `a..desktop`, `.a.desktop`) are accepted on the
baseline and rejected after the fix; existing coverage has no boundary cases;
the new slots close that gap with a parent/candidate sign change
Broad or full suite: required-because `CMakeLists.txt` owns the suite, no lint
config or CI exists, and the predicate is shared by persistence, plan, and
controller users
Runtime or testbed: local CMake/Ninja build only; no live session
Independent acceptance: required-separate-fresh-worker

Evidence tier: E2
Authorized implementation stages: predicate + tests → documentation → one
commit → one normal push → public verification → terminal report
Combined implementation envelope: allowed
Implementation stage gates: focused tests pass; full CTest passes; diff inside
the allowlist; no host/desktop/launch/bridge/device side effect occurs
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: the exact public baseline `2931588...`; one
revertable commit
Activated stricter profile: none
Terminal implementation report point: one terminal report after commit, push,
and public-ref verification

Implementation-PASS is non-independent repository evidence. A separate fresh
Worker must accept the immutable public candidate before any COOPERATOR IRL run.
Only the COOPERATOR can establish live desktop/launch/placement behavior.

Do not claim acceptance-PASS, deployment-PASS, production readiness, physical
acceptance, M2/G4 closure, M3 closure, M4 closure, M4 live desktop/launch/
placement behavior, autostart, hibernate/hybrid sleep, general input-remapper
coexistence, remapping, M5, per-key RGB, license selection, or measured
control-to-zone placement.

## Exact META trace persistence

External trace disposition: configured
Trace discovery: META README and the exact trace destination
Trace project key: contextdesk
Trace logical-whole projection identity: 05-m4-state-and-ledger-reconciliation
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_implementation_01.md
Destination path: projects/contextdesk/00/05-m4-state-and-ledger-reconciliation/
Report filename: 01_report_01.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR for META; WORKER for the one product commit
Archival: wait-for-report

The ORCHESTRATOR persists this exact prompt bytes to
`projects/contextdesk/00/05-m4-state-and-ledger-reconciliation/01_implementation_01.md`
before delivery. The WORKER may write only the report file at
`projects/contextdesk/00/05-m4-state-and-ledger-reconciliation/01_report_01.md`
in the COOPERATOR-owned META working tree.

Before substantive implementation, verify the already-persisted prompt file
exists and is byte-identical to the received prompt; read it back completely.
Stop on a non-identical or unsafe collision. Do not alter `00_notes.md`,
`00_handout.md`, `01_planning_00.md`, or `01_report_00.md`, create a handout, or
write any other META path.

After implementation, write the complete terminal report first to the report
path, read it back completely, and verify the header, coordinates, content, and
filename. Do not overwrite a non-identical existing report. Do not stage,
commit, push, pull, merge, rebase, or otherwise mutate META Git history or refs.
The COOPERATOR archives the exact prompt/report pair together in one first-add
commit only after the report exists.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

It must echo the opening persistent-role and three coordinate fields exactly
once, with their values unchanged, and include:

- status: `PASS`, `PARTIAL`, or `BLOCKED`;
- phase-qualified result: `implementation-PASS` only when every gate, focused
  and full validation, one commit/push, and public-ref verification pass;
- start and end product commit, baseline, AP pin, public META baseline, and the
  accepted-plan identity;
- exact changed product paths with purpose and proof that every other path,
  `.ap`, broker, packaging, dependencies, and host state remained unchanged;
- the applied plan sections and the two widened edits, with the exact
  before/after for the predicate and the tense fixes;
- focused and full CTest results with counts from actual output;
- explicit statement that no real KWin/OpenRGB/device/broker/host/desktop/
  launch/bridge-reload operation ran;
- exact commit, push, public-ref equality, parent, and changed-path evidence;
- the open access-profile observation and the recorded ledger dispositions;
- META prompt/report persistence and readback, with META Git publication
  remaining COOPERATOR-owned;
- deviations, resolved issues/near-misses, pre-existing failure classification,
  residual risks, missing evidence, and plan fidelity;
- exactly one smallest next step: ORCHESTRATOR reconciliation followed, only if
  accepted, by a separate fresh independent code-acceptance Worker;
- exactly one `Report justification: new-mutation`;
- `Resolved Execution Issues / Near-Misses: none` or a complete entry;
- `Pre-Existing Failure Classification: none` or a complete entry;
- compact critique:

  `Orchestration critique:`

  `MEASURED: none | <verified finding; evidence; effect; smallest correction>`

  `LEAD: none | <unverified possibility; cheapest useful check>`

- exactly one `Logical-whole closure: not-closed` line;
- the exact authority-expiry sentence below.

Explicit non-claims: no acceptance-PASS, deployment-PASS, production readiness,
physical acceptance, M2/G4 closure, M3 closure, M4 closure, M4 live
desktop/launch/placement behavior, autostart, hibernate/hybrid sleep, general
input-remapper coexistence, remapping, deck behavior, M5 integration, per-key
RGB, license selection, or measured control-to-zone placement; no claim that
tests prove live behavior; no claim that Session 27 was an independent Worker
result.

Authority for this Worker expires at this terminal report.

## Stop conditions

Stop before mutation on a non-current or contaminated session, Native Plan Mode
mismatch, coordinate/authority contradiction, product/AP/META identity or
public-ref failure, dirty/unexplained worktree, unsafe trace path/collision,
unavailable accepted plan, or need for a non-allowlisted path, an additional
dependency, host/desktop mutation, launch, device access, secret, or subagent.

After mutation, stop `PARTIAL` without committing when a planned replacement
does not match the actual anchor content, when a required test fails and cannot
be corrected in scope, or when any required gate cannot pass. Preserve the first
causal failure; do not weaken, skip, or endlessly rerun gates.

If validation passes but commit/push/public verification fails, preserve the
exact safe state and report `PARTIAL`. Use `PASS` only for one fully validated
and publicly verified implementation commit.

Stop immediately after the terminal report. Do not perform any live desktop
mutation, launch, bridge reload, acceptance, deployment, or host enablement
under this authority.
