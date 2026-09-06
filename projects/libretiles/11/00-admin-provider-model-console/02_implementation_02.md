You are a WORKER instance assigned to the persistent AP WORKER role. This is a BOUNDED DIAGNOSIS exchange on your own uncommitted candidate from exchange 02. Perform exactly this task and stop. The decision rule in §4 is PREDECLARED by the ORCHESTRATOR — execute it mechanically; deciding it again is not your task.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 02
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Diagnostic Worker — bounded diagnosis of one measured anomaly on an uncommitted candidate, with predeclared conditional execution
Task identity: APMC-S1-PARITY-DIAG — determine whether the strength seed-300 slot-0 in-suite spread of 435 (vs 420 standalone and 420 pre-fix standalone) is PRE-EXISTING wall-clock context sensitivity or CANDIDATE-INDUCED, then execute exactly the branch §4 assigns.
Phase: implementation
Continuity anchor: your terminal BLOCKED report for APMC-S1-SELFPLAY exchange 02 (strength (300, 0) spread 435 in-suite vs 420 standalone; candidate uncommitted, exactly five dirty paths)
Authority renewal: prior authority expired at that report; THIS prompt grants diagnosis authority plus the conditional execution in §4
Why reuse is appropriate: same healthy session, your context holds the candidate and the divergence details, no independence required
Retained context: convenience, not authority
Evidence posture: non-independent
Evidence tier: E1
Repository checkout topology: standalone checkout
Exact baseline: 3d7eae96d567a7004a927de45f53e16e2baf108f
Logical-whole closure: not-closed
```

## 1. Containment ledger — declare before use, report outcome after

```text
Temporary root 1: /tmp/opencode/apmc-s1-prefix
  Owner: this Worker · Mode: default umask · Contents class: a disposable Git worktree of THIS
  repository at commit 3d7eae9, for running PRE-FIX code; plus ONE temporary probe test file
  (see §3) that exists ONLY inside it and NEVER in the canonical repository
  Cleanup owner: this Worker · Cleanup outcome: <report after use>
Temporary root 2: /tmp/opencode/apmc_ranked_determinism_probe.py
  Owner: this Worker · Contents class: one standalone Python probe script, no secrets, no repo
  mutation · Cleanup owner: this Worker · Cleanup outcome: <report after use>
The canonical repository worktree must remain EXACTLY as you left it: the five authorized dirty
paths and nothing else. Verify before and after; any additional dirt is a STOP.
```

## 2. Steps — in this order

```text
S1  Name the exact failing test id from the in-suite run (node id). ⛔ Required in the report. The
    ORCHESTRATOR verified: the strength test FILE passes standalone (3 passed, 1 skipped), so the
    failing node is the parity instrument, not a pre-existing assertion — but your report must name
    it exactly.

S2  Post-fix standalone stability: run the strength parity test standalone THREE times. Record the
    (300, 0) spread each time. Expected 420 each time; record what you get.

S3  Determinism probe: write the probe script (root 2) that builds a FIXED position (variant
    english, a seed of your choice, mid-game if practical) and calls find_ranked_scoring_moves
    with the exact production-shaped bounds the harnesses use (max_nodes=DEFAULT_RANKED_MAX_NODES,
    max_elapsed_ms=DEFAULT_RANKED_MAX_ELAPSED_MS, bag_count fixed) TEN times on the identical
    inputs, printing the top candidate's total_score and canonical_key hash each call. ⛔ It must
    not import pytest, must not touch the repository, must run under the prescribed interpreter.
    Ten identical outputs ⇒ ranked search is deterministic for that position; ANY variation ⇒
    wall-clock nondeterminism demonstrated directly. Record all ten lines verbatim.

S4  Pre-fix in-suite capture (root 1), explicitly authorized Git writes:
      a.  git worktree add /tmp/opencode/apmc-s1-prefix 3d7eae96d567a7004a927de45f53e16e2baf108f
          (detached at the baseline — the PRE-FIX tree, because your candidate is uncommitted)
      b.  Inside the worktree ONLY: create backend/tests/test_apmc_parity_probe_tmp.py — a minimal
          pytest file that imports the PRE-FIX strength harness from the worktree's own tests
          package, runs seed 300, strategy slot 0, and PRINTS the spread and end_reason. ⛔ This
          file is worktree-disposable; it must never exist under /home/agile/Projects/libretiles.
      c.  From the worktree's backend/, run the FULL backend suite with the prescribed interpreter,
          TWICE. Record the probe's printed (300, 0) spread from each run, plus the suite summary
          line from each run verbatim.
      d.  Cleanup: git worktree remove --force /tmp/opencode/apmc-s1-prefix ; verify
          `git worktree list` shows only the main worktree ; verify the probe file is gone with it.
