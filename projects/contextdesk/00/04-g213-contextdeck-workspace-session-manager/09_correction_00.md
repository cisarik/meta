Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 09
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: CONTEXTDECK-M4-SLICE-B-CORRECTION
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to a genuinely fresh Worker session
Reasoning recommendation: High
Reasoning basis: corrects a fail-closed runtime defect in the desktop mutation
executor plus a runtime checkpoint-path placement and a stale documentation
claim; bounded but safety-relevant
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E3
Evidence-tier basis: the correction changes runtime behavior in host-mutating
code and the checkpoint file location, so it requires a separate full-fresh
re-acceptance rather than a scoped one
Internal delegation: prohibited

# ContextDeck M4 Slice B — correct current-step gating and checkpoint path

You are a genuinely fresh WORKER. You did not implement the candidate and did
not perform its independent acceptance. Native Plan Mode must be OFF. Do not
use subagents.

Implement one bounded correction for the confirmed blockers in public
`08_report_00.md`. The candidate `5087277…` returned `PARTIAL`: A1 and A3–A7
PASS, but A2 failed on a non-fail-closed `current` step and A8 failed on two
documentation mismatches. Fix exactly those three findings, validate, publish
exactly one product correction commit, persist one terminal report, and stop.
You do not accept your own correction. Do not change any other accepted
behavior, capability, mutation, or opt-in split.

## Authoritative correction transition

Implementation authority: explicit-bounded-correction
Prior implementation candidate:
`50872779c619a97be061d7f0df414ccae6bde7e6`
Prior implementation parent:
`aca6c68542bbc9f1b8ee891415a04b0a95e8372e`
Independent acceptance result: `PARTIAL`, not acceptance-PASS
Independent acceptance artifact:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/08_report_00.md`
Independent acceptance artifact SHA-256:
`010fc3e4ba1c864453b2ee0125de2c4946640e08426ba941fb0794d09a098521`
Exact baseline: `50872779c619a97be061d7f0df414ccae6bde7e6`
Changed-path allowlist: the ceiling in "Exact changed-path allowlist"
Implementation boundaries: fix exactly the three confirmed findings below; no
new capability, mutation, opt-in, dependency, or scope
Independence required: no for this correction; yes for the following separate
full-fresh re-acceptance (runtime behavior changes)

## The three confirmed findings

### Finding 1 (A2, runtime) — `current` step is not fail-closed

In `src/workspace/DesktopMutator.cpp` the optional `current` step (around
lines 315–324) sets `residualClass = "current-switch-skipped"` and continues
when the `Properties.Set` on `current` fails or times out. Execution then
proceeds to the opted-in `removeDesktop` removals and the transaction returns
`ok = true`, after which the post-apply launch phase still runs. This violates
the accepted contract (`07_implementation_00.md` §1: every step gates the next;
any error stops the sequence and triggers the revert path) and the candidate's
own changed documentation.

Correction: make the `current` step fail-closed. On any failure or timeout of
the `current` `Properties.Set`, stop the sequence and run the revert path (use
the existing `failApply`/revert mechanism, not a soft residual). A precondition
contradiction such as a missing target desktop must also stop before the opted-in
removals and the launch phase rather than continue. Preserve the bounded
`current-restore-skipped` revert residual (that is the revert-side skip, which
stays). Add one focused regression using the existing fake failure-injection
(`setFailMethod`) proving that a failed `current` set aborts and reverts and
does not reach removal or launch.

### Finding 2 (A8, runtime path) — checkpoint is one directory too high

`AppController` sets the checkpoint to
`m_store.configRoot() + "/workspace-checkpoint.json"`; `ProfileStore::configRoot()`
is `$XDG_CONFIG_HOME` or `$HOME/.config`, so the file is written as
`<config root>/workspace-checkpoint.json`, one directory above the documented
and planned product directory. `docs/specification.md` and `docs/operations.md`
document `$XDG_CONFIG_HOME/contextdeck/workspace-checkpoint.json` (fallback
`$HOME/.config/contextdeck/workspace-checkpoint.json`), which is the accepted
plan/preflight intent.

Correction decision (ORCHESTRATOR): place the checkpoint in the ContextDeck
product configuration directory alongside the profile document, i.e.
`<config root>/contextdeck/workspace-checkpoint.json`, matching the documented
path and the accepted intent. Keep the atomic `QSaveFile` write, no
direct-write fallback, and user-only permissions unchanged. Add one focused
regression proving the default production checkpoint path is the product
directory (not the bare config root), using the existing config-root injection
seam. The documented path stays as-is once the code matches it.

### Finding 3 (A8, documentation) — stale Apply claim

`docs/specification.md` (around line 555) still says for the `Plochy` page:
"Apply hidden/disabled until a later authorized slice". Slice B implements and
enables Apply with preconditions plus checkpoint revert. Update that row to
describe the implemented Apply/revert controls and their explicit preconditions
truthfully; do not overclaim live behavior.

## Exact repositories and immutable gates

Canonical product repository: `https://github.com/cisarik/contextdesk`
Required branch: `main`
Required product HEAD and public `main` before mutation:
`50872779c619a97be061d7f0df414ccae6bde7e6`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

