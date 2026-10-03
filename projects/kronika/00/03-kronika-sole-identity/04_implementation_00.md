# Authoritative Worker prompt — Worker session 04, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `04`, exchange `01`. Stored under the
Meta filename mapping as `04_implementation_00.md`, with report destination
`04_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C0 — ADR-0085, index update, five living-prohibition sentences, identity retention ledger
Reasoning recommendation: Medium
Recommended context capacity: approximately 250k tokens
```

Rationale: ordinary bounded documentation work plus one new contract test, with
every mutation enumerated by line and every value independently measured. That
is the `Medium` band. It is not `Low` because a hash ledger and a multi-part
contract test must be computed correctly rather than mechanically. Escalate only
by naming the concrete evidence you could not obtain at this profile.

This is cut **C0** of the accepted plan `03_report_00.md`. It is the first
implementation grant of this whole. No later cut's authority is implied.

## Accepted plan you are implementing

The Orchestrator accepted `03_report_00.md` on 2026-10-02 as decision-complete:
ADR-0085 plus the sequence C0 through C9, where only C6 changes the web host and
only C8 restarts capture. Read that file in full before editing. It is a frozen
artifact; do not edit it and do not treat it as authority beyond cut C0.

Four Orchestrator review findings against that plan are folded into this grant:

- Finding 2: the plan's question-12 frozen/living split excluded `deploy/`,
  `scripts/`, `src/`, `tests/` and `extension/`, so a path-name miss in exactly
  the trees where the rename is mechanical could not be caught. This grant
  therefore requires a **path-name ledger** that is active from C0 and is green
  now, so that later cuts shrink it by an exact enumerated set and any missed
  rename fails loudly at that cut instead of at the end.
- Finding 4: `deploy/ubuntu/fn-production-env-deploy` contains a `framenest`
  reference although its filename does not match, so filename enumeration alone
  is insufficient. This is why the grant also requires a **content occurrence
  ledger**.
- Finding 5: the plan's "living-prohibition edits" list names seven files, but
  exactly five sentences in four files forbid the rename. See the enumerated
  mutation below. Do not touch `README.md`, `PRODUCT.md` or `SERVER.md` in this
  cut.
- Finding 1 concerns C7 and does not apply here, but the ledgers created now are
  what will make C7's complete enumeration checkable.

## Goal

Record the sole-identity decision in ADR-0085, remove the five normative
sentences that currently forbid it, and install a live retention ledger that
makes every later rename mechanically verifiable — without renaming anything,
moving any package, changing any unit, script, header, environment prefix or host
path, or touching the NUC.

## Verified current state

```text
Repository checkout topology: standalone checkout
Expected branch: main
Expected HEAD: ca649f6eb6231591292e174dff994fd0f4448378
Expected subject: fix(test): isolate the operator gate Fish tests from personal configuration
Remote origin: https://github.com/cisarik/kronika
Public main: ca649f6eb6231591292e174dff994fd0f4448378
Working tree: clean
Containing-repository .ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS, governing variant stable
ap.project.conf projectId: cisarik/kronika
CPython: 3.13.9   Poetry: 2.3.2   Node: v26.8.2   fish: 4.9.3
Working directory: /home/agile/Projects/kronika
```

Baseline at this commit, measured by the Orchestrator through the canonical
route: Python `4145 passed, 8 skipped, 3 warnings, 0 failed`; JavaScript
`554 total, 549 passed, 0 failed, 5 skipped`. If your run does not reproduce
this, stop and report.

Host note: the development host is a CachyOS Linux workstation. The MacBook
paths in older artifacts are historical text. The stale clone at
`/home/agile/Projects/framenest` is not a work source and contains `private/`,
which you must never read.

## Enumerated mutation — exactly these, nothing else

### 1. Add `docs/adr/0085-kronika-sole-identity.md`

Number 0085, the next free number. Status `Accepted`. Decision date `2026-10-02`.
Accepted by the Cooperator on that date. It records the decision; it must not
claim the code has already moved.

It supersedes, **by citation and not by patch**, exactly three passages of
ADR-0082, which is not edited:

- `docs/adr/0082-kronika-one-product-and-private-records.md` lines 87-89: the
  internal `framenest` package, migration history, compatible HTTP headers and
  deployment identifiers remain during that stage, and there is no mass
  `framenest` rename.
- The same file, lines 208-209: the `framenest` package, provenance module,
  migration history, HTTP headers and deployment identifiers stay.
