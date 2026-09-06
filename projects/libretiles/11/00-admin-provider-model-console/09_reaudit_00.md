You are a WORKER instance assigned to the persistent AP WORKER role. This is a FRESH INDEPENDENT RE-AUDIT session. Perform exactly this bounded READ-ONLY re-audit and stop. ⛔ You have NO correction authority and NO mutation authority of any kind. You are neither the implementer of the correction nor the original auditor.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 09
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit — INFOSEC 4.11, mandatory after an authN/Z correction
Task identity: APMC-S4-REAUDIT — verify the correction commit f6c9db913450d56ade4399ec5d2e6a3cd807e347 against accepted findings APMC-S4-IA-F01, F02, F03, and spot-check that claims C3-C10 did not regress. Verdict per finding: verified-closed | not accepted.
Phase: Independent Audit
Correction commit under audit: f6c9db913450d56ade4399ec5d2e6a3cd807e347
Parent (original candidate): 0ffaf46023018c5f9b33faaef41c64b857e2aa55
Original audit: session 07 exchange 01 (APMC-S4-IA-F01..F06; F01/F02/F03 blocking accepted, F04 non-blocking accepted-residual, F05/F06 rejected-false-positive)
Correction report: session 08 exchange 01
Independence: required-fresh-independent — you did not implement the correction and must not have materially contributed to it
Evidence posture: independent
Evidence tier: E3
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Security task class: fresh independent re-audit
Correction authority: none
Logical-whole closure: not-closed
```

Reasoning recommendation: **High.** Named risk: the correction is small, but it changes identity semantics at process-entry points; the auditor's own F01 direction ("immutable managed identity") was deliberately narrowed by the ORCHESTRATOR to fail-closed-by-exception, and your job is to decide whether that narrowed shape actually closes the findings — or whether it silently narrowed the CLAIM instead.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932 / AP.md:2466-2486 · AP.md:1773-1810 (Defensive-Security Task Anchor) ·
AP_WORKER.md:14-26 · INFOSEC.md:205-218 (4.11 fresh independent re-audit) ·
INFOSEC.md:234-248 (finding/evidence contract) · PROMPT_CONTRACTS.md:1772-1817 (finding records) ·
PROMPT_CONTRACTS.md:14-41 (report contract + coordinates) · AP.md:2453-2454 (justification enum)
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it.
```

