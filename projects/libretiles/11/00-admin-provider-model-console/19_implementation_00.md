You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An accepted plan grants you nothing; THIS prompt does.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 19
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: APMC-S3B-REPORT — position-set DiagnosticRun terminal reporting: persist-already-driven plies become a model-position artifact with honest ModelPositionSample fill, nullable score, and the D3 additive aggregates. FAKE MODE ONLY. Provider calls: ZERO.
Phase: implementation
Implementation authority: explicit
Exact baseline: a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20
Changed-path allowlist: exactly the five paths in section 4
Implementation boundaries: positive and negative authority in sections 3-5
Independence required: no
Evidence posture: non-independent
Evidence tier: E2
Evidence tier basis: report/metric wiring on an already-audited fake runner; no new mint; no new privilege surface; no live provider path. Independent 3b acceptance is NOT required unless the implementation secretly goes live.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risks: (1) cloning 91_ step 4 into a second mount/drive loop would double worker turns and poison ply identity; (2) writing `0` or omitting a key’s null where the metric was not measured poisons the model-choice number this whole exists to produce; (3) constructing a single-model report from mixed seat catalog rows would attribute two rivals to one sample stream.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1444-1462      Git and remote safety — every write needs the exact authority THIS prompt names
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   role and authority boundary
PROMPT_CONTRACTS.md:14-41   the report contract and the coordinate fields you echo back unchanged
PROMPT_CONTRACTS.md:203     the phase-result enum. Expected Worker result spelling:
                            `implementation-PASS`. Planning uses `not-applicable`; do not invent
                            a third spelling.
AP.md:2452-2454      the CLOSED report-justification enum. Read it; do not recall it.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it
   yourself. That sentence is what makes a reading shortcut fail closed.
```

## Mandatory reading — by symbol; re-measure every symbol before you use it

```text
/home/agile/Projects/libretiles/AGENTS.md
backend/game/management/commands/run_diagnostic_match.py
    run() → _drive_position_set already mounts, drives, persists DiagnosticPly(position_index),
    exhausts with position_set_exhausted, then _finish → _write_report.
    TODAY _write_report ALWAYS builds AiMatchSample / report_kind=ai-match.
    state.records has no position identity. _persist_ply writes ranked_best_score=None.
backend/game/diagnostics.py
    ModelPositionSample.score: int            ⭐ D2-forced exception: change to int | None
    Verdict = Literal["pass", "fail"]         ⭐ ModelPositionSample.verdict uses Verdict
    TurnVerdict includes pass_with_telemetry / external_incomplete — NOT valid on this sample
    REASON_GENERIC_UNCHANGED = "generic_unchanged_turn"
    COMPLETION_SOURCE_VOCABULARY  (exactly six strings)
    build_model_position_report / model_position_sample_to_dict / _vocabulary_report_envelope
    SECRET_KEY_FRAGMENTS — no new key may contain a fragment
    ARTIFACT_ID = "libretiles.ai-play-diagnostic/v1"  ⛔ do not bump
backend/assets/diagnostics/ai_play_report_v1.schema.json
    $id / artifact const stay v1
    modelPositionSample.properties.score is { "type": "integer" }  ⭐ make ["integer", "null"]
    summary.additionalProperties is already true; required stays sample_count/pass_count/fail_count
backend/game/models.py          DiagnosticPly related_name="plies"; position_index nullable
backend/tests/test_diagnostic_runner.py
    test_position_set_run_persists_position_index_and_exhausts asserts report_kind == "ai-match"
    _create_run defaults seat0=FREE_RIVAL_IDS[0], seat1=FREE_RIVAL_IDS[1] (MIXED)
backend/tests/test_ai_play_engine_diagnostic.py
    vocabulary / schema / serialization coverage for other report kinds — preserve it
backend/assets/diagnostics/position_sets/english-f5ae61b4.json
    set_digest f5ae61b467b4f21e6fe9ee94024e9c3c06e09e0dbae7e6cc8954ff911dc86ef4
    24 positions, indices 0..23, eight per phase, no ended snapshots
    every engine_baseline.ranked_best_score is a positive int
    positions 3 and 6 have ranked_search_complete=false
    to_move_seat_index: seat 0 thirteen times, seat 1 eleven times
