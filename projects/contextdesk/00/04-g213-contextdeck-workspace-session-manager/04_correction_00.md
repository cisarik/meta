Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 04
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: CONTEXTDECK-M4-SLICE-A-DIAGNOSTICS-PRIVACY-CORRECTION
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to a genuinely fresh Worker session
Reasoning recommendation: Maximum (COOPERATOR-selected; ORCHESTRATOR recommended Medium)
Reasoning basis: one bounded test-only correction adding a single missing
diagnostics-privacy regression; the departure to the client maximum/enhanced
mode is an accepted COOPERATOR decision and does not change any authority
boundary
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E1
Evidence-tier basis: bounded reversible test-only addition with no runtime,
semantic, schema, or authority change; requires one public correction commit and
a following scoped fresh re-acceptance
Internal delegation: prohibited

# ContextDeck M4 Slice A — add the missing diagnostics-privacy regression

You are a genuinely fresh WORKER. You did not implement the candidate and did
not perform its independent acceptance. Native Plan Mode must be OFF. Do not
use subagents.

Implement one bounded correction for the single confirmed acceptance blocker in
public `03_report_00.md`: add the missing durable causal regression that proves
`AppController::diagnostics()` does not expose title-fallback patterns, captions,
desktop names, or desktop UUIDs. Validate, publish exactly one product
correction commit, persist one terminal report, and stop. You do not accept your
own correction.

This correction must change **one test file only**. If the new test reveals that
the production property is actually violated, stop `PARTIAL` and report it; do
not edit production code, because that is outside this allowlist.

## Authoritative correction transition

Implementation authority: explicit-bounded-correction
Prior implementation candidate:
`c7c8eb90d31947bc32c498691ec926885f43cb64`
Prior implementation parent:
`502ae75571358ec95d33c836084b5e2253850731`
Independent acceptance result: `PARTIAL`, not acceptance-PASS
Independent acceptance artifact:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/03_report_00.md`
Independent acceptance pair commit:
`06439c9`
Independent acceptance artifact SHA-256:
`8dce3dc3f98848c230c75b9e9f004430be78253b1c60aea60de01e043ba0c3d3`
Exact baseline: `c7c8eb90d31947bc32c498691ec926885f43cb64`
Changed-path allowlist: `tests/unit/test_workspace_lighting.cpp` (only)
Implementation boundaries: add one focused diagnostics-privacy regression test
to the existing registered `test_workspace_lighting` target; no production
source, schema, resolver, receiver, controller, UI, documentation, or build
change
Independence required: no for this correction; yes for the following separate
scoped fresh re-acceptance

## The single confirmed finding

The accepted plan and the implementation prompt (`02_implementation_00.md` §7,
"Required causal evidence includes") require the persistent regression
`title-fallback privacy: diagnostics maps omit pattern/caption keys`. The
candidate `c7c8eb9` contains no such test. `tests/unit/test_workspace_lighting.cpp`
calls `controller.diagnostics()` but only for `lightingUpdates` and
`identityUpdates`; no test asserts that the new title-fallback pattern, a
caption, a desktop name, or a desktop UUID is absent from the diagnostics map.
The implementation report's `Missing evidence: none required by this envelope`
statement is therefore inaccurate. The runtime property is believed correct by
static inspection; the acceptance defect is the absent durable regression.

The correction must add, in `tests/unit/test_workspace_lighting.cpp`, a focused
test that:

- constructs an `AppController` with a temporary configuration root, following
  the existing pattern in that file;
- establishes a document state that includes a workspace named session with at
  least one user-authored desktop name and at least one application profile
  whose title fallback is enabled with a user-authored pattern, using unique
  synthetic sentinel values (never real captions, titles, or desktop names);
- reads `AppController::diagnostics()` and asserts that neither its keys nor its
  values contain those sentinels, and that no diagnostics key exposes a
  title pattern, caption, desktop name, or desktop UUID;
- is deterministic, uses only existing dependencies, and does not start the
  session application, OpenRGB, the broker, a real KWin session, or any device.

Design the insertion so it fits the existing test class and registered target.
Do not add a new test file, a new CMake target, or any new dependency.

## Exact repositories and immutable gates

Canonical product repository: `https://github.com/cisarik/contextdesk`
Required branch: `main`
Required product HEAD and public `main` before mutation:
`c7c8eb90d31947bc32c498691ec926885f43cb64`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

