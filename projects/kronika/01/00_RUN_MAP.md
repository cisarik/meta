# Kronika run 01 — Run Map

```text
Run map author: Master Orchestrator, AP run 10
Mechanical persister: Fresh Implementation Worker session 07
Created: 2026-11-08
Observed against: AP d7023cf; Kronika 246c9f8; .ap d7023cf
```

The run is open. This run map is discovery and decision support only. It is not a roadmap,
selection, plan, grant or second semantic owner. Kronika's `ROADMAP.md`,
accepted ADRs and the COOPERATOR's decisions keep their owners. The COOPERATOR
may reorder, add or drop entries at any time; the order below is a
recommendation, never a selection. AP owns the meaning
(`.ap/AP.md#run-level-handouts`) and the record spelling
(`.ap/PROMPT_CONTRACTS.md#run-map-record`); the Meta `README.md` section Run
Maps and Provisional Handouts owns only this file's location.

```text
Run map: kronika-run-01
Run objective: after the closed UX refresh, deliver the bounded household-product improvements proposed in the closed 00 handout §9.2, one Cooperator-selected logical whole at a time; exclusions: Gallery/Details visual redesign (frozen), internet publication, new provider or acquisition pipelines, identity or authorization model changes, deployment beyond the routine release helper, and the parked roadmap rows
Run map authority: discovery-only
Run entry: 00 | ux-refresh-acceptance-and-promotion | closed | depends on: none | handout: /Users/agile/meta/projects/kronika/01/00-ux-refresh-acceptance-and-promotion/00_handout.md | evidence: Closed-by-ORCHESTRATOR on 2026-11-08 with Cooperator-declared production acceptance at 7ee4684 after E3 acceptance-PASS at cb5fa4d, per the closure record in that whole's 00_notes.md.
Run entry: 01 | timeline-and-history-media-thumbnails | provisional | depends on: ux-refresh-acceptance-and-promotion | handout: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/00_handout.md | evidence: The accepted in-process GalleryPreviewBackfillCoordinator and the existing gallery-preview route make previews available, and docs/UX_AUDIT.md lists Timeline/History thumbnails as an unimplemented recommendation.
Run entry: 02 | upload-flow-polish | provisional | depends on: timeline-and-history-media-thumbnails | handout: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/00_handout.md | evidence: Proposed in the closed 00 handout §9.2 as optional automatic start after file choice with duplicate review preserved and companion-visible progress, with risk U6 recording a UI-context dependency on whole 01.
Run entry: 03 | companion-download-notifications | provisional | depends on: upload-flow-polish | handout: /Users/agile/meta/projects/kronika/01/03-companion-download-notifications/00_handout.md | evidence: Proposed in the closed 00 handout §9.2 to surface completed X/YouTube downloads in the companion side-panel history and toolbar badge, reusing the existing own-history and request-detail read paths.
Run entry: 04 | household-onboarding | provisional | depends on: companion-download-notifications | handout: /Users/agile/meta/projects/kronika/01/04-household-onboarding/00_handout.md | evidence: Proposed in the closed 00 handout §9.2 as a first-run explainer of roles, privacy and sharing for ordinary members plus a plain-language install guide, without changing the identity or authorization model.
Run entry: 05 | humanized-error-copy | provisional | depends on: household-onboarding | handout: /Users/agile/meta/projects/kronika/01/05-humanized-error-copy/00_handout.md | evidence: Proposed in the closed 00 handout §9.2 to replace raw user-facing codes such as http_403 with actionable text after an inventory, keeping machine codes for diagnostics.
Run entry: 06 | accessibility-pass | provisional | depends on: humanized-error-copy | handout: /Users/agile/meta/projects/kronika/01/06-accessibility-pass/00_handout.md | evidence: Proposed in the closed 00 handout §9.2 for keyboard paths, focus, screen-reader names and glass-button contrast, with the Cooperator's rendered review as acceptance and the Gallery/Details freeze respected.
Run entry: 07 | app-js-modularization-planning | provisional | depends on: accessibility-pass | handout: /Users/agile/meta/projects/kronika/01/07-app-js-modularization-planning/00_handout.md | evidence: Proposed in the closed 00 handout §9.2 as planning only for the app.js monolith (predecessor residual R9), requiring an asset-allowlist decision and a vm-harness test strategy before any implementation.
Run entry: 08 | product-language-decision | provisional | depends on: app-js-modularization-planning | handout: /Users/agile/meta/projects/kronika/01/08-product-language-decision/00_handout.md | evidence: Proposed in the closed 00 handout §9.2 as a Cooperator product decision on UI language (the UI is English and the Cooperator communicates in Slovak), discovery and decision only.
```

## Notes on the record

**Run objective provenance.** This refresh derived the objective and
exclusions from the closed 00 handout §9.2, which lists the eight candidates as
"proposals, not adopted direction", and from the eight provisional handouts'
scope and out-of-scope lists. The parked roadmap rows are the S3 host
remainder, capture-mode Search and Research, S5 ZIP activation and S7-C capture
integration (`AGENTS.md`). The evidence available to this refresh records no
Cooperator-selected run objective. The COOPERATOR confirms, narrows or replaces
it before the run map informs a recommendation.

**Dependencies.** Entry 01 builds on the closed 00 whole's accepted preview
backfill. Entry 02 depends on 01 through the recorded UI-context risk U6.
Entries 03–08 preserve each handout's stated predecessor-wait rule (the
predecessor closes before the whole opens); that rule records the prepared
order, not a measured product dependency. The COOPERATOR selects the final
order. A reorder refreshes the affected unopened handouts' predecessor lines or
replaces them with successor handouts.

**Status vocabulary.** A run entry's status is one of `provisional`,
`handed-off`, `active`, `closed`, `superseded` or `dropped`
(`.ap/PROMPT_CONTRACTS.md#run-map-record`). Only the run-scoped Orchestrator
changes a status, from the whole's own selection, revalidation and closure
evidence; closure remains that whole's Orchestrator decision.

**Handouts.** Entries 01–08 point to provisional handouts refreshed on
2026-11-08 against AP `d7023cf`, Kronika `246c9f8` and `.ap` `d7023cf`. Each is
a seed, not authority; its receiving Orchestrator records a Handout
Revalidation Record in that whole's `00_notes.md` before the first Planner
prompt. Entry 00's handout is frozen historical evidence.

**Relationship to AP run 10.** These entries are Kronika wholes. They are not
wholes of AP run 10, whose only whole is
`master-orchestrator-and-report-persistence`.
