You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 13
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: R14 — one persistent announcer, and a role on every named rack tile
Implementation authority: explicit
Independence required: no
Reasoning recommendation: high. Basis — this slice REMOVES accessibility attributes that the previous
  slice added, and replaces eight of them with one. Doing that safely requires understanding WHY the
  previous shape was wrong, not just where it is. A Worker who treats this as "add more ARIA" will make it
  worse.
Report justification: new-mutation
Context-pressure rule: report visible context usage if it exceeds 70%.

=====================================================================
1. REPOSITORY GATE
=====================================================================
Repository checkout topology: standalone checkout
Repository identity: https://github.com/cisarik/libretiles
Working directory: /home/agile/Projects/libretiles
Expected branch: main
Working-copy topology: canonical checkout.

  git rev-parse HEAD                     -> e8cc7bb3be6b1e403102ed4e89c04996a0349fd3
  git rev-parse HEAD:.ap                 -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                         -> ## main...origin/main
  git status --porcelain=v1              -> EMPTY
  git ls-remote origin refs/heads/main   -> e8cc7bb3be6b1e403102ed4e89c04996a0349fd3

STOP if any value disagrees.

=====================================================================
2. MANDATORY READING, IN THIS ORDER
=====================================================================
1. /home/agile/Projects/libretiles/AGENTS.md
2. /home/agile/Projects/libretiles/frontend/AGENTS.md
3. .ap/AP.md sections 5, 8, 9, 12, 18, 19
4. .ap/AP_WORKER.md
5. `git show e8cc7bb --stat` and then the full diff of the previous slice. You are correcting it. Read
   what it did before you change it.
6. frontend/src/components/game/AIThinkingOverlay.tsx — ALL of it, especially :245-320
7. frontend/src/components/game/TurnStatusNotice.tsx — all 40 lines
8. frontend/src/app/game/[id]/page.tsx :100-110 (the `Toast` type), :190-400 (`ToastOverlay`),
   :1446-1478 (the `turnStatus` memo), :1650-1695 and :1755-1770 (the mount sites)
9. frontend/src/components/tiles/TileRack.tsx :18-100 (`DraggableTile`) and :222-270 (the branch)
10. frontend/src/lib/i18n/GLOSSARY.md — the `## Accessibility` section, which this slice corrects
11. frontend/src/lib/i18n/i18n.test.ts — `AC-DIALOG-PRESENT` and `AC-STATUS-NOT-DIALOG`

=====================================================================
3. GOAL — ONE COHERENT OUTCOME
=====================================================================
Replace eight scattered pseudo-live-regions with ONE persistent announcer that actually announces, and make
the rack tile's accessible name valid in every state.

This is a REMEDIATION slice. The previous slice was accepted and its gates are green, but the Orchestrator's
independent review found three defects — `uii-01-F21`, `uii-01-F22` and `uii-01-F20`. All three were caused
by ORCHESTRATOR INSTRUCTIONS, not by Worker error. You are not cleaning up someone's sloppiness; you are
correcting a design that was specified wrongly.

Net effect on the codebase: `role="status"` goes from 8 occurrences to 1, `aria-live` from 8 to 1. This
slice makes the product SMALLER and the accessibility REAL.

=====================================================================
4. MEASURED DEFECT ANALYSIS — the evidence, so you can check it yourself
=====================================================================

--- 4.1 uii-01-F21 — the AI overlay re-announces itself once per second ---

```text
FACT (ARIA spec)   role="status" carries an implicit aria-atomic="true". When ANY descendant changes, the
                   ENTIRE region is re-announced, not just the changed node.
FACT (this code)   AIThinkingOverlay.tsx:271-273 puts role="status" + aria-live="polite" on the
                   `fixed inset-0` container.
FACT (this code)   AIThinkingOverlay.tsx:298-304 renders {formatTime(aiCountdown)} INSIDE that container.
                   `aiCountdown` is a per-second store countdown.
FACT (this code)   AIThinkingOverlay.tsx:325-339 appends candidate rows inside the same container.
CONSEQUENCE        for the whole AI turn, an assistive technology re-reads the timer, the best score, every
                   provider pill and every candidate row roughly once a second.
REGRESSION         at the parent commit c3f75e3 there WAS a narrow correct announcer:
                   `<p aria-live="polite">` on the single telemetry line. The previous slice removed it —
                   correctly, since it would have nested — and replaced it with something worse.
```

