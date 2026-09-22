Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 04
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-PUBLIC-IDENTITY-CLEAN-START-S3
Native planning mode: not-used
Delivery route: manual Cooperator delivery to a genuinely fresh Worker session
Reasoning recommendation: Extra High
Reasoning basis: cross-cutting removal of a second headless engine across driver, probe, CLI, config, tests, and current documentation; Extra High is Cooperator-selected for this whole; do not use Max
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: reversible source, test, and documentation edits plus one tracked-file deletion under an exact allowlist, declared-route full suite, and one local commit; publication and independent acceptance are later grants
Internal delegation: prohibited
Independence required: no
Evidence posture: non-independent

# Kronika S3 — remove the parked Obscura engine

You are a genuinely fresh WORKER. You did not plan this whole and you did not
implement S1 or S2. Those authorities expired. This prompt grants one bounded
implementation task: **S3 only**. Native Plan Mode must be **OFF**. Do not use
subagents. Do not continue any previous chat.

Do not implement S4, S5, A1, P1, P2, or V1. Do not push. Do not add a remote.
Do not construct public `main`. Do not close the logical whole.

```text
STOP: Native Plan Mode off. This is implementation, not planning.
STOP: S3 only. No public-doc rewrite (S4), no orphan commit (S5), no origin,
      no push.
STOP: Do not recreate lab/cli-chatgpt-190 or work/kronika-clean-start.
      Do not touch main.
STOP: Do not open, quote, copy, or display docs/environment.md.
STOP: Do not read, copy, migrate, or delete ~/.local/state/chatgpt-cli,
      ~/.local/state/kronika, or any live token, profile, or database.
STOP: Do not uninstall, move, patch, or delete any host binary or engine
      install (~/.local/opt/obscura included). Do not touch real Chromium
      profiles. This slice removes repository code and current documentation
      only.
STOP: Preserve Chromium behavior: BaseCdpDriver, ChromiumDriver, the raw-CDP
      client, navigate retry/timeout, the login wizard, resource policy,
      ingest, authoring, deep research, probe admission and the
      E_PROBE_CHROME_MISSING failure.
STOP: Do not rename `chatgpt-cli`/`chatgpt_cli` identity strings in the docs
      you touch; S4 owns the identity rewrite. Remove only Obscura material.
STOP: Do not spawn Workers or subagents.
```

## Implementation Authority Record

```text
Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 04
Worker exchange ordinal: 01
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: f25392472d043d753a3844c3a9a6321ae5cf09a5
Changed-path allowlist: listed below
Implementation boundaries: parked-engine removal only; one local commit on
  work/kronika-clean-start; no publication
Independence required: no
```

Predecessor evidence (not same-session authority): the S3 section of
`01_report_00.md` and the terminal reports `02_report_00.md` (S1) and
`03_report_00.md` (S2) in the same Meta directory. Read them as data; this
prompt is the complete new S3 grant.

Meta storage:

```text
01_planning_00.md + 01_report_00.md       session 01 / exchange 01 (Planner)
02_implementation_00.md + 02_report_00.md session 02 / exchange 01 (S1)
03_implementation_00.md + 03_report_00.md session 03 / exchange 01 (S2)
04_implementation_00.md + 04_report_00.md session 04 / exchange 01 (this S3)
```

External trace and delivery record:

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/
Trace project key: kronika
Trace logical-whole projection identity: kronika-public-identity-and-clean-start
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 04_implementation_00.md
Destination path: /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start
Report filename: 04_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

State verified at this baseline: S2 landed as one local commit
`f25392472d043d753a3844c3a9a6321ae5cf09a5` on `work/kronika-clean-start`
(parent `1c8a659073368f26c289cbedf616a2dfed338b4b`, tree
`209bb1c2d7769f1139f589779539955ba21d556f`, subject
`fix(cli): remove unimplemented recovery scaffolding`); `main` and
`lab/cli-chatgpt-190` both `2727451d2502925377637e19fa435917c970a996` (190
commits); no remotes; worktree clean; AP pin
`7478ddb07d2c3911f79e1aa1441f0115a31c45d8` in both the gitlink and `.ap` HEAD.

## Mandatory reading (verified task-relevant anchors)

- `.ap/AP_WORKER.md` (Worker operational spine) and the WORKER row of the
  `.ap/AP.md` minimum-reading spine.
