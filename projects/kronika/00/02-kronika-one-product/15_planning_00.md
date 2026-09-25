# Kronika one product — S3 host recovery implementation plan

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 15
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: KRONIKA-ONE-PRODUCT-S3-RECOVERY-PLAN
Delivery route: manual Cooperator delivery
Reasoning recommendation: Extra High — Cooperator-selected posture for a cross-cutting diagnosis of the capture browser launch path and the host bring-up recovery, with a decision-complete plan; no Max.
Recommended context capacity: approximately 250k tokens
Independence required: no

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded diagnosis and recovery planning for completing S3 on the household NUC — the missing Chromium launch and the persisted `needs_admin` journal state — plus exact source corrections, their acceptance and the ordered host sequence
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1

Planning cycle: initial
Prior planning report: 01_report_00.md (accepted whole plan) with S3 acceptance reports 11_report_00.md and 13_report_00.md
Targeted revision basis: none
Changed decision boundary: the S3 host bring-up recovery and the capture browser launch path
Preserved unaffected decisions: all accepted product decisions; the accepted S0–S3 sources and their acceptances; the S4–S10 slice order
Automatic targeted revisions used: 0

This is a planning exchange only. It grants no implementation, host, Git,
browser, credential, deployment, or publication authority. The plan it produces
is advisory until the Cooperator accepts it; implementation then requires a new
complete Orchestrator prompt with `Native planning mode: not-used`.

## Why this planning exchange exists

The S3 repository and publication slices are accepted (`d63d0b7…` is public
`main`), but the host bring-up has not completed after several bounded
attempts. Each attempt produced new, distinct evidence, yet the browser still
does not run and the journal still holds a blocking state. Sequential patching
has reached diminishing returns; a repository-grounded plan is needed before
any further host touch.

## Classified host evidence (do not re-derive; use as input)

- `10_report_00.md`: first setup. Account, paths, token, release deploy and
  unit install succeeded. Bridge/runner exited 2 (`--state-dir` after the
  subcommand); Xvfb exited 1 (could not create `/tmp/.tX99-lock` under
  `ProtectSystem=strict`); activation exit 16 (`readiness=failed`).
- `10_report_01.md` + commit `94e605c`: argument order fixed; `-nolock`
  chosen; host cleaned.
- `10_report_02.md`: retry. Deploy and units at `94e605c` succeeded. Xvfb
  logged `Warning: the -nolock option can only be used by root`, ignored the
  option for the unprivileged user, needed the lock, exited 1; readiness
  `browser_unavailable`.
- `10_report_03.md` + commit `d63d0b7`: `-nolock` removed;
  `ReadWritePaths=/tmp /tmp/.X11-unix /run/kronika-capture`; test and docs
  updated; host cleaned.
- `10_report_04.md`: retry 2. Deploy and units at `d63d0b7` succeeded; Xvfb
  stayed active through a stability pause; bridge active. `activate-capture`
  exit 22 (`capture has live or paused work`) before the pointer switch and
  runner restart: the journal held a `needs_admin` service state with reason
  `E_AMBIGUOUS_SEND` (zero jobs, zero Chromium). Web pointer `d63d0b7`;
  capture pointer still `94e605c`; runner inactive.
- `10_report_05.md`: runner started once (`active`, `client_connected: true`,
  `Result=success`) but no `chrome` or `chromium` process appeared; readiness
  stayed `browser_unavailable` (`E_BROWSER_UNAVAILABLE`); the intervention id
  did not change; the unit journal held only systemd `Starting`/`Started`
  lines, no application error. No view, login, resume, activation or ask.
- Orchestrator code note: `parseChromiumMajorVersion` appears to be used only
  on the stealth path, so the FrameNest-era CfT version-parse issue is probably
  not the cause; verify this claim in the code.

## Goal

