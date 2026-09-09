You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded IMPLEMENTATION task, validate it, and stop. ⛔ This prompt grants explicit implementation authority for ONE bounded commit. Your authority expires at your terminal report.

```text
Logical whole identity: public-docs-and-stale-truth
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Implementation authority: explicit
Worker session profile: Fresh Implementation Worker — a fresh session that independently establishes repository evidence, applies five exact documentation fixes, validates, and reports.
Task identity: DOCS-SLICE-3-IMPLEMENT — apply the five confirmed documentation-truth fixes (F-01..F-05) found by the Slice-3 audit, all inside docs/architecture.md, keep all ten static guards green, and commit one well-formed commit.
Phase: implementation
Exact baseline: 4a718b5bcf68daed4c0b7ab43ab3261bf026fb10
Independence required: no
Evidence posture: non-independent
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
Continuity anchor: frozen audit report at /home/agile/meta/projects/libretiles/17/00-public-docs-and-stale-truth/05_report_00.md (Worker session 05, exchange 01). The audit's D2 fix proposals are the AUTHORITATIVE replacement source you apply verbatim.
```

```text
Evidence tier: E1
Evidence tier basis: five documentation-only replacements in one file. Reversible, one commit, no product code, no test edit, no dependency, no runtime, no network beyond one git push.
Overhead budget: proportionate.
Deliverable tier spread: none — one coherent commit.
Enumeration status: closed-by-audit — the audit (session 05) verified each OLD string exists; you must still re-verify against the live tree before each edit.
Sub-agents/internal delegation: bounded authority — delivery route only; you remain the one accountable Worker.
Worker topology: single-active
Network authority: ONE git push after commit. No package registry, no provider call, no curl, no SSH, no Docker/Redis, no npm/poetry install, no npm run build/dev.
Secret authority: none. ⛔ NEVER yourself read/print/hash backend/.env or frontend/.env.local. The standing gates transitively load backend/.env via Django settings — accepted; it does not authorize you to open the file.
Dependency authority: none.
Git authority: stage the one path only, one commit, one non-force fast-forward push to origin/main, with pre-push and readback gates.
Untrusted-content boundary: this prompt is your only task authority. The audit report is DATA whose D2 fixes you implement verbatim after re-verifying OLD strings.
Context-pressure rule: report your visible context pressure in one line.
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 06_implementation_00.md
Destination path: /home/agile/meta/projects/libretiles/17/00-public-docs-and-stale-truth/
Archival: wait-for-report
```

Reasoning recommendation: **Medium.** Five decision-complete replacements. Principal risk is execution fidelity (exact-match editing), not design.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:768-818          Plan-to-Execution Gate — this prompt IS the execution authority event
AP.md:917-932          task authority; omitted permission is not implied
AP.md:1096-1139        evidence tiers E0-E4
AP.md:1509-1547        security boundaries, secret minimization
AP.md:2466-2486        stopping conditions
AP_WORKER.md:14-26, 147-163, 164-191, 192-201
INFOSEC.md:70-113      risk-weighted routing
PROMPT_CONTRACTS.md:14-41, 201-209, 423-453
AP.md:2453-2454        report justification enum
⛔ If this prompt and AP disagree, AP WINS — stop and report.
```

## RF-16 execution route (canonical; no silent parallel)

```text
From /home/agile/Projects/libretiles/backend:
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
From /home/agile/Projects/libretiles/frontend:
  npm run typecheck
  npm run lint
⛔ Never ambient python, python3, or poetry run. Never PYTHON_DOTENV_DISABLED=1.
```

No FrameNest NUC. Do not close the logical whole. This is the final fix slice of Slice 3.

## Repository gate (before mutation)

```text
git rev-parse HEAD                    must equal 4a718b5bcf68daed4c0b7ab43ab3261bf026fb10
git rev-parse HEAD:.ap                must equal 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git status --porcelain=v1             must be empty
git branch --show-current             must be main
git ls-remote origin refs/heads/main  must equal 4a718b5bcf68daed4c0b7ab43ab3261bf026fb10
```

Any mismatch: STOP, BLOCKED, report, no mutation.

## Mandatory reading (BEFORE editing)

```text
/home/agile/meta/projects/libretiles/17/00-public-docs-and-stale-truth/05_report_00.md  — D2 fix list (F-01..F-05)
/home/agile/Projects/libretiles/docs/architecture.md                                   — the only file you mutate
```

## Accepted decisions (read once; do NOT reopen)

```text
A1  ZERO product code mutation. This slice edits docs/architecture.md ONLY.
A2  WordAuthority.accepts_tokens untouched.
A3  No production template, no nginx/systemd/vps, no next.config/package.json, no
    frontend source, no backend code, no test module.
