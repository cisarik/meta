# Authoritative Worker prompt — Worker session 10, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `10`, exchange `01`. Stored under the
Meta filename mapping as `10_correction_00.md`, with report destination
`10_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 10
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-04 — make the resolver's documented precedence and conflict scope match measured behaviour
Reasoning recommendation: Low
Recommended context capacity: approximately 250k tokens
```

Rationale: this correction changes **no runtime behaviour at all**. It rewrites
one docstring paragraph to match what the code already does, documents a rule that
already holds, and adds tests that pin behaviour which already exists. That is
mechanical, localized, trivially reversible work with strong verification, which
is the `Low` band. Escalate only by naming the concrete evidence you could not
obtain at this profile.

This is correction **C1d**, closing finding A1 and recording decision A2 from the
accepted independent re-audit `09_report_00.md`. It is not cut C2.

## Why this correction exists

The re-audit accepted C1c and returned `PASS with findings`. Its material finding
was **not** a behaviour defect. It was a false safety claim:

`src/framenest/identity_env.py:196-201`, in the docstring of the function that
defines the resolver's value-selection precedence, states: "the compatible
spelling is consulted first, so the identity spelling cannot be shadowed by a case
variant of the compatible one." That is false. Consulting the compatible layer
first is exactly what lets it win. The next sentence then says the reverse is not
true, so the paragraph is internally incoherent.

Measured, by the re-audit: `kronika_port=9998` together with
`framenest_port=9999` resolves to **9999**, so a case variant of the compatible
spelling evicts a case variant of the identity spelling with no conflict raised.
A **case-exact** `KRONIKA_<SUFFIX>` is immune, because the first layer
short-circuits. The behaviour is pre-C1-preserving, so nothing regressed. The
defect is the claim — and it sits where cut C7 will read it when it deletes the
compatible fallback.

Decision A2 is recorded here: the conflict rule is **per-channel**, and it must be
stated rather than enforced across channels.

## Goal

Make every documented statement about the identity resolver **true**, and pin the
behaviour with tests so a future docstring cannot drift from the code again.

No runtime behaviour may change. If any step would require one, stop and report.

## Verified current state

```text
Repository checkout topology: standalone checkout
Expected branch: feat/kronika-identity-dual-read
Expected HEAD: 24bea56daca28603d81cac8d7ed7e3888ba90671
Expected subject: fix(identity): restore pre-cut process-environment parity for old spellings
Lineage: 18c357c published main -> 90c93ea C1 -> c02c675 C1b -> 24bea56 C1c
Remote origin: https://github.com/cisarik/kronika
Public main: 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672
The branch is deliberately unpublished. Do not push.
Working tree: clean
Containing-repository .ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS, governing variant stable
Working directory: /home/agile/Projects/kronika
```

Baseline at this commit, measured by the Orchestrator through the canonical
route: Python `4347 passed, 8 skipped, 3 warnings, 0 failed`; JavaScript
`554 total, 549 passed, 0 failed, 5 skipped`.

The retention ledger is live. Your change adds documentation text and tests, so
Part C scalars may move. **Re-pin only what genuinely moved, report each movement
with its exact cause, and never contort a docstring or a test to hold a
counter.** Part A and Part B must not move.

## Required mutation

### 1. Rewrite the inverted docstring paragraph

Rewrite the closing paragraph of `lookup_field_value`'s docstring so it states
what the code does. The corrected claim, which you must verify before writing:

- The **case-exact** identity spelling is consulted first and short-circuits, so
  it **cannot** be shadowed by a case variant of the compatible spelling, nor by a
  case variant of itself.
- When **both** spellings are present only as case variants, the **compatible**
  spelling wins, because the compatible layer precedes the identity layer. A case
  variant of the identity spelling **can** therefore be shadowed by a case variant
  of the compatible one.
- This is deliberate, and the reason is pre-C1 behavioural parity: before the
  resolver existed the library read the compatible spelling at whatever case it
  was written, so a case variant of the compatible name is what an operator had
  working before this cut.
