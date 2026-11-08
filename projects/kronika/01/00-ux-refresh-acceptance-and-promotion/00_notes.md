# Era 01 Whole Notes — Kronika UX refresh, acceptance, and documentation promotion

Classification: private local historical/evidentiary projection for this
logical whole. Orchestrator-owned, append-only during the whole, frozen at
closure. Public-safe by default. Michal owns any meta Git commit.

Working identity:

```text
ux-refresh-acceptance-and-promotion
```

Trace:

```text
/Users/agile/meta/projects/kronika/01/00-ux-refresh-acceptance-and-promotion/
```

Opening handout: `00_handout.md` (identical to the local workstation copy saved
as `ORCHESTRATOR_RESTORATION_2026-11-07_ux-refresh.md`). No Worker has been
dispatched. The next Worker session ordinal is 01. The first exchange, when
issued, is stored as `01_planning_00.md` with report destination
`01_report_00.md` in the same directory.

Opening date: 2026-11-07. Opening Orchestrator: fresh instance, continuation of
a PARTIAL restoration produced outside the repository by a direct-action coding
agent for the Cooperator.

Predecessor whole: `00/03-kronika-sole-identity` (closed 2026-10-02). Its
closure signal was emitted in the Orchestrator chat; do not emit it again.

## Objective

Close the evidence and documentation gaps of the last Kronika session before
building on top of it:

1. Map the exact acceptance claims and control matrix for commits
   `8cbbcad..cb5fa4d`, i.e. the icon-first web shell + companion refactor, the
   dialog-icon `MutationObserver`, the YouTube save flow, the preview
   backfill coordinator, and the ingress `companion_mutation=True` change on
   `POST /api/youtube/requests`.
2. Author a fresh independent audit (E3) of the security-boundary change and the
   other new surfaces, per AGENTS § Security Boundaries and INFOSEC routing.
3. Accept or correct based on findings, scoped or full-fresh.
4. Promote durable truth: ADR, README, SPEC, SECURITY, GALLERY, DEVELOPMENT,
   `kronika.env.example`, and give `docs/UX_AUDIT.md` a lifecycle + inbound
   link (RF-14).
5. Publish the accepted commit, refresh the NUC to it via
   `deploy/ubuntu/kronika-release`, then obtain Cooperator rendered acceptance
   on the NUC.

## Continuity facts verified at opening

- Kronika `main` local HEAD equals public origin:
  `cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738`, tree clean.
- `.ap` gitlink and submodule HEAD:
  `73e20ef80b88700d5fcbc397cd8edd4fc425869f`; `./.ap/ap doctor` PASS (strict
  pin, clean submodule, managed block, governing variant `stable`).
- `./.ap/ap project check --baseline cb5fa4d...` PASS on the local macOS
  checkout (uv-supplied CPython 3.13.14, Poetry-owned `.venv`).
- Upgrade ledger `docs/AP_UPGRADE_OBSERVATIONS.md`: entry
  `consumer-declared-execution-and-capability-route-binding` in state
  `accepted`, `retain-active`; revalidated against AP commit
  `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`, which is an ancestor of the
  pinned `73e20ef` and still governs the consumer-declared route.
- NUC web release last-seen at `9318af471c51c24dbcd8244ab83bcbafb5c7f5c9`
  (`layout: canonical`, `service_active: active`, `database_revision: 0035`,
  `backup_restore_readiness: ready`); capture release
  `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`.
- NUC sudo timestamp: active. Michal ran `sudo -v` for this session. The
  lifecycle stays — Cooperator `sudo -v` outside the Worker, Worker ends with
  `sudo -K`.
- `docs/UX_AUDIT.md` has no inbound link from any other document.
- Delta `9318af4..cb5fa4d` is extension-only (`service_worker.js`, one contract
  test); server code identical. Delta `8cbbcad..9318af4` covers web shell,
  companion, ingress, configuration, backfill coordinator, and tests.
- One verification side effect: the end-to-end test acquired a public 19-second
  YouTube video (`jNQXAC9IVRw`, "Me at the zoo") as a requester-private
  download for Michal's identity. To be decided: keep or remove via the
  administrator removal workflow.

## Session log

- **2026-11-07 — Whole opened.** Meta directory created and `00_notes.md`
  written. Opening handout present. No Worker prompt issued. No repository, Git,
  NUC, browser or filesystem mutation.
- **2026-11-07 — Continuation Bootstrap Stage 1 (read-only) complete.**
  Repository, AP pin, `ap doctor`, `ap project check`, upgrade ledger, and NUC
  `kronika-release status` verified. One decision outstanding: selection of
  this whole's first Worker exchange and delivery route.
- **2026-11-07 — Planner prompt issued and stored.** Worker session `01`,
  exchange `01`, profile Planner, `fresh-worker-session`, `Native planning mode:
  required`, plan-only, `approval-gated`, one cycle, E2 evidence tier for the
  claims mapping (security boundary routed separately to E3 with a fresh
  independent Worker), INFOSEC activation (R3 route for the companion YouTube
  ingress change). Stored as `01_planning_00.md`; report destination
  `01_report_00.md`. The prompt sets read-only authority only and maps ten
  acceptance claim families, the documentation-promotion inventory with exact
  files, and the NUC refresh gate ordering. Reasoning recommended at `High`,
  named risk: ingress security-boundary change without prior acceptance. The
  prompt declares Meta trace disposition `configured` with the activated
  destination and `Archival: wait-for-report`.
- **2026-11-07 — Delivery route selection requested.** Per AP §3
  (Instances, Sessions, and Worker Session Profiles), I must select the
  subsequent delivery route around the first Planner and preserve it. Route
  selection is pending: direct session dispatch (default for this Agent
  Orchestrator with functioning dispatch) or manual copy-paste (Cooperator
  opt-out / P14 model rotation).

## Next step

Await the Cooperator's delivery-route decision, then dispatch the Planner
(`01_planning_00.md`) and wait for the terminal planning report
(`01_report_00.md`).
