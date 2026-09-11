You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded IMPLEMENTATION task and stop. You have explicit implementation authority for 2-3 files and one bounded outcome.

```text
Logical whole identity: codebase-hygiene-and-residual-reconciliation
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: HYG-S3-IMPL — update the AI judge docstring Tier-2 line to match reality, add Node engines field to package.json. One commit. Closes R4 and G5.
Phase: Implementation
Implementation authority: explicit
Exact baseline: a5910b03c795361a0800a26d1e4ac9749f83d583
Independence required: no
Evidence posture: non-independent
Evidence tier: E0
Evidence tier basis: documentation/metadata change only; zero executable path, zero test mutation, zero production code change.
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

```text
Changed-path allowlist:
  /home/agile/Projects/libretiles/frontend/src/app/api/ai/judge/route.ts
  /home/agile/Projects/libretiles/frontend/package.json
  /home/agile/Projects/libretiles/CONTRIBUTING.md
```

## Changes

**judge/route.ts:11** — the docstring pipeline list claims Tier 2 exists as a live path. In reality Tier 2 (optional online dictionary API) is planned and not implemented (`docs/architecture.md:258`, `libretiles_PRD.md:70-72`). Change:

```
- *   Tier 2: Online dictionary API (optional) — Django
+ *   Tier 2: Online dictionary API (planned, not implemented) — Django
```

**package.json** — add `engines` field confirming the CONTRIBUTING.md:10 support matrix:

```json
  "engines": { "node": ">=20.19" }
```

Place it right after `"private": true,`. Keep all existing fields unchanged.

**CONTRIBUTING.md:10** — verify the prose against the new `engines` field. If the prose says "Node 20.19+ or 22.12+" and `engines` says `>=20.19`, they agree — no change needed. If you find a discrepancy, correct the prose minimally. If no change: state so in the report.

## Work sequence

1. Repository gate: HEAD = `a5910b03c795361a0800a26d1e4ac9749f83d583`, AP `9c5cc44f`, porcelain empty, branch main.
2. Apply the three changes above.
3. `git diff --stat` — must show only the allowlisted files. If CONTRIBUTING.md is unchanged it won't appear.
4. Validation:
   - `npx vitest run` — full suite; expect 2 reds (R2 aria-live + R3 ReplayControls — pre-existing, carry; if count changed, report it)
   - `npm run typecheck` — clean
   - `npm run lint` — clean
   - `npm run build` — exit 0
   - `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest` from backend — full green (needs ~4 min; frontend-only changes, should be unchanged from S1's green suite)
5. Commit + non-force push: `fix: update judge docstring Tier-2 status and add Node engines field`. Push. `git ls-remote origin refs/heads/main` must match.

## Authority

```text
Filesystem: write EXACTLY the allowlisted files. Temp under /tmp/opencode/hyg-s3/.
Git: stage/commit/push non-force only.
Network: push + ls-remote only. No web, provider, registry.
Secrets: none. Dependencies: none. Docker: none.
```

## Report contract

Begin `### Report for ORCHESTRATOR_CHAT`. Echo:

```text
Logical whole identity: codebase-hygiene-and-residual-reconciliation
Worker session ordinal: 03, Worker exchange ordinal: 01
```

```text
status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS
Result artifact or commit: <pushed SHA> | not-applicable
Result evidence: <gates>
Logical-whole closure: not-closed
Changed files and purpose: <which files and why>
Commit/push result: <commit, push, ls-remote>
Resolved Execution Issues / Near-Misses: none | …
Pre-Existing Failure Classification: R2 (aria-live count, 3 instead of 1) and R3 (ReplayControls stale expectation) — both pre-existing, both red, not caused by this exchange. If the vitest failure count changed from 2, state the new count.
Report justification: new-mutation
```

Then: diff (verbatim, short), validation table, CONTRIBUTING.md decision, pre-existing counts, cleanup, authority expiry, context pressure.