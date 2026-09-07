### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 18, Worker exchange ordinal: 01
```

- **Status:** PASS — D1–D7 completed as an advisory plan.
- **Phase-qualified result:** `not-applicable`.
- **Start/end commit:** both `a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20`.
- **Changed files:** none.
- **Tests/validation:** opening and closing repository gates passed; AP gitlink matched `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; porcelain empty. Read-only source/schema inspection and stdlib fixture-digest verification completed. No tests or application processes run.
- **Commit/push:** `not-applicable`.
- **Deviations/risks/missing evidence:** no authority deviations. Nullable `score` requires a narrow vocabulary/schema correction. Aggregate fields are not implemented in slice 2. No live-quality evidence was obtained.
- **Smallest next step:** issue one complete E2 implementation grant to a fresh Worker, explicitly including the five paths in D5.
- **Report justification:** `new-evidence`.
- **Authority expiry:** this planning authority expires upon submission; implementation remains prohibited in this session.

Evidence tier: **E0**. Evidence posture: **non-independent**. Logical-whole closure: **not-closed**.

### D1 — Drive path

**Choose B: extend `_write_report` for `instrument="position-set"`.**

The landed path already performs the required work:

1. `run()` dispatches to `_drive_position_set`.
2. That loop loads the committed asset, mounts each snapshot, resolves its acting seat, sends one turn through the existing Node worker, reconciles persistence, and writes `DiagnosticPly(position_index=index)`.
3. Exhaustion sets `position_set_exhausted`.
4. `_finish()` shuts down the worker and calls `_write_report`.

The gap is exactly that `_write_report` constructs an `AiMatchSample` unconditionally. The existing position-set test even asserts `report_kind == "ai-match"`. Sources: [runner](/home/agile/Projects/libretiles/backend/game/management/commands/run_diagnostic_match.py:563), [position loop](/home/agile/Projects/libretiles/backend/game/management/commands/run_diagnostic_match.py:686), [existing regression](/home/agile/Projects/libretiles/backend/tests/test_diagnostic_runner.py:480).

The extension should:

- Read persisted `run.plies`, ordered by `position_index`, and join them to snapshots by that index. Do not depend on `state.records`, which lacks position identity.
- Construct existing `ModelPositionSample` objects, call `build_model_position_report`, then add the aggregates specified below.
- Retain the existing redaction, JSON dumping, atomic file writer, report-path persistence, and no-overwrite behavior.
- Preserve the full-game report branch.

This introduces no command, turn loop, snapshot remount during reporting, engine search, worker invocation, or historical-report backfill.

**Single-pair precondition:** select the same catalog row for both seats, using the existing launcher. The fixture acts from seat 0 thirteen times and seat 1 eleven times. Both seat providers/model IDs, recorded run model IDs, and observed ply identities must agree before publishing a single-model report. Reject unsupported mixed-pair report construction before writing the artifact; retain the existing run/ply evidence and report-error logging. No launcher redesign is needed.

### D2 — ModelPositionSample fill

The verified set digest is:

```text
f5ae61b467b4f21e6fe9ee94024e9c3c06e09e0dbae7e6cc8954ff911dc86ef4
```

Recomputing the generator’s canonical hash over `config` and `positions` matched it. The fixture has indices `0..23`, eight positions per phase, and no ended snapshots.

The mapping is:

| Destination | Source and treatment |
|---|---|
| `set_digest` → serialized `position.set_digest` | Verified asset digest, equal to `run.position_set_digest`. |
| `position_index` → `position.position_index` | `DiagnosticPly.position_index`; require agreement with the snapshot’s index. |
| `ply.seat_index`, `model_id`, `assist_mode`, `score_authority` | Same-named columns, validated against the run and snapshot. |
| `ply.model_authored`, `first_validate_valid`, `valid_candidate_count`, `model_legal_score` | Same-named columns; preserve `None`. |
| `ply.ranked_best_score` | Joined snapshot’s `engine_baseline.ranked_best_score`. |
| `ply.ranked_search_complete` | Joined snapshot’s `engine_baseline.ranked_search_complete`. |
| `ply.give_up_while_legal`, `playability_status`, `completion_source`, `terminal_cause` | Same-named columns; preserve `None`. |
| `ply.provider_requests_used`, `steps_consumed`, `wall_clock_ms`, `malformed_or_non_tool`, `fallback_attempt_index`, `executed_runtime_mode` | Same-named columns without zero/default coercion. |
| `ply.earlier_attempt_failures` | JSON list becomes a tuple; JSON null remains `None`. |
| `score` | `None` for the authorized `generic_unchanged` execution. No placement score was measured. |
| `verdict` | `"fail"` for that unchanged fake turn. |
| `reason_code` | Existing `REASON_GENERIC_UNCHANGED`, serialized as `"generic_unchanged_turn"`. |

