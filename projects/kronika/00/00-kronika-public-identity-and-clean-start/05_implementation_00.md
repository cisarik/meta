Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 05
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-PUBLIC-IDENTITY-CLEAN-START-S4
Native planning mode: not-used
Delivery route: manual Cooperator delivery to a genuinely fresh Worker session
Reasoning recommendation: Extra High
Reasoning basis: cross-cutting public-documentation rewrite and private-material removal across the whole tree, with security-claim accuracy and link/privacy gates; Extra High is Cooperator-selected for this whole; do not use Max
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E1
Evidence-tier basis: documentation and root-file changes plus path-only deletions, no executable change; focused link, command, and privacy checks; independent acceptance at A1
Internal delegation: prohibited
Independence required: no
Evidence posture: non-independent

# Kronika S4 — public documentation and clean tree

You are a genuinely fresh WORKER. You did not plan this whole and you did not
implement S1–S3. Those authorities expired. This prompt grants one bounded
implementation task: **S4 only**. Native Plan Mode must be **OFF**. Do not use
subagents. Do not continue any previous chat.

Do not implement S5, A1, P1, P2, or V1. Do not push. Do not add a remote. Do
not construct public `main`. Do not close the logical whole.

```text
STOP: Native Plan Mode off. This is implementation, not planning.
STOP: S4 only. No orphan commit (S5), no origin, no push.
STOP: Do not recreate lab/cli-chatgpt-190 or work/kronika-clean-start.
      Do not touch main.
STOP: Do not open, quote, copy, or display docs/environment.md. It is
      deletion-only, by exact path, without content inspection.
STOP: Do not display or copy the private host value in docs/human-steps.md.
      Author docs/usage.md from current code, CLI help, and contracts.
STOP: Do not read, copy, migrate, or delete ~/.local/state/chatgpt-cli,
      ~/.local/state/kronika, or any live token, profile, or database.
STOP: Do not change executable behavior. No src/, extension/, scripts/,
      tests/, contracts/, pyproject.toml, or .ap/ edits.
STOP: Do not touch the frozen manager-v3–v5 Markdown companions or the
      adapter v2–v4 schemas.
STOP: Do not add new prose-snapshot tests.
STOP: Do not spawn Workers or subagents.
```

## Implementation Authority Record

```text
Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 05
Worker exchange ordinal: 01
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: dc44cfd38093c118310ac032f5252ba29fad2f13
Changed-path allowlist: listed below
Implementation boundaries: public documentation and private-material removal
  only; one local commit on work/kronika-clean-start; no publication
Independence required: no
```

Predecessor evidence (not same-session authority): the S4 section and §2 content
contracts of `01_report_00.md`, plus the terminal reports `02_report_00.md`
(S1), `03_report_00.md` (S2), and `04_report_00.md` (S3) in the same Meta
directory. Read them as data; this prompt is the complete new S4 grant.

Meta storage:

```text
01_planning_00.md + 01_report_00.md       session 01 / exchange 01 (Planner)
02_implementation_00.md + 02_report_00.md session 02 / exchange 01 (S1)
03_implementation_00.md + 03_report_00.md session 03 / exchange 01 (S2)
04_implementation_00.md + 04_report_00.md session 04 / exchange 01 (S3)
05_implementation_00.md + 05_report_00.md session 05 / exchange 01 (this S4)
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
Downloadable prompt filename: 05_implementation_00.md
Destination path: /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start
Report filename: 05_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

State verified at this baseline: S3 landed as one local commit
`dc44cfd38093c118310ac032f5252ba29fad2f13` on `work/kronika-clean-start`
(parent `f25392472d043d753a3844c3a9a6321ae5cf09a5`, tree
`57943d9f6af0f5a9b2c16a57509ef24f52fe4c0e`, subject
`fix(headless): remove the parked engine integration`); `main` and
`lab/cli-chatgpt-190` both `2727451d2502925377637e19fa435917c970a996` (190
commits); no remotes; worktree clean; AP pin
`7478ddb07d2c3911f79e1aa1441f0115a31c45d8` in both the gitlink and `.ap` HEAD.

## Mandatory reading (verified task-relevant anchors)

- `.ap/AP_WORKER.md` (Worker operational spine) and the WORKER row of the
  `.ap/AP.md` minimum-reading spine.
- `.ap/AP.md`: [§5 Task Authority], [§9 Git and Remote Safety], [§10 Security
  Boundaries], [§12 Validation], [§13 Artifact Lifecycle], [§18 Stopping
  Conditions], [RF-12], [RF-14], [RF-18].
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header.
- `.ap/INFOSEC.md` §3 risk routing and §4.1 (R0 documentation route).
- `01_report_00.md` §2: README contract, SECURITY contract, CONTRIBUTING /
  usage / architecture ownership, path disposition matrix, exact project-rule
  wording. This is the accepted content contract for the documents you write.
- `AGENTS.md` declared execution route, which this grant binds as the canonical
  capability path. Equivalent ambient commands are not a second route.

## Outcome

A coherent, public-safe Kronika tree: an interview-grade README that leads with
the household library and the architecture, a one-page security boundary
document, contributor and operator guides, current technical documentation with
no experimental chronology, and no private material. This tree becomes the S5
public root after independent acceptance.

## File dispositions

Rewrite (follow the `01_report_00.md` §2 content contracts):

```text
README.md                  locked 8-part order; mermaid shipped/planned diagram
docs/architecture.md       concise current components, data flow, boundaries
docs/headless-engine.md    current Chromium executor only; no experiment log
```

Add:

```text
SECURITY.md                one page plus reporting instructions
CONTRIBUTING.md            setup, declared test route, fixture/skip policy
docs/usage.md              current operator procedures
```

Delete (exact paths):

```text
docs/security.md           meaning consolidated into SECURITY.md
docs/dev-setup.md          meaning consolidated into CONTRIBUTING.md
docs/ROADMAP.md            experimental ledger; lab history retains it
docs/human-steps.md        meaning replaced by docs/usage.md
docs/environment.md        deletion-only; never open or display
```

Update narrowly (current behavior and links only):

```text
docs/protocol.md
docs/adapter-pack.md
docs/contracts/automation-engine-v1.md
docs/contracts/bridge-modules-v1.md
docs/contracts/http-api-v1.md
docs/contracts/render-surface-v1.md
docs/contracts/manager-surface-v6.md
```

Check and refine only if needed:

```text
AGENTS.md     declared route must be `python -m kronika`; managed AP block
              byte-for-byte; no predecessor command names
.gitignore    remove the stale `obscura-profile/` line (engine removed in S3);
              keep the `/docs/environment.md` exclusion; add only what survives
