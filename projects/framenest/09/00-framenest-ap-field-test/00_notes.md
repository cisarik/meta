# Orchestrator notes — `framenest-ap-field-test`

Relationship: local AP-run convention (`00_notes.md` beside the whole handout).
Orchestrator-only, append-only, dated, English, public-safe. Evidence, never
authority. Created at whole open after verified predecessor selection.

Logical whole: `framenest-ap-field-test`
Orchestrator session: 01 (this chat). Worker session ordinal starts at 01 when
a Worker prompt is issued.

---

## 2026-08-28 — Restoration (Stage 1 re-verified; Stage 2 not re-asked)

### Immediate gates (tool-verified this session)

| Check | Expected (handout) | Observed |
|---|---|---|
| Public AP `refs/heads/main` | `86ae6e8c…` or classify if moved | `86ae6e8c27d2b919d776021bee915b7292908b0e` — equal to pin; tip has not moved |
| FrameNest `HEAD` | `d0ea8c8e50c2884f1dbdd4643fa83494b72c4cc7` | match |
| FrameNest porcelain | empty | empty |
| `.ap` worktree `HEAD` | `86ae6e8c…` | match; gitlink `160000 86ae6e8c…` |
| `./.ap/ap doctor` | PASS, strict pinned commit | `ap doctor: PASS`; strict pinned; managed `AGENTS.md` block OK; variant `stable` |
| Ledger entry `consumer-declared-execution-and-capability-route-binding` | `state: untriaged` | confirmed; last revalidated against `5abb2adfcd1d5f3391df9c3044b4b81ac1aac923`, not yet against the adopted pin |
| Era directory | this whole's files | `00_handout.md` only before this notes file |

Pin-adoption commit `d0ea8c8…`: 1 file (`.ap` gitlink). Parent is product freeze
`472553cadcd3d4ca87a9792a2c306bd0afeea7c1`. Branch
`feat/x-meme-browser-companion` is ahead of `origin` by 9 commits (project
practice; this whole has no push authority). NUC out of scope.

No evidence/prompt contradiction on the numbered gates. Public AP `main` has
not moved beyond the adopted pin.

### Predecessor Cooperator selection (verbatim; not re-asked)

Intake recorded in `00_handout.md` Section 3. Michal selected this whole in
the predecessor session (2026-08-27). This restoration does not re-open Stage 2
discovery. Chicken-and-egg for field-test check 3 is recorded under scoring
notes below.

### Required reading completed this restoration

ORCHESTRATOR spine floor from `.ap/AP.md` ("Per-Role Minimum-Reading Spine"):
named `AP.md` anchors in that row; `.ap/AP_ORCHESTRATOR.md` (Continuation
Bootstrap + per-whole notes); `.ap/PROMPT_CONTRACTS.md` (structures; ledger
contract location verified); project-root `AGENTS.md` (managed block + product
overlay). Additional handout-named surfaces: detectability subsection and
RF capsules as needed; `.ap/AP_WORKER.md` opening; ADR-0021; ledger file;
`ARTIFACT_LIFECYCLE.md` notes row.

### Check 2 candidate from this Orchestrator (not yet scored as independent)

Asked of this session by the restoration prompt itself: what must be read
before the first exchange in a new whole?

Short list matching the ORCHESTRATOR spine (not "everything", not a shrug):

1. `.ap/AP.md` — the ORCHESTRATOR row of **Per-Role Minimum-Reading Spine**
   (named `AP.md` sections in that table, including RF capsules listed there).
2. `.ap/AP_ORCHESTRATOR.md`
3. `.ap/PROMPT_CONTRACTS.md` (prompt issuance and activated annexes)
4. Project-root `AGENTS.md`

Prompt-named required reading and activated surfaces add to this floor.
Reference-on-demand surfaces (`PROMPT_ENGINEERING_PATTERNS.md`, `INFOSEC.md`
only when activated, `ARTIFACT_LIFECYCLE.md` for artifact work,
`INTEGRATION.md`/`UPDATING.md` for integration or update tasks) are not the
minimum.

Scoring caveat: this answer was produced under a rich restoration handout, not
under a minimal resume seed. Stronger independence for checks 2–3 requires
Mode 2.

### Field-test check tracking (in progress)

| Check | Status this session | Note |
|---|---|---|
| 1 Fresh Orchestrator from a standard resume seed | partial | This chat is a fresh Orchestrator; the seed was the rich `00_handout.md`, not the non-normative minimal seed in `AP_ORCHESTRATOR.md`. |
| 2 Spine reading list | candidate recorded above | Mode 1 would score this chat; Mode 2 scores a separate subject. |
| 3 Stage 2 proposes exactly one whole and asks to select | predecessor-complete | Handout forbids re-asking. Mode 1 scores Stage-2 *behavior* (this whole already selected), not discovery. Mode 2 can still demonstrate discovery. |
| 4 `00_notes.md` created beside handout, dated, selection recorded | this file | Created 2026-08-28 at open. |
| 5 One real Worker task with coordinates + WORKER spine reading | pending | After mode choice. |
| 6 Report begins `### Report for ORCHESTRATOR_CHAT` and echoes three coordinates | pending | |
| 7 Notes gain a dated Worker-claim review | pending | |
| 8 PASS iff 2, 3, 4, 6, 7 hold | pending | Individual failures are field observations / ledger candidates, not catastrophe unless tooling or safety breaks. |

### Ledger (deferred to execution step 5.d; no mutation)

Active entry remains `untriaged` / non-authorizing. Triage against pin
`86ae6e8c…` is in-scope for this whole and is not started.

### Open Cooperator decision

Mode of the field test: Mode 1 (this session as subject) vs Mode 2 (separate
subject session / authorized fresh dispatch of a seed-only subject).
Orchestrator recommendation: Mode 2 for evidence quality. Honor either choice
without relitigating.

No Worker prompt issued. No FrameNest, AP, or Meta Git writes. No NUC contact.

---

## 2026-08-28 — Mode 1 selected (verbatim)

Cooperator reply in this chat (verbatim): `1`

Interpreted as Mode 1 (this Orchestrator session as subject). Recommendation
was Mode 2; the Cooperator choice is honored without relitigation.

Scoring under Mode 1 (chicken-and-egg recorded):

- Check 2: Orchestrator answers the spine list in the same chat that issues
  the Worker prompt (rich-handout caveat remains).
- Check 3: this whole was already selected; Stage 2 *behavior* is that exactly
  one whole is in force (`framenest-ap-field-test`) and is not re-opened.
- Check 4: this notes file already exists with the selection recorded.
- Checks 5–7: Worker session `01` / exchange `01` issued as
  `01_implementation_00.md` (copy-paste delivery; dispatch not selected).
  Ledger triage is the one real Worker task (handout 5.d).

No FrameNest, AP, or Meta Git writes in this notes update.

---

## 2026-08-28 — Cooperator correction: dispatch, archival, emoji

Cooperator (verbatim intent): Worker should have saved `01_report_00.md`;
Orchestrator should have launched the Worker as a subagent under the new AP;
look at why the new version forgets these; emoji signals for him are missing.

### Immediate file/git facts (tool-verified)

- `01_report_00.md` is byte-identical to `01_implementation_00.md` (`cmp`
  silent; both 343 lines). It is the prompt, not a Worker terminal report.
  Cooperator said he copy-pasted from Worker output; the archived companion
  does not contain `implementation-PASS`, start/end commit, or a compact
  core. Check 6 cannot be scored from this file.
- FrameNest HEAD is `85028f725537adcf922f2587d62f1bad68cd5924`
  (`docs: triage AP upgrade observation to accepted`; parent `d0ea8c8…`;
  only `docs/AP_UPGRADE_OBSERVATIONS.md`; porcelain empty). Ledger entry is
  `accepted`, `Last revalidated against: 86ae6e8c…`, still non-authorizing.
  Mutation happened; the durable report text is not in the trace.

### Why these drop under pin `86ae6e8c…` (classification, not apology)

1. **Dispatch vs copy-paste (AP defect candidate + Orchestrator miss).**
   Pin text: Agent Orchestrator may dispatch when the Cooperator-selected
   route or accepted plan authorizes it; default stays `not-used`; copy-paste
   remains lawful; ambient capability does not authorize (ADR-0018/0019);
   a parent-context spawn is not a fresh independent session (RF-05).
   Handout §6.4: dispatch only if Michal selects it. This Orchestrator
   treated Mode 1 + that sentence as copy-paste, and used him as the
   message bus.
   Competing rule with no resolution order: Cooperator-experience
   "no manual message-bus where a route exists" vs default-not-used vs
   ambient-does-not-authorize. A spine-following Orchestrator picks the
   conservative fork. Detection surface is Cooperator pain, not an
   artifact. Independence was `no` on this task; the parent-context
   disqualifier was over-applied to block all dispatch.
   Orchestrator miss: Mode 1 was chosen to be lean; copy-paste was the
   opposite. Lawful fallback is not the same as the lowest-friction
   authorized delivery.

2. **Who writes `01_report_00.md` (AP rule vs Cooperator expectation).**
   `PROMPT_CONTRACTS.md` Cooperator Delivery record: "The Worker does not
   archive the current pair." RF-02/RF-19: Orchestrator archives after the
   report exists; Worker is forbidden from self-granting trace writes.
   This prompt restated that ban explicitly. So the Worker following the
   grant must not save the companion. Combined with copy-paste delivery,
   the Cooperator became both courier and archivist. He then archived the
   prompt. AP has no check that the companion is a report rather than the
   prompt. Detection surface: Cooperator labor + silent wrong file.

3. **Emoji (consumer overlay gap + same detectability class as ADR-0021).**
   Emoji is not an AP field (AP.md §19; INTUITION.md §7; INTEGRATION.md
   optional presentation profile, inactive by default). Emission is
   required only when project rules activate a Cooperator presentation
   profile (RF-02). FrameNest `AGENTS.md` outside the managed block
   declares the upgrade ledger and product overlay, not a presentation
   profile or emoji set. INTUITION.md is reference-on-demand, not on the
   ORCHESTRATOR spine. Spine-following therefore emits none. This is the
   motivating ADR-0021 case (signaling dropped because it had no detection
   surface) now happening at the consumer overlay: AP moved marks out;
   FrameNest did not declare them back in.

These are field observations / upgrade-ledger candidates, not catastrophe.
`ap doctor` still PASS; pin remains operational.

### Check tracking update

| Check | Status | Note |
|---|---|---|
| 5 Prompt issued with coordinates + WORKER spine | held | `01_implementation_00.md` |
| 6 Report header + three coordinates | not scorable from archive | companion is the prompt; need the actual Worker terminal text |
| 7 Notes Worker-claim review | this entry | review of claims is blocked on missing report; git mutation reviewed as subordinate evidence |

No impersonation of the missing Worker report. No silent rewrite of
`01_report_00.md`. No new ledger entry added (would need a grant).

Open: Cooperator supplies the actual Worker terminal report, or the
Orchestrator cannot complete check 6.

---

## 2026-08-28 — Worker-claim review (session 01 / exchange 01)

Cooperator pointed this session at the corrected
`01_report_00.md` (now 23 lines; no longer identical to the prompt).

### Report shape (check 6)

File begins exactly `### Report for ORCHESTRATOR_CHAT`. Echoes once:

```text
Logical whole identity: framenest-ap-field-test
Worker session ordinal: 01
Worker exchange ordinal: 01
```

Status `PASS`; `implementation-PASS`; justification `new-mutation`;
`Logical-whole closure: not-closed`; authority-expiry stated. Compact core
present. Check 6: **held**.

### Claims vs repository (Orchestrator-verified)

| Claim | Class | Verdict |
|---|---|---|
| Start `d0ea8c8…` / end `85028f7…` | git | match `HEAD` / `HEAD^` |
| Only `docs/AP_UPGRADE_OBSERVATIONS.md` | git show --stat | match (6 lines, 3 fields) |
| Entry `accepted`, still `non-authorizing`, `Last revalidated against: 86ae6e8c…`, grant none, `retain-active` | file | match |
| Porcelain empty; `ap doctor` PASS; pin `86ae6e8c…` | this session | match |
| No push | branch still ahead of origin | consistent |
| `.ap/ap` resolves `runtime.cpython.executable` relative to `--root`; fail text at lines 857–859 | Orchestrator read of `.ap/ap` | corroborates source claim |
| Isolated-worktree `runtime-info` failed with that exact error | worker-observed | not re-run here; accepted as corroboration of the source path, not independent runtime evidence |

Disposition `accepted` is the lawful RF-09 transition for “miss still
exists at the pin”. Entry remains non-authorizing. No product-code or `.ap`
mutation. No catastrophe.

### Field-test score (Mode 1)

PASS criterion is checks **2, 3, 4, 6, 7**.

| Check | Score | Caveat |
|---|---|---|
| 1 Standard resume seed | partial | rich `00_handout.md`, not the minimal seed |
| 2 Spine reading list | hold | demonstrated in this Orchestrator chat; rich-handout weakness |
| 3 Stage 2 one whole + select | hold as behavior | predecessor already selected; not discovery |
| 4 `00_notes.md` at open | hold | |
| 5 Worker prompt + WORKER spine | hold | copy-paste delivery; dispatch observation recorded above |
| 6 Report header + coordinates | hold | after Cooperator replaced the prompt-duplicate companion |
| 7 Dated Worker-claim review | hold | this entry |
| 8 | **PASS** | observations (dispatch default, Worker-must-not-archive, emoji overlay) are ledger candidates, not score failures |

Recommended closure: Cooperator `PASS` / `close` this whole. Pin stays
local. Accepted ledger entry carries forward (`retain-active`). Era-10
handout after that decision.

No FrameNest/AP/Meta Git writes in this notes update. No impersonation:
the report text is the Cooperator-corrected file, not reconstructed.

---

## 2026-08-28 — Closure and successor selection

Cooperator directed closure of this whole and the next kebab. Verbatim
intent (Slovak, 2026-08-28): Agent Orchestrator should create subagents
unless he explicitly says otherwise; when he wants another model he is the
messenger; pin-time `AGENTS.md` should integrate that; generate exhaustive
findings (emoji unused + subagent problem); expert Worker prompt; static
closure; maximum fresh Orchestrator prompt; prevent recurrence; check
wrong-pin / unpushed-AP; use `PROMPT_ENGINEERING_PATTERNS.md`.

Orchestrator actions this entry: `02_field_observations.md`,
`02_closure.md` CLOSED: PASS; successor first staged under FrameNest `10/`
then relocated the same day to `meta/projects/ap/07/` (Cooperator: AP
protocol work belongs in the AP meta tree). Wrong-pin hypothesis rejected
(public main = pin = local ap HEAD `86ae6e8c…`).

This notes file froze at first close; the following entry is a same-day
amendment.

---

## 2026-08-28 — Successor relocated to `meta/projects/ap/07`

Cooperator: if this whole fixes AP protocol, handout and planning should
be under `meta/projects/ap/07`; if it were dual AP+FrameNest product, keep
FrameNest 10.

Orchestrator: mutation owner is `cisarik/ap`; FrameNest overlay is a later
pin-adoption. Live files:

```text
/home/agile/meta/projects/ap/07/00-ap-default-agent-dispatch-and-pin-presentation/00_handout.md
/home/agile/meta/projects/ap/07/00-ap-default-agent-dispatch-and-pin-presentation/01_planning_00.md
```

FrameNest `10/` deleted 2026-08-28 after Cooperator confirmation. Dispatch
payload rule added: verbatim prompt only, no parent wrap. Planning
implementation-in-same-session set to prohibited (era-06 posture).