Canonical META repository: `https://github.com/cisarik/meta.git`
Required public META baseline:
`06439c943d196c336e3997ecf079a31e3cb8b639`
Required M4 trace:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/`

Repository checkout topology: standalone product checkout on `main`
Working-copy topology: canonical product checkout

Before any product or META file mutation:

1. Verify the complete prompt, genuinely fresh session, Native Plan Mode OFF,
   session/exchange coordinates, correction authority, and no subagents.
2. Verify canonical remote, active `main`, exact HEAD and parent, clean
   tracked/untracked state, no Git locks, matching AP gitlink/checkout, and
   `./.ap/ap doctor` PASS (variant `stable`).
3. Use direct `git ls-remote` to prove public product `main` equals the exact
   baseline. Do not pull, merge, rebase, switch, reset, clean, stash, or
   silently retarget.
4. Verify META public `main` equals the exact baseline or a later verified
   descendant, the `03_report_00.md` hash, and the acceptance pair commit.
5. Verify the M4 trace directory and parents are real directories, not symlinks;
   the correction prompt/report destinations must be absent or byte-identical.
6. Verify `dbus-run-session` and existing build tools without installing.
7. Read the current test file and `AppController.h` before editing. Confirm the
   only needed path is inside the allowlist; an extra path is a stopping
   condition.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-12, RF-18, RF-19, Acceptance/Correction
  and Escalation, phase-qualified results, stopping;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Acceptance and Correction
  Record, exchange/trace, delivery record;
- `AGENTS.md`, `README.md`, `ROADMAP.md`;
- `docs/specification.md` and `docs/architecture.md` for the schema-4
  assignment/title-fallback and diagnostics privacy rules;
- `02_implementation_00.md` §7, `02_report_00.md`, and `03_report_00.md`;
- `tests/unit/test_workspace_lighting.cpp` and `src/app/AppController.{h,cpp}`.

## Product invariants

- No keylogging, raw event logging, window-caption logging, desktop ID/name
  logging, telemetry, secrets, or private paths.
- Captions and titles are sensitive: never logged, never persisted, never in
  diagnostics.
- No host, desktop, launch, OpenRGB, broker, or device operation.
- No external source copying while licensing remains unresolved.

## Command, dependency, host, and data authority

Allowed commands: read-only source/Git inspection; existing CMake/Ninja build;
the exact focused/full CTest routes below; `git diff`, `git status`, exact-path
staging, one commit, one normal push, and direct public-ref readback
Forbidden commands: destructive Git recovery; force push; history rewrite;
branch/tag/remote/config changes; package manager; sudo; service/device tools;
live D-Bus calls to KWin; application launch; OpenRGB CLI; broker operations
Dependency authority: none
Host authority: none
Device authority: none
Secret authority: none
Network authority: canonical product/META Git public verification and the one
authorized normal product push only

No synthetic fixture may contain a real caption, real window title, real
desktop name, or any private data.

## Git publication authority

After the focused and full suites pass and exact-path review proves the diff is
the single allowlisted test file:

1. Inspect `git diff --check`, `git diff --name-only`, `git status --short`, and
   the complete diff.
2. Stage only `tests/unit/test_workspace_lighting.cpp`. Never use `git add .`
   or `git add -A`.
3. Create exactly one normal commit with subject:
   `Add M4 Slice A diagnostics privacy regression`
4. Push only `main` to the canonical product origin using a normal non-force
   fast-forward push.
5. Verify local HEAD, `origin/main`, and direct public `ls-remote` all equal the
   new full commit; parent equals `c7c8eb90d31947bc32c498691ec926885f43cb64`;
   changed paths are exactly the one allowlisted file.

If commit or push authentication is unavailable, report `PARTIAL` with the exact
local/publication state. Do not expose or repurpose credentials.

## Validation

```sh
cmake -S . -B build -G Ninja
cmake --build build

ctest --test-dir build --output-on-failure \
  -R '^(test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_plan|test_openrgb_protocol)$'

ctest --test-dir build --output-on-failure

