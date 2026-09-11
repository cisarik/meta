# Handout prompt for a fresh Agent Orchestrator — Libre Tiles, UI/UX Polish

Authored by the Agent Orchestrator at the closure of the release-readiness-triage effort (Meta 19/08) at commit `4d33ad618dc131662193078f183e0b78a94c18f1`, on 2026-09-10. Seeds ONE candidate logical whole: **`ui-ux-polish`** — the last product whole before real-VPS deployment. This handout IS the Cooperator's explicit instruction.

---

## Handout Integrity Record (D-13)

```text
Supersedes: none — this file is a NEW forward-horizon handout.
Coordinate review: honest; written against the published commit
  4d33ad618dc131662193078f183e0b78a94c18f1 on 2026-09-10. Repository facts below were read from
  the live tree, AGENTS.md, PRD, and the 19/00–19/08 closure records; every file:line claim
  was re-measured or is labelled hypothesis.
Enumeration fidelity: the frontend route/component inventory below was produced by the
  Orchestrator's exploration commands on 2026-09-10. It is a hypothesis list; re-derive from
  the live tree.
Numbers not re-measured: browser behaviour across screens, animation performance, mobile
  responsiveness, Playwright availability — all unknown until the Orchestrator measures them
  live in a browser.
Known-stale-by-design: the Cooperator's working tree has 12 modified files + an untracked
  overlay (opt_in.py) implementing LIBRETILES_RUN_SIMULATION slow-test deselection — that
  is the Cooperator's own in-progress work, NOT part of this whole, and must NOT be mutated
  or committed by the Orchestrator.
Predecessor: the release-readiness-triage effort (Meta 19/00–19/08) CLOSED all eight successor
  wholes at 4d33ad6. Backend pytest: 1244 passed, 0 failed. Frontend vitest: 1 red (R2
  aria-live, owned by THIS whole's accessibility decision).
Baseline commit: 4d33ad618dc131662193078f183e0b78a94c18f1 (origin/main aligned, 7 commits
  ahead of the whole-18 closure at 996d9c7).
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656 (DO NOT upgrade).
Meta archive: /home/agile/meta, layout per /home/agile/meta/README.md. Next available
  directory: /home/agile/meta/projects/libretiles/20/00-ui-ux-polish/.
```

---

## 0. Cooperator Intent (verbatim, translated from Slovak)

```text
The Cooperator explicitly instructed:

"I want you to use MCP browser Playwright — or just go through all screens
yourself — take screenshots automatically, then go screen by screen step by
step together with me. I will comment and explain what I imagine could be
better. After you have all the screenshots, cooperate with me step by step
according to the AP protocol as Cooperator. I may also send you my
brainstorming. Maybe the Orchestrator itself will see imperfections.

This is our last communication before VPS deployment. The project must look
visually professional — eye-candy, user-friendly. It already is to a large
degree, but there is still room for improvement in UI/UX.

Maximum effort on the handout so the new fresh Orchestrator understands
everything that is already solved in the frontend."
```

Key phrases from the Cooperator: **professional**, **eye-candy**, **user-friendly**, **screen-by-screen**, **screenshots automatically**, **cooperative review**.

---

## 1. Mission

1. The Orchestrator starts with a read-only autonomous browser pass of EVERY screen in the application, taking full-page screenshots of each, and records observations (spacing, alignment, colors, text overflow, accessibility, mobile responsiveness, animation glitches, loading states, error states).
2. After the autonomous pass, the Orchestrator presents the screenshot library to the Cooperator and they go through it **screen by screen, step by step**. The Cooperator comments, brainstorms, and makes product decisions. The Orchestrator classifies findings, proposes corrections, and obtains explicit Cooperator approval for each material change.
3. After the review pass, the Orchestrator implements the approved corrections autonomously — one bounded slice per screen or per UX concern — with full AP lifecycle (planning for architecture-impacting changes, implementation, acceptance, closure).
4. **The R2 accessibility-pin decision is the FIRST act of this whole** — the Cooperator must decide: "exactly one persistent announcer" as a product invariant, or game-surface-only rule, or a different scope. The Orchestrator presents the evidence (three `aria-live` sites: LiveAnnouncer, ReplayControls ticker, SimulationArena status) and obtains the decision.
5. Leave the VPS deployment (D2) as the explicitly deferred NEXT phase. This whole must NOT deploy.

