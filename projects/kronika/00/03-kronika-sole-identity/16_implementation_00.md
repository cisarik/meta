# Authoritative Worker prompt — Worker session 16, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `16`, exchange `01`. Stored under the
Meta filename mapping as `16_implementation_00.md`, with report destination
`16_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 16
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C2D — retire the remaining product display prose and operator output
Reasoning recommendation: Medium
Recommended context capacity: approximately 250k tokens
```

Rationale: `Medium`, one band above C2c. The changes are still substitutions with
no logic, but the inventory now spans Python domain constants, argparse `help=`
text, API error payloads, stderr output and one external AI prompt, and the
correct handling of several of those requires judgement rather than mechanical
replacement. The judgement is bounded and stated below.

This is cut **C2d**, and it is deliberately placed **before C3**.

## Why this cut exists

The Cooperator has confirmed the target in explicit terms: **zero user-visible and
operational occurrences of the retired spelling, with the ADR-0085 named frozen
residues deliberately kept.** That decision has a useful consequence. It gives the
remaining cuts a sharp membership test:

```text
IN SCOPE   user-visible strings, operator-facing process output, CLI help text,
           validation messages that reach an API response, and operational values
OUT OF SCOPE  source docstrings, test module docstrings, comments, Python class and
           module names, and the ADR-0085 named frozen residues
```

Keeping docstrings out is deliberate, so that this cut stays narrow and auditable
instead of becoming a spelling sweep.

C2b and C2c settled the browser surfaces. **They could not finish this**, because
their grants deliberately excluded product Python. The product is currently split:
the web shell says Kronika while nine `Invalid FrameNest …` domain messages, the
`framenest-db --help` text and the production `--help` text still say the retired
name. C2c's own report is what surfaced the CLI residue.

## A correction the Orchestrator must disclose

My first inventory for this cut was **incomplete**, and you must not treat the
in-scope list below as exhaustive. I produced it by ranking grep output by
frequency and truncating it with `head -50`. The truncation was silent, and it hid
roughly a dozen real sites, including every `INVALID_*_MESSAGE` constant in
`domain/`, all five argparse `help=` strings, and the `server.py` stderr line.

The Orchestrator's second, untruncated derivation found 96 occurrences of the
standalone brand word in `src/framenest` and produced the list below. **Your first
act is still to re-derive independently.** Do not trust my count, and do not trust
my list; trust your own derivation and report any site I missed.

Derive by matching the brand as a **standalone word**, because a substring search
returns class names and module paths as noise:

```text
rg -n -P '(?<![A-Za-z_])FrameNest(?![A-Za-z])' src/framenest
```

Then classify every hit into exactly one of: user-visible or operational string, in
scope; docstring or comment, out of scope; class or module name, out of scope;
frozen residue, out of scope.

## The two lessons you must apply

**Lesson 1, from C2c: reject a weak pin.** In `application/x_acquisition.py` the
**identical** sentence `Requested category conflicts with the existing FrameNest
save.` appears at **lines 370, 374 and 379 of the same method**. A whole-file or
whole-function regex pin on that sentence stays green if one or two of the three
occurrences are renamed. The same sentence also appears at
`adapters/api/x_request_api.py:207`. Any pin covering it must count or scope **all
four** occurrences.

**Lesson 2, mine, and it runs the other way.** A grep for the retired brand in the
tests returns **false positives**, because a large share of the hits are
**negative** assertions that assert the brand is **absent**:

```text
assert ">FrameNest<" not in header_section
assert.doesNotMatch(adapterSource, /textContent = ["']Save to FrameNest["']/)
```

Those are correct and must not be repointed. Before treating any test hit as work,
open the line and establish whether it asserts **presence or absence**. Presence is
work; absence is already correct.

## Measured assertion inventory — use these as your expected counts

The Orchestrator measured the test-side cost of this cut before issuing it, so you
do not have to discover its size. **Exactly thirteen test literals pin any in-scope
string.** Any count you derive that disagrees with this table is a finding in its
own right and must be reported.

