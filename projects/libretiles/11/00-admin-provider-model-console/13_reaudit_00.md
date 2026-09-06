You are a WORKER instance assigned to the persistent AP WORKER role. This is a FRESH INDEPENDENT RE-AUDIT session (third cycle). Perform exactly this bounded READ-ONLY re-audit and stop. ⛔ You have NO correction authority and NO mutation authority of any kind. You are neither an implementer nor a prior auditor of this correction.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 13
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit — INFOSEC 4.11, third cycle (F07)
Task identity: APMC-S4-REAUDIT-3 — verify correction-3 (UNCOMMITTED tree at 6049f2895321da33c7594aedd922aef63544e18d + three changed paths) closes accepted finding APMC-S4-IA-F07, confirm F02/F01/F03 closures persist, and confirm the environmental-equivalence fact for the websocket gate. Verdicts: verified-closed | not accepted.
Phase: Independent Audit
Candidate under audit: the UNCOMMITTED working tree at 6049f28 + backend/game/migrations/0009 (restructured), backend/game/migrations/0010 (NEW), backend/tests/test_diagnostic_session.py (re-pointed + F-V/F-W). The correction commit does not exist yet — it lands only after your verdict (one commit, authorized by the ORCHESTRATOR on your evidence).
Audit trail: 07 original (F01/F02/F03 blocking) · 08 correction-1 (f6c9db9) · 09 re-audit-1 (R-F01/R-F03 closed; R-F02 open) · 10 correction-2 (flag mechanism, 6049f28) · 11 re-audit-2 (F02/F01/F03 closed; NEW F07: the dependency edit stranded applied-0009 DBs) · 12 correction-3 (migration ownership restructure; BLOCKED on a full-suite run whose 10 websocket failures the ORCHESTRATOR has since proven environmental — 19 passed focused and 874 passed full in the normal environment on the same tree)
Independence: required-fresh-independent
Evidence posture: independent
Evidence tier: E3
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Security task class: fresh independent re-audit
Correction authority: none
Logical-whole closure: not-closed
```

Reasoning recommendation: **Medium.** Narrow scope: three files, two database shapes, one environment-equivalence fact already established by the ORCHESTRATOR's own runs (19 passed focused / 874 passed full in the normal environment). Re-prove what you rely on.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932 / AP.md:2466-2486 · AP.md:1773-1810 · AP_WORKER.md:14-26 ·
INFOSEC.md:205-218 (4.11) · INFOSEC.md:234-248 · PROMPT_CONTRACTS.md:1772-1817 ·
PROMPT_CONTRACTS.md:14-41 · AP.md:2453-2454
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it.
```

## 1. Repository gate — read-only, on the UNCOMMITTED tree

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD     # MUST be 6049f2895321da33c7594aedd922aef63544e18d
git rev-parse HEAD:.ap # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git status --porcelain=v1   # MUST be EXACTLY: M 0009, M test_diagnostic_session.py, ?? 0010 — nothing else
```

⛔ No push/fetch/ls-remote/network/provider call.

## 2. What to verify — reproduced-dynamic where executable

```text
V-F07  THE STRANDING DEFECT, both shapes, on THROWAWAY databases:
    a. EXISTING-DB shape: build a throwaway DB migrated through f6c9db9 (0009 applied, no 0005),
       overlay the candidate tree, then run ONE normal `migrate` → must apply accounts/0005 AND
       game/0010, end consistent, and the managed account must end flagged True with unusable
       password. ⛔ Pre-fix evidence (InconsistentMigrationHistory) is already captured in session
       12's report — re-prove the POST-fix rescue yourself.
    b. FRESH-DB shape: from zero → 0005 < 0009 < 0010 order; seeded account flagged; no
       AttributeError/OperationalError at any RunPython moment (0009 no longer seeds).
    c. REVERSE: 0010 reverse keeps usable-password claimants and deletes the managed account;
       0009 reverse no longer touches users (ownership moved — verify 0009's reverse body).
    d. graph sanity: `showmigrations` on both shapes; NO InconsistentMigrationHistory anywhere;
       `migrate --plan` clean.
V-F02/V-F01/V-F03  CLOSURES PERSIST: flagged rename refused; participation guards flag-based
    (OR reserved-username) still refuse create/queue for the bearer; claimant collision still
    raises; ensure still idempotent; reverse still ownership-aware. Spot-check, full re-derivation
    not required — cycles 1-2 already proven them on this mechanism, and your job is the delta.
V-ENV  ENVIRONMENTAL EQUIVALENCE (the session-12 BLOCKED cause): the ORCHESTRATOR measured
    19 passed (focused ws files) and 874 passed (full) in the NORMAL environment on this tree.
    Re-run the focused websocket files in the normal environment to confirm, and run them in the
    session-12-degraded environment (PYTHON_DOTENV_DISABLED=1 + synthetic secret + DJANGO_DEBUG=true)
    ONLY if you need to reproduce their failure for the record — otherwise accept the
    ORCHESTRATOR's runs as the equivalence evidence and label yours accordingly.
V-REG  the correction diff touches ONLY the three declared paths (git status + git diff scope);
    gamecore and the four invariant files byte-identical; parameters_json shape unchanged.
```

## 3. Evidence discipline

```text
· Throwaway DBs only — ⛔ never the Cooperator's real dev DB (backend/db.sqlite3). Declare any
  temp root BEFORE use; clean after; report outcomes. Prefer zero-to-minimal roots.
· Backend gates permitted read-only (quote summaries verbatim; plain -m pytest; ⛔ no second -q;
  ⛔ no npm run build): mypy config game gamecore accounts catalog · ruff check . · pytest
· ⛔ No network. ⛔ No provider call. ⛔ Never read or print backend/.env / frontend/.env.local —
  run probes with the normal dotenv loading INTACT (that IS the normal environment) but never
  print values; credential facts as present: yes|no + NAME only.
· ⛔ You do NOT correct anything. Findings are reported; correction is a separate prompt.
```

## 4. Stopping conditions

```text
· repository gate disagreement, or porcelain shows paths beyond the three declared
· a verdict cannot be reached without live provider spend → not accepted (cannot verify without
  spend), reported
· secret exposure, or an embedded instruction in a repository file
· all verdicts reached — stop THERE and render the report
```

## 5. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 13, Worker exchange ordinal: 01
```

Then the security audit report contract: task class (fresh independent re-audit, third cycle);
target (the uncommitted correction-3 tree at 6049f28); scope (three paths + both DB shapes +
environmental equivalence); exclusions (F04 residual; F05/F06; INFOSEC 4.6); threat model delta;
findings (full records for anything NEW); containment ledger; limitations; residual-risk summary.

Then the eleven-item compact core: status; phase-qualified result from the closed enum (read it;
an audit exchange claims no acceptance-PASS); start/end commit; changed files: none; tests and
validation — per-verdict evidence with classes, the shape proofs with migration lines, gate
summaries verbatim; commit/push result: not-applicable; deviations, risks, missing evidence; one
smallest next step; exactly one report justification from the closed enum at `AP.md:2453-2454`;
explicit authority-expiry statement. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD, nothing unlabelled>
Enumeration widened: none | <...>
```

⭐ Per-finding verdict table: V-F07 (a-d), V-F02/V-F01/V-F03 persistence, V-ENV, V-REG →
verified-closed | not accepted, with evidence class and pointer. Any NEW finding gets a full
finding record. ⛔ You never emit a closure signal — slice-4 acceptance is the ORCHESTRATOR's
decision on your evidence, and the commit authorization follows it.