⚠ This directly contradicts the reason `polite` was chosen over `assertive` in the first place: so
announcements would queue rather than interrupt. A once-per-second atomic re-read is maximal interruption.

--- 4.2 uii-01-F22 — a live region that mounts with its content may never announce ---

```text
FACT (ARIA)   an assistive technology observes MUTATIONS inside a live region. A region that appears in the
              DOM already containing its text presents no mutation to observe, so the announcement is
              commonly dropped entirely.
FACT          ToastOverlay is rendered on demand              game/[id]/page.tsx:1760  `{toast && ...}`
FACT          TurnStatusNotice returns null when there is no text   TurnStatusNotice.tsx:14
FACT          AIThinkingOverlay lives inside `{aiThinking && ...}` in an AnimatePresence
CONSEQUENCE   all three delivered "status regions" probably announce NOTHING, ever.
NOT A REGRESSION  the parent commit's `<section aria-live>` was conditional in exactly the same way. This
              is a pre-existing property that the previous slice inherited rather than introduced.
```

--- 4.3 uii-01-F20 — the rack tile's name is dropped in exchange mode ---

```text
FACT   TileRack.tsx:46 spreads dnd-kit's `attributes` ONLY when
         !(isExchangeMode || interactionDisabled || !dragEnabled)
       (line 38 is the same expression used for dnd-kit's own `disabled` option — do not confuse them)
FACT   `attributes` is where role and tabIndex come from. Verified in the installed package,
       @dnd-kit/core 6.3.1, node_modules/@dnd-kit/core/dist/core.esm.js:3432-3438:
         { role, tabIndex, 'aria-disabled': disabled, 'aria-pressed': ..., 'aria-roledescription': ...,
           'aria-describedby': ... }   with role defaulting to 'button' and tabIndex to 0
FACT   TileRack.tsx:86 sets aria-label unconditionally on that same motion.div
CONSEQUENCE  in EXCHANGE MODE and when it is NOT YOUR TURN the element is a role-less generic div carrying
       an aria-label. `aria-label` is not permitted on a generic element and is commonly ignored, so the
       name is silently dropped. In exchange mode those tiles are still clickable, so this is real.
NOT AFFECTED  the tap path. TapSelectableTile renders a real <button> and is correct. Do not touch it.
```

=====================================================================
5. ⛔ THE ONE MECHANISM: A SINGLE PERSISTENT ANNOUNCER
=====================================================================
F21 and F22 have ONE shared fix, and taking it is what makes this slice a simplification instead of another
layer. Do not fix them separately.

```text
ADD     exactly ONE visually hidden region, mounted UNCONDITIONALLY, present before any text changes:
          role="status"  aria-live="polite"  aria-atomic="true"  aria-label={t("a11y.status.turn")}
        Its text content is a single short string, or empty.

REMOVE  role="status" and aria-live from ALL SIX ToastOverlay branches   page.tsx role= :195 :250 :288
                                                                                 :327 :369 :384
                                                                        with each aria-live on the line
                                                                        immediately below
REMOVE  role="status", aria-live and aria-label from the AIThinkingOverlay container   AIThinkingOverlay
        and REPLACE with role="group" + the SAME aria-label. `group` is a valid host for an accessible
        name and is NOT a live region, so the ticking timer becomes harmless and the key stays in use.
REMOVE  role="status", aria-live and aria-label from TurnStatusNotice, which becomes plain visual text
        again. Its `useT` import then becomes unused — remove the import too or lint will fail.
```

⚠ AFTER this slice the repository must contain exactly ONE `aria-live` and exactly ONE `role="status"` in
`frontend/src` outside test files. That is the check; run it.

--- 5.1 Where the announcer mounts, and why it matters ---

Mount it in `frontend/src/app/game/[id]/page.tsx` immediately adjacent to `<BlankPicker ... />` at ~:1691 —
inside `<DndContext>`, OUTSIDE every `AnimatePresence`, and NOT behind any `&&` on `gameState`, `toast`,
`aiThinking` or `game_mode`. The entire point is that the element exists BEFORE its text changes. If you
mount it conditionally you have reimplemented `uii-01-F22`.