```text
 7  "Invalid FrameNest …"     test_media.py:3  test_libraries.py:2
                             test_identities.py:1  test_devices.py:1
 2  "FrameNest Server"        test_library_workflow.py:212,227
 2  "FrameNest configuration could not be loaded."
                             test_operator_cli_hygiene.py and one other
 1  "FrameNest startup failed. Check logs for details."
 1  "Requested category conflicts with the existing FrameNest save."
                             test_x_request_api.py:282
 0  every other in-scope string
```

Three consequences follow, and each one changes how you must work.

**The five argparse `help=` strings are entirely untested.** `test_operator_cli_hygiene`
only asserts that `--help` **succeeds** from an unrelated working directory; it never
inspects the text. That is why those five renames are free. It also means you cannot
demonstrate them failing on revert. Say so plainly in your report rather than
performing a meaningless revert demonstration for them.

**Three of the four category-conflict occurrences are entirely unpinned.** The single
pin at `test_x_request_api.py:282` is a **scoped** comparison of an API error
payload, so it covers `x_request_api.py:207` only. The three in
`application/x_acquisition.py:370,374,379` raise the same exception class and produce
the same sentence, but no test asserts their text. Renaming them is therefore free
**and unverified**: no test will catch a mistake, and no test will fail if you forget
them. You must state this coverage gap explicitly in your report, and you must prove
by enumeration that all four were changed rather than relying on a red test.

**Both `FrameNest Server` pins are correctly scoped**, at `test_library_workflow.py:212`
and `:227`. The second one asserts the **persisted** row via `devices.list_all()[0]
.display_name`, so it genuinely proves the new default reaches the database. That is
the single most valuable assertion in this cut; make sure it passes.

## In scope

Re-derive all of this. The line numbers are for orientation only.

### 1. The domain validation message constants

`src/framenest/domain/` stores these as named module constants, so each is a single
change point. All of them are surfaced through API error responses:

```text
domain/media.py:11,12,13            INVALID_MEDIA_MESSAGE, _LOCATION_, _PATH_
domain/media_cover.py:11,12         INVALID_COVER_MESSAGE, _SOURCE_OBSERVATION_
domain/media_metadata.py:20         INVALID_MEDIA_METADATA_MESSAGE
domain/media_user_alias.py:22       INVALID_MEDIA_USER_ALIAS_MESSAGE
domain/identities.py:9              INVALID_IDENTITY_MESSAGE
domain/devices.py:9                 INVALID_DEVICE_MESSAGE
domain/libraries.py:11,12           INVALID_LIBRARY_MESSAGE, _ROOT_
domain/uploads.py:14                INVALID_UPLOAD_SESSION_MESSAGE
```

Change the brand word only. Keep each constant's name, its position, and the exact
non-brand wording, because these strings are part of the domain's error contract.

### 2. The API error payloads

```text
adapters/api/media_alias_api.py:40           ALIAS_INVALID_MESSAGE
adapters/api/x_request_api.py:185            "Invalid FrameNest media user alias.", 422
adapters/api/x_request_api.py:207            the category-conflict sentence
application/x_acquisition.py:370,374,379     the same sentence, three times
```

### 3. The runtime and CLI output

```text
infrastructure/runtime/development.py:222,273,286,296,314,316,338,355,418,468,479,619
infrastructure/runtime/production.py:86      "FrameNest health check failed."
adapters/cli/ai.py:720                       "FrameNest configuration could not be loaded."
infrastructure/persistence/cli.py:70         the same sentence, second occurrence
adapters/cli/youtube.py:187                  "The loopback FrameNest operator API is unavailable."
server.py:147                                stderr configuration-error line
```

### 4. The argparse help text, which is user-visible operational output

```text
infrastructure/runtime/production.py:114,118 framenest-production --help strings
infrastructure/persistence/cli.py:85,86      framenest-db --help strings
```

### 5. The configuration error

```text
configuration.py:461   "FrameNest private storage paths must not overlap"
```

### 6. The migration connection error

```text
infrastructure/persistence/alembic_environment/env.py:11
  "FrameNest migration connection is unavailable."
```

This is operator output on a migration failure. In scope. It is **not** one of the
frozen Alembic revision files.

### 7. The device display-name default

```text
application/library_workflow.py:21
  SERVER_DEVICE_DISPLAY_NAME = "FrameNest Server"
```

Change the value to `"Kronika Server"`. Change **nothing else** in that module, and
do not rename the constant. It is the default applied to a newly registered device.

