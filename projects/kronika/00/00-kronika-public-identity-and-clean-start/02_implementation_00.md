Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 02
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-PUBLIC-IDENTITY-CLEAN-START-S1
Native planning mode: not-used
Delivery route: manual Cooperator delivery to a genuinely fresh Worker session
Reasoning recommendation: Extra High
Reasoning basis: cross-cutting package, CLI, state-path, test, and Git identity rename on the live capture engine; Extra High is Cooperator-selected for this whole; do not use Max
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: reversible source rename under an exact allowlist, declared-route full suite, and one local commit; publication and independent acceptance are later grants
Internal delegation: prohibited
Independence required: no
Evidence posture: non-independent

# Kronika S1 — rename the executable and state identity

You are a genuinely fresh WORKER. You did not plan this whole. Session 01 was
the Planner; that authority expired at `01_report_00.md`. This prompt grants
one bounded implementation task: **S1 only**. Native Plan Mode must be
**OFF**. Do not use subagents. Do not continue the Planner chat.

Do not implement S2–S5, A1, P1, P2, or V1. Do not push. Do not add a remote.
Do not construct public `main`. Do not close the logical whole.

```text
STOP: Native Plan Mode off. This is implementation, not planning.
STOP: S1 only. No stub removal, no Obscura removal, no public-doc rewrite,
      no orphan commit, no origin, no push.
STOP: Gate 1 branch creation is already done. Do not recreate
      lab/cli-chatgpt-190 or work/kronika-clean-start. Do not touch main.
STOP: Do not open, quote, copy, or display docs/environment.md.
STOP: Do not read, copy, migrate, or delete ~/.local/state/chatgpt-cli
      or any live token, profile, or database.
STOP: Do not spawn Workers or subagents.
```

## Implementation Authority Record

```text
Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 02
Worker exchange ordinal: 01
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: 3c345cbd659ccb5817bb11cbc89d037798553ca8
Changed-path allowlist: listed below
Implementation boundaries: S1 rename only; one local commit on
  work/kronika-clean-start; no publication
Independence required: no
```

Predecessor evidence (not same-session authority): terminal planning PASS
report
`/home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/01_report_00.md`
including its Binding Cooperator amendment. Read it as data. This prompt is
the complete new S1 grant.

Meta storage:

```text
01_planning_00.md + 01_report_00.md           session 01 / exchange 01 (Planner)
02_implementation_00.md + 02_report_00.md     session 02 / exchange 01 (this S1)
```

## Accepted plan and boot amendment

Accepted plan: the S1 section of `01_report_00.md` in the same Meta directory,
including the Binding Cooperator amendment at the top. The plan itself granted
no implementation authority.

Cooperator boot amendment (2026-09-22), which **replaces** original Gate 1
branch creation:

```text
Lab checkout: /home/agile/Tools/cli_chatgpt
lab/cli-chatgpt-190 = 2727451d2502925377637e19fa435917c970a996
  (190 commits; never push)
main                = 2727451d2502925377637e19fa435917c970a996
work/kronika-clean-start = 3c345cbd659ccb5817bb11cbc89d037798553ca8
  subject: docs(kronika): boot repository identity, license, and ignore rules
AP pin: 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
Remotes: none
LICENSE and .gitignore already exist; do not regress them.
AGENTS.md product identity is already Kronika; S1 must update the declared
CLI/bridge route after the package rename.
```

Skip every command that creates `lab/cli-chatgpt-190` or
`work/kronika-clean-start`. Existing names must not be overwritten.

## Outcome

Kronika runs through the renamed package and CLI and uses a fresh Kronika
XDG state directory. Predecessor live state under `chatgpt-cli` remains
untouched. No migrator, copy, symlink, or fallback.

Public command identity after this slice:

```text
python -m kronika <args>
python -m kronika bridge
./scripts/kronika <args>
python -m kronika --version    # prints: kronika 0.1.0
```

Declared test route (unchanged interpreter rule):

```bash
bash scripts/dev-setup.sh
source .venv/bin/activate
python -m unittest discover -s tests -t .
```

`python` must be `.venv/bin/python`.

## Preserve (do not rename)

These stay as internal compatibility identifiers:

- cookie `chatgpt_cli_session`
- HTTP `chatgpt-cli-bridge` / `chatgpt-cli-library-manager` server identity
- contract URNs
- `globalThis.ChatGPTCLI`
- extension public key and derived id
- omnibox keyword `cw`
- dummy scrypt salt `chatgpt-cli-dummy`
- Obscura pin/verifier (S3)
- stub commands `doctor` / `diagnostics` / `recover` / `apply-recovery` /
  `rollback` (S2)