These cover all **21** `PlyMetricRecord` fields. Serialization flattens them into the sample; there is no nested JSON `ply` object. Sources: [vocabulary and serializer](/home/agile/Projects/libretiles/backend/game/diagnostics.py:753), [persisted columns](/home/agile/Projects/libretiles/backend/game/models.py:285).

The two baseline fields are report-time enrichment only. Do not rewrite `DiagnosticPly`, regenerate the fixture, or substitute baseline `witness_status` for the unmeasured turn’s `playability_status`.

The exact literals are:

```text
Verdict = Literal["pass", "fail"]
TurnVerdict = Literal["pass", "pass_with_telemetry", "fail", "external_incomplete"]
```

`ModelPositionSample.verdict` uses **Verdict**. Neither `did_not_measure` nor `pass_with_telemetry` is valid there. `reason_code` is a bounded string, not a closed enum; using the existing constant avoids introducing a new reason.

**Required narrow correction:** [ModelPositionSample.score](/home/agile/Projects/libretiles/backend/game/diagnostics.py:781) currently has type `int`, and [the schema](/home/agile/Projects/libretiles/backend/assets/diagnostics/ai_play_report_v1.schema.json:417) requires integer `score`. Change only this sample’s type to `int | None` and its schema property to `["integer", "null"]`. Keep the property required. The serializer already preserves `None`; no verdict widening or migration is necessary.

The schema’s required model-position fields remain:

```text
position, seat_index, model_id, assist_mode, score_authority,
score, verdict, reason_code
```

For truncated or aborted runs, serialize actual persisted plies only. Represent unattempted positions through coverage counts, not invented samples.

### D3 — Aggregation

**Measured starting point:** `build_model_position_report` currently supplies only:

```text
summary.sample_count
summary.pass_count
summary.fail_count
```

The schema allows additional summary properties. Neither file currently defines move-quality aggregation, `did_not_measure`, a completion-source histogram, or model-position truncation fields. The following are **proposed 3b additions**, not claimed existing vocabulary. Source: [report envelope](/home/agile/Projects/libretiles/backend/game/diagnostics.py:1335).

For position \(i\):

\[
r_i=\frac{\text{model\_legal\_score}_i}
          {\text{snapshot.engine\_baseline.ranked\_best\_score}_i}
\]

Include `samples[i].move_quality_ratio` only when:

- `model_authored is True`;
- `completion_source` is `provider_candidate` or `repair_candidate`;
- the numerator is a measured integer;
- the denominator is a positive integer.

Exclude booleans masquerading as integers. Missing numerator, missing/nonpositive denominator, or engine-rescue authorship produces **no ratio field**, not zero.

Use the arithmetic mean of eligible position ratios for `summary.move_quality_ratio`. Every eligible position has equal weight. Omit that key when no ratios exist. A genuinely measured zero numerator remains zero; do not use truthiness to detect missingness.

Do not require `ranked_search_complete=True` or clamp ratios to one: this is comparison with a bounded baseline, not a certified optimum. All 24 denominators are positive; positions **3 and 6** have incomplete searches.

Exact proposed summary contract:

| Key | Meaning |
|---|---|
| `sample_count`, `pass_count`, `fail_count` | Existing builder counts over emitted samples. |
| `position_count` | Fixture size: 24. |
| `unattempted_count` | Fixture positions with no persisted ply. |
| `end_reason` | `run.diagnostic_end_reason`, falling back to terminal run status. |
| `truncated` | Whether `end_reason == "truncated"`. Cancellation/failure retain their own reasons. |
| `move_quality_sample_count` | Number of eligible position ratios. |
| `did_not_measure` | Emitted samples lacking a ratio; equals `sample_count - move_quality_sample_count`. Unattempted positions are counted separately. |
| `move_quality_ratio` | Mean defined above; absent when the eligible count is zero. |
| `completion_source_counts` | Counts for exactly the six existing completion-source values. |
| `completion_source_did_not_measure_count` | Samples whose completion source is `None`. |
| `total_provider_requests` | Sum only when every emitted ply has a measured count; omit for empty/partially unknown evidence. |