- The cross-prefix **conflict** check is unaffected and remains case-exact, because
  `lookup_env` runs unconditionally before any layer decides.

### 2. Every documented sentence must be traceable to a measurement

This is the deliverable that matters. For **each** statement in the rewritten
docstring, and for each statement you add anywhere documenting the conflict rule,
name in your report the specific measurement or code fact that supports it, and
give the evidence class: a measurement you took, a line of code you read, or an
authority document.

A claim with no supporting evidence must be deleted, not hedged. **Do not write a
sentence you have not verified.** The defect being corrected was exactly an
unverified sentence that read as a safety guarantee, so a hedged rewrite would
reproduce the same failure in softer words.

Include the corrected measurement set in your own support:

| Input | Current measured result |
|---|---|
| `KRONIKA_PORT=9998` + `FRAMENEST_PORT=9999` | conflict, exit 2 |
| `kronika_port=9998` + `framenest_port=9999` | `9999`, no conflict |
| `KRONIKA_PORT=9998` + `framenest_port=9999` | `9998`, no conflict |
| `KRONIKA_PORT=9998` + `KRONIKA_PORT=9999` (same name, cannot coexist exactly) | n/a; instead use two case variants of one name |
| `KRONIKA_PORT=9998` + `FRAMENEST_PORT=9998` | accepted |
| `KRONIKA_PORT=` + `framenest_port=9999` | `9999` |
| `kronika_port=` + `FRAMENEST_PORT=9999` | `9999` |

Verify each row yourself rather than trusting the table, and report any row where
the code disagrees with it — in which case the docstring follows the code, and the
table is what was wrong.

### 3. Document the per-channel conflict rule

State it explicitly in the resolver's own documentation, at the place a future
reader of the resolver will actually look:

- The conflict check is **per-channel**. `lookup_env` runs once per source over
  that source's mapping only.
- `KRONIKA_<S>` in the process environment together with `FRAMENEST_<S>` in the
  environment file therefore raises **no** conflict, and the process environment
  value wins, because process-over-environment-file precedence is the library's
  documented and intentional ordering.
- The reverse arrangement behaves the same way.
- State **why** no cross-channel check exists: failing closed on a cross-channel
  pair would break any deployment where the environment file supplies a default
  and the process environment overrides it. That is normal, intended operation,
  not a misconfiguration.
- Be precise about the scope: this is a deliberately silent resolution, not an
  oversight, and it is a divergence from a hypothetical global conflict rule.

Also check the module-level docstring of `src/framenest/identity_env.py` and the
docstring of `lookup_env` for the same omission, and correct them if they imply a
global rule.

### 4. Pin the layer order and the channel rule with tests

- One test pinning the observed layer order, so a future refactor that inverts it
  fails rather than passing silently. It must cover the case-exact identity
  short-circuit **and** the case-variant eviction, since those are the two halves
  of the corrected claim.
- One test pinning the per-channel rule in both arrangements, so the documented
  behaviour cannot drift.
- Every test must be shown failing when the property it names is violated. A test
  never seen failing is not evidence; demonstrate it.

### 5. Parity-test value guard

`tests/contract/test_kronika_settings_parity.py` builds its variable names from
`COMPATIBLE_ENVIRONMENT_PREFIX`. If cut C3 or C7 changes that constant's
**value**, the matrix silently changes its subject and the parity claim becomes
vacuous with no test failing.

Add the guard: assert `COMPATIBLE_ENVIRONMENT_PREFIX == "FRAMENEST_"` and
`FrameNestSettings.model_config["env_prefix"] == "FRAMENEST_"`. This is one line
plus the import. Show it failing when the constant is temporarily changed to a
different value in memory.

## Explicitly out of scope

- **No runtime behaviour change.** Not one line of executable logic may change. If
  the corrected documentation would only be true after a code change, stop and
  report instead.
