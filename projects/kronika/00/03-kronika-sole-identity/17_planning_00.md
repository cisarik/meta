# Authoritative Worker prompt — Worker session 17, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `17`, exchange `01`. Stored under the
Meta filename mapping as `17_planning_00.md`, with report destination
`17_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 17
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: used
Worker session profile: Planning Worker, read-only
Task identity: KSI-PLAN-CLOSE — plan the completion of the logical whole from C3 to C9
Reasoning recommendation: High
Recommended context capacity: approximately 400k tokens
```

Rationale: `High`, the highest band issued in this whole. You are not renaming
strings. You are reconciling an accepted ten-cut plan against five cuts of
accumulated evidence, three of which found real defects in how the Orchestrator
derives its work, and producing a completion plan that a later sequence of
implementation Workers can execute without re-deriving anything. Most of the value
you add will be in what you find that the plan and the Orchestrator both got
wrong.

## Mandate

Produce **one completion plan for `kronika-sole-identity`, from the current state
through to closing the logical whole**, covering the accepted cuts `C3` through
`C9`, plus the items that exist in reality but in no accepted cut.

The plan must be executable by fresh Implementation Workers who have none of this
context. For every cut, state the exact mutation, the exact authority a Worker
would need, the evidence that closes it, its rollback, its preconditions, and the
machine-checkable proof that the cut did what it claimed.

**You have no authority to change anything.** You produce a plan, not a mutation.

Three things are wanted beyond sequencing, and they matter more than the
sequencing:

1. **Correct the record.** Several statements in the accepted plan and several
   statements the Orchestrator made to the Cooperator are now known to be wrong.
   They are listed below. Say plainly which of your findings invalidate which.
2. **Close the open items.** A list of unresolved defects and unanswered questions
   is listed below. Each needs either a decision inside your plan, or an explicit
   statement that it cannot be decided at planning time and why.
3. **State the closure conditions.** What must be true for this logical whole to
   be closed, and what evidence proves each one.

## Verified current state

Measured by the Orchestrator at `d5955d5`, not carried forward:

```text
Repository checkout:            /home/agile/Projects/kronika
Branch:                         main
Local HEAD:                     d5955d5c0478ef7fa025fa9f8cba26ef56656883
Local main is AHEAD of public main by 3 commits. Nothing from C2b, C2c or C2d is pushed.
Public main:                    9c71bfb0a06cb30c5d747816e9067f6a25350c58
Remote origin:                  https://github.com/cisarik/kronika.git
Containing-repository .ap gitlink and submodule HEAD:
                                73e20ef80b88700d5fc397cd8edd4fc425869f
ap doctor:                      PASS, governing variant stable
Node:                           v26.8.2
```

Suite baselines at `d5955d5`, each reproduced by the Orchestrator or by the Worker
of that cut:

```text
Python declared test:  4359 passed, 8 skipped, 3 warnings, 0 failed
JavaScript:            583 total, 578 passed, 0 failed, 5 skipped
Retention module:      15 passed
ap project check:      PASS at every commit in this whole
```

NUC state, from a Cooperator-run `framenest-release status` on 2026-10-02 plus
one read-only `framenest-catalog device list`:

```text
Web release served:           9c71bfb0a06cb30c5d747816e9067f6a25350c58
Web service:                  framenest.service, active
Database revision:            0035, equal to head
Catalog backup:               ready
Capture release:              94e605c17b881461fad3e22fd8c7fca32cb93976
Installed web env file:       /etc/framenest/framenest.env, 24 FRAMENEST_ lines, 0 KRONIKA_
Devices in catalog:           1
Capture fingerprint (compare after every web deploy):
  capture_code_tree            e65422fa576fa5b9947e7408e6980e56707c72c4
  capture_runtime_contract     691500d51dc9a2f3966de144c3592b0b984e8b2753cca4d599aee3793ee35e6b
  capture_unit_contract        5799ec63d85bf54ee749b56579f3281fb66477f3e8b17f78b62620b18ffe8c40
  capture_bridge_protocol      1
```

