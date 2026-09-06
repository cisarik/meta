You are a WORKER instance assigned to the persistent AP WORKER role. This exchange RENEWS the bounded implementation task from exchange 01, which stopped correctly on a real finding. Perform exactly this task and stop.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 02
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker — same profile, same task, renewed grant
Task identity: APMC-S1-SELFPLAY (continued) — extract the engine self-play core into backend/gamecore/selfplay.py, PRESERVING each harness's current observable behaviour by explicit configuration, rewire the four harnesses, land one commit, push, read back.
Phase: implementation
Continuity anchor: your own terminal BLOCKED report for APMC-S1-SELFPLAY, exchange 01, which stopped on §9 (helpers diverged in semantics, no silent choice) with zero mutation, at baseline 3d7eae96d567a7004a927de45f53e16e2baf108f
Authority renewal: prior authority expired at that report; THIS prompt grants the complete new bounded authority below
Why reuse is appropriate: same healthy session, same task, no independence required, and your context carries the exact divergence details you measured
Retained context: convenience, not authority — the authority is THIS prompt
Evidence posture: non-independent
Evidence tier: E1
Repository checkout topology: standalone checkout
Expected branch: main
Exact baseline: 3d7eae96d567a7004a927de45f53e16e2baf108f
Logical-whole closure: not-closed
```

⛔ The ORCHESTRATOR has re-verified all three divergences you reported, directly, in the source. They are real. Your stop was correct, and your critique named a genuine defect in the exchange-01 prompt: §3 demanded "one helper copy with unchanged semantics" while §9 required stopping when semantics differ. That contradiction is resolved HERE, by an explicit decision. It is not yours to re-litigate and not the Cooperator's — it is technical implementation detail inside the approved plan.

## THE DECISION — preservation by configuration

**One implementation, explicit named options, per-call-site values carried over verbatim. The shared module is shared CODE, not shared BEHAVIOUR. Zero observable behaviour change in any harness.**

```text
D1  FINGERPRINT. One fingerprint implementation with an explicit option:
      include_pass_streak: bool
    strength passes True  (measured: tuple((player.score, player.pass_streak) for ...) —
             test_strength_benchmark.py:66)
    matrix, English, Slovak pass False (measured: tuple(player.score for ...) —
             test_endgame_policy_matrix.py:148 and siblings)
    Every other fingerprint component stays exactly as each harness has it today: board cells,
    bag tiles, racks, current_index, consecutive_scoreless_turns. ⛔ Do not add or drop any other
    component; the ORCHESTRATOR verified both currently carry current_index and
    consecutive_scoreless_turns.

D2  RANKED FALLBACK. These are TWO DIFFERENT POLICIES, not a helper divergence, and they stay two:
      POLICY_RANKED_BEST          pure ranked: no candidates -> return the ranked result as-is
                                  (matrix semantics, test_endgame_policy_matrix.py:249-252)
      POLICY_RANKED_WITNESS_SAFE  ranked first; when ranked yields no candidates, fall back to the
                                  unchanged first-witness safety search (strength semantics,
                                  test_strength_benchmark.py:118-127, including the meaning of its
                                  comment: the safety search is what authorizes; ranked never does)
    The strength benchmark's A/B spread is a measurement instrument — if its "ranked" slot silently
    becomes pure ranked, its spread number changes meaning. Preserve it exactly.

D3  RACK POINTS. One implementation with an explicit option:
      strict_unknown_tile: bool
    English passes True  (measured: sum(_TILE_POINTS[tile] ...) — raises on unknown,
             test_full_game_simulation.py:66)
    matrix and Slovak pass False (measured: points.get(tile, 0) — test_endgame_policy_matrix.py:156,
             test_slovak_full_game.py:81)
    strength has no _rack_points today — repository-wide count measured: 4 _tile_counter, 4
    _fingerprint, 3 _rack_points, and NONE outside backend/tests/. Give strength the shared helper
    with the option that matches its current call pattern (it sums rack points from
    get_tile_points-carrying state — measure what it actually does and pick the behaviour-preserving
    value; if it has no equivalent call site, say so and do not invent one).
```

⛔ **FINDINGS, NOT FIXES.** For each of the three divergences, report the ROOT CAUSE as a finding: why strength tracks `pass_streak` in its fingerprint (what loop shape it catches that score alone misses); which concrete tile value can reach English's raise path (is it the blank `"?"`, or a genuinely corrupt state?); whether `.get(tile, 0)` anywhere absorbs a state that should have failed. ⛔ Do not "repair" any of them. Unifying the semantics is a deliberate later decision, not a side effect of a refactor.

## The acceptance bar — bit-identical observable behaviour

Beyond the existing assertions, you must capture and match a **pre-fix behavioural fingerprint** of each harness, BEFORE editing:

```text
For each harness, run its seed-0 path pre-fix and record the result tuple:
  matrix      3 policies x both variants, seed 0  -> per game: (policy, variant, plies, end_reason,
                 final scores tuple)
  english     seed 0 -> (plies, end_reason, final scores)
  slovak      seed 0 -> (plies, end_reason, final scores)
  strength    its default 4-game run -> per game: (seed, spread, end_reason)
