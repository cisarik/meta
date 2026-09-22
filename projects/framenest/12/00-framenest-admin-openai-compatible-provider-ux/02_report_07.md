### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-admin-openai-compatible-provider-registry-and-vision-probe
Worker session ordinal: 02
Worker exchange ordinal: 07
Persistent role identity: WORKER
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Implementation
Task identity: CORRECT-ANALYZE-VISION-CAPABILITY-REFUSAL
status: PASS
Phase-qualified result: implementation-PASS
Start commit: 87411e040157c51f3e1056e8a6e62c0c8c514018
End commit: 7ff6546f345827d6df20bd5b13d5e57cb4bc90db
Report justification: new-mutation
Logical-whole closure: not-closed

Continuity anchor verified: this session's terminal exchange-02 through
exchange-06 reports (`02_report_02.md` … `02_report_06.md`, all PASS) and
their commits `980db7af…` … `87411e04…`; prior authority expired at the last
report. This exchange is a complete renewed grant for one bounded correction
of the accepted finding from the fresh independent acceptance session 03,
exchange 01 (refuted negative control N7). Current repository evidence agreed
with that finding; no conflict arose. Evidence is non-independent (same
session).

Repository gate (re-observed 2026-09-16, read-only): HEAD equal to the
accepted candidate under correction
`87411e040157c51f3e1056e8a6e62c0c8c514018`; porcelain clean before the first
edit; branch `feat/x-meme-browser-companion`; remote
`https://github.com/cisarik/framenest.git`; `.ap` gitlink == `.ap` HEAD ==
`7478ddb07d2c3911f79e1aa1441f0115a31c45d8`; `./.ap/ap doctor` PASS (stable
variant, managed block OK); `ap project check --baseline
87411e040157c51f3e1056e8a6e62c0c8c514018` PASS; `runtime-info` provenance
resolved under `/home/agile/Projects/framenest/src/framenest/__init__.py`; no
foreign worktree and no active mutation observed.

## 1. Coordinates

Echoed exactly once in the header block above.

## 2. Status

PASS. The confirmed finding is corrected at every Analyze boundary inside the
exact allowlist: both suggestion-preview routes, the durable-analysis request
route, and the automatic-analysis executor now refuse a dynamically resolved
model that does not declare `vision_input` with the sanitized
`AI_MODEL_CAPABILITY_MISSING` / `PROVIDER_MODEL_CAPABILITY_MISSING`
classification, with zero provider calls. Pong, the CLI `vision-probe`, the
movie-identification wiring, and all existing classification semantics are
unchanged; all focused and affected suites pass on the committed candidate.

## 3. Phase-qualified result

implementation-PASS (non-independent; same-session evidence).

## 4. Start and end commit

- Start (accepted candidate under correction):
  `87411e040157c51f3e1056e8a6e62c0c8c514018`
- End (corrective commit): `7ff6546f345827d6df20bd5b13d5e57cb4bc90db`

## 5. Changed files and purpose (exact allowlisted paths only)

- `src/framenest/adapters/api/media_suggestion_api.py` — added the sanitized
  `AI_MODEL_CAPABILITY_MISSING` code/message constants and a
  `_model_lacks_vision(dependencies)` preflight used by both
  `POST /api/libraries/{library_id}/media-suggestion-preview` and
  `POST /api/media/{media_id}/locations/{location_id}/ai-suggestion-preview`
  after the existing provider-configured check and before any preview or
  provider work. Existing order is preserved exactly: audience check
  (imported route) → `confirm_cloud_upload` → provider configured →
  `vision_input` capability → execute. Refusal returns `409
  AI_MODEL_CAPABILITY_MISSING` with no preview call. When `read_provider` is
  None (legacy statically injected test dependencies) or resolution raises,
  the helper returns False and current behavior is preserved; a capability
  miss is refused only when a dynamic resolution proves it.
- `src/framenest/adapters/api/media_analysis_lifecycle_api.py` — the same
  preflight for the durable-analysis request route after the configured
  check, returning `409 AI_MODEL_CAPABILITY_MISSING` before
  `request_manual_analysis` is consulted, so no run is created and no provider
  call occurs.