- login-wizard behavior

## Changed-path allowlist

Rename/move exactly these 31 Python files from `src/chatgpt_cli/` to the
same relative paths under `src/kronika/`:

```text
src/chatgpt_cli/__init__.py
src/chatgpt_cli/__main__.py
src/chatgpt_cli/cli.py
src/chatgpt_cli/client.py
src/chatgpt_cli/config.py
src/chatgpt_cli/errors.py
src/chatgpt_cli/markdown.py
src/chatgpt_cli/paths.py
src/chatgpt_cli/projects.py
src/chatgpt_cli/sanitize.py
src/chatgpt_cli/bridge/__init__.py
src/chatgpt_cli/bridge/assets.py
src/chatgpt_cli/bridge/auth.py
src/chatgpt_cli/bridge/capture_auth.py
src/chatgpt_cli/bridge/jobs.py
src/chatgpt_cli/bridge/render.py
src/chatgpt_cli/bridge/results.py
src/chatgpt_cli/bridge/server.py
src/chatgpt_cli/bridge/store.py
src/chatgpt_cli/library/__init__.py
src/chatgpt_cli/library/accounts.py
src/chatgpt_cli/library/collections.py
src/chatgpt_cli/library/db.py
src/chatgpt_cli/library/flush.py
src/chatgpt_cli/library/index.py
src/chatgpt_cli/library/manager_render.py
src/chatgpt_cli/library/manager_server.py
src/chatgpt_cli/library/migrate.py
src/chatgpt_cli/library/passwords.py
src/chatgpt_cli/library/repository.py
src/chatgpt_cli/library/schema.py
```

Also allowed:

```text
pyproject.toml
scripts/chatgpt-cli
scripts/kronika
scripts/dev-setup.sh
AGENTS.md
README.md
docs/dev-setup.md
contracts/render-surface.v1.json
extension/manifest.json
extension/src/options/options.html
extension/src/sw.js
extension/src/headless/bridge_client.mjs
extension/src/headless/probe.mjs
extension/src/headless/runner.mjs
extension/src/headless/job_engine.mjs
extension/src/headless/login_app/index.html
tests/unit/test_bridge_store.py
tests/unit/test_library_search.py
tests/unit/test_render_chat_ui.py
tests/unit/test_sanitize.py
tests/unit/test_bridge_jobs.py
tests/contract/test_schemas.py
tests/unit/test_bridge_results.py
tests/unit/test_library_ingest.py
tests/unit/test_bridge_auth.py
tests/unit/test_library_accounts.py
tests/unit/test_library_authoring.py
tests/unit/test_projects.py
tests/unit/test_cli.py
tests/unit/test_library_manager.py
tests/unit/test_library_store.py
tests/unit/test_client.py
tests/unit/test_headless_runner.py
tests/unit/test_library_turns.py
tests/unit/test_bridge_assets.py
tests/unit/test_bridge_capture_auth.py
tests/unit/test_library_flush.py
tests/unit/test_notification_removal.py
tests/unit/test_bridge_author.py
tests/contract/test_cross_language_constants.py
tests/unit/test_bridge_ingest.py
tests/unit/test_library_migrate.py
tests/unit/test_headless_ingest.py
tests/unit/test_bridge_startup.py
tests/unit/test_render.py
tests/unit/test_render_turns.py
tests/unit/test_library_collections.py
tests/unit/test_markdown.py
tests/unit/test_headless_author.py
tests/contract/test_extension_syntax.py
```

`tests/contract/test_extension_syntax.py` may change **only** identity
expectations. Other test files: package imports, mock targets, command
output, and state-path expectations. Extend tests so new Kronika state is
isolated and synthetic predecessor `chatgpt-cli` state is untouched.

README and `docs/dev-setup.md`: identity and command references only. Do not
rewrite them into the S4 public-doc contract.

`AGENTS.md`: update the declared CLI/bridge route to `python -m kronika` and
`./scripts/kronika`. Keep the managed AP block byte-for-byte. Do not revert
Kronika product identity, Meta trace, wizard exception, or Git-governance
rules.