Initialize the histogram using `COMPLETION_SOURCE_VOCABULARY`. Its six zero counts are observed occurrence counts, not fabricated move scores. Do not add an `"unknown"` completion-source value.

For a complete assisted `generic_unchanged` run, the expected result is:

```text
sample_count=24, pass_count=0, fail_count=24
position_count=24, unattempted_count=0
end_reason="position_set_exhausted", truncated=false
move_quality_sample_count=0, did_not_measure=24
move_quality_ratio: absent
completion_source_counts: all six counts are 0
completion_source_did_not_measure_count=24
total_provider_requests=0
every sample.score=null
every sample.model_legal_score=null
```

Mark the artifact and samples `executed_runtime_mode="fake"`. Retain request identity, digest, selected provider/model, assist mode, script, queue mode, and provisional-cap provenance through explicit safe fields. Do not serialize the whole parameters dictionary or add `external_provider_invocations` from evidence absent in `DiagnosticPly`.

Apply `redacted_copy` after augmentation. Keep artifact ID **`libretiles.ai-play-diagnostic/v1`**.

### D4 — Honest fake

The following implementation remains restricted to `generic_unchanged`, selected-only, fake execution. `LIVE_SENTINEL` refusal remains intact.

A green acceptance test must prove:

- The landed runner emits 24 persisted plies and a 24-sample **model-position** artifact for the same pair in both seats.
- Every serialized `score` and `model_legal_score` is explicitly null; unavailable booleans/counters retain null.
- Every baseline score/completeness value matches its indexed fixture snapshot.
- No per-position or aggregate ratio is written; `did_not_measure=24`.
- `Move` count does not increase; reported provider requests are measured zeros.
- Report construction works with empty `state.records`, consumes persisted rows, and performs no worker call or snapshot remount.
- Repeated report writing preserves the existing artifact.

Separate synthetic unit inputs exercise ratio arithmetic: positive numerator, measured zero, absent numerator, absent/zero denominator, incomplete baseline, ratio above one, and backend-rescue exclusion. These fixtures are arithmetic evidence, never live model performance.

The real fake branch returns before catalog fetching or invoking the supplied POST handler. Therefore a green fake test proves reporting and orchestration plumbing; it does **not** prove model quality or real provider execution. Source: [generic fake branch](/home/agile/Projects/libretiles/frontend/src/lib/ai-play-diagnostic.ts:410).

A later live grant must authorize actual provider execution through the existing runner/worker, establish measured runtime and persisted scoring evidence, and resolve verdict treatment for additional terminal cases. Existing `model_legal_score` can supply the model-authored numerator; unpersisted engine-rescue scores must remain unknown unless separately instrumented. Those changes are outside the next exchange.

### D5 — One implementation exchange: allowlist, fail-before, tier

Proposed mutation allowlist:

| Exact path | Permitted change |
|---|---|
| `backend/game/management/commands/run_diagnostic_match.py` | Position-report branch and local mapping/aggregation helpers; report-input validation. |
| `backend/game/diagnostics.py` | **D2-forced exception only:** nullable `ModelPositionSample.score` annotation and explanatory comment. |
| `backend/assets/diagnostics/ai_play_report_v1.schema.json` | Nullable model-position score; typed additive ratio/summary properties. Preserve ID, required fields, and verdict enums. |
| `backend/tests/test_diagnostic_runner.py` | Position-report integration, mapping, aggregation, coverage, and refusal regressions. |
| `backend/tests/test_ai_play_engine_diagnostic.py` | Nullable vocabulary/schema/serialization checks; preserve other report-kind coverage. |

**Negative authority:** no gamecore changes; no model/schema migration changes, including `0009`, `0010`, or `0011`; no fixture/generator changes; no services, admin launcher, mint, Node worker, frontend, slice-6 templates, base URL, SSRF, dependencies, AP, or accepted-residual remediation. No second command or turn loop.

The implementation should establish these tests before production edits. Their baseline outcomes below are source-grounded predictions; they were **not run** in this planning session.

| ID | Required assertion or refusal boundary | Baseline posture |
|---|---|---|
| `APMC-S3B-F01` | Same-pair, 24-position run produces 24 model-position samples. | Fails: currently one ai-match sample. |
| `APMC-S3B-F02` | Required score supports null in vocabulary, schema, and serialized fake output. | Fails current declared contract. |
| `APMC-S3B-F03` | Persisted row/index join supplies all metrics and exact snapshot baselines despite empty runner memory. | Mapping absent. |
| `APMC-S3B-F04` | Ratio arithmetic and all D3 missingness/histogram keys match the contract. | Aggregation absent. |
| `APMC-S3B-F05` | Cap at two positions reports two samples, 22 unattempted, truncation, and no fabricated ratio. Authorship abort retains its actual terminal reason. | Required position coverage absent. |
| `APMC-S3B-F06` | Missing/mismatched digest, invalid/duplicate position index, variant/seat mismatch, or mixed catalog pair refuses report publication before atomic writing/path update. | New reporting guards. |
| `APMC-S3B-F07` | No extra IPC turns/remounts during reporting; repeated writes do not overwrite; full-game report remains ai-match. | Preserve existing behavior and extend assertions. |
| `APMC-S3B-F08` | LIVE_SENTINEL still refuses before claim/mint/spawn; credential whitelist and six-source vocabulary remain unchanged. | Existing negative controls must stay green. |

For F06, valid null baseline values mean unavailable measurement; malformed structures/types are input errors. Never repair them to zero.

**Evidence tier: E2**, non-independent implementation evidence. No fresh independent acceptance is required for this fake report-wiring cut. Any live expansion requires a different grant and evidence assessment.

Following-exchange validation should run focused regressions plus backend Ruff, full configured mypy scope, and the offline backend suite. Use the mandated sanitized `.venv/bin/python` route, no additional `-q`, and no build/install. Disable dotenv loading before Django initialization using `PYTHON_DOTENV_DISABLED=1`—supported by the installed library—and supply test-only settings. Keep test artifacts contained; do not access the existing secret files or application database.

**Proposed Git authority for that future grant:** explicit-path staging of these five files, commit on existing `main`, and push `HEAD:main` to the repository’s configured origin, followed by authorized readback. No new branch or force push. This session performed none of those actions.

### D6 — K1 boundary

Fake 3b measures serialization, attribution, missingness, arithmetic, and coverage using already committed baselines and provider-free observations. It therefore does not need the 8–12 NIM calls. K1 still owes measured requests-per-ply and relevant timing/terminal behavior through the actual granted live path, including repair/rescue and failure accounting, before deriving a defensible 24-position provider-request ceiling. Keep instrument subcaps provisional; retain the 200 default/1000 admin maximum. This plan neither starts K1 nor freezes a live cap.

### D7 — Orchestration critique

| MEASURED | LEAD |
|---|---|
| The prompt describes aggregation as already specified by slice-2 vocabulary. Landed code provides nullable ply inputs and the report envelope, but no ratio, histogram, truncation, or `did_not_measure` aggregation. | The execution grant should explicitly authorize D3’s additive contract instead of describing it as existing implementation. |
| The prompt prefers no diagnostics edits, yet its demanded honest score cannot satisfy the current integer-only sample/schema contract. | Include the precise D2 exception in the implementation allowlist. The prompt already permits this exception; no AP conflict exists. |
| [91_ step 4](/home/agile/meta/projects/libretiles/11/00-admin-provider-model-console/91_orchestrator-handout-1.md:215) describes mounting and driving each position. The accepted runner already owns both operations. | Scope 3b to terminal reporting over persisted plies; copying step 4 literally into implementation risks a second drive loop. |
| Step 4 specifies one catalog pair, while the launcher accepts two seat models and the fixture uses both seats. | Use the same pair in both existing selectors and validate identity before publishing a single-model report. |
| Step 4 refers to a K1-derived ceiling. Current configuration explicitly marks subcaps provisional, and this grant excludes live work. | Keep K1 and live-cap finalization in their separately authorized exchange. |
| `generic_unchanged` imports the established worker path but returns before invoking the move route. | Describe fake acceptance as plumbing/report evidence; do not claim it demonstrates model strength or live move execution. |

**Resolved Execution Issues / Near-Misses:** native Plan-mode absence correctly treated as expected under the complete `not-used` reissue. No implementation or delegation occurred.

**Pre-Existing Failure Classification:** measured report-kind and nullable-score/aggregate gaps are the planned 3b work. Accepted slice-5 residuals remain untouched.

**Enumeration widened:** persisted-row fields and constraints; terminal/report paths; schema definitions and serializers; existing regressions; snapshot hashing and baseline completeness; seat/model selection; actual generic-fake execution; 91_ step 4; dotenv-loading behavior.

**Context pressure:** low; sufficient context remained to complete all seven deliverables.

**Authority expired upon this report’s submission.**