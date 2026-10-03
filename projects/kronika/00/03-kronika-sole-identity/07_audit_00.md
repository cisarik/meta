# Authoritative Worker prompt — Worker session 07, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `07`, exchange `01`. Stored under the
Meta filename mapping as `07_audit_00.md`, with report destination
`07_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 07
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Task identity: KSI-AUDIT-C1 — adversarial audit of cuts C1 and C1b
Reasoning recommendation: High
Recommended context capacity: approximately 250k tokens
```

Rationale: the audited cut widened a mutation-authorization boundary and
introduced a fail-closed resolver over 639 environment variables. Finding a real
defect here matters more than the cost of the audit, and the audit must reason
adversarially about trust boundaries rather than confirm the implementation's
intent. `High` is the named-risk profile for a security boundary. Not `Extra
High`: there is no unresolved contradiction here, only adversarial verification.

You are independent of the sessions that implemented this state. Sessions `05`
and `06` are not your evidence; their reports are claims to be tested. **You must
not treat a passing test suite as proof.** A test and the behaviour it asserts can
share a wrong assumption. Where you can construct an independent check that does
not reuse the implementation's own helpers, prefer it, and say which checks were
independent and which reused existing coverage.

This audit is read-only and **non-authorizing**. It cannot fix anything. Its only
product is a truthful report.

## Verified state under audit

```text
Repository checkout topology: standalone checkout
Expected branch: feat/kronika-identity-dual-read
Expected HEAD: c02c6753694d5d4958045bb79f80b5eb94b9c75c
Expected subject: fix(identity): exit 2 on an identity-environment conflict at every entry point
Parent of HEAD: 90c93eac94171182039a76fbb1c956e42b44da2c   (cut C1)
Base of both cuts: 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672   (published main)
Remote origin: https://github.com/cisarik/kronika
Public main: 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672
The branch is deliberately unpublished. Not publishing it is not a finding.
Working tree: clean
Containing-repository .ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS, governing variant stable
ap.project.conf projectId: cisarik/kronika, provenanceModule framenest
CPython: 3.13.9   pydantic-settings 2.14.2   Poetry: 2.3.2   Node: v26.8.2
Working directory: /home/agile/Projects/kronika
```

Measurements the Orchestrator took at `c02c675…`, for you to reproduce or
contradict, not to trust:

```text
Python --operation test: 4314 passed, 8 skipped, 3 warnings, 0 failed
JavaScript node --test tests/*.test.js: 554 total, 549 passed, 0 failed, 5 skipped
git diff 90c93ea..c02c675 is empty for ap.project.conf, pyproject.toml, deploy/**,
  deploy/systemd/**, docs/**, root Markdown files, src/kronika_capture/**,
  the 36 applied Alembic revision files, and
  src/framenest/adapters/api/tailscale_ingress.py
git diff 18c357c..c02c675 KRONIKA_ occurrences added outside tests: exactly three
  code tokens, all read-side prefix constants
```

## What the audited cuts claim

State the claims, then test each one.

- **C1**: one resolver reads `KRONIKA_<SUFFIX>` and `FRAMENEST_<SUFFIX>`;
  exactly one set wins, both unset yields the caller default, both set and equal
  is accepted, both set and different **fails closed** with suffix-only messages
  and never a value; an empty string behaves as unset; the mutation gate accepts
  both header spellings; durable-artifact readers accept both spellings; **no
  writer emits a `KRONIKA_` spelling**; the installed
  `/etc/framenest/framenest.env` shape keeps working.
- **C1b**: a conflict exits **2** at every in-package entry point that can
  surface it; no other exit status changed; no traceback is reachable from a
  conflict.

## Audit scope — attack these, do not merely re-read them

### 1. The mutation-authorization boundary

This is the highest-consequence surface. C1 widened it.