The Orchestrator's own session cannot reach the NUC: the sanctioned gate probe
returns `ssh-agent: ready` with exit 0, but SSH to the host times out, because
that session is the untrusted Cursor/AppImage ambient environment and is not on
the tailnet. **Every NUC observation is therefore a Cooperator terminal action.**
Plan for that. Do not plan on observing the host yourself.

## The accepted plan is the authority for what was decided

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/03_report_00.md` is
the accepted plan. Read it in full. It defines `C0` through `C9`, the standing
rules, the fourteen answered questions, and the per-cut mutation, evidence and
rollback.

`docs/adr/0085-kronika-sole-identity.md` is the accepted identity authority. Read
it in full, especially **"Named frozen residues"**.

Completed and accepted, do not re-plan: `C0` ADR, `C1` dual-read, `C1b` exit 2,
`C1c` parity, `C1d` precedence, `C1e` content-path ledger, `C2` companion dual
headers and storage, `C2a` web protocol dual-accept, `C2b` visible names,
`C2c` visible companion prose and download stem, `C2d` product prose and operator
output.

Remaining per the accepted plan: `C3` package, distribution and command rename
with aliases. `C4` one release entry, old layout still routine. `C5` durable
writers switch. `C6` NUC web migration. `C7` remove aliases, fallbacks and old
entry points. `C8` capture paths with explicit restart. `C9` delete retired copies.

The plan's standing rules that survive everything below:

```text
One repository, cisarik/kronika. No history rewrite, no force push, no second product.
cisarik/cli_chatgpt at 66c40d43c577276b0ad304a494fbbb1ffb6fc933 stays active.
kronika-capture and the kronika-capture-* units are not renamed.
Alembic revision bytes through 0035 are never edited. Head stays 0035 in every cut.
  No cut adds a migration, so every routine deploy stays inside the same-schema rule.
Writers of durable on-disk identifiers keep the old spelling until the matching
  readers are already the installed NUC release.
Routine deploy/rollback never installs unit files, never renames Unix accounts,
  never moves /opt, /etc, /var or the socket, and never restarts capture.
Tooling paths stay exactly:
  /opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry
  /opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13
/mnt/framenest-catalog-offdevice is not renamed and not created.
Implementation grants checkout only /home/agile/Projects/kronika. The stale clone
  /home/agile/Projects/framenest is not a work source.
Evidence tiers: C3, C4 and C7 are E2; C5 is E3; C6, C8 and C9 are E4.
```

## Corrections: things known to be wrong

Each of these was verified by the Orchestrator. Where they conflict with the
accepted plan, **say so and give the corrected form**.

**Correction 1 — the sequence is C0 through C9, not C0 through C7.** The
Orchestrator told the Cooperator repeatedly that the whole ends at `C7`. That is
wrong. `C8` (capture paths with an explicit restart grant) and `C9` (delete
retired copies, one-way) exist in the accepted plan and are **not optional tails**.
A completion plan that stops at C7 does not close the logical whole.

**Correction 2 — `script.py.mako` belongs to C3, not C4.** In the C2d grant the
Orchestrator excluded it and assigned it to C4. The accepted plan assigns it to
C3: *"`script.py.mako` is updated so future revisions import `kronika`; it is not
used to regenerate applied files."* Plan accordingly. The Orchestrator verified
that `script.py.mako` is **not** in `FROZEN_ALEMBIC_SHA256`, so updating it does
not move a frozen pin and there is no conflict.

**Correction 3 — the frozen Alembic set is 36 keys, not 36 version files and not
38.** Measured: `FROZEN_ALEMBIC_SHA256` holds exactly 36 keys, being the 35
numbered revisions `0001` through `0035` plus `__init__.py`. A Worker of session
16 reported "38 entries" in its verification table, which was wrong. Note that
`versions/__init__.py` carries the docstring `Immutable FrameNest Alembic
revisions.`; its **bytes stay frozen while its path moves** in C3, which makes it
a frozen residue inside a relocated file. Plan for that explicitly, because a
naive content sweep will try to rename it.

**Correction 4 — the NUC state in the plan is stale.** The plan's NUC paragraphs
assume web release `0c850996…`. The observed web release is `9c71bfb…`, which is
ahead of the plan's baseline. This affects nothing about C5's precondition, which
requires C1 to be installed or an ancestor — `9c71bfb` contains C1 — but every NUC
state line in the plan must be re-baselined in your plan.

**Correction 5 — the Fish universal block is mislabelled.** Question 14's
Cooperator-visible block is headed `# [MacBook / fish]`. The Cooperator's
environment is **not a MacBook**. It is a **CachyOS Linux PC**, working directory
`/home/agile/Projects/kronika`, shell fish 4.9.3. Any block C4 issues must be
headed `# [PC CachyOS / fish]`. The repository communication rule requires the
environment label to be truthful, and `AGENTS.md` names `bash` for an already-open
NUC session and fish for the Cooperator's own machine.

