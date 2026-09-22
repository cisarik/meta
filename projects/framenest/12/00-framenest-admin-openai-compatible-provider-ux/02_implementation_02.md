# Correction Exchange 02 — Session 02 — Settings Validator Accepts Declarative Provider Ids

Persistent role identity: WORKER
Logical whole identity: framenest-admin-openai-compatible-provider-registry-and-vision-probe
Worker session ordinal: 02
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Implementation
Task identity: CORRECT-SETTINGS-PROVIDER-ID-VALIDATOR
Implementation authority: explicit (one confirmed defect, exact paths, one corrective commit)
Delivery route: Agent Orchestrator default dispatch into the same session (continuity anchor below)
Reasoning recommendation: Medium — a small, exactly specified validator correction with focused tests; the slice-1 context is retained
Recommended context capacity: approximately 250k tokens
Independence required: no
Sub-agents or internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active

## Continuity anchor and authority renewal

Continuity anchor: your terminal PARTIAL report for exchange 01
(`/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/02_report.md`)
and your local commit `f41df797d74ddd0a54c6c0d31f995bda8a8a4661`. Prior authority
expired at that report. This is a complete renewed grant for one bounded
correction. Retained context is convenience, not authority; if retained context
conflicts with current repository evidence, current repository evidence wins —
stop and report the conflict. Evidence produced in this exchange is
non-independent (same session).

Why reuse: the session is healthy, the assumptions are unchanged, the
correction is a direct continuation of the confirmed finding, and no
independence is required.

## Confirmed finding (why this exchange exists)

Your exchange-01 report §8 finding 1, independently confirmed by the
Orchestrator: `src/framenest/configuration.py` still validates
`FrameNestSettings.ai_provider_id` against the retired two-id enum
(`SUPPORTED_AI_PROVIDER_IDS` at line 53; validator at lines 372-380), so
`FRAMENEST_AI_PROVIDER_ID` cannot name a declared provider end-to-end. That
contradicts the accepted plan's D5 sentence "declared ids are valid in the
environment override".

## Exact correction scope

1. In `src/framenest/configuration.py`, replace the enum membership check on
   `ai_provider_id` with a bounded syntax validation equal to the declared
   provider id rule used by `provider_records.py`
   (`^[a-z0-9][a-z0-9._-]{0,63}$`, normalized with `.strip()`), so any
   syntactically valid built-in or declared id is accepted at settings
   construction. Do not import infrastructure modules into this file; keep
   the rule local. The built-in ids already match this rule.
2. Remove `SUPPORTED_AI_PROVIDER_IDS` only after verifying no other source or
   test imports it; if an importer exists, keep the constant unchanged and
   only stop using it in the validator.
3. Do not change any other validator, default, field, or behavior in the
   file. `ai_model_id` bounds and everything else stay exactly as they are.

## Changed-path allowlist

```text
src/framenest/configuration.py
tests/unit/test_configuration.py
tests/unit/infrastructure/ai/test_registry.py
```

No other file may be created, edited, deleted, or moved.

## Tests

1. `tests/unit/test_configuration.py`: a declared id such as `opencode-go`
   is accepted by `FrameNestSettings(...)` / the environment override path;
   a syntactically invalid id (for example `OpenCode!`) is rejected with the
   sanitized configuration error; built-in ids keep working.
2. `tests/unit/infrastructure/ai/test_registry.py`: replace the
   `model_copy` workaround for the "environment override to a declared
   provider" case with a normally constructed settings object, proving the
   override end-to-end at the settings boundary; keep the other cases
   unchanged.
3. Re-run the full slice-1 selection once on the corrected candidate.

## Commands (canonical execution route — binding)

```text
./.ap/ap ap project check --root /home/agile/Projects/framenest --baseline f41df797d74ddd0a54c6c0d31f995bda8a8a4661
./.ap/ap ap exec --root /home/agile/Projects/framenest --baseline f41df797d74ddd0a54c6c0d31f995bda8a8a4661 --operation runtime-info
./.ap/ap ap exec --root /home/agile/Projects/framenest --baseline f41df797d74ddd0a54c6c0d31f995bda8a8a4661 --operation test-focus -- tests/unit/infrastructure/ai tests/unit/adapters/cli/test_ai_cli.py tests/contract/test_ai_server_composition.py tests/contract/test_production_ai_deployment.py tests/contract/test_automatic_analysis_settings_api.py tests/unit/test_configuration.py -q -p no:cacheprovider
```

## Repository gate

Re-verify before editing: HEAD equals `f41df797d74ddd0a54c6c0d31f995bda8a8a4661`
(the Orchestrator-authorized baseline for this correction), porcelain clean,
branch `feat/x-meme-browser-companion`, `.ap` gitlink unchanged and
`./.ap/ap ap doctor` PASS. Stop on any unexplained difference.

## Authority

Positive: edit only the allowlisted paths; run the declared route and
read-only Git commands; stage exactly those paths; one corrective commit
with subject `Accept declarative provider ids in settings environment override`;
no push. Write exactly the Meta report below.

Negative: everything outside the allowlist; any other Git write; any network,
provider, NUC, SSH, sudo, browser, GUI, environment-reconstruction, or
secret-access action; no documentation or ADR changes; no weakening or
deleting an existing test; no `git add .`/`-A`.

## Meta persistence contract (execute exactly)

```text
Meta persistence owner: this Worker, for the single report path named below.
Prompt persistence owner: ORCHESTRATOR (already written; do not rewrite it).
Exact report destination: /home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/02_report_02.md
Write the complete terminal report to that path after the work, then verify
byte identity. Do not create other Meta files. Do not rename. Do not commit
Meta Git. Do not commit FrameNest unless this prompt grants FrameNest Git.
If the path already contains a terminal report, STOP (PARTIAL) — do not
overwrite.
The Cooperator must not be asked to create, paste, or rename files.
```

## Report contract

Begin exactly with `### Report for ORCHESTRATOR_CHAT`; echo these
coordinates once (`Worker session ordinal: 02`, `Worker exchange ordinal: 02`);
include the compact core: status PASS/PARTIAL/BLOCKED; phase-qualified result
`implementation-PASS` on PASS else `not-applicable`; start commit
`f41df79…`; end commit (corrective commit SHA); changed files; tests and
validation with exact counts; commit result; deviations/risks; one smallest
next step; `Report justification: new-mutation`; authority-expiry statement;
`Orchestration critique` (MEASURED/LEAD); Resolved Execution Issues /
Near-Misses and Pre-Existing Failure Classification; `Logical-whole closure:
not-closed`. Save, read back fully, verify identity, then a short separate
completion notice with location and SHA-256.

## Stopping conditions

Stop and report BLOCKED or PARTIAL when a gate fails or differs
unclassifiably, a needed change exceeds the allowlist, an existing test must
be weakened to pass, the execution route is unusable, the Meta destination is
occupied or unsafe, or retained context conflicts with repository evidence.

Authority expiry: this terminal report ends the correction grant; no
autonomous continuation.
