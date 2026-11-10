# Kronika — Fresh Orchestrator Handoff

```text
Restoration classification: PARTIAL
Handout status: provisional
Capability profile: Orchestrator
Initialization signal: You are a fresh Orchestrator instance assigned to the ORCHESTRATOR role for the Kronika project.
Orchestrator session scope: logical-whole
Development run identity: kronika-run-01
Current phase: Restoration (Continuation Bootstrap Stage 1 not yet performed)
Reasoning recommendation: selecting a Worker is premature
Restoration date: 2026-11-10
Refreshed: 2026-11-10
Refreshed against: AP d7023cf; Kronika e6b26eb; .ap d7023cf
Handout author: the run-scoped Orchestrator of Kronika run 01 (this session)
Original handout author: not-applicable (new whole)
Mechanical persister: the same run-scoped Orchestrator
Predecessor wholes: 01-timeline-and-history-media-thumbnails (closed 2026-11-10 at e6b26eb); 09-timeline-complete-chronicle (closed 2026-11-10 at 65772c6)
Run map: /Users/agile/meta/projects/kronika/01/00_RUN_MAP.md
Handout destination: /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/
Restoration grants mutation authority: no
```

This prompt transfers information, never authority. It is a **provisional
seed** for the final application-shell UI/UX consistency whole. The receiving
per-whole Orchestrator revalidates it in Continuation Bootstrap Stage 1 and
records a Handout Revalidation Record before the first Planner prompt.

The COOPERATOR is **Michal**. Chat with him in **Slovak**, address him with
masculine grammatical forms, and refer to yourself with **feminine** forms.
Worker prompts, Worker reports, repository documentation, and Meta artifacts are
professional **English**.

---

## 0. Cooperator operating preferences

```text
No subagents. The Orchestrator prepares prompts and reconciliation itself.
Meta is the prompt/report archive; write exact prompts, reports, notes, handouts
  and run-map updates there.
Manual Worker delivery. The COOPERATOR sends every Worker prompt manually.
Direct-write Worker reports. Workers write terminal reports to the exact Meta
  path and read them back; the COOPERATOR never copy-pastes report content.
Meta Git belongs to the COOPERATOR. Do not commit or push Meta.
Repository and NUC work stay under the exact current Worker grant.
```

---

## 1. Current state

```text
Repository: https://github.com/cisarik/kronika (main)
Local checkout: /Users/agile/Projects/kronika
Public main / NUC: e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd
AP pin: d7023cf037f6d17885c3ede5c04812c61640da50
Database revision: 0035
Backup restore readiness: ready
NUC sudo timestamp: revoked after the e6b26eb deployment
```

Closed whole 01 delivered the History Questions-only correction at `e6b26eb`.
Closed whole 09 delivered the complete Timeline chronicle and its UI polish at
`65772c6`. The deferred `upload-flow-polish` whole remains prepared and waits
until this UI/UX consistency whole finishes, unless the Cooperator reorders.

---

## 2. Cooperator's requested UI/UX consistency changes

The Cooperator tested the deployed `e6b26eb` and asked for one final
application-shell consistency pass:

1. **Unify Timeline search with Gallery search.** Timeline currently has a plain
   input plus Search/Clear buttons; Gallery has the established icon-led search
   field with a green border and "Search titles and tags" placeholder. The
   Timeline search should look and behave like the Gallery search, not like a
   second control family.
2. **Separate browsing from actions.** Timeline, Gallery and History are
   browsing tabs. Search, Research and Review are actions. Move the three action
   entries into a right-aligned action group under the top-right shell buttons;
   they should not look like rounded browsing tabs. Use square/unrounded action
   styling and preserve route/capability behavior.
3. **Remove table-link underlines.** The Timeline and History chronicle row title
   links show an underline, including on hover. Remove it; keep the row hover
   and focus affordance.
4. **Reorder and align Timeline filters.** Publication should be the first filter
   on the left and visually distinguished with the green border language used by
   the tabs. Kind, Status and Visibility should align to the right, matching the
   table columns. Search should follow the Gallery search treatment.
5. **Fix the visibility glyph.** In the Timeline visibility cell, `🕰️` for
   legacy publication does not communicate "public"; use an eye-style glyph for
   public/legacy visibility. Keep `🔒` for private. Preserve household/withdrawn
   glyphs where they still make sense, and keep accessible text.
6. **Keep the result eye-candy and consistent** with the current dark green
   design, responsive at 320/390 px, keyboard accessible, 44 px targets, no
   layout shift, and no behavior, API, privacy or data change.

