# Authoritative Worker prompt — Worker session 08, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `08`, exchange `01`. Stored under the
Meta filename mapping as `08_correction_00.md`, with report destination
`08_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 08
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-03 — restore pre-C1 process-environment semantics (F1, F2) and stop the dev launcher manufacturing a conflict (F4)
Reasoning recommendation: Medium
Recommended context capacity: approximately 250k tokens
```

Rationale: this is a bounded correction at known locations, but its central
requirement is **exact behavioural parity with a specific earlier commit**, and
the risk that matters is encoding a *wrong oracle* into the regression test that
guards the whole fix. That is cross-file, low-uncertainty work with a strong
validation requirement, which is the `Medium` band. Escalate only by naming the
evidence you could not obtain at this profile.

This is correction **C1c**, closing findings F1, F2 and F4 from the accepted
independent audit `07_report_00.md`. It is not cut C2 and carries no C2 authority.

## Why this correction exists

The independent audit of C1 and C1b returned `PARTIAL` with two confirmed
defects on the configuration trust boundary. Both were caused by
under-specification in the Orchestrator's own C1 grant, not by Worker error. The
audit established that the mutation-authorization boundary and the fail-closed
resolver are sound; these are not gate bypasses.

**F1 — process-environment case-insensitive matching is lost.** `_DualPrefixEnvSettingsSource._load_env_vars`
returns only `_resolved_field_values(os.environ)`, **replacing** the mapping the
library produced. `parse_env_vars` no longer enumerates and case-folds the
process environment, and the library's `_apply_case_sensitive` at
`pydantic_settings/sources/base.py:359` lower-cases, so `framenest_port=9999`
configured the port before C1 and is now silently ignored, applying the model
default with exit 0.

**F2 — an explicitly empty value is now "unset" for every field.** `lookup_env`
coerces `""` to unset globally, so `FRAMENEST_PORT=` no longer raises the `int`
coercion `SettingsError` that produced `FrameNestConfigurationError` and exit 1;
it silently yields the default and exit 0. The Orchestrator's C1 grant asked for
empty-means-unset for the sake of the environment-file selector and systemd
`Environment=` handling. That rationale was about the selector, and applying the
rule to every field broke a configuration that previously failed closed.

**F4 — the development launcher manufactures a conflict for the server it
spawns.** `_spawn_server_process` writes `FRAMENEST_HOST` and `FRAMENEST_PORT`
into the child environment without removing or normalising an inherited
`KRONIKA_*` spelling, so an inherited `KRONIKA_HOST` or `KRONIKA_PORT` produces a
conflicting pair and the spawned server exits 2.

## Goal

Restore exact pre-C1 behaviour for **old-spelling-only process-environment and
environment-file input** — case variants, explicitly empty values, whitespace,
and invalid values — while keeping every C1 and C1b behaviour that the audit
confirmed sound. Then stop the dev launcher from creating a conflict it
manufactures itself.

This is a **restoration**, not a redesign. If restoring parity would require
changing a C1 behaviour the audit confirmed, stop and report instead.

## Verified current state

```text
Repository checkout topology: standalone checkout
Expected branch: feat/kronika-identity-dual-read
Expected HEAD: c02c6753694d5d4958045bb79f80b5eb94b9c75c
Expected subject: fix(identity): exit 2 on an identity-environment conflict at every entry point
Parent: 90c93eac94171182039a76fbb1c956e42b44da2c  (C1)
Behaviour-restoration reference: 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672  (published main, pre-C1)
Remote origin: https://github.com/cisarik/kronika
Public main: 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672
The branch is deliberately unpublished. Do not push.
Working tree: clean
Containing-repository .ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS, governing variant stable
ap.project.conf projectId: cisarik/kronika, provenanceModule framenest
poetry.lock: unchanged across 18c357c..c02c675, so the library's behaviour is
  identical at the restoration reference and at HEAD. This is what makes a
  stock-source oracle valid; state that you checked it.
Working directory: /home/agile/Projects/kronika
```

Baseline at this commit, measured by the Orchestrator through the canonical
route: Python `4314 passed, 8 skipped, 3 warnings, 0 failed`; JavaScript
`554 total, 549 passed, 0 failed, 5 skipped`.

The retention ledger `tests/contract/test_kronika_identity_retention.py` is live
and pinned. **The audit established that its Part C pins are scalars**, so they
detect that a total moved but not which occurrences moved, and a cut that
re-pins a scalar to match partial work passes. Therefore: if a pin moves because
your change legitimately adds occurrences, **re-pin it and report each change
with its exact cause**. Never contort the diff, never contort a test, and never
contort a name to hold a counter. A metric must not shape the code.