---

## 2. Verified Starting State

```text
T1  Repository: /home/agile/Projects/libretiles; branch main; HEAD == origin/main ==
    4d33ad618dc131662193078f183e0b78a94c18f1.
T2  AP pin: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656.
T3  ⚠ Working tree is DIRTY (Cooperator's work, DO NOT TOUCH): 12 modified files
    + untracked backend/tests/opt_in.py. This implements LIBRETILES_RUN_SIMULATION
    slow-test deselection gating. It is NOT this whole's scope.
T4  Backend gates: pytest 1244 passed / 27 skipped / 0 failed; mypy 119 files clean;
    ruff clean; makemigrations no changes.
T5  Frontend gates: vitest 1 failed (R2 aria-live), 719 passed, 3 skipped; typecheck/lint/
    build clean. The lone red is the accessibility pin — the known pre-existing.
T6  CI: .github/workflows/ci.yml (static gates: mypy/ruff/makemigrations on backend,
    typecheck/lint/build on frontend; pytest/vitest are local-only) and sbom.yml
    (CycloneDX artifacts on push). Both workflows are unexercised in GitHub Actions.
T7  12 backend variants shipped playable (readiness: "playable" for all 12 per
    list_variant_summaries). 12 locale catalogs, 12 flag icons.
T8  Cooperator language is Slovak. Material decisions and costed choices must be
    presented legibly to him. Authoritative prompts and reports are structurally
    English per AP. He uses "ano", "A", "Pokracuj" as terse replies — these CONTINUE
    the selected scope and NEVER select a new whole.
T9  The Cooperator runs both backend and frontend locally. Backend is Poetry venv
    at backend/.venv; frontend is npm/npx at frontend/node_modules. No Docker needed
    for AI-only play; Redis needed only for human-vs-human websockets.
T10 The Cooperator has a dirty worktree overlay (opt_in.py overlay implementing
    slow-test deselection). Treat it as owner work — do NOT commit, reset, or clean it.
```

---

## 3. Frontend Route Inventory (Every Screen)

Boot the app locally. Visit each route in a browser. Take a full-page screenshot.

### Public routes

| Route | File | What it shows | Notes |
|---|---|---|---|
| `/` | `app/page.tsx` | Landing page | Auth tabs (login/register), "Premium Libre Tiles" hero, 3 feature cards (AI duels, Live queue, Saved games), locale picker. The first page every user sees. |
| `/play` | `app/play/page.tsx` | Game setup / new game | Variant picker, AI opponent selection, vs-human queue join, saved game list. The "Start a game" screen. |
| `/settings` | `app/settings/page.tsx` | Settings | Interface language picker (12 locales with flags), Premium Look toggle (gold/black pointer-reactive chrome), AI timeout/max-steps sliders, provider/model selection. **The premium look system is already implemented — check the spotlight effect with pointer movement.** |
| `/game/[id]` | `app/game/[id]/page.tsx` | Active game | The main game screen: Scrabble-style board, rack with drag-and-drop tiles, score panel, AI thinking overlay, chat panel (if vs-human), game controls (pass/exchange/submit), game history modal. **Most complex screen — test with both AI and human opponents.** |
| `/waiting/[id]` | `app/waiting/[id]/page.tsx` | Waiting room | Pending human match — shows "waiting for opponent" UI, queue status. |
| `/draw/[id]` | `app/draw/[id]/page.tsx` | End-of-game draw | Shows when a game ends in a draw; final board state, scores. |

