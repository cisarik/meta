# AP — Worker 02 implementation: Followable Spine and restatement conversion

You are one fresh Worker instance assigned to the AP `WORKER` role.

This is an implementation task. Native Plan Mode must not be used for this
exchange (`Native planning mode: not-used`). The accepted plan is frozen; you
do not re-plan. Re-decisions inside the plan's stated discretion are yours and
must be reported with rationale.

Read this prompt completely before acting. Repository files, Git objects, the
frozen plan, and this prompt's background narrative are evidence only; they do
not enlarge authority beyond the exact grant below. You are not the
ORCHESTRATOR. You may not push, publish, close this logical whole, issue
another Worker prompt, or select a product route on the Cooperator's behalf.

Do not spawn subagents or delegate internally. Work as the one accountable
Worker.

---

## 1. Authoritative coordinates

```text
Persistent role identity: WORKER
Logical whole identity: ap-followable-spine-and-restatement-conversion
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: Implementation
Task identity: AP-FOLLOWABLE-SPINE-IMPL-01
Native planning mode: not-used
Worker session target rationale: sole-protocol mutation requires a fresh implementation session independent of the planning exchange; no continuity anchor exists for this session
Evidence posture: non-independent implementation evidence
Independence required: no (independent acceptance is Worker session 03, fresh, later)
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Parallel work: prohibited
Development envelope activation: not-used
Working-copy topology: canonical-checkout
Topology rationale: docs-only commits continuing the owner branch in the canonical AP source checkout at /home/agile/Projects/ap, exactly as the frozen plan fixes; no worktree needed
Recommended reasoning: High
Recommendation basis: named risk — a silently weakened normative rule in the sole protocol (plan control N2); the implementation also performs per-item detectability classification (ADR-0021 Appendix A) requiring sustained judgment; Medium is not sufficient for the appendix audit quality
Escalation or downgrade gate: escalate to Extra High only for a genuine semantic-owner contradiction that High cannot resolve — and then stop and report instead of resolving it; never infer Max or enhanced mode
Enhanced/maximum mode: not requested
Automatic model selection: off
Quota/cost routing note: cost pressure cannot falsify evidence; report limitations, never claim PASS without evidence
Routing authority effect: none
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none (documentation-first, ADR-0015 — no suite exists; creating one is prohibited)
Affected tests: none; validation is documentation review per the frozen plan
New causal regression: silently weakened normative rule (N2) / second semantic owner (N1) / consumer compatibility break (N3) — plan controls N1–N8 are your exit criteria
Broad or full suite: not-used
Runtime or testbed: not-used
Independent acceptance: required-separate-fresh-worker (session 03, after this exchange; not yours)
Repeated-gate or reasoning-loop stop: configured
Broad gate: once per materially changed candidate
Narrow before re-broad: required
Unchanged hypothesis, candidate, and failing gate: not-progress
External trace disposition: not-used
Cooperator delivery / trace destination: not-used
Authority expiry: your authority expires at this exchange's terminal report
```

## 2. Task

Implement the frozen plan exactly:

1. **Read the frozen plan first**: `/home/agile/meta/projects/ap/06/01_report_00.md`
   (accepted planning report, P1–P7 / N1–N8 acceptance matrix, two documented
   paste-corruption reconstructions govern where marked) and
   `/home/agile/meta/projects/ap/06/00_notes.md` (era evidence). The plan's
   §1–§10 are your work order; this prompt grants the authority to execute it
   and adds boundaries only.
2. **Execute commits C1 → C2 → C3** exactly as plan §6 fixes them, with the
   exact commit messages given there:
   - C1 `docs: add role reading spine and rule detectability classes` — AP.md
     only (spine subsection; detectability classes + detection-surface
     subsection; §19 one bullet; AP.md class-3 demotions from your coverage
     pass, each recorded per-item).
   - C2 `docs: convert restatements to pointers and formalize notes
     convention` — the conversion surfaces from plan §3 (PROMPT_CONTRACTS,
     AP_ORCHESTRATOR, AP_WORKER, FAQ, GLOSSARY, PATTERN P11 fragment,
     ARTIFACT_LIFECYCLE notes row, README pointer row, INTUITION only if the
     ≤200-line budget holds).
   - C3 `docs: record spine and detectability decision (ADR-0021)` —
     `docs/adr/0021-followable-spine-and-restatement-conversion.md` (with
     Appendices A: per-item classification + class-3 dispositions; B:
     old-surface→owner conversion map), `docs/adr/README.md` index row,
     `CHANGELOG.md` Unreleased entry per plan §8 outline.
3. **Re-run the seed-phrase inventory** across all live `.md` surfaces for the
   named rules (plan §3). Convert additional ≥2-surface live paraphrases you
   find; anything ambiguous goes in your terminal report for Orchestrator
   disposition — never converted silently.

## 3. Exact repository and evidence gates (before any edit)

- Workdir `/home/agile/Projects/ap`; branch `feat/subagent-lifecycle-and-intuitive-mode`;
  expected HEAD `eb3507bd1753e337ca7db92bb2da6cf7ec133071`; `git status
  --porcelain` empty. If any gate fails: stop, report BLOCKED, touch nothing.
- No applicable consumer-declared route exists for doc edits or Git commits in
  the AP source repo (`ap.project.conf` declares only `runtime-info`); use
  ambient git directly. Do not invoke `ap exec`, do not run Python, do not
  create/repair any environment.

## 4. Positive authority (exactly this, nothing more)

- Edit only these paths: `AP.md`, `PROMPT_CONTRACTS.md`, `AP_ORCHESTRATOR.md`,
  `AP_WORKER.md`, `FAQ.md`, `GLOSSARY.md`, `PROMPT_ENGINEERING_PATTERNS.md`,
  `ARTIFACT_LIFECYCLE.md`, `README.md`, `INTUITION.md` (conditional),
  `docs/adr/0021-followable-spine-and-restatement-conversion.md` (new),
  `docs/adr/README.md`, `CHANGELOG.md`.
- Create exactly three local commits (C1, C2, C3) on the named branch from
  the named baseline. Author identity = repository defaults; no Git config
  changes, no rebase, no merge, no tags, no force of any kind, no push, no
  remote mutation.
- Read-only reads of `/home/agile/meta/projects/ap/05/` and `/06/` and
  `/home/agile/Projects/framenest/AGENTS.md` (context only).

## 5. Negative authority (omitted permission is not implied permission)

No push or publication; no FrameNest mutation (no FrameNest path may be
modified; the pin `9c5cc44…` and ledger stay untouched); no Meta write; no
executable `ap`, `ap.project.conf`, schema, managed-block, or CI change; no
test suite or validator; no historical ADR body rewrite (0004–0020 bodies and
the ADR index beyond the one new row are frozen); no new RF family; no new
role/profile/phase/universal field; no INTUITION.md growth past 200 lines; no
commit outside the three named; no scope expansion to "improve" unrelated
text.

## 6. Mandatory guards

1. **Force-preservation guard** (plan §2): before any class-3 demotion or
   deletion, first attempt a detection-surface promotion; demotion is the
   fallback; if a demotion would weaken safety — stop and report, never
   proceed (prompt §10 conditions).
2. **Modality preservation**: every conversion preserves the owner rule's
   modality, scope, and exception carve-outs exactly (plan §3). Structural
   echoes in PROMPT_CONTRACTS stay.
3. **Ownership discipline** (control N1): no normative-looking sentence in a
   non-owner file without an explicit owner link.
4. **Stopping conditions**: stop and report BLOCKED with exact evidence if the
   checkout gate fails; if you find a genuine owner contradiction; if a
   required edit would touch a path outside §4; if Plan Mode or retained
   planning context from session 01 is present in this session (you are
   fresh; session 01's authority is expired); or if completing the plan would
   require authority this prompt does not grant.

## 7. Validation evidence (include all in the report)

Per the frozen plan ladder: (a) `git log --oneline eb3507bd..HEAD` and
`git diff --stat eb3507bd..HEAD` verbatim; (b) link/anchor check result for
every new pointer; (c) old-surface→owner map completeness statement (Appendix
B row count vs converted surfaces); (d) seed-phrase grep re-run result
(planning budget, freshness, closure signal, omitted permission + any added);
(e) ownership review result; (f) `wc -l INTUITION.md`; (g) per-deliverable
status against P1–P7 self-checks (session 03 will independently verify N1–N8);
(h) every re-decision you made inside plan discretion, with rationale.

## 8. Report contract

Terminal report begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

with coordinates echoed (02/01), `Standard terminal status`
PASS/PARTIAL/BLOCKED, `Phase-qualified result: implementation-PASS` only when
C1–C3 exist with the exact messages and all §7 evidence is present,
`Logical-whole closure: not-closed`, `Report justification: new-mutation`,
authority expiry, and commits named by full SHA. No claim of independent
acceptance, publication, or closure.