Canonical META repository: `https://github.com/cisarik/meta.git`
Required public META baseline: the current public `main` at delivery time; a
later verified descendant is acceptable after ancestry and changed-path review
proves no M4 artifact changed. The `07` and `08` pairs may still be pending
COOPERATOR first-add; verify them by path and SHA-256 if unarchived.
Required M4 trace:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/`

Repository checkout topology: standalone product checkout on `main`
Working-copy topology: canonical product checkout

Before any product or META file mutation:

1. Verify the complete prompt, genuinely fresh session, Native Plan Mode OFF,
   coordinates, correction authority, and no subagents.
2. Verify canonical remote, active `main`, exact HEAD and parent, clean state,
   no Git locks, matching AP gitlink/checkout, and `./.ap/ap doctor` PASS.
3. Prove public product `main` equals the exact baseline with direct
   `git ls-remote`. Do not pull, merge, rebase, switch, reset, clean, stash, or
   retarget.
4. Verify META public `main` and the acceptance artifact hash above; accept a
   later descendant only after ancestry and changed-path review.
5. Verify `dbus-run-session`, CMake, Ninja, and the KF6 packages without
   installing.
6. Read `src/workspace/DesktopMutator.{h,cpp}`, `src/app/AppController.{h,cpp}`,
   `src/core/Persistence.{h,cpp}`, the two documents, and the relevant tests
   before editing. Every needed path must be inside the allowlist.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-12, RF-18, RF-19, acceptance/correction
  and escalation, implementation authority, Git safety, stopping;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Acceptance and Correction
  Record, exchange/trace, delivery record;
- `AGENTS.md`, `README.md`, `ROADMAP.md`;
- `docs/specification.md`, `docs/architecture.md`, `docs/operations.md`,
  `docs/testing-m4.md`;
- `07_implementation_00.md`, `07_report_00.md`, and `08_report_00.md`;
- the changed source and test files listed in the allowlist.

## Product invariants

- G213 only; five zones, never per-key; broker static/inactive.
- Typed launch only; no shell; no `kwinrulesrc`; no autostart.
- Captions, titles, desktop names, and UUIDs are sensitive: never logged.
- No host, desktop, launch, bridge-reload, OpenRGB, or device operation during
  this exchange.

## Command, dependency, host, and data authority

Allowed commands: read-only source/Git inspection; existing CMake/Ninja build;
the exact test routes below; `git diff`, `git status`, exact-path staging, one
commit, one normal push, direct public-ref readback
Forbidden commands: destructive Git recovery; force push; history rewrite;
branch/tag/remote/config changes; package manager; sudo; service/device tools;
live D-Bus calls to KWin; application launch; OpenRGB CLI; broker operations
Dependency authority: none; the two KF6 components already added remain the only
new dependency
Host authority: none
Device authority: none
Secret authority: none
Network authority: canonical product/META Git public verification and the one
authorized normal product push only

No raw input, key names, serials, host addresses, desktop names/IDs, captions,
or private paths may enter logs, documents, prompts, reports, or META.

## Validation

```sh
cmake -S . -B build -G Ninja
cmake --build build

ctest --test-dir build --output-on-failure \
  -R '^(test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_plan|test_openrgb_protocol|test_workspace_mutator|test_placement_resolver|test_application_launcher)$'

ctest --test-dir build --output-on-failure

