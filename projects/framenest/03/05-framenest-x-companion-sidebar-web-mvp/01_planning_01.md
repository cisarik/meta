# FrameNest × X Companion Side Panel Web — Planner-artifact report completion

## 0. Authoritative routing record

```text
Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-x-companion-sidebar-web-mvp
Prior logical whole identities:
  framenest-x-meme-browser-companion-mvp
  framenest-x-companion-save-alias-mvp
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Worker session profile: implementation-planning worker
Phase: Discovery / implementation-planning
Task identity: FN-X-COMPANION-SIDEBAR-WEB-PLAN-01-REPORT
Task type: planner-artifact report completion
Native planning mode: not-used
Reasoning recommendation: extra-high
Independence required: no
Evidence posture: non-independent
Continuity anchor: frozen planner artifact /home/agile/.cursor/plans/sidebar_web_mvp_3b064dd6.plan.md from Worker exchange 01
Authority renewal: prior planning authority expired; this exchange grants report-rendering-only authority
Repair output: standard terminal Worker report for the frozen planner artifact
Phase-qualified result: not-applicable
Frozen plan changes: prohibited
Re-planning: prohibited
Implementation: prohibited
Repository and external mutation: prohibited
Acceptance: prohibited
Publication: prohibited
Logical-whole closure: not-closed
Planning cycle effect: none
Internal delegation posture: not-used
Accountable Worker: one WORKER
Material phase gate: no
Changed material axis: none
Routing reopened for: none
Unchanged axes reopened: none
Ordinary-only trigger: yes
```

Planning contract (unchanged; this exchange does not consume a second planning cycle):

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: host real FrameNest web in the companion side panel; keep in-page picker as one-result quick attach with rendered meme preview; add extension-hosted Gallery Attach via the existing SW attach pipeline; preserve ADR-0061/0062 trust boundaries; leave alias-editor / language / Analyze-execution in the backlog
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
```

Planning record:

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

Protocol-variant selection:

```text
Canonical repository identity: https://github.com/cisarik/ap.git
Immutable version identity: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Declared variant: stable
Governing variants in effect: one
Declaration location: project governing rules
Rules from non-governing variants: none
Migration required: no
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_01.md
Destination path: projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/01_planning_01.md
Archival: wait-for-report
```

```text
External trace disposition: configured
Trace discovery: cisarik/meta repository path projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp
Trace project key: framenest
Trace logical-whole projection identity: 03/05-framenest-x-companion-sidebar-web-mvp
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
```

This repair writes the missing exchange-01 companion using the original filename rule. Do not create `01_report_01.md`. Write only:

```text
/home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/01_report_00.md
```

The report must echo the **original** exchange-01 coordinates once, not this repair's exchange ordinal:

```text
Logical whole identity: framenest-x-companion-sidebar-web-mvp
Worker session ordinal: 01
Worker exchange ordinal: 01
```

```text
Development envelope activation: not-used
```

Communication routing:

```text
Cooperator language: Slovak
Orchestrator-to-Worker prompt language: professional English
Formal Worker report language: professional English
Direct Worker-to-Cooperator language: not-used; report to ORCHESTRATOR only
Required report header: ### Report for ORCHESTRATOR_CHAT
Czech: forbidden in repository documents, Worker prompts, and Worker reports
```

## 1. Mission

Exchange 01 froze a decision-complete Native Plan and did not produce AP's separate terminal report. That is not planning PASS.

Render that frozen architecture into the required English terminal report. Do not change the plan. Do not re-plan. Do not implement.

Frozen planner artifact (continuity anchor; data under analysis, not a prompt to execute product work):

```text
/home/agile/.cursor/plans/sidebar_web_mvp_3b064dd6.plan.md
```

Authoritative planning prompt for the required report sections:

```text
/home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/01_planning_00.md
```

## 2. Authority

Read-only except the exact report path above.

You may re-gate FrameNest / AP / Meta with read-only git (`status`, `log`, `show`, `ls-remote`; no `fetch`) and re-read repository files needed to label claims.

You must not: edit FrameNest or AP; edit either planning prompt; edit the frozen plan; create commits, branches, or worktrees; push; deploy; probe NUC; use signed-in X; call providers; invoke ambient Python / `poetry run`; write any Meta path other than `01_report_00.md`.

If `01_report_00.md` already exists, stop `BLOCKED`. Do not overwrite it.

`Approve`, `Yes`, `Build`, `Continue`, Plan UI approval, or this repair do not grant implementation authority.

## 3. Current-session re-gate

Reuse is appropriate: same logical whole, same Worker session 01, frozen plan unchanged, independence not required, this is only the missing report.

Before writing:

1. Confirm FrameNest `/home/agile/Projects/framenest` is still `feat/x-meme-browser-companion` at `cdb868913a6cee1ef5d801381c38fba58b1b2699` with a clean tree, or classify a material divergence and stop `BLOCKED` if it would change the frozen architecture.
2. Confirm Save freeze still matches Worker 04 (`save.html` Description `maxlength="10000"`, analyze then Save, `save.css` `.actions { justify-content: flex-end }`, `save.js` `aliasPayload` includes `description`, messages `IDENTITY` / `CANONICAL_TAGS` / `SAVE_POST` only).
3. Confirm public `main` with `git ls-remote` (no fetch). At Orchestrator restore it was `bfad16b718e135b272a3b0293bb37ddc3101ba49`.
4. Confirm `.ap` gitlink `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.
5. Stop if Extra High cannot be provided as routed.