git diff --check
git diff --name-only
git status --short
```

The full registered suite is required because a shared test target is edited.
Record real counts. Do not weaken, skip, or loop tests to manufacture green
output. If the new test fails because `diagnostics()` actually exposes a
sensitive value, stop `PARTIAL` and report the exact leak class; do not edit
production code.

## Exact META trace persistence

External trace disposition: configured
Trace discovery: META README and the exact M4 trace destination
Trace project key: contextdesk
Trace logical-whole projection identity: 04-g213-contextdeck-workspace-session-manager
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 04_correction_00.md
Destination path: projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/
Report filename: 04_report_00.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR for META; WORKER for the one product commit
Archival: wait-for-report

The ORCHESTRATOR persists this exact prompt bytes to
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/04_correction_00.md`
before delivery. The WORKER may write only the report file at
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/04_report_00.md`.

Verify the already-persisted prompt is byte-identical to the received prompt and
read it back completely. Stop on a non-identical collision. Do not alter earlier
M4 pairs or `00_notes.md`. After publication, write and completely read back the
terminal report. Do not stage, commit, push, pull, merge, rebase, switch, or
modify META Git history or refs. The COOPERATOR owns first-add archival of this
exact pair after the report exists.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo the opening persistent-role and three coordinate fields exactly once with
values unchanged, and include:

- status: `PASS`, `PARTIAL`, or `BLOCKED`;
- phase-qualified result: `implementation-PASS` only when the focused/full
  suites pass, one commit/push/public-ref verification passes, and the diff is
  exactly the single allowlisted test file; otherwise the truthful result;
- exactly one `Report justification: new-mutation` when product mutation
  occurred;
- start commit, end commit, required parent, AP pin, public META baseline, and
  the acceptance artifact identity;
- exact changed path with purpose and proof that all other paths, `.ap`, broker,
  RGB transport, KWin bridge, packaging, dependencies, and host state remained
  unchanged;
- the exact new test name and what it asserts, with the sentinel strategy
  described generically (no real captions/names);
- focused and full CTest results with counts from actual output;
- private-bus evidence and statement that no real KWin/OpenRGB/device/broker/
  host/desktop/launch operation ran;
- exact commit, push, public-ref equality, parent, and changed-path evidence;
- exact META prompt/report persistence and complete-readback evidence, while
  stating META Git publication remains COOPERATOR-owned;
- deviations, resolved execution issues/near-misses, pre-existing failure
  classification, residual risks, missing evidence, and any plan fidelity
  concern, including whether the new test passes or reveals a leak;
- exactly one smallest next step: ORCHESTRATOR reconciliation followed, only if
  accepted, by a separate scoped fresh re-acceptance Worker;
- compact `Orchestration critique` with `MEASURED:` and `LEAD:`;
- exactly one `Logical-whole closure: not-closed` line;
- the exact authority-expiry sentence below.

Explicit report non-claims: no acceptance-PASS, deployment-PASS, production
readiness, physical acceptance, M2/G4 closure, independent G3 re-audit,
autostart, hibernate/hybrid sleep, general input-remapper coexistence, M3
closure, M3 physical five-zone observation, desktop/launch/placement behavior,
remapping, deck behavior, M5 integration, per-key RGB, or measured
control-to-zone placement; no claim that tests prove live desktop or physical
device behavior; no claim that Session 27 was an independent Worker result.

Authority for this Worker expires at this terminal report.

## Stop conditions

Stop before mutation on a non-fresh/contaminated session, Native Plan Mode
mismatch, coordinate/authority contradiction, product/AP/META identity or
public-ref failure, dirty/unexplained worktree, unsafe trace path/collision,
missing required tool/private-bus runner, or need for a non-allowlisted path,
dependency, host access, device access, secret, or subagent.

After mutation, stop `PARTIAL` without committing when the required test cannot
be implemented faithfully inside the single-path allowlist, or when the new test
fails because the runtime diagnostics map leaks a sensitive value. Preserve the
first causal failure; do not weaken, skip, or endlessly rerun gates, and do not
edit production code.

If validation passes but commit/push/public verification fails, preserve the
exact safe state and report `PARTIAL`. Use `PASS` only for one fully validated
and publicly verified correction commit.

Stop immediately after the terminal report. Do not begin re-acceptance, Slice B,
deployment, or host enablement under this authority.