- The same file, line 196: "Local paths need not be renamed", superseded only
  for product commands, the settings prefix, the mutation header, systemd unit
  names and the host paths this ADR names. Explicitly **not** superseded for Git
  history, for the historical MacBook path in old artifacts, or for the tooling
  paths below.

The ADR must state:

- The product identity is Kronika. The import package is `kronika` at
  `src/kronika`. The distribution name is `kronika`. `provenanceModule` is
  `kronika`. Console scripts are `kronika-*` as mapped in the accepted plan's
  cut C3. The root launcher is `./kronika`.
- The settings prefix is `KRONIKA_`. The mutation header is
  `X-Kronika-Request: 1`. Command error-code strings use the `KRONIKA_` prefix
  after the removal cut.
- Web host layout: `/opt/kronika/releases`, `/opt/kronika/current`,
  `/etc/kronika/kronika.env`, `/var/lib/kronika`, `/var/cache/kronika`,
  `/run/kronika/kronika.sock`, Unix account `kronika`, units
  `kronika.service`, `kronika-catalog-backup.service` and `.timer`,
  `kronika-catalog-offdevice.service` and `.timer`.
- The sole release entry becomes `deploy/ubuntu/kronika-release`, the same
  engine and not a second deployment system.
- Applied Alembic bytes through `0035` stay byte-identical. The only mechanism
  that loads `from framenest.infrastructure.persistence.sqlite_batch_fk import
  ...` is a process-local `sys.modules` alias installed by the migration loader.
  There is no `src/framenest` package and no `framenest` distribution after C3.
- Named frozen residues, so they are not later mistaken for leftover rename work:
  the two accepted tooling paths
  `/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry` and
  `/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13`;
  protocol magic `FNCBE01`; the capture state-directory name
  `framenest-chatgpt-page`; the off-device mount path
  `/mnt/framenest-catalog-offdevice`; historical ADR bodies;
  `docs/FEDORA_SERVICE.md`; `docs/NUC_HOST_BASELINE.md`; and existing backup
  archives and sidecars, which readers keep accepting.
- The compatibility windows and their removal gates are the ordered cuts in the
  accepted plan. A mass search-and-replace is not an implementation of this ADR.
- This ADR grants no implementation, no deploy and no host migration.

It must also restate, as still accepted and unaffected, the boundaries this whole
inherits: one repository `cisarik/kronika`; no Git history rewrite; no force
push; `cisarik/cli_chatgpt` at `66c40d43c577276b0ad304a494fbbb1ffb6fc933`
stays active; the parked capture module and its constraints; Gallery as a
separate frozen view; the administrator-curated Timeline; owner-private records
with administrator read of product records; household publication only by
administrator approval; internet publication off; Search and Research through
the ADR-0083 and ADR-0084 provider boundary with research disabled by default;
loopback-first with Tailscale-only remote ingress; and the single release helper.

### 2. Update `docs/adr/README.md`

Add the ADR-0085 row in the existing style, and one supersession paragraph in the
same style as the existing ADR-0083 paragraph. The paragraph must state that
ADR-0082's historical reasoning stays in that file. Do not restructure the index
and do not renumber anything.

### 3. Replace exactly five prohibition sentences

Each was read verbatim at the verified baseline. Replace the sentence only, keep
the surrounding paragraph structure and line style, and do not touch historical
narrative of what S10 already did.

| File | Lines | Current sentence |
|---|---|---|
| `AGENTS.md` | 21-22 | `Do not perform a mass branding replacement.` |
| `AGENTS.md` | 24-25 | `The internal \`framenest\` package, migration history, compatible HTTP headers and deployment identifiers remain.` |
| `SPEC.md` | 32-34 | `The internal \`framenest\` package, migration history, compatible HTTP headers and deployment identifiers MUST remain during this stage.` |
| `DEVELOPMENT.md` | 39-40 | `The internal \`framenest\` application, headers and migration history remain.` |
| `ROADMAP.md` | 78-79 | `no mass \`framenest\` rename is part of the transition.` |

Replacement requirement: each becomes a pointer that ADR-0085 is the identity
authority and that the ordered cuts implement it. Preserve the other constraints
in the same sentence or paragraph, for example "The existing release helper
remains the only deployment system" and "Do not port a second manager, account
system, family library or Git history", and preserve the requirement that the
change is an ordered cut sequence rather than a mass replacement.