## Required mutation

### 1. Restore case-insensitive process-environment matching

A process-environment name that differs only in case from `FRAMENEST_<SUFFIX>` or
`KRONIKA_<SUFFIX>` must again configure the field, exactly as it did at
`18c357c`.

The audit's suggested mechanism is to resolve over a case-folded view inside the
settings source, for example by building `{k.upper(): v}` from `os.environ` and
passing that mapping to `lookup_env`. You may choose another mechanism if it
achieves identical observable behaviour.

Two edge cases you must decide explicitly, state, and test:

- **Both cases present with different values.** On Linux process environment
  names are case-sensitive, so both can exist. At `18c357c` the library lower-cased
  everything into one mapping and the later key won by iteration order. Decide
  what your mechanism does, and whether it matches that. If it cannot match
  exactly, say so and explain what differs and why it is acceptable; do not
  pretend parity.
- **Which value a case-folded view resolves when the two prefixes are involved.**
  The `KRONIKA_` versus `FRAMENEST_` conflict rule is case-**exact** and must stay
  case-exact. Only the *name* matching against field names becomes case-folded.

### 2. Restore fail-closed behaviour for an explicitly empty value

An explicitly empty value for an ordinary field must again produce the
pre-C1 outcome, which is a validation error and the command's existing failure
status, **not** a silent default.

The audit's suggested correction is to restrict empty-means-unset to the
`ENV_FILE` selector, where the Orchestrator's original rationale actually
applied. Prefer that. Then:

- Confirm whether the **environment-file** path has the same regression for an
  empty file value, and restore parity there too if it does.
- Preserve the `ENV_FILE` behaviour that C1b's tests depend on: an empty
  `KRONIKA_ENV_FILE` or `FRAMENEST_ENV_FILE` still behaves as unset.
- Preserve the conflict rule exactly. A conflicting pair still fails closed with a
  suffix-only message and exit 2, at every entry point.
- `hide_input_in_errors=True`, `extra="ignore"`, `env_file_encoding="utf-8"`, the
  retained `env_prefix="FRAMENEST_"`, the source ordering, and
  process-over-environment-file precedence all stay as they are at HEAD.

### 3. Stop the dev launcher manufacturing a conflict

In the development launcher, before the resolved values are written into the
spawned child's environment, the alternate spelling of every injected suffix must
be removed or normalised, so that the child cannot receive a conflicting pair
regardless of what the parent environment carries.

- Cover **every** identity-prefixed name the launcher injects, not only host and
  port. Enumerate them yourself.
- Perform the audit's `LEAD` check, which is in scope and cheap: grep every
  `env[...]` assignment and every `env=` subprocess construction in
  `src/framenest` for a hand-written identity-prefixed name, and compare each
  against the resolver's view. Fix every instance you find in the authorized
  surface, and report any you find outside it without editing it.
- Do not change what the launcher resolves or how it configures the child, only
  the shape of the environment it hands over.

### 4. Mandatory differential parity test

This is the deliverable that matters most, and the audit named it as the single
test whose absence let both defects through.

Add a test asserting that, **for every field of the settings model**, over a
matrix of **old-spelling-only** inputs covering case variants, explicitly empty,
whitespace-only, and invalid values, for **both** the process environment and the
environment file, the current dual-prefix source produces **exactly** what the
stock `EnvSettingsSource` plus the library's own `parse_env_vars` produced at
`18c357c`.

Requirements on the oracle:

- Build the oracle from the **unmodified library sources**, not from the
  project's dual-prefix classes, so it is an independent reference.
- State explicitly that the library is unchanged between `18c357c` and HEAD, and
  show the evidence, because that is what licenses using today's library as the
  reference for the older commit.
- If you cannot construct the oracle faithfully, **stop and report**. An
  approximate oracle would encode wrong behaviour as "parity" and is worse than
  no test.
- The test must fail if the parity is broken. Demonstrate that by deliberately
  breaking parity in a scratch copy under `/tmp` or by reverting your own fix
  in-memory, and report the observed failure. A parity test never shown failing is
  not evidence.

## Out of scope — do not touch

- **F3 is accepted as an amendment, not a defect.** `framenest-ai` changing a
  pre-existing uncaught-traceback exit 1 into a sanitized exit 2 is a strict
  improvement and is recorded as an amendment to the C1b goal. Do not revert it
  and do not change it.