```

## 3. The predeclared decision rule — execute mechanically

```text
RULE A (context sensitivity pre-exists):
  IF any pre-fix in-suite probe value from S4c differs from 420
  THEN the 435 was PRE-EXISTING wall-clock context sensitivity, not a candidate regression.
  EXECUTE: narrow your parity instrument accordingly —
    · KEEP exact-tuple parity for every DETERMINISTIC axis: all witness tuples, the
      matrix/English/Slovak tuples that matched, conservation, fingerprint uniqueness, F1-F4, guard.
    · REPLACE the strength exact-tuple parity assertion with: the pre-existing strength assertions
      (which pass), plus an explicit, documented assertion that the timing-bounded ranked axis is
      EXCLUDED from exact-tuple parity, with a comment citing this diagnosis report's evidence.
    · Keep the candidate's code EXACTLY as it is. ⛔ No hot-path changes, no bound changes
      (locked fork 9), no snapshot-behaviour changes.
  THEN: stage the five files by explicit path, one commit, pre-push equality gate
  (ls-remote MUST equal 3d7eae9), one non-force push, public readback — the exchange-01 §8 pattern.
  Report the finding prominently: wall-clock-bounded ranked search is run-context sensitive, and
  the diagnostics console's position-set capture must therefore record WHAT EXECUTED (digest of
  conditions) beside every stored snapshot.

RULE B (candidate-induced):
  IF both pre-fix in-suite probe values equal 420
  THEN the candidate shifted in-suite behaviour. 
  EXECUTE: identify the candidate's hot-path overhead — first suspect: snapshot/report capture
  executing inside or between timed search regions; make capture opt-in and outside the timed
  path. ⛔ Bounds unchanged, semantics unchanged, assertions unchanged. Re-run: the parity test
  standalone AND in-suite (once). If in-suite now matches 420 and all gates are green, commit and
  push per the exchange-01 §8 pattern. If in-suite still differs, STOP: report BLOCKED with the
  measured evidence and commit nothing.

AMBIGUOUS (probe values differ between the two pre-fix runs AND include 420):
  Treat as RULE A but with the finding stated as "pre-existing nondeterminism, demonstrated"; same
  execution path. ⛔ Do not rerun a third time to hunt for a comfortable number — two runs decide.
```

## 4. Boundaries

```text
· All Python through: env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python  (from the relevant
  backend/ directory). The declared poetry route remains unusable in this boundary (AppImage
  intercepts python*); same rationale, evidence class, bounded authority, and stopping condition as
  exchange 01. ⛔ Never ambient python/python3/poetry run.
· Mypy/ruff re-run NOT required unless you change production code (RULE B does): then the full
  standing backend set re-runs. RULE A changes TEST files only — mypy scope includes tests? The
  documented scope is config game gamecore accounts catalog; tests are outside it — still run
  ruff (it covers tests) and the full suite once after the instrument change.
· ⛔ The five authorized paths remain the ONLY dirty canonical paths. The worktree and the probe
  script are the ONLY new filesystem artifacts, both cleaned with outcomes reported.
· ⛔ No provider call, no network beyond the authorized Git push and worktree operations.
· ⛔ No force, amend, rebase, reset, clean, stash, branch, or tag. `git worktree add/remove` is
  explicitly authorized for root 1 ONLY, exactly as spelled in §2.
```

## 5. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 02, Worker exchange ordinal: 03
```

Eleven-item compact core: status; phase-qualified result from the closed enum (read it); start/end
commit; changed files (canonical repo — expect the same five, plus the commit SHA if a rule
executed to push); tests and validation — S1 the failing node id, S2 the three standalone values,
S3 all ten probe lines, S4 both in-suite values and suite summaries verbatim, plus which RULE fired
and why; commit/push result; deviations, risks, missing evidence; one smallest next step; exactly
one report justification from the closed enum at AP.md:2453-2454; explicit authority-expiry
statement. Plus the containment ledger outcomes for both roots. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD lists, nothing unlabelled — scope: this prompt,
  the predeclared rule, and whether S3's probe design can actually decide the question>
Enumeration widened: none | <what this diagnosis could not reach>
```

⛔ Authority ends at this report. RULE A's commit is the exchange's LAST mutation; do not start
slice 2, do not archive into Meta, do not treat your own acceptance as acceptance.