**Important context you are not being asked to act on:** the one device on the NUC
does **not** carry this value. Its stored name was supplied by the operator at
registration time through `--display-name`. So this change affects only devices
registered from now on, and it will **not** repair the existing row. That row is
handled by a separate operator data operation that the Orchestrator owns. Do not
attempt it, and do not write to any database.

### 8. The external AI system prompt — read this twice

```text
application/movie_identification.py:236
  f"""You are FrameNest's movie identification assistant.
```

This string is **sent to an external AI provider**. It is the one site in this cut
that leaves the host, and it is not user-visible in the interface.

Change the brand word only, so the sentence reads `You are Kronika's movie
identification assistant.` Do **not** restructure the prompt, do not change any
other instruction, and do not change its f-string placeholders.

Report this change as its own item, because it is the only externally visible
consequence in this cut and the Cooperator must be told about it explicitly.

## Exclusion classes — apply them precisely

**Excluded 1 — deliberately dual-spelled message, DO NOT CHANGE.**
`adapters/api/tailscale_ingress.py:869` reads `"The FrameNest or Kronika mutation
header is required "`. That names **both** spellings **on purpose**, and it is
correct today, because C2 sends both headers and the server accepts both. Simplifying
it to a single spelling would be a one-sided cross-boundary change. It becomes
correct to simplify at **C7**, when the old header is retired. Leave it. If you
believe it must change now, stop and report instead of editing.

**Excluded 2 — the mutation header and both cross-boundary protocol strings.**
`X-FrameNest-Request`, `framenest-companion.v1` and `framenest.companion.web.v1`
stay until C5 and C7. Roughly twenty-four test assertions pin the header
deliberately. Do not change any of them and do not repoint those assertions.

**Excluded 3 — Python class and module names.** `FrameNestSettings`,
`FrameNestConfigurationError`, `FrameNestJsonFormatter` and the long
`FrameNest*Error` domain hierarchy travel with the package rename at **C3**. Leave
every one alone.

**Excluded 4 — docstrings and comments.** Roughly a third of the 96 hits are
module, class and function docstrings, plus prose comments such as
`devices.py:34` and `upload_validation_coordinator.py:78`. The confirmed target
excludes them. Leave them. List them in your report as an enumerated out-of-scope
class so a later cut can pick them up knowingly.

**Excluded 5 — the 36 applied Alembic revision files and the ADR-0085 named frozen
residues.** The revisions contain
`NotImplementedError("FrameNest migration downgrades are not supported.")` at
`versions/0001_initial_foundation.py:17`, `versions/0002_device_registry.py:30` and
`versions/0003_library_registry.py:56`. These are frozen by ADR-0085 and by Part A
of the retention ledger. Do not touch them.

**Excluded 6 — the Alembic scaffolding, named so it cannot be lost.**
`infrastructure/persistence/alembic_environment/script.py.mako:19` contains
`raise NotImplementedError("FrameNest migration downgrades are not supported.")` in
the **template that generates future migration files**. It is not one of the 36
frozen revisions, so it is not frozen, but renaming it changes what every future
migration will say, and that belongs with the migration-hosting concerns of **C4**.
Leave it and report it.

**Excluded 7 — the development launcher default paths.** In
`infrastructure/runtime/development.py`, `_database_path`, `_runtime_dir` and
`_log_path` embed the retired brand in macOS and XDG paths such as
`~/Library/Application Support/FrameNest/development/catalog.sqlite3`. Each returns
exactly one path and never reads the old one, so renaming orphans an existing
development database rather than migrating it. **C4 owns this.** Change only the
message strings in that module, and change no path expression in it.

## Authority

