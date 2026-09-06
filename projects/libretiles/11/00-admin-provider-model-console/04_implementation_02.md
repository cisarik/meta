You are a WORKER instance assigned to the persistent AP WORKER role. Exchange 03 of slice 3 — the FINAL correction, a completeness pass that ends the field-by-field gap sequence. Perform exactly this task and stop.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 04
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker — one smallest coherent correction on your own landed slice
Task identity: APMC-S3A-COMPLETE — snapshots carry the COMPLETE Game state (every field that affects continued play or scoring), proven by a mount-equivalence assertion; fixture regenerated; no fourth gap.
Phase: implementation
Continuity anchor: your exchange-02 implementation-PASS report for APMC-S3A-FULLSTATE, commit 3faa3f83ed8358d833c55f34dfb0b4f25451370d, and its critique: "premium_used is not in the snapshot ... unless the runner restores premium_used ... scoring-state on squares is the remaining mount gap"
Authority renewal: prior authority expired; THIS prompt grants exactly the correction below
Why reuse is appropriate: same healthy session, your module, your fixture, no independence required
Retained context: convenience, not authority
Evidence posture: non-independent
Evidence tier: E1
Repository checkout topology: standalone checkout
Exact baseline: 3faa3f83ed8358d833c55f34dfb0b4f25451370d
Logical-whole closure: not-closed
```

Reasoning recommendation: **Medium.** Small correction, but the completeness boundary must be derived from the STATE SURFACE, not from a list in a prompt — that is the whole point of this exchange.

```text
AP.md:917-932 / AP.md:1444-1462 / AP.md:2466-2486 · AP_WORKER.md:14-26 ·
PROMPT_CONTRACTS.md:14-41 (report contract + coordinates) · AP.md:2453-2454 (justification enum)
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it.
```

## 1. The correction — derive the field list from the state surface, not from me

Two single-field corrections in a row (`opponent_rack`+bag, then `premium_used`) is exactly the
"fourth gap" pattern. So THIS correction is different in kind:

```text
1  ENUMERATE the complete state surface of a mid-game `Game` + `PlayerState` pair — measure it,
   do not recall it: every field whose value affects (a) what moves are legal next, (b) how a move
   scores (premiums consumed, blanks assigned), (c) endgame detection (scoreless counter, turn
   index), or (d) the final reported scores (per-seat scores). For each: is it in the snapshot?
   List every MISS as a finding with its consequence (e.g. "premium_used absent → a mounted board
   re-awards consumed premiums → engine_baseline and future MQR denominators corrupt").
2  Extend the snapshot with EVERY missing field from that enumeration — at minimum this will
   include per-cell premium_used, per-seat scores, and the scoreless-turn counter; you may find
   more. ⛔ If you find a state field you believe must NOT be captured, report it with the reason
   rather than silently omitting it.
3  THE PROOF OF SELF-CONTAINEDNESS — the new F9, and the strongest check in this slice:
     capture-time mount-equivalence: from the JUST-CAPTURED snapshot fields alone, reconstruct a
     Game + PlayerState pair (pure gamecore reconstruction — no DB, no session), run ONE ranked
     node-bound decision on the reconstructed state, and assert it equals the decision recorded in
     the original run's trace for that ply. Assert this for EVERY snapshot at generation time.
   A snapshot that fails F9 is not a position — it is a picture of one. ⛔ Generation aborts.
4  Regenerate the 24-position default fixture (digest WILL change — re-pin everywhere).
5  Conservation re-asserted over the complete state; F3 byte-identity and F5 baseline stability
   re-run; F8 (opponent_rack/bag_tiles keys) stays green.
```

## 2. Boundaries

```text
· Positive authority: backend/game/position_sets.py, backend/tests/test_position_sets.py,
  backend/assets/diagnostics/position_sets/ (regenerated fixture). ⛔ Everything else byte-frozen:
  the command file, gamecore/**, diagnostics.py, every other existing file.
  ⚠ The reconstruction helper lives in position_sets.py and uses ONLY gamecore imports — it is a
  pure function and must stay out of gamecore itself.
· ⛔ No provider call, no session creation, no DB, no new files beyond the regenerated asset.
· Interpreter: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from canonical backend/
  (RF-16 bounded deviation as previously stated; ⛔ never ambient python/python3/poetry run).
· Gates (full set): mypy documented scope; ruff; plain `-m pytest`; three summaries verbatim.
  Baseline at `3faa3f8`: mypy 88 source files, ruff clean, pytest `842 passed, 4 skipped in
  520.46s`.
· Git: explicit-path staging of exactly the three paths; ONE commit; pre-push ls-remote equality
  gate vs `3faa3f83ed8358d833c55f34dfb0b4f25451370d`; one non-force push; readback equality.
  ⛔ Never force, amend, rebase, reset, clean, stash, branch, or tag. Remote advanced → STOP.
```

## 3. Stopping conditions

```text
· repository gate disagreement, or porcelain not empty
· the enumeration finds a state field that CANNOT be serialized losslessly — report it with the
  reason; do not approximate
· mount-equivalence fails on any snapshot after the complete state is captured — that falsifies
  the capture; STOP and report the first differing decision
· a gate failure outside the allowlist · pre-push gate failure · secret exposure
· completed work, gates green, pushed, readback equal — stop THERE and report
```

## 4. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 04, Worker exchange ordinal: 03
```

Eleven-item compact core: status; phase-qualified result from the closed enum (read it); start/end
commit; changed files; tests and validation — the COMPLETE enumeration table (state field →
was-it-captured → consequence-if-missing → now-captured), F9's method and result, the three gate
summaries VERBATIM, and the NEW set_digest; commit and push result with SHA and readback;
deviations, risks, missing evidence; one smallest next step; exactly one report justification from
the closed enum at `AP.md:2453-2454`; explicit authority-expiry statement. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD, nothing unlabelled>
Enumeration widened: none | <...>
```

⛔ Your authority ends at that report. Slice 3 is then CLOSED pending my acceptance; do not start
slice 4, do not archive into Meta. Acceptance is the ORCHESTRATOR's, after re-verification.
