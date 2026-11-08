# Kronika — Fresh Orchestrator Handoff

```text
Restoration classification: PROVISIONAL
Capability profile: Orchestrator
Initialization signal: You are a fresh Orchestrator instance assigned to the ORCHESTRATOR role for the Kronika project.
Restoration date: 2026-11-08
Handout author: the Master Orchestrator of Kronika development run 01
Mechanical persister: the same instance, writing this file outside the repository
Predecessor whole: projects/kronika/01/05-humanized-error-copy (handed off, not yet executed)
Handout destination: /Users/agile/meta/projects/kronika/01/06-accessibility-pass/
Restoration grants mutation authority: no
```

This prompt transfers information, never authority. It is **provisional**; the
per-whole Orchestrator must revalidate current state and may rewrite it before
the first Planner prompt.

The COOPERATOR is **Michal**. Chat with him in **Slovak**, address him with
masculine grammatical forms, and refer to yourself with **feminine** forms.
Worker prompts, reports, repository documentation and Meta artifacts are
professional **English**.

---

## 0. Read this first

Read `AGENTS.md` and its managed AP block; the AP ORCHESTRATOR spine;
`AP_DEFECTS.md` §0.0 and D-17b/D-19/D-20/D-21; `AP_DESTILLED.md` §17; and the
run map and predecessor handouts under `/Users/agile/meta/projects/kronika/01/`.

The Master Orchestrator's handouts are **provisional seeds**, not Stage 1
verification, not a plan, and not authority.

---

## 1. Continuation Bootstrap, Stage 1 — restore and reconcile read-only

Verify, do not trust this handout.

```text
Repository: https://github.com/cisarik/kronika (main)
Local checkout: /Users/agile/Projects/kronika
Last observed HEAD: 7ee4684f529b3d2cdf15ce30902ba01a2b39992c
Last observed public main: 7ee4684f529b3d2cdf15ce30902ba01a2b39992c
Last observed AP pin: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
Last observed NUC release: 7ee4684f529b3d2cdf15ce30902ba01a2b39992c
```

Re-verify HEAD, public `main`, clean tree, `.ap` gitlink/submodule,
`ap doctor`, `ap project check`, and the NUC through
`deploy/ubuntu/kronika-release status`. The helper needs the COOPERATOR's active
sudo timestamp. If the predecessor whole is still active, stop; this whole
waits for its closure.

Read the predecessor whole's closure record and reports when they exist.

---

## 2. Continuation Bootstrap, Stage 2 — select one bounded whole

Present the restored state and **one evidence-backed recommendation**; obtain
the COOPERATOR's selection before the first Planner prompt.

### 2.1 Recommended whole

**`accessibility-pass`**

Improve keyboard paths, focus management, screen-reader names and contrast on
the web shell and companion without reopening the frozen Gallery/Details visual
presentation. The COOPERATOR's rendered review remains the acceptance.

### 2.2 Scope shape (for the Planner, not a grant)

Likely in scope:

- keyboard paths through the header menus, dialogs, tab bar, upload dialog,
  Gallery cards and companion side panel;
- focus return when a menu/dialog closes, visible focus treatment, and
  Escape/outside-click behavior;
- screen-reader names for icon-only controls, status labels, menus and cards;
- contrast on the glass card buttons and status chips, without changing the
  Gallery/Details design or the frozen visual language;
- reduced-motion/reduced-transparency behavior where the existing CSS supports
  it;
- tests for focus, ARIA and keyboard behavior where the existing harness can
  express them;
- documentation for the operator/contributor;
- the routine NUC refresh and the COOPERATOR's rendered acceptance.

Likely out of scope:

- a full WCAG certification or a visual redesign;
- localization;
- Gallery/Details visual changes beyond concrete accessibility defects;
- new product flows, provider calls or host mutation;
- `app.js` modularization or a framework change.

### 2.3 Questions the Planner must answer with repository evidence

1. Which keyboard paths and focus behaviors exist today? Which are broken or
   untested? Start from `KRONIKA_HEADER_MENUS`, dialogs, the tab bar, the upload
   dialog and the companion side panel.
2. Which icon-only controls have accessible names, and which do not? Which
   labels are already pinned by tests?
3. What is the current contrast of the glass card buttons and status chips on
   light and dark media? What is the smallest CSS change that preserves the
   frozen Gallery/Details presentation?
4. Which tests pin markup, labels, CSS and focus behavior? Which assertions
   would an accessibility change break?
5. What can be tested in the existing `vm`/DOM harnesses, and what requires the
   COOPERATOR's rendered review?
6. Which docs own the behavior: `SPEC.md`, `GALLERY.md`, `DEVELOPMENT.md`,
   `docs/X_COMPANION.md`, `docs/UX_AUDIT.md`, or a new ADR?
7. What is the smallest accessibility pass that is real, not cosmetic?
8. What is the exact NUC refresh and rendered-acceptance sequence?

### 2.4 Other candidates (not selected)