```text
Positive authority: edit exactly the in-scope items 1 to 8 above, plus any
  additional file your independent derivation shows must change, each reported
  explicitly; create one commit on local main; run the declared JavaScript route and
  the declared AP test operations; run read-only Git inspection.

Negative authority: any change to the deliberately dual-spelled message in
  Excluded 1; any change to a mutation header spelling or to either
  cross-boundary protocol string in Excluded 2; any change to a Python class or
  module name in Excluded 3; any change to a docstring or comment in Excluded 4;
  any change to the 36 applied Alembic revision files in Excluded 5; any change to
  script.py.mako or any other Alembic scaffolding in Excluded 6; any change to a
  path expression, a directory name or a default path in development.py under
  Excluded 7; any change to any file under extension/**, which C2b and C2c settled;
  any change to src/framenest/adapters/api/web/**; any executable logic change;
  any database or filesystem write of any kind; any NUC contact, including SSH, the
  NUC worker gate, and deploy/ubuntu/framenest-release in every mode; any provider
  or capture-browser contact; any execution of a kronika-capture command; any
  change to any ADR, docs/**, AGENTS.md, root Markdown file, pyproject.toml,
  ap.project.conf, deploy/**, scripts/**, .gitmodules or .gitignore; any new branch,
  push, tag, merge, rebase or history rewrite; any dependency install, update or
  lockfile change; any reading of private/**, personal Fish configuration, browser
  profiles, cookies, tokens, credential stores, .secrets or ~/.config/opencode; any
  write to /home/agile/meta.

Commands: JavaScript evidence goes only through `node --test tests/*.test.js` and
  focused `node --test <path>`. Python evidence goes only through
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  77bcb81c8a5f84e91ec4b31dd12f8ad2204016a8 --operation <id> -- <argv>`, plus
  `./.ap/ap project check --root /home/agile/Projects/kronika --baseline
  77bcb81c8a5f84e91ec4b31dd12f8ad2204016a8`. Never invoke `.venv/bin/python`,
  `python`, `python3` or `poetry run` for evidence, including as a text editor.
  Read-only Git inspection is allowed (`git status`, `git rev-parse`, `git log`,
  `git show`, `git diff`, `git ls-files`, `git grep`, `git ls-remote`,
  `git submodule status`, `git merge-base`); no other Git command. Throwaway probe
  files under /tmp only. Any other command must be stated in the report with its
  purpose and a confirmation that it mutated nothing.

Dependency authority: none.

Git authority: one commit on local main. No push, no new branch, no tag, no merge.

Network authority: none beyond read-only public Git ref verification. In particular,
  do not contact any AI provider; the prompt in item 8 is a string edit, never a call.

Secret authority: none.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only, plus scratch
  files under /tmp.

Browser authority: none. Do not open Brave, do not load the extension, do not touch
  a real profile.
```

## Verification

1. Confirm branch `main`, HEAD `77bcb81c8a5f84e91ec4b31dd12f8ad2204016a8`, clean
   tree, submodule at `73e20ef80b88700d5fc397cd8edd4fc425869f`, `ap doctor` PASS,
   `ap project check --baseline` PASS. Stop without editing if any fails.
2. Produce your own standalone-word derivation and classification, and **reconcile
   it against my list before editing.** Report your count, my count, and every site
   I missed or mis-classified. Explain any difference before you touch a file.
3. Build the assertion inventory for the in-scope strings and **reconcile it against
   the measured table above before editing.** Expect exactly thirteen literals. For
   each, establish by opening the line whether it asserts **presence or absence**,
   and state which. Report the count of literals pinning the domain
   `Invalid FrameNest …` messages separately; it must be seven.
4. Reproduce both baselines once. Expect Python `4359 passed, 8 skipped, 3 warnings`
   and JavaScript `578 passed, 0 failed, 5 skipped`. The suite takes about eleven
   minutes; let it finish once. **Do not edit while a suite is running.**
5. Make the changes, brand word only.
6. For each repointed assertion, show it failing when the new text is reverted. The
   five argparse help strings have no assertion and therefore **cannot** be
   demonstrated this way; say so instead of faking it. For the category-conflict
   sentence, show that reverting **only one of the four** occurrences turns its pin
   red, and separately prove by enumeration that the three unpinned occurrences were
   changed at all.
7. Prove by enumeration that no user-visible or operational occurrence of the
   retired brand remains in `src/framenest`, after removing the classes you
   classified as out of scope. Report both the remaining count and the full
   out-of-scope list.
8. Prove Excluded 1 through 7 are byte-identical by comparing the occurrence
   multiset of each excluded token at `77bcb81` against your working tree. Report
   each total. `tailscale_ingress.py:869` in particular must still contain both
   spellings.
9. Run `node --test tests/*.test.js` and the full declared `test` operation once.
   Report exact counts for both. **The JavaScript count must not change**, because
   this cut touches no JavaScript; if it does, stop and explain.
10. Run the retention module. Files may leave `EXPECTED_FRAMENEST_CONTENT_PATHS`;
    report any movement with its cause and re-pin only what genuinely moved. **Part A
    and Part B must not move.** In particular no Alembic revision may move.
11. Confirm `git diff --stat 77bcb81..HEAD` touches only reported paths.
12. After the commit run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <new commit SHA>` and confirm PASS.

```text
Evidence tier: E1. String substitutions with no logic change, no contract change and
  no remote effect, with the excluded classes proven byte-identical. The external
  prompt edit is a string edit only and must be reported as such.
```

## Git

One commit on local `main`, parent `77bcb81c8a5f84e91ec4b31dd12f8ad2204016a8`.
Suggested subject:

```text
refactor(identity): retire the remaining product prose and operator output
```

Do not push. Publication is a separate bounded grant.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if either baseline does not reproduce; if your derivation and the
  Orchestrator's list cannot be reconciled before editing; if any site turns out to
  be machine-read, docstring or deliberately dual rather than user-visible or
  operational text; if `tailscale_ingress.py:869` would have to change; if any path
  expression in development.py would have to change; if any Alembic revision or any
  Part A or Part B ledger pin would move; if the JavaScript count changes; if any
  step would need a real browser profile or a provider call; if context pressure
  reaches the point where a bounded rotation is cheaper than a degraded commit.

Completion: one commit; every in-scope string retired; the four occurrence sites of
  the category-conflict sentence handled together; every repointed assertion
  demonstrated failing on revert; Excluded 1 through 7 proven byte-identical; both
  routes green with an unchanged JavaScript count; Part A and Part B unmoved; tree
  clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `16_report_00.md` in /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this
  prompt expires. No further implementation, no push, no publication, no NUC contact
  and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `16` and exchange `01` unchanged. Then:
your derivation with its total and its full classification; the reconciliation
against the Orchestrator's list, naming every site I missed; the exact diff of every
path; the before-and-after text of every renamed string; the assertion inventory
reconciled against the measured thirteen, with the count of literals pinning the
domain `Invalid FrameNest …` messages; every repointed assertion with its revert
demonstration, and an explicit statement for the five help strings that no
demonstration is possible because none of them is asserted; the four-occurrence
category-conflict enumeration together with an explicit statement that three of the
four are unpinned and that the single scoped pin covers only
`x_request_api.py:207`; the external AI prompt as its own item; the byte-identity
totals for Excluded 1 through 7; baseline and final exact counts for both routes;
every ledger movement with its cause; the commit SHA; deviations, risks and missing
evidence; and one smallest next step.

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
disclose it on the first line of the report body.

## Mandatory reading

- `docs/adr/0085-kronika-sole-identity.md` in full, especially "Named frozen
  residues".
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/15_report_00.md`,
  sections 3, 11 and 12, which are your specification.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/00_notes.md`, the
  entries dated 2026-10-02 on the device observation and the truncation error.
- `src/framenest/infrastructure/runtime/development.py` in full, so you can tell a
  message string from a path expression without guessing.
- `src/framenest/infrastructure/runtime/production.py` around lines 80-125.
- `src/framenest/infrastructure/persistence/cli.py` in full; it is short.
- `src/framenest/adapters/api/tailscale_ingress.py` around lines 860-880.
- `src/framenest/application/movie_identification.py` around lines 225-250.
- `src/framenest/application/library_workflow.py` around lines 15-30 and 190-200.
- `src/framenest/application/x_acquisition.py` around lines 360-385.
- `tests/contract/test_kronika_identity_retention.py` in full.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md` Worker Execution section,
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the product's user-visible and operational surface will carry no
retired spelling, and one deploy will close C2b, C2c and C2d together. What remains
under the old brand afterwards is only what the confirmed target excludes: docstrings
and comments, class and module names at C3, the launcher paths and Alembic
scaffolding at C4, the environment, storage and header keys at C5 and C7, the
deliberately dual-spelled message and both protocol strings at C7, and the
ADR-0085 frozen residues permanently. The single stored device display name on the
NUC is a separate operator data operation that follows the deploy.