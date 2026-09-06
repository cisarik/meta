You are a WORKER instance assigned to the persistent AP WORKER role. Exchange 04 of the bounded slice-1 task. The ORCHESTRATOR has completed the S4 measurement you could not; RULE B is now the predeclared branch. Perform exactly this task and stop.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 02
Worker exchange ordinal: 04
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Diagnostic Worker — bounded diagnosis and one smallest coherent correction on your own uncommitted candidate
Task identity: APMC-S1-PARITY-FIX — determine WHY your candidate shifts the strength (300, 0) result in-suite only, correct it with the smallest coherent change, re-verify, and commit+push only if green.
Phase: implementation
Continuity anchor: your exchange-03 BLOCKED report (S4 interpreter failure; S2 three standalone 420s; S3 ten identical probe lines; candidate uncommitted, five dirty paths)
Authority renewal: prior authority expired; THIS prompt grants the diagnosis + correction + conditional commit below
Why reuse is appropriate: same healthy session, candidate and divergence context retained, no independence required
Retained context: convenience, not authority
Evidence posture: non-independent
Evidence tier: E1
Repository checkout topology: standalone checkout
Exact baseline: 3d7eae96d567a7004a927de45f53e16e2baf108f
Logical-whole closure: not-closed
```

## 1. ORCHESTRATOR-DIRECT evidence from the completed S4 — treat as given, non-independent

The ORCHESTRATOR ran your S4 himself in a disposable worktree at the exact baseline (created detached at `3d7eae9`, cleaned afterwards; canonical porcelain re-verified as exactly your five dirty paths):

```text
METHOD  worktree at 3d7eae9 + symlink worktree/frontend/node_modules -> canonical node_modules
        (frontend source is identical — the candidate touches only backend files) + the canonical
        backend/.env sourced into the subshell silently (bounded secret handling; no value printed)
        + the canonical venv interpreter by ABSOLUTE PATH with CWD = worktree backend.
        ⚠ Honest caveat: the two runs' final summary lines were not captured; the probe line was.
RUN 1   APMC-S4-PREFIX result=StrengthGameResult(seed=300, strategy_slot=0, plies=35,
        ranked_score=585, witness_score=165, end_reason=BAG_EMPTY_AND_PLAYER_OUT)   -> spread 420
RUN 2   identical, plies=35, 585, 165                                               -> spread 420
```

Decision matrix now complete:

```text
pre-fix   standalone 420 · IN-SUITE 420 x2 (faithful load)
post-fix  standalone 420 x3 (your S2) · IN-SUITE 435 (your exchange-02 run)
```

⇒ **RULE B FIRES.** The original test never pinned exact spreads (`all(result.spread > 0)` only —
verified at HEAD), so the 435 breaks ONLY your added parity pin, and the pre-fix behaviour is
in-suite-stable. Your candidate changes the in-suite result.

## 2. The decisive constraint for your diagnosis

`find_ranked_scoring_moves` is UNTOUCHED production code (locked fork 9). The ORCHESTRATOR's two
faithful pre-fix in-suite runs were STABLE — so under suite load the search itself completes
deterministically when its INPUTS are identical. Two live hypotheses, in order of plausibility:

```text
H-A  DETERMINISTIC INPUT DIFFERENCE that is environment-dependent. ⭐ Prime suspect: per-process
     HASH RANDOMIZATION. If any per-ply path in your module or its callers iterates a SET or dict
     of strings in a way that reaches the search (placement set ordering, a frozenset of rare
     tiles, a points mapping keyed by tile, candidate dedup order), per-process hash seed
     differences change exploration order and can flip the top candidate under the ranked budget.
     This explains "stable per context, different across contexts" better than load flakiness.
H-B  HOT-PATH OVERHEAD shifting the search's internal wall-clock budget. Note the budget is
     measured INSIDE the search; external per-ply work cannot change it directly — but any extra
     work BETWEEN the search start and its internal timing checkpoints, or a callback into the
     timed region, can. Weaker than H-A given the evidence, but not excluded.