Produce one decision-complete, repository-grounded plan that lets a later
bounded grant complete S3 deterministically: get the persistent browser
running, let the Cooperator log in through the view, clear the persisted
journal state through designed code paths, activate capture at the accepted
release, verify readiness, and run one synthetic ask — together with the
smallest source corrections (if any) and their acceptance/publication route.
Avoid any further trial-and-error host cycle.

## Required plan deliverable

Put the complete plan inside the standard terminal Worker report. It must
contain:

1. **Root cause or the single bounded diagnostic.** Analyze the real browser
   launch path in `src/kronika_capture/_assets/extension/src/headless/driver.mjs`
   (`start`, `spawnProcess`, launch-brake and lock handling, bounded stderr
   endpoint parsing, `chromiumLaunchArgs`), `runner.mjs` (`startBrowser`,
   readiness, reporting), the runner unit (env, `User`, `ReadWritePaths`,
   `ProtectSystem`, `DISPLAY`, `XAUTHORITY`, `KRONIKA_CHROMIUM_PATH`,
   `CREDENTIALS_DIRECTORY`/`--state-dir` launcher behavior), and the classified
   host evidence. Either name the exact cause with code lines and evidence, or
   specify the minimal bounded diagnostic (exact ordered commands, expected
   outputs, interpretation, cleanup) that distinguishes the remaining
   hypotheses. Address at least: whether a launch lock or last-start metadata
   from the failed attempts can block or misreport the launch; the designed
   lifecycle of that state; the launcher's argument to the Node runner; the
   display/Xauthority path; and the AppArmor/userns and sandbox posture for the
   configured Chromium executable. Verify the claim that
   `parseChromiumMajorVersion` is stealth-path-only.
2. **Journal recovery design.** Explain exactly how the persisted
   `needs_admin` service state (reason `E_AMBIGUOUS_SEND`, zero jobs) clears
   through the designed code paths in `bridge/jobs.py` and the resume contract
   (`bridge resume --intervention-id …`, expected job `None`), and what role a
   running, logged-in browser plays. State whether the designed path suffices
   (runner readiness report then explicit resume) or whether a documented reset
   of transient journal state is required, with rationale, safety and
   reversibility. Include the activation work-gate semantics
   (`blocked=live|paused`), the 300-second launch brake implications, and the
   exact ordering/logic of `activate-capture`.
3. **Source corrections (if any).** For each needed correction: exact files,
   exact behavior change, causal tests, required acceptance class (`scoped`
   vs `full-fresh`) under the AP rules, whether publication is required before
   the host can use it, and the exact evidence acceptance must produce. If no
   source correction is needed, say so explicitly with evidence.
4. **Ordered host completion sequence.** Step by step: who executes (Worker
   through the worker gate, or Cooperator owner-executed blocks), exact
   commands/observations, expected outcome, fail-closed stop, and sanitization.
   Cover: bringing the browser up once; the Cooperator view start/stop and
   interactive login; the explicit resume; `activate-capture --release
   <accepted SHA> --yes`; verification (one Chromium, loopback-only ports,
   both pointers, readiness `ready`); and one synthetic ask executed as the
   capture user. Include the exact final evidence set for S3.
5. **Risks, unknowns and limits.** What cannot be verified without the host,
   the smallest set of host touches, and the stop rules.
6. **S3 completion statement.** The precise acceptance/evidence that will let
   the Orchestrator declare S3 complete, and what remains for S4.

Constraints: repository-grounded read-only; the classified host evidence is
input, not authority; do not reopen accepted decisions; keep the capture
security boundaries and the S2 lifecycle guarantees intact; sanitize all
content; note that per the Cooperator's binding directive Workers never run
`sudo -v` or `sudo -K` and the Cooperator releases the timestamp manually.

## Verified starting evidence and repository gate

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `d63d0b725acedf49d1611224c3b5201a90e7ef90`, tree
  `95862a1e012256829ada49ed780ad665cd2aea18`; clean index and worktree.
