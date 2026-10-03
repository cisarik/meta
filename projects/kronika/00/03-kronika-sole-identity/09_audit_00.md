# Authoritative Worker prompt — Worker session 09, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `09`, exchange `01`. Stored under the
Meta filename mapping as `09_audit_00.md`, with report destination
`09_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 09
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Task identity: KSI-AUDIT-C1C — independent re-audit of correction C1c and of C1/C1b non-regression
Reasoning recommendation: High
Recommended context capacity: approximately 250k tokens
```

Rationale: this is an independent re-audit of a material correction on a
configuration trust boundary, and its central question — whether the parity
oracle is a *faithful* reference rather than a convenient one — is exactly the
kind of question that must not be answered affirmatively by reading intent. That
is a named-risk `High`. Not `Extra High`: no contradiction is unresolved, only
verification.

You are independent of sessions `05`, `06` and `08`. Their reports are **claims to
be tested**. Session `07` was an independent audit whose findings you are
re-checking; it is evidence about the *previous* state, not about this one.

This audit is read-only and **non-authorizing**. It cannot fix anything.

## Verified state under audit

```text
Repository checkout topology: standalone checkout
Expected branch: feat/kronika-identity-dual-read
Expected HEAD: 24bea56daca28603d81cac8d7ed7e3888ba90671
Expected subject: fix(identity): restore pre-cut process-environment parity for old spellings
Lineage on this branch:
  18c357c  published main, pre-C1 behaviour reference
  90c93ea  cut C1
  c02c675  correction C1b
  24bea56  correction C1c  (under audit)
Remote origin: https://github.com/cisarik/kronika
Public main: 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672
The branch is deliberately unpublished. Not publishing it is not a finding.
Working tree: clean
Containing-repository .ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS, governing variant stable
ap.project.conf projectId: cisarik/kronika, provenanceModule framenest
poetry.lock and pyproject.toml: byte-identical at 18c357c and at 24bea56
CPython: 3.13.9   pydantic-settings 2.14.2   Node: v26.8.2
Working directory: /home/agile/Projects/kronika
```

Measurements to reproduce or contradict, not to trust: Python
`4347 passed, 8 skipped, 3 warnings, 0 failed`; JavaScript
`554 total, 549 passed, 0 failed, 5 skipped`; `git diff c02c675..24bea56` empty for
every path outside `src/framenest/configuration.py`,
`src/framenest/identity_env.py`,
`src/framenest/infrastructure/runtime/development.py` and the three test files.

## What the correction claims

Restore exact pre-C1 behaviour for **old-spelling-only** process-environment and
environment-file input — case variants, explicitly empty, whitespace, invalid —
while keeping every C1 and C1b behaviour confirmed sound; stop the development
launcher from manufacturing a conflict in the environment it hands to the server
it spawns; and add a mandatory differential parity regression.

## Priority 1 — is the oracle a faithful reference?

This is the first thing to check, and getting it wrong invalidates the entire
correction's evidence.

- The oracle is claimed to be the library's own
  `BaseSettings.__dict__["settings_customise_sources"]`, patched onto the project
  class, so the library builds its own stock `EnvSettingsSource` and
  `DotEnvSettingsSource`. Verify that is what actually happens, and that no
  project dual-prefix class participates.
- Does patching the hook faithfully reproduce the pre-C1 path, or does it differ
  from `git show 18c357c:src/framenest/configuration.py` in any way that matters?
  The pre-C1 file had no override at all; prove the patched hook is equivalent to
  having no override, for every relevant input class, not only the tested ones.
- Does `test_the_settings_library_is_unchanged_since_the_restoration_reference`
  genuinely enforce its licence, or can it pass while the oracle is invalid? Try
  to construct a situation where the lockfile differs and the test still passes.
- Is the oracle ever used in a way that makes the test **tautological** — for
  example comparing the implementation against something derived from the
  implementation?

## Priority 2 — does the parity test actually catch the defects?

- The correction claims three in-memory reversions produced 773, 742 and 773
  mismatches. Reproduce them. A parity test never shown failing is not evidence.
- Does the test detect F1 and F2 **separately**, not merely their union?
- The test compares built settings via `model_dump` with `SecretStr` unmasked, and
  compares failure **type plus sorted field locations**, deliberately not
  messages, because the library embeds the source class name in `SettingsError`
  text. Judge whether that carve-out hides anything material. Could a regression
  be invisible because it changes only a message?
- The matrix sets **one variable at a time**. Identify precisely which
  simultaneous combinations are therefore uncovered, and whether any of them
  changed behaviour in C1, C1b or C1c. The claim is that only the prefix pairs
  did, and that those have dedicated tests. Verify or refute it.
- Is the 2340-comparison count honest, and does the test actually build settings
  twice per comparison?
- Does the test depend on `git show` reaching the reference commit, and does it
  fail loudly rather than silently weakening if the commit becomes unreachable?

## Priority 3 — the declared divergence

`KRONIKA_PORT=9998` together with `framenest_port=9999` resolves to 9998 with no
conflict raised, because the conflict rule is case-exact. This is declared as a
correct trade: the input contains the new spelling, so it is not
old-spelling-only, and making the conflict rule case-insensitive is forbidden.