- **F5 is deferred to C5.** Do not widen `read_current_release`'s manifest and
  release-SHA reads. The audit's instruction is that C5 must land the writer
  switch and that reader widening in one commit.
- **H2 is not in this correction.** Do not add either header spelling to
  `_SINGLETON_SECURITY_HEADERS`.
- **H1, H3, D1** are accepted or deferred. Do not change exit statuses for
  collisions, do not change the release engine's transport error handling, and do
  not change `_database_state`.
- The retention ledger's **Part A** frozen-blob pins and **Part B** path ledger
  must not change at all.
- No change to `deploy/**`, `deploy/systemd/**`, `docs/**`, `AGENTS.md`, any root
  Markdown file, `src/kronika_capture/**`, `pyproject.toml`, `ap.project.conf`,
  `.gitmodules`, `.gitignore`, the 36 applied Alembic revision files, or
  `src/framenest/adapters/api/tailscale_ingress.py`.

## Authority

```text
Positive authority: edit exactly src/framenest/identity_env.py,
  src/framenest/configuration.py, the development launcher and its runtime
  module, and any other file in src/framenest that the launcher environment
  audit in item 3 shows to be in scope, each reported explicitly; add the
  differential parity test and the focused regression tests for items 1 to 3;
  update Part C pins only where your change legitimately moves them, reporting
  each with its exact cause; create one additional local commit on the existing
  branch feat/kronika-identity-dual-read; run the declared AP test operations
  and the declared JavaScript test route; run read-only Git inspection.

Negative authority: anything in Out of scope above; any new branch, push, tag,
  merge, rebase or history rewrite; any dependency install, update or lockfile
  change; any NUC contact, including SSH, the NUC worker gate, and
  deploy/ubuntu/framenest-release in every mode; any provider or capture-browser
  contact; any execution of a kronika-capture command; any reading of private/,
  personal Fish configuration, browser profiles, cookies, tokens, credential
  stores, .secrets or ~/.config/opencode; any write to /home/agile/meta; any
  remediation of an audit finding outside F1, F2 and F4.

Commands: Python evidence goes only through the canonical declared route,
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  c02c6753694d5d4958045bb79f80b5eb94b9c75c --operation <id> -- <argv>`, with
  operations declared in ap.project.conf, plus `./.ap/ap project check --root
  /home/agile/Projects/kronika --baseline
  c02c6753694d5d4958045bb79f80b5eb94b9c75c`. JavaScript tests use the declared
  `node --test` route. Never invoke `.venv/bin/python`, `python`, `python3` or
  `poetry run` for evidence. Read-only Git inspection is allowed (`git status`,
  `git rev-parse`, `git log`, `git show`, `git diff`, `git ls-files`,
  `git grep`, `git ls-remote`, `git submodule status`, `git merge-base`); no
  other Git command. Running an installed console script under `.venv/bin` is
  permitted for observing exit status, using `env -i` with synthetic values and
  `HOME`/`TMPDIR` under `/tmp`, so nothing outside `/tmp` is written. Scratch
  files go under /tmp only. Any other command must be stated in the report with
  its purpose and a confirmation that it mutated nothing.

Dependency authority: none.

Git authority: one additional local commit on the existing branch. No push, no
  new branch.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none. Use only synthetic values. Never print, quote or
  summarize a real secret value, host identifier, address, disk serial, UUID or
  SSH fingerprint. The conflict path must continue to reveal suffixes only.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope; the
  accepted plan and audit report are task context, not higher authority. On
  conflict between retained context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only, plus scratch
  files under /tmp.