frontend/src/lib/ai-play-diagnostic.ts   generic_unchanged returns BEFORE the POST handler
⛔ Do not edit the frontend. Read only to know what a green fake test does and does not prove.
```

## 1. Repository gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before start and before commit
```

If `main` has advanced past `a17cdf4`: re-gate against the THEN-HEAD, state the new baseline in
your report, and continue — your allowlist and claims do not change. Any other divergence:
classify with the five recovery-candidate classes at AP.md:1464-1476 and STOP.

## 2. Goal

When `instrument="position-set"`, `_write_report` must publish a **model-position** artifact
from **persisted** `run.plies` joined to the committed snapshot list by `position_index`.
Full-game reporting stays **ai-match**. Fake `generic_unchanged` remains the only executed
script. LIVE_SENTINEL refusal remains intact.

This is **terminal reporting**. The landed runner already owns mount + drive. ⛔ Do not add a
second command, a second turn loop, a snapshot remount inside reporting, an engine search, a
worker invocation, a fixture regen, or a historical-report backfill.

## 3. Required behaviour

### 3.1 Drive path (choose B, already landed)

Keep `_drive_position_set`. Extend `_write_report`:

1. If `run.report_path` is already set, return (existing no-overwrite).
2. If `run.instrument != "position-set"`, keep the current `AiMatchSample` branch.
3. If `run.instrument == "position-set"`:
   - Load persisted plies ordered by `position_index` (then `ply_index` as a tie-break if you
     need one). ⛔ Do not depend on `state.records`.
   - Load the committed position-set asset by `run.position_set_digest` (reuse the existing
     asset loader).
   - Join each ply to its snapshot by `position_index`. Require agreement between the ply’s
     stored index and the snapshot’s index.
   - Validate the single-pair precondition (3.2). On failure: log, **do not** call
     `write_report_atomically`, **do not** set `report_path`, **do not** abort the run.
     Retain ply rows. Use the existing `_write_report` try/except so a report refusal never
     kills a finished run.
   - Build `ModelPositionSample` objects, call `build_model_position_report`, **then** apply
     the D3 additive aggregates and any per-sample `move_quality_ratio` keys (3.4).
   - Apply `redacted_copy` **after** augmentation.
   - Dump JSON, `write_report_atomically`, persist `report_path` exactly as today.

`_vocabulary_report_envelope` types `summary` as `dict[str, int]`. Mixed-type D3 keys therefore
belong in the **command’s post-builder augmentation**. ⛔ Do not rewrite that envelope, and do
not change `diagnostics.py` beyond the D2 score annotation plus an explanatory comment.

### 3.2 Single-pair precondition

A published model-position report describes **one** catalog pair. Before writing:

- `run.seat0_model_id` equals `run.seat1_model_id`
- both session AI slots resolve to that same `provider` + `model_id`
- every persisted ply’s `model_id` equals that identity
- `run.position_set_digest` equals the asset `set_digest` and every sample’s `set_digest`

The existing admin launcher already has two seat selectors. Tests that want a published
artifact must pass the **same** `AIModel` instance to both seats (`model_id` is unique;
do not `get_or_create` a second row with the same id). Mixed-pair position-set runs remain
legal to **drive**; they are illegal to **publish** as a single-model report. No launcher
redesign.

### 3.3 ModelPositionSample fill

Reconstruct `PlyMetricRecord` from the DiagnosticPly columns. Preserve `None`. JSON
`earlier_attempt_failures`: a JSON list becomes a tuple; JSON null stays `None`; any other
JSON shape is a publication refusal (malformed), never coerced to `[]`.

Report-time overlay **only** (do not UPDATE DiagnosticPly):

- `ply.ranked_best_score` ← snapshot `engine_baseline.ranked_best_score`
- `ply.ranked_search_complete` ← snapshot `engine_baseline.ranked_search_complete`

Valid JSON null / missing baseline values mean **unmeasured**. Malformed types or structures
(including a bool masquerading as an int) are publication refusals. Never repair them to `0`.
Do not substitute baseline `witness_status` for the ply’s `playability_status`.

Remaining fields: same-named DiagnosticPly columns. `set_digest` / `position_index` from the
joined snapshot, agreeing with the ply.