- Can any request reach a mutation **without** a header carrying exactly the
  expected value? Consider: absent header; wrong value; duplicate header of one
  spelling; both spellings present with one wrong; both present and correct;
  case variations in the header name; a header name with trailing whitespace;
  multiple values folded into one comma-joined line; the header arriving on a
  route that never had the gate; and the gate's own helper `_single_value`
  returning `None` for a multi-valued header, which is indistinguishable from
  absent at the call site.
- Did accepting a second spelling change the gate's behaviour for any request
  that the **old** spelling alone would have handled? The old behaviour must be
  bit-for-bit preserved for old-only requests.
- Did anything leak into an origin, CORS, companion-origin or trusted-header
  list that was not there before? Verify by diffing those lists, not by reading
  comments.
- Is the new spelling reachable in a path that bypasses ingress provenance?

### 2. The fail-closed resolver

- Is there **any** conflict path that returns a partial result, silently prefers
  one value, or falls through to a default? Try to construct one.
- Can a value escape through a message, a log record, an exception `repr`, a
  traceback, an audit event, a structured-logging field, a subprocess argument,
  or a test snapshot? Check the structured logging path, not only `print`.
- Case sensitivity: `lookup_env` is case-exact while
  `canonical_identity_environment` upper-cases keys, because the library
  lower-cases environment-file keys. Can a mixed-case environment-file key or a
  mixed-case process variable produce a different outcome from the equivalent
  upper-case one? Is that difference a defect or an accepted narrowing?
- Whitespace-only values: an all-whitespace value is not the empty string. Is its
  treatment identical to the pre-C1 behaviour under `env_prefix`?
- Does every reader that can surface a conflict actually route through the
  resolver, including any `environ` mapping callers and the
  `public_published_application` path?
- Does the resolver's exception type hierarchy create any import cycle risk or
  any partially-initialised module path at interpreter start?

### 3. The stdlib-only mirrors

Two deploy engines cannot import the package and therefore mirror the resolver.
- Are the three copies semantically equivalent **including edge cases**: empty
  string, whitespace, case, conflict detection, conflict message content, and
  the exit status?
- Can they drift, and what is the concrete divergence that a future edit to one
  copy could introduce? Name it.
- Does a mirror's conflict path leak a value where the package one would not?

### 4. Writer invariance

- Independently establish that no newly written durable artifact, emitted error
  code, or sent header uses a `KRONIKA_` spelling. Do this by enumerating write
  sites, not by trusting a grep count.
- Confirm `PROTOCOL_MAGIC` `FNCBE01`, `version("framenest")`,
  `DEVELOPMENT_DATABASE_DIRECTORY`, the emitted `FRAMENEST_*` code strings, and
  the injected `env FRAMENEST_ENV_FILE=` are all unchanged from `18c357c`.
- Check whether anything the **installed NUC** will read is now unreadable, or
  anything it will write now unreadable by the currently installed release.

### 5. The exit-status claim

- Independently verify that **no exit status other than the conflict status**
  changed between `18c357c` and `c02c675`, at every entry point, for ordinary
  success, ordinary failure, and invalid invocation.
- Assess this known collision independently and do not rubber-stamp it: ten entry
  points already returned 2 for an ordinary usage error before C1b, so exit 2 does
  not uniquely identify a conflict. Search the repository for anything that
  branches on exit status, and state whether the collision can mislead any real
  caller, script, test, systemd unit, or operator runbook.
- Assess this known deviation independently: `_database_state` in
  `infrastructure/runtime/development.py` still swallows a conflict and reports
  `unknown`. Decide whether that is acceptable and what could still go wrong.

### 6. The retention ledger's actual value

- Are the pins enforcing what they claim, or is any of them tautological — that
  is, derived from the same source it is supposed to police?
- The ledger counts **every occurrence of the product word**, including in
  ordinary code such as an import line. Sessions `05` and `06` report holding
  counters fixed partly by extending existing import statements rather than
  adding new ones. Assess whether the ledger is now creating pressure to distort
  code to match a metric, and whether cut C3 will need it re-pinned.