## Deficiencies in C0 through C2d that you must plan around

These are not hypothetical. Each was found by measurement.

**D-1. Nineteen of C2d's forty-nine product changes have no behavioural test
coverage.** Five argparse help and description strings, ten `development.py`
runtime messages, and all four occurrences of the category-conflict sentence
revert to green. The only automated signal is the retention ledger's whole-tree
occurrence **count**, which fires when *something* moved and never on *what* it
moved to, so it cannot distinguish a correct rename from a wrong one; one of four
occurrences trips it exactly as readily as four of four. Session 16 recommended a
per-site agreement guard deriving the expected brand from the single identity. No
such guard exists on the Python side. Decide whether that guard is its own cut,
folds into C3, or is deferred, and if deferred, say what carries the risk.

**D-2. The device display name on the NUC is a data value no cut owns.** The
catalog holds exactly one device whose `display_name` is `"FrameNest NUC"`. It was
supplied by the operator at registration through `framenest-catalog device register
--display-name`, so `SERVER_DEVICE_DISPLAY_NAME` at
`application/library_workflow.py:21` was **never used on that host**. C2d changed
that constant to `"Kronika Server"` for future registrations only; it does not
repair the existing row. The product exposes `device register|get|list` and **no
`rename`, `update` or `delete`**. `catalog_schema.py:75` declares
`ForeignKey("devices.id", ondelete="RESTRICT")` with a unique constraint on
`(device_id, path_flavor, root_root)`, so delete-and-re-register is blocked while
any library exists and would mint a new `device_id` orphaning library links. A
single-column `UPDATE devices SET display_name` is the only path preserving
`device_id`, and therefore every library foreign key.

**D-3. That operation bypasses two application invariants.** `engine.py` sets
`PRAGMA foreign_keys=ON` and a `busy_timeout` on every connect and then calls
`verify_private_catalog(normalized_path)`, which re-validates the directory, the
database file and the SQLite auxiliary files. The standalone `sqlite3` binary
defaults `foreign_keys` to **OFF** and runs no such verification. Plan the
operation: its exact mechanism, whether the service is stopped or the write is
made live, the backup taken first, the verification that reads the value back
without printing private media paths, and whether the read-only
`framenest-catalog device list` surface is sufficient for that verification.

**D-4. One unanswered catalog question.** Whether any `libraries.display_name`
also carries the retired brand is **unknown**. `library list` output contains
private media root paths and must never be pasted into a report or a trace; only a
yes-or-no answer may be recorded. If a library row also carries the brand, the data
operation in D-2 widens to two tables. Decide how this observation is obtained and
how it is bounded.