- Independently judge whether that trade is safe. Specifically: can a case variant
  of the compatible spelling be used to **evade** a value the identity spelling
  selected, in any entry point, including the development launcher?
- Can a case variant of the **identity** spelling interact badly with layer
  ordering, for example shadowing or being shadowed in a way that was not analysed?
- Is "the input contains the new spelling, so it is not old-spelling-only" a
  sound argument, or a convenient one?

## Priority 4 — non-regression of everything C1 and C1b established

Session `07` confirmed these at `c02c675`. Re-establish them at `24bea56`, because
a correction can silently undo an audited property:

- the mutation gate accepts both header spellings, rejects absent, wrong-valued,
  duplicate and both-present-with-one-wrong, and old-only requests behave
  bit-for-bit as before C1;
- `lookup_env` remains the single case-exact conflict authority, called
  unconditionally before any value-selection layer, and no conflict path returns a
  partial result or leaks a value;
- a conflict still exits 2 at every enumerated in-package entry point, with a
  suffix-only message and no traceback;
- **writer invariance**: no newly written durable artifact, emitted error code or
  sent header uses a `KRONIKA_` spelling;
- the installed `/etc/framenest/framenest.env` shape still works, and every
  `EnvironmentFile=` key style that worked before still works;
- `hide_input_in_errors`, `extra="ignore"`, `env_file_encoding`, the retained
  `env_prefix="FRAMENEST_"` and process-over-environment-file precedence are
  intact.

## Priority 5 — the launcher normalisation

- `drop_identity_environment_spellings` mutates the mapping in place and deletes
  every case variant of both prefixes for the given suffixes. Can it remove too
  much, too little, or something a different setting needs? Consider suffix
  relationships and any name that differs only by case between two settings.
- With a conflicting or case-variant parent environment, does the spawned child
  now receive exactly one name per injected suffix and build settings from the
  launcher's resolved values?
- The claim is that `development.py` is the **only** place in `src/framenest` that
  builds a child environment containing an identity-prefixed name, and that the
  launcher injects **three** names, not four. Verify both by enumeration, not by
  reading the report.

## Priority 6 — the retention ledger, and the C3 decision

Session `07` established that Part C pins **scalars**, so a cut that renames some
things and re-pins a scalar to match partial work **passes**, and a genuinely
missed rename can survive until C7.

- Are the six Part C movements reported by C1c arithmetically honest? Recompute
  them independently.
- Confirm Part A and Part B did not move.
- Give a decision the Orchestrator can act on: **must Part C be strengthened
  before C3, and if so, what exactly should it pin?** C3 moves every file to
  `kronika.*` and changes the ledger's own `src/*/…` glob, so a full re-pin is
  required. A scalar that must be re-pinned wholesale at the one cut where the
  rename actually happens is close to useless before that cut. Propose the
  smallest change that makes a partial rename detectable at the cut that owns it.

## Also assess, do not rediscover

- The reported redundant work: `_settings_init_sources` builds the stock sources
  at HEAD and `settings_customise_sources` then discards them, so every settings
  build folds `parse_env_vars(os.environ)` twice. Confirm it is a performance
  observation and **not** a correctness one, and say whether it matters at the
  observed scale.
- The parity test references `FrameNestSettings` by name and will need the C3
  rename. Confirm that is a mechanical rename and not a hidden coupling.

## Authority

```text
Positive authority: read-only inspection inside /home/agile/Projects/kronika at
  24bea56daca28603d81cac8d7ed7e3888ba90671, including .ap at its pinned commit;
  read-only public verification of https://github.com/cisarik/kronika.git;
  read-only Git inspection and diffing across 18c357c, 90c93ea, c02c675 and
  24bea56; execution of the declared AP test operations, including focused runs and
  at most one full Python suite run and one JavaScript route run; running installed
  console scripts as subprocesses to observe real exit statuses and output, under
  `env -i` with synthetic values and `HOME`/`TMPDIR` under /tmp, so nothing
  outside /tmp is written and no real database, credential, media path or profile
  is touched; writing throwaway probe scripts and in-memory monkeypatches under
  /tmp only.

Negative authority: any file edit, create, move, rename or deletion inside
  /home/agile/Projects/kronika, including any test file; any write to
  /home/agile/meta; any Git write of any kind — no add, commit, branch, tag,
  merge, rebase, stash, checkout, switch, reset, clean or push; any dependency
  install, update or lockfile change; any NUC contact, including SSH, the NUC
  worker gate, and deploy/ubuntu/framenest-release in every mode; any
  deploy/systemd, package-manager, systemd, AppArmor, UFW, Tailscale, mount or
  storage operation; any provider or capture-browser contact; any execution of a
  kronika-capture command; any reading of private/, personal Fish configuration,
  browser profiles, cookies, tokens, credential stores, .secrets or
  ~/.config/opencode; any reading of a real database, real media, a real credential
  drop-in or a real backup archive; any remediation of any finding.

Commands: Python evidence goes only through the canonical declared route,
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  24bea56daca28603d81cac8d7ed7e3888ba90671 --operation <id> -- <argv>`, with
  operations declared in ap.project.conf, plus `./.ap/ap project check --root
  /home/agile/Projects/kronika --baseline
  24bea56daca28603d81cac8d7ed7e3888ba90671`. JavaScript tests use the declared
  `node --test` route. Never invoke `.venv/bin/python`, `python`, `python3` or
  `poetry run` for evidence — including as a text editor. Library sources under
  `.venv/…/pydantic_settings/` are read with the read tool, never imported by a
  hand-launched interpreter. Read-only Git inspection is allowed (`git status`,
  `git rev-parse`, `git log`, `git show`, `git diff`, `git ls-files`, `git grep`,
  `git ls-remote`, `git submodule status`, `git merge-base`, `git cat-file`); no
  other Git command. Any other command must be stated in the report with its
  purpose and a confirmation that it mutated nothing.