- Would a genuinely missed rename actually fail at the cut that owns it, or could
  it survive to the end?

### 7. Scope compliance and unexamined risk

- Did either cut modify anything outside its authorized surface? Check the full
  `18c357c..c02c675` diff against the accepted plan
  `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/03_report_00.md`
  and the issued prompts `05_implementation_00.md` and `06_correction_00.md`.
- What is materially untested? Name the highest-value missing test.

## Known and already accepted — assess, do not rediscover as new

These were disclosed by the implementing sessions and accepted by the
Orchestrator. Your job is to judge whether they matter, not to report them as
novel:

- `env_prefix="FRAMENEST_"` was deliberately **retained** as the library's
  internal key spelling instead of being replaced, because `env_prefix=""` would
  make bare ambient names such as `PORT` or `HOSTNAME` become application
  configuration. Judge whether the retained prefix creates any other exposure.
- `EXIT_IDENTITY_ENVIRONMENT_CONFLICT` is consumed at exactly one place; the two
  mirrors keep their own constant.
- `_database_state` swallowing a conflict, as described in scope 5.
- The exit-2 collision, as described in scope 5.
- The retention ledger's counter pressure, as described in scope 6.

## Authority

```text
Positive authority: read-only inspection inside /home/agile/Projects/kronika at
  c02c6753694d5d4958045bb79f80b5eb94b9c75c, including .ap at its pinned commit;
  read-only public verification of https://github.com/cisarik/kronika.git;
  read-only Git inspection and diffing across 18c357c, 90c93ea and c02c675;
  execution of the declared AP test operations, including focused runs and at
  most one full Python suite run and one JavaScript route run; running installed
  console scripts as subprocesses to observe real exit statuses and real output,
  using synthetic values and hermetic temporary roots so that nothing outside
  /tmp is written and no real database, credential, media path or profile is
  touched; writing throwaway probe scripts under /tmp only.

Negative authority: any file edit, create, move, rename or deletion inside
  /home/agile/Projects/kronika, including any test file; any write to
  /home/agile/meta; any Git write of any kind — no add, commit, branch, tag,
  merge, rebase, stash, checkout, switch, reset, clean or push; any dependency
  install, update or lockfile change; any NUC contact, including SSH, the NUC
  worker gate, and deploy/ubuntu/framenest-release in every mode; any
  deploy/systemd, package-manager, systemd, AppArmor, UFW, Tailscale, mount or
  storage operation; any provider or capture-browser contact; any execution of a
  kronika-capture command; any reading of private/, personal Fish configuration
  including ~/.config/fish/** and fish_variables, browser profiles, cookies,
  tokens, credential stores, .secrets, or ~/.config/opencode; any reading of a
  real database, real media, a real credential drop-in, or a real backup archive;
  any remediation of any finding.

Commands: Python evidence goes only through the canonical declared route,
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  c02c6753694d5d4958045bb79f80b5eb94b9c75c --operation <id> -- <argv>`, with
  operations declared in ap.project.conf, plus `./.ap/ap project check --root
  /home/agile/Projects/kronika --baseline
  c02c6753694d5d4958045bb79f80b5eb94b9c75c`. JavaScript tests use the declared
  `node --test` route. Never invoke `.venv/bin/python`, `python`, `python3` or
  `poetry run` for evidence. Read-only Git inspection is allowed (`git status`,
  `git rev-parse`, `git log`, `git show`, `git diff`, `git ls-files`, `git grep`,
  `git ls-remote`, `git submodule status`, `git merge-base`, `git cat-file`); no
  other Git command. Running an installed console script under `.venv/bin` is
  permitted for observing exit status and output; state each such invocation and
  confirm it wrote nothing outside /tmp. Any other command must be stated in the
  report with its purpose and a confirmation that it mutated nothing.

Dependency authority: none.