**D-5. Two default path components are assigned to no cut.** The accepted plan
assigns `DEVELOPMENT_DATABASE_DIRECTORY` to C3-then-C7, but the macOS and XDG
**path components** that embed the brand in
`infrastructure/runtime/development.py:720,726,741,747,758,763` — including
`~/Library/Application Support/FrameNest/development/catalog.sqlite3`,
`~/Library/Logs/FrameNest/development/server.log` and the XDG equivalents — are in
no cut. Each returns exactly one path and never reads the old one, so renaming
orphans an existing development database rather than migrating it.
`infrastructure/ai/configuration.py:173` is the same class,
`~/Library/Application Support/FrameNest/ai/config.json`, and is likewise assigned
nowhere. Assign both, or state why they are out of the whole.

**D-6. A stale test fixture.** `tests/contract/test_development_cli.py:175` holds
`message="FrameNest is running."` inside a fake `RuntimeStatus`. It is fixture
data, not an assertion, so C2d deliberately left it. It is now unrepresentative of
the real message and will diverge further at C3 and C4. Decide which cut repairs it
and whether any other fake still asserts the old spelling.

**D-7. The same string is both deletable and frozen.**
`framenest-chatgpt-page` is simultaneously a `[project.scripts]` entry that C7 must
delete and a capture state-directory name that ADR-0085 freezes and that must
**never move**. A grep-driven C7 sweep cannot distinguish the two uses of one
identical token. This is the sharpest remaining trap in the whole and needs an
explicit, testable rule rather than reviewer care.

**D-8. The Orchestrator's derivation method failed three times and so did the
Worker's.** Session 14 found the Orchestrator's C2b rename list incomplete. Session
15 found it incomplete again, by four to one, including a 197-character whole-sentence
constant no short search could find, and found two of the four named pins were
whole-file regexes over a literal occurring twice. Session 16 found the C2d site
list short by seven occurrences across three files **and one line attributed to the
wrong string**, plus one omitted pin and one pin that was not a pin, and received
an instruction to demonstrate a red test that could not exist. In the same session
the Worker committed three transcription errors in its own verification tables: a
nonexistent token written with another token's count, a header count of 71 against
a measured 74, and a frozen-set size of 38 against a measured 36. Every one was an
**absolute count in a verification table**, never a delta, so no conclusion was
wrong — but the pattern is the finding: **both parties transcribed tables from
recall instead of regenerating them.**

## The discipline rules this whole paid for

State these in your plan as binding method for every remaining cut. They are
empirical, not stylistic.

```text
1. Derive site lists by PARSING each artefact, never from a prose enumeration and
   never from an earlier turn's list.
2. Resolve every listed line to its literal text BEFORE classifying it. A single
   read would have caught the youtube.py:187 mis-attribution.
3. A literal in a test fixture is NOT a pin. Require assertion context.
4. Re-pin PER OCCURRENCE, never per file and never per function.
5. Reject any display pin that is a whole-file or whole-function regex where the
   literal occurs more than once.
6. Never truncate an inventory. If output is truncated, disclose it. A silent
   head -N hid roughly a dozen real sites in C2d.
7. Verify every mechanical probe against a known-impossible number. A sha256sum
   comparison that reported 36 of 36 Alembic revisions changed would have been a
   formatting artifact, caught only because 36/36 is implausible.
8. Regenerate every verification table at report time. Never transcribe one.
9. A grep hit is not a finding. Open the line and establish presence versus absence
   before classifying. A large share of brand hits are negative assertions.
10. Where a demonstration is impossible, say so. Do not perform a fake one.
```

## Machine-readable inventories to start from

Do not enumerate these from prose. Read them from the machine, and prefer these
over any list in a report or in a prompt:

```text
tests/contract/test_kronika_identity_retention.py
  FROZEN_DOCUMENT_SHA256               86 keys: ADR bodies 0001-0084 plus
                                       docs/FEDORA_SERVICE.md and
                                       docs/NUC_HOST_BASELINE.md
  FROZEN_ALEMBIC_SHA256                36 keys: revisions 0001-0035 plus
                                       versions/__init__.py
  EXPECTED_FRAMENEST_BASENAME_PATHS    20 paths whose basename carries the brand:
                                       three framenest-ai-credential-*.conf,
                                       framenest-catalog-backup.service/.timer,
                                       framenest-catalog-offdevice.service/.timer,
                                       framenest.env.example,
                                       framenest-research-credential.conf,
                                       framenest.service,
                                       framenest-catalog-export-v1,
                                       framenest-release, framenest_release.py,
                                       the root framenest launcher,
                                       three scripts/operator/infosec/*.sh,
                                       framenest_mullvad_egress.fish and .sh,
                                       framenest_nuc_worker_gate.fish
  EXPECTED_FRAMENEST_CONTENT_PATHS     membership of content-carrying paths, so a
                                       partial rename fails
  PER_TREE_FRAMENEST_OCCURRENCE_COUNT  per-tree occurrence counts; a WEAK pin, it
                                       detects that something moved and never what
```

**This resolves an earlier Orchestrator finding.** Three cuts ago the Orchestrator
recorded that C7 omitted five categories of file — credential confs, the env
example, off-device units, the catalog export and five operator scripts. They are
**already enumerated by name in Part B**. C4 and C7 must read them from the ledger
rather than reconstruct them from prose.

Standalone-word derivation, which is the correct search for prose occurrences:

```text
rg -n -P '(?<![A-Za-z_])FrameNest(?![A-Za-z])' src
```

At `d5955d5` this yields **47** in `src/framenest`, all out of scope: 33 module,
class and function docstrings, 1 comment, 7 default path expressions, 3 frozen
revision lines, `script.py.mako`, the deliberately dual-spelled message at
`tailscale_ingress.py:869`, and the mutation header at `web/app.js:437`.

## Per-cut trap register

Carry these into the plan; each is a specific way the named cut can fail.

**C3.** Move `src/framenest` to `src/kronika` with rename detection; `pyproject.toml`
name and Poetry packages; `ap.project.conf` `provenanceModule`; thirteen canonical
`kronika-*` scripts with `framenest-*` aliases; the `./kronika` launcher with
`./framenest` as a wrapper; class and settings renames such as
`FrameNestSettings` to `KronikaSettings`, which alone has 505 references. The
Alembic directory moves while revision bytes do not. **Eleven applied revisions
import `framenest.infrastructure.persistence.sqlite_batch_fk`**, so the in-memory
`sys.modules` alias is mandatory and must be installed before
`ScriptDirectory.from_config` and idempotently at the start of Alembic `env.py`,
binding only `sqlite_batch_fk` and its parent names. No other `framenest.*` import
may resolve, and a future revision importing any other `framenest` name must fail
the fresh-database test, which is the intended alarm. The C3 re-gate is ordered and
mandatory: edit, `--candidate` must print `PASS (non-authorizing)`, one commit
without amend, then `--baseline <new SHA>` for both `project check` and `ap exec`,
then both suites. **The pre-C3 SHA is never a valid baseline for that worktree,
because worktree and baseline drift of `ap.project.conf` forbids execution.**
`script.py.mako` is updated in this cut. Backups still write
`application.name = "framenest"` until C5. `version("framenest")` becomes
`version("kronika")`.

**C4.** The engine moves to `deploy/ubuntu/kronika_release.py` with a Fish entry
`deploy/ubuntu/kronika-release`, and `framenest-release` becomes a wrapper, so no
commit lacks both. Routine constants deliberately stay on the old layout. A new
`migrate-identity` subcommand is added and **its running is forbidden by C4's
grant**. The `ExecStart` guard is the thing that makes a premature C7 deploy
refuse: before any symlink switch, every basename in the installed web unit's
`ExecStart` and `ExecStartPre` must exist as a non-symlink file in the target
release's `.venv/bin`, or it exits without switching and without restarting. The
gate rename to `kronika_nuc_worker_gate.fish` reads `KRONIKA_NUC_SSH_*` and falls
back to `FRAMENEST_NUC_SSH_*`, exit 2 on conflict naming suffixes only. The
hermetic Fish test must be `fish --no-config` with a synthetic environment and must
not read `~/.config/fish/**` or `fish_variables`. A unit test asserts
`migrate-identity` is not invoked by `deploy`, `rollback`, `activate-capture` or
`rollback-capture`. Remember Correction 5 for the Cooperator-visible block.