⚠ EXPECTED AND CORRECT: the FIRST value is not announced, because at mount the text is already present.
`turnStatus.text` is non-null on load, so the initial turn status is silent and every subsequent change is
announced. That is how this pattern works. Do NOT add a mount-delay, a double render, a `useEffect` that
clears and re-sets the text, or any other trick to force the first announcement. If you find yourself
writing one, stop and report instead.

--- 5.2 What it announces: toast first, turn status otherwise ---

```text
INPUT 1  toast.message      every Toast variant has a `message: string`   page.tsx:102-109
INPUT 2  turnStatus.text    fully localized through t/tf                  page.tsx:1446-1477
RULE     a present toast WINS, because it is the more recent event. Otherwise the turn status. If neither
         exists, the announcer renders empty.
```

⛔ Do NOT announce `aiStatusMessage`, and do NOT announce `humanState`. `aiStatusMessage` changes per
provider attempt and would be chatty; `humanState` is deliberately still English pending its own slice
(`AC-NO-TELEMETRY-KEY`). The AI turn is ALREADY covered, because `turnStatus` returns
`t("game.status.aiThinking")` while `aiThinking` is true — see page.tsx:1456-1465. Adding a second AI
announcement source would duplicate it.

--- 5.3 The pure helper, because this project tests arithmetic as functions ---

Put BOTH the component and a pure exported helper in ONE new file:

```text
frontend/src/components/game/LiveAnnouncer.tsx        (CREATE — the only new file in this slice)
  export function composeAnnouncement(input: { toastMessage?: string | null;
                                              turnStatusText?: string | null }): string
  export function LiveAnnouncer({ message }: { message: string })
```

⚠ Do NOT annotate the component's return type as `JSX.Element`. React is 19.2.4, the global `JSX` namespace
is not reliably available, and this codebase uses `JSX.Element` exactly ZERO times. Let the return type be
inferred, like every other component here.

`composeAnnouncement` returns the toast message when it is a non-empty string, else the turn status text
when it is a non-empty string, else `""`. It is pure, it has no hooks, and it is unit-testable without
rendering — the same reason `nextPickerHighlight` and `filterPickerOptions` were extracted in slice R1.

The component itself needs `useT` for its `aria-label`, so give the file `"use client"` at the top, matching
every other file in `components/game/`. It takes `message` as a PROP and reads nothing from the store: the
message is the game page's business, the label is the component's.

The game page computes the message with `useMemo` over `toast?.message` and `turnStatus.text` and passes it
in. Named exports from a COMPONENT file are fine; the App Router export restriction in
`frontend/AGENTS.md` applies only to `page.tsx` files, and this is why the helper does not live in the page.

--- 5.4 Visually hidden: the class, and the pre-authorized fallback ---

Use Tailwind's built-in `sr-only` utility. Tailwind is 4.2.2 and ships it, but it is JIT — the class is
emitted only because a source file references it, and NOTHING in this codebase references it today
(measured: 0 occurrences).

```text
VERIFY AFTER THE BUILD   grep -c "sr-only" .next/static/css/*.css   must be >= 1
FALLBACK if it is 0      replace the class with an explicit inline style on the same element:
                           position:absolute; width:1px; height:1px; padding:0; margin:-1px;
                           overflow:hidden; clip-path:inset(50%); white-space:nowrap; border:0
                         and SAY IN THE REPORT that you took the fallback and what the count was.
```

⛔ Do NOT hide the announcer with `display:none`, `visibility:hidden`, `hidden`, `opacity-0` alone, or
`width/height: 0`. Every one of those removes the element from the accessibility tree, which would give you
a region that is present, persistent, and completely silent.

=====================================================================
6. ⛔ THE RACK TILE FIX — exactly this, nothing more
=====================================================================
In `DraggableTile` in `frontend/src/components/tiles/TileRack.tsx`, at line 46:

```text
NOW      {...(isExchangeMode || interactionDisabled || !dragEnabled ? {} : { ...listeners, ...attributes })}
BECOMES  spread `attributes` ALWAYS, and keep `listeners` conditional on exactly the same expression.
THEN     set tabIndex explicitly AFTER the spread:  tabIndex={selectEnabled ? 0 : -1}
```

Reasons, so you do not "improve" this:

```text
why always spread attributes   role="button" is what makes the existing aria-label valid and exposed. It
                               also brings aria-disabled, which dnd-kit already computes correctly from
                               the same `disabled` value.
why keep listeners conditional the listeners are the DRAG behaviour. Spreading them when drag is disabled
                               would change gameplay. This slice changes no gameplay.
why tabIndex is overridden     attributes bring tabIndex: 0. Without the override, tiles you cannot
                               interact with would become Tab stops when it is not your turn — up to seven
                               new stops for no benefit. `selectEnabled` already exists at :41 and is
                               exactly the right condition: it is true in exchange mode, where the tiles
                               ARE clickable.
```

⛔ Do NOT touch `TapSelectableTile`. Do NOT add `aria-pressed` to `DraggableTile`. Do NOT change
`ariaLabel`, `tf("a11y.rackTile")`, `TILE_POINTS`, or the `letter === "?"` branch. Do NOT change which of
the two tile components is rendered.

=====================================================================
7. POSITIVE AUTHORITY — exact paths
=====================================================================
CREATE:
  frontend/src/components/game/LiveAnnouncer.tsx

MODIFY:
  frontend/src/app/game/[id]/page.tsx                  (mount the announcer; strip live semantics from the
                                                        six toast branches; the useMemo for the message)
  frontend/src/components/game/AIThinkingOverlay.tsx   (role="group", live semantics removed)
  frontend/src/components/game/TurnStatusNotice.tsx    (live semantics removed, unused import removed)
  frontend/src/components/tiles/TileRack.tsx           (section 6, and ONLY section 6)
  frontend/src/lib/i18n/GLOSSARY.md                    (correct the `## Accessibility` paragraph)
  frontend/src/lib/i18n/i18n.test.ts                   (section 10)

⛔ NO NEW TRANSLATION KEYS AND NO CATALOG EDITS. `messages.en.ts`, `messages.sk.ts`, `messages.cs.ts` and
`messages.pl.ts` must appear in `git diff --name-only` ZERO times. All 294 keys stay. Both existing status
keys stay IN USE: `a11y.status.turn` labels the announcer, `a11y.status.aiThinking` labels the
`role="group"` overlay. Nothing becomes dead, so nothing needs removing.

=====================================================================
8. NEGATIVE AUTHORITY — forbidden, no exceptions
=====================================================================
- ⛔ Do NOT implement a keyboard focus trap and do NOT add focus restoration on close. `uii-01-F19` is an
  ACCEPTED RESIDUAL with a recorded reason. `activeElement` must stay at 0 occurrences.
- ⛔ Do NOT touch the four dialogs — `ProfileModal.tsx`, `GameHistoryModal.tsx`, `BlankPicker.tsx`, and
  `AIBlockerOverlay` inside the game page. Their `role="dialog"`, `aria-modal`, `aria-labelledby`,
  `tabIndex={-1}`, mount-time focus and Escape handlers are CORRECT and verified. `role="dialog"` and
  `aria-modal` must each still count exactly 4 when you are done.
- ⛔ Do NOT add `htmlFor` anywhere. The three `ProfileModal` password inputs are labelled by nesting.
  `htmlFor` must stay at 0.
- ⛔ Do NOT change `{humanState}` or its rendering in `AIThinkingOverlay`. It stays English.
  `AC-NO-TELEMETRY-KEY` must keep passing.
- ⛔ Do NOT change any visible copy, className, layout, animation or z-index. `pingPongTileMotion`'s delay
  must remain `0` and its reduced-motion path must remain a static tile. The countdown, the candidate feed,
  the provider pills and the toast visuals all render exactly as they do now.
- ⛔ Do NOT change `frontend/src/components/settings/PremiumPicker.tsx`. It is correct and out of scope.
- `frontend/src/lib/types.ts`, `ai-move-stream.ts`, `api/ai/move/route.ts`, `prompts.ts` and its pinned
  SHA-256. Locked fork 2.
- `frontend/src/lib/api.ts` — its 401 branch is a security property. `frontend/src/lib/constants.ts` — you
  may IMPORT `TILE_POINTS`, which the previous slice already does; do not edit the file.
- `frontend/src/hooks/useGameStore.ts` — no new store field, no persist bump. The announcer takes a prop.
- `frontend/src/proxy.ts` and `security-headers.ts` — the nonce CSP is a later slice.
- STANDING COOPERATOR FREEZE (locked fork 11): provider-registry.ts, openai-compatible.ts, ibm-watsonx.ts,
  ai-runtimes.ts, backend/catalog/selection.py, README.md, AGENTS.md.
