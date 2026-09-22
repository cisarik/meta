# Bounded Correction Exchange 07 — Session 02 — `vision_input` Refusal on the Analyze Paths

Persistent role identity: WORKER
Logical whole identity: framenest-admin-openai-compatible-provider-registry-and-vision-probe
Worker session ordinal: 02
Worker exchange ordinal: 07
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Implementation
Task identity: CORRECT-ANALYZE-VISION-CAPABILITY-REFUSAL
Implementation authority: explicit (one confirmed finding, exact paths, one corrective commit)
Delivery route: Agent Orchestrator default dispatch into the same session (continuity anchor below)
Reasoning recommendation: High — named risk: the correction implements a normative SPEC §22/ADR-0081 sentence on the Analyze boundary; the refusal must be exactly scoped, must not change classify/accounting semantics for real provider failures, and must not break existing analyze tests
Recommended context capacity: approximately 250k tokens
Independence required: no
Sub-agents or internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active

## Continuity anchor and authority renewal

Continuity anchor: your terminal PASS reports for exchanges 02-06
(`02_report_02.md` … `02_report_06.md`) and your commits `980db7af…` …
`87411e04…`. Prior authority expired at the last report. This is a complete
renewed grant for one bounded correction. Retained context is convenience,
not authority; repository evidence wins on conflict. Evidence in this
exchange is non-independent (same session).

## Confirmed finding (independent acceptance session 03, exchange 01)