- **A3**: the dropped `_env_*` constructor overrides. Unreachable today; recorded
  for the C3 grant, not fixed here.
- **Part C strengthening.** The pinned `EXPECTED_FRAMENEST_CONTENT_PATHS` set is a
  separate small grant and must not be started here.
- **ADR-0085 must not be edited.** It is published and accepted, and it states no
  conflict rule at all, so nothing in it is contradicted by documenting the
  per-channel rule. If you believe the ADR does need an amendment, stop and report
  that instead of editing it.
- The redundant double fold in the settings source: performance only, measured at
  about 0.008 % of a build. Do not touch it.
- F3, F5, H1, H2, H3 and D1 remain as recorded.
- No change to `deploy/**`, `deploy/systemd/**`, `docs/**`, `AGENTS.md`, any root
  Markdown file, `src/kronika_capture/**`, `pyproject.toml`, `ap.project.conf`,
  `.gitmodules`, `.gitignore`, the 36 applied Alembic revision files, or
  `src/framenest/adapters/api/tailscale_ingress.py`.

## Authority

```text
Positive authority: edit exactly src/framenest/identity_env.py (docstrings only)
  and tests/contract/test_kronika_settings_parity.py (the value guard and new
  tests); add tests to the most appropriate existing test module for the
  resolver, reported explicitly; update Part C pins only where your change
  genuinely moves them, reporting each with its exact cause; create one additional
  local commit on the existing branch feat/kronika-identity-dual-read; run the
  declared AP test operations and the declared JavaScript test route; run read-only
  Git inspection.

Negative authority: any change to executable logic, which is prohibited in this
  correction; anything in Explicitly out of scope above; any new branch, push,
  tag, merge, rebase or history rewrite; any dependency install, update or
  lockfile change; any NUC contact, including SSH, the NUC worker gate, and
  deploy/ubuntu/framenest-release in every mode; any provider or capture-browser
  contact; any execution of a kronika-capture command; any reading of private/,
  personal Fish configuration, browser profiles, cookies, tokens, credential
  stores, .secrets or ~/.config/opencode; any write to /home/agile/meta.

Commands: Python evidence goes only through the canonical declared route,
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  24bea56daca28603d81cac8d7ed7e3888ba90671 --operation <id> -- <argv>`, with
  operations declared in ap.project.conf, plus `./.ap/ap project check --root
  /home/agile/Projects/kronika --baseline
  24bea56daca28603d81cac8d7ed7e3888ba90671`. JavaScript tests use the declared
  `node --test` route. Never invoke `.venv/bin/python`, `python`, `python3` or
  `poetry run` for evidence, including as a text editor. Read-only Git inspection
  is allowed (`git status`, `git rev-parse`, `git log`, `git show`, `git diff`,
  `git ls-files`, `git grep`, `git ls-remote`, `git submodule status`,
  `git merge-base`); no other Git command. Running an installed console script
  under `.venv/bin` is permitted to observe exit status, under `env -i` with
  synthetic values and `HOME`/`TMPDIR` under /tmp, so nothing outside /tmp is
  written. Scratch files go under /tmp only. Any other command must be stated in
  the report with its purpose and a confirmation that it mutated nothing.

Dependency authority: none.

Git authority: one additional local commit on the existing branch. No push, no new
  branch.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none. Use only synthetic values. The conflict path must continue
  to reveal suffixes only.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope; the
  accepted plan and prior reports are task context, not authority. On conflict
  between retained context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only, plus scratch
  files under /tmp.