**`AGENTS.md` lines 33-51 are the AP-managed integration block. You must not
edit any line inside it.** `README.md`, `PRODUCT.md` and `SERVER.md` must not be
edited in this cut; they contain no present-tense rename prohibition, and their
descriptive prose belongs to later cuts.

### 4. Add `tests/contract/test_kronika_identity_retention.py`

Three live parts. No part may be skipped, xfailed or disabled.

**Part A — frozen-blob hashes.** Pin SHA-256 values for the bytes of: every file
in `docs/adr/` whose name matches `^\d{4}-` with a number at or below `0084`,
excluding `docs/adr/README.md`; `docs/FEDORA_SERVICE.md`;
`docs/NUC_HOST_BASELINE.md`; and the contents of all 36 files under
`src/framenest/infrastructure/persistence/alembic_environment/versions/`. The
test asserts each pinned blob is byte-identical. These are the applied or
historical bytes that no cut may ever edit; a path move in a later cut is allowed
to change a path, never these bytes.

**Part B — path-name ledger.** Pin the exact set of tracked paths whose basename
contains `framenest`, case-insensitively, and assert the set matches exactly.
Compute it fresh at this baseline, and cross-check it against the
Orchestrator-measured list below; stop and report on any mismatch rather than
adjusting the pinned value silently. The Orchestrator-measured set, 23 paths:

```text
deploy/systemd/framenest-ai-credential-nvidia-nim.conf
deploy/systemd/framenest-ai-credential-opencode-go.conf
deploy/systemd/framenest-ai-credential-vercel-ai-gateway.conf
deploy/systemd/framenest-catalog-backup.service
deploy/systemd/framenest-catalog-backup.timer
deploy/systemd/framenest-catalog-offdevice.service
deploy/systemd/framenest-catalog-offdevice.timer
deploy/systemd/framenest.env.example
deploy/systemd/framenest-research-credential.conf
deploy/systemd/framenest.service
deploy/ubuntu/framenest-catalog-export-v1
deploy/ubuntu/framenest-release
deploy/ubuntu/framenest_release.py
framenest
scripts/operator/infosec/framenest_log_triage.sh
scripts/operator/infosec/framenest_public_surface_check.sh
scripts/operator/infosec/framenest_socket_permissions_check.sh
scripts/operator/network/framenest_mullvad_egress.fish
scripts/operator/network/framenest_mullvad_egress.sh
scripts/operator/network/framenest_nuc_worker_gate.fish
```

That is 20. Ten more paths live under `src/framenest/`, which is one renamed
directory and not a set of individual filenames; enumerate the full set yourself
from `git ls-files` and confirm it against this list plus the `src/framenest/`
tree. The test must derive the expected set from a pinned literal in the test
file, not by recomputing it from the working tree, or it would tautologically
pass. Each later cut shrinks this pinned set by an exact enumerated difference.

**Part C — content occurrence ledger.** Pin per-tree occurrence counts so that a
missed content rename is detectable even where the filename is clean, which is
the `deploy/ubuntu/fn-production-env-deploy` case from finding 4. Cross-check
against the Orchestrator-measured values and stop on mismatch:

| Measure | Value |
|---|---:|
| `FRAMENEST_[A-Z0-9_]+` token occurrences | 637 |
| distinct `FRAMENEST_[A-Z0-9_]+` names | 102 |
| bare `FRAMENEST_` spellings with no trailing name | 2 |
| `X-FrameNest-Request` occurrences / files | 53 / 28 |
| `/opt/framenest` / `/etc/framenest` | 198 / 73 |
| `/var/lib/framenest` / `/var/cache/framenest` | 91 / 20 |
| `/mnt/framenest-catalog-offdevice` | 12 |
| `User=framenest` / `Group=framenest` | 5 / 5 |
| capitalized `FrameNest` occurrences / files | 3335 / 478 |
| tracked files matching case-insensitive `framenest`: src / tests / deploy / scripts / docs / extension | 254 / 314 / 19 / 7 / 87 / 12 |
| `framenest-*` console script entries in `pyproject.toml` | 14 |

The two bare `FRAMENEST_` spellings are `env_prefix="FRAMENEST_"` in
`src/framenest/configuration.py` and a prose prefix in `docs/adr/0020*`. This cut
adds no `framenest` token of its own beyond what ADR-0085 legitimately needs; if
your recount differs from the table after your own edits, adjust the table only
for the delta your ADR text causes, and state that delta explicitly in the
report. ADR-0085 will legitimately contain `framenest` as cited historical text.