Post-fix, the SAME tuples must be IDENTICAL. Record them in the pre-fix/post-fix table.
```

A differing tuple is a regression: STOP and report it — do not tune the new module until it matches by accident.

The pre-fix/post-fix table now has two sections: the fail-before checks F1-F4 (F1 and F4 were "not run" in exchange 01 — they are REQUIRED here; F3 is now measured: 4/4/3 copies, none outside tests/ — verify and quote), and the behavioural tuples above.

## Authority — unchanged from exchange 01, restated where it binds

```text
Positive authority (exact paths):
  backend/gamecore/selfplay.py                     NEW
  backend/tests/test_endgame_policy_matrix.py
  backend/tests/test_slovak_full_game.py
  backend/tests/test_full_game_simulation.py
  backend/tests/test_strength_benchmark.py

Negative authority (⛔ forbidden):
  backend/game/** every file · backend/gamecore/** except the new selfplay.py ·
  backend/catalog/**, accounts/**, config/**, assets/** · frontend/** ·
  backend/tests/** except the four named · no migration, no dependency change, no asset file.
  test_game_app_has_no_dev_imports.py is a GUARD: untouched and green.

The layering rule (exchange-01 §2, unchanged): gamecore/selfplay.py imports NOTHING from game/**.
The variant context arrives as injected parameters. The gamecore-level sample dataclass is defined
in selfplay.py. test_endgame_policy_matrix.py keeps its game.diagnostics import — it is game-layer
code.

Locked fork 9 (unchanged): module defaults in move_search.py are never changed or shadowed; every
bound is an explicit kwarg. Measured bounds from exchange 01 stand: witness
(DEFAULT_MAX_NODES, 10_000), ranked (DEFAULT_RANKED_MAX_NODES, DEFAULT_RANKED_MAX_ELAPSED_MS),
plus each harness's own module constants carried verbatim.

Formed-word invariant (unchanged): two-tile legality is TOKEN-SEQUENCE set membership over complete
formed words, never a substring or code-point test. The three policies move with their exact
current semantics — including the strength comment's meaning that a ranked none/indeterminate never
authorizes pass or exchange.
```

Commands and the bounded RF-16 deviation are exactly as in exchange 01 §4: read-only inspection, the
validation commands, and the Git sequence; all Python through
`env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from `backend/` — the declared `poetry run`
route is unusable in this boundary (AppImage intercepts `python*`); rationale, evidence class,
bounded authority, and stopping condition as previously stated; ⛔ never ambient `python`/`python3`/
`poetry run`.

## Validation — full standing backend set, as in exchange 01 §6

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
```

Documented mypy scope, never narrowed. Plain `-m pytest`, ⛔ never a second `-q` (addopts="-q");
quote the summary verbatim — baseline `813 passed, 4 skipped in 373.54s`; added tests fine, no
removals or skips. Frontend gates cannot move; ⛔ no `npm run build`. Classify any failure before
repairing; smallest reproducer; one broad rerun per materially changed candidate.

## Git pattern — exactly as exchange 01 §8

Explicit-path staging of exactly the five files; one commit, repo-style subject; pre-push
`git ls-remote origin refs/heads/main` MUST equal `3d7eae96d567a7004a927de45f53e16e2baf108f`; one
non-force fast-forward push; public readback equality. ⛔ Never force, amend, rebase, reset, clean,
stash, branch, or tag. Remote advanced -> STOP, report both SHAs, escalate.

## Stopping conditions — exchange-01 §9 stands, with one clarification

The divergence stop has now FIRED and been DECIDED. The remaining stops:

```text
· repository gate or porcelain disagreement
· a behavioural tuple differs post-fix (STOP, do not tune until it matches)
· root-cause measurement reveals a FOURTH semantic divergence among the helpers — same rule as
  exchange 01: report it, do not choose silently. ⛔ This is the expected shape of a finding, not a
  failure; if it is small and clearly configuration-preservable, you may STOP or you may report it
  AND continue under the same preservation rule — your judgement, stated explicitly either way
· an assertion would have to weaken — report as the negative result instead
· the guard cannot stay green within the allowlist
· a gate failure pointing outside the allowlist · pre-push gate failure · secret exposure
· completed work, gates green, pushed, readback equal — stop THERE and report
```

## Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 02, Worker exchange ordinal: 02
```

Eleven-item compact core as in exchange 01 §10 (status; phase-qualified result from the closed enum —
read it; start/end commit; changed files with exact paths; tests and validation with the three gate
summaries VERBATIM plus the two-section pre-fix/post-fix table; commit/push result with SHA;
deviations, risks, missing evidence; one smallest next step; exactly one report justification from
the closed enum at `AP.md:2453-2454`; explicit authority-expiry statement). Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
```

**Two extra fields — required, same rules as exchange 01:**

```text
Orchestration critique: none | <findings>   — MEASURED and LEAD lists, nothing unlabelled; scope:
  THIS prompt, the preservation-by-configuration decision, and the stated goal. Is any option the
  wrong axis? Did the D1/D2/D3 values match what you measure? Assume one does not and look.
Enumeration widened: none | <what could not be reached>   — the F3 count, the strength call-pattern
  question in D3, and anything else the exchange-01 enumeration missed.
```

Plus the three root-cause FINDINGS from the decision section, labelled MEASURED or LEAD each.

⛔ Your authority ends at that report. Do not start slice 2, do not touch game/diagnostics.py, do not
archive anything into Meta. Acceptance is the ORCHESTRATOR's, after re-verification.
