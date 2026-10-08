# Authoritative Worker prompt — Worker session 25, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `25`, exchange `01`. Stored under the
Meta filename mapping as `25_planning_00.md`, with report destination
`25_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 25
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner, read-only
Task identity: KSI-PLAN-CLOSE2 — plan the remaining identity sequence to logical-whole closure
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. This is the closure plan for a logical whole that has already
spent twenty-four Worker sessions and nineteen published commits. You are not
renaming strings. You are re-deriving the current state of a large migration
from primary repository evidence, reconciling it against an accepted
fifteen-step plan and a restoration handout, and producing a decision-complete
plan for every remaining cut through `CLOSE`. Most of the value you add will be
in what you find that the plan, the handout and the preceding Orchestrator all
got wrong.

## Mandate

Produce **one completion plan for `kronika-sole-identity`, from the current
state through closing the logical whole**, covering:

- the accepted remaining cuts: `C-DATA`, `C-LOCAL`, `C6`, `C7-A`, `C7-B`,
  `C8-A`, `C8-B`, `C9-A`, `C9-B`, and a terminal read-only `CLOSE`;
- the three named obligations that exist in reality but in no accepted cut
  (below);
- the deferred Cooperator request for a clean-install runbook (below).

The plan must be executable by fresh Implementation Workers who have none of
this context. For every work item state the exact mutation, the exact authority
a Worker would need, the evidence that closes it, the machine-checkable proof,
its rollback, and its preconditions. Every future implementation report must
also identify its exact starting commit, tested commit, publication commit and,
when relevant, served commit.

**You have no authority to change anything.** You produce a plan, not a
mutation.

Three things are wanted beyond sequencing, and they matter more than the
sequencing:

1. **Re-derive, do not transcribe.** Establish the current state from the
   repository, the ledger and read-only Git evidence. Treat every figure and
   every claim in the restoration handout as a claim to check, and produce a
   reconciliation table: handout claim, your measured value, source
   (file:line or command), verdict (confirmed / corrected / unverifiable-here).
   Where this prompt disagrees with the repository, the repository wins and the
   disagreement is a finding.
2. **Correct the record and close the open items.** Known corrections and open
   items are listed below. Say plainly which are still true and which have
   moved.
3. **State the closure conditions clause by clause.** What must be true for this
   logical whole to be closed, and the evidence that proves each clause.

## Where everything lives

```text
Canonical repository:  /home/agile/Projects/kronika
Meta trace directory:  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/
Restoration handout:   25_handout_00.md   (its body self-names 25_restoration_00.md;
                                            storage naming is Meta policy)
Accepted plan:         17_report_00.md    the fifteen-step completion plan
Chronological ledger:  00_notes.md        every decision, defect and Orchestrator
                                          error, in order