Do **not** implement the question-12 living-prose `\bframenest\b` scan at this
cut. It is armed in cut C7. Record that intent in the test module docstring only;
do not add a disabled or skipped test.

## Authority

```text
Positive authority: create exactly
  docs/adr/0085-kronika-sole-identity.md,
  tests/contract/test_kronika_identity_retention.py;
  edit exactly docs/adr/README.md, AGENTS.md, SPEC.md, DEVELOPMENT.md and
  ROADMAP.md, and only the five sentences enumerated above;
  create one local branch named docs/adr-0085-kronika-sole-identity from main;
  stage and commit exactly those seven paths; run the declared AP test
  operations and the declared JavaScript test route; run read-only Git
  inspection.

Negative authority: any other file creation, edit, move, rename or deletion in
  /home/agile/Projects/kronika, including all of src/, tests/ other than the one
  new file, deploy/, scripts/, extension/, pyproject.toml, ap.project.conf,
  .gitmodules and .gitignore; any edit to AGENTS.md lines 33-51; any edit to
  docs/adr/0082*, docs/adr/0083*, docs/adr/0084*, README.md, PRODUCT.md,
  SERVER.md, SECURITY.md or docs/FEDORA_SERVICE.md; any package move, import
  rewrite, packaging, console script, header, environment prefix, unit file,
  release helper or host path change; any dependency install, update or lockfile
  change; any Git push, tag, merge, rebase, remote branch creation or history
  rewrite; any NUC contact, including SSH, the NUC worker gate and
  deploy/ubuntu/framenest-release in every mode; any deploy/systemd,
  package-manager, systemd, AppArmor, UFW, Tailscale, mount or storage
  operation; any provider or capture-browser contact; any reading of private/,
  personal Fish configuration, browser profiles, cookies, tokens, credential
  stores, .secrets, or ~/.config/opencode; any write to /home/agile/meta.

Commands: Python evidence and tests go only through the canonical declared
  route, `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  ca649f6eb6231591292e174dff994fd0f4448378 --operation <id> -- <argv>`, with
  operations declared in ap.project.conf, plus `./.ap/ap project check --root
  /home/agile/Projects/kronika --baseline
  ca649f6eb6231591292e174dff994fd0f4448378`. JavaScript tests use the declared
  `node --test` route. Never invoke `.venv/bin/python`, `python`, `python3` or
  `poetry run` for evidence. Read-only Git inspection is allowed (`git status`,
  `git rev-parse`, `git log`, `git show`, `git ls-files`, `git grep`,
  `git ls-remote`, `git submodule status`, `git merge-base`); no other Git
  command. If a specific step needs a command outside the declared routes, state
  it in the report with its purpose and confirm it mutated nothing.

Dependency authority: none. The canonical `.venv` is correct; do not reinstall,
  update or relock anything.

Git authority: create the named local branch, stage only the seven enumerated
  paths, make exactly one local commit. No push, no publication, no tag, no
  merge.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none. Never print, quote or summarize secret values, host
  identifiers, addresses, disk serials, UUIDs or SSH fingerprints.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` is authoritative inside its scope; the accepted plan
  `03_report_00.md` and this prompt are task context, not higher authority. On
  conflict between retained context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only. No destructive
  mutation, no remote effect, no deployment, no credential effect, no billing
  effect.

