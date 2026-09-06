You are a WORKER instance assigned to the persistent AP WORKER role. Exchange 04 of slice 3 — a MICRO-correction that closes the slice: the conditions digest must identify CONTENT, not only configuration. Perform exactly this task and stop.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 04
Worker exchange ordinal: 04
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker — one micro-correction on your own landed slice
Task identity: APMC-S3A-DIGEST — fold the legality- and scoring-identity ASSET HASHES (premiums layout, variant lexicon) into conditions_digest, so two assets with equal digests cannot have different content; regenerate the fixture; close slice 3.
Phase: implementation
Continuity anchor: your exchange-03 implementation-PASS report for APMC-S3A-COMPLETE, commit c9396f417baf5b44e60469432be871671d030a37, and your own LEAD: "a layout change would alter scores of an old fixture without changing that fixture's set_digest"
Authority renewal: prior authority expired; THIS prompt grants exactly the correction below
Why reuse is appropriate: same healthy session, your module and fixture; no independence required
Retained context: convenience, not authority
Evidence posture: non-independent
Evidence tier: E1
Repository checkout topology: standalone checkout
Exact baseline: c9396f417baf5b44e60469432be871671d030a37
Logical-whole closure: not-closed
```

Reasoning recommendation: **Medium.** A small, well-defined digest-composition change with one judgment call the ORCHESTRATOR has already made (which assets hash in).

```text
AP.md:917-932 / AP.md:1444-1462 / AP.md:2466-2486 · AP_WORKER.md:14-26 ·
PROMPT_CONTRACTS.md:14-41 (report contract + coordinates) · AP.md:2453-2454 (justification enum)
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it.
```

## 1. The correction — exactly this

```text
1  conditions_digest gains the SHA-256 of every ASSET the snapshot's legality and scoring identity
   depends on, measured at generation time:
     · the premiums layout file the Board is built from (your LEAD — the proven case)
     · the variant's lexicon asset(s) (a changed lexicon changes legality → different decisions →
       different baselines under an unchanged digest)
   Use the existing asset-resolution helpers (the same paths Board / WordAuthority load from);
   hash file CONTENTS. List the hashed asset identities + their digests as a small map INSIDE the
   envelope (e.g. asset_digests: {<name>: <sha256>}), so a reader can see what the set depends on
   without recomputing.
2  set_digest therefore changes ⇒ regenerate the 24-position default fixture, re-pin everywhere.
3  F3 (byte-identity across two same-config runs) and F5 (node-bound stability) re-run on the new
   envelope. F9 mount-equivalence re-runs at generation as before.
4  NEW fail-before F10: pre-fix, conditions_digest is unchanged when a hashed asset's content is
   perturbed — capture that exact equality (perturb a COPY in a temp location if the real asset
   must not be touched; ⛔ never modify the real assets/dicts or premiums files, even temporarily).
   Post-fix: the digest moves. Restore the copy, digest returns. (If perturbing for the test is
   impractical without touching real assets, assert the composition instead: the digest function's
   input includes the asset hashes — state which shape you took.)
```

## 2. Boundaries

```text
· Positive authority: backend/game/position_sets.py, backend/tests/test_position_sets.py,
  backend/assets/diagnostics/position_sets/ (regenerated fixture). ⛔ Everything else byte-frozen —
  including backend/assets/premiums.json and backend/assets/dicts/** (READ-ONLY for hashing).
· ⛔ No provider call, no DB, no new files beyond the regenerated fixture.
· Interpreter: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from canonical backend/
  (RF-16 bounded deviation as previously stated; ⛔ never ambient python/python3/poetry run).
· Gates (full set): mypy documented scope; ruff; plain `-m pytest`; three summaries verbatim.
  Baseline at `c9396f4`: mypy 88 source files, ruff clean, pytest `843 passed, 4 skipped in
  538.19s`.
· Git: explicit-path staging of exactly the three paths; ONE commit; pre-push ls-remote equality
  gate vs `c9396f417baf5b44e60469432be871671d030a37`; one non-force push; readback equality.
  ⛔ Never force, amend, rebase, reset, clean, stash, branch, or tag. Remote advanced → STOP.
```

## 3. Stopping conditions

```text
· repository gate disagreement, or porcelain not empty
· an asset whose content hash cannot be resolved through the existing helpers (report, do not
  hardcode a path)
· digest instability across two same-config runs — STOP, that falsifies the determinism premise
· a gate failure outside the allowlist · pre-push gate failure · secret exposure
· completed work, gates green, pushed, readback equal — stop THERE and report
```

## 4. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 04, Worker exchange ordinal: 04
```

Eleven-item compact core: status; phase-qualified result from the closed enum (read it); start/end
commit; changed files; tests and validation — the F10 evidence, the hashed-asset map, F3/F5/F9
re-run results, the three gate summaries VERBATIM, and the NEW set_digest; commit and push result
with SHA and readback; deviations, risks, missing evidence; one smallest next step; exactly one
report justification from the closed enum at `AP.md:2453-2454`; explicit authority-expiry
statement. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD, nothing unlabelled>
Enumeration widened: none | <...>
```

⛔ Your authority ends at that report. Slice 3 is then CLOSED pending my acceptance; do not start
slice 4, do not archive into Meta. Acceptance is the ORCHESTRATOR's, after re-verification.