For this grant’s authorized `generic_unchanged` execution (no placement score measured):

```text
score        = None
verdict      = "fail"
reason_code  = REASON_GENERIC_UNCHANGED   # serializes as "generic_unchanged_turn"
```

`did_not_measure` and `pass_with_telemetry` are **not** valid `ModelPositionSample.verdict`
values. `reason_code` is a bounded string, not a new enum.

Serialize via `model_position_sample_to_dict` (flat ply fields + `position`; no nested `ply`
object). Truncated or aborted runs: serialize **actual persisted plies only**. Represent
unattempted fixture positions through coverage counts, not invented samples.

### 3.4 Aggregation — authorized NEW contract (not existing slice-2 vocabulary)

Today `build_model_position_report` supplies only `summary.sample_count`, `pass_count`,
`fail_count`. You are authorized to **add** the following after that call. Schema-type them
under `summary` / `modelPositionSample` without making the new keys required.

Per-position ratio, attached as `samples[i].move_quality_ratio` **only when all** hold:

- `model_authored is True` (the boolean True, not a truthy integer)
- `completion_source` is `provider_candidate` or `repair_candidate`
- numerator `model_legal_score` is a measured `int` and not a `bool`
- denominator snapshot `engine_baseline.ranked_best_score` is a **positive** `int` and not a `bool`

Otherwise **omit the key**. Do not write `0` for ineligible positions. A genuinely measured
zero numerator remains `0` (ratio `0`); do not use truthiness to detect missingness. Do **not**
require `ranked_search_complete=True`. Do **not** clamp ratios to 1. Engine-rescue /
`backend_ranked_candidate` / `backend_witness_rescue` authorship produces no ratio field.

`summary.move_quality_ratio` = arithmetic mean of eligible position ratios, equal weight.
**Omit that summary key** when the eligible count is 0.

| Key | Meaning |
|---|---|
| `sample_count`, `pass_count`, `fail_count` | Existing builder counts over **emitted** samples |
| `position_count` | Fixture size (24 for the committed English set) |
| `unattempted_count` | Fixture positions with no persisted ply |
| `end_reason` | `run.diagnostic_end_reason`, else terminal `run.status` |
| `truncated` | `end_reason == "truncated"` exactly. Cancel/failure keep their own reasons |
| `move_quality_sample_count` | Number of eligible position ratios |
| `did_not_measure` | Emitted samples lacking a ratio; `sample_count - move_quality_sample_count`. Unattempted positions are counted separately |
| `move_quality_ratio` | Mean defined above; absent when eligible count is 0 |
| `completion_source_counts` | Counts for **exactly** the six `COMPLETION_SOURCE_VOCABULARY` values, initialized to 0 |
| `completion_source_did_not_measure_count` | Samples whose `completion_source is None` |
| `total_provider_requests` | Sum only when **every** emitted ply has a measured integer count; omit for empty or partially unknown evidence |

Histogram zeros are observed occurrence counts, not fabricated move scores. ⛔ Do not add an
`"unknown"` completion-source value. A non-null source outside the six-word vocabulary is
malformed publication input (refuse), not a seventh bucket.

Mark the artifact and samples `executed_runtime_mode="fake"`. Retain request identity, digest,
selected provider/model, assist mode, script, queue mode, and provisional-cap provenance
through **explicit safe fields** already compatible with `SECRET_KEY_FRAGMENTS` and with
`build_model_position_report`’s `requested: Mapping[str, str | int]`. ⛔ Do not serialize the
whole `parameters_json`. ⛔ Do not add `external_provider_invocations` from evidence that is
absent on `DiagnosticPly`. Keep artifact ID `libretiles.ai-play-diagnostic/v1`.

