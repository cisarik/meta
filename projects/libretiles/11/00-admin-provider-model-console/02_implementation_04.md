You are a WORKER instance assigned to the persistent AP WORKER role. Exchange 05 — the final exchange of slice 1. The ORCHESTRATOR disposes of the unreproduced anomaly; this exchange executes that disposition and publishes the slice. Perform exactly this task and stop.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 02
Worker exchange ordinal: 05
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker — test-instrument redesign, gates, publication
Task identity: APMC-S1-PUBLISH — replace the unsound exact-tuple pins on wall-clock-capped configurations with a deterministic parity mode, keep every pre-existing assertion, run the full gates, and publish slice 1 with one commit and a verified push.
Phase: implementation
Continuity anchor: your exchange-04 BLOCKED report (435 unreproduced across three further full-suite-context runs; 18/18 ranked calls identical inputs and outputs; traversal 22,842-24,373 nodes at the same 750 ms cap with an identical selected output)
Authority renewal: prior authority expired; THIS prompt grants the test-file redesign and publication below
Why reuse is appropriate: same healthy session, candidate and full diagnosis context retained, no independence required
Retained context: convenience, not authority
Evidence posture: non-independent
Evidence tier: E1
Repository checkout topology: standalone checkout
Exact baseline: 3d7eae96d567a7004a927de45f53e16e2baf108f
Logical-whole closure: not-closed
```

## 1. ORCHESTRATOR disposition of the anomaly — final, execute mechanically

```text
D1  The 435 event is disposed as a TRANSIENT ENVIRONMENTAL EVENT during one full-suite run:
    unreproduced across five subsequent suite-context/standalone runs; 18/18 ranked calls carried
    identical inputs AND selected outputs across contexts; traversal at the 750 ms cap varies
    (22,842-24,373 nodes) with an UNCHANGED selected output; garbage collection occurs inside the
    timed region. Both H-A and H-B are unestablished. ⛔ No production-code correction is justified
    and none will be made.

D2  THE REAL DEFECT FOUND BY THIS DIAGNOSIS is the instrument: an exact-tuple pin on a
    wall-clock-capped search is load-sensitive and can false-positive on transient machine state —
    on ANY code, pre-fix or post-fix. This applies to EVERY such pin in your parity checks, not
    only strength. The pin caught an anomaly, the diagnosis ran, the instrument is now refined on
    evidence. That is the instrument working, then being made sound.

D3  THE REDESIGN (test files ONLY — ⛔ zero production-code changes):
    a. DETERMINISTIC PARITY MODE: the parity games keep the same seeds but configure the ranked
       calls to bind by NODES, not time — explicit kwargs on every call (e.g. max_nodes=20_000,
       max_elapsed_ms=10_000_000; you choose values that bind by nodes, stay fast, and are stable;
       defaults in move_search.py untouched — explicit kwargs are the fork-9-lawful shape, and
       SelfPlayConfig already carries bounds as fields). Pin the EXACT tuples there. ⭐ These pins
       are the permanent extraction-regression tripwire: any input-construction or ordering
       regression now fails deterministically, and timing flakes can no longer false-positive.
       Label the mode clearly in the test names/docstrings and state the reason in one comment
       (wall-clock cap makes exact pins load-sensitive; node-bound mode is deterministic).
       ⚠ The deterministic-mode tuples are NEW baselines captured from the candidate. The
       extraction-equivalence evidence is separate and already established (18/18 input/output
       identity, standalone production parity, pre-fix in-suite parity). Do not conflate them.
    b. PRODUCTION-CONFIG RUNS keep every PRE-EXISTING assertion (strength: all spreads > 0;
       matrix/English/Slovak: their own existing assertions) and RECORD the tuples by printing
       them — ⛔ no exact pins on any wall-clock-capped value anywhere.
    c. F1-F4 fail-before checks and the two-section pre-fix/post-fix table from exchange 02 stay
       in your report, updated to the final state.
```

## 2. Then publish — the full sequence, in order

```bash
# 1. gates, from backend/, the prescribed interpreter:
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
#    ⛔ documented mypy scope, never narrowed; plain -m pytest, never a second -q; quote every
#    summary verbatim. Expected: mypy 86 source files clean; ruff clean; pytest all passed with
#    your added tests and the deterministic pins green, 4 skipped, none removed.
# 2. stage by EXPLICIT PATH — exactly five files, never git add -A or git add .
git add backend/gamecore/selfplay.py \
        backend/tests/test_endgame_policy_matrix.py \
        backend/tests/test_full_game_simulation.py \
        backend/tests/test_slovak_full_game.py \
        backend/tests/test_strength_benchmark.py
# 3. verify the staged diff is EXACTLY these five files and contains NO temporary instrumentation
git diff --cached --stat
# 4. one commit, repo-style subject, e.g. "feat(gamecore) importable engine self-play core"
# 5. pre-push equality gate — MUST print 3d7eae96d567a7004a927de45f53e16e2baf108f
git ls-remote origin refs/heads/main
# 6. one non-force fast-forward push
git push origin main
# 7. public readback — local and remote MUST be equal; quote both
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

⛔ Never force, amend, rebase, reset, clean, stash, branch, or tag. If the pre-push gate prints a
different SHA, the remote advanced: STOP, report both SHAs, commit nothing, escalate.

## 3. Boundaries

```text
· Positive authority: the five paths only. Test-file redesign inside them; ⛔ selfplay.py must end
  this exchange byte-identical to how it started it (production code is DONE — if you believe it
  needs a change, STOP and report instead).
· Negative authority: everything else per exchange 01 §4. ⛔ No new files. ⛔ No bounds changes in
  production code; explicit kwargs in tests only. ⛔ No assertion removal — pre-existing
  assertions all stay; the ONLY assertions that change are the Worker-added exact pins moving
  from wall-clock-capped to node-bound configurations.
· Interpreter: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from canonical backend/
  (works there; the worktree route is NOT needed this exchange). ⛔ Never ambient
  python/python3/poetry run; ⛔ no environment reconstruction.
· Network: the authorized Git push and ls-remote only. ⛔ No provider call. ⛔ No worktree, no
  new /tmp artifacts.
```

## 4. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 02, Worker exchange ordinal: 05
```

Eleven-item compact core: status; phase-qualified result from the closed enum (read it —
`implementation-PASS` is the expected value); start/end commit; changed files with exact paths;
tests and validation — the three gate summaries VERBATIM, the new deterministic-mode tuples (the
new pins, listed), one line confirming selfplay.py ended byte-identical; commit and push result
with the SHA and the readback pair; deviations, risks, or missing evidence; one smallest next
step; exactly one report justification from the closed enum at AP.md:2453-2454; explicit
authority-expiry statement. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD, nothing unlabelled — scope: this prompt, the
  disposition D1-D3, and the deterministic-mode design. Are the chosen node bounds genuinely
  binding-by-nodes and fast? Would 20_000 be too tight to discriminate the policies?>
Enumeration widened: none | <...>
```

⛔ Authority ends at this report. The push is the exchange's last mutation. Do not start slice 2,
do not archive into Meta. Acceptance is the ORCHESTRATOR's, after re-verification.