---

## 3. Scope shape (for the Planner, not a grant)

Likely in scope:

- shell navigation markup, grouping and responsive styling for browsing vs
  action entries;
- a shared Gallery/Timeline search field treatment and its existing behavior;
- Timeline filter order, alignment, publication emphasis and the matching
  responsive layout;
- Timeline/History row link decoration and hover/focus;
- the visibility/publication glyph mapping and accessible text;
- Node and local-web tests for the changed markup, CSS and behavior;
- the exact durable documentation sentence(s) that own the changed UI.

Likely out of scope:

- any API, repository, authorization, schema, migration, payload or data change;
- reopening the closed Timeline/History data models or the Gallery/Details
  freeze;
- a new search backend, saved search, filters or query semantics;
- companion, upload, provider, deployment or host changes;
- the deferred `upload-flow-polish` product whole.

---

## 4. Questions the Planner must answer

1. Where exactly are the shell navigation, the Gallery search field, the
   Timeline search/filter bar, the chronicle row links and the glyph mapping
   implemented? Name the functions, elements, classes and tests.
2. What is the smallest shared component/markup treatment that makes the Timeline
   search identical to Gallery without duplicating behavior or creating a second
   semantic owner?
3. How should browsing tabs and action entries be grouped in the DOM and CSS so
   the action group is right-aligned under the top-right controls, is square,
   responsive and keyboard accessible? Which existing route/capability checks
   must remain?
4. What is the exact desktop and narrow layout for the new filter order
   Publication / Kind / Status / Visibility and the Gallery-style search? Which
   table columns do they align to?
5. How should link underlines be removed without changing row focus, hover,
   accessible names or History behavior?
6. What is the exact visibility/publication glyph and accessible-text matrix?
   Which existing glyphs stay, which change, and how is public/legacy represented?
7. Which tests pin the current nav, search, filters, links, glyphs and responsive
   rules? Which must change, and what new causal tests are needed?
8. Which durable documents own the new shell/search/filter presentation? Do not
   create a second semantic owner or reopen the closed data models.
9. What is the exact changed-path allowlist, validation commands and acceptance
   route? Recommend E2 plus Cooperator rendered acceptance while the change stays
   presentation-only; identify a fresh independent trigger if it does not.
10. What is the smallest coherent candidate and the exact publication/NUC
    rendered-acceptance sequence?

---

## 5. First actions for the fresh Orchestrator

1. Read `AGENTS.md`, the AP spine, this handout and the closed whole 01/09
   evidence.
2. Verify the repository, AP pin, public main/NUC `e6b26eb`, clean tree and the
   upgrade ledger.
3. Revalidate this handout and record the Handout Revalidation Record in this
   whole's `00_notes.md`.
4. Preserve the COOPERATOR's selected UI/UX consistency objective.
5. Prepare the first Planner prompt for session `01`, exchange `01`,
   `fresh-worker-session`, `Native planning mode: required`, manual delivery and
   direct-write report `01_report_00.md`; archive it as `01_planning_00.md`.
6. Do not dispatch, do not use a subagent, and do not commit Meta.
7. After the Planner report, reconcile it, obtain the Cooperator's plan decision,
   then proceed through a bounded implementation, acceptance, publication,
   NUC deployment and rendered acceptance.
8. Do not open the deferred `upload-flow-polish` whole until this one is closed
   or the Cooperator reorders.

The Meta directory is:

```text
/Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/
```

---

## 6. Readiness review

| Review | Result |
|---|---|
| Contradiction | No contradiction with the closed 01/09 state; the change is presentation-only |
| Omission | Exact selectors, layout, tests and docs are for the Planner |
| Stale state | Repository/NUC observed at e6b26eb; revalidate |
| Authority | No mutation authority transferred; every Worker action needs a new complete prompt delivered manually |
| Active mutation | None |
| Active Worker | None for this whole |
| Security boundary | No API, privacy, authorization or data change |
| Strategic direction | Gallery/Details freeze, Timeline/History behavior and closed wholes remain |
| Next-step executability | Executable after Stage 1, the Handout Revalidation Record and the first Planner prompt |

Overall: **PARTIAL** — the direction is clear and the predecessor state is
known, but the exact shell/search/filter implementation plan is not written and
the whole has not opened. This is a prepared seed, not current-state authority.

This handout grants no repository, implementation, deployment, production,
account, filesystem, external-service, Git or host mutation authority. Verify
independently, then prepare the first Planner prompt for the COOPERATOR's manual
delivery.
