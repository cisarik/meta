# Kronika whole 02 — upload-flow-polish

## Opening and Handout Revalidation — 2026-11-10

The COOPERATOR selected `upload-flow-polish` on 2026-11-09 and deferred it until
the preceding UI/UX wholes closed. Whole 01 closed at `e6b26eb`, whole 09 closed
at `65772c6` and whole 10 closed at `8646146` after the Cooperator's final
rendered PASS. The deferral condition is satisfied; this whole opens as a new
logical whole with an independent planning cycle.

```text
Handout revalidation: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/00_handout.md
Received handout status: provisional
Revalidated against: Kronika 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e; AP d7023cf037f6d17885c3ede5c04812c61640da50; NUC active/web 8646146; run map entries 01, 09 and 10 closed; ADR-0088
Usable facts: repository URL and canonical checkout; the Cooperator's selection of upload-flow-polish; the polish objective, likely scope, out-of-scope exclusions and nine planning questions; the manual-delivery, direct-write-report, no-subagent and Meta-Git operating rules; the repository/NUC security boundaries; the upgrade-ledger path; the first Planner coordinates; the whole's Meta directory
Stale facts and corrections: last observed repository HEAD b66ec8f -> 8646146; public main b66ec8f -> 8646146; NUC active/web b66ec8f -> 8646146 with capture 5b86d896b3ea03f89fef2c90f7af2c121d0ef915 and database revision 0035; predecessor whole 01 formal closure pending -> closed at e6b26eb with Cooperator-declared production acceptance; whole 02 deferred until after entry 10 -> entry 10 closed at 8646146; run-map entry 01 active and entry 02 handed-off -> entries 01, 09 and 10 closed and entry 02 active; ADR-0083 separate personal History view -> superseded by ADR-0088 Timeline-as-single-overview, no separate History view; whole 01 preview change as the latest shell context -> whole 10 additionally changed header search, navigation, Timeline filters and chronicle presentation
Not revalidated: none
Handout disposition: adopted-with-corrections
```

The handout remains historical seed evidence; this record is the current
revalidation and does not edit the handout. The Planner must read both and
re-measure the upload flow, companion bridge, shell, tests and documentation
rather than trusting either artifact.

## Stage 1 evidence — 2026-11-10

```text
Repository: https://github.com/cisarik/kronika
Local checkout: /Users/agile/Projects/kronika
HEAD and public main: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
Branch: main; working tree clean
AP pin: d7023cf037f6d17885c3ede5c04812c61640da50 (.ap gitlink, submodule HEAD and governing stable variant)
ap doctor: PASS
ap project check --baseline 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e: PASS
NUC: layout canonical; active/web 8646146; capture 5b86d896b3ea03f89fef2c90f7af2c121d0ef915; service active; database revision 0035; backup restore-readiness ready; sudo timestamp revoked after deployment
Upgrade ledger: docs/AP_UPGRADE_OBSERVATIONS.md valid; one active entry consumer-declared-execution-and-capability-route-binding remains accepted, non-authorizing, retain-active; no ledger mutation
```

The NUC facts were observed through the canonical release helper during the
whole 10 deployment. The sudo timestamp was then revoked with `sudo -K`; a later
deployment needs a fresh Cooperator authorization. No repository, Git, NUC,
browser, provider, secret or host mutation was performed during this
revalidation.

## Current product context the Planner must preserve

- ADR-0088 is current: the Timeline is the single authorized overview; the
  separate History view is removed; question and answer APIs remain; Gallery and
  Details remain separate.
- Whole 10's final shell is at `8646146`: header-slot Timeline/Gallery search,
  Publishing-first Timeline filters, no visible Timeline hero/lede/note,
  request/record routes keep Timeline current, and the chronicle/listbox/glyph
  behavior is accepted.
- ADR-0086 owns the companion `open_upload` message and the hosted upload
  dialog; the extension side panel's upload control posts it only after the
  sidebar handshake.
- The upload security boundary remains: `upload.submit` for ordinary users,
  `upload.manage` for administrators, quarantine before validation, exact
  duplicate disposition, no publication without the existing approval
  semantics, no public upload service.

## Next step

Prepare the first Planner prompt for Worker session `01`, exchange `01`,
`fresh-worker-session`, `Native planning mode: required`, `Planning cycle:
initial`, `Plan disposition: approval-gated`, implementation prohibited in the
same session and a fresh post-plan implementation session. The prompt is
`01_planning_00.md`; the terminal report is `01_report_00.md`. The Cooperator
delivers it manually.

