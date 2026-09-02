### Report for ORCHESTRATOR_CHAT

1. Logical whole `ui-internationalization`, Worker session ordinal 13, Worker exchange ordinal 01.
2. **status: PASS**
3. **phase-qualified result: implementation-PASS**
4. **start commit:** `e8cc7bb3be6b1e403102ed4e89c04996a0349fd3`  
   **end commit:** `74b5339e5bdcdd036041b6bf908c5454f7d8a400`
5. **Build-gate route: PRIMARY.** `ss -tlnp | grep :3000` printed nothing (grep exit 1). Build ran; `.next` was written by this Worker.
6. **Changed files**
   - `frontend/src/components/game/LiveAnnouncer.tsx` (CREATE) — persistent polite announcer plus `composeAnnouncement`
   - `frontend/src/app/game/[id]/page.tsx` — mount announcer; strip live semantics from six toast branches; `useMemo` for the message
   - `frontend/src/components/game/AIThinkingOverlay.tsx` — `role="group"`; live semantics removed
   - `frontend/src/components/game/TurnStatusNotice.tsx` — live semantics and unused `useT` removed
   - `frontend/src/components/tiles/TileRack.tsx` — always spread `attributes`; listeners stay conditional; `tabIndex` override
   - `frontend/src/lib/i18n/GLOSSARY.md` — Accessibility paragraph corrected
   - `frontend/src/lib/i18n/i18n.test.ts` — new AC-* tests; authorized toast-count inversion  
   **`git diff --name-only` for the four `messages.*.ts` files: EMPTY.**  
   **`git diff --name-only backend/`: EMPTY.**
7. **Before/after counts** (`frontend/src`, `.ts`/`.tsx`, excluding `*.test.*`):

   Command:
   ```text
   python3 - <<'PY'
   from pathlib import Path
   root = Path("frontend/src")
   needles = ["aria-live", 'role="status"', 'role="dialog"', "aria-modal",
              'role="group"', "htmlFor", "tabIndex", "activeElement"]
   # walk ts/tsx, skip .test.
   PY
   ```

   | token | before | after |
   |---|---|---|
   | `aria-live` | 8 | **1** |
   | `role="status"` | 8 | **1** |
   | `role="dialog"` | 4 | **4** |
   | `aria-modal` | 4 | **4** |
   | `role="group"` | 0 | **1** |
   | `htmlFor` | 0 | **0** |
   | `tabIndex` | 4 | **5** |
   | `activeElement` | 0 | **0** |

   End state **1, 1, 4, 4, 1, 0, 5, 0** as specified (ts/tsx). Including `GLOSSARY.md`, `aria-modal` is 5 because the Accessibility paragraph still names `` `aria-modal` `` in prose; that is documentation, not a fifth dialog.
8. **Announcer mount.** `frontend/src/app/game/[id]/page.tsx:1688`:
   ```1687:1689:frontend/src/app/game/[id]/page.tsx
         <BlankPicker onSelect={handleBlankSelect} />
         <LiveAnnouncer message={announcement} />
         <DragOverlay
   ```
   It is a direct child of `DndContext` (the sole root of the authenticated `GamePage` return). Ancestors: `GamePage` → `DndContext`. Siblings include two `AnimatePresence` trees, the `min-h-screen` column, the conditional AI overlay, `BlankPicker`, and `DragOverlay`. None of those is an ancestor. There is no `&&` on `gameState`, `toast`, `aiThinking`, or `game_mode`. The `if (!token)` early return is a different tree (session-expired), as specified: the announcer lives inside `DndContext`.
9. **Composition rule.** `composeAnnouncement` returns a non-empty (after trim) `toastMessage` if present, else a non-empty `turnStatusText`, else `""`. The game page memos `toast?.message` and `turnStatus.text` only. `aiStatusMessage` and `humanState` are not inputs. AI turns are already covered by `turnStatus` → `t("game.status.aiThinking")`.
10. **`sr-only`.** `grep -c "sr-only" .next/static/css/*.css` → **1**. Tailwind emitted the utility. Section 5.4 fallback was **not** taken.
11. **Rack tile.**  
    Before: `{...(isExchangeMode \|\| interactionDisabled \|\| !dragEnabled ? {} : { ...listeners, ...attributes })}`  
    After: `{...attributes}` always; `{...(same expression ? {} : listeners)}`; then `tabIndex={selectEnabled ? 0 : -1}`.  
    Drag listeners remain gated on the same expression, so drag behaviour is unchanged. `TapSelectableTile` was not edited. `AC-RACK-ROLE` used `renderToStaticMarkup` of `TileRack` **without** `DndContext`; that path succeeded (no source-slice fallback).