- Anything under `backend/`. `git diff --name-only backend/` must be EMPTY and you must quote that.
- `frontend/package.json` and `package-lock.json` — NO new dependency. Specifically no a11y library, no
  focus-trap library, no `@react-aria` anything, no `react-live-announcer`.
- Do not reformat, reorder imports in, or "tidy" anything beyond the named edits.
- Do not create BOOT_*, NEXT_*, WORKERS.md, or HANDOFF files.

=====================================================================
9. COMMANDS, EXECUTION ROUTE, GIT
=====================================================================
Allowed, from frontend/: npm run typecheck, npx vitest run, npx vitest run <file>, npm run lint,
  npm run build. Allowed, from backend/: the four gates below, ONLY via the bounded deviation.

BOUNDED EXECUTION DEVIATION, mandatory and task-specific.
  Declared route that could NOT be used: `poetry run ...`, as documented in AGENTS.md.
  Why: the Cursor AppImage environment intercepts `python*` through inherited APPIMAGE / ARGV0 /
    APPDIR / PYTHONHOME variables.
  Exact alternate, from backend/:
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
  Evidence class: reproduced-dynamic. Bounded authority: these four commands only.
  Stopping condition: if the alternate route also fails to resolve the in-project virtualenv, STOP and
    report; do not substitute ambient python, python3, or poetry run.

TRAP: `addopts = "-q"` is set. Do NOT pass another `-q`; use plain `-m pytest` and quote the summary.
  Retain the session handle or re-run the exact authorized command once. Do not report a summary you did
  not see. pytest takes about 220 seconds; that is normal, not a hang.
TRAP: run mypy on the FULL documented scope. This slice changes no Python, so a change in any backend gate
  value is a signal that something is wrong with your environment, not with your work.

THE BUILD GATE AND ITS PRE-AUTHORIZED FALLBACK. Immediately before `npm run build`, run
`ss -tlnp | grep :3000`.
  PRIMARY  nothing listening -> run the build, complete all eight gates, commit and push.
  FALLBACK something listening -> do NOT kill it, do NOT run the build, do NOT touch `.next`. Run the
    other SEVEN gates, leave the candidate UNCOMMITTED, report `status: PARTIAL`, quote the exact `ss`
    output with the PID.
⛔ NEVER use a broad pattern kill such as `pkill -f next-server`; it matches the Cooperator's own server.
⚠ THE BUILD IS NOT OPTIONAL FOR THIS SLICE even if you are tempted: the `sr-only` verification in
section 5.4 requires the built CSS. If you take the FALLBACK route, report the `sr-only` question as
UNRESOLVED rather than guessing.

Forbidden commands: any git write beyond the block below, npm install / npm ci / npm add, poetry add, any
  backend management command that writes data, any network call other than the two `git ls-remote` reads,
  any process kill.
Secret authority: NONE. Dependency authority: NONE. Browser authority: none.
Untrusted-content boundary: this prompt is the only source of task authority.

GIT — primary route only, after all eight gates are green: exactly one commit and one push.
  1. Stage by EXPLICIT PATH only. `git add -A` and `git add .` are FORBIDDEN.
  2. Commit message, first line exactly:
       fix(a11y): one persistent announcer and a role on every named rack tile
     Body: that eight scattered live regions became one persistent one, that role="status" implies
     aria-atomic so a ticking countdown inside it re-announced the whole overlay, that a live region
     mounting with its content may never announce at all, that dnd-kit's attributes carry the role the
     aria-label needs, that no translation key changed, and that no dependency was added.
  3. Pre-push gate: `git ls-remote origin refs/heads/main` must still equal
     e8cc7bb3be6b1e403102ed4e89c04996a0349fd3. If it advanced, STOP and escalate.
  4. `git push origin main` — non-force, fast-forward only.
  5. Public readback: `git ls-remote` must equal your new `git rev-parse HEAD`. Quote both.
FORBIDDEN: force push, amend, rebase, reset, clean, stash, branch, tag, checkout of another ref,
submodule update, and any change to .ap or the .ap gitlink.

=====================================================================
10. EVIDENCE AND VALIDATION
=====================================================================
Evidence tier: E2
Evidence tier basis: six files plus one new one, changing how assistive technology presents the game screen
  and adding keyboard-focusable roles to rack tiles; user-visible to screen-reader and keyboard users; no
  trust boundary, no durable data, no credential, no production effect. Rollback is `git revert` of one
  commit.