The fresh independent acceptance of candidate `87411e04…` returned BLOCKED on
one refuted negative control (N7): **no Analyze path refuses a selected model
that does not declare `vision_input`**, although SPEC.md:726-727
("Analyze and the vision probe MUST refuse a selected model that does not
declare `vision_input`"), ADR-0081 decision 4, and AI_WORKSPACE.md:218-220 all
assert it. Audit evidence: `media_suggestion_api.py:251` and `:352` preflight
only provider configuration; `media_analysis_lifecycle_api.py:383` preflights
only provider configuration; the automatic executor (`application.py:677-695`
composition, `media_analysis_lifecycle.py` `ExecuteAutomaticMediaAnalysis`)
does not check; `AI_MODEL_CAPABILITY_MISSING` occurs only in
`ai_admin_api.py` (pong). Pong and the CLI `vision-probe` are correct and must
not change.

## Exact correction scope

1. **`src/framenest/adapters/api/media_suggestion_api.py`** — both
   `POST /api/libraries/{library_id}/media-suggestion-preview` and
   `POST /api/media/{media_id}/locations/{location_id}/ai-suggestion-preview`:
   after the existing provider-configured preflight and before any provider
   call, when `dependencies.read_provider` is present, resolve the current
   provider and refuse a selected model whose declared capabilities lack
   `vision_input` with `409 AI_MODEL_CAPABILITY_MISSING` and a sanitized
   message (for example "The selected AI model does not support image
   analysis."). Zero provider calls on refusal. When `read_provider` is None
   (legacy statically injected test dependencies), keep current behavior.
   Preserve the existing check order otherwise: audience check (imported
   route) → `confirm_cloud_upload` → provider configured → capability →
   execute.
2. **`src/framenest/adapters/api/media_analysis_lifecycle_api.py`** — the
   durable-analysis request route: same capability preflight after the
   configured check, `409 AI_MODEL_CAPABILITY_MISSING`, no provider call.
3. **`src/framenest/application/media_analysis_lifecycle.py`** — in
   `ExecuteAutomaticMediaAnalysis`:
   - add an optional constructor parameter
     `read_model_capabilities: Callable[[], Sequence[str]] | None = None`;
   - in `execute`, before `self._provider.suggest(request)`, when the reader
     is present and `"vision_input"` is not in the returned capabilities,
     raise a new sanitized exception (for example
     `MediaAnalysisLifecycleModelCapabilityError`), classified by
     `_classify_failure` as `PROVIDER_MODEL_CAPABILITY_MISSING` with message
     "AI provider model does not support image analysis." and
     `retryable=False`;
   - the new code MUST NOT be added to `_PROVIDER_SUBMISSION_ERROR_CODES`
     (no provider submission occurred) and MUST NOT alter any existing
     classification.
   - The reader's own exceptions (for example unconfigured/unavailable) keep
     their current classifications; do not swallow them.
4. **`src/framenest/adapters/api/application.py`** — wire the automatic
   executor's `read_model_capabilities` from the shared dynamic resolver:
   resolve per call; if `resolved.provider is None`, raise the existing
   sanitized `MediaSuggestionProviderUnavailableError` (preserving today's
   `PROVIDER_UNAVAILABLE` behavior for an unconfigured scheduler run); else
   return `resolved.capabilities_for(resolved.model_id or "")`. Do not change
   the movie-identification wiring.
5. **Documentation: none.** SPEC/ADR/AI_WORKSPACE already state the
   behavior; this correction makes the code match them. Do not touch any
   documentation file.

## Changed-path allowlist

```text
src/framenest/adapters/api/media_suggestion_api.py
src/framenest/adapters/api/media_analysis_lifecycle_api.py
src/framenest/application/media_analysis_lifecycle.py
src/framenest/adapters/api/application.py
tests/contract/test_media_suggestion_api.py
tests/contract/test_media_analysis_lifecycle_api.py
tests/unit/application/test_media_analysis_lifecycle.py
```

No other file may be created, edited, deleted, or moved.

## Tests

1. `tests/contract/test_media_suggestion_api.py`: with a declared provider
   whose selected model lacks `vision_input`, both preview routes return
   `409 AI_MODEL_CAPABILITY_MISSING` with zero transport calls; a
   `vision_input` model still analyzes as before.
2. `tests/contract/test_media_analysis_lifecycle_api.py`: the
   durable-analysis request returns `409 AI_MODEL_CAPABILITY_MISSING` for a
   non-vision selected model with zero provider calls; existing vision cases
   unchanged.
3. `tests/unit/application/test_media_analysis_lifecycle.py`: executor
   preflight — a non-vision model yields `PROVIDER_MODEL_CAPABILITY_MISSING`
   with `retryable=False`, no provider submission, and no provider call; an
   absent/None reader keeps current behavior; a reader raising the
   unavailable error still classifies as `PROVIDER_UNAVAILABLE`.

## Commands (canonical execution route — binding; note the working spelling)

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 87411e040157c51f3e1056e8a6e62c0c8c514018
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 87411e040157c51f3e1056e8a6e62c0c8c514018 --operation runtime-info
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 87411e040157c51f3e1056e8a6e62c0c8c514018 --operation test-focus -- tests/unit/infrastructure/ai tests/unit/application/test_media_analysis_lifecycle.py tests/contract/test_media_suggestion_api.py tests/contract/test_media_analysis_lifecycle_api.py tests/contract/test_automatic_analysis_privacy_contract.py tests/contract/test_ai_provider_admin_api.py tests/contract/test_tailscale_ingress_security.py -q -p no:cacheprovider
```

## Repository gate

Verify: HEAD equals `87411e040157c51f3e1056e8a6e62c0c8c514018` (the accepted
candidate under correction), porcelain clean, branch
`feat/x-meme-browser-companion`, `.ap` gitlink unchanged,
`./.ap/ap doctor` PASS. Stop on any unexplained difference.

## Authority

Positive: edit only the allowlisted paths; the declared AP route; read-only
Git; stage exactly the allowlisted paths; one corrective commit with subject
`Refuse non-vision models on Analyze paths`; no push; the single Meta report
below.

Negative: everything outside the allowlist; any documentation, ADR, web/UI,
CLI, provider-records, registry, or vision-probe change; any other Git write;
any provider/network call (tests use fake transports); NUC/SSH/sudo/browser/
GUI; ambient Python, `poetry run`, `pip`, `uv`, environment reconstruction;
secret access; `git add .`/`-A`; no weakening or deleting existing tests; do
not alter pong or CLI `vision-probe` behavior.

## Meta persistence contract (execute exactly)

```text
Meta persistence owner: this Worker, for the single report path named below.
Prompt persistence owner: ORCHESTRATOR (already written; do not rewrite it).
Exact report destination: /home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/02_report_07.md
Write the complete terminal report to that path after the work, then verify
byte identity. Do not create other Meta files. Do not rename. Do not commit
Meta Git. Do not commit FrameNest unless this prompt grants FrameNest Git.
If the path already contains a terminal report, STOP (PARTIAL) — do not
overwrite.
The Cooperator must not be asked to create, paste, or rename files.
```

## Report contract

Begin exactly with `### Report for ORCHESTRATOR_CHAT`; echo these coordinates
once (`Worker session ordinal: 02`, `Worker exchange ordinal: 07`); compact
core: status; `Phase-qualified result: implementation-PASS` on PASS else
`not-applicable`; start commit `87411e04…`; end commit (corrective commit);
changed files; tests and validation with exact counts; commit result;
deviations/risks; one smallest next step; `Report justification: new-mutation`;
authority-expiry statement; `Orchestration critique` (MEASURED/LEAD);
Resolved Execution Issues / Near-Misses and Pre-Existing Failure
Classification; `Logical-whole closure: not-closed`. Save, read back fully,
verify identity, then a short separate completion notice with location and
SHA-256.

## Stopping conditions

Stop and report BLOCKED or PARTIAL when a gate fails unclassifiably, a needed
change exceeds the allowlist, an existing test must be weakened, the
execution route is unusable, the Meta destination is occupied or unsafe, or
retained context conflicts with repository evidence.

Authority expiry: this terminal report ends the correction grant; no
autonomous continuation.