```

## 3. The surgical diagnosis

```text
S-A  Temporarily instrument YOUR candidate (your five files; temporary edits are allowed and must
     be reverted before any commit) to dump, for seed 300 slot 0, EVERY ply's ranked-search INPUTS
     and top OUTPUT: rack tuple, board token tuple, bag_count, the four bounds, tile_points
     mapping identity/content hash, and the chosen canonical_key + total_score.
     Run standalone AND in-suite (full suite, canonical backend, prescribed relative interpreter —
     it works there). DIFF the two dumps.
S-B  IF inputs are identical and outputs differ -> timing: proceed to §4 correction (H-B).
     IF inputs differ -> you have the deterministic difference; fix the input construction
     (H-A; check PYTHONHASHSEED sensitivity by running the in-suite context once with
     PYTHONHASHSEED=0 and once unpinned — if pinning changes the outcome, that is your answer).
S-C  ⛔ Whatever you find: bounds unchanged, policy semantics unchanged, existing assertions
     unchanged, move_search.py untouched.
```

## 4. The correction, re-verification, conditional commit

```text
· Apply the SMALLEST coherent correction consistent with §3 (H-A: make the per-ply input
  construction order-stable — sort/derive from ordered structures; H-B: move capture out of the
  timed path / make it opt-in). ⛔ No behaviour change beyond restoring in-suite parity.
· Re-verify: the strength parity standalone (expect 420) AND the FULL canonical suite in-suite
  (expect the parity assertion to pass; capture the summary line verbatim). Both must show 420
  for (300, 0).
· IF in-suite still differs after the correction: STOP, commit nothing, report BLOCKED with the
  input-dump diff evidence. The next decision is the ORCHESTRATOR's.
· IF green: revert all temporary instrumentation, re-run the FULL standing backend set
  (documented mypy scope; ruff; plain -m pytest; quote summaries verbatim — baseline
  813 passed, 4 skipped in 373.54s), then commit the five files by EXPLICIT PATH, one commit,
  pre-push ls-remote equality gate vs 3d7eae9, one non-force push, public readback — the
  exchange-01 §8 pattern exactly.
· Your added parity instrument stays EXACTLY as strong as it was. ⛔ Under RULE B you do NOT
  narrow it — the candidate must meet it.
```

## 5. Boundaries

```text
· Positive authority: the same five paths, plus TEMPORARY in-repo instrumentation which MUST be
  reverted pre-commit (verify with git diff --stat before staging).
· Negative authority: everything else as in exchange 01 §4. ⛔ No new permanent files. ⛔ No bounds,
  semantics, or assertion changes. ⛔ No frontend. ⛔ No provider call.
· Interpreter: the prescribed `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from canonical
  backend/ (relative route WORKS there — it failed only in the disposable worktree; do not
  recreate that problem). ⛔ Never ambient python/python3/poetry run. ⛔ No environment
  reconstruction; the RF-16 stopping condition stands.
· Temporary worktrees: NOT authorized this exchange (S4 is complete). ⛔ No new /tmp artifacts
  except throwaway dump files, which you clean and report.
```

## 6. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 02, Worker exchange ordinal: 04
```

Eleven-item compact core: status; phase-qualified result from the closed enum (read it); start/end
commit; changed files with exact paths (post-revert state); tests and validation — the H-A/H-B
verdict WITH the input-dump diff evidence (bounded: one representative ply, not a full dump), the
in-suite parity result, the three gate summaries verbatim if committed; commit/push result with SHA
or none; deviations, risks, missing evidence; one smallest next step; exactly one report
justification from the closed enum at AP.md:2453-2454; explicit authority-expiry statement. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD, nothing unlabelled — scope: this prompt, the
  H-A/H-B split, and whether the parity instrument itself is even sound for a wall-clock-bounded
  policy. If you conclude it is NOT sound, say so here even while meeting it.>
Enumeration widened: none | <...>
```

⛔ Authority ends at this report. If committed, the push is the exchange's last mutation. Do not
start slice 2, do not archive into Meta. Acceptance is the ORCHESTRATOR's, after re-verification.