Browser authority: none.
```

## Verification

Before editing confirm branch `feat/kronika-identity-dual-read`, HEAD `24bea56…`,
clean tree, submodule at the pin, `ap doctor` PASS, `ap project check --baseline`
PASS. Stop without editing if any fails.

Then:

1. Verify every row of the measured table in item 2 yourself and report the
   results. If any row disagrees with the code, the docstring follows the code and
   you report the table as wrong.
2. Reproduce the baseline once with the declared `test` operation. Expect
   `4347 passed, 8 skipped, 3 warnings`. The suite takes about eleven minutes; let
   it finish once. **Do not edit while a suite is running.**
3. Prove before you write that the current docstring is false: run the
   `kronika_port=9998` + `framenest_port=9999` case and record that the identity
   case variant is evicted. That measurement is the justification for the rewrite.
4. Make the changes.
5. Show each new test failing when its named property is violated.
6. Confirm `git diff --stat c02c675..HEAD` still shows no change to
   `src/framenest/adapters/api/tailscale_ingress.py`, and that
   `git diff --stat 24bea56..HEAD` shows **docstring and test changes only** —
   that is the primary proof that no runtime behaviour changed.
7. Run the retention test and report every Part C movement with its cause; Part A
   and Part B must be unchanged.
8. Run the full declared `test` operation once. Report exact counts; skips remain
   8 and warnings 3.
9. Run `node --test tests/*.test.js`. Expect no change.
10. After the commit run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <new commit SHA>` and confirm PASS.

```text
Evidence tier: E1. Localized, documentation and tests only, no runtime behaviour
  change, trivially reversible, with strong verification.
```

## Git

One additional commit on `feat/kronika-identity-dual-read`, parent
`24bea56daca28603d81cac8d7ed7e3888ba90671`. Suggested subject:

```text
docs(identity): state the resolver's measured precedence and per-channel conflict rule
```

Do not push. Do not create a new branch.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the baseline does not reproduce; if any measured row contradicts the
  issued table in a way you cannot reconcile with the re-audit's finding; if any
  step would require changing executable logic; if a documented statement cannot be
  supported by a measurement, a code fact or an authority document, in which case
  delete the statement instead of hedging it; if Part A or Part B pins would move;
  if you conclude ADR-0085 needs an amendment; if context pressure reaches the
  point where a bounded rotation is cheaper than a degraded commit.

Completion: one additional commit, documentation and tests only, every documented
  statement traceable to evidence, the layer order and channel rule pinned by tests
  shown failing on violation, the value guard in place and shown failing, Part A
  and Part B unmoved, both routes green, tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `10_report_00.md` in
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
echoing `kronika-sole-identity`, session `10` and exchange `01` unchanged. Then:
the exact diff of every path; **a statement-by-statement table of every sentence
you wrote or changed, with its supporting evidence and its evidence class**; your
measured results for every row of the item-2 table, with any disagreement reported;
the before-and-after demonstration that the old docstring was false; the
demonstration that each new test fails when its property is violated; the
demonstration that the value guard fails when the constant changes; every Part C
movement with its cause; the proof that no executable logic changed; baseline and
final exact counts; the branch name and all four commit SHAs on this branch;
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
disclose it on the first line of the report body.

## Mandatory reading

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/09_report_00.md`,
  findings A1, A2 and A3 and the Also-assess items. A1 and A2 are your
  specification; A3 is explicitly not yours.
- `src/framenest/identity_env.py` in full, especially `lookup_env`,
  `lookup_field_value`, `folded_identity_environment` and
  `drop_identity_environment_spellings`.
- `src/framenest/configuration.py` around `_resolved_field_values` and the two
  dual-prefix source classes, to confirm what the layers actually do.
- `tests/contract/test_kronika_settings_parity.py` in full, especially `_spelled`.
- `docs/adr/0085-kronika-sole-identity.md` in full, to confirm it states no
  conflict rule and therefore is not contradicted.
- `tests/contract/test_kronika_identity_retention.py` in full.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md` Worker Execution section,
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real database, media path, profile or backup archive.

## Communication

Report text, docstrings and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator checks the statement-by-statement evidence table and
the no-executable-change proof. The Part C strengthening is the next separate
small grant and must be settled before C2's grant is written, because C3's
re-pin depends on it.