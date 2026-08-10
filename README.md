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

Worker prompt/report filenames inside a logical whole follow the governing AP
pin and the trace grammar applicable when those artifacts were created.

Historical prompt and report contents are not rewritten merely to modernize
old path references or make earlier artifacts look as though they were created
under a later layout.

## Authority

Meta stores selective historical evidence only. Current task authority comes
from the current authoritative prompt; protocol meaning comes from the
governing immutable AP; project truth comes from canonical project and external
evidence.

Repository layout is Meta-local implementation policy and must not be promoted
to universal AP semantics merely because Meta is an AP trace implementation.