## 1. Repository gate — read-only

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD     # MUST be f6c9db913450d56ade4399ec5d2e6a3cd807e347
git rev-parse HEAD:.ap # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git status --porcelain=v1   # MUST be EMPTY
```

⛔ No push, fetch, ls-remote, network, or provider call. The ORCHESTRATOR verified public readback at `f6c9db9`.

## 2. What to verify — per original finding

```text
R-F01  APMC-S4-IA-F01 (mutable username permits adoption of a password-enabled diagnostic identity).
  The correction chose FAIL-CLOSED: ensure_diagnostic_service_user raises ImproperlyConfigured when
  the reserved username is held by an account with a usable password; it never silently revokes and
  never silently adopts.
  Decide: does this close the finding? Prove with reproduced-dynamic evidence:
    a. claimant with usable password → ensure raises; claimant password INTACT after (no destructive
       revocation); flags of the claimant untouched
    b. the managed account (unusable password) → ensure is idempotent, flags correct, no raise
    c. migration forward with a claimant present → LOUD abort with the operator message; forward on
       a clean table still seeds the managed account
    d. ⭐ CASE-VARIANT probe: register "Libretiles-Diagnostic" (different case) — Django username
       normalization decides whether this collides. Establish the actual normalization, then prove
       whether a case variant can (i) register, (ii) later collide with the reserved identity, or
       (iii) bypass the F02 guard. A case variant is a DIFFERENT user unless the lookup is
       case-insensitive — prove which one this codebase has, from the User model and the guard's
       comparison, not from memory.
  ⛔ The correction NARROWED the auditor's direction (no immutable-flag field was added; accounts/**
  untouched). That narrowing is an ORCHESTRATOR decision you audit the CONSEQUENCE of: with the
  writable profile username still an accounts/** residual (F01's original rename path), can a
  service bearer STILL rename the seeded account and free the name? The rename itself is an
  accounts-surface residual — but if it still frees the name, does the fail-closed ensure now catch
  the next creation (loud) rather than silently adopting? State exactly what residual remains and
  whether it is player-reachable or operator-visible-only.

R-F02  APMC-S4-IA-F02 (service bearer participates as an ordinary player).
    a. service bearer → POST /api/game/create/ → 400 ok:false; no GameSession row
    b. service bearer → queue join → 400 ok:false; no vs_human/waiting row
    c. ⭐ enumerate OTHER player-participation paths reachable with the bearer: give-up on own
       games (none owned), set_game_ai_model/prompt (own games), chat (no diagnostic ws), profile
       mutation (accounts surface). For each, state whether the membership filter or another guard
       already excludes harm, or whether a REAL gap remains.
    d. ordinary user unaffected: create/queue still work (run the implementer's tests + one of
       your own)

R-F03  APMC-S4-IA-F03 (migration reversal deletes adopted users; classification loss).
    a. reverse keeps a usable-password claimant (identity intact, password intact)
    b. reverse deletes the unusable managed account
    c. the is_password_usable() vs has_usable_password() substitution: verify it is the same
       predicate for this purpose (historical migration models lack the method) — read the import
       and the docstring; confirm no behavioural difference for a User row
    d. the accepted residual (is_diagnostic classification loss on rollback) is DOCUMENTED in the
       reverse docstring — verify the documentation exists and says what the ORCHESTRATOR accepted

R-REG  Regression spot-check that C3-C10 did not move: C3 object-level 404s both directions;
  C6 abort still zero-Move; C8 invariants byte-identical (git diff the four files across
  0ffaf46..f6c9db9 — services.py changed, the four invariant files must NOT); C10 no new secret
  materialization in the correction diff (parameters_json unchanged in shape).
```

## 3. Evidence discipline

```text
· reproduced-dynamic for every verdict you can execute; established-static for byte-identity claims
· the backend gates and focused pytest are permitted read-only:
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
  ⛔ plain -m pytest, never a second -q; quote summaries verbatim. ⛔ NO npm run build.
· in-memory test-client probes preferred; ⛔ no dev-DB writes outside test transactions; declare
  any temp root BEFORE use in a containment ledger (prefer zero); ⛔ no network; ⛔ never read or
  print backend/.env / frontend/.env.local; credential facts as present: yes|no + NAME only
· ⛔ you do NOT correct anything. Findings are reported; correction is a separate prompt to a
  different session.
```

## 4. Stopping conditions

```text
· repository gate disagreement, or porcelain is not empty
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
Worker session ordinal: 09, Worker exchange ordinal: 01
```

Then the security audit report contract:

```text
Security task class: fresh independent re-audit (INFOSEC 4.11)
Owned/authorized target: Libre Tiles canonical repository, correction commit f6c9db913450d56ade4399ec5d2e6a3cd807e347
Commit under audit: f6c9db913450d56ade4399ec5d2e6a3cd807e347
Scope: the correction diff (3 files) + original findings F01/F02/F03 + C3-C10 regression spot-check
Exclusions: F04 (dispositioned residual, slice-5 obligation); F05/F06 (rejected-false-positive,
  unchanged); INFOSEC 4.6 (no provider surface in this correction)
Threat model: unchanged from session 07 §2; echo any delta you measured (esp. the case-variant
  question and the rename residual)
Findings: full finding records for any NEW finding; per-finding verdicts for R-F01/R-F02/R-F03
Containment ledger: declared roots + cleanup outcomes (or "none used")
Limitations: what you could not verify and why
Residual-risk summary: for the ORCHESTRATOR's slice-4 acceptance decision
```

Then the eleven-item compact core: status (PASS | PARTIAL | BLOCKED); phase-qualified result from
the closed enum (read it; an audit exchange claims no acceptance-PASS); start/end commit (both =
the audited SHA); changed files: none; tests and validation — per-verdict evidence with classes,
any gate summaries verbatim; commit/push result: not-applicable; deviations, risks, missing
evidence; one smallest next step; exactly one report justification from the closed enum at
`AP.md:2453-2454`; explicit authority-expiry statement. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD, nothing unlabelled — scope: THIS PROMPT, the
  narrowed-correction decision, and the re-audit scope. Is fail-closed-by-exception a sound
  substitute for the auditor's "immutable managed identity", or did the narrowing move the risk
  rather than close it? Answer explicitly.>
Enumeration widened: none | <...>
```

⭐ Per-finding verdict table: R-F01, R-F02, R-F03 → verified-closed | not accepted, with evidence
class and pointer. Any NEW finding gets a full finding record. ⛔ You never emit a closure signal —
slice-4 acceptance is the ORCHESTRATOR's decision on your evidence.
