# Authoritative Worker prompt — Worker session 06, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `06`, exchange `01`. Stored under the
Meta filename mapping as `06_correction_00.md`, with report destination
`06_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-02 — uniform exit status 2 for an identity-environment conflict at every in-package entry point
Reasoning recommendation: Medium
Recommended context capacity: approximately 250k tokens
```

Rationale: this is a bounded correction at known locations with a stated
requirement, but it spans every command entry point and its risk is regression
in **other** exit statuses rather than in the new one. That cross-entry-point
regression surface is what keeps it at `Medium` rather than `Low`.

This is correction **C1b**, closing the one deviation the Orchestrator accepted
from Worker session 05. It is not cut C2 and carries no C2 authority.

## Why this correction exists

The accepted plan `03_report_00.md` requires that a conflict between the two
accepted prefixes **fails closed with exit status 2 for CLIs**, and the message
names the suffixes only. Worker session 05 implemented the resolver and proved
exit 2 for the two stdlib-only deploy engines. It reported, correctly, that the
in-package entry points fall back to their own existing sanitized exit statuses
of 1 or 6, and it declined to edit modules outside its authorized surface.

The Orchestrator has now measured that the deviation is **wider than five
entry points**. These modules construct settings and can therefore surface an
`IdentityEnvironmentConflictError`:

```text
src/framenest/server.py                                          (framenest-server)
src/framenest/infrastructure/persistence/cli.py                  (framenest-db)
src/framenest/infrastructure/runtime/production.py               (framenest-production)
src/framenest/infrastructure/runtime/development.py              (framenest-dev)
src/framenest/adapters/cli/ai.py                                 (framenest-ai)
src/framenest/adapters/cli/catalog.py                            (framenest-catalog)
src/framenest/adapters/cli/library.py                            (framenest-library)
src/framenest/adapters/cli/youtube.py                            (framenest-youtube)
src/framenest/adapters/cli/previews.py                           (framenest-previews)
src/framenest/adapters/cli/covers.py                             (framenest-covers)
src/framenest/adapters/cli/sidecar.py                            (framenest-sidecar)
```

Worker session 05 named five of these. Treat the list above as a lead, not as
the scope: **enumerate every module that constructs `FrameNestSettings` or calls
`load_settings`, and handle each one you find.** Also enumerate the remaining
console scripts in `pyproject.toml` and state, per script, whether it can surface
the conflict and how. A script that provably cannot is a legitimate report line,
not a gap.

## Goal

Make an identity-environment conflict exit with status **2** at every in-package
entry point that can surface it, with a message naming only the affected
suffixes, without changing any other exit status, any other output shape, or any
existing failure mode, and without leaking a value.

## Verified current state

```text
Repository checkout topology: standalone checkout
Expected branch: feat/kronika-identity-dual-read
Expected HEAD: 90c93eac94171182039a76fbb1c956e42b44da2c
Expected subject: feat(identity): read both KRONIKA_ and FRAMENEST_ spellings, write only the old
Remote origin: https://github.com/cisarik/kronika
Public main: 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672
Note: this branch is deliberately not published. Do not push it.
Working tree: clean
Containing-repository .ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS, governing variant stable
ap.project.conf projectId: cisarik/kronika, provenanceModule framenest
Working directory: /home/agile/Projects/kronika
```

Baseline at this commit, measured by the Orchestrator through the canonical
route: Python `4274 passed, 8 skipped, 3 warnings, 0 failed`; JavaScript
`554 total, 549 passed, 0 failed, 5 skipped`. If your run does not reproduce
this, stop and report.

The retention test `tests/contract/test_kronika_identity_retention.py` is live.
This correction should not change any pinned count, because it adds no `KRONIKA_`
or `FRAMENEST_` spelling and renames no path. If a pin moves, that is a signal
you changed something you should not have. Stop and report rather than re-pinning.

Host note: the development host is a CachyOS Linux workstation. The MacBook
paths in older artifacts are historical text. The stale clone at
`/home/agile/Projects/framenest` is not a work source and contains `private/`,
which you must never read.

## Required mutation

### 1. Uniform conflict exit status

At every in-package entry point you enumerate, an
`IdentityEnvironmentConflictError` must produce process exit status **2** and a
message that names the two variable **suffixes** only, with no value, length,
hash or repr of either value, in that command's existing output shape.

Two mechanisms are acceptable. Choose one, apply it consistently, and state which
you used and why:

