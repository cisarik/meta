### Report for ORCHESTRATOR_CHAT

Logical whole identity: admin-provider-model-console  
Worker session ordinal: 02, Worker exchange ordinal: 04

**Status: BLOCKED**  
Phase-qualified result: `not-applicable`

The original `435` result did not reproduce. Both diagnostic full-suite runs passed the unchanged strength parity assertion at **420**. No causal input/output divergence was found, so no hypothesis-specific correction was justified or applied.

Start/end commit: `3d7eae96d567a7004a927de45f53e16e2baf108f`.

The same five candidate paths remain uncommitted, unchanged by this exchange after instrumentation removal:

- `backend/gamecore/selfplay.py`
- `backend/tests/test_endgame_policy_matrix.py`
- `backend/tests/test_full_game_simulation.py`
- `backend/tests/test_slovak_full_game.py`
- `backend/tests/test_strength_benchmark.py`

Validation:

| Run | Strength `(300, 0)` spread | Summary, verbatim |
|---|---:|---|
| Instrumented standalone | 420 | `1 passed in 17.35s` |
| Instrumented full suite | 420 | `825 passed, 4 skipped in 425.54s (0:07:05)` |
| Full suite, unchanged production candidate; dump written after gameplay | 420 | `825 passed, 4 skipped in 427.38s (0:07:07)` |

**H-A/H-B findings:** All **18 ranked calls** had identical recorded inputs and selected outputs across the standalone run and both suite runs. H-A was not observed. Internal timing varied, but H-B as the cause of the original output difference remains unproved.

Representative ply **31**:

```text
Input SHA-256:
c4aae79a7609b4e44f51a97865d7c6c9e54d4256dddd03bd948cfa71bd3c0ba9

Rack: ("B", "D", "R", "R", "O", "?", "I")
Bag count: 1
Bounds: max_nodes=500000, max_elapsed_ms=750,
        top_k=8, max_unique_placements=25000
Differing input fields: none
Selected canonical key: ((2, 5, "D", ""), (3, 5, "?", "S"))
Selected score: 29

Standalone:             23338 nodes, 750 ms
Instrumented suite:     23067 nodes, 750 ms
Post-game capture suite:23016 nodes, 750 ms
```

An additional bounded probe repeated that exact position ten times: every call selected score `29` and the same canonical key, while traversal ranged from **22,842 to 24,373 nodes**, always capped at `750 ms`.

Garbage collection was observed inside timed searches, but no observed collection caused a selected-output difference. This does not establish snapshot capture as the original cause.

Commit/push: **none**. No final publication gate sequence was run because no corrective result was established. Mypy and Ruff were not rerun in this exchange.

Cleanup: all temporary instrumentation was removed. Both instrumented files were verified byte-for-byte against their entry versions. These three dump files were deleted and their absence verified:

- `/tmp/opencode/apmc-s1-standalone.jsonl`
- `/tmp/opencode/apmc-s1-suite.jsonl`
- `/tmp/opencode/apmc-s1-suite-postgame.jsonl`

Final porcelain contains exactly the original five candidate paths. `git diff --check` passed.

Resolved Execution Issues / Near-Misses: a large dump exceeded tool-output limits; bounded summaries were subsequently read from the intact file. A second observation method wrote existing snapshots only after gameplay to remove search-time instrumentation effects.

Pre-Existing Failure Classification: none established. The Orchestrator’s supplied baseline measurements remain non-independent evidence; their missing suite summaries remain a limitation.

Orchestration critique:

- **MEASURED:** The prescribed comparison produced identical inputs **and** outputs, leaving neither diagnostic divergence case established. Green repetitions alone do not demonstrate a correction.
- **LEAD:** Exact final-score parity may be fragile for a wall-clock-capped policy. Variable traversal was demonstrated; selected-output variability was not reproduced here.

Enumeration widened: timing checkpoints include garbage-collection work; post-game snapshots provide an observation method that leaves production search execution unchanged.

Smallest next step: Orchestrator disposition of the unreproduced anomaly before further correction or publication.

Context pressure: moderate.  
Report justification: `new-evidence`.

Authority expires with this report. Logical-whole closure remains `not-closed`; acceptance belongs to the Orchestrator.