Independent acceptance complete. All gates verified directly against the immutable Git object.

## Worker 03 — Exchange 01 — Terminal Acceptance Report

**Task:** AP-CONSUMER-ROUTE-BINDING-ACCEPT-03
**Logical whole:** ap-consumer-declared-execution-route-and-capability-gate-binding
**Decision: ACCEPT**

### Independence & routing gate — PASS
Fresh Worker session, no participation in Worker 01/02, Native Plan Mode absent, Worker 03 exchange-01 coordinates received, no prior authority reused, no internal delegation, no repair performed.

### Repository identity gate — PASS (all 13)
- Root `/home/agile/Projects/ap`; origin fetch/push = `https://github.com/cisarik/ap.git`.
- `HEAD` = `10ac2ed33e7246233dd813e508f7850465119efc`; branch `feat/consumer-declared-route-binding`.
- Tree `b4c82c66…`, parent `95bd6448…`, subject `docs: bind Worker prompts to declared routes`, exactly **one** commit (`rev-list --count` = 1) from baseline.
- Credential-free `ls-remote`: public `refs/heads/main` = `95bd644829d48dcd188627f3e495e649df577eca` (matches expected).
- Working tree clean; no untracked paths; no active merge/rebase/cherry-pick/bisect/sequencer/lock; no remote ref contains the candidate (remote has only `HEAD`+`main`=95bd6448); no root `AGENTS.md`.
- **Stale `.git/REBASE_HEAD`**: present (41 bytes) with no `rebase-merge`/`rebase-apply`/sequencer/`MERGE_HEAD`/`CHERRY_PICK_HEAD` and no `git status` rebase indicator → **pre-existing, non-blocking**. Left untouched.
- **Note (non-finding):** local `main` = `4e7bfa56…` is a pre-existing ancestor of public `main` (stale local clone branch, 5 commits behind), not moved by this docs-only candidate; the candidate branches correctly from public baseline.

### Changed-path set — PASS
Exactly 8 paths (`git diff --name-status` vs `95bd6448`), all documentation, no mode/symlink/binary/schema/managed-block/test/CI/config change. `git diff --check` clean.

### Semantic acceptance matrix — PASS
- **9.1 Consumer ownership:** RF-16 retains exact operations/commands, env/tooling policy, capability gates, local values, credentials/privilege; AP neutral. ✓
- **9.2 Applicability:** triggered only by applicable *and usable* route; "not every project declares either surface." ✓
- **9.3 Pre-issuance resolution:** Orchestrator resolves baseline/rules/route/usability before issuance; "listing project files as required reading alone is not that binding." ✓
- **9.4 Canonical route:** prompt names/activates it as canonical execution/capability path. ✓
- **9.5 Parallel-route contradiction:** silent ambient route prohibited (positive via `Commands`/`Positive authority`, negative via `Negative authority`); Worker and Orchestrator both gain explicit stop conditions. ✓
- **9.6 Bounded deviation:** declares unused route, exact alternate, rationale, evidence class, bounded authority, stop condition; reuses existing fields, no new record, never a second canonical route. ✓
- **9.7 Ambient/failure:** RF-06 classifies ambient state as convenience (not authority/guaranteed capability); classify-before-remediate, prefer one declared-route reproduction, no silent env reconstruction, stop on unresolved contradiction. "SSH" used only as neutral route-class example. ✓
- **9.8 No-route:** fallback is exact project-owned guidance, no invented toolchain; Dev-Envelope may remain `not-used`. ✓
- **9.9 Distinction:** optional Dev-Envelope Activation, machine-readable `ap.project.conf`, and natural-language capability gates remain distinct. ✓

### Owner map — PASS
`AP.md` sole live normative owner; RF-06/RF-16 carry the semantics; all seven other surfaces are deliberate projections (operational/advisory/historical), no second normative owner, no material duplication. ADR-0018 status correctly `Implementation candidate` (not `Accepted`). Executable `ap` unchanged and makes no prompt-validation claim (verified `project check`/contract validation only). `git diff --check` clean.

**Recommendation: accept.** No concrete finding returned. Closure, publication, and consumer adoption remain out of scope for this read-only acceptance.