Trace prompts/reports: 01_* through 24_*  in order
```

Read the chronological ledger (`00_notes.md`) before the reports. It is the only
place where the reasoning behind each decision is recorded together with the
mistakes, and several of its entries are the sole explanation for why a later
cut is shaped the way it is. The trace is subordinate evidence: it is the fastest
way to reconstruct what was decided and what went wrong, but it never outranks
the repository.

A stale clone exists at `/home/agile/Projects/framenest` and must not be used as
a work source. The old macOS path `/Users/agile/Projects/framenest` appears only
in historical artifacts.

## Verified current state, measured by the Orchestrator on 2026-10-07

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Local HEAD:                   3194f48f6b343a460ed5988d92999f91ef999a79
Public main:                  3194f48f6b343a460ed5988d92999f91ef999a79, divergence 0 0
Working tree:                 clean before and after today's suite runs
Remote origin:                https://github.com/cisarik/kronika
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Node:                         v26.8.2
Python declared test:         4625 passed, 8 skipped, 3 warnings, 0 failed
                              (reproduced today through the declared AP route, 670 s)
JavaScript:                   583 total, 578 passed, 0 failed, 5 skipped
                              (reproduced today, `node --test tests/*.test.js`)
Retention module:             15 passed (reproduced today)
Frozen documents:             86 keys (tests/contract/test_kronika_identity_retention.py)
Frozen Alembic files:         36 keys (revisions 0001-0035 plus versions/__init__.py)
The 19 commits C0..C5:        verified present in `git log` in the handout's order,
                              `ca649f6` through `3194f48`
```

The complete installed release is `3194f48`. **The artifact and rollback floor
is `3194f48`; `ed5bcb4` is superseded as the floor.** Never describe a C1
descendant as safe for C5 artifacts.

**NUC facts are carried, not measured here.** The Orchestrator session cannot
reach the NUC (the sanctioned gate probe returns `ssh-agent: ready`, but SSH
times out from the untrusted ambient session). Every host observation is a
Cooperator terminal action; fresh host preflight is a `C6` precondition. The
carried host state at handout time was:

```text
active web release:  3194f48f6b343a460ed5988d92999f91ef999a79
layout:              old          (correct; C6 has not run)
capture release:     94e605c17b881461fad3e22fd8c7fca32cb93976
database revision:   0035, equal to head
service:             active
backup readiness:    ready
web unit:            framenest.service, User=framenest
host layout:         /opt/framenest, /etc/framenest, /var/lib/framenest
```

Two host facts that were measured in the previous session and are easy to get
wrong: the installed web unit names a console script **directly inside
`.venv/bin`** in both `ExecStartPre` and `ExecStart`, with
`check-database-ready` and `serve` as **arguments** (no interpreter-wrapper
form); and **capture units are already `kronika-capture-*`** while web units are
still `framenest-*`, so capture identity is asymmetric on purpose and already
correct. Do not "uniformise" it.

## The accepted plan is the authority for what was decided

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/17_report_00.md`
is the accepted completion plan. Read it in full. It defines the standing
execution rules, the per-cut mutation, evidence and rollback, the Corrections
table, `D-1` through `D-8`, and the closure conditions.

`docs/adr/0085-kronika-sole-identity.md` is the accepted identity authority.
Read it in full, especially **"Named frozen residues"**.

Completed and accepted; do not re-plan, but do verify the commits exist:
`C0` ADR-0085, `C1` dual-read resolver, `C1b` exit 2, `C1c` parity,
`C1d` precedence documentation, `C1e` content-path ledger, `C2` companion dual
headers and storage migration, `C2a` web protocol dual accept, `C2b` visible
names, `C2c` companion prose and download stem, `C2d` product prose and operator
output, `C3-A` per-occurrence agreement guards, `C3-B` package/distribution/
executable move, its brace correction and its test-side repoint, `C4-A`
canonical release entry + complete marker readers + installed-unit guard,
`C4-B` host migration machinery and canonical host artifacts, `C5` durable
writers switched.

Remaining per the accepted plan, plus the ordering constraints that are
load-bearing:

```text
C-DATA   correct the existing catalog display label      MUST precede C6
C-LOCAL  migrate development and AI state                MUST precede C7-B
C6       NUC web identity migration                      highest web-availability risk
C7-A     emit canonical protocols before removing readers
C7-B     remove aliases, fallbacks and old entry points
C8-A     capture path migration, unchanged capture release
C8-B     capture software identity, separately reviewed delta
C9-A     exact retirement of old host objects, one-way
C9-B     remove transition machinery, finalize docs
CLOSE    read-only acceptance that closes the whole
```

**A recorded sequence deviation.** The accepted plan's table orders
`C4-B -> C-DATA -> C-LOCAL -> C5`. `C5` was executed before `C-DATA` and
`C-LOCAL`. The deviation was assessed as not harmful because the cuts are
independent, but it is real: `C-DATA` must still precede `C6`, and `C-LOCAL`
must still precede `C7-B`. Your plan must restore and respect those constraints.

## Named obligations that are not yet cuts

1. **Operator-script canonical counterparts.** Five Part B paths have no
   canonical counterpart yet: three under `scripts/operator/infosec/`
   (`framenest_log_triage.sh`, `framenest_public_surface_check.sh`,
   `framenest_socket_permissions_check.sh`) and two under
   `scripts/operator/network/` (`framenest_mullvad_egress.fish`,
   `framenest_mullvad_egress.sh`). The Cooperator has decided they get **their
   own bounded cut before C7-B**, because `C7-B` removes the old entry points
   and the counterparts must exist first. They are **not** a `C6` precondition.
   Verify this inventory yourself from the tree and the Part B ledger.
2. **Three dead builders** added by `C4-B` with no caller and no test:
   `cmd_remote_switch_layout_release`, `cmd_remote_unit_enabled_state`,
   `migration_unit_required` in `deploy/ubuntu/kronika_release.py`. Measured
   today at lines 2457, 2533 and 2753. They must be removed in the next cut
   that touches the engine. Confirm by derivation (callers and test
   references), not by this list.
3. **Runbook gap.** `docs/UBUNTU_NUC_DEPLOYMENT.md` documents a stale-lock
   recovery whose own precondition does not hold on the real host (the real
   residue held four files including `previous-release`, which the runbook does
   not list), and whose block still references schema `0032`/`0033`. Measured
   today: those literals remain at lines ~895, ~927-928 and ~961. It needs its
   own documentation cut.

**A deferred Cooperator request to place in the plan:** a **clean-install
runbook** for a from-scratch Ubuntu NUC with fully canonical host and tailnet
identity. He will perform that installation himself and wants
**documentation, not scripts**. He deferred it until the identity is removed
from the repository, so place it after the identity-removal cuts. Two host-side
residues belong in that document and must be described without their values:
his operator SSH identity filename still carries the retired spelling, and his
canonical transport variables currently arrive through a shell export in a user
dotfile rather than through the universal-variable mechanism the plan's
question 14 assumed.

## Known corrections and open items to address

Each of these is a claim to check, not a fact to transcribe. Where one is stale,
say so with your measurement.

- **The class-name residue figures in the restoration handout are approximate
  and now stale.** The handout says "roughly 1,423 occurrences across about 95
  classes". Measured today under `src/kronika`: **61** distinct `class FrameNest*`
  definitions and **1,483** `FrameNest*` tokens; `src` plus `tests` gives
  **1,954** tokens. The repository is right. The deliberate decision stands:
  `FrameNest*Error` classes, `FrameNestJsonFormatter`, `FrameNestRedactionFilter`,
  `FrameNestLogger` and `FrameNestConfigurationError` are **out of scope** for
  the confirmed goal. Decide and state whether their retirement is a bounded
  later cut inside this whole or formally excluded for the life of the
  repository, and record which. The Cooperator-confirmed membership test places
  Python class and module names out of scope, so exclusion does not violate the
  goal; the earlier Orchestrator note called this "named follow-up work".
- **The trace file on disk is `25_handout_00.md`** while the handout body
  self-names `25_restoration_00.md`. Storage naming is Meta policy; the file
  that exists is the evidence. Note it; do not act on it.
- **Host state is carried.** Re-baseline every host claim in your plan; do not
  inherit the handout's `status` block as current. In particular the web release
  served, the effective unit/drop-in set, enabled timers, account mapping,
  environment key names, configured path classes, optional integrations and
  capture continuity all need a fresh Cooperator preflight.
- **Capture identity must stay labelled.** Three distinct values exist and were
  repeatedly conflated before: target-source capture subtree at the release
  under consideration; target-source capture subtree at another release; and
  the installed capture release with its own subtree. The installed capture
  release `94e605c` already differs from current source in three capture files
  beyond branding (driver, runner and `cli.py`, +157/-28 across two commits).
  `C8-B` must review that complete delta and must never be approved as a
  path-only or identity-only move. Label target-source identity and
  installed-runtime identity separately in every receipt.
- **The removal cut (`C7-A`/`C7-B`) carries a derived list, not a given one.**
  From the ledger, at minimum, verify and plan: deletion of the SQLite resolver
  mirrors and the compatible fallback; the `lookup_field_value`/`lookup_env`
  collapse check before the fallback is deleted; any still-missing `_env_*`
  parity cases; the retired duplicate alarm and dual storage keys in the
  companion; deletion (not re-pinning) of the two deliberately brittle
  `v: <expr>` multiset assertions in the same commit that moves the protocol
  constants; the dual mutation header removal after `C7-A` emission; and the
  deferred DOM/class identifiers with their paired style edits and rendered
  acceptance. Re-derive this set from the tree; do not trust this parenthesis
  as complete.
- **The AP execution contract is live.** The Worker route is the declared one
  below and the baseline is the current HEAD. Do not treat any earlier SHA as a
  valid baseline for a mutated worktree.

## The discipline rules this whole paid for

State these in your plan as binding method for every remaining cut. They are
empirical, not stylistic.

```text
 1. Derive site lists by PARSING each artefact. Never from a prose enumeration,
    and never from an earlier prompt's list.
 2. Resolve every cited line to its literal text BEFORE classifying it.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Pin and verify each occurrence independently. Never per file, never per
    function.
 5. Reject any display pin that is a whole-file or whole-function regex where
    the literal occurs more than once.
 6. Never truncate an inventory. If output is truncated, disclose it and
    reprocess.
 7. Verify every mechanical probe against a known-impossible number. A
    formatting artifact must not become a finding.
 8. Regenerate every verification table at report time. Never transcribe one.
 9. Open and classify every grep hit. Distinguish production presence,
    historical compatibility and negative assertions.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

Two operational applications are mandatory: report the counting scope, and keep
source-artifact evidence separate from live-host evidence.

**Three recurring defect patterns to hunt actively, and to require of later
cuts:**

- **A test that passes while checking nothing.** This whole found it twice: four
  import-boundary guards iterating a directory that no longer existed, and three
  gate tests passing because the Cooperator's personal Fish configuration
  supplied the variables. Whenever a guard reads a path, a name or an
  environment value, ask what happens when that input is absent.
- **A pair that collapses.** `accepted_durable_identity` **raises** when its two
  spellings become equal (loud and good). A literal `frozenset({a, b})`
  **collapses silently** and makes historical artifacts unreadable. Sort every
  acceptance set into these two categories, and demonstrate the silent one
  wherever it exists.
- **A verification table transcribed rather than regenerated.** Three Workers
  reported `FROZEN_ALEMBIC_SHA256` as 38 keys; it has **36**. Measure it.

**The single most effective corrective, empirically:** issue **derivation rules
plus a sample to reconcile against**, and require the Worker to report **every
site that no test exercises**. That immediately found four latent sites and two
vacuous guards. Use it as the standard shape of every later cut's inventory
instruction.

## Machine-readable inventories to start from

Do not enumerate these from prose. Read them from the machine and report what
you read, with file and line:

```text
tests/contract/test_kronika_identity_retention.py
  FROZEN_DOCUMENT_SHA256               86 keys
  FROZEN_ALEMBIC_SHA256                36 keys (revisions 0001-0035 plus
                                       versions/__init__.py)
  EXPECTED_FRAMENEST_BASENAME_PATHS    20 paths whose basename carries the
                                       retired spelling
  EXPECTED_FRAMENEST_CONTENT_PATHS     content-carrying path membership set; a
                                       partial rename fails it
  PER_TREE_FRAMENEST_OCCURRENCE_COUNT  per-tree occurrence counts; a WEAK pin,
                                       it detects that something moved, never
                                       what it moved to
```

Standalone-word derivation for prose occurrences:

```text
rg -n -P '(?<![A-Za-z_])FrameNest(?![A-Za-z])' src
```

**The retention ledger is silent under a wrong-brand rename.** It is keyed to
the retired spelling, so a correct-looking replacement with the wrong brand
moves none of its counters. A zero-result text search is **not** the closure
test; frozen material, negative assertions, historical readers and non-operative
prose legitimately retain tokens.

## Risk surfaces your plan must address explicitly

- **Target-source versus installed-runtime identity.** Every capture and release
  claim must say which one it measures. A fingerprint computed from the release
  under consideration is not evidence about the installed runtime.
- **Paired constants that can collapse.** For every writer/content pair, name
  whether a collapse raises or fails silently, and require the silent category
  to be demonstrated before its writer is switched. Historical readers remain
  readable permanently.
- **Vacuous guards.** Any guard over a moved path, renamed symbol or absent
  environment input must be proven non-vacuous on the current tree.
- **Host facts must be observed, not inferred.** The plan must state, per cut,
  which facts are carried, which a Cooperator preflight must freshly establish,
  and which are machine-checkable in-repo.
- **Native plan mode is a client state, not hard enforcement on every client.**
  Your read-only boundary is the negative authority in this prompt, and the tree
  must be verified clean at the end.

## The confirmed goal, which bounds the whole

The Cooperator chose explicitly and this is not open:

```text
Zero user-visible and operational occurrences of the retired spelling, with the
ADR-0085 named frozen residues deliberately kept. No ADR amendment is pending
and none is authorised.
```

Membership test for every remaining cut:

```text
IN SCOPE     user-visible strings, operator-facing process output, CLI help
             text, validation messages that reach an API response, operational
             values, and durable writer identities
OUT OF SCOPE source docstrings, comments, Python class and module names, and the
             ADR-0085 named frozen residues
```

**Residues that survive closure deliberately** — your plan must enumerate them
at `CLOSE`, so closure is not confused with zero occurrences:

```text
/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry
/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13
FNCBE01, the encrypted protocol magic
the capture state directory name framenest-chatgpt-page
/mnt/framenest-catalog-offdevice
docs/FEDORA_SERVICE.md and docs/NUC_HOST_BASELINE.md
the 86 frozen document hashes and the 36 frozen Alembic revision hashes
historical ADR bodies, historical artifacts and readers, and the accepted
  Python class-name residue unless you decide otherwise
```

## Closure conditions you must state clause by clause

The final state must be, with the evidence that proves each clause:

```text
one canonical application package and distribution
exactly the canonical executable set
all 86 and 36 frozen hashes intact
canonical visible and operator output
canonical environment and request protocols
preserved catalog relationships
retained development and AI state
durable compatibility preserved
a canonical NUC web layout
a canonical capture operational identity with the frozen state path
retired objects safely removed
a scheduled backup working on the new layout
rendered behavior accepted by the Cooperator
no scope expansion
a final independent reconciliation distinguishing measured from carried evidence
```

## Authority

```text
Positive authority: read any tracked file in /home/agile/Projects/kronika; read
  every file in the Meta trace directory named above; run read-only Git
  inspection; run the declared JavaScript route and the declared AP test
  operations if you need to confirm a baseline; produce the plan.

Negative authority: ANY file mutation, including in the repository, in /tmp and
  in the Meta trace; any commit, branch, tag, merge, rebase, stash or history
  rewrite; any push; any NUC contact, including SSH and the NUC worker gate; any
  provider or capture-browser contact; any execution of a kronika-capture
  command; any database write of any kind; any dependency install, update or
  lockfile change; any reading of private/**, personal Fish configuration,
  browser profiles, cookies, tokens, credential stores, .secrets or
  ~/.config/opencode; any writing of the plan to a file.

Commands: Python evidence goes only through
  ./.ap/ap project check --root /home/agile/Projects/kronika --baseline 3194f48f6b343a460ed5988d92999f91ef999a79
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 3194f48f6b343a460ed5988d92999f91ef999a79 --operation <id> [-- <argv>]
  (operations: runtime-info, test, test-focus). Never invoke .venv/bin/python,
  python, python3 or poetry run for evidence, including as a text editor.
  JavaScript evidence goes only through `node --test tests/*.test.js` and
  focused `node --test <path>`.
  Read-only Git inspection is allowed (`git status`, `git rev-parse`, `git log`,
  `git show`, `git diff`, `git ls-files`, `git grep`, `git ls-remote`,
  `git submodule status`, `git merge-base`); no other Git command. Any other
  command must be stated in the report with its purpose and a confirmation that
  it mutated nothing.

Dependency authority: none.
Git authority: none. Read-only inspection only. No commit of any kind.
Network authority: none beyond read-only public Git ref verification.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and published ADR-0085 are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.
Side-effect authority: none. This cut is read-only by design; its evidence tier
  is planning-grade.
Browser authority: none. Do not open Brave, do not load the extension.
```

## Verification

1. Confirm branch `main`, HEAD `3194f48f6b343a460ed5988d92999f91ef999a79`,
   clean tree, submodule at `73e20ef80b88700d5fcbc397cd8edd4fc425869f`,
   `ap doctor` PASS. Stop if any fails.
2. Read ADR-0085 and the accepted plan `17_report_00.md` in full before planning
   anything.
3. Read the restoration handout `25_handout_00.md` in full, and the
   chronological ledger `00_notes.md` at least for every entry from 2026-10-02
   onward.
4. Re-derive the current state and every figure you use. Produce the
   reconciliation table: for each restoration-handout claim, your measured
   value, source, verdict. Claims to cover at minimum: HEAD, branch, public-main
   equality, AP pin, Node, `ap doctor`; the Python, JavaScript and retention
   baselines; the 86 and 36 frozen-key counts; the class-name residue figure;
   the nineteen completed commits; the NUC live-state block (carried,
   unverifiable from the repository); and the frozen-residue list.
5. Read the machine-readable inventories from
   `tests/contract/test_kronika_identity_retention.py` and report your readings.
6. Produce the completion plan: for each work item, mutation, authority,
   evidence, machine-checkable proof, rollback, preconditions, and its ordering
   constraint.
7. Address the three named obligations, the deferred clean-install runbook, and
   the class-name decision explicitly.
8. State the closure conditions clause by clause, and the residues that survive
   closure.
9. Confirm the working tree is still clean and HEAD unchanged before you finish.

```text
Evidence tier: planning-grade. Read-only analysis producing an executable plan.
```

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if ADR-0085 and the accepted plan contradict each other in a way that
  changes the goal; if closing the whole would require an ADR amendment, which
  is unauthorised; if any step you plan would need real provider, browser,
  capture or host authority you were not granted; if a claim in this prompt is
  contradicted by the repository and the contradiction is material to the plan;
  if context pressure reaches the point where a bounded rotation is cheaper than
  a degraded plan.

Completion: one plan covering the remaining sequence to CLOSE plus the named
  obligations, every known correction addressed by name, the reconciliation
  table complete, machine-readable inventories re-derived from the repository,
  closure conditions and surviving residues stated, tree clean and HEAD
  unchanged.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `25_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No implementation, no commit, no push, no publication,
  no NUC contact and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed. You are planning its closure, not performing it.
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-evidence`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `25` and exchange `01` unchanged.
Native planning mode requires this artifact to open with a level-1 title; if
your client's surface forces a preamble above the report header, disclose it on
the first line of the report body.

Then, in this order:

1. **Reconciliation table** for every restoration-handout claim you checked.
2. **The plan**, work item by work item through `CLOSE`, each with mutation,
   authority, evidence, proof, rollback, preconditions and ordering constraint.
3. **The three named obligations** and the deferred clean-install runbook, each
   with a placement decision.
4. **The class-name decision** and any other scope/exclusion decisions, stated
   explicitly.
5. **Closure conditions**, clause by clause, with the evidence for each and the
   residues that survive.
6. **The discipline rules** and the three recurring defect patterns, confirmed
   or amended, with application notes for the remaining cuts.
7. **Inventory figures** you read from the repository, each labelled with its
   file and line.
8. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification.

Finish every terminal report with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

The Orchestrator expects real findings against the accepted plan, the
restoration handout and its own prior statements. A plan that reports nothing
wrong with this prompt is less credible than one that finds something, not more.

## Mandatory reading

- `.ap/AP.md` — the WORKER spine rows plus RF-03, RF-06, RF-09, RF-12, RF-16,
  RF-17, RF-18, RF-19; `.ap/AP_WORKER.md`; `docs/WORKER_EXECUTION_CONTRACT.md`;
  `AGENTS.md`.
- `docs/adr/0085-kronika-sole-identity.md` in full, especially "Named frozen
  residues".
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/17_report_00.md`
  in full — your specification for the remaining cuts.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_handout_00.md`
  in full — the claims you must reconcile.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/00_notes.md` —
  the chronological ledger; read every entry from 2026-10-02 onward.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/23_report_00.md`
  and `24_report_00.md` — the C4-B and C5 evidence base.
- `tests/contract/test_kronika_identity_retention.py` in full — the
  machine-readable inventory and the enforcement mechanism.
- `deploy/ubuntu/kronika_release.py` and the canonical entry
  `deploy/ubuntu/kronika-release` — layout selector, marker readers, guard, dead
  builders, migration machinery.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` in full — including the stale-lock recovery
  section and its schema references.
- `docs/BACKUP_AND_RECOVERY.md` in full — the durable backup/recovery contract.
- `deploy/systemd/` in full — canonical units, the environment template, capture
  naming asymmetry.
- `scripts/operator/` — the five counterpart paths and the canonical gate.
- `pyproject.toml` and `ap.project.conf` — the current distribution, executable
  set and AP contract.
- `ROADMAP.md`, `PRODUCT.md`, `SPEC.md`, `SERVER.md`, `README.md` — the
  living-documentation surface `C9-B` must finalize.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real browser profile.

## Communication

Report text and the plan are professional English. Do not use Czech or Slovak.

## Orchestrator note

Three things this prompt deliberately does not decide for you, because they are
the Orchestrator's or the Cooperator's to own and yours to inform: the exact cut
boundaries where your derivation shows a cut must split or merge; the `C-DATA`
mechanism and window, which remain a Cooperator decision on your prepared
proposal; and whether the whole closes at `C9-B` plus `CLOSE` or needs a further
bounded cut. Report your recommendation on each with your reasoning, and mark
clearly anything you believe requires the Cooperator's decision rather than
yours.