Browser authority: none.
```

## Verification

Before editing, confirm branch `main`, HEAD `ca649f6eb6231591292e174dff994fd0f4448378`,
clean tree, public `main` equal to that SHA, submodule at the pin, `ap doctor`
PASS and `ap project check --baseline` PASS. Stop without editing if any fails.

Then:

1. Reproduce the baseline once with the declared `test` operation and
   `node --test tests/*.test.js`. Expect `4145 passed, 8 skipped, 3 warnings` and
   `549 passed, 0 failed, 5 skipped`. The suite takes about eleven minutes; let
   it finish once and do not rerun it.
2. Enumerate the Part B path set and the Part C counts fresh from the working
   tree and cross-check against the tables. Stop on mismatch.
3. Make exactly the four enumerated mutations.
4. Run the new test file through the canonical route. Expect it to pass, with no
   skip and no xfail.
5. Run the full declared `test` operation once more. Expect zero failures and no
   new skips beyond the baseline's 8. Report exact counts. The delta from step 1
   must be exactly the new tests added and nothing else.
6. Run `node --test tests/*.test.js`. Expect the baseline result unchanged.
7. Verify `git status --porcelain` lists only the seven enumerated paths before
   you commit, and is empty after.
8. After the commit, run `./.ap/ap project check --root
   /home/agile/Projects/kronika --baseline <new commit SHA>` and confirm PASS.

```text
Evidence tier: E2. Multiple layers, user-visible normative documentation, and a
  new contract test that becomes the enforcement mechanism for later cuts.
  Reversible by reverting one commit before publication.
```

## Git

One local commit on `docs/adr-0085-kronika-sole-identity`, parent
`ca649f6eb6231591292e174dff994fd0f4448378`. Suggested subject:

```text
docs: record the Kronika sole identity in ADR-0085
```

Seven paths: `docs/adr/0085-kronika-sole-identity.md`,
`tests/contract/test_kronika_identity_retention.py`, `docs/adr/README.md`,
`AGENTS.md`, `SPEC.md`, `DEVELOPMENT.md`, `ROADMAP.md`. Do not push.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the baseline does not reproduce; if the measured Part B or Part C
  values differ from the Orchestrator tables in a way your edits do not explain;
  if the full suite shows a failure you cannot attribute and cannot explain with
  evidence; if any step would require an edit outside the seven enumerated
  paths; if ADR-0082 or the AGENTS.md managed block would have to change; if
  context pressure reaches the point where a bounded rotation is cheaper than a
  degraded commit.

Completion: exactly one commit on the named branch containing exactly the seven
  enumerated paths, the new retention test green with no skip, the full Python
  suite green with no new skip, the JavaScript route unchanged, and the tree
  clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `04_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this
  prompt expires. No further implementation, no push, no publication and no
  further cut is authorized by it. Cuts C1 through C9 each require their own
  separate bounded grant.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
Published NUC state: unchanged; the NUC still serves whatever release it already
  runs
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing logical-whole identity `kronika-sole-identity`, Worker session ordinal
`04` and Worker exchange ordinal `01` unchanged. Then: the full diff of all seven
paths; confirmation that `git diff` for ADR-0082, ADR-0083, ADR-0084,
README.md, PRODUCT.md, SERVER.md, SECURITY.md and `docs/FEDORA_SERVICE.md` is
empty; confirmation that AGENTS.md lines 33-51 are unchanged; the ADR-0085 text
in full or a complete statement of where it is; your measured Part B path set and
Part C table with any delta from the Orchestrator tables and its cause; the new
test's structure and how each part fails on a deliberate mutation; baseline and
final exact test counts for both routes; the branch name and commit SHA;
deviations, risks and missing evidence; and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification.

Finish every terminal report with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

If your client's native surface forces any preamble above the report header,
disclose it on the first line of the report body, as Worker session 03 did.

## Mandatory reading

Read only what this cut requires:

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/03_report_00.md`,
  the accepted plan, in full. It is the specification for C0.
- `docs/adr/README.md` in full, for index style and the existing supersession
  paragraph pattern.
- `docs/adr/0082-kronika-one-product-and-private-records.md` lines 80-95,
  190-215, to cite supersession precisely without editing the file.
- `docs/adr/0083-modular-research-providers-and-administrator-curated-timeline.md`
  and `docs/adr/0084-administrator-managed-research-settings-and-versioned-pricing.md`,
  for ADR structure, status wording and the supersession-section convention.
- The five prohibition sentences in their surrounding paragraph context.
- `docs/WORKER_EXECUTION_CONTRACT.md` sections on the canonical Python route and
  on failure classification.
- `AGENTS.md` Worker Execution section and its managed AP integration block
  boundaries.
- `.ap/AP_WORKER.md`, and `.ap/AP.md` §5, §9, §10 and §13.
- Existing `tests/contract/*.py` for the contract-test conventions this
  repository already uses, including `test_fedora_systemd_service.py` for how it
  pins repository paths.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, or
any credential store.

## Communication

Report text, the ADR, and code comments are professional English. Do not use
Czech or Slovak in repository or report artifacts.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the diff, the ledgers and the counts.
Publication of this branch is a separate bounded grant and does not follow from
acceptance. Cut C1 requires its own grant and its own authority; nothing in this
prompt carries forward.