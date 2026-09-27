# Kronika one product — S4-A correction: preserve research configuration in AI CLI writers

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 28
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-S4-A-CLI-RESEARCH-PRESERVATION
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — mechanical localized fix with strong focused validation; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Fresh-session opening

This is a genuinely fresh Worker session; inherit no prior authority. This is
one smallest coherent correction for one confirmed finding inside the S4-A
row. No other change is authorized. The corrector never self-certifies;
independent acceptance follows. No subagents.

## Finding (confirmed, from `27_report_00.md` MEASURED)

`src/framenest/adapters/cli/ai.py` rebuilds `AiServerConfig` in four places
without the new `research` field, so a later media CLI configuration save
drops a stored research section. The administrator API already uses
`replace()` and preserves it. The four constructors are around lines 342
(`configure_provider_command`), 375 (`configure_non_interactive_command`),
449 (`provider_add_command`) and 518 (`provider_remove_command`) at the
baseline. `AiServerConfig` now has `research: ResearchConfiguration | None`.

## Starting state (verified read-only at issuance, 2026-09-26)

- FrameNest checkout `/home/agile/Projects/framenest`; branch
  `feat/kronika-one-product`; HEAD
  `75e9b07b2bf2269568382e28d40a8d2ff8d4bc28` (parent
  `72009c3b525b6a46e87223cb9a143b5079d89cbf`, tree
  `9f52d90790e4c1d0b37a6594d9c13071fa94a007`); clean index and worktree;
  local `main` = `origin/main` = `fd277a9…`; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- `private/**` is never read; no host, network or credential action.

## Goal

Preserve the stored research configuration across every AI CLI configuration
write, with a focused regression test. One commit.

## Exact mutation allowlist (baseline `75e9b07…`)

```text
src/framenest/adapters/cli/ai.py
tests/unit/adapters/cli/test_ai_cli.py
```

## Required change

In each of the four `AiServerConfig(...)` constructions in
`src/framenest/adapters/cli/ai.py`, carry the existing research
configuration forward: when a previously loaded configuration exists, pass
its `research` value; otherwise pass `None`. Do not change any other field,
default, message or control flow. Do not rename functions, alter the
interactive prompts, or touch the administrator API.

In `tests/unit/adapters/cli/test_ai_cli.py`, add a focused regression that:

- writes a configuration file containing a valid research section through the
  storage API,
- runs at least the non-interactive provider configuration writer and the
  provider add and remove writers (and, where the existing test harness makes
  it practical, the interactive writer) against that file,
- asserts after each save that the research section is still present and
  unchanged, and that the media provider selection and provider records are
  preserved,
- confirms that a configuration without a research section still saves
  without inventing one.

Extend existing tests; do not remove or weaken assertions.

## Step 0 — preconditions (fail closed)

- Verify physical root, branch, HEAD, parent, tree, clean index and worktree,
  local `main` = `origin/main` = `fd277a9…`, public `refs/heads/main` via
  `git ls-remote`, and the AP pin `7478ddb0…` (gitlink and `.ap` HEAD).
- Confirm the four constructors omit `research` at this baseline. Classify
  divergence with RF-12; stop on unexplained remainder.

## Declared execution route

From the repository root with the exact baseline:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 75e9b07b2bf2269568382e28d40a8d2ff8d4bc28

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 75e9b07b2bf2269568382e28d40a8d2ff8d4bc28 --operation test-focus -- tests/unit/adapters/cli/test_ai_cli.py tests/unit/infrastructure/ai tests/unit/test_import_boundaries.py -q -p no:cacheprovider
```

JavaScript tests: not-used — no JavaScript change. No ambient Python.

## Git and commit rules

Stage only the two allowlisted paths after reviewing the complete diff and
`git diff --cached --check`. Create exactly one local commit:

```text
fix(kronika): preserve research configuration in AI CLI writers
```

Do not push, fetch, tag, merge or rebase. Do not touch `.ap`, the managed
block, the ledger, `pyproject.toml`, `poetry.lock` or any migration.

## Authority and containment

Positive authority: read-only repository inspection; edits to the two
allowed paths; the declared route commands; one local commit; the terminal
report write at the exact destination when absent.

Negative authority: no other path; no schema, validator, API, adapter,
migration, dependency, packaging or configuration-state change; no network,
provider, credential, host, SSH, gate, sudo, service or browser action; no
`private/**`; no push/publication/deployment; no subagents.

## Stopping conditions

Stop and report on: baseline or topology drift; a required change outside the
two paths; an unusable declared route; a failing test that cannot be fixed
inside the allowlist; or any instruction conflict. Preserve the first causal
failure; do not improvise.

## Validation

Validation ladder: selected.
Inspection and provenance: required.
Existing focused tests: `tests/unit/adapters/cli/test_ai_cli.py`.
Affected tests: the declared selection.
New causal regression: the research-preservation test — the baseline drops
the section, so it fails before the correction.
Broad or full suite: not-used.
Runtime or testbed: not-used.
Independent acceptance: not-required for this correction; the row receives a
separate focused acceptance of the corrected candidate.

## Completion and report contract

`PASS` means the two-path change is committed with the declared route passing
and the regression failing on the baseline behavior in the reviewed diff.
`PARTIAL`/`BLOCKED` otherwise. Use `Phase-qualified result:
implementation-PASS` for PASS, otherwise `not-applicable`, and
`Logical-whole closure: not-closed`. `Report justification: new-mutation`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the exact
changed paths and constructor lines; the test evidence with counts; the
commit SHA, parent, tree and subject; post-commit status; unchanged AP pin,
managed block and ledger; deviations, risks and missing evidence; one
smallest next step (focused independent acceptance of the corrected S4-A
candidate); authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

The formal report is in English; the short completion notice to the
Cooperator is in Slovak, masculine address. Finalize the report, save it at
the exact destination, read it back in full, verify its first line,
coordinates, content and path, then send the separate short completion
notice with status, path and SHA-256. Do not run `sudo -v` or `sudo -K`.
Terminal report or cancellation expires this authority.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 28_correction_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 28_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
