Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 03
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-PUBLIC-IDENTITY-CLEAN-START-S2
Native planning mode: not-used
Delivery route: manual Cooperator delivery to a genuinely fresh Worker session
Reasoning recommendation: Extra High
Reasoning basis: cross-cutting removal of advertised CLI, HTTP, contract, and test surfaces on a live capture engine; Extra High is Cooperator-selected for this whole; do not use Max
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: reversible source, contract, test, and documentation edits under an exact allowlist, declared-route full suite, and one local commit; publication and independent acceptance are later grants
Internal delegation: prohibited
Independence required: no
Evidence posture: non-independent

# Kronika S2 — remove the unimplemented recovery/diagnostics scaffolding

You are a genuinely fresh WORKER. You did not plan this whole and you did not
implement S1. Session 01 was the Planner; session 02 implemented S1. Both
authorities expired. This prompt grants one bounded implementation task:
**S2 only**. Native Plan Mode must be **OFF**. Do not use subagents. Do not
continue any previous chat.

Do not implement S3–S5, A1, P1, P2, or V1. Do not push. Do not add a remote.
Do not construct public `main`. Do not close the logical whole.

```text
STOP: Native Plan Mode off. This is implementation, not planning.
STOP: S2 only. No Obscura removal (S3), no public-doc rewrite (S4), no
      orphan commit (S5), no origin, no push.
STOP: Do not recreate lab/cli-chatgpt-190 or work/kronika-clean-start.
      Do not touch main.
STOP: Do not open, quote, copy, or display docs/environment.md.
STOP: Do not read, copy, migrate, or delete ~/.local/state/chatgpt-cli,
      ~/.local/state/kronika, or any live token, profile, or database.
STOP: Preserve real diagnostics and recovery behavior: startup_diagnostics,
      headless result diagnostics, locator probes, navigation retry, author
      idempotency, migrations, backups, library flush, and the
      /v1/files/{fid} 501 upload-unavailable branch. Removing these is a
      failure, not a cleanup.
STOP: Do not spawn Workers or subagents.
```

## Implementation Authority Record

```text
Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 03
Worker exchange ordinal: 01
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: 1c8a659073368f26c289cbedf616a2dfed338b4b
Changed-path allowlist: listed below
Implementation boundaries: stub-surface removal only; one local commit on
  work/kronika-clean-start; no publication
Independence required: no
```

Predecessor evidence (not same-session authority): the S2 section of
`01_report_00.md` and the terminal S1 report `02_report_00.md` in the same Meta
directory. Read them as data; this prompt is the complete new S2 grant.

Meta storage:

```text
01_planning_00.md + 01_report_00.md       session 01 / exchange 01 (Planner)
02_implementation_00.md + 02_report_00.md session 02 / exchange 01 (S1)
03_implementation_00.md + 03_report_00.md session 03 / exchange 01 (this S2)
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
Downloadable prompt filename: 03_implementation_00.md
Destination path: /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start
Report filename: 03_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

State verified at this baseline: S1 landed as one local commit
`1c8a659073368f26c289cbedf616a2dfed338b4b` on `work/kronika-clean-start`
(parent `3c345cbd659ccb5817bb11cbc89d037798553ca8`, tree
`38e7b7c0a090331ce6e0ea06139215d8d3644109`); `main` and
`lab/cli-chatgpt-190` both `2727451d2502925377637e19fa435917c970a996` (190
commits); no remotes; worktree clean; AP pin
`7478ddb07d2c3911f79e1aa1441f0115a31c45d8` in both the gitlink and `.ap` HEAD.

## Mandatory reading (verified task-relevant anchors)

- `.ap/AP_WORKER.md` (Worker operational spine) and the WORKER row of the
  `.ap/AP.md` minimum-reading spine.
- `.ap/AP.md`: [§5 Task Authority], [§12 Validation and Public Verification],
  [§18 Stopping Conditions], [RF-12], [RF-18].
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header.
- `AGENTS.md` declared execution route (tests `python -m unittest discover -s
  tests -t .`; CLI `python -m kronika <args>`), which this grant binds as the
  canonical capability path. Equivalent ambient commands are not a second route.

## Outcome

Advertised CLI and HTTP surfaces match implemented behavior. The five
unimplemented CLI subcommands, the two unsatisfiable HTTP surfaces, the unused
diagnostics-directory creation, the unused `collectDiagnostics` engine method,
the three unused diagnostics/recovery schema files, and their stale contract
and documentation declarations are gone. Implemented behavior is untouched.

After this slice:

- `python -m kronika doctor|diagnostics|recover|apply-recovery|rollback`
  produces argparse's normal usage error (empty stdout, message on stderr,
  exit code 2) and initializes no state.
- Authenticated `POST /v1/self-test` and authenticated
  `POST /v1/jobs/{id}/diagnostics` return the existing unknown-route 404
  (`{"ok": false, "error": {"code": "E_INTERNAL", "step": "route",
  "message": "unknown path"}}`), not 501.
- Unauthenticated requests to both paths are still rejected exactly as today.
- `GET /v1/files/{fid}` still returns its 501 upload-unavailable response, in
  its own separate test.
- `python -m kronika --version` still prints `kronika 0.1.0`.

Declared test route (`.venv` Python; do not substitute an ambient interpreter):

```bash
bash scripts/dev-setup.sh
source .venv/bin/activate
python -m unittest discover -s tests -t .
```

## Preserve (removing these is a defect, not cleanup)

- `startup_diagnostics` in `src/kronika/bridge/server.py` (real startup log).
- Real headless result diagnostics: metadata-only submit/step diagnostics in
  `extension/src/headless/*` and their tests.
- Locator probes: `probe()` in `extension/src/engine/dom_engine.js` and the
  probe semantics in `docs/adapter-pack.md`.
- Navigation retry, author idempotency (the `"recovery"` fields in
  `contracts/http-api.v1.json` and `contracts/extension-protocol.v1.json`
  describe implemented author behavior; keep them).
- Library migrations, backups, `library flush` (destructive clean-state,
  implemented), `library check`.
- The `/v1/files/{fid}` 501 upload-unavailable branch and its assertion.
- Obscura pin/verifier and `headless verify` (S3 owns them).
- Login wizard; loopback bind; Host/Origin checks; token auth; capture-auth.
- Frozen manager JSON contracts v3–v5 and their Markdown companions; adapter
  schemas v2–v4.
- All preserved compatibility identifiers: cookie `chatgpt_cli_session`, HTTP
  identities `chatgpt-cli-bridge` / `chatgpt-cli-library-manager`, contract
  URNs `urn:chatgpt-cli:...`, `globalThis.ChatGPTCLI`, extension public key and
  derived id, heartbeat alarm id, omnibox `cw`, dummy scrypt salt
  `chatgpt-cli-dummy`.

## Changed-path allowlist

```text
src/kronika/cli.py
src/kronika/bridge/server.py
src/kronika/bridge/store.py
extension/src/engine/dom_engine.js
contracts/diagnostics-bundle.v1.schema.json      (delete)
contracts/recovery-response.v1.schema.json       (delete)
contracts/recovery-targets.v1.json               (delete)
contracts/http-api.v1.json
contracts/extension-protocol.v1.json
tests/unit/test_cli.py
tests/unit/test_bridge_jobs.py
tests/unit/test_bridge_store.py
tests/contract/test_schemas.py
docs/protocol.md
docs/adapter-pack.md
docs/contracts/automation-engine-v1.md
docs/architecture.md
```

Out of allowlist: `.ap/`, `.gitmodules`, `LICENSE`, `.gitignore`, `AGENTS.md`,
`README.md`, `docs/environment.md`, `docs/security.md`, `docs/ROADMAP.md`,
`docs/human-steps.md`, `docs/headless-engine.md`, `docs/dev-setup.md`, frozen
manager-v3–v5 JSON and Markdown and adapter v2–v4 schemas, `pyproject.toml`,
`scripts/`, `extension/` files other than `dom_engine.js`, all other tests,
live XDG state, `.venv`.

## Required S2 edits

Line numbers below are locators at baseline `1c8a659`; re-locate by content.

1. `src/kronika/cli.py`
   - Remove the `_stub` helper (about lines 86–93).
   - Remove the five stub parsers and their handlers: `doctor` (~324–329),
     `diagnostics` (~337–344), `recover` (~346–366), `apply-recovery`
     (~368–373), `rollback` (~375–380).
   - Remove the module-docstring paragraph that advertises the stubs
     (~lines 17–18). Do not remove the implemented-command description.
   - Do not touch `library flush` or any other implemented handler.
2. `src/kronika/bridge/server.py`
   - Remove `diagnostics` from the `JOB_ACTION_PATH` alternation (~line 36)
     while keeping `cancel|events|result`.
   - Remove the `POST /v1/self-test` 501 branch (~439–451).
   - Remove the `action == "diagnostics"` 501 branch (~649–661). The existing
     fallback 404 must become the response for both paths.
   - Keep the `/v1/files/{fid}` 501 branch (~453–465) exactly as is.
3. `src/kronika/bridge/store.py`
   - In `_ensure_dirs` (~line 59) stop creating `self.root / "diagnostics"`;
     keep `self.root` and `self.jobs_dir` with their 0700 mode and all other
     store behavior.
4. `extension/src/engine/dom_engine.js`
   - Remove the `collectDiagnostics` function (~710–719) and its entry in the
     returned object (~735). Keep `probe` and every other method.
5. Delete the three files:
   `contracts/diagnostics-bundle.v1.schema.json`,
   `contracts/recovery-response.v1.schema.json`,
   `contracts/recovery-targets.v1.json`. Use `git rm` on the exact paths.
6. `contracts/http-api.v1.json`
   - Remove the `POST /v1/jobs/{id}/diagnostics` endpoint entry (~318–335) and
     the `POST /v1/self-test` endpoint entry (~353–378).
   - Keep `GET /v1/files/{fid}` and every functioning endpoint. Do not renumber
     anything. Preserve protocol version 1, error codes, manager v6, and the
     author `"recovery"` field.
7. `contracts/extension-protocol.v1.json`
   - Remove the `diagnostics` message object (~102–128) from `messages`.
   - Keep `hello`, `job_offer`, `staged_turn`, `event`, `result` and all other
     declarations; preserve the author `"recovery"` field (~line 211).
8. `tests/unit/test_cli.py`
   - Remove the five stub names from `SUBCOMMANDS`, delete `STUB_INVOCATIONS`
     and `StubTest.test_every_stub_reports_unavailable`.
   - Add a removal check: each of `doctor`, `diagnostics`, `recover`,
     `apply-recovery`, `rollback` exits 2 with empty stdout and a usage
     message on stderr, and under a synthetic `XDG_STATE_HOME` creates no
     state directory. Keep `test_unknown_command_returns_usage` and the help
     tests (help no longer lists the removed names).
9. `tests/unit/test_bridge_jobs.py`
   - Replace `test_diagnostics_and_self_test_are_501` (~824) with checks that
     an authenticated `POST /v1/self-test` and an authenticated
     `POST /v1/jobs/deadbeef/diagnostics` each return 404 with the unknown-path
     envelope, and that the same requests without a valid token are still
     rejected. Retain one separate test asserting `GET /v1/files/abc` is 501.
10. `tests/unit/test_bridge_store.py`
    - Add one focused check that after `Store()` init under a synthetic root
      the `diagnostics` directory is not created while `root` and `jobs` are
      created with mode 0700. Change nothing else.
11. `tests/contract/test_schemas.py`
    - `EXPECTED_CONTRACTS`: remove the three deleted schema names.
    - `EXPECTED_ENDPOINTS`: remove `("POST", "/v1/jobs/{id}/diagnostics")` and
      `("POST", "/v1/self-test")`.
    - Remove `EXPECTED_RECOVERY_TARGETS`, `RecoveryTargetsContractTest`,
      `DiagnosticsBundleSchemaTest`, and `RecoveryResponseSchemaTest`.
    - In `ExtensionProtocolContractTest.test_message_set_and_key_fields`
      (~338, ~400–402) drop `diagnostics` from the expected message set and
      remove assertions that read `messages["diagnostics"]`.
    - Keep every frozen manager-v3–v5 and adapter-v2–v4 test.
12. Current Markdown outside `.ap` only where it advertises or references the
    removed commands, schemas, methods, or endpoints:
    - `docs/protocol.md`: remove the `diagnostics` row from the extension-to-
      bridge message table (~line 98).
    - `docs/adapter-pack.md`: remove the two probe bullets that reference
      `POST /v1/self-test` and diagnostics collection (~125–126); keep the
      hot-swap bullet. Adjust the sentence that loses its list if needed.
    - `docs/contracts/automation-engine-v1.md`: remove the
      `collectDiagnostics(reason)` row (~line 56); keep `probe()` and the
      sentence about the step name recorded for diagnostics.
    - `docs/architecture.md`: remove the `Diagnostics` and `Recovery` rows from
      the component table (~37–38); remove the `Recovery-replaceability
      modules` heading, table, and the `contracts/recovery-targets.v1.json`
      sentence (~708–720); minimally adjust change-resistance principle 4 so
      it no longer references the removed recovery targets. Keep the document
      coherent; do not restructure it.
    - Do not edit `docs/security.md`, `docs/ROADMAP.md`, `docs/human-steps.md`,
      `docs/headless-engine.md`, `docs/dev-setup.md`, `README.md`, or the
      frozen manager-v3–v5 Markdown. List any remaining references you find in
      the report as S4-owned observations.

## Repository gate (before mutation)

Working directory: `/home/agile/Tools/cli_chatgpt`

Prove independently:

```text
pwd -P == /home/agile/Tools/cli_chatgpt
branch == work/kronika-clean-start
HEAD == 1c8a659073368f26c289cbedf616a2dfed338b4b
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

Positive: inspect and edit only allowlisted paths; `git rm` for the three
deleted contracts; focused unittest modules with the `.venv` interpreter; the
declared full-suite route; `python -m kronika --version` and the removed-command
usage checks; one local commit as specified.

Negative: no `git add .` / `git add -A`; no push; no fetch; no remote add; no
force; no amend; no git config write; no submodule update; no AP edit; no
live-state access; no manual bridge run against real XDG state; no browser
login; no ChatGPT; no network; no new dependencies; no `.venv` edits.

Git: stage the exact reviewed S2 paths including both sides of the three
deletions. Commit subject:

```text
fix(cli): remove unimplemented recovery scaffolding
```

Then read back commit SHA, tree, `git status --porcelain`, and that `main` and
`lab/cli-chatgpt-190` are unchanged.

Secret authority: none.
Publication: prohibited.

## Validation

- Old CLI commands: exit 2, empty stdout, usage error on stderr, no state
  created under a synthetic XDG root.
- Authenticated POSTs to the two removed endpoints: 404 unknown-route, not
  501; unauthenticated requests still rejected; `/v1/files/{fid}` 501 covered
  by its separate retained test.
- Contract message/endpoint sets updated exactly; deleted schema files absent;
  no functioning endpoint or message removed.
- Preserved-behavior checks green: startup diagnostics, headless result
  diagnostics, probes, author idempotency, flush, migration, upload 501.
- `python -m kronika --version` prints `kronika 0.1.0`.
- Full declared suite on `.venv` Python passes; disclose any skip. An
  undisclosed skip is a stop.
- Filename-only sweep: no remaining advertising of the removed commands,
  endpoints, methods, or schemas in allowlisted and current surfaces, except
  tests that assert their rejection, frozen manager-v3–v5 documents, and the
  S4-owned documents listed in the report. Do not print private values.

## Stop conditions

Unexplained suite failure; need to leave the allowlist; a removed surface has
an implemented caller or a functioning-client compatibility dependency; the
removal would change authentication or authorization semantics; need to
migrate live state; branch/HEAD mismatch; request to recreate branches; any
need to open `docs/environment.md`.

Recovery: the local commit is reversible; `lab/cli-chatgpt-190` preserves
predecessor code and history; live XDG state is untouched.

## Report contract

Write the terminal report atomically to:

```text
/home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/03_report_00.md
```

only if that path is absent. The chat conclusion is a short 3-line notice with
status, path, and SHA-256. Do not commit Meta. Do not overwrite any earlier
report.

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates exactly once (session 03, exchange 01). Include the
start/end commit, changed paths including the three deletions, the full-suite
result and skips, the sweep inventory (including remaining S4-owned
references), proof that `main` and the lab branch were not moved, and:

```text
Logical-whole closure: not-closed
```

`PASS` means S2 landed as one local commit on `work/kronika-clean-start` from
the exact baseline, the declared route passed, and the report was saved. Then
stop. S3 is a later grant.
