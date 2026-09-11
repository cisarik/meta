# meta

Historical evidence archive for project development traces.

`cisarik/meta` is evidence and history, not task authority, protocol authority,
a roadmap, or a replacement for canonical project repositories.

## Layout

Project traces live under:

`projects/<project>/<archive-sequence>/<logical-whole-sequence>-<logical-whole-identity>/`

Both sequence components are two-digit ordering keys.

`<archive-sequence>` is an archive-ordering group. It does not encode a
calendar date and does not require daily rollover.

`<logical-whole-sequence>` orders logical wholes inside that archive group.

A logical whole keeps one directory for its full lifecycle even when the work
spans multiple calendar days. Dates and timestamps are recovered from Git and
file metadata rather than directory names.

Worker prompt/report filenames inside a logical whole use this Meta-local
storage contract:

    <worker-session>_<phase>_<meta-exchange-index>.md
    <worker-session>_report_<meta-exchange-index>.md

`<worker-session>` remains the one-based, two-digit AP Worker-session ordinal.
`<meta-exchange-index>` is a Meta-local, zero-based, two-digit storage index.
The filename suffix is not itself the AP Worker-exchange ordinal:

    meta_exchange_index = Worker exchange ordinal - 1

Every completed exchange has exactly one prompt and one matching report with
the same session ordinal and Meta exchange index. Phase changes do not reset
either coordinate. Examples:

| AP session / exchange | Meta prompt | Meta report |
|---|---|---|
| 01 / 01 | `01_planning_00.md` | `01_report_00.md` |
| 01 / 02 | `01_implementation_01.md` | `01_report_01.md` |
| 02 / 01 | `02_acceptance_00.md` | `02_report_00.md` |

Phase labels include `planning`, `implementation`, `correction`, `acceptance`,
`audit`, `diagnostic`, `publication`, and justified completion or `re-*` labels.
A label does not renew authority or reset AP's finite revision/correction budget.
If the governing AP permits an interruption instead of a report, its local name
is `<worker-session>_interruption_<meta-exchange-index>.md`; it does not occupy a
report filename. Companion identity and authorized authorship belong to AP RF-19.

## Notes, Handouts, and Closure

New logical wholes using this activated AP/Meta convention open with
`00_notes.md`; an opening `00_handout.md` is optional. Notes semantics belong to
governing AP §13:
Orchestrator-authored entries (including selected delivery and reconciliation)
may be stored exactly by a named authorized persister, retained through the whole,
and frozen at closure.

Later `xx_handout.md` and `xx_closure.md` share a **handoff/closure artifact
sequence**, separate from Worker-session numbering. The next prefix is one
higher than the largest prefix already used by a handout or closure in this
whole, treating the opening position as `00` when none exists. Worker prompt,
report, and interruption prefixes do not participate. A handout or closure never
consumes a Worker-session ordinal. For example, after `00_handout.md`,
`01_handout.md` and `02_closure.md` can coexist with Worker `01_report_01.md`.
Keep existing historical names and gaps; do not renumber or silently normalize
old profile-qualified handouts.

AP §14 owns handout authorship and continuity: an Orchestrator, an explicitly
assigned Worker, or the Cooperator may author one truthfully, while an assigned
Worker's handout remains separate from its standard report and notes remain
Orchestrator-authored. Apply that owner for predecessor relationships, retained
decisions/delivery, supersession, observation limits, active work, and readiness;
apply AP Continuation Bootstrap when restoring an already planned whole. The
filename identifies storage, not exclusive authorship, successor access profile,
reconciliation authority, or precedence over an earlier decision.

Detection of this local storage convention is **artifact-detectable** on names,
coordinate arithmetic, notes entries, handout/closure predecessors, and Git
first-add evidence. Universal semantics and lifecycle obligations remain in AP.

Prompt and report contents remain exact historical evidence. Path
normalization does not rewrite them. Old literal path references inside
historical artifacts are preserved as historical text.

Meta naming is storage and discovery policy only. It grants no task, AP,
project, acceptance, publication, deployment, production, or closure
authority. Exact file preparation under a named grant is distinct from Git
archival: a new prompt/report pair is first added together in one commit only
after the report exists. The configured delivery record and positive grant name
prompt/report persisters and Git ownership; in ChatOrchestrator workflows Meta
Git operations belong to the Cooperator. Historical first-add mismatches remain
history and require explicit prospective reconciliation, not silent rewriting.

## Authority

Meta stores selective historical evidence only. Current task authority comes
from the current authoritative prompt; protocol meaning comes from the
governing immutable AP; project truth comes from canonical project and external
evidence.

Repository layout is Meta-local implementation policy and must not be promoted
to universal AP semantics merely because Meta is an AP trace implementation.