- **(a) Direct catch.** Handle `IdentityEnvironmentConflictError` ahead of that
  command's existing `except` clauses and return 2.
- **(b) Sanitized translation, exit mapped.** Keep Worker session 05's design of
  translating into the command's own sanitized error type, and make that type map
  to exit status 2.

Mechanism (b) preserves each command's existing error-reporting contract more
faithfully. Prefer it unless you can show a concrete reason (a) is required. If
you use (a), say which command's output contract you had to bypass and why.

### 2. Consume the dead constant

`EXIT_IDENTITY_ENVIRONMENT_CONFLICT` in `src/framenest/identity_env.py` is
currently defined and never consumed. Use it as the single in-package source of
the value 2, so the constant stops being dead and in-package handlers cannot
drift apart. The two stdlib-only deploy-engine mirrors keep their own local
constant, because a stdlib-only mirror cannot import this one; do not attempt to
remove that duplication in this correction.

### 3. What must not change

- No exit status other than the conflict status may change, for any entry point,
  for any input. This is the primary regression risk of this correction.
- No success or failure output shape may change beyond the conflict path.
- No traceback may become reachable from a conflict, at any entry point.
- `hide_input_in_errors`, `extra="ignore"`, `env_file_encoding`, the retained
  `env_prefix`, and process-over-env-file precedence all stay as Worker session
  05 left them.
- No writer may switch to a `KRONIKA_` spelling. The session 05 invariant stands:
  readers learn the new spelling, writers keep the old one.
- `deploy/ubuntu/framenest_release.py` and `deploy/ubuntu/production_ai_deploy.py`
  are **not** in scope. Their behaviour is already proven correct.
- No package move, no `ap.project.conf` change, no `pyproject.toml` change, no
  console-script rename, no header change, no unit or host path change, no
  Alembic change, no documentation change.

## Authority

```text
Positive authority: edit exactly src/framenest/identity_env.py and the
  in-package entry-point modules you enumerate and report under Goal; add tests
  for every behaviour listed under Verification; create one local commit on the
  existing branch feat/kronika-identity-dual-read; run the declared AP test
  operations and the declared JavaScript test route; run read-only Git
  inspection.

Negative authority: any change to deploy/**, deploy/systemd/**, pyproject.toml,
  ap.project.conf, .gitmodules, .gitignore; any change under
  src/framenest/infrastructure/persistence/alembic_environment/versions/; any
  change to docs/**, AGENTS.md or any root Markdown file; any change to
  src/kronika_capture/**; any change to the mutation header gate in
  src/framenest/adapters/api/tailscale_ingress.py; any change to a durable
  artifact reader or writer; any new branch, push, tag, merge, rebase or history
  rewrite; any dependency install, update or lockfile change; any NUC contact,
  including SSH, the NUC worker gate, and deploy/ubuntu/framenest-release in
  every mode; any provider or capture-browser contact; any reading of private/,
  personal Fish configuration, browser profiles, cookies, tokens, credential
  stores, .secrets or ~/.config/opencode; any write to /home/agile/meta.

Commands: Python evidence and tests go only through the canonical declared
  route, `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  90c93eac94171182039a76fbb1c956e42b44da2c --operation <id> -- <argv>`, with
  operations declared in ap.project.conf, plus `./.ap/ap project check --root
  /home/agile/Projects/kronika --baseline
  90c93eac94171182039a76fbb1c956e42b44da2c`. JavaScript tests use the declared
  `node --test` route. Never invoke `.venv/bin/python`, `python`, `python3` or
  `poetry run` for evidence. Read-only Git inspection is allowed (`git status`,
  `git rev-parse`, `git log`, `git show`, `git ls-files`, `git grep`,
  `git ls-remote`, `git submodule status`, `git merge-base`); no other Git
  command. Any other command must be stated in the report with its purpose and a
  confirmation that it mutated nothing.

Dependency authority: none. If you conclude a dependency is required, stop and
  report.

Git authority: one additional local commit on the existing branch
  feat/kronika-identity-dual-read. No new branch, no push, no publication.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none. This applies with extra force to the conflict path,
  which must reveal suffixes only.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope; the
  accepted plan and this prompt are task context, not higher authority. On
  conflict between retained context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only.

Browser authority: none.
```

## Verification

Before editing confirm branch `feat/kronika-identity-dual-read`, HEAD `90c93ea…`,
clean tree, submodule at the pin, `ap doctor` PASS, `ap project check --baseline`
PASS. Stop without editing if any fails.