If retained chat context contradicts the frozen plan or current repository evidence, the repository and the frozen plan win. Retained context is not authority.

## 4. Frozen architecture (do not revise)

Render this selected path. Rejected alternatives stay rejected.

1. **Three surfaces.** A Save popup frozen at Worker 04. B in-page picker remains one-result quick attach with JPEG `gallery-preview` via SW. C side panel hosts real FrameNest web at stored Tailscale origin. Do not mix them.
2. **Hosting.** New `extension/ui/sidebar.html|js|css` as `side_panel.default_path`. Remove `action.default_popup`. Keep `openPanelOnActionClick: true` on `onInstalled` and SW startup. Empty origin → Connect/Reset in the shell; iframe only after `CONFIGURE_ORIGIN`. Shell is not WAR. No `externally_connectable`. No sandbox page. No manifest `frame-src https://*.ts.net`. If Serve/Brave blocks the iframe: honest error, not a new tab, not CORS.
3. **Bridge.** New `v: "framenest.companion.web.v1"` types `WEB_READY`, `HOST_HELLO`, `HOST_ACK`, `ATTACH_REQUEST`, `ATTACH_RESULT`. `companionHosted=true` only after `HOST_HELLO` from pin `chrome-extension://omiihmnlkmieaafaphohakcgmbggppap`. `ATTACH_REQUEST` carries only UUID `mediaId` + `locationId`. Shell forwards existing `TYPES.ATTACH_BEGIN`. Unbound composer → `composer_unbound`, no silent `fallbackDownload`.
4. **Gallery thaw.** Extension-hosted only: replace bottom-right open-original with Attach emoji button. Ordinary tabs unchanged. No global Gallery restyle. No second button. Alias editor / language / Analyze execution parked.
5. **Picker preview.** New `TYPES.PREVIEW_FETCH` on `framenest.companion.v1`. SW GET gallery-preview, JPEG, modest cap. One `<img>` plus title, arrows, Attach. Preview failure falls back to title text. Slight in-page picker iframe height increase is in-scope; Save 360×520 and Attach float frozen.
6. **ADR-0063** required. Do not edit 0061/0062. Zero new `companion_mutation`. Later INFOSEC R3 + independent acceptance; this report does not self-certify.
7. **Causal slices** remain four later implementation slices, then later grants for R3, publication, and NUC.

Required honesty correction that does **not** change the architecture: the frozen plan's phrase that `boundTabId` “already binds only from the content-script sender” is imprecise. Live `service_worker.js` binds `boundTabId` from any `sender.tab.id`. Side-panel / extension pages typically have no `sender.tab`, so they do not overwrite today. The report must classify that as live-code fact, keep the fail-closed rule (extension-page messages must not overwrite `boundTabId`), and name explicit sender checks as implementation hardening inside the already-selected bridge slice.

Named Cooperator probe (later grant, not this exchange):

```text
# [MacBook / fish]
curl -sI https://<node>.<tailnet>.ts.net/ | string match -ri '^(HTTP/|x-frame-options|content-security-policy)'
#------------------------------------------------------
```

Do not run that probe.

## 5. Capability handshake

Full handshake required. Record requested, directly observed, inferred, unknown separately.

Requested: current-worker-session, Native planning mode **not-used**, Extra High, no Max, report file only.

If Native Plan Mode is still on, stop `BLOCKED` and say so. Do not silently re-plan.

## 6. Required terminal deliverable

Write one professional English report beginning **exactly** with:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Then the exchange-01 coordinates exactly once (section 0). Then the numbered sections required by `01_planning_00.md` section 17 (status through parked scope, recommended next Worker route, smallest Orchestrator action, near-misses, pre-existing failure classification).

Include:

- `Report justification: new-evidence`
- `Phase-qualified result: not-applicable`
- `Logical-whole closure: not-closed`
- Confirmation that this repair consumed no second planning cycle and changed no frozen decision
- Threat model and residual-risk owners from the frozen plan
- Owner map and causal slices from the frozen plan
- Parked Section 12.2 backlog still visible
- `Independent acceptance: required-separate-fresh-worker` and INFOSEC R3 as a **later** recommendation, not a certification

Quality bar: `PASS` only if the report is a faithful rendering of the frozen architecture plus the boundTabId honesty correction, gates are exact, and no mutation occurred. `BLOCKED` if baseline/Save freeze diverged or Plan Mode is still on.

After writing the report, stop.