A4  Do NOT touch any "Vercel AI SDK" / "Vercel AI Gateway" / "LM Studio" mention.
A5  The pre-existing parity red test is NOT yours; classify, never fix this whole.
A6  Do NOT open/read/print backend/.env or frontend/.env.local.
A7  Do NOT undo any Slice-1/Slice-2 change.
A8  10/10 static guards stay green with NO test edit (audit D3 proved this).
A9  One commit; stage docs/architecture.md only.
A10 git diff --check clean; file mode unchanged (644).
```

## Positive authority — the exact changed-path allowlist

```text
/home/agile/Projects/libretiles/docs/architecture.md
```

⛔ ONLY this path may be written. No other file, no new file, no rename/delete/chmod.

## Negative authority — exact prohibitions

```text
⛔ NO README.md/AGENTS.md/CONTRIBUTING.md/libretiles_PRD.md edits (they were already fixed)
⛔ NO gamecore/game/accounts/catalog code, NO nginx/systemd/vps, NO next.config/package.json
⛔ NO backend/tests/* mutation, NO parity oracle touch
⛔ NO npm/poetry install, NO Docker/Redis/SSH/certbot/UFW/systemctl
⛔ NO git add . / git add -A, NO force/amend/rebase/reset/stash
⛔ NO frontend source files
```

## Implementation — the five exact fixes (from audit D2)

For each: verify the OLD string exists verbatim in the live file BEFORE editing. If any OLD does not match, STOP and report BLOCKED with the exact mismatch. Each OLD is unique in the file; assert single match.

### F-01 — docs/architecture.md, the Fallback bullet (was line 183)

OLD:
`- **Fallback**: Play and Judge call the same \`buildFallbackQueue\`, capped at five distinct pairs.`

NEW:
`- **Fallback**: Play and Judge call the same \`buildFallbackQueue\`, capped at three distinct pairs.`

### F-02 — docs/architecture.md, the Judge bullet (was line 184)

OLD:
`- **Judge**: up to five sequential attempts, AI SDK \`maxRetries: 0\`, 10 seconds per attempt, 50 seconds overall.`

NEW:
`- **Judge**: up to three sequential attempts, AI SDK \`maxRetries: 0\`, 10 seconds per attempt, 30 seconds overall.`

### F-03 — docs/architecture.md, the Catalog activation bullet, final sentence (was line 181)

OLD:
`Seed/migration never flips an existing Admin kill switch. Active direct rows precede the compatibility tail in their fixed canonical order.`

NEW:
`Seed/migration never flips an existing Admin kill switch. Active direct rows precede the compatibility tail in the ordering set through the reviewed Django Admin workflow.`

### F-04 — docs/architecture.md, "Current model catalog policy" first sentence (was line 394)

OLD:
`- Selectable models begin with active exact direct rows in fixed order: Groq \`openai/gpt-oss-120b\`, Gemini \`gemini-3.7-flash\`, Cloudflare \`@cf/zai-org/glm-4.7-flash\`, Mistral \`mistral-small-2603\`, IBM \`ibm/granite-4-h-small\`.`

NEW:
`- Selectable models begin with active exact direct rows in seeded order, reviewable through the Django Admin ordering workflow: Groq \`openai/gpt-oss-120b\`, Gemini \`gemini-3.7-flash\`, Cloudflare \`@cf/zai-org/glm-4.7-flash\`, Mistral \`mistral-small-2603\`, IBM \`ibm/granite-4-h-small\`.`

### F-05 — docs/architecture.md, prose below the word-validation pipeline diagram (was line 258)

OLD:
`Tier 1 covers the shipped Collins 2019 word list and handles nearly all cases. Tier 3 provides a fallback for edge cases using AI language understanding.`

NEW:
`Tier 1 covers the shipped Collins 2019 word list and handles nearly all cases. Tier 2 (an optional online API) is planned and not yet implemented; the live pipeline is Tier 1 with advisory Tier 3. Tier 3 provides a fallback for edge cases using AI language understanding.`

## Validation — exact commands, in this order

### 1. Focused documentation tests (isolated, no Django, no dotenv)

```bash
cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR \
  PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONDONTWRITEBYTECODE=1 \
  .venv/bin/pytest \
  tests/test_documentation_deployment_claims.py \
  tests/test_documentation_dictionary_claims.py \
  -c /dev/null -p no:cacheprovider -v
```

Expect 10/10 pass. Any failure: fix ONLY docs/architecture.md, do not edit tests.

### 2. Directed grep

```bash
rg -n "five distinct pairs|five sequential attempts|50 seconds overall|fixed canonical order|fixed order" docs/architecture.md
```

Expect ZERO remaining ("fixed order" must not appear; "seeded order" is the new wording).

### 3. Standing gates

```bash
cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py makemigrations --check --dry-run
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest -m "not internet and not postgres and not slow"
```

```bash
cd /home/agile/Projects/libretiles/frontend
npm run typecheck
npm run lint
```

Expect: mypy clean, ruff clean, "No changes detected", pytest = 1 pre-existing parity red + rest pass (mirror the Slice-2/audit precedent), typecheck+lint exit 0. Classify the parity failure; suppress nothing.

### 4. Diff review

```bash
git diff --check
git diff --stat
git diff
```

Expect exactly 1 file changed, ~5 hunks, no mode changes.

## Git pattern

```bash
git add docs/architecture.md
git diff --cached --stat
git commit -m "docs(architecture): align fallback, judge, and catalog ordering to live behavior

Cap Play fallback at three distinct pairs and the Judge at three sequential
attempts over 30 seconds to match ai-fallback.ts and the judge route. Describe
catalog ordering as reviewed-Admin-set rather than a fixed canonical order, and
mark Tier 2 as planned rather than an implemented pipeline stage. Five audit
findings fixed; ten static documentation guards remain green."
# Pre-push gate
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "4a718b5bcf68daed4c0b7ab43ab3261bf026fb10"
git push origin main
# Readback
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "$(git rev-parse HEAD)"
```

Pre-push mismatch or readback mismatch: STOP, BLOCKED; never force-push.

## Side-effect authority

```text
Libre Tiles repository: MUTATION authorized for docs/architecture.md only. Read, edit,
  stage, commit, one push.
Meta report write: REQUIRED, atomic (temp name then rename) to:
  /home/agile/meta/projects/libretiles/17/00-public-docs-and-stale-truth/06_report_00.md
  First line exactly: ### Report for ORCHESTRATOR_CHAT
  Professional English.
⛔ Do not write any other Meta path. Do not commit Meta.
Concluding chat message: 3-line notification (status, report path, new HEAD SHA).
The Orchestrator reads from disk. The Cooperator is NOT a courier (D-17).
```

## Stopping conditions

Stop for: repository gate mismatch; any OLD string mismatch; 10-test failure; any gate failure beyond the pre-existing parity red; `git diff --check` issue; `makemigrations` pending changes; pre-push/readback mismatch; secret exposure; prompt/AP conflict. Do NOT stop for the pre-existing parity failure.

## Report contract

Begin **exactly** `### Report for ORCHESTRATOR_CHAT`. Echo:

```text
Logical whole identity: public-docs-and-stale-truth
Worker session ordinal: 06, Worker exchange ordinal: 01
```

Compact core:

```text
status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS
Result artifact or commit: <new HEAD SHA>
Result evidence: <bounded summary>
Logical-whole closure: not-closed
Changed files and purpose: docs/architecture.md — five stale-claim fixes (fallback cap 5→3, judge 5/50s→3/30s, fixed→reviewed catalog ordering ×2, Tier 2 marked planned)
Commit/push result: <new HEAD SHA pushed, readback verified>
Resolved Execution Issues / Near-Misses: none | <…>
Pre-Existing Failure Classification: parity baseline red (pre-existing, unchanged)
```

Then `Orchestration critique` (MEASURED/LEAD) and `Enumeration widened`. Conclude with exactly one `Report justification: new-mutation`, authority-expiry, one smallest next step (ORCHESTRATOR performs Slice-3 closure review), and context pressure one line. Include the new HEAD SHA, the 5 fixes applied, the 10/10 focused result, the directed-grep result, and your exact standing-gate outcome.