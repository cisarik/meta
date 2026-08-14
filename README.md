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
the same session ordinal and Meta exchange index. `00_handout.md` is reserved
for the Orchestrator handout and is not a Worker exchange.

Prompt and report contents remain exact historical evidence. Path
normalization does not rewrite them. Old literal path references inside
historical artifacts are preserved as historical text.

Meta naming is storage and discovery policy only. It grants no task, AP,
project, acceptance, publication, deployment, production, or closure
authority. Future prompt/report pairs are added only after the report exists.
This Meta-maintenance prompt and its report are not archived in Meta.

## Authority

Meta stores selective historical evidence only. Current task authority comes
from the current authoritative prompt; protocol meaning comes from the
governing immutable AP; project truth comes from canonical project and external
evidence.

Repository layout is Meta-local implementation policy and must not be promoted
to universal AP semantics merely because Meta is an AP trace implementation.
