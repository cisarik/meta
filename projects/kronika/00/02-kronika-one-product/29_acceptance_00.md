# Kronika one product — S4-A focused independent acceptance

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 29
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S4-A-CONTRACTS-ACCEPTANCE
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — focused independent acceptance of a shared AI configuration schema change and its cross-writer preservation correction; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: yes — required-fresh-independent

## Session and independence declaration

This must be a genuinely fresh session that did not implement or correct the
S4-A row. Declare your actual independence posture. Prior plans, reports and
trace evidence are evidence; inherited implementation reasoning is
disqualifying. You do not correct anything; findings are reported, never
fixed. Do not contact any host, call any provider or read credentials. Do not
ask for or receive prompts in another session.

## Acceptance and Correction Record

```text
Acceptance candidate: 40e51cb2d061ead96850c9c94aa59de54d5e1310
  (tree ec3c6c9db49ede4bfcd3616263b388bb26451834, branch feat/kronika-one-product,
   parent 75e9b07b2bf2269568382e28d40a8d2ff8d4bc28)
Acceptance owner map: the S4-A row delta against 72009c3b525b6a46e87223cb9a143b5079d89cbf
  (10 paths: the 8 implementation paths plus the 2-path CLI preservation
  correction); implementation report 27_report_00.md; correction report
  28_report_00.md; the accepted plan and ADR-0083
Acceptance allowlist: read-only review of the candidate and governing AP; the
  declared focused route; one declared temporary probe root under /tmp
Acceptance risk claims: the seven fixed claims below
Acceptance control matrix: the fixed positive and negative controls below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 1
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## Starting state (verified at issuance, 2026-09-26)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `40e51cb2d061ead96850c9c94aa59de54d5e1310`, parent
  `75e9b07b2bf2269568382e28d40a8d2ff8d4bc28`, tree
  `ec3c6c9db49ede4bfcd3616263b388bb26451834`; clean index and worktree; the
  row diff against `72009c3…` is exactly ten paths.
- Local `main` = `origin/main` = public `refs/heads/main` = `fd277a9…` (the
  S4-D documentation commit and the S4-A row are not yet published).
- Governing AP gitlink and `.ap` HEAD:
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- `AI_CONFIG_SCHEMA_VERSION` is 3; no real research adapter, network call,
  credential value, API or UI exists.
- `private/**` is never read. No host, SSH, gate, sudo, service, provider or
  credential action. Never print a secret-shaped value.

## Fixed claims

1. **Domain contracts.** `src/framenest/domain/research.py` provides the
   operation kinds, the non-terminal/terminal lifecycle states, the separate
   remote-cleanup and accounting states, the provider descriptor, the request
   and observation values, integer micro-USD usage values and the stable
   sanitized error codes; no error value carries raw provider text; the
   import-boundary test proves the domain tree stays framework-free.
2. **Application ports.** `src/framenest/application/ports/research.py`
   defines only the `ResearchProvider`, request-repository, budget-ledger and
   atomic-completion protocols and imports only the domain module.
3. **Registry and selection.** `research_registry.py` exposes
   `openai-responses` as unconfigured with search and research capabilities
   and an explicit not-guaranteed idempotency statement, `chatgpt-page` as
   parked and unavailable for new work, and a non-selectable self-hosted
   extension constant. Selection is a frozen server-side snapshot;
   `live_ready` is false; configuration is not live readiness; there is no
   fallback and no client-supplied endpoint, model or tool input; any fake
   provider exists only in tests.
4. **Configuration schema v3.** Version 3 accepts versions `{1, 2, 3}`;
   version 1 and 2 files read losslessly and are not rewritten by a read; an
   absent `research` section loads as disabled and is not invented on save;
   present research values are non-secret only; unknown, secret-shaped,
   endpoint and out-of-range values are rejected without echoing the
   submitted secret; future or non-integer versions remain rejected; saving
   preserves media provider selection and declared provider records.
5. **CLI preservation.** All four AI CLI configuration writers
   (`configure_command`, `configure_non_interactive_command`,
   `provider_add_command`, `provider_remove_command`) carry a previously
   loaded `research` value and pass `None` when no configuration was loaded;
   the added regression fails on the uncorrected baseline behavior and passes
   on the candidate; the administrator API is unchanged; no other field,
   prompt, message or control flow changed.
6. **Containment.** The row diff against `72009c3…` is exactly ten paths; no
   adapter, network use, credential value, API, UI, migration, dependency,
   packaging or configuration-state change; `.ap`, the managed block and
   `docs/AP_UPGRADE_OBSERVATIONS.md` are unchanged; nothing was pushed.
7. **Evidence honesty.** Live readiness, account access, price schedules and
   provider behavior are not claimed; the descriptor is `unconfigured`;
   research stays disabled by default; residual limitations are stated.

## Fixed control matrix

Positive controls (run independently from the repository root; report observed
counts and exit codes):

```text
git rev-parse HEAD 'HEAD^{tree}' 'HEAD^'
git diff --name-status 72009c3b525b6a46e87223cb9a143b5079d89cbf HEAD
git status --porcelain

./.ap/ap project check --root /home/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310 --operation test-focus -- tests/unit/adapters/cli/test_ai_cli.py tests/unit/infrastructure/ai tests/unit/test_import_boundaries.py tests/contract/test_ai_server_composition.py tests/contract/test_ai_provider_admin_api.py tests/contract/test_research_provider_contract.py -q -p no:cacheprovider
```

Negative and adversarial controls (bounded synthetic work under one declared
temporary root, e.g. `/tmp/kronika-one-product-s4a-acceptance`, mode 0700,
synthetic data only, cleaned up by you):

- Exercise the fake provider through every port method and observation class;
  confirm no outcome value can carry trusted HTML or raw provider text.
- Write synthetic configuration files for versions 1, 2 and 3 and for absent,
  present, malformed, secret-shaped, endpoint-bearing and out-of-range
  research sections; confirm accept/reject behavior and that rejection text
  never echoes a submitted secret; confirm future versions (including 999)
  stay rejected.
- Confirm a selection snapshot stays stable across a configuration change and
  that no fallback provider is selected.
- Confirm the parked provider is unavailable for new work and that the
  self-hosted constant is not selectable.
- Run the CLI preservation scenario with a present and with an absent
  research section through the four writers; confirm media selection and
  provider records are preserved and no research key is invented.
- Leak hunt over the ten-path diff: no endpoint field, no credential value,
  no adapter, no network import, no API/UI, no migration, no AP or
  dependency change.

State every observed result; unverified controls are reported as unverified,
never as PASS.

## Authority and containment

Positive authority: read-only inspection of the candidate and governing
`.ap`; the declared route; creation, use and cleanup of one declared
temporary probe root under `/tmp` (mode 0700, synthetic data only); the
terminal report write at the exact destination when absent.

Negative authority: no host, SSH, gate, sudo, service or browser action; no
provider call, credential value or network use; no product, test,
documentation, configuration, AP, packaging or migration edit; no correction;
no push or publication; no new dependency; no subagent; no Meta commit. Do
not read `private/**`, tokens or profiles.

## Stopping conditions

Stop with `PARTIAL` or `BLOCKED` on: identity or git-state mismatch; a route
that cannot run; a probe exceeding the authorized effects; sensitive output;
or a required control that cannot be established without a forbidden
mutation. Preserve the first causal failure; missing evidence is never PASS.

## Evidence selection and report delivery

Evidence tier: E2
Evidence tier basis: cross-cutting reversible contracts and a shared
configuration schema with focused independent contract review
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the declared route
Affected tests: the S4-A row delta and the AI configuration surface
New causal regression: none — this is acceptance
Broad or full suite: not-used
Runtime or testbed: declared route plus synthetic temporary probes; no host
Independent acceptance: required-separate-fresh-worker (this exchange)

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
Downloadable prompt filename: 29_acceptance_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 29_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

## Completion and report contract

`PASS` means every fixed claim is independently established and no blocking
finding remains. Use `Phase-qualified result: acceptance-PASS` only for a
PASS. Logical-whole closure stays `not-closed`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the
completed Acceptance and Correction Record; per-claim verdicts; the control
matrix with observed counts and exit codes; adversarial outcomes; findings if
any (full finding structure); containment and cleanup; residual risk and
limitations; one smallest next step (S6 records, access and approval);
`Report justification: final-acceptance`; authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

Direct communication with the Cooperator (the short completion notice) is in
Slovak, masculine address for him. This prompt and the formal report are in
English. Do not use subagents. Do not commit Meta artifacts. Finalize the
report, save it at the exact destination only if absent, read it back in full,
verify its first line/coordinates/content/path, then send the short separate
completion notice with status, exact path and SHA-256. Terminal report or
cancellation expires this authority.