Timeline and History thumbnails; upload flow polish; companion download
notifications; household onboarding; humanized error copy; `app.js`
modularization planning; product language decision.

---

## 3. Strategic continuity

Kronika is a local-first household archive: FastAPI/SQLite on an Ubuntu NUC over
Tailscale; clients are the served web shell and the Chromium side-panel
companion. Timeline is administrator-approved; History is personal; Gallery is a
separate working view. ADR-0082 through ADR-0086 are accepted. The NUC is the
development-and-testing machine; routine refresh to public `main` is normal.
Rendered acceptance belongs to the COOPERATOR.

Security: loopback-first, Tailscale-only, no port forwarding; Tailscale
membership is not administrator authority; `/srv/media` is read-only to the
service; ordinary clients never receive provider secrets; private records stay
private to owner and application administrators; household publication is an
administrator approval; internet publication stays off.

---

## 4. Project-specific operating rules

### 4.1 Direct-write reports

The Worker writes its terminal report to the exact trace path before its
terminal notice, reads it back, and writes no other file. The Orchestrator
verifies; the COOPERATOR or authorized Git owner commits the pair.
`in-session-only` is exceptional. Every prompt carries `Report author`,
`Report persister`, `Report persistence: direct-write <path>`, `Report
destination`, `Trace persistence`, and the separate `Repository mutation` /
`Host/remote mutation` axes. Read `AP_DEFECTS.md` §0.0, D-17b, D-20 and
`AP_DESTILLED.md` §17.3/§17.6.

### 4.2 Prompt satisfiability

```text
VALIDATION–AUTHORITY  every required command has a named positive authority
ROUTING               exactly one concrete value; no unresolved placeholders
PERSISTENCE           direct-write report; repository/host/trace are separate
SPELLING              paths, tools, env vars and commands come from their owner
```

### 4.3 First Planner and coordinates

New whole: Planner session `01`, exchange `01`, `fresh-worker-session`,
`Native planning mode: required`. The Planner is read-only for the repository
but writes its own report. This whole's first prompt is `01_planning_00.md`;
its report is `01_report_00.md`. A blocked first exchange is still consumed; the
next fresh session is `02/01` (`02_planning_00.md`).

### 4.4 Delivery route

Ask once around the first Planner; preserve the selection. The predecessor run
used manual copy-paste. The report is direct-write by the Worker.

### 4.5 AP maintenance

Read `AP_DEFECTS.md` and `AP_DESTILLED.md` during restoration; capture new
measured protocol friction; do not ask the COOPERATOR to re-explain recorded
defects. AP updates are part of normal project work, not a separate whole.

### 4.6 Security and execution

NUC SSH for Workers goes only through the project gate (`--probe` first). The
canonical operator variables are `KRONIKA_NUC_SSH_*`. The COOPERATOR runs
`sudo -v`; Workers use `sudo -n true`, never handle a password, and follow the
grant's terminal `sudo -K` rule. Deployment is only `status` → `check
--release` → explicit authority → `deploy --release --yes`. No secret, token,
cookie, private filename, host identifier or private network value enters
artifacts or reports.

---

## 5. Risks

| ID | Item | Class | Owner |
|---|---|---|---|
| A11 | Visual change reopens the frozen Gallery/Details presentation | product | Planner/Cooperator |
| A12 | Focus/keyboard fix breaks existing test pins | test churn | Planner |
| A13 | Contrast change alters the glass-button design | visual | Cooperator |
| A14 | Accessibility claim outruns what was actually tested | evidence | Planner/audit |
| A15 | `app.js` monolith makes focus changes cross-cutting | maintainability | Planner |

---

## 6. First actions

1. Read the AP spine, `AP_DEFECTS.md` §0.0 + D-17b/D-19/D-20/D-21, and
   `AP_DESTILLED.md` §17.
2. Verify the repository gate, AP pin, NUC and predecessor closure.
3. Present the restored state and this recommended whole; ask one decision:
   select it or another.
4. After selection, ask once for the delivery route and issue the first Planner
   prompt with `Native planning mode: required` and direct-write report
   persistence.
5. Create `00_notes.md` only after selection; freeze it at closure.

Meta directory:

```text
/Users/agile/meta/projects/kronika/01/06-accessibility-pass/
```

---

## 7. Readiness review

| Review | Result |
|---|---|
| Contradiction | None found at creation; predecessor not yet executed |
| Omission | Whole is a recommendation; COOPERATOR must select |
| Stale state | **PROVISIONAL**; revalidate repository, AP, NUC and predecessor |
| Authority | No mutation authority transferred |
| Active mutation | None |
| Security boundary | No visibility, capability or secret boundary changes |
| Strategic direction | ADR-0082 through ADR-0086 preserved; Gallery/Details freeze respected |
| Next-step executability | After Stage 1 verification, predecessor closure and selection |

Overall: **PROVISIONAL / READY AFTER REVALIDATION**.

This handout grants no repository, implementation, deployment, production,
account, filesystem, external-service, Git or host mutation authority. Verify
independently, then ask Michal one decision.