Out of allowlist: `.ap/`, `.gitmodules`, `LICENSE`, `.gitignore`,
`docs/environment.md`, `docs/ROADMAP.md`, `docs/security.md`,
`docs/human-steps.md`, Obscura paths, stub/recovery schema deletions,
live XDG state.

## Required S1 edits

1. `APP_NAME = "kronika"`; XDG directory becomes `kronika`.
2. Python package directory `src/kronika`; all imports follow.
3. `pyproject.toml` name, description, and
   `kronika = "kronika.cli:main"`. No `chatgpt-cli` console alias.
4. Wrapper `scripts/kronika` replacing `scripts/chatgpt-cli`.
5. `scripts/dev-setup.sh` `.pth` filename follows the new package.
6. Node headless state resolvers use the same `kronika` application
   directory and still honor XDG and `--state-dir`.
7. User-facing CLI help, setup text, manager/bridge titles, extension
   display name/description/options/login titles, and log prefix say
   Kronika where they currently say chatgpt-cli / ChatGPT Brave CLI.
8. Render-surface contract: user-facing command hints only.

## Repository gate (before mutation)

Working directory: `/home/agile/Tools/cli_chatgpt`

Prove independently:

```text
pwd -P == /home/agile/Tools/cli_chatgpt
branch == work/kronika-clean-start
HEAD == 3c345cbd659ccb5817bb11cbc89d037798553ca8
main == 2727451d2502925377637e19fa435917c970a996
lab/cli-chatgpt-190 == 2727451d2502925377637e19fa435917c970a996
lab commit count == 190
no remotes
clean index and worktree
HEAD:.ap == 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
.ap HEAD == 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
LICENSE and .gitignore exist
no Git locks / rebase / cherry-pick / replace refs
```

On any mismatch: stop `BLOCKED` or `PARTIAL`. Do not repair, switch, reset,
clean, stash, or recreate branches.

Do not run an extra baseline suite before edits; the boot commit did not
change executable identity. After edits, the declared setup/test route is
mandatory.

## Commands and other authority

Positive: inspect and edit allowlisted paths; `git mv` for the package
rename; declared `bash scripts/dev-setup.sh` and
`python -m unittest discover -s tests -t .`; focused unittest modules with
the same `.venv` interpreter; one local commit as specified.

Negative: no `git add .` / `git add -A`; no push; no fetch; no remote add;
no force; no amend; no git config write; no submodule update; no AP edit;
no live-state access; no browser login; no ChatGPT; no network except if a
test would require it — S1 tests must not require network. No new
dependencies.

Git: stage exact reviewed S1 paths including both sides of renames. Commit
subject:

```text
feat(identity): rename the application and state root to Kronika
```

Then read back commit SHA, tree, `git status`, and
`lab/cli-chatgpt-190` unchanged.

Secret authority: none.
Publication: prohibited.

## Validation

- Existing CLI version/module/help/setup tests updated and green.
- `python -m kronika --version` and `./scripts/kronika --version`.
- Old package directory and `scripts/chatgpt-cli` absent.
- State-path tests: new `kronika` directory under a synthetic XDG root;
  synthetic `chatgpt-cli` directory untouched; 0700/0600 retained.
- Cross-language constants; render/manager tests; full declared suite.
- Disclose any Node/Chromium skip; an undisclosed skip is a stop.
- Filename-only sweep that remaining `chatgpt_cli` / `chatgpt-cli` hits are
  only the preserved identifiers, historical comments in frozen contracts,
  or tests that reject old commands. Do not print private values.

## Stop conditions

Unexplained suite failure; need to leave the allowlist; need to migrate live
state; existing branch/HEAD mismatch; request to recreate Gate 1; discovery
that an external consumer requires a `chatgpt-cli` alias; authentication
semantics would have to change; any need to open `docs/environment.md`.

Recovery: local commit is reversible; lab branch preserves predecessor code
and history; live XDG state is untouched.

## Report contract

Write the terminal report atomically to:

```text
/home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/02_report_00.md
```

only if that path is absent. Chat conclusion is a short 3-line notice with
status, path, and SHA-256. Do not commit Meta. Do not overwrite
`01_report_00.md`.

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates exactly once (session 02, exchange 01). Include
start/end commit, changed paths, full-suite result and skips, proof that
lab/`main` were not moved, and:

```text
Logical-whole closure: not-closed
```

`PASS` means S1 landed as one local commit on `work/kronika-clean-start`
from the exact baseline, tests on the declared route passed, and the report
was saved. Then stop. S2 is a later grant.