### Admin routes (staff only)

| Route | File | What it shows |
|---|---|---|
| `/admin` | `app/admin/page.tsx` | Admin dashboard — game list, model selection, catalog management |
| `/admin/login` | `app/admin/login/page.tsx` | Staff login gate |
| `/admin/analytics` | `app/admin/analytics/page.tsx` | Analytics dashboard — model performance, provider stats, game metrics |
| `/admin/playground` | `app/admin/playground/page.tsx` | Simulation playground — run AI vs AI simulations, configure settings |
| `/admin/replay/[id]` | `app/admin/replay/[id]/page.tsx` | Game replay — VCR controls, dual rack visualizer, board replay, move inspector, score breakdown, tool timeline |

### Auth & modal surfaces (in-app, not routes)

| Surface | Component | Notes |
|---|---|---|
| Profile modal | `components/game/ProfileModal.tsx` | Username, password change form, logout. Accessible from header. |
| Game history modal | `components/game/GameHistoryModal.tsx` | List of saved games; resume/continue. |
| Blank picker | `components/game/BlankPicker.tsx` | Select letter for a blank tile placement. Modal dialog. |
| AI thinking overlay | `components/game/AIThinkingOverlay.tsx` | Provider/model attempt pills, ping-pong tile animation, turn telemetry. Shown during AI turns. |
| Chat panel | `components/game/ChatPanel.tsx` | In-game chat for human-vs-human. |
| Game controls | `components/game/GameControls.tsx` | Pass / Exchange / Submit buttons, turn status. |
| Header / Score panel | `components/game/ScorePanel.tsx` | Player scores, bag tile count, language variant badge, profile/games buttons. |

---

## 4. What's Already Solved (Do Not Reinvent)

```text
S1  Premium Look system — fully implemented. frontend/src/lib/premiumSurface.ts
    exports 16 named exports: 6 spot-light gradient styles (PREMIUM_PANEL_STYLE,
    PREMIUM_HEADER_STYLE, PREMIUM_MODAL_STYLE, PREMIUM_MODAL_CARD_STYLE,
    PREMIUM_FOOTER_STYLE, PREMIUM_PING_PONG_TILE_STYLE), a gold-text-shadow CSS
    class, a pointer-reactive handler (handlePremiumSurfacePointer), and a
    ping-pong tile motion factory with reduced-motion respect.
    Controlled by Zustand store flag premiumLookEnabled, persisted to localStorage.
    Used by: settings page, game header/footer, AI thinking overlay tile.

S2  i18n — 12 locales fully shipped. LOCALES = en/sk/cs/pl/de/pt/is/it/nl/da/sv/af
    in frontend/src/lib/i18n/locales.ts. All 12 catalogs at messages.XX.ts.
    REVIEWED_LOCALES = en/sk/cs/pl (test file). All 12 locale flags at
    frontend/public/XX.png (48x32). LOCALE_FLAG_SRC and VARIANT_FLAG_SRC are
    PARTIAL-typed by design with conditional spreads: a thirteenth locale must
    NOT silently request a missing flag.

S3  Framer Motion animations throughout: board tile placement, score updates,
    ping-pong AI thinking tile, draw animation, modal transitions. DnD Kit for
    rack-to-board drag and drop.

S4  Responsive layout: board, rack, score panel, settings all use Tailwind breakpoints.
    Touch drag-and-drop works.

S5  AI thinking overlay: ordered provider/model pills per attempt, gold/black
    ping-pong tile on active attempt, reduced-motion static tile fallback,
    flat amber chrome when Premium Look is off, transient telemetry copy cleared
    with turn completion.

S6  Accessibility basics: aria-live regions (3 existing — the R2 pin question),
    aria-labels on board cells and buttons, role=dialog on modals, keyboard-
    navigable game controls. CSP headers via proxy.ts with nonce-based
    script-src strict-dynamic, frame-ancestors none, permission-policy.

S7  Human-vs-human multiplayer: WebSocket realtime sync via Django Channels,
    queue join/cancel, waiting room, in-game chat, server-derived acting slot.
    Profile modal with password change. Logout shortcut in header cluster.

S8  All game features: variant selection (12 playable variants), AI play with
    selectable provider/model, judge validation, pass/exchange/submit, scoring,
    tile bag, blank assignment, word validation against Collins 2019.
```