Then:

1. Enumerate every module constructing `FrameNestSettings` or calling
   `load_settings`, and every console script in `pyproject.toml`. Report the
   complete mapping: entry point, module, can it surface the conflict, and how
   it is now handled.
2. Reproduce the baseline once with the declared `test` operation and
   `node --test tests/*.test.js`. Expect `4274 passed, 8 skipped, 3 warnings` and
   `549 passed, 0 failed, 5 skipped`. The suite takes about eleven minutes; let
   it finish once. Do not edit while a suite is running.
3. Implement the mutation.
4. For **each** entry point that can surface the conflict, add and run a named
   test proving: a conflicting pair exits **2**; the output names the two
   variable suffixes and contains neither value, nor a length, nor a hash, nor a
   repr; there is no traceback; and the command's normal success and normal
   failure statuses are unchanged.
5. Add a test proving the empty-string case still behaves as unset at the entry
   point, and that identical values in both prefixes still succeed, so the
   correction cannot have broken Worker session 05's behaviour.
6. Run the retention test and confirm **no pin moved**.
7. Run the full declared `test` operation once. Report exact counts; skips must
   remain 8 and warnings 3.
8. Run `node --test tests/*.test.js`. Expect no change; this correction touches
   no JavaScript.
9. Confirm `git diff --stat` for the previous commit `18c357c..HEAD` still shows
   no change to `ap.project.conf`, `pyproject.toml`, `deploy/**`,
   `deploy/systemd/**`, the 36 applied Alembic files, `docs/**`, root Markdown
   files, or `src/kronika_capture/**`.
10. After the commit run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <new commit SHA>` and confirm PASS.

```text
Evidence tier: E2. Exit statuses are a user-visible operator contract across many
  entry points, so the primary risk is regression in statuses other than the new
  one. That risk is why the full suite is required here rather than only focused
  tests.
```

## Git

One additional commit on `feat/kronika-identity-dual-read`, parent
`90c93eac94171182039a76fbb1c956e42b44da2c`. Suggested subject:

```text
fix(identity): exit 2 on an identity-environment conflict at every entry point
```

Do not push. Do not create a new branch.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the baseline does not reproduce; if uniform exit 2 would require
  changing an exit status other than the conflict status; if uniform exit 2 would
  require changing a command's output contract beyond the conflict path; if any
  retention-test pin moves; if a change would need a path outside the authorized
  surface; if you find an entry point whose conflict path cannot reach exit 2
  without one of the above; if context pressure reaches the point where a
  bounded rotation is cheaper than a degraded commit.

Completion: one additional commit on the existing branch, exit 2 proven at every
  enumerated entry point with no value disclosure and no traceback, every other
  exit status unchanged, session 05 behaviour preserved, retention pins unmoved,
  both routes green, tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `06_report_00.md` in
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
echoing `kronika-sole-identity`, session `06` and exchange `01` unchanged. Then:
the complete entry-point enumeration from Verification step 1, including scripts
that provably cannot surface the conflict; which mechanism (a) or (b) you used
and why; the exact diff of every path; the named test per entry point for
Verification step 4; the empty-string and identical-value regression tests;
confirmation that no retention pin moved; confirmation that no other exit status
changed anywhere; baseline and final exact counts for both routes; the branch
name and both commit SHAs; deviations, risks and missing evidence; and one
smallest next step.

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

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/03_report_00.md`,
  the accepted plan, C1's fail-closed clause and the exit-2 requirement.
- `src/framenest/identity_env.py` in full.
- `src/framenest/configuration.py` around its settings loader and its
  `FrameNestConfigurationError` handling.
- Each entry-point module's `main()` and its existing top-level exception
  handling, so you extend the established pattern rather than inventing one.
- `deploy/ubuntu/production_ai_deploy.py` lines 20-35 and 180-190, as the
  already-correct stdlib-only reference for the exit-2 shape.
- `tests/contract/test_kronika_cli_and_release_readers.py` in full, to see how
  the session 05 exit-2 tests are written.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md` Worker Execution section,
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, or
any credential store.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak in repository or report artifacts.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the entry-point enumeration and the
no-other-status-changed claim. The expected next envelope is a fresh independent
audit of the whole C1 plus C1b state, because C1 widened a mutation-authorization
boundary. Publication and the routine NUC refresh each remain separate bounded
grants.