- `src/framenest/application/media_analysis_lifecycle.py` — added
  `MediaAnalysisLifecycleModelCapabilityError` and the optional
  `read_model_capabilities: Callable[[], Sequence[str]] | None` constructor
  parameter on `AutomaticImportedMediaSuggestionExecutor`; when the reader is
  present and `"vision_input"` is absent, the executor raises the new
  sanitized error before any media validation, preparation, or
  `self._provider.suggest(request)` call. `_classify_failure` classifies it as
  `PROVIDER_MODEL_CAPABILITY_MISSING` with message `AI provider model does not
  support image analysis.` and `retryable=False`; the new code was not added
  to `_PROVIDER_SUBMISSION_ERROR_CODES`, so `provider_submission_occurred` is
  False and no existing classification changed. The reader's own exceptions
  propagate unchanged (verified: `MediaSuggestionProviderUnavailableError`
  still classifies as `PROVIDER_UNAVAILABLE`).
- `src/framenest/adapters/api/application.py` — wired the automatic executor's
  `read_model_capabilities` from the shared dynamic resolver: resolve per
  call; if `resolved.provider is None`, raise the existing sanitized
  `MediaSuggestionProviderUnavailableError` (preserving today's
  `PROVIDER_UNAVAILABLE` behavior for an unconfigured scheduler run); else
  return `resolved.capabilities_for(resolved.model_id or "")`. Movie
  identification wiring is untouched.
- `tests/contract/test_media_suggestion_api.py` — extended the injected-deps
  helper with an optional `read_provider`; new tests prove that both preview
  routes return `409 AI_MODEL_CAPABILITY_MISSING` with zero preview calls for
  a non-vision resolved model, and that a `vision_input` resolved model still
  analyzes as before.
- `tests/contract/test_media_analysis_lifecycle_api.py` — new tests prove the
  durable-analysis request returns `409 AI_MODEL_CAPABILITY_MISSING` for a
  non-vision resolved model with zero scheduling calls, and still schedules
  for a vision model.
- `tests/unit/application/test_media_analysis_lifecycle.py` — new executor
  preflight tests: a non-vision model raises before any media access or
  provider call; a `None` reader keeps current behavior (media validation
  still runs first); a non-vision automatic run persists
  `PROVIDER_MODEL_CAPABILITY_MISSING` with `retryable=False` and no
  `provider_submission_occurred`; a reader raising the unavailable error still
  classifies as `PROVIDER_UNAVAILABLE` with no provider call.

Diff summary: 7 files changed, 376 insertions(+), 1 deletion(-). Pong
(`ai_admin_api.py`), the CLI `vision-probe`, provider records, the registry,
the vision-probe judge, and all documentation are unchanged; the automatic
analysis privacy-contract suite passed unmodified.

## 6. Tests and validation

