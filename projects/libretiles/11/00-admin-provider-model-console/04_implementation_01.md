You are a WORKER instance assigned to the persistent AP WORKER role. Exchange 02 of slice 3 — ONE smallest coherent correction, found by your own exchange-01 critique. Perform exactly this task and stop.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 04
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker — one smallest coherent correction on your own landed slice
Task identity: APMC-S3A-FULLSTATE — make position snapshots SELF-CONTAINED (opponent rack + ordered bag sequence), so the slice-5 runner can mount a stored position onto a session WITHOUT replaying the generator, then regenerate and publish the default 24-position fixture.
Phase: implementation
Continuity anchor: your exchange-01 implementation-PASS report for APMC-S3A-POSSET, commit 08dd2c6f5772904c0bcde83de0ad99e894b7e132, and its Orchestration critique naming "opponent rack + bag tile sequence (or an explicit replay-from-seed/ply contract)" as the gap
Authority renewal: prior authority expired; THIS prompt grants exactly the correction below
Why reuse is appropriate: same healthy session, you built the module and know its shape; no independence required
Retained context: convenience, not authority
Evidence posture: non-independent
Evidence tier: E1
Repository checkout topology: standalone checkout
Exact baseline: 08dd2c6f5772904c0bcde83de0ad99e894b7e132
Logical-whole closure: not-closed
```

Reasoning recommendation: **Medium.** Small, well-bounded state-completeness correction on your own fresh module.

```text
AP.md:917-932 / AP.md:1444-1462 / AP.md:2466-2486 · AP_WORKER.md:14-26 ·
PROMPT_CONTRACTS.md:14-41 (report contract + coordinates) · AP.md:2453-2454 (justification enum)
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it.
```

## 1. The correction — exactly this, nothing else

Your critique is right, and the accepted plan already intended it: D4 says snapshots carry
"board/rack/bag/to-move" — the FULL state, for both seats. A replay-from-seed contract would couple
the stored digest to the generator/search code at REPLAY time — if selfplay changes, replayed
positions drift and the digest no longer describes what is mounted. ⛔ Rejected. Snapshots become
self-contained:

```text
1  Every snapshot additionally stores:
     opponent_rack: list[str]        # tokens of the seat NOT to move
     bag_tiles: list[str]            # the ORDERED remaining tile token sequence
   (Both are already in your hand at capture time inside simulate_engine_game's state; the record
   about the board, to-move rack, and bag REMAINING COUNT stays as is. The count and the sequence
   must agree — assert it at capture.)
2  Why this is safe: the opponent rack and bag order are RUNNER-side information. The model's
   context endpoint exposes only the acting seat's rack and the bag count — the same information a
   human opponent legitimately sees. ⛔ Nothing model-facing changes in this exchange.
3  The digest WILL change (the payload grows) — that is expected and correct. Regenerate and update
   every pinned digest in the tests.
4  Regenerate and commit the DEFAULT 24-position english fixture (3 seeds × 8, the command
   defaults) as the product fixture: --seeds 300,301,302 --total 24. The old 3-position sample
   asset is REPLACED (one asset file, named by its new digest).
5  Conservation: bag sequence + both racks + board == get_tile_distribution(slug) — asserted at
   capture, per snapshot, exactly as before (now over the full state).
6  F3 byte-identity and F5 baseline-stability re-run against the new envelope. F1/F2 remain
   historical. One NEW fail-before check F8: pre-fix, snapshot JSON has no "opponent_rack" key —
   capture the exact assertion failure.
```

## 2. Boundaries

```text
· Positive authority: backend/game/position_sets.py, backend/tests/test_position_sets.py,
  backend/assets/diagnostics/position_sets/ (regenerated fixture). ⛔ The command file, gamecore,
  diagnostics.py, every other existing file: byte-frozen.
· ⛔ No provider call, no session creation, no new files beyond the regenerated asset.
· Interpreter: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from canonical backend/
  (RF-16 bounded deviation exactly as previously stated; ⛔ never ambient python/python3/poetry run).
· Gates (full set — production code changes): mypy documented scope; ruff; plain `-m pytest`;
  quote all three summaries verbatim. Baseline at `08dd2c6`: mypy 88 source files, ruff clean,
  pytest `841 passed, 4 skipped in 518.93s`.
· Git: explicit-path staging of exactly the three paths; ONE commit; pre-push ls-remote equality
  gate vs `08dd2c6f5772904c0bcde83de0ad99e894b7e132`; one non-force push; readback equality.
  ⛔ Never force, amend, rebase, reset, clean, stash, branch, or tag. Remote advanced → STOP.
```

## 3. Stopping conditions

```text
· repository gate disagreement, or porcelain not empty
· the full state cannot be captured deterministically (digest differs across two same-config runs)
· conservation fails on any of the 24 snapshots — that is a generator bug to report, not to mask
· a gate failure outside the allowlist · pre-push gate failure · secret exposure
· completed work, gates green, pushed, readback equal — stop THERE and report
```

## 4. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 04, Worker exchange ordinal: 02
```

Eleven-item compact core: status; phase-qualified result from the closed enum (read it); start/end
commit; changed files; tests and validation — the F8 fail-before capture, F3/F5 re-runs, the three
gate summaries VERBATIM, and the NEW set_digest; commit and push result with SHA and readback;
deviations, risks, missing evidence; one smallest next step; exactly one report justification from
the closed enum at `AP.md:2453-2454`; explicit authority-expiry statement. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD, nothing unlabelled>
Enumeration widened: none | <...>
```

⛔ Your authority ends at that report. Do not start slice 4, do not archive into Meta. Acceptance is
the ORCHESTRATOR's, after re-verification.