git diff --check
git diff --name-only
git status --short
```

The full registered suite is required. Do not weaken, skip, or loop tests.

## Exact changed-path allowlist

Modify only the necessary subset of this ceiling:

```text
src/app/AppController.h
src/app/AppController.cpp
src/workspace/DesktopMutator.h
src/workspace/DesktopMutator.cpp
src/workspace/WorkspaceCheckpoint.h
src/workspace/WorkspaceCheckpoint.cpp
docs/specification.md
docs/operations.md
tests/unit/test_workspace_mutator.cpp
tests/unit/test_workspace_lighting.cpp
```

Do not change `.ap/`, the KWin bridge, `src/context/`, `SessionApplication.*`,
`src/core/Types.h`, `src/core/Persistence.cpp` (unless a path helper genuinely
requires it, in which case stop `PARTIAL` and name it), other tests, packaging,
dependencies, or host configuration. If one additional path is genuinely
required, stop `PARTIAL` without committing and name it.

## Git publication authority

After the focused and full suites pass and exact-path review proves the diff is
inside the ceiling:

1. Inspect `git diff --check`, `git diff --name-only`, `git status --short`, and
   the complete diff.
2. Stage only exact changed allowlisted paths. Never `git add .`/`-A`.
3. Create exactly one normal commit with subject:
   `Fix M4 Slice B current-step gating and checkpoint path`
4. Push only `main` to canonical origin with a normal non-force fast-forward.
5. Verify local HEAD, `origin/main`, and direct public `ls-remote` all equal the
   new commit; parent equals `5087277…`; changed paths are the authorized subset.

If commit/push auth is unavailable, report `PARTIAL` with exact state.

## Exact META trace persistence

External trace disposition: configured
Trace discovery: META README and exact M4 trace
Trace project key: contextdesk
Trace logical-whole projection identity: 04-g213-contextdeck-workspace-session-manager
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 09_correction_00.md
Destination path: projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/
Report filename: 09_report_00.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR for META; WORKER for the one product commit
Archival: wait-for-report

The ORCHESTRATOR persists this exact prompt bytes to
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/09_correction_00.md`
before delivery. The WORKER may write only the report file at
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/09_report_00.md`.
Verify the persisted prompt is byte-identical and read it back completely. Do not
alter earlier M4 pairs or `00_notes.md`. After publication, write and completely
read back the terminal report. Do not mutate META Git; the COOPERATOR owns
first-add archival.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo the opening persistent-role and three coordinate fields exactly once with
values unchanged, and include:

- status `PASS`, `PARTIAL`, or `BLOCKED`;
- phase-qualified result: `implementation-PASS` only when the focused/full
  suites pass, one commit/push/public-ref verification passes, and the diff is
  inside the ceiling;
- exactly one `Report justification: new-mutation`;
- start/end commit, baseline, parent, AP pin, public META baseline, and the
  acceptance artifact identity;
- exact changed paths with purpose and proof that all other paths, `.ap`, the
  bridge, context, session app, dependencies, and host state remained unchanged;
- for each finding: the exact fix, the new or updated regression, and the
  observed result;
- focused and full CTest results with counts from actual output;
- private-bus evidence and statement that no real KWin/OpenRGB/device/broker/
  host/desktop/launch operation ran;
- exact commit, push, public-ref equality, parent, and changed-path evidence;
- META prompt/report persistence and readback, META Git publication remaining
  COOPERATOR-owned;
- deviations, resolved issues/near-misses, pre-existing failure classification,
  residual risks, and missing evidence;
- exactly one smallest next step: ORCHESTRATOR reconciliation followed, only if
  accepted, by a separate **full-fresh** independent code-acceptance Worker;
- compact `Orchestration critique` with `MEASURED:` and `LEAD:`;
- exactly one `Logical-whole closure: not-closed` line;
- the exact authority-expiry sentence below.

Explicit non-claims: no acceptance-PASS, deployment-PASS, production readiness,
physical acceptance, M2/G4 closure, M3 closure, autostart, hibernate/hybrid
sleep, general input-remapper coexistence, live desktop/launch/placement
behavior, remapping, M5, per-key RGB, or measured control-to-zone placement.

Authority for this Worker expires at this terminal report.

## Stop conditions

Stop before mutation on a non-fresh/contaminated session, Native Plan Mode
mismatch, coordinate/authority contradiction, product/AP/META identity or
public-ref failure, dirty/unexplained worktree, unsafe trace path/collision,
missing required tool/package, or need for a non-allowlisted path, dependency,
host access, device access, secret, or subagent.

After mutation, stop `PARTIAL` without committing when a fix cannot be made
faithfully inside the ceiling or a required test fails and cannot be corrected
in scope. Preserve the first causal failure; do not weaken, skip, or endlessly
rerun gates.

If validation passes but commit/push/public verification fails, preserve the
exact safe state and report `PARTIAL`. Use `PASS` only for one fully validated
and publicly verified correction commit.

Stop immediately after the terminal report. Do not begin the full-fresh
re-acceptance, a live IRL run, deployment, or host enablement under this
authority.