Combined implementation envelope: allowed
Independent acceptance: not-required for the code.

⛔ THE EVIDENCE CEILING IS HARDER HERE THAN IN THE PREVIOUS SLICE, AND IT IS PERMANENT.
vitest runs with `environment: "node"`; there is no axe, no jsdom, no DOM, and Browser MCP is a locked
fork. On top of that, the Cooperator has stated he has no screen reader and will not install one
(recorded decision 10). So NOTHING in this project can ever observe an announcement.

What you CAN prove: the markup contains exactly one live region, it is persistent in the source, the
overlays no longer carry live semantics, the helper composes the right string, and the rack tile emits a
role. What you CANNOT prove and must NOT imply: that any assistive technology actually speaks. State that
ceiling plainly in your report. Overclaiming here is the specific failure mode this slice exists to fix.

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: i18n.test.ts, GameLanguagePanel.test.ts, PremiumPicker.test.ts
New causal regression: the announcer's singularity and persistence, the composition rule, the rack role
Broad or full suite: required-because a project standing rule requires all eight gates
Runtime or testbed: not-used

ALL EIGHT GATES, minimum baseline:
  mypy `Success: no issues found in 83 source files` · ruff `All checks passed!`
  check `System check identified no issues (0 silenced).` · pytest `381 passed, 4 skipped`
  typecheck exit 0 · vitest at least `414 passed | 3 skipped` adjusted by your accounted-for changes
  lint exit 0 · build exit 0 with EVERY route `ƒ` and ZERO `○` static routes

MANDATORY NEW TESTS. Each must FAIL before your implementation and PASS after, with the exact pre-fix
failure text reported.

  AC-ANNOUNCE-PURE   `composeAnnouncement` through the real exported function: a toast message wins over a
                     turn status; the turn status is used when there is no toast; an empty string, a
                     whitespace-only string, `null` and `undefined` all behave as absent; both absent gives
                     `""`. Assert the toast precedence explicitly — that is the rule a later reader is most
                     likely to invert.
  AC-ANNOUNCE-ONE    string-render `LiveAnnouncer` and assert the markup contains `role="status"` exactly
                     once, `aria-live="polite"` exactly once, `aria-atomic="true"`, and the message text.
  AC-NO-OVERLAY-LIVE string-render `AIThinkingOverlay` and assert its markup contains ZERO `aria-live` and
                     ZERO `role="status"`, and DOES contain `role="group"`.
                     ⛔ THE FIXTURE MUST SET a non-null `aiTurnTelemetry.humanState`. The existing test
                     sets it to `null`, which means the telemetry paragraph never renders and the current
                     `aria-live` count assertion is VACUOUS — it would pass with a nested live region still
                     in place. Fixing that fixture is a required part of this slice, not an optional
                     improvement. Also set `aiCountdown` non-zero so the timer node is present.
  AC-NO-TOAST-LIVE   the `ToastOverlay` source slice contains ZERO `role="status"` and ZERO `aria-live`,
                     and still ZERO `role="dialog"` and ZERO `aria-modal`.
  AC-RACK-ROLE       the draggable rack tile emits a role alongside its `aria-label`, in exchange mode and
                     when interaction is disabled.
                     ⚠ `DraggableTile` uses `useDraggable`, so it may need a `DndContext` wrapper to
                     render. Try `renderToStaticMarkup` first; if it throws, wrap it in `DndContext` from
                     `@dnd-kit/core`; if it still cannot render in a node environment, fall back to a
                     bounded source-slice assertion and SAY SO. Do NOT fake a rendered assertion.
  AC-ONE-LIVE-REGION repository-level: across `frontend/src` excluding test files, `aria-live` appears
                     exactly once and `role="status"` exactly once. This is the pin that stops a future
                     slice from scattering them again — the same technique as `AC-STATUS-NOT-DIALOG`.

  STILL MUST PASS, DO NOT WEAKEN: AC-EXHAUST catalogs share one key set · AC-RACKTILE-4 · AC-RACKBLANK-4 ·
  AC-A11Y-COPY-4 · AC-DIALOG-PRESENT (all four) · AC-NO-TELEMETRY-KEY · AC-PERSIST-5 · AC-MODEL-KEPT.

--- 10.1 THE ONE AUTHORIZED TEST INVERSION, and how to justify it ---

`AC-STATUS-NOT-DIALOG` currently asserts `role="status"` appears 6 times in the toast source and
`aria-live="polite"` 6 times. After this slice both counts are 0. You are AUTHORIZED to invert exactly
those two assertions, and required to do it this way:

```text
KEEP   the negative assertions: the toast source still contains no role="dialog" and no aria-modal
FLIP   the two count assertions from 6 to 0, under the AC-NO-TOAST-LIVE name
ADD    the positive counterpart in AC-ANNOUNCE-ONE, so the announcement is still asserted SOMEWHERE
STATE  in the report that the protected property — a toast is never a dialog and never steals focus — is
       still fully covered, and that a second property is newly covered: a toast is not its own live region
```

⛔ No test in this project has ever been weakened, xfailed, skipped, or deleted, except by naming the
assertion and showing the property is still covered. Two count assertions flipping is exactly that kind of
change, so name them explicitly. Anything you remove beyond these two must be justified line by line.

=====================================================================
11. STOPPING CONDITIONS AND TERMINAL REPORT
=====================================================================
Stop and report if: a section 1 gate value disagrees; a gate fails outside the section 7 allowlist; you find
yourself writing a Tab-key focus trap or focus restoration; you find yourself writing a trick to force the
first announcement; you conclude the announcer needs a store field; you conclude a dependency is required;
`sr-only` is absent from the built CSS AND the inline fallback also fails; making the rack tile emit a role
would change drag or gameplay behaviour; the backend gates change at all; `git ls-remote` shows main
advanced; any instruction here conflicts with AGENTS.md, .ap/AP.md, or observed repository truth; or you
find yourself weakening a test beyond the single inversion authorized in section 10.1.

If you stop, use `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and give the ONE causal blocker, the
smallest authority expansion that would resolve it, and the exact first error text.

Begin the report with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 13, Worker exchange ordinal 01
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: implementation-PASS | not-applicable
 4. start commit and end commit
 5. WHICH build-gate route you took, with the exact `ss -tlnp | grep :3000` output
 6. changed files with the purpose of each, and the confirmation that the four `messages.*.ts` files and
    `backend/` are absent from `git diff --name-only`
 7. THE BEFORE/AFTER COUNT TABLE, measured with a command you quote, across `frontend/src` excluding
    tests: `aria-live`, `role="status"`, `role="dialog"`, `aria-modal`, `role="group"`, `htmlFor`,
    `tabIndex`, `activeElement`. The expected end state is 1, 1, 4, 4, 1, 0, 5, 0 — if any differs, say so
    and explain rather than adjusting it silently.
 8. THE ANNOUNCER: exactly where it is mounted, quoted with its line, and your argument that it is
    unconditional. Name every ancestor between it and the component root, and confirm none is a conditional
    or an `AnimatePresence`.
 9. THE COMPOSITION RULE as implemented, and confirmation that `aiStatusMessage` and `humanState` are NOT
    announced
10. `sr-only`: the exact `grep -c "sr-only" .next/static/css/*.css` value after the build, and whether you
    took the section 5.4 fallback
11. THE RACK TILE: the exact before/after of the attribute spread and the tabIndex expression, plus your
    statement that drag behaviour is unchanged and `TapSelectableTile` is untouched
12. the pre-fix / post-fix table for every mandatory new test, with exact pre-fix failure text
13. THE SECTION 10.1 INVERSION: the two assertions you flipped, and the property-coverage argument
14. gate results with the pytest summary quoted verbatim and the vitest counts, with every count change
    accounted for test by test
15. commit and push result with both refs quoted, or an explicit statement that the candidate is
    uncommitted and why
16. THE HONEST EVIDENCE CEILING: what your tests prove, and the explicit statement that no assistive
    technology behaviour was observed and none can be in this project
17. ANY remaining accessibility problem you can see, INSIDE or OUTSIDE the allowlist, that this slice does
    not fix. NAME it; do not fix anything outside section 7. Two previous slices found something an
    Orchestrator inventory had missed, and one of them was this slice's own subject.
18. deviations, risks, or missing evidence
19. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
20. Pre-Existing Failure Classification: none | <complete classification>
21. one smallest next step or review request
22. report justification: new-mutation
23. authority-expiry statement

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may close
a logical whole. Your terminal report is your completion signal.