Git authority: read-only inspection and diffing only. No branch creation, no
  staging, no commit, no push.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none. Use only synthetic values you invent. Never print, quote
  or summarize a real secret value, host identifier, address, disk serial, UUID
  or SSH fingerprint.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope; the
  accepted plan and the implementing sessions' reports are **claims under audit**,
  not authority. If the implementation and the plan disagree, that is a finding.
  On conflict between retained context and current repository evidence, stop and
  report.

Side-effect authority: authorized read-only only, plus throwaway files under /tmp.
  No reversible local repository mutation, no destructive mutation, no remote
  effect, no deployment, no credential effect, no billing effect.

Browser authority: none. No browser, and no capture command.
```

## Evidence

```text
Validation: reproduce or contradict every measurement given above. Run the audit
  scope as adversarial probing, not as a walkthrough. For each finding, state the
  exact reproduction, the observed behaviour, the expected behaviour, and the
  smallest correction. Distinguish a confirmed defect, an accepted deviation with
  a residual risk, a hardening opportunity, and a question that needs an
  Orchestrator or Cooperator decision.

Evidence tier: this audit supplies the independent evidence for accepting an E2
  cut that widened a trust boundary, and it is the gate before C2. Its own output
  is a finding set, not a mutation.
```

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the branch is not at c02c675; if any step would require a mutation
  inside the repository; if a probe would touch a real database, credential,
  media path, profile or capture browser; if a finding is a genuine
  cross-cutting contradiction needing a Cooperator or Orchestrator decision
  rather than an audit finding; if context pressure reaches the point where a
  bounded rotation is cheaper than a degraded audit.

Completion: one terminal report containing the complete finding set, whether or
  not it is empty.

Required report sections: the standard report core and the exact header
  `### Report for ORCHESTRATOR_CHAT`, echoing `kronika-sole-identity`, session
  `07` and exchange `01` unchanged; the repository gate result; which given
  measurements you reproduced and which you contradicted; a findings table with
  severity, exact reproduction, observed, expected, smallest correction and
  whether the finding blocks acceptance of C1 or C1b; an explicit statement per
  audit-scope area of what you probed and what you could not probe; your
  independent judgement on each known-and-accepted item; the highest-value
  missing test; and one smallest next step.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `07_report_00.md` in
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

- `.ap/AP.md` at the pinned commit, §5 Task Authority, §9 Git and Remote Safety,
  §10 Security Boundaries, §12 Validation and Public Verification, §13 Artifact
  Lifecycle.
- `.ap/AP_WORKER.md` in full.
- `AGENTS.md` at the repository root, especially the Worker Execution section,
  and the managed AP integration block boundaries.
- `docs/WORKER_EXECUTION_CONTRACT.md`.
- `docs/adr/0085-kronika-sole-identity.md` in full — the authority under which
  this behaviour is intended.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/03_report_00.md`,
  the accepted plan, cuts C1, C2, C5 and C6, as the specification to audit against.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/05_report_00.md`
  and `06_report_00.md` — as **claims under audit**, not as evidence.
- The complete `18c357c..c02c675` diff, which is the primary object of the audit.
- `src/framenest/identity_env.py` in full, and
  `src/framenest/configuration.py` around the settings source and the error
  translation sites.
- `src/framenest/adapters/api/tailscale_ingress.py` around the mutation gate and
  `_single_value`.
- `deploy/ubuntu/framenest_release.py` and `deploy/ubuntu/production_ai_deploy.py`
  mirror sections.
- `tests/contract/test_kronika_identity_retention.py` in full.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real database, media path, profile or backup archive.

## Communication

Report text is professional English. Do not use Czech or Slovak.

## Orchestrator acceptance note

This audit is the gate before C2. A confirmed trust-boundary defect sends the work
back to a bounded correction; a hardening opportunity is triaged, not auto-applied;
a Cooperator decision is escalated. Publication of the branch and the routine NUC
refresh each remain separate bounded grants regardless of the audit outcome.