Exact AP route selection (pre-commit and re-run post-commit):

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 87411e040157c51f3e1056e8a6e62c0c8c514018 --operation test-focus -- tests/unit/infrastructure/ai tests/unit/application/test_media_analysis_lifecycle.py tests/contract/test_media_suggestion_api.py tests/contract/test_media_analysis_lifecycle_api.py tests/contract/test_automatic_analysis_privacy_contract.py tests/contract/test_ai_provider_admin_api.py tests/contract/test_tailscale_ingress_security.py -q -p no:cacheprovider
```

Result: `482 passed in 56.37s` and `482 passed in 56.51s` (0 failed, 0
skipped). The eight new tests were additionally run by name
(`-k "capability or vision"`) -> `13 passed, 60 deselected`, confirming they
execute and cover the refusal and the retained vision path.

Final diff inspection: the full committed diff was inspected;
`git status --porcelain` is empty after the commit; `git diff --name-only`
shows exactly the seven allowlisted paths; no secret shape, key, home path,
or provider payload was added.

## 7. Commit result

Exactly one local corrective commit on `feat/x-meme-browser-companion`:

```text
7ff6546f345827d6df20bd5b13d5e57cb4bc90db Refuse non-vision models on Analyze paths
```

Staging was path-exact (7 allowlisted paths, no `git add .`, no wildcard). No
push, no fetch, no branch/tag/merge/rebase/reset/clean/checkout/stash/config
operation; only read-only Git reads plus the single `git add`/`git commit`.
The local commit is not canonical; the AP `--baseline` remained the accepted
candidate `87411e04…`.

## 8. Deviations, risks, or missing evidence

- The executor capability check is placed immediately after the
  provider-configured check and before media validation/preparation rather
  than immediately before `suggest`; it is still strictly before any provider
  call and additionally avoids wasted local preparation. This is a deliberate,
  documented placement inside the granted scope.
- The API helpers fail open when `read_provider` is absent or raises, and fail
  closed only on a proven capability miss; the route preflight is therefore
  authoritative in the real composition, while legacy statically injected
  tests keep their behavior. A resolve error still surfaces through the lazy
  provider at execution time with its existing sanitized classification.
- Each preview/durable request resolves twice (configured check plus
  capability check). The bounded TOCTOU window only affects which sanitized
  refusal is returned if an operator edits the config between the two reads;
  no provider call is possible on refusal.
- No documentation was changed, as instructed; the correction now matches
  SPEC §22, ADR-0081 decision 4, and AI_WORKSPACE.
- Retained risk: a model that genuinely declares `vision_input` but receives
  non-image content still fails through the existing provider taxonomy; this
  correction only implements the declared-capability contract.

Missing evidence: none for the allowlisted surface. No provider, NUC,
network, credential, browser, or deployment action occurred; tests use fakes.

## 9. Smallest next step / review request

Fresh independent re-acceptance of the corrected candidate `7ff6546…`
(covering N7 and scoped regression), then publication, routine NUC refresh,
and the Cooperator's numbered acceptance run.

## 10. Report justification

Report justification: new-mutation

## 11. Authority expiry

This terminal report, cancellation, or supersession ends the correction
grant; retained context is not continuing authority; no autonomous
continuation. The commit awaits Orchestrator reconciliation and independent
re-acceptance.

## 12. Orchestration critique

```text
Orchestration critique:
MEASURED: The N7 finding is fully corrected at all four Analyze boundaries (both preview routes, the durable-analysis request, and the automatic executor) with the sanitized capability refusal, zero provider calls, and no change to pong, CLI vision-probe, movie-identification wiring, or existing failure classifications; the full affected selection is green pre- and post-commit (`482 passed`, plus `13 passed` for the new tests). The only judgment calls are the early executor check placement and fail-open helper behavior, both documented above and consistent with the prompt's stopping order.
LEAD: None material. If the Cooperator's live Analyze run after publication uses a model that declares `vision_input`, behavior is unchanged; the remaining product observation is the slice-2 strict-judge pong, already surfaced for the numbered acceptance.
```

## 13. Resolved Execution Issues / Near-Misses and Pre-Existing Failure Classification

Resolved Execution Issues / Near-Misses: the prompt's command blocks again
spell the declared operations as `./.ap/ap ap …`; the working invocation is
`./.ap/ap …` (used in exchanges 01-06; same declared operations, baseline,
and evidence class). No other near-miss occurred.

Pre-Existing Failure Classification: none. The corrected candidate
`87411e04…` was green on the then-selected docs-contract suites before this
exchange; the acceptance finding was a coverage/claim gap, not a test failure
carried in from the repository.

## Persistence and hygiene

Changed files: only the 7 exact allowlisted paths in section 5.

Git result: one local commit `7ff6546f345827d6df20bd5b13d5e57cb4bc90db`; no
push; no other Git write.

Persistence: this report was saved to the exact granted destination
`/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/02_report_07.md`
after verifying the parent path, symlink resolution, and destination absence;
the complete saved content was read back before the separate completion
notice. Meta Git archival remains with the COOPERATOR; no Meta Git operation
was performed.