12. **Pre-fix / post-fix**

    | test | pre-fix | post-fix |
    |---|---|---|
    | AC-ANNOUNCE-PURE | `Error: Cannot find package '@/components/game/LiveAnnouncer' imported from .../i18n.test.ts` | PASS |
    | AC-ANNOUNCE-ONE | same missing-module error | PASS |
    | AC-NO-OVERLAY-LIVE | `AssertionError: expected 1 to be +0` at `aria-live=` count (fixture had timer + `humanState`) | PASS |
    | AC-NO-TOAST-LIVE | `AssertionError: expected 6 to be +0` at `role="status"` | PASS |
    | AC-ONE-LIVE-REGION | `AssertionError: expected 8 to be 1` | PASS |
    | AC-RACK-ROLE | `AssertionError: expected '<div class="flex w-full...' to match /role="/` (aria-label present, no role, exchange mode) | PASS |

13. **Section 10.1 inversion.** Flipped `toast.match(/role="status"/g)?.length` **6 → 0** and `toast.match(/aria-live="polite"/g)?.length` **6 → 0**, under **AC-NO-TOAST-LIVE**. Kept `not.toContain('role="dialog"')` and `not.toContain("aria-modal")`. The overlay half of `AC-STATUS-NOT-DIALOG` was replaced by **AC-NO-OVERLAY-LIVE** (zero live/status, has `role="group"`). Positive announcement coverage is **AC-ANNOUNCE-ONE**. A toast is still never a dialog and never steals focus; it is also no longer its own live region. Nothing else was xfailed, skipped, or deleted.
14. **Gates**
    - mypy: `Success: no issues found in 83 source files`
    - ruff: `All checks passed!`
    - check: `System check identified no issues (0 silenced).`
    - pytest: `381 passed, 4 skipped in 221.00s (0:03:40)`
    - typecheck: exit 0
    - vitest: **418 passed | 3 skipped** (was 414 passed | 3 skipped). Net **+4**: six new tests (PURE, ONE, NO-OVERLAY-LIVE, NO-TOAST-LIVE, ONE-LIVE-REGION, RACK-ROLE) minus the two inverted `AC-STATUS-NOT-DIALOG` cases.
    - lint: exit 0
    - build: exit 0; every listed route `ƒ`; zero `○` static routes
15. **Commit and push.** `git ls-remote origin refs/heads/main` before push was still `e8cc7bb3be6b1e403102ed4e89c04996a0349fd3`. Pushed `main` non-force.  
    Local HEAD: `74b5339e5bdcdd036041b6bf908c5454f7d8a400`  
    Public `refs/heads/main`: `74b5339e5bdcdd036041b6bf908c5454f7d8a400`
16. **Evidence ceiling.** Tests prove markup singularity (one `aria-live` / one `role="status"` in product ts/tsx), persistence in source (unconditional mount next to `BlankPicker`), composition precedence, overlay no longer a live region, and a rendered rack `role` beside `aria-label` in exchange mode and when interaction is disabled. **No assistive technology was observed. None can be in this project** (vitest `environment: "node"`, no axe/jsdom, Browser MCP locked, Cooperator decision 10: no screen reader). These tests do not prove that anything is spoken.
17. **Remaining accessibility (not fixed)**
    - **Toast `aria-label` on a generic `motion.div`.** Section 5 authorized removing `role` and `aria-live` only; the six `aria-label={t("a11y.status.turn")}` attributes remain on role-less containers. Same class of defect as `uii-01-F20`.
    - **`DraggableTile` is now `role="button"` in exchange mode with no Enter/Space handler.** `TapSelectableTile` has `onKeyDown`; the draggable path does not. Tab can land on exchange tiles (`selectEnabled` → `tabIndex={0}`) without a keyboard activation path.
    - **`uii-01-F19`** — no focus trap / no focus restoration (`activeElement` still 0). Accepted residual.
    - Initial `turnStatus` is silent by design (region mounts with text already present).
    - `{humanState}` remains English (`AC-NO-TELEMETRY-KEY`).
    - Session-expired `!token` tree has no announcer (outside `DndContext`, as specified).
    - Invalid-word toasts announce `toast.message` only, not the visual heading or word chips.
18. **Deviations / missing evidence.** Announce tests used a dynamic `import()` for the pre-fix run so the rest of `i18n.test.ts` could load; the committed tests use a static import. `AC-ONE-LIVE-REGION` scans `.ts`/`.tsx` excluding tests, not markdown. `DndContext` is imported in the rack test for the authorized fallback and was unused on the successful render path; lint still passed. Context usage was high during mandatory reading of `page.tsx` and `git show e8cc7bb`; not independently metered.
19. **Resolved Execution Issues / Near-Misses:** none
20. **Pre-Existing Failure Classification:** none
21. **Smallest next step.** Independent review of the single announcer mount and of leftover toast `aria-label` on generic elements — do not add a focus trap unless a later slice reopens `uii-01-F19`.
22. **report justification: new-mutation**
23. **Authority expired** at this terminal report. Logical-whole closure: **not-closed**.