---

## 5. Known UX Gaps and PRD Items (What to Polish)

```text
G1  R2 accessibility-pin decision — FIRST ACT. Three aria-live regions exist:
    LiveAnnouncer.tsx:25 (polite), ReplayControls.tsx:19 (polite on the ticker),
    SimulationArena.tsx:39 (polite on status text). The test at i18n.test.ts:829
    expects exactly one. Cooperator decides the product invariant.

G2  Mobile bottom-sheet rack and pinch-zoom — unimplemented (PRD Phase 5).
    Currently mobile uses the same rack layout as desktop; no pinch-zoom on board.

G3  Per-game move timeline with expandable word details — unimplemented (PRD Phase 5).
    The admin replay engine has this for replays; the game screen does not.

G4  AI thinking particles — unimplemented (PRD Phase 5). The AIThinkingOverlay
    has pills and a ping-pong tile, but no decorative particles.

G5  Playwright E2E tests — absent (PRD Phase 8, triage W-F → deferred here).

G6  General visual polish candidates (hypothesis — the Orchestrator's browser
    pass will find these): spacing consistency across screens, loading skeletons
    or spinners during data fetch, empty-state components, error-state components,
    toast/notification system consistency, color contrast in non-premium mode,
    focus ring visibility, hover/active state consistency, text truncation in
    narrow viewports, board cell size at extreme viewport widths, rack tile sizing
    consistency, modal backdrop and scroll lock behavior, transition/animation
    smoothness, performance on slower devices.

G7  The dirty worktree overlays the Cooperator's local libretiles-run-simulation
    gating. If he wants it committed, he'll say so. Do not fold it into this whole
    unless he explicitly routes it.
```

---

## 6. How to Run Locally

The Orchestrator runs these commands to boot the app for browser screenshots:

```bash
# Terminal 1 — backend:
cd /home/agile/Projects/libretiles/backend
source .venv/bin/activate
python manage.py runserver 127.0.0.1:8000

# Terminal 2 — frontend:
cd /home/agile/Projects/libretiles/frontend
npm run dev
# Opens at http://localhost:3000
```

No Docker, Redis, or .env credentials needed for AI-only play. The app boots and reaches the landing page. If the Orchestrator needs AI turns to work (for the game screen), the Cooperator's frontend/.env.local provides OpenRouter/NVIDIA keys — the Orchestrator must NOT read or log the keys, only report their presence/absence as `present: yes` or `present: no`.

**For screenshots:** the Orchestrator uses Playwright (if available as MCP browser tool) or manual browser screenshots. One full-page capture per route listed in section 3. For the game screen, a static board state is fine; no AI turn needs to complete. For admin routes, access `/admin` and any derivative pages — if authentication is needed, the Cooperator provides credentials or creates a test session.

**Screenshot checklist** (numbered for the Cooperator review):

```
 1. /          — Landing page (logged out)
 2. /          — Landing page (logged in, if session available)
 3. /play      — New game setup
 4. /settings  — Settings page (premium look OFF)
 5. /settings  — Settings page (premium look ON — test the spotlight)
 6. /game/[id] — Active game (AI turn)
 7. /game/[id] — Active game (player turn, rack with tiles)
 8. /game/[id] — Game history modal
 9. /game/[id] — Profile modal
10. /game/[id] — Blank picker modal
11. /game/[id] — AI thinking overlay visible
12. /game/[id] — Chat panel (vs-human)
13. /waiting/[id] — Waiting room
14. /draw/[id]  — End-of-game draw screen
15. /admin      — Admin dashboard
16. /admin/analytics — Analytics page
17. /admin/playground — Simulation playground
18. /admin/replay/[id] — Replay studio
19. All screens at 375px width (mobile)
20. All screens at 768px width (tablet)
```