Dependency authority: none.

Git authority: read-only inspection and diffing only.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none. Use only synthetic values. Never print, quote or summarize
  a real secret value, host identifier, address, disk serial, UUID or SSH
  fingerprint.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope; the
  accepted plan and the prior sessions' reports are **claims under audit**, not
  authority. If the implementation and the plan disagree, that is a finding. On
  conflict between retained context and current repository evidence, stop.

Side-effect authority: authorized read-only only, plus throwaway files under /tmp.

Browser authority: none. No browser, and no capture command.
```

## Evidence

```text
Validation: reproduce or contradict every measurement given above. Attack the
  oracle, the parity test and the ledger the way session 07 attacked the gate.
  For each finding, state the exact reproduction, observed, expected and smallest
  correction. Distinguish a confirmed defect, an accepted deviation with a
  residual risk, a hardening opportunity, and a question needing an Orchestrator or
  Cooperator decision.

Evidence tier: this re-audit is the gate before C2 and before publication. Its
  output is a finding set, not a mutation.
```

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the branch is not at 24bea56; if any step would require a mutation
  inside the repository; if a probe would touch a real database, credential, media
  path, profile or capture browser; if a finding is a genuine cross-cutting
  contradiction needing a Cooperator or Orchestrator decision; if context pressure
  reaches the point where a bounded rotation is cheaper than a degraded audit.

Completion: one terminal report containing the complete finding set, whether or
  not it is empty.

Required report sections: the standard report core and the exact header
  `### Report for ORCHESTRATOR_CHAT`, echoing `kronika-sole-identity`, session
  `09` and exchange `01` unchanged; the repository gate result; which given
  measurements you reproduced and which you contradicted; a findings table with
  severity, exact reproduction, observed, expected, smallest correction, and
  whether the finding blocks acceptance of C1c; an explicit verdict per priority
  area, including whether the oracle is faithful and whether the parity test is
  sound; your independent recomputation of the six ledger movements; your
  actionable decision on strengthening Part C before C3; your judgement on each
  Also-assess item; the highest-value missing test; and one smallest next step.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `09_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this
  prompt expires. No remediation, no push, no publication, no NUC refresh and no
  later cut is authorized by it, whatever the findings say.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none, by design
```

Report justification: exactly one of `new-evidence`, `new-material-risk`,
`new-mutation`, `changed-external-state`, `final-acceptance`, `explicit-closure`.
The expected value is `new-evidence` or `new-material-risk`. `new-mutation` is
invalid for this prompt.

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
  the accepted independent audit. F1, F2, F4 and the Part C finding are the
  specification that C1c had to satisfy.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/08_report_00.md`
  and `06_report_00.md` and `05_report_00.md` — as **claims under audit**.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/03_report_00.md`,
  the accepted plan, C1 and C2.
- `docs/adr/0085-kronika-sole-identity.md` in full.
- The complete `18c357c..24bea56` diff, and `c02c675..24bea56` separately. The
  primary object of the audit is the latter; the former is the non-regression base.
- `git show 18c357c:src/framenest/configuration.py` — the behaviour being restored.
- `src/framenest/identity_env.py` in full, especially `lookup_env`,
  `lookup_field_value`, `folded_identity_environment` and
  `drop_identity_environment_spellings`.
- `src/framenest/configuration.py` in full, especially the two dual-prefix source
  classes, `_resolved_field_values`, `_identity_suffix` and `settings_customise_sources`.
- `tests/contract/test_kronika_settings_parity.py` in full.
- `tests/contract/test_kronika_identity_retention.py` in full.
- Library sources, read with the read tool: `pydantic_settings/main.py`,
  `sources/base.py`, `sources/providers/env.py`, `sources/providers/dotenv.py`.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md` Worker Execution section,
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §12, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real database, media path, profile or backup archive.

## Communication

Report text is professional English. Do not use Czech or Slovak.

## Orchestrator acceptance note

This re-audit is the gate before C2 and before publication of the branch. A
confirmed trust-boundary or parity defect sends the work back to a bounded
correction; the Part C strengthening is a separate small decision that must be
settled before C3's grant is written. Publication of the branch and the routine NUC
refresh each remain separate bounded grants regardless of the outcome.