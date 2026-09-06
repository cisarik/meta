You are a WORKER instance assigned to the persistent AP WORKER role. Exchange 05 of slice 3 — the CLOSING micro-correction: the digest rule becomes a closed class, not an open list. Perform exactly this task and stop.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 04
Worker exchange ordinal: 05
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker — one micro-correction on your own landed slice
Task identity: APMC-S3A-DIGEST-CLASS — every content asset the generation path resolves through the asset helpers is hashed (adding the variant definition JSON), and the rule is stated in the code so no future generation input can silently bypass it; fixture regenerated; slice 3 closes.
Phase: implementation
Continuity anchor: your exchange-04 implementation-PASS report for APMC-S3A-DIGEST, commit 51fa78ed14a6d975ebf52330c4bbe0f15e22edd5, and your own LEAD: "variant JSON (tile points / distribution) is still outside the hash ... the remaining scoring-identity coupling"
Authority renewal: prior authority expired; THIS prompt grants exactly the correction below
Why reuse is appropriate: same healthy session, your module; no independence required
Retained context: convenience, not authority
Evidence posture: non-independent
Evidence tier: E1
Repository checkout topology: standalone checkout
Exact baseline: 51fa78ed14a6d975ebf52330c4bbe0f15e22edd5
Logical-whole closure: not-closed
```

Reasoning recommendation: **Medium.** One helper extension plus a stated rule; the only judgment is the closure shape, which the ORCHESTRATOR has fixed below.

```text
AP.md:917-932 / AP.md:1444-1462 / AP.md:2466-2486 · AP_WORKER.md:14-26 ·
PROMPT_CONTRACTS.md:14-41 (report contract + coordinates) · AP.md:2453-2454 (justification enum)
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it.
```

## 1. The correction — close the CLASS by construction

```text
1  EXTEND collect_asset_digests: it must hash EVERY content asset the generation path resolves
   through the asset helpers — premiums layout, the variant's lexicon asset(s), the variant's
   two-tile file when present, AND the variant definition JSON (tile points / distribution — your
   LEAD). Derive the list from the SAME resolution calls the generator itself makes (variant
   context / Board / WordAuthority paths), so a future generation input added through those
   helpers is hashed automatically. State the rule in the helper's docstring:
     "conditions_digest binds configuration + every content asset resolved through the asset
      helpers. Code identity is pinned by generator_source_revision, not by this digest."
2  That stated rule CLOSES the gap sequence: any future input either comes through an asset
   helper (hashed) or is code (commit-pinned). No further digest corrections are anticipated; if
   one is ever needed, it is a new finding, not this rule failing.
3  set_digest changes ⇒ regenerate the 24-position default fixture, re-pin everywhere.
4  F3 / F5 / F9 / F10 re-run on the new envelope. F10's composition check extends to the variant
   JSON entry.
```

## 2. Boundaries

```text
· Positive authority: backend/game/position_sets.py, backend/tests/test_position_sets.py,
  backend/assets/diagnostics/position_sets/ (regenerated fixture). ⛔ Everything else byte-frozen,
  including every file under backend/assets/** (READ-ONLY for hashing).
· ⛔ No provider call, no DB, no new files beyond the regenerated fixture.
· Interpreter: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from canonical backend/
  (RF-16 bounded deviation as previously stated; ⛔ never ambient python/python3/poetry run).
· Gates (full set): mypy documented scope; ruff; plain `-m pytest`; three summaries verbatim.
  Baseline at `51fa78e`: mypy 88 source files, ruff clean, pytest `844 passed, 4 skipped in
  557.04s`.
· Git: explicit-path staging of exactly the three paths; ONE commit; pre-push ls-remote equality
  gate vs `51fa78ed14a6d975ebf52330c4bbe0f15e22edd5`; one non-force push; readback equality.
  ⛔ Never force, amend, rebase, reset, clean, stash, branch, or tag. Remote advanced → STOP.
```

## 3. Stopping conditions

```text
· repository gate disagreement, or porcelain not empty
· an asset path used by generation that the helpers cannot resolve for hashing (report it — that
  is a finding about the helpers, not something to hardcode)
· digest instability across two same-config runs — STOP
· a gate failure outside the allowlist · pre-push gate failure · secret exposure
· completed work, gates green, pushed, readback equal — stop THERE and report
```

## 4. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 04, Worker exchange ordinal: 05
```

Eleven-item compact core: status; phase-qualified result from the closed enum (read it); start/end
commit; changed files; tests and validation — the complete hashed-asset map, F3/F5/F9/F10 re-run
results, the three gate summaries VERBATIM, and the NEW set_digest; commit and push result with SHA
and readback; deviations, risks, missing evidence; one smallest next step; exactly one report
justification from the closed enum at `AP.md:2453-2454`; explicit authority-expiry statement. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD, nothing unlabelled>
Enumeration widened: none | <...>
```

⛔ Your authority ends at that report. Slice 3 is then CLOSED pending my acceptance; do not start
slice 4, do not archive into Meta. Acceptance is the ORCHESTRATOR's, after re-verification.
