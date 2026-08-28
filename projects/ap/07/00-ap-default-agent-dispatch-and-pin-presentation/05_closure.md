# Era 07 Closure — ap-default-agent-dispatch-and-pin-presentation

```text
Logical whole identity: ap-default-agent-dispatch-and-pin-presentation
Standard terminal status: PASS
Phase-qualified result: publication-PASS
Result artifact or commit: 2fbf8d3fa4699d1af073dcbf135c4f11789fdcd4
Result evidence: fresh independent acceptance-PASS (session 03); publication-PASS (session 04) verified by independent Orchestrator credential-free readback (git ls-remote)
Logical-whole closure: closed-by-ORCHESTRATOR
Required preceding results: satisfied
Cooperator-owned decisions: satisfied (Stage 2 whole selection, plan acceptance, brainstorming refinements, publication grant)
Residual-risk disposition: satisfied
Upgrade-ledger reconciliation: complete (AP protocol improvements published; FrameNest consumer pin-adoption is a separate follow-on whole)
Active mutation: none
Closure actor: ORCHESTRATOR
Declared closure signal: closed-by-ORCHESTRATOR
Signal owner: orchestrator
Worker emission of closure signal: prohibited
Accepted evidence: planning-PASS 01 (plan accepted by Cooperator „prijímam"); implementation-PASS 02 (candidate 2fbf8d3…, object-verified); acceptance-PASS 03 (fresh independent audit); publication-PASS 04 (public main == 2fbf8d3fa4699d1af073dcbf135c4f11789fdcd4, readback 2×)
Public Git equality: equal (https://github.com/cisarik/ap.git refs/heads/main == 2fbf8d3fa4699d1af073dcbf135c4f11789fdcd4)
Orchestrator acceptance: accepted
Closure authority: present
Closure date: 2026-08-28
```

---

## 1. Accepted Outcome

Candidate `2fbf8d3fa4699d1af073dcbf135c4f11789fdcd4` (stack `be6a6ae` and `2fbf8d3` on baseline `86ae6e8c…`) is published as public AP `main`:

1. **Observation A — Agent Orchestrator Default Dispatch & Model Opt-Out (P14):**
   - In `AP.md` §3, `RF-02`, and `RF-06`, Agent Orchestrators default to direct prompt dispatch of one complete authoritative Worker prompt into one concrete session.
   - P14 model-opt-out exception formally codified: copy-paste prompt delivery is a lawful selected route when the Cooperator rotates model family, client, or manually acts as messenger.
   - `RF-05` parent-context disqualifier remains strict: subagents inheriting parent conversation/reasoning cannot provide independent acceptance.
   - Dispatch capability is defined as a delivery mechanism and never expands task authority.

2. **Observation B — Direct Trace Archival & Companion Integrity Invariant:**
   - In `AP.md` `RF-19` and `RF-02`, the Orchestrator directly archives prompt+report pairs upon dispatch return without Cooperator messenger labor.
   - Companion Integrity Invariant codified: an archived companion `*_report_*.md` must be a valid terminal report (starting with `### Report for ORCHESTRATOR_CHAT`) and must never be byte-identical to or a duplicate of the issued prompt.
   - Anti-pattern added to `AP.md` §19 rejecting prompt-duplicate report companions.

3. **Observation C — Pin-Time Discoverability Hook in `UPDATING.md`:**
   - `UPDATING.md` Review Checklist includes an explicit item to verify or refresh optional project-owned declarations in `AGENTS.md` outside the managed block at pin update.
   - `INTEGRATION.md` provides a ready-to-use non-normative project-owned presentation capsule (illustrating status marks 🟢🟡🔴, delivery capsule, and natural-language separation).

4. **Orchestrator Initialization Signal in Restoration Handouts:**
   - In `AP.md` §3 & §14, `AP_ORCHESTRATOR.md`, `PROMPT_CONTRACTS.md`, `GLOSSARY.md`, `INTUITION.md`, and `docs/adr/0022-*`, every generated restoration prompt / handout for a successor Orchestrator must declare `Capability profile: Agent Orchestrator | Read-Only Orchestrator` and emit an explicit initialization signal for the Cooperator.

5. **Historical Architecture & Delivery:**
   - `docs/adr/0022-default-agent-dispatch-trace-integrity-and-pin-presentation.md` created, indexed in `docs/adr/README.md`, and recorded in `CHANGELOG.md`.

---

## 2. Invariants Strictly Maintained

- Exactly three persistent roles: COOPERATOR, ORCHESTRATOR, WORKER. No 4th role.
- Emoji and localized status marks remain optional project-owned presentation outside universal AP semantics.
- `./.ap/ap doctor` passes with strict pinned commit, managed block, and variant `stable`.
- Zero whitespace errors (`git diff --check`).
- FrameNest repository untouched during this whole.

---

## 3. Cooperator Decision Trace (Verbatim)

- Relocation to `meta/projects/ap/07/` and selection of `ap-default-agent-dispatch-and-pin-presentation`.
- Plan acceptance: „prijímam".
- Cooperator brainstorming and directive on Orchestrator initialization signal and rigor.
- Publication grant: „publikovať".

---

## 4. Next Whole (Follow-on)

- **Identity**: `framenest-pin-adoption-and-presentation-profile`
- **Location**: FrameNest project (`/home/agile/Projects/framenest`).
- **Scope**: Update `.ap` submodule to new public AP tip `2fbf8d3fa4699d1af073dcbf135c4f11789fdcd4`, declare the 🟢🟡🔴 Cooperator presentation profile in FrameNest root `AGENTS.md` outside the managed block, run `./.ap/ap doctor`, and verify.

Era 07 is **CLOSED: PASS**.