**C5.** Preconditions: C1 is installed or an ancestor, which is satisfied, and the
writer change is **not** published in the same release as the first dual-read. The
checkpoint backup is written by the target code before cutover and must still
verify on the rollback release, which is safe only because C4's readers come from
C1. New artifacts use Kronika spellings; existing files are not rewritten; readers
still accept the old spelling; `FNCBE01` stays; the off-device root string stays
`/mnt/framenest-catalog-offdevice`. Rollback past C1 is **not** safe for C5
artifacts. This is the cut where the writer invariant in the standing rules is
actually spent.

**C6.** The highest-risk cut and the one most likely to leave the web service not
serving, because the account rename, the unit swap and the Tailscale Serve
retarget must land in one window. Writers stop first; the plan aborts if any
process still runs as `framenest`. **Capture processes run as `kronika-capture` and
must still be running, and the capture release SHA must be unchanged** — the
Orchestrator measured that all five capture units already use
`User=kronika-capture` with `/etc/kronika-capture/capture.env`, while all web units
use `User=framenest` with `/etc/framenest/framenest.env`. So capture identity is
already asymmetric with application identity and C6 is **not** a uniform rename.
`groupmod` then `usermod` so UID and GID stay; abort rather than create a second
account. Directories are **copied, not moved**, so rollback has its bytes. The env
copy is checked by name count only and never printed. Tailscale is an edit of the
existing handler to the new socket, never `serve reset` when another handler
exists, and a failed Tailscale edit with a healthy service is **rollback, not
success**. C9 must not start inside the C6 window.

**C7.** Removal is allowed only when all four preconditions hold: C6 done and
`kronika.service` active; the name-only env check shows zero `^FRAMENEST_` lines;
the Orchestrator has recorded the Cooperator's confirmations for the Fish
universals and for the Brave companion reload; the C4 `ExecStart` guard is in the
helper being run. It deletes the thirteen aliases, the `./framenest` wrapper and
`framenest-chatgpt-page` from `[project.scripts]`; removes the env fallback, the old
header spelling, the old gate-variable fallback, the release wrapper and the gate
wrapper; switches emitted CLI error codes from `FRAMEST_*` to `KRONIKA_*` while
numeric exit statuses stay; changes `DEVELOPMENT_DATABASE_DIRECTORY`. It applies
the question-12 living-prose denylist, under which a case-insensitive
`\bframenest\b` match in a living file fails unless copied verbatim into an
exception list, and the only allowed exceptions are the ADR-0085 frozen residues.
Deploying C7 onto a host still running `framenest.service` must **refuse** via the
guard. See D-7 for the trap in this cut.

**C8.** Not a side effect of C6 or of any routine web deploy. Needs a grant
explicitly allowing one stop and start of the capture bridge, runner and Xvfb, via
a **new** `migrate-capture-paths` subcommand rather than `activate-capture`, which
stays a release-switch operation. The web service is not stopped. Unit names stay
`kronika-capture-*`. The most likely cut to leave capture not serving; the least
likely to leave the web service down. Rollback restores the previous capture units
and `/opt/framenest/capture-current`.

**C9.** Separate E4 grant, only after C8 and after one scheduled backup on the new
layout reports `ready`. Deletes the disabled `framenest*` units, `/etc/framenest`,
the copied-from `/var/lib/framenest` and `/var/cache/framenest`, and
`/opt/framenest/current` if it is not the capture target. Never deletes tooling,
media, profiles, secrets or backup archives, and never deletes a release directory
that `capture-current` still resolves into. **One-way.**

## The confirmed goal, which bounds the whole

The Cooperator was asked to choose between two readings of "the word framenest
should appear nowhere" and chose explicitly:

```text
Zero user-visible and operational occurrences of the retired spelling, with the
ADR-0085 named frozen residues deliberately kept. No ADR amendment is pending and
none is authorised.
```

That decision gives the remaining cuts a sharp membership test:

```text
IN SCOPE     user-visible strings, operator-facing process output, CLI help text,
             validation messages that reach an API response, and operational values
OUT OF SCOPE source docstrings, test module docstrings, comments, Python class and
             module names, and the ADR-0085 named frozen residues
```

The 47 residual occurrences in `src/framenest` are all out of scope by this test.
Plan whether docstrings and comments are retired as a deliberate later cut or
formally excluded for the life of the repository, and state which.

## Authority

```text
Positive authority: read any tracked file in /home/agile/Projects/kronika; read
  every file in the Meta trace directory listed under Mandatory reading; run
  read-only Git inspection; run the declared JavaScript route and the declared AP
  test operations if you need to confirm a baseline; produce the plan.

Negative authority: ANY file mutation, including in the repository, in /tmp and in
  the Meta trace; any commit, branch, tag, merge, rebase, stash or history rewrite;
  any push; any NUC contact, including SSH, the NUC worker gate, and
  deploy/ubuntu/framenest-release in every mode; any provider or capture-browser
  contact; any execution of a kronika-capture command; any database write of any
  kind; any dependency install, update or lockfile change; any reading of
  private/**, personal Fish configuration, browser profiles, cookies, tokens,
  credential stores, .secrets or ~/.config/opencode; any writing of the plan to a
  file.

Commands: JavaScript evidence goes only through `node --test tests/*.test.js` and
  focused `node --test <path>`. Python evidence goes only through
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  d5955d5c0478ef7fa025fa9f8cba26ef56656883 --operation <id> -- <argv>`, plus
  `./.ap/ap project check --root /home/agile/Projects/kronika --baseline
  d5955d5c0478ef7fa025fa9f8cba26ef56656883`. Never invoke `.venv/bin/python`,
  `python`, `python3` or `poetry run` for evidence, including as a text editor.
  Read-only Git inspection is allowed (`git status`, `git rev-parse`, `git log`,
  `git show`, `git diff`, `git ls-files`, `git grep`, `git ls-remote`,
  `git submodule status`, `git merge-base`); no other Git command. Any other
  command must be stated in the report with its purpose and a confirmation that it
  mutated nothing.

Dependency authority: none.

Git authority: none. Read-only inspection only. No commit of any kind.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.

Side-effect authority: none. This cut is read-only by design, which is why its
  evidence tier is planning-grade rather than E2.

Browser authority: none. Do not open Brave, do not load the extension.
```

## Verification

1. Confirm branch `main`, HEAD `d5955d5c0478ef7fa025fa9f8cba26ef56656883`, clean
   tree, submodule at `73e20ef80b88700d5fc397cd8edd4fc425869f`, `ap doctor` PASS.
   Stop if any fails.
2. Read ADR-0085 and the accepted plan in full before planning anything.
3. For every machine-readable inventory named above, **read the value from the
   repository and report what you read**, rather than repeating a figure from this
   prompt. If a figure here disagrees with the repository, the repository wins and
   the disagreement is a finding. Correction 3 in this prompt is a worked example:
   the Orchestrator checked the frozen-set size before reporting a suspected plan
   conflict, found the conflict did not exist, and did not report a false alarm.
4. Derive the current occurrence inventory yourself and reconcile it against the
   47 figure given here. Report both numbers and explain any difference.
5. Produce the completion plan. For each cut give the exact mutation, the exact
   authority a fresh Implementation Worker needs, the evidence that closes it, the
   machine-checkable proof, its rollback, and its preconditions.
6. Address every one of `Correction 1` through `Correction 5` and `D-1` through
   `D-8` explicitly, by name. Do not leave any unaddressed and do not merely
   restate it.
7. State the closure conditions for the logical whole and the evidence for each.
8. Confirm the working tree is still clean and HEAD unchanged before you finish.

```text
Evidence tier: planning-grade. Read-only analysis producing an executable plan.
```

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if ADR-0085 and the accepted plan contradict each other in a way that
  changes the goal; if closing the whole would require an ADR amendment, which is
  unauthorised; if any step you plan would need real provider, browser, capture or
  host authority you were not granted; if context pressure reaches the point where
  a bounded rotation is cheaper than a degraded plan.

Completion: one plan covering C3 to C9 plus the unowned items, every correction and
  deficiency addressed by name, machine-readable inventories re-derived from the
  repository, closure conditions stated, tree clean and HEAD unchanged.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `17_report_00.md` in /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this
  prompt expires. No implementation, no commit, no push, no publication, no NUC
  contact and no later cut is authorized by it.

Phase-qualified result: to be declared by you; this whole is not phase-qualified
Logical-whole closure: not-closed. You are planning its closure, not performing it.
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-evidence`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `17` and exchange `01` unchanged. Native
planning mode requires this artifact to open with a level-1 title; if your client's
surface forces a preamble above the report header, disclose it on the first line of
the report body.

Then, in this order:

1. **The plan**, cut by cut, C3 through C9, plus the unowned items, each with
   mutation, authority, evidence, proof, rollback and preconditions.
2. **Corrections**, addressing `Correction 1` through `Correction 5` by name, with
   your independent verdict on each.
3. **Deficiencies**, addressing `D-1` through `D-8` by name, each with a decision
   inside your plan or an explicit statement that it cannot be decided at planning
   time and why.
4. **Closure conditions** for the logical whole, with the evidence for each.
5. **The ten discipline rules**, confirmed, amended or replaced, with your reason.
6. The inventory figures you read from the repository, each labelled with its file
   and line, so the Orchestrator can check them without re-running your work.
7. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification.

Finish every terminal report with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

The Orchestrator expects real findings against the accepted plan and against its
own prior statements. Three of the last four Workers did find them, and two of those
findings were against the Orchestrator. A plan that reports nothing wrong with this
prompt is less credible than one that finds something, not more.

## Mandatory reading

- `docs/adr/0085-kronika-sole-identity.md` in full, especially "Named frozen
  residues".
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/03_report_00.md`
  in full. It is your specification for C3 to C9.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/16_report_00.md`
  in full, sections 3, 4, 7, 9, 10, 12, 13, 15 and 16. It is the evidence base for
  D-1 through D-8 and for both transcription-error findings.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/15_report_00.md`,
  sections 11 and 12.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/00_notes.md`, all
  entries dated 2026-10-02.
- `tests/contract/test_kronika_identity_retention.py` in full. It is the
  machine-readable inventory and the enforcement mechanism for C7.
- `deploy/ubuntu/framenest_release.py`, for the C4 engine move and the `ExecStart`
  guard.
- `scripts/operator/network/framenest_nuc_worker_gate.fish`, for the C4 rename and
  the prefix fallback.
- `pyproject.toml` and `ap.project.conf`, for the C3 package, distribution and
  provenance changes and the re-gate.
- `src/framenest/infrastructure/persistence/alembic_environment/` in full, for the
  alias, `env.py` and `script.py.mako`.
- `src/framenest/infrastructure/persistence/engine.py` and `catalog_schema.py`, for
  D-2 and D-3.
- `deploy/systemd/` in full, for the C6 unit installation and the capture naming
  asymmetry.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` and `docs/BACKUP_AND_RECOVERY.md`, for the C6
  Tailscale procedure and the C5 backup contract.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real browser profile.

## Communication

Report text and the plan are professional English. Do not use Czech or Slovak.

## Orchestrator note

Three things this prompt deliberately does not decide for you, because they are the
Orchestrator's to own and yours to inform: the exact cut boundaries if you find
`C3` must be split; the mechanism and window for the D-2 data operation; and whether
the whole closes at C9 or needs a terminal cut of its own. Report your
recommendation on each with your reasoning, and mark clearly anything you believe
requires the Cooperator's decision rather than yours.