- `.ap/AP.md`: [§5 Task Authority], [§9 Git and Remote Safety], [§10 Security
  Boundaries], [§12 Validation and Public Verification], [§18 Stopping
  Conditions], [RF-12], [RF-18].
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header.
- `AGENTS.md` declared execution route (tests `python -m unittest discover -s
  tests -t .`; CLI `python -m kronika <args>`), which this grant binds as the
  canonical capability path. Equivalent ambient commands are not a second route.

## Outcome

Chromium is the sole headless implementation and documented engine. The
`ObscuraDriver`, the probe's engine/engine-path selection, the Obscura pin
constants, the `headless verify` command and its handlers, the parked patch
notes, and the current documentation that presents Obscura as the pinned or
selectable engine are gone. Every shared Chromium behavior is preserved.

After this slice:

- `node extension/src/headless/probe.mjs ...` admits Chromium only;
  `--engine obscura` and `--engine-path` are rejected as unknown arguments in
  `parseArgs`, before any profile directory or process is touched.
- `python -m kronika headless verify` (and `headless`) exits 2 with the normal
  argparse usage error and initializes no state.
- `python -m kronika --version` still prints `kronika 0.1.0`.
- The four shared-behavior fake-driver harnesses run against `ChromiumDriver`
  with `chromePath: "unused"` and keep their fill, click, retry, and
  fingerprint assertions.

Declared test route (`.venv` Python; do not substitute an ambient interpreter):

```bash
bash scripts/dev-setup.sh
source .venv/bin/activate
python -m unittest discover -s tests -t .
```

## Preserve (removing these is a defect, not cleanup)

- `BaseCdpDriver`, `ChromiumDriver`, and `cdp_client.mjs` behavior: raw CDP
  transport, endpoint discovery via `DevToolsActivePort`, loopback assertions,
  `Target.createTarget`/`attachToTarget`, evaluate, screenshot, stop.
- Navigate retry/timeout semantics (`navigateRetries = 1`,
  `E_DRIVER_NAVIGATE_RETRY`, `E_DRIVER_TIMEOUT`).
- Login wizard: probe `login` mode, `login_server.mjs`, `login_app/`, the
  fill/click/no-progress error semantics, and the bounded snapshot helpers.
- Resource policy, answer asset capture, follow-up ingest, authoring, deep
  research, and their tests.
- Probe flags that stay: `--profile`, `--url`, `--chrome-path`, `--headed`,
  `--stealth` (Chromium meaning), and the `E_PROBE_CHROME_MISSING` failure
  before any process starts.
- Profile/screenshot privacy: engine-owned profiles and
  `<state>/headless-probe/` 0700/0600 output.
- Bridge client, runner, job engine, contracts, and compatibility identifiers.
- The real headless result diagnostics preserved by S2.

## Changed-path allowlist

```text
tools/obscura-patches/README.md                  (delete)
extension/src/headless/driver.mjs
extension/src/headless/probe.mjs
extension/src/headless/cdp_client.mjs
src/kronika/cli.py
src/kronika/config.py
tests/unit/test_cli.py
tests/contract/test_extension_syntax.py
docs/headless-engine.md
docs/human-steps.md
docs/architecture.md
docs/security.md
```

Out of allowlist: `.ap/`, `.gitmodules`, `LICENSE`, `.gitignore`, `AGENTS.md`,
`README.md`, `docs/environment.md`, `docs/ROADMAP.md`, `docs/dev-setup.md`,
`docs/protocol.md`, `docs/adapter-pack.md`, `docs/contracts/**`, contracts,
`extension/src/headless/runner.mjs`, `job_engine.mjs`, `bridge_client.mjs`,
`login_server.mjs`, `login_app/**`, all other tests, live XDG state, `.venv`,
and every host install outside the repository.

## Required S3 edits

Line numbers below are locators at baseline `f253924`; re-locate by content.

1. `extension/src/headless/driver.mjs`
   - Remove `class ObscuraDriver extends BaseCdpDriver` and its whole body
     (~984–1122).
   - Update the header comment so the seam describes Chromium only.
   - Remove `pickFreePort` and the `node:net` `createServer` import if no
     remaining caller exists; keep `loopbackUrl`, `spawn`, `spawnSync`,
     `readChromiumMajorVersion`, and every Chromium helper.
2. `extension/src/headless/probe.mjs`
   - Remove the `ObscuraDriver` import, `DEFAULT_ENGINE_PATH`, `ENGINES`,
     `DEFAULT_ENGINE` (or keep only what Chromium still needs), the `--engine`
     and `--engine-path` parsing and validation, `options.engine` /
     `options.enginePath`, the Obscura branch of `newDriver`, and every
     `options.engine === "obscura"` ternary (~370, ~425, ~471, ~524, ~925).
   - Usage text and header comment become Chromium-only; `--stealth` keeps its
     Chromium meaning only.
   - Probe result JSON stays truthful: either a constant `engine: "chromium"`
     or the field removed, and `engine_binary` becomes
     `basename(options.chromePath)`. Pick the smaller coherent change.
   - Unknown `--engine` / `--engine-path` are rejected by `parseArgs` before
     `ensureProfileDir` or any process access.
3. `extension/src/headless/cdp_client.mjs`
   - Update the header comment that says the code was extracted from the
     Obscura driver; describe it neutrally. No behavior change.
4. `src/kronika/cli.py`
   - Remove the `headless` subparser group (its only action was `verify`),
     `_cmd_headless`, `_headless_verify`, and the module-docstring sentence
     that advertises `headless verify`.
   - Remove the now-unused imports (`hashlib`, `subprocess`, and the three
     `HEADLESS_*` config imports). `getpass` and `socket` remain used.
5. `src/kronika/config.py`
   - Remove `HEADLESS_ENGINE_VERSION`, `HEADLESS_ENGINE_SHA256`, and
     `HEADLESS_VERIFY_TIMEOUT_S` when no remaining caller exists.
6. `tests/unit/test_cli.py`
   - Remove `HeadlessVerifyTest` and `headless` from `SUBCOMMANDS`.
   - Add a removal check: `headless` and `headless verify` exit 2 with a usage
     error, empty stdout, and no state directory under a synthetic
     `XDG_STATE_HOME`. Keep the bridge-status `client: headless` tests
     (~302–311); those test the bridge client kind, not the CLI command.
7. `tests/contract/test_extension_syntax.py`
   - Retarget the four shared-behavior fake-driver harnesses from
     `ObscuraDriver` to `ChromiumDriver`, using `chromePath: "unused"`:
     `FakeFillDriver` (~877), `FakeClickDriver` (~948), `FakeDriver` (~1192),
     `FakeFingerprintDriver` (~1440). Preserve their fill, click, retry, and
     fingerprint assertions.
   - Retarget `test_driver_exposes_both_engines_behind_one_seam` (~1280) to a
     Chromium-only seam test: drop the `ObscuraDriver` symbol, keep
     `BaseCdpDriver`, `ChromiumDriver`, `CHROMIUM_BINARY_CANDIDATES`,
     `pickChromiumBinary`, `chromiumLaunchArgs`, `chromiumUserAgent`,
     `readChromiumMajorVersion`, `fingerprint`,
     `--disable-blink-features=AutomationControlled`,
     `parseDevToolsActivePort`, `readDevToolsActivePort`, `DevToolsActivePort`,
     `Target.attachToTarget`, `_awaitEndpoint`; rename the test accordingly.
   - Replace `test_probe_defaults_to_chromium_and_keeps_obscura_selectable`
     (~1508) with: probe admits Chromium only, still checks
     `E_PROBE_CHROME_MISSING`, `--chrome-path`, `--headed`,
     `existsSync(options.chromePath)`, and asserts that `--engine obscura` and
     `--engine-path` are rejected before process/profile access.
8. Current documentation that presents Obscura as the pinned or selectable
   engine (remove Obscura-only material; do not rename product identity):
   - `docs/headless-engine.md`: correct the Pinned install section (engine
     table and the `headless verify` command/paragraph), the driver
     description, the probe usage block and flag semantics, the login example,
     the profile path, and the stealth semantics to Chromium-only. Historical
     HE-* chronology subsections (HE-3e attempt, HE-2h outcome, PLAN-HE-01
     decision record, Cooperator acceptance) may keep clearly historical
     Obscura mentions; list each in the report as S4-owned.
   - `docs/architecture.md`: update the engine-process and engine-profile
     sentences (~271, ~280) to Chromium only.
   - `docs/security.md`: correct the Obscura pin/verify/profile claims
     (~216–218, ~237–242, ~254–255) and the "Chromium/Obscura headless
     engines" phrase (~1267) to Chromium-only facts. Do not rewrite the
     historical Cooperator residual-risk quotes (~207–209, ~277).
   - `docs/human-steps.md`: remove the optional parked-Obscura pin step
     (~244–245).
   - `docs/ROADMAP.md`: historical ledger scheduled for S4 removal. Do not
     edit; list its remaining Obscura references in the report as S4-owned.
   - `docs/environment.md`: never open; excluded; S4 deletes it by path.

## Repository gate (before mutation)

Working directory: `/home/agile/Tools/cli_chatgpt`

Prove independently:

```text
pwd -P == /home/agile/Tools/cli_chatgpt
branch == work/kronika-clean-start
HEAD == f25392472d043d753a3844c3a9a6321ae5cf09a5
main == 2727451d2502925377637e19fa435917c970a996
lab/cli-chatgpt-190 == 2727451d2502925377637e19fa435917c970a996
lab commit count == 190
no remotes
clean index and worktree
HEAD:.ap == 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
.ap HEAD == 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
no Git locks / rebase / cherry-pick / replace refs
```

On any mismatch: stop `BLOCKED` or `PARTIAL`. Do not repair, switch, reset,
clean, stash, or recreate branches.

## Commands and other authority

Positive: inspect and edit only allowlisted paths; `git rm` for the parked
patch notes; focused unittest modules with the `.venv` interpreter; the declared
full-suite route; `node --input-type=module` harness runs through the existing
tests; `python -m kronika --version` and the removed-command usage checks; one
local commit as specified.

Negative: no `git add .` / `git add -A`; no push; no fetch; no remote add; no
force; no amend; no git config write; no submodule update; no AP edit; no
live-state access; no host-binary or engine-install changes; no real Chromium
profile access; no browser login; no ChatGPT; no network; no new dependencies;
no `.venv` edits.

Git: stage the exact reviewed S3 paths including the deletion. Commit subject:

```text
fix(headless): remove the parked engine integration
```

Then read back commit SHA, tree, `git status --porcelain`, and that `main` and
`lab/cli-chatgpt-190` are unchanged.

Secret authority: none.
Publication: prohibited.

## Validation

- Probe admission: Chromium only; `--engine obscura` and `--engine-path`
  rejected before process/profile access; `E_PROBE_CHROME_MISSING` retained.
- `python -m kronika headless verify` and `headless` exit 2 with usage error
  and no state creation; `python -m kronika --version` prints `kronika 0.1.0`.
- The four retargeted fake-driver harnesses pass with their original
  assertions; the Chromium seam test passes; driver/login tests pass.
- Headless runner/ingest/author/deep-research modules and resource-policy and
  real Chromium synthetic fixtures still pass.
- Full declared suite on `.venv` Python passes; disclose any skip. An
  undisclosed skip is a stop.
- Filename-only sweep: no `Obscura` reference remains in `src/`, `extension/`,
  `scripts/`, `tests/`, `contracts/`, or the allowlisted docs, except clearly
  historical records explicitly listed as S4-owned. Do not print private
  values.

## Stop conditions

Unexplained suite failure; need to leave the allowlist; a shared helper whose
behavior cannot be preserved; need to uninstall a host binary or touch a real
profile; need to migrate live state; branch/HEAD mismatch; request to recreate
branches; any need to open `docs/environment.md`.

Recovery: the local commit is reversible; `lab/cli-chatgpt-190` preserves
predecessor code and history; the parked host binary and live XDG state are
untouched.

## Report contract

Write the terminal report atomically to:

```text
/home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/04_report_00.md
```

only if that path is absent. The chat conclusion is a short 3-line notice with
status, path, and SHA-256. Do not commit Meta. Do not overwrite any earlier
report.

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates exactly once (session 04, exchange 01). Include the
start/end commit, changed paths including the deletion, the full-suite result
and skips, the sweep inventory (including S4-owned historical references),
proof that `main` and the lab branch were not moved, and:

```text
Logical-whole closure: not-closed
```

`PASS` means S3 landed as one local commit on `work/kronika-clean-start` from
the exact baseline, the declared route passed, and the report was saved. Then
stop. S4 is a later grant.