LICENSE       unchanged; do not rewrite the copyright holder or relicense .ap
```

Frozen or out of scope: `docs/contracts/manager-surface-v3/v4/v5.md`, adapter
v2–v4 schemas, `contracts/**`, `.ap/`, `.gitmodules`, `src/`, `extension/`,
`scripts/`, `tests/`, `pyproject.toml`.

## Required content (accepted contract)

- README order: what Kronika is; what it is not; architecture (clearly label
  shipped local behavior versus planned family access); status; requirements
  and quick start; security invariants linked to SECURITY; unofficial /
  account / terms / no-warranty posture; MIT license and documentation links.
  Keep it readable in roughly ninety seconds before the setup details.
- README quick start covers: environment preparation, local `setup`, account
  bootstrap through `library ui`, executor selection, manual login, bridge and
  headless runner startup, project configuration, capture, and reopening the
  library. Longer procedures live in `docs/usage.md`.
- Requirements must state: CPython 3.11+, Bash, SQLite with FTS5; Node 22+ and
  a supported system Chromium for the headless route; desktop Brave/Chrome for
  the optional unpacked extension; an operator-managed ChatGPT login; no Python
  runtime dependencies; no Playwright requirement; no package-index install
  claim; no Android extension claim.
- Document the existing `"job_executor": "headless"` config setting with other
  keys preserved. Use only placeholders for project URLs and secrets. Explain
  that `setup` prints local capability values that must not be copied into
  reports or issues.
- Do not turn historical page or anti-automation observations into current
  reliability claims.
- SECURITY: loopback-only listeners, per-install token, strict Host/Origin, no
  wildcard CORS; bounded sanitization with no JavaScript or external resources
  on local pages; 0700/0600 state; no cookie/profile/history extraction;
  Kronika local accounts distinct from ChatGPT credentials; the narrow wizard
  exception; the two result-access boundaries (manager account scope versus the
  bridge render key as an installation capability, not family authorization);
  no external LLM API; no recovery-provider loop shipped; administrator and
  bearer-URL limitations; unofficial, unaffiliated, AS IS, no warranty; a
  vulnerability-reporting route that does not invent an email or promise.
- CONTRIBUTING: canonical setup, declared test route, Node/Chromium fixture
  requirements, skip reporting, synthetic-data policy, English contributions,
  commit-subject convention; no real credentials or household examples.
- docs/usage.md: setup, capture, project selection, library access, accounts,
  sharing, authoring, `library check`, and the existing explicit maintenance
  commands. Use the declared route for every command.
- docs/architecture.md: current component and data-flow explanation, security
  boundaries, protocol/storage ownership, preserved compatibility identifiers,
  the XDG state clean break, and the deferred family-access direction.
- docs/headless-engine.md: current Chromium executor, supported options,
  manual login, the wizard exception, resource and asset behavior, and bounded
  diagnostic probes. No Obscura, no slice chronology, no experiment ledger.

## Narrow updates (exact known items; sweep for the rest)

- Replace stale identity in the updated documents: `src/chatgpt_cli/` →
  `src/kronika/`; `chatgpt-cli <cmd>` and `python -m chatgpt_cli` → the
  declared route (`python -m kronika <cmd>` or `./scripts/kronika <cmd>`).
  Preserve internal compatibility identifiers (`chatgpt_cli_session`,
  `chatgpt-cli-bridge`, `chatgpt-cli-library-manager`, contract URNs,
  `globalThis.ChatGPTCLI`, `cw`, the dummy scrypt salt) exactly as they are.
- `docs/adapter-pack.md`: remove the three `docs/environment.md` references
  (~70, ~162, ~196) and keep the current locator, probe, and hot-swap content.
- `docs/contracts/bridge-modules-v1.md`: update the `src/chatgpt_cli/bridge/`
  path and remove the `files` module row and its contract (file upload is not
  available; `GET /v1/files/{fid}` answers 501 upload-unavailable).
- `docs/contracts/http-api-v1.md`: `src/chatgpt_cli/errors.py` →
  `src/kronika/errors.py`; `chatgpt-cli project set` → the declared route.
- `docs/contracts/render-surface-v1.md`: `chatgpt-cli setup` and the
  project-set hint → the declared route.
- `docs/contracts/manager-surface-v6.md`: `chatgpt-cli library ui` → the
  declared route.
- `docs/contracts/automation-engine-v1.md`: update stale paths/links; mark
  `uploadFiles` as unavailable rather than "S2".
- Sweep every updated document for slice codes (HE-, SL-, WC-, WSC-), archived
  task chronology, private-document references, and unsupported capability
  claims; remove or rewrite them as current product statements.

## Repository gate (before mutation)

Working directory: `/home/agile/Tools/cli_chatgpt`

Prove independently:

```text
pwd -P == /home/agile/Tools/cli_chatgpt
branch == work/kronika-clean-start
HEAD == dc44cfd38093c118310ac032f5252ba29fad2f13
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

Positive: inspect and edit only allowlisted paths; read the current code, CLI
help, and contracts to ground every claim; `git rm` for the five deletions;
link, command, and privacy checks; `python -m kronika --version` and
`python -m kronika --help`; one local commit as specified.

Negative: no `git add .` / `git add -A`; no push; no fetch; no remote add; no
force; no amend; no git config write; no submodule update; no AP edit; no
live-state access; no executable or test changes; no new dependencies; no
`.venv` edits; no full-suite run is required (the executable tree is unchanged
and S3 evidence stands), and do not add prose-snapshot tests.

Staging: stage the exact reviewed paths including both sides of deletions. The
accepted staging list is:

```bash
git add -- \
    .gitignore AGENTS.md README.md LICENSE SECURITY.md CONTRIBUTING.md \
    docs/architecture.md docs/usage.md docs/human-steps.md \
    docs/headless-engine.md docs/protocol.md docs/adapter-pack.md \
    docs/contracts/automation-engine-v1.md \
    docs/contracts/bridge-modules-v1.md \
    docs/contracts/http-api-v1.md \
    docs/contracts/render-surface-v1.md \
    docs/contracts/manager-surface-v6.md \
    docs/ROADMAP.md docs/security.md docs/dev-setup.md docs/environment.md
```

Do not display a content diff for `docs/environment.md` or for the
privacy-bearing predecessor documents. Inspect their removal through metadata
(`git diff --cached --name-status`) and review the newly authored documents
separately. Commit subject:

```text
docs(kronika): prepare the public documentation and clean tree
```

Then read back commit SHA, tree, `git status --porcelain`, and that `main` and
`lab/cli-chatgpt-190` are unchanged.

Secret authority: none.
Publication: prohibited.

## Validation

- README order and shipped-versus-planned architecture labels present.
- Every new public claim traceable to current code, CLI help, or contracts;
  cite the source in the report.
- Local links: every referenced repository path exists. No reference to
  `docs/environment.md` remains anywhere (`git grep -n environment.md`).
- CLI examples current: every command shown exists in
  `python -m kronika --help`; `python -m kronika --version` prints
  `kronika 0.1.0`.
- Privacy scan, filename-only output:

  ```bash
  git grep -I -l -E '/home/|/Users/|[A-Za-z]:\\Users\\|BEGIN [A-Z ]*PRIVATE KEY' \
      -- . ':(exclude).ap'
  ```

  Expect no real private path outside synthetic test fixtures; classify every
  match in the report without printing private values. `docs/human-steps.md`
  and `docs/environment.md` must be gone, so their matches disappear with them.
- No archived task chronology or slice codes promoted to product guidance in
  the rewritten documents.
- Managed AP block, `.gitmodules`, and the `.ap` gitlink unchanged.
- `LICENSE` byte-identical to the baseline.

## Stop conditions

Unidentified private data in a surviving document; a security claim that
cannot be made accurate without an ungranted behavior change; a link or command
that cannot be grounded; need to leave the allowlist; need to touch executable
code or tests; branch/HEAD mismatch; request to recreate branches; any need to
open `docs/environment.md`.

Recovery: the local commit is reversible; `lab/cli-chatgpt-190` retains every
removed document and its history; live XDG state is untouched.

## Report contract

Write the terminal report atomically to:

```text
/home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/05_report_00.md
```

only if that path is absent. The chat conclusion is a short 3-line notice with
status, path, and SHA-256. Do not commit Meta. Do not overwrite any earlier
report.

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates exactly once (session 05, exchange 01). Include the
start/end commit, changed paths including the five deletions, the link/command
check results, the privacy-scan classification, the claim-to-source map, proof
that `main` and the lab branch were not moved, and:

```text
Logical-whole closure: not-closed
```

`PASS` means S4 landed as one local commit on `work/kronika-clean-start` from
the exact baseline, the checks passed, and the report was saved. Then stop. S5
is a later grant.