---

## 7. Screen-by-Screen Cooperative Workflow

```text
Phase 1 — Autonomous Screenshot Pass (Orchestrator only, read-only)
  - Boot the app.
  - Navigate to every route/surface in section 3.
  - Take full-page screenshots (desktop + mobile widths).
  - Record observations: spacing, colors, overflow, animation glitches,
    responsiveness issues, accessibility concerns, missing loading/error/empty
    states, visual inconsistencies.
  - Produce a preliminary findings list (numbered, with screenshot references).
  - Do NOT implement anything in this phase.

Phase 2 — Cooperative Review (Cooperator + Orchestrator)
  - Present the screenshot library to the Cooperator.
  - Go screen by screen, step by step (1-20 from the checklist).
  - For each screen, the Orchestrator presents observations; the Cooperator
    comments, brainstorms, and makes product decisions.
  - Classify every finding: bug, polish, design-debt, deferred, accepted.
  - The R2 accessibility-pin decision is screen-independent — present it first.
  - After all screens are reviewed, the Cooperator approves the correction
    backlog (which items to fix, in what priority).

Phase 3 — Bounded Implementation (Orchestrator with Workers)
  - One bounded implementation slice per screen or per UX concern.
  - Full AP lifecycle: prompt, implementation, acceptance, closure.
  - Each slice commits to origin/main with non-force push.
  - Run backend pytest + frontend typecheck/lint/build between slices.
  - The R2 red stays red until the Cooperator decides the pin.

Phase 4 — Final Acceptance
  - Re-screenshot all changed screens.
  - Cooperator final review and sign-off.
  - Close the logical whole.
```

---

## 8. Standing Constraints and Locks

```text
L1  Free-only product. No Stripe, no credits, no billing, no USD.
L2  Nine providers shipped. Provider list, constants, tier, exact model tuples,
    and provider documentation are FROZEN. Do NOT change any provider.
L3  No network to update package registries or audit dependencies — the DRF bump
    carried from W-H is a pre-deployment item for the NEXT phase (see §9).
L4  The dirty worktree is the Cooperator's. Do NOT commit it, reset it, or
    clean it. Do NOT fold it into this whole.
L5  AP pin 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656. Do NOT upgrade.
L6  The PARTIAL flag-table shape (LOCALE_FLAG_SRC, VARIANT_FLAG_SRC) stays
    by design. If a 13th locale is added, the CONDITIONAL spread guard must
    not be removed. REVIEWED_LOCALES stays en/sk/cs/pl.
L7  Backend WordAuthority is the sole word-validity path. Do not change it.
    The frozen parity oracle is protected.
L8  Published Docker Compose topology (commit 996d9c7 → 4d33ad6) is accepted.
    Deployment-artifact changes need the disposable Docker validator.
L9  No host, SSH, DNS, TLS, or production action without explicit Cooperator
    host grant (the VPS deployment whole — after this one).
```

---

## 9. Pre-Deployment Items Carried from Triage (Not This Whole)

These items were discovered or carried during the release-readiness triage and belong to the **NEXT phase** (real-VPS deployment, D2) or a small pre-deploy security slice. The Orchestrator should KNOW about them but NOT fold them into UI/UX polish:

```text
P1  djangorestframework 3.17.0 → 3.17.2 (CVE-2026-73228, JSON parser bypass).
    Warranted security bump. Belongs to a pre-deploy dependency update slice.
P2  Board-defense wide acceptance red (SK winrate 0.45)— accepted-residual,
    known-fail, manual-only. Not a ship-stopper.
P3  Postgres parity opt-in suite — not yet run; deferred to CI.
P4  Endgame wide acceptance — green but fragile (+4 margin); manual-only.
P5  W-E nightly CI suites (endgame matrix, Slovak extra, 100-seed witness) —
    workflow files not yet created; separate CI follow-on.
P6  All tripwire tests survived the 2026-09-10 posture check.
P7  The Cooperator's opt_in.py overlay (slow-test deselection gating) is
    his in-progress work. When he commits it, it may need a CI integration slice.
```

---

## 10. The R2 Accessibility-Pin Decision (Detail)

This is the FIRST decision the Orchestrator presents. Here is the evidence:

```text
Three aria-live regions in the frontend source (all measured at baseline):

  frontend/src/components/game/LiveAnnouncer.tsx:25
    aria-live="polite" — a <div> that announces game-state changes
    ("Your turn", "Opponent played", etc.)

  frontend/src/components/admin/ReplayControls.tsx:19
    aria-live={props.isPlaying ? "off" : "polite"} — the ply ticker
    paragraph: "Ply 1 of 2: Ada played AT for 4 points"

  frontend/src/components/admin/SimulationArena.tsx:39
    aria-live="polite" — simulation status text:
    "Waiting for the next committed turn."

Test: frontend/src/lib/i18n/i18n.test.ts:829-842
    AC-ONE-LIVE-REGION: scans entire frontend/src (excluding test files)
    for aria-live and role="status"; asserts exactly 1.

Test result: FAIL — measured 3 live, 1 status, expected 1 live, 1 status.
```

The Cooperator must decide ONE of:

```text
A  "Exactly one persistent announcer" IS the product invariant.
   → ReplayControls and SimulationArena must route their announcements
     through LiveAnnouncer (or drop their aria-live), AND the test
     scope must be exactly "aria-live=1, role=status=1" across src.

B  "One announcer in the game surface only" — admin components are
   auxiliary tools, not the product surface.
   → Test scope narrows to exclude admin trees. Still 1 live + 1 status
     in the game surface.

C  "The three live regions are intentional — different contexts need
   different announcers."
   → Accept as intentional design. Remove or rescope the test.

D  Something else the Cooperator imagines.
```

---

## 11. Explicitly Out of Scope

```text
- Real-VPS deployment, DNS, TLS, SSH, host hardening.
- drf bump (carried to deployment phase per §9 P1).
- CI workflow additions (nightly suites, postgres parity — carried).
- Provider list/model changes (frozen lock L2).
- Backend game logic or word authority changes.
- AP pin upgrade.
- The Cooperator's dirty worktree overlay.
- Stripe, LM Studio, Vercel AI Gateway, host systemd (permanent decisions).
```

---

## 12. Standing Quality Gates

```text
Backend (from /home/agile/Projects/libretiles/backend):
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py makemigrations --check --dry-run
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest

Frontend (from /home/agile/Projects/libretiles/frontend):
  npm run typecheck
  npm run lint
  npm run build

Never ambient python, python3, or poetry run.
```

---

## 13. Your Exact First Bounded Step

```text
1. Restore read-only: verify T1–T2, read AGENTS.md, .ap/AP.md, .ap/AP_ORCHESTRATOR.md,
   .ap/AP_WORKER.md, .ap/PROMPT_CONTRACTS.md, /home/agile/meta/README.md, and this file.
2. Emit the SELECTION ECHO for ui-ux-polish.
3. Boot the app locally (backend runserver 127.0.0.1:8000 + frontend npm run dev).
4. AUTONOMOUS SCREENSHOT PASS: visit every route/surface in section 3, take
   screenshots at desktop and mobile widths (sections 6, 7), record observations.
5. Present the screenshot library + R2 accessibility-pin question to the Cooperator.
6. Go screen by screen, step by step, with the Cooperator. Obtain approval for
   each correction.
7. Implement approved corrections autonomously, one slice at a time.
8. Close the whole only after the Cooperator's final acceptance.
```