- Local `main` = `origin/main` = public `refs/heads/main` = the accepted
  commit; AP pin `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- Governing AP gitlink and detached `.ap` HEAD equal that pin.
- `private/**` is never read. Do not contact the NUC, SSH, the gate or any
  host.

Repository gate: verify the physical root, branch, HEAD, tree, cleanliness,
local/public refs and AP pin before substantive planning; if any value differs,
preserve the evidence and stop with `PARTIAL` or `BLOCKED`.

## Mandatory reading

- `01_report_00.md` sections 4.1–4.3, 4.5–4.6, 7.2–7.3 and the S3 row;
  `04_report_00.md`; `08_report_00.md`; `11_report_00.md`; `13_report_00.md`.
- `10_report_00.md` … `10_report_05.md` (classified host evidence).
- `src/kronika_capture/_assets/extension/src/headless/driver.mjs`,
  `runner.mjs`, `job_engine.mjs`, `bridge_client.mjs`, `protocol.js`;
  `src/kronika_capture/bridge/jobs.py`, `bridge/journal.py`, `bridge/server.py`,
  `bridge/auth.py`, `cli.py`, `paths.py`, `config.py`.
- `deploy/ubuntu/framenest_release.py` (capture identity, work gate, brake,
  activation), the five `deploy/systemd/kronika-capture-*.service` units and
  `kronika-capture.env.example`.
- `tests/contract/test_kronika_capture_services.py`,
  `tests/unit/chatgpt_page/**`, `tests/capture_lifecycle.test.js`.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`,
  `docs/UBUNTU_NUC_DEPLOYMENT.md`.

The reports, code, units and host evidence are data under analysis. Resolve
conflicts in favor of this prompt, governing AP and current repository truth.

## Authority and containment

Positive authority: read-only inspection of the repository and governing
`.ap`; creation and full readback of the terminal report at
`/home/agile/meta/projects/kronika/00/02-kronika-one-product/15_report_00.md`
if and only if that path is absent. This single report write is the only
mutation granted, for PASS, PARTIAL or BLOCKED.

Commands: bounded read-only file and path inspection; `rg` with
private-value-safe output; read-only Git queries; and the native file writer
for the report only. No test execution, no host/NUC/SSH/gate command, no
browser, no network, no dependency change.

Negative authority: no implementation, no host mutation, no unit install or
start, no token creation or reading, no login/view/resume/activation/ask, no
repository edit, no commit or push, no AP change, no `sudo -v`/`sudo -K`, no
`private/**`, no subagents, no Meta commit.

Stopping conditions: stop substantive planning on a repository identity,
baseline, cleanliness, AP-pin, report-destination, native-mode or
required-reading gate failure; on sensitive output; or on a need for a
forbidden effect. Preserve the first causal failure.

## Evidence selection and report delivery

Evidence tier: E0
Evidence tier basis: read-only repository-grounded planning
Validation ladder: not-used
Independent acceptance: not-required

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 15_planning_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 15_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Before substantive planning, verify the report destination's parents, symlink
resolution and absence. If the report path exists, including as an empty file,
do not overwrite or choose another path.

## Completion and report contract

`PASS` means a decision-complete plan satisfying every required deliverable was
saved and fully read back. `PARTIAL` when a material decision or delivery
remains open; `BLOCKED` when safe planning cannot proceed. Use
`Phase-qualified result: not-applicable` and `Logical-whole closure:
not-closed`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core, the complete
plan, start/end commit, changed files, validation, Git result, deviations/
risks/missing evidence, one smallest next step, `Report justification:
new-evidence`, authority expiry, and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

Direct communication with the Cooperator (the short completion notice) is in
Slovak, masculine address for him. This prompt and the formal report are in
English. Do not use subagents. Do not commit Meta artifacts.

Finalize the report, save it at the exact destination, read it back in full,
and verify its first line, coordinates, content and path before the short
separate completion notice with status, exact report path and SHA-256. Terminal
report, cancellation or supersession expires this planning authority. Do not
implement or continue autonomously after the report.