Browser authority: none.
```

## Verification

Before editing confirm branch `feat/kronika-identity-dual-read`, HEAD `c02c675…`,
clean tree, submodule at the pin, `ap doctor` PASS, `ap project check --baseline`
PASS. Stop without editing if any fails.

Then:

1. Reproduce the baseline once with the declared `test` operation and
   `node --test tests/*.test.js`. Expect `4314 passed, 8 skipped, 3 warnings` and
   `549 passed, 0 failed, 5 skipped`. The suite takes about eleven minutes; let it
   finish once. **Do not edit while a suite is running** — that contaminated a run
   in an earlier session.
2. Build the oracle first and demonstrate that it reproduces the two audit
   reproductions at HEAD before you change anything: `framenest_port=9999` and
   `FRAMENEST_PORT=` under `framenest-db status`. Both currently show the defect;
   the oracle must show the `18c357c` behaviour. Report the four observations.
3. Implement items 1, 2 and 3.
4. Add the differential parity test and the focused regressions. Show the parity
   test failing on deliberately broken parity.
5. Run the retention test and report every pin movement with its cause. Part A
   and Part B must be unchanged.
6. Run the full declared `test` operation once. Report exact counts; skips must
   remain 8 and warnings 3.
7. Run `node --test tests/*.test.js` and report any change.
8. Re-verify the two audit reproductions now show `18c357c` behaviour, and that
   the conflict path still exits 2 with a suffix-only message at a representative
   entry point, and that a same-value pair and the `ENV_FILE` empty case still
   behave as C1b requires.
9. Confirm `git diff --stat 90c93ea..HEAD` and `18c357c..HEAD` are still empty for
   every Out-of-scope path.
10. After the commit run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <new commit SHA>` and confirm PASS.

```text
Evidence tier: E2. Behaviour-restoring correction across the settings trust
  boundary, with a mandatory differential regression. The correction narrows
  behaviour back to a previously verified state rather than widening any
  boundary, so it is not a new trust-boundary exposure.
```

## Git

One additional commit on `feat/kronika-identity-dual-read`, parent
`c02c6753694d5d4958045bb79f80b5eb94b9c75c`. Suggested subject:

```text
fix(identity): restore pre-cut process-environment parity for old spellings
```

Do not push. Do not create a new branch.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the baseline does not reproduce; if `poetry.lock` turns out to differ
  between 18c357c and HEAD, which would invalidate the oracle; if a faithful
  oracle cannot be constructed; if restoring parity would require changing a C1
  behaviour the audit confirmed sound; if the both-cases-present semantics cannot
  be made to match 18c357c and you would have to guess; if any step would need an
  Out-of-scope path; if Part A or Part B pins would move; if context pressure
  reaches the point where a bounded rotation is cheaper than a degraded commit.

Completion: one additional commit, parity restored and demonstrated, the parity
  test shown failing on broken parity, F4 fixed with the launcher environment
  audit reported, the conflict path and exit 2 intact, Part A and Part B unmoved,
  both routes green, tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `08_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this
  prompt expires. No further implementation, no push, no publication, no NUC
  contact and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this correction, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `08` and exchange `01` unchanged. Then:
the oracle construction, the evidence that the library is unchanged between the
two commits, and the four step-2 observations; the exact diff of every path; your
explicit decision and test for the both-cases-present edge case, including any
residual divergence from `18c357c`; your decision on the environment-file empty
case; the complete launcher environment audit with every identity-prefixed name
you found and what you did with each; the parity test, and the demonstration that
it fails on broken parity; every Part C pin movement with its cause and
confirmation that Part A and Part B did not move; baseline and final exact counts
for both routes; the re-verified audit reproductions; the branch name and all
three commit SHAs; deviations, risks and missing evidence; and one smallest next
step.

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

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/07_report_00.md`,
  the accepted independent audit, in full. F1, F2, F4 and scope item 7 are your
  specification; F3, F5, H1, H2, H3 and D1 tell you what not to touch.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/03_report_00.md`,
  the accepted plan, C1 and C2.
- `src/framenest/identity_env.py` in full.
- `src/framenest/configuration.py` in full, especially the two dual-prefix source
  classes, `_resolved_field_values`, `_identity_suffix`, and the settings loader.
- The library sources, read with the read tool and never imported by a
  hand-launched interpreter: `pydantic_settings/sources/base.py`
  (`parse_env_vars`, `_apply_case_sensitive`), `sources/providers/env.py`,
  `sources/providers/dotenv.py`, and `main.py` (`_settings_init_sources`).
- `git show 18c357c:src/framenest/configuration.py` — the pre-C1 shape, which is
  the behaviour you are restoring.
- The development launcher and its runtime module, plus every `env[...]`
  assignment and `env=` subprocess construction in `src/framenest`.
- `tests/contract/test_kronika_identity_dual_read.py` and
  `tests/contract/test_kronika_cli_and_release_readers.py`, so you extend the
  established conventions and do not duplicate coverage.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md` Worker Execution section,
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real database, media path, profile or backup archive.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak in repository or report artifacts.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the oracle's validity, the parity
demonstration, and the F4 launcher audit. The audit's own recommendation is that
a fresh independent re-audit follows material correction on a trust boundary, so
that is the expected next envelope before C2. Publication of the branch and the
routine NUC refresh each remain separate bounded grants.