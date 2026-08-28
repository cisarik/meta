# Field observations — `framenest-ap-field-test` against AP pin `86ae6e8c`

Relationship: historical evidence for this whole and non-authorizing input to
the successor whole. Not task authority. Not an AP semantic owner. Not a
FrameNest ledger row until a later exact grant writes
`docs/AP_UPGRADE_OBSERVATIONS.md`.

Observed: 2026-08-28, Orchestrator session 01 of `framenest-ap-field-test`,
Mode 1, Worker session 01 / exchange 01.
Governing AP: public `https://github.com/cisarik/ap.git` `refs/heads/main` =
`86ae6e8c27d2b919d776021bee915b7292908b0e` (also FrameNest `.ap` gitlink and
worktree). This **is** the published tip. Local `/home/agile/Projects/ap` at
the same SHA has **no** commits ahead of `86ae6e8c`. The gaps below are in
the published protocol, not a missing push and not a wrong pin.

Cooperator (Michal) correction and design intent, 2026-08-28, recorded
verbatim in `00_notes.md` and `02_closure.md`.

---

## 0. What the field test proved (so these observations are not a failed pin)

Eight-check score under Mode 1: **PASS** on checks 2, 3, 4, 6, 7.

Proof he is on the new AP: pin SHA above + `./.ap/ap doctor` PASS (strict
pinned commit, managed `AGENTS.md` block, variant `stable`).

Ledger entry `consumer-declared-execution-and-capability-route-binding`
moved `untriaged` → `accepted` at FrameNest commit
`85028f725537adcf922f2587d62f1bad68cd5924` (allowlist
`docs/AP_UPGRADE_OBSERVATIONS.md` only; still `non-authorizing`;
`retain-active`). Isolated-worktree `ap exec --root <worktree>` launch-path
miss still exists at this pin (`.ap/ap` resolves
`runtime.cpython.executable` relative to `--root`; fail string at lines
857–859). That is a **different** observation from the three below.

Catastrophe path (revert `d0ea8c8…`) was **not** taken.

---

## 1. Observation A — Agent Orchestrator default dispatch

### Stable identifier (proposed ledger Entry)

`agent-orchestrator-default-dispatch-unless-cooperator-opts-out`

### One-line summary

A spine-following Agent Orchestrator with a working dispatch client used the
Cooperator as a copy-paste message bus, because published AP defaults dispatch
to `not-used` and treats ambient dispatch capability as non-authorizing, while
Cooperator ergonomics forbid that bus when a delivery route exists.

### What happened (durable evidence)

1. Restoration handout `00_handout.md` named the profile **Agent Orchestrator**
   and invariant 4: no manual message-bus work where a route exists;
   copy-paste is the lawful fallback; dispatch only if Michal selects it.
2. Mode 1 (verbatim `1`) asked the Orchestrator to issue one real Worker task
   as the leanest path. The Orchestrator issued
   `01_implementation_00.md` for copy-paste into a new chat.
3. The client in this session exposes session-dispatch (Cursor Task /
   subagent). The Worker task had `Independence required: no`.
4. Michal opened a Worker chat, pasted, ran the task (commit `85028f7…`),
   then had to ferry the report back. He stated the new AP should have the
   Agent Orchestrator create subagents unless he explicitly says otherwise,
   and that he needs to be the messenger **when he wants a different model**.

### What the published pin actually says

Quoted owners (do not treat this file as a second owner):

- AP.md §3 Orchestrator capability profile: dispatch when the
  Cooperator-selected route **or** accepted plan authorizes it; default
  remains not-used; copy-paste remains lawful; parent-context spawn is not a
  fresh independent session.
- ADR-0019: whole-or-route authorization; ambient tool availability does not
  authorize (ADR-0018 lesson); default remains not-used; rejected
  per-spawn microapproval.
- AP_ORCHESTRATOR.md decision table: dispatch only when selected route or
  accepted plan authorizes it; otherwise copy-paste.
- Handout §6.4 over-specified “dispatch only if Michal selects it”, which a
  fresh Orchestrator read as **opt-in**, not **opt-out**.

There is **no** published resolution order among:

| Rule | Effect in this incident |
|---|---|
| Default dispatch `not-used` | Orchestrator does not dispatch |
| Ambient capability does not authorize (ADR-0018/0019) | Task-tool presence is not a grant |
| No Cooperator message-bus where a route exists | Dispatch should have been used |
| Parent-context spawn cannot be independent (RF-05) | Over-applied to a non-independent Worker |
| Mode 1 “leanest” | Copy-paste was the opposite of lean for the Cooperator |

A spine-following Orchestrator conservatively picks the first two and
produces Cooperator labor. Detection surface today: Cooperator complaint
(behavioral-normative). No report field, doctor check, or ledger gate
fails.

### Cooperator-selected design (this is intent, not yet AP text)

1. **Default for Agent Orchestrator:** deliver one complete authoritative
   Worker prompt into one concrete session (dispatch / subagent) **unless**
   the Cooperator explicitly opts out.
2. **Lawful opt-out:** Cooperator wants another model, another client, or
   says he will be the messenger. Then copy-paste is the route (P14 model
   rotation), not a failure.
3. **Independence unchanged:** a parent-context spawn still cannot provide
   independent acceptance (RF-05). Default dispatch is for ordinary
   non-independent Workers. Independent acceptance still requires a
   genuinely fresh session under the vendor-neutral functional test
   (prompt-only initial context, no parent transcript, own terminal report).
4. **Pin-time consumer overlay:** this default must be integrated into
   consumer `AGENTS.md` at pin / `ap init` / `UPDATING.md` apply, so a
   spine-following Orchestrator in FrameNest does not have to rediscover it
   from INTUITION.md (reference-on-demand) or a Meta handout.

### Classification

- AP-defect candidate (followability / Cooperator ergonomics), not a
  FrameNest product defect, not a wrong pin.
- Detectability: behavioral-normative today; the successor whole should
  give it an artifact detection surface (prompt routing field, consumer
  `AGENTS.md` declaration, and/or doctor-visible pin checklist) or
  deliberately keep it behavioral with a named surface.
- Suggested RF owners to inspect (planner decides, this file does not
  add a family): RF-02 (dispatch delivery), RF-05 (fresh vs parent-context),
  RF-06 (capability ≠ authority), RF-15 (pin/init consumer projection),
  RF-19 (Orchestrator archives after outcome when dispatch returns the
  report in-session).

### Non-goals

- Fourth persistent role.
- Vendor-required Cursor Task tool.
- Treating dispatch capability as task authority.
- Claiming a parent-context subagent is an independent audit.
- Forcing dispatch when the Cooperator wants another model.

---

## 2. Observation B — Worker must not archive; Cooperator became archivist

### Stable identifier (proposed ledger Entry)

`trace-companion-archival-owner-versus-cooperator-message-bus`

### One-line summary

Published AP forbids the Worker from archiving the prompt/report pair and
assigns archival to the Orchestrator after the report exists; combined with
copy-paste delivery this made the Cooperator both courier and archivist, and
the first archived `01_report_00.md` was a byte-identical copy of the prompt.

### What happened

- Prompt `01_implementation_00.md` set `External trace disposition:
  configured`, `Archival: wait-for-report`, `Trace archival owner:
  ORCHESTRATOR`, and explicitly: “The Worker does not write, archive, or
  edit the trace directory.”
- That restates PROMPT_CONTRACTS.md Cooperator Delivery record (“The Worker
  does not archive the current pair”) and RF-19 / RF-02 (Orchestrator
  archives after the outcome exists).
- Michal expected the Worker to write `01_report_00.md`. The Worker
  following the grant must not. He copy-pasted; first archive was the
  prompt (343 lines, `cmp` identical). He later replaced it with the real
  23-line report. Check 6 could be scored only after that correction.
- AP has no check that a companion named `*_report_*.md` is a report rather
  than the prompt.

### Cooperator-selected design intent (coupled to Observation A)

When dispatch is the default, the Orchestrator receives the terminal report
in-session and **must** archive the exact prompt + actual outcome into the
activated trace. The Worker still does not self-grant trace writes. The
Cooperator is not the archivist. Copy-paste opt-out (other model) remains
the case where the Cooperator ferries text; the Orchestrator still archives
after receiving it, and must reject a companion that is identical to the
prompt.

### Classification

- Partly AP followability (no companion-integrity check; archival owner vs
  Cooperator expectation undocumented in the spine).
- Partly consequence of Observation A (wrong delivery route).
- Suggested owners: RF-19 (trace archival), RF-02 (Orchestrator-direct
  archival), PROMPT_CONTRACTS delivery record. Not a new role.

---

## 3. Observation C — Emoji / Cooperator presentation dropped after the pin

### Stable identifier (proposed ledger Entry)

`consumer-pin-does-not-activate-presentation-profile-or-emoji`

### One-line summary

Era-06 AP moved emoji out of the protocol (not an AP field; optional
project-owned presentation; inactive by default). FrameNest `AGENTS.md`
outside the managed block never declared a presentation profile at pin
`86ae6e8c`, so a spine-following Orchestrator emitted none. Michal noticed
immediately.

### What the published pin actually says

- AP.md §19: treating a Cooperator presentation profile, emoji, localized
  capsule, or downloadable filename as **task authority** is an anti-pattern.
- RF-02: **when project rules activate** a Cooperator presentation profile,
  the Orchestrator **must** emit it after the copyable English Worker prompt.
- INTEGRATION.md “Optional Presentation Profile…”: declare in root
  `AGENTS.md` outside the managed block; absence preserves current behavior;
  emoji set is not universally required.
- INTUITION.md §7: signaling is project-owned optional presentation,
  inactive by default. INTUITION.md is **reference-on-demand**, not on the
  ORCHESTRATOR spine.
- UPDATING.md pin checklist: verify `AGENTS.md` still points to `.ap/`;
  it does **not** require declaring or refreshing a presentation profile.
- `ap init` managed block names AP.md / handbooks / PROMPT_CONTRACTS; it
  does not template emoji or dispatch-default overlay.

This is the ADR-0021 motivating failure mode (signaling dropped because it
had no detection surface) relocated to the **consumer overlay**: AP moved
marks out; the pin route did not write them back into FrameNest
`AGENTS.md`.

### Cooperator-selected design

1. At pin / `ap init` / `UPDATING.md` apply, consumer `AGENTS.md` (outside
   the managed block) receives a project-owned presentation profile if the
   project wants one — FrameNest does: emoji status marks for Michal.
2. Proposed FrameNest marks (presentation only, never Worker-authority
   fields, never copied into the Worker grant as AP fields):

```text
🟢 healthy / proceed / PASS
🟡 wait / one open decision
🔴 stop / BLOCKED / catastrophe
```

3. Emission: one-glance state at the top of Orchestrator-to-Michal
   messages (Slovak). Not an AP field. Not a fourth role.

### Classification

- Consumer overlay gap (FrameNest `AGENTS.md`) **and** AP pin-route gap
  (`UPDATING.md` / `ap init` / INTEGRATION.md do not make the optional
  declaration discoverable at pin).
- Detectability: Cooperator complaint. Successor should give pin-time a
  detection surface (checklist item or managed-adjacent template) without
  making emoji universal AP.

---

## 4. Cross-cutting: why a fresh Orchestrator “forgets”

| Mechanism in pin `86ae6e8c` | Field effect |
|---|---|
| Per-role spine is a floor; INTUITION.md and INTEGRATION optional profiles are reference-on-demand | Dispatch default and emoji are not in the first-exchange reading list |
| Default dispatch `not-used` + ambient ≠ authority | Conservative Orchestrator never dispatches |
| Parent-context disqualifier written more saliently than “no message-bus” | All subagents treated as independence fraud |
| Worker must not archive; Orchestrator archives after | With copy-paste, Cooperator is the only person holding the report |
| Presentation profile inactive by default; pin checklist does not mention it | Emoji vanish at adoption |
| Handout-local over-specification (“dispatch only if he selects”) | Overrides Agent Orchestrator capability in the restoration prompt itself |

None of these break `ap doctor`. Followability failed in Cooperator UX,
which is exactly what era 06 claimed to improve.

---

## 5. Suggested successor shape (non-authorizing)

Logical whole (Cooperator-selected 2026-08-28):
`ap-default-agent-dispatch-and-pin-presentation`

**Meta home (relocated 2026-08-28):**
`/home/agile/meta/projects/ap/07/00-ap-default-agent-dispatch-and-pin-presentation/`
not FrameNest `10/` (consumer field-test tree). Mutation owner is
`cisarik/ap`. FrameNest `AGENTS.md` overlay is a **later pin-adoption
whole** after AP publishes — same split as era-06 closure.

Primary repository: `https://github.com/cisarik/ap.git` checkout
`/home/agile/Projects/ap` at `86ae6e8c…`.

Recommended sequence (Orchestrator owns; Worker plans then implements):

1. Read-only restoration of AP + these observations.
2. Implementation planning (one cycle) naming exact AP.md / projection /
   UPDATING / INTEGRATION / `ap init` owners, detection surfaces, and the
   model-opt-out exception.
3. Cooperator accepts the plan (material protocol design).
4. Implementation on AP; independent acceptance as required for semantic
   owner mutation; publication grant.
5. Separate FrameNest pin-adoption whole: new gitlink + `AGENTS.md`
   presentation overlay (🟢🟡🔴). Do not hide product scope there.
6. Do not silently absorb Observation A/B/C into the already-`accepted`
   launch-path ledger entry. New entries keep stable identifiers above.

---

## 6. Inventory of cited surfaces (coverage for exhaustive successor work)

Must be re-read at the pin, not from this paraphrase:

- `.ap/AP.md`: §3 capability profiles and dispatch; RF-02, RF-05, RF-06,
  RF-15, RF-19; §17 compact communication; §19 anti-patterns (emoji as
  authority; opaque tool-task swarms; parent-context as independent audit).
- `.ap/AP_ORCHESTRATOR.md`: Continuation Bootstrap; Capability Profiles,
  Dispatch, and Direct Action; per-whole `00_notes.md`.
- `.ap/AP_WORKER.md`: session target; Worker does not archive unless
  separately granted.
- `.ap/PROMPT_CONTRACTS.md`: session-and-mode routing; Cooperator Delivery
  and Trace Destination; Worker Exchange Identity; ledger contract.
- `.ap/PROMPT_ENGINEERING_PATTERNS.md`: P01, P02, P03, P04, P06, P11, P14,
  P16, P19 (selected for the staged planning prompt).
- `.ap/INTEGRATION.md` optional presentation profile.
- `.ap/UPDATING.md` review checklist.
- `.ap/INTUITION.md` §7 (explanatory; never owner).
- `.ap/docs/adr/0017-*.md`, `0018-*.md`, `0019-*.md`, `0021-*.md`.
- FrameNest `AGENTS.md` (managed block + overlay).
- FrameNest `docs/AP_UPGRADE_OBSERVATIONS.md` (existing `accepted` entry
  stays; do not conflate).

---

*End of observations. Successor mutation requires a new complete prompt.*