Complete assisted `generic_unchanged` same-pair run, expected:

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
every sample.ranked_best_score / ranked_search_complete equals its indexed snapshot baseline
report_kind=model-position
executed_runtime_mode=fake
```

`run.score_authority == "engine"` on a completed position-set run is the **engine** authority
for the session, not a claim that the model scored 24 times. Do not present `fail_count=24` as
model skill. Product copy is slice 6; this slice only serializes honest fields.

### 3.5 Fail-before, then tests, then production edits

Capture the F01–F08 baseline outcomes **before** production edits, verbatim in the report.
Then establish the tests. Then edit production code. Predictions below are source-grounded;
you must still measure.

| ID | Required assertion or refusal boundary | Baseline posture |
|---|---|---|
| `APMC-S3B-F01` | Same-pair, 24-position fake run → 24 model-position samples, contract in 3.4. Update the existing position-set test; do not leave `ai-match` as the expected kind. | Fails: currently one ai-match sample |
| `APMC-S3B-F02` | Required `score` supports null in vocabulary, schema, and serialized fake output | Fails current declared contract |
| `APMC-S3B-F03` | Persisted row/index join supplies all 21 ply metrics and exact snapshot baselines despite empty `state.records` | Mapping absent |
| `APMC-S3B-F04` | Ratio arithmetic + D3 missingness/histogram keys match 3.4. Synthetic cases: positive numerator, measured zero, absent numerator, absent/zero denominator, incomplete baseline (`ranked_search_complete=false` still eligible), ratio above one, backend-rescue / non-model-authored exclusion | Aggregation absent |
| `APMC-S3B-F05` | `max_plies=2` → two samples, 22 unattempted, `end_reason=truncated`, `truncated=true`, no fabricated ratio. Authorship abort on a position-set run retains `model_authorship_failure` (not rewritten to truncated) and serializes only actual plies | Required position coverage absent |
| `APMC-S3B-F06` | Missing/mismatched digest, invalid/duplicate `position_index`, variant/seat mismatch, mixed catalog pair, or malformed baseline/failures JSON refuses publication **before** atomic write / `report_path` update. Run/ply evidence retained | New reporting guards |
| `APMC-S3B-F07` | Reporting performs no worker call and no `apply_position_snapshot`. Repeated `_write_report` does not overwrite. Full-game report remains `ai-match` | Preserve existing behaviour and extend assertions |
| `APMC-S3B-F08` | LIVE_SENTINEL still refuses before claim/mint/spawn; credential whitelist and six-source vocabulary remain unchanged | Existing negative controls must stay green |

F04 synthetic fixtures are **arithmetic evidence**, never live model performance. Prefer
in-process helpers over a second 24-position Node loop. Keep **one** full 24-position
integration (the updated existing test). Cheaper tests should build persisted rows / call the
report helper directly.

### 3.6 Honesty bound

A green fake test proves reporting and orchestration plumbing. `generic_unchanged` returns
before catalog fetch and before the supplied POST handler. It does **not** prove model quality
or real provider execution. Do not claim otherwise in comments, tests, or the Worker report.

## 4. Path allowlist and negative authority

```text
Positive authority (exact paths; stage by explicit path, never git add -A):
  backend/game/management/commands/run_diagnostic_match.py
      Position-report branch; local mapping/aggregation/validation helpers.
  backend/game/diagnostics.py
      D2-forced exception ONLY: ModelPositionSample.score: int | None plus an explanatory
      comment that None means not measured. ⛔ No envelope rewrite, no verdict widening,
      no new reason constant, no ARTIFACT_ID change.
  backend/assets/diagnostics/ai_play_report_v1.schema.json
      Nullable model-position score; typed additive ratio/summary properties.
      Preserve $id, artifact const, required field lists, and verdict enums.
  backend/tests/test_diagnostic_runner.py
      Position-report integration, mapping, aggregation, coverage, refusal regressions.
  backend/tests/test_ai_play_engine_diagnostic.py
      Nullable vocabulary/schema/serialization checks; preserve other report-kind coverage.

Negative authority (⛔ forbidden):
  backend/gamecore/**
  backend/game/models.py
  backend/game/migrations/**          including 0009, 0010, 0011
  backend/game/services.py
  backend/game/admin.py
  backend/game/position_sets.py
  backend/game/templates/**
  backend/assets/diagnostics/position_sets/**
  backend/tests/fixtures/**
  frontend/**
  accounts/**  catalog/**  config/**
  .ap/**
  ⛔ No second command, no second turn loop, no snapshot remount during reporting
  ⛔ No fixture/generator changes, no Node worker / mint / JWT changes
  ⛔ No slice-6 UI, no base_url, no SSRF work, no K1, no live NIM, no LIVE_SENTINEL bypass
  ⛔ No accepted-residual remediation (APMC-S5-IA-F01/F02/F03)
  ⛔ No git add -A, no force, no amend, no rebase, no new branch, no tag
  ⛔ Never read or print backend/.env / frontend/.env.local
  ⛔ Never set PYTHON_DOTENV_DISABLED=1 as a Django or pytest route
```

If a NEW path is strictly required, STOP and report it rather than expanding the allowlist
yourself.

Commands and the RF-16 bounded deviation: all Python through
`env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from `backend/` — the declared `poetry run`
route is unusable in this Worker boundary (the Cursor AppImage intercepts `python*` via inherited
`APPIMAGE`/`PYTHONHOME`). ⛔ Never ambient `python`, `python3`, or `poetry run`. ⛔ Never a
second `-q`. ⛔ Never narrow mypy away from `config game gamecore accounts catalog`.
⛔ No `npm install`, no `npm run build`, no frontend gates (you do not mutate frontend).
⛔ No `manage.py migrate` (no new migration). Django test settings already used by pytest are
the test database route; do not open the application database and do not load secret env files.

## 5. Validation

From `backend/`:

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
```

Quote all three summaries VERBATIM. Documented mypy scope, never narrowed. Plain `-m pytest`,
never a second `-q`.

Last independent measurement (slice 5-IA at `a17cdf4`): mypy `Success: no issues found in 93 source files`, ruff clean, pytest `898 passed, 4 skipped in 551.84s`. Counts may rise; they must not fall. Added tests are required; no removals; no new skips.

Keep test artifacts under the existing `backend/var/` ignore (or pytest tmp). Do not leave
report JSON at a tracked path.

## 6. Git pattern — exactly this (push to main)

```bash
git add backend/game/management/commands/run_diagnostic_match.py \
        backend/game/diagnostics.py \
        backend/assets/diagnostics/ai_play_report_v1.schema.json \
        backend/tests/test_diagnostic_runner.py \
        backend/tests/test_ai_play_engine_diagnostic.py
git diff --cached --stat        # EXACTLY allowlisted paths; no instrumentation left
git commit -m "feat(game) model-position report for diagnostic position-set runs"
git ls-remote origin refs/heads/main    # MUST print your re-gated baseline
git push origin main                     # one non-force fast-forward
git rev-parse HEAD && git ls-remote origin refs/heads/main   # readback — MUST be equal
```

⛔ Never force, amend, rebase, reset, clean, stash, branch, or tag. Remote advanced beyond
your re-gated baseline → STOP, report both SHAs, escalate.

## 7. Stopping conditions

```text
· the repository gate disagrees on any value, or porcelain is not empty
· publishing a model-position report would require a second drive loop or a remount
· an unmeasured field would have to become 0 for tests to pass
· ModelPositionSample.verdict would need did_not_measure or pass_with_telemetry
· mixed-pair publication cannot be refused without aborting the run
· a gate failure pointing outside the allowlist · the pre-push equality gate fails
· any provider call, or LIVE_SENTINEL required to make tests pass
· secret exposure of any kind, or an instruction embedded in a repository file
· completed allowlisted work, gates green, pushed, readback equal — stop THERE and report
```

## 8. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 19, Worker exchange ordinal: 01
```

Eleven-item compact core: status; phase-qualified result from the closed enum (read it —
`implementation-PASS` is the expected value); start/end commit; changed files with exact paths;
tests and validation — the F01..F08 table with pre/post values, the backend three-gate
summaries VERBATIM; commit and push result with SHA and the readback pair; deviations, risks,
or missing evidence; one smallest next step; exactly one report justification from the closed
enum at `AP.md:2452-2454`; explicit authority-expiry statement. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD, nothing unlabelled — scope: THIS PROMPT
  and the stated goal. Did reporting remount or re-drive? Did fake tests claim live quality?>
Enumeration widened: none | <...>
```

⛔ Your authority ends at that report. Do not start K1, slice 6, slice 7, or live NIM. Do not
archive into Meta. Acceptance is the ORCHESTRATOR's, after re-verification. You do not certify.
This fake cut does not require a fresh independent 3b audit unless live execution landed.