## Planner report reconciliation — 2026-11-10

`01_report_00.md` is present and was read back in full. The Planner reported
`Status: PARTIAL` solely because the active client Plan Mode prohibited the
report write; the exact report is now persisted at the intended path and read
back, so the persistence limitation is resolved. The plan result is
`planning-PASS`; the design is decision-complete.

The plan recommends:

- one opt-in checkbox, **“Start automatically after choosing a file”**, off by
  default, retained only for one open dialog and reset on dialog reopen; never
  persisted;
- auto-start invokes the existing capability-gated start handler once and
  preserves duplicate review (administrator keep/discard, ordinary silent
  keep-separate), quarantine, validation, publication semantics and the
  existing recovery/cancel/pause/resume model;
- companion progress and terminal results remain inside the existing hosted
  upload dialog; no new message type, panel indicator or protocol change;
- closing two source-observed gaps: selection must not replace an in-flight
  create or unresolved recovery, and a server-confirmed full `receiving` offset
  must offer a reachable Resume that completes without PATCH;
- no API, payload, authorization, schema, migration or companion-protocol
  change;
- nine proposed changed paths: `index.html`, `app.js`, `styles.css`,
  `tests/upload_cockpit_async_ownership.test.js`,
  `tests/companion_web_bridge.test.js`,
  `tests/contract/test_local_web_application.py`, `SPEC.md`, `DEVELOPMENT.md`
  and `docs/X_COMPANION.md`;
- `SPEC.md` §18 as the sole normative owner; `DEVELOPMENT.md` and
  `docs/X_COMPANION.md` updated; `SECURITY.md` unchanged; no new ADR;
  ADR-0086, ADR-0088 and the Gallery/Details freeze preserved;
- no open product decisions; recommended implementation reasoning High, one
  fresh independent E2 acceptance, then publication, routine NUC refresh and
  Cooperator rendered acceptance.

The Orchestrator spot-checked the material claims: the baseline, public `main`
and AP pin are unchanged; all nine proposed paths and all selected Python/Node
test files exist; the upload routes use `upload.submit`; the companion `#frame`
hosts the shell and the sidebar posts `open_upload`; no auto-start markup exists
today. The plan is consistent with current source. No repository, Git, NUC,
browser, provider or host mutation occurred.

Plan status: **reconciled and submitted for Cooperator approval**; not yet
accepted and not yet implementation authority. The two product choices in the
plan — per-dialog default-off auto-start and companion progress inside the
existing dialog — are part of the approval request.

## Plan approval — 2026-11-10

The COOPERATOR approved the reconciled plan as-is and confirmed both product
choices:

1. auto-start is **off by default**, retained only for one open upload dialog
   and reset on dialog reopen; it is not persisted;
2. companion progress and terminal results remain inside the existing hosted
   upload dialog; no persistent panel indicator or new companion message type is
   required.

The plan report `01_report_00.md` is the design of record. The approved scope is
the nine-path UI/test/documentation slice, with no API, payload, authorization,
schema, migration, extension-production or companion-protocol change.

Implementation prompt `02_implementation_00.md` is prepared for a genuinely
fresh Worker session `02`, exchange `01`, `fresh-worker-session`, `Native
planning mode: not-used`, explicit implementation authority, baseline
`8646146`, the exact nine-path allowlist and report `02_report_00.md`. The
Cooperator delivers it manually. Implementation, acceptance, publication,
deployment and rendered acceptance remain pending.

## Implementation delivery mismatch — 2026-11-10

The file `02_report_00.md` is byte-identical to `01_report_00.md` (SHA-256
`42d28851c7236d17bd8a3297dbd04a96dd940190bd44a515f0b167dbf87a9ef3`) and
carries the Planner's session 01 / Planning coordinates, not the implementation
session 02 coordinates. The repository is still at
`8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`; there is no implementation commit,
no worktree change and no new branch. The file is a misdelivered planning copy,
not a terminal implementation report, and is preserved unchanged as delivery
evidence.

The implementation session 02/01 coordinates are consumed. A corrected
implementation prompt `03_implementation_00.md` is prepared for a genuinely
fresh session `03`, exchange `01`, with baseline `8646146`, the same accepted
plan and nine-path allowlist, and report `03_report_00.md`. The prior report path
`02_report_00.md` must not be overwritten. Implementation, acceptance,
publication, deployment and rendered acceptance remain pending.
