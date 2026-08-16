---
name: Route Binding Plan
overview: "Current public AP does not yet make an applicable consumer-declared execution operation or capability gate canonical in the Worker prompt, nor reject an equivalent-looking ambient route. Recommend Shape A: docs/projection-only clarification of RF-06 and RF-16, with no new record, command, schema, or executable `ap` change."
todos:
  - id: impl-ap-md
    content: Clarify RF-06/RF-16, §5, prompt-synthesis, compact communication, stopping, and anti-patterns in AP.md
    status: pending
  - id: impl-projections
    content: Project the same invariant into AP_ORCHESTRATOR.md, AP_WORKER.md, PROMPT_CONTRACTS.md Commands fields, and P08 fixtures
    status: pending
  - id: impl-historical
    content: Add ADR-0018 plus CHANGELOG and adr README historical projections
    status: pending
  - id: verify-docs-only
    content: "Independent acceptance: semantic/projection review, positive/negative/deviation/no-route/pin-compat checks; no ap or suite change"
    status: pending
isProject: false
---

# Consumer-declared route binding — implementation plan

## Native Plan Mode

Active. This artifact grants **no implementation authority**. Execution requires a later complete Orchestrator prompt with `Native planning mode: not-used` and a fresh Worker session.

## Verdict

**AP change required.** Ledger recommendation (do not mutate now): keep the unique FrameNest entry `consumer-declared-execution-and-capability-route-binding` `untriaged` until a separately authorized FrameNest task; then `accepted` → `implemented` after durable public AP evidence. Not `duplicate`, `invalidated`, `parked`, or `rejected`.

ADR-0017 overlaps only the optional development-envelope-by-reference and “do not recopy declared tooling” posture. It does not own prompt-vs-declared-route contradiction, Orchestrator pre-issuance resolution duty, or natural-language capability-gate binding.

## Why change is justified

Field evidence (FrameNest `5abb2adf…` → public `fc355d6…`): project already had `ap.project.conf` operations and a project SSH gate, but authoritative prompts still offered or reconstructed ambient raw Python/SSH. FrameNest closed the **consumer** whole and left this AP observation `untriaged`.

Current public AP `95bd6448…`:

- `ap exec` enforces a declared operation **only after** the Worker invokes it ([ADR-0012](https://github.com/cisarik/ap/blob/95bd644829d48dcd188627f3e495e649df577eca/docs/adr/0012-baseline-bound-project-execution.md)).
- Common Worker Task Fields `Commands` may list raw interpreter/shell/SSH beside a declared route; no contradiction rule exists.
- Development Envelope Activation may legally remain `not-used` (different object from `ap.project.conf`).
- Prompt-synthesis readiness lists “path and command authority” and “explicit project-specific deviations” but does not require resolving an applicable consumer-declared route first.

## Chosen shape: A (minimal clarification)

Compare:

- **A — refine RF-06/RF-16 + projections.** Existing fields can express route identity (`Commands` / required reading), canonical use, contradictory-route prohibition (`Negative authority`), and bounded deviation (explicit deviation in the prompt). No new annex.
- **B — new structural record.** Rejected: would duplicate Development Envelope, `Commands`, side-effect, and capability-handshake fields.
- **C — no AP change.** Rejected: ADR-0017 and FrameNest consumer docs do not own the prompt-construction invariant; `ap` never sees the prompt.

**Documentation versus executable:** `Docs/projection only`. `ap` has no prompt surface; a validator would parse wording. ADR-0015 forbids a new conformance suite.

## Exact later semantics (implementation Worker)

Applicability: consuming project has a **usable** declared route for the task — either a baseline-declared `ap.project.conf` operation, or a project-owned capability gate named in project rules (not only machine-readable conf). Absence of both is valid compatibility; fallback is exact project-owned guidance, not an AP-invented toolchain.

Orchestrator **must** resolve governing AP baseline and any applicable declared route **before** issuance. When usable, the prompt names it as canonical. Copied raw interpreter/shell/SSH/reconstructed ambient routes must not appear as an equivalent parallel route.

Deviation is lawful only when the declared route is unavailable or unsuitable: record the declared route, exact alternate, rationale, evidence class, bounded authority, and stop. A deviation is not a second standing canonical route.

Ambient IDE/terminal/socket/prior session is convenience state, not authority. Classify an ambient-environment failure before remediation; one focused reproduction through the declared sanitized route is preferred.

Historical pins keep original meaning. FrameNest pin `17b7e085…` is unchanged until a later adoption whole.

## Later path allowlist (AP only)

Semantic owner:

- [AP.md](/home/agile/Projects/ap/AP.md) — RF-06, RF-16, §5, prompt-synthesis readiness, Compact Communication, stopping, anti-patterns

Operational/structural (at most 4):

- [AP_ORCHESTRATOR.md](/home/agile/Projects/ap/AP_ORCHESTRATOR.md) — prompt construction / command authority
- [AP_WORKER.md](/home/agile/Projects/ap/AP_WORKER.md) — contradiction stop, ambient classification
- [PROMPT_CONTRACTS.md](/home/agile/Projects/ap/PROMPT_CONTRACTS.md) — `Commands` / positive/negative authority purpose text; no new record
- [PROMPT_ENGINEERING_PATTERNS.md](/home/agile/Projects/ap/PROMPT_ENGINEERING_PATTERNS.md) — P08 generic positive + parallel-raw negative fixture (no FrameNest names)

Historical:

- `CHANGELOG.md`
- new `docs/adr/0018-consumer-declared-execution-route-binding.md`
- `docs/adr/README.md`

**Forbidden:** `ap`, `ap.project.conf`, managed `AGENTS.md` block, schema, new RF family, new command, tests/conformance suite, FrameNest, Meta, pin, NUC, FAQ/README/GLOSSARY/INTEGRATION unless a later review proves inconsistency (default: untouched).

## Lifecycle after approval (no authority now)

1. Fresh implementation prompt, `Native planning mode: not-used`
2. One implementation attempt on the allowlist
3. Bounded correction only for one classified defect
4. Fresh independent acceptance
5. AP publication + credential-free `ls-remote`
6. **AP closure after publication/acceptance** (consumer ledger and pin adoption stay separate, matching ADR-0016/0017)
7. Later FrameNest ledger `implemented` with public AP SHA as disposition evidence
8. Optional later FrameNest pin adoption; no NUC/product work

## Complexity Budget

Within presumptive maxima: 1 semantic owner, 2 RF families, 4 projections, 1 ADR, 0 executable surfaces, 0 consumer repos, 0 schema/managed-block/command changes, 1 plan-only cycle, 1 implementation attempt, 1 independent acceptance.
