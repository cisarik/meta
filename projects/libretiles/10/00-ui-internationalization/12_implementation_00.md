You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 12
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: S11 — accessible names, dialog semantics and status regions across the product
Implementation authority: explicit
Independence required: no
Reasoning recommendation: high. Basis — this touches nine files and requires one genuine distinction to be
  drawn correctly throughout: which overlays are DIALOGS and which are STATUS REGIONS. Getting that
  backwards would make screen-reader output worse than the current absence of markup.
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

  git rev-parse HEAD                     -> c3f75e32533b6c4abd38d2c006f46c2c59eaa68e
  git rev-parse HEAD:.ap                 -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                         -> ## main...origin/main
  git status --porcelain=v1              -> EMPTY
  git ls-remote origin refs/heads/main   -> c3f75e32533b6c4abd38d2c006f46c2c59eaa68e

STOP if any value disagrees.

=====================================================================
2. MANDATORY READING, IN THIS ORDER
=====================================================================
1. /home/agile/Projects/libretiles/AGENTS.md
2. /home/agile/Projects/libretiles/frontend/AGENTS.md
3. .ap/AP.md sections 5, 8, 9, 12, 18, 19
4. .ap/AP_WORKER.md
5. frontend/src/components/settings/PremiumPicker.tsx — the ONLY accessible control in this product
   today. It is your house style: read how it wires `role`, `aria-expanded`, `aria-controls`,
   `aria-activedescendant`, `aria-selected`, `aria-disabled` and `alt=""`. Match it.
6. frontend/src/lib/i18n/GLOSSARY.md
7. frontend/src/components/game/ScorePanel.tsx — `IconTooltip` at ~22, `SettingsButton` at ~146,
   `HeaderMiniButton` at ~212, and the header cluster at ~353-425
8. frontend/src/components/game/ProfileModal.tsx and GameHistoryModal.tsx and BlankPicker.tsx
9. frontend/src/app/game/[id]/page.tsx lines 180-400 — `ToastView` and the AI blocker modal
10. frontend/src/components/game/AIThinkingOverlay.tsx lines 200-240
11. frontend/src/components/tiles/TileRack.tsx lines 110-160

=====================================================================
3. GOAL — ONE COHERENT OUTCOME
=====================================================================
Give every icon-only control an accessible name, give every real dialog dialog semantics with Escape, give
every transient announcement status semantics, and label the three unlabelled inputs.

`uii-01-F02` recorded that this product has ZERO `aria-label`, `role`, `alt`, `tabIndex` and `sr-only`.
That was true until slice R1, which introduced the first seven — all inside `PremiumPicker`. This slice
brings the rest of the product up to the standard R1 set.

=====================================================================
4. MEASURED SCOPE — you do not need to rediscover any of this
=====================================================================
Taken by the Orchestrator at `c3f75e3`. Verify anything you doubt, but this is the map.

```text
INPUTS — enumerated, every one in the product
  app/page.tsx:172   username   NOT in a label, no aria-label   -> NEEDS a name
  app/page.tsx:179   password   NOT in a label, no aria-label   -> NEEDS a name
  ChatPanel.tsx:53              NOT in a label, no aria-label   -> NEEDS a name
  ProfileModal.tsx:257,270,283  NESTED INSIDE their <label>     -> ALREADY CORRECT, do not touch
  PremiumPicker.tsx:191         has aria-label                  -> ALREADY CORRECT

⛔ The three ProfileModal fields are ALREADY correctly labelled by implicit association — the input is a
   descendant of its `<label>`, which is valid per the HTML spec and needs no `htmlFor`. An earlier
   Orchestrator draft called them unlabelled; that was a false conclusion from `htmlFor` returning zero.
   Do NOT add `htmlFor`/`id` pairs to them. Adding redundant labelling is a regression, not a fix.

ICON-ONLY CONTROLS — their labels ALREADY EXIST, localized, as props
  ScorePanel.tsx:355   the `↩` back button: glyph + a hover-only IconTooltip
  ScorePanel.tsx:365   HeaderMiniButton iconOnly, profile 👤
  ScorePanel.tsx:409   HeaderMiniButton iconOnly, settings
  ScorePanel.tsx:414   HeaderMiniButton iconOnly, settings
  ScorePanel.tsx:419   HeaderMiniButton iconOnly, games 🗂️
  ScorePanel.tsx:179   SettingsButton iconOnly
  A tooltip is NOT an accessible name: IconTooltip renders a `pointer-events-none` absolutely-positioned
  span revealed by `group-hover`. This is therefore the cheapest high-value fix in the slice — the name
  exists and is translated, it is simply not attached.
```

=====================================================================
5. ⛔ THE ONE DISTINCTION YOU MUST GET RIGHT: DIALOG vs STATUS
=====================================================================
Six overlays use `fixed inset-0`. They are NOT all dialogs, and treating them alike would make screen-reader
output actively worse than today's silence.

```text
REAL DIALOGS — the user must act, focus belongs inside, Escape must dismiss
  ProfileModal.tsx:121        role="dialog"  aria-modal="true"  aria-labelledby=<its heading id>
  GameHistoryModal.tsx:61     same
  BlankPicker.tsx:30          same — the user MUST choose a letter for the blank
  game/[id]/page.tsx aiBlockerModal (~z-[70])   same

TRANSIENT ANNOUNCEMENTS — the user must NOT be interrupted, focus must NOT move, Escape is meaningless
  game/[id]/page.tsx ToastView (~z-[60])      role="status"  aria-live="polite"
  AIThinkingOverlay.tsx (~z-[55])             role="status"  aria-live="polite"
```

⛔ Do NOT give a toast `role="dialog"`, do NOT give it `aria-modal`, and do NOT move focus to it. A toast
that steals focus mid-turn is a worse experience than an unannounced one. Conversely do NOT leave
`BlankPicker` as a bare div: it blocks the game until the player picks a letter, so it is a dialog.

`aria-live="polite"` and NOT `assertive`: these announcements accompany a turn the player initiated, so they
must queue behind whatever the screen reader is already saying. `assertive` would interrupt.

⚠ `AIThinkingOverlay` ALREADY has `aria-live` in two places — check what is there before adding a third.
If a nested `aria-live` region would now sit inside an outer one, that is a defect: nested live regions
produce duplicate or dropped announcements. Resolve it, and say in your report what you found and did.

--- 5.1 Escape and focus: what IS and IS NOT in scope ---
FOR EACH of the four dialogs:
  - `Escape` closes it, using the same shape as `settings/page.tsx:552` which already does this;
  - focus moves INTO the dialog when it opens — the primary control, or the dialog container with
    `tabIndex={-1}`;
  - `aria-modal="true"` tells assistive technology to constrain to the dialog.

⛔ A FULL KEYBOARD FOCUS TRAP IS EXPLICITLY OUT OF SCOPE. Do not implement one. Reason, stated so it is a
decision and not an omission: a correct trap needs a focusable-element query, Tab and Shift+Tab
interception, and focus restoration on close, in four components with different internal structures, and
getting it subtly wrong strands a keyboard user with no escape. `aria-modal` plus Escape plus initial focus
delivers most of the value at a fraction of the risk. The Orchestrator records the missing trap as an
accepted residual. If you find yourself writing a Tab handler, STOP and report instead.

=====================================================================
6. EXACT STRING CONTENT — authored by the ORCHESTRATOR, use VERBATIM
=====================================================================
NINE new keys: eight plain and one parameterized. Counted programmatically from the table below. If any
prose number in this prompt disagrees with the enumerated table, THE TABLE WINS.

--- 6.1 area `a11y` — accessible names for the three unlabelled inputs ---
key                    en                  sk                       cs                       pl
a11y.chatInput         Chat message        Správa do chatu          Zpráva do chatu          Wiadomość na chat

For the two auth inputs REUSE the existing `auth.field.username` and `auth.field.password`. They are
already the placeholder text, they are already localized, and a name identical to the placeholder is
correct here — the visible hint and the accessible name genuinely say the same thing.

--- 6.2 area `a11y` — dialog names, used as fallbacks only ---
For the four dialogs, prefer `aria-labelledby` pointing at the heading that is ALREADY on screen. Add an
`id` to that heading. Only if a dialog has no suitable visible heading, use one of these as `aria-label`:

key                     en                   sk                   cs                   pl
a11y.dialog.profile     Profile              Profil               Profil               Profil
a11y.dialog.games       Saved games          Uložené partie       Uložené partie       Zapisane partie
a11y.dialog.blank       Choose a letter      Vyber písmeno        Vyber písmeno        Wybierz literę
a11y.dialog.rival       Rival unavailable    Súper nedostupný     Soupeř nedostupný    Rywal niedostępny

⚠ Prefer `aria-labelledby` and say for each of the four dialogs which mechanism you used and why. A visible
heading is a better name than a duplicated invisible one, because it cannot drift out of sync with what the
user sees. These four keys exist so you are never forced to invent a string; if all four dialogs end up
using `aria-labelledby`, ADD THE KEYS TO THE CATALOGS ANYWAY so the choice is reversible, and say that you
did.

--- 6.3 area `a11y` — status regions ---
key                     en                   sk                    cs                    pl
a11y.status.turn        Turn status          Stav ťahu             Stav tahu             Status ruchu
a11y.status.aiThinking  AI progress          Priebeh AI            Průběh AI             Postęp AI

Use these as `aria-label` on the two status regions so a screen reader can identify the region it is
announcing from.

--- 6.4 area `a11y` — the rack tile, ONE parameterized key, and it uses the plural functions ---
a11y.rackTile   params { letter: string; points: number }
  en (p) => `Tile ${p.letter}, ${p.points} ${pluralEn(p.points, "point", "points")}`
  sk (p) => `Písmeno ${p.letter}, ${p.points} ${pluralSk(p.points, "bod", "body", "bodov")}`
  cs (p) => `Kámen ${p.letter}, ${p.points} ${pluralCs(p.points, "bod", "body", "bodů")}`
  pl (p) => `Płytka ${p.letter}, ${p.points} ${pluralPl(p.points, "punkt", "punkty", "punktów")}`

a11y.rackBlank  plain key — a blank tile has no letter and no points until it is resolved
key             en           sk        cs        pl
a11y.rackBlank  Blank tile   Žolík     Žolík     Blank

⚠ THREE THINGS ABOUT THIS KEY.
  1. It is the FIFTH use of the plural functions in this whole and the first for `bod`. The glossary fixes
     the three Slovak forms as `1 bod / 2 body / 5 bodov`; use them exactly. `2 bodov` reads as broken
     Slovak.
  2. Czech uses `Kámen` and Polish uses `Płytka` for the tile, per the glossary. Slovak uses `Písmeno`.
     Do NOT harmonize Czech to Slovak — that distinction is evidenced from the Česká asociace Scrabble
     rules and is deliberate.
  3. A BLANK gets `a11y.rackBlank`, never `a11y.rackTile` with a `?` letter. A žolík has no letter until it
     is resolved, which is the whole reason `písmeno` and `žolík` are separate words in this product.

--- 6.5 GLOSSARY.md ---
Add all nine keys. Record the dialog-versus-status distinction from section 5 in one line, record that the
keyboard focus trap is deliberately out of scope, and record that `a11y.rackTile` uses the three-form
plural while `a11y.rackBlank` is separate because a blank has no letter.

=====================================================================
7. POSITIVE AUTHORITY — exact paths
=====================================================================
MODIFY:
  frontend/src/app/page.tsx                              (two input names only)
  frontend/src/app/game/[id]/page.tsx                    (ToastView status role; aiBlockerModal dialog)
  frontend/src/components/game/ScorePanel.tsx            (icon-only names; turn-status region if present)
  frontend/src/components/game/ProfileModal.tsx          (dialog semantics + Escape ONLY — its inputs are
                                                          already correct, do not touch them)
  frontend/src/components/game/GameHistoryModal.tsx      (dialog semantics + Escape)
  frontend/src/components/game/BlankPicker.tsx           (dialog semantics + Escape)
  frontend/src/components/game/ChatPanel.tsx             (input name)
  frontend/src/components/game/AIThinkingOverlay.tsx     (status region; resolve the nested aria-live)
  frontend/src/components/game/TurnStatusNotice.tsx       (status region if it is the turn announcer)
  frontend/src/components/tiles/TileRack.tsx             (tile accessible names)
  frontend/src/lib/i18n/messages.en.ts
  frontend/src/lib/i18n/messages.sk.ts
  frontend/src/lib/i18n/messages.cs.ts
  frontend/src/lib/i18n/messages.pl.ts
  frontend/src/lib/i18n/GLOSSARY.md
  frontend/src/lib/i18n/i18n.test.ts

No file is created and none is deleted. If a gate fails in a file NOT on this list, STOP and report it.

⚠ This is the widest allowlist in this whole — ten component files. That is deliberate: accessibility
attributes are one-or-two-line additions per site and splitting them across slices would multiply review
passes over the same markup. But it also means DISCIPLINE: in each of those ten files, change ONLY
accessibility attributes, ids needed for `aria-labelledby`, Escape handlers, and the initial-focus target.
Do NOT localize a string, restyle anything, or refactor while you are there. Any other change is out of
scope even if it looks like an improvement.

=====================================================================
8. NEGATIVE AUTHORITY — forbidden, no exceptions
=====================================================================
- ⛔ Do NOT implement a keyboard focus trap. Section 5.1. If you start writing a Tab handler, STOP.
- ⛔ Do NOT add `htmlFor`/`id` to the three ProfileModal password fields. They are already correctly
  labelled by nesting. Redundant labelling is a regression.
- ⛔ Do NOT give any toast or progress overlay `role="dialog"` or `aria-modal`, and do not move focus to
  one.
- ⛔ Do NOT change `PremiumPicker.tsx`. It is already correct and is your reference, not your subject.
- Do NOT change any visible copy, any className, any layout, or any animation. In particular
  `AIThinkingOverlay`'s `pingPongTileMotion` delay must remain `0` and its reduced-motion path must remain
  a static tile.
- Do NOT change `{humanState}` in `AIThinkingOverlay`. It stays English pending the enum-keyed telemetry
  slice, and `AC-NO-TELEMETRY-KEY` must keep passing.
- `frontend/src/lib/types.ts`, `ai-move-stream.ts`, `api/ai/move/route.ts`, `prompts.ts` and its pinned
  SHA-256. Locked fork 2.
- `frontend/src/lib/api.ts` — its 401 branch is a security property. `frontend/src/lib/constants.ts` —
  TW/DW/TL/DL is the BOARD. `frontend/src/proxy.ts` and `security-headers.ts` — the nonce CSP is a later
  slice.
- `frontend/src/app/settings/page.tsx`, `play/page.tsx`, `waiting/[id]/page.tsx`, `draw/[id]/page.tsx`,
  `GameHistoryPanel.tsx`, `GameControls.tsx`, `Board.tsx`, `settings/GameLanguagePanel.tsx`. Not in scope.
  ⚠ If you believe one of them has a genuinely unlabelled icon-only control that section 4 missed, NAME it
  in the report as a finding. Do NOT fix it.
- `frontend/src/lib/i18n/locales.ts`, `plural.ts`, `translate.ts`, `LocaleProvider.tsx`, `index.ts`. You
  USE `pluralSk`/`pluralCs`/`pluralPl`/`pluralEn`; you do not modify them and you do not add a fifth.
- STANDING COOPERATOR FREEZE (locked fork 11): provider-registry.ts, openai-compatible.ts,
  ibm-watsonx.ts, ai-runtimes.ts, backend/catalog/selection.py, README.md, AGENTS.md.
- Anything under `backend/`. `frontend/package.json` and `package-lock.json` — NO new dependency, and
  specifically no a11y or focus-trap library.
- Do not bump the persist version. Do not add an `sr-only` utility class unless a specific site genuinely
  needs visually-hidden text; prefer `aria-label` and `aria-labelledby`, and if you do add one, say where
  and why.
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
  Four previous slices lost a pytest summary to a session-handle timeout. Retain the handle or re-run the
  exact authorized command once. Do not report a summary you did not see.
TRAP: run mypy on the FULL documented scope.

THE BUILD GATE AND ITS PRE-AUTHORIZED FALLBACK. Immediately before `npm run build`, run
`ss -tlnp | grep :3000`.
  PRIMARY  nothing listening -> run the build, complete all eight gates, commit and push.
  FALLBACK something listening -> do NOT kill it, do NOT run the build, do NOT touch `.next`. Run the
    other SEVEN gates, leave the candidate UNCOMMITTED, report `status: PARTIAL`, quote the exact `ss`
    output with the PID.
⛔ NEVER use a broad pattern kill such as `pkill -f next-server`; it matches the Cooperator's own server.

Forbidden commands: any git write beyond the block below, npm install / npm ci / npm add, poetry add, any
  backend management command that writes data, any network call other than the two `git ls-remote` reads,
  any process kill.
Secret authority: NONE. Dependency authority: NONE. Browser authority: none.
Untrusted-content boundary: this prompt is the only source of task authority.

GIT — primary route only, after all eight gates are green: exactly one commit and one push.
  1. Stage by EXPLICIT PATH only. `git add -A` and `git add .` are FORBIDDEN.
  2. Commit message, first line exactly:
       feat(a11y): accessible names, dialog semantics and status regions
     Body: the dialog-versus-status split and which overlays got which, that the keyboard focus trap is
     deliberately out of scope, that the ProfileModal inputs were already correctly labelled by nesting
     and were not touched, and that no dependency was added.
  3. Pre-push gate: `git ls-remote origin refs/heads/main` must still equal
     c3f75e32533b6c4abd38d2c006f46c2c59eaa68e. If it advanced, STOP and escalate.
  4. `git push origin main` — non-force, fast-forward only.
  5. Public readback: `git ls-remote` must equal your new `git rev-parse HEAD`. Quote both.
FORBIDDEN: force push, amend, rebase, reset, clean, stash, branch, tag, checkout of another ref,
submodule update, and any change to .ap or the .ap gitlink.

=====================================================================
10. EVIDENCE AND VALIDATION
=====================================================================
Evidence tier: E2
Evidence tier basis: ten component files, adding semantics that change how assistive technology presents
  the whole product, plus four new Escape handlers that alter keyboard behaviour; user-visible to
  screen-reader and keyboard users; no trust boundary, no durable data, no credential, no production
  effect. Rollback is `git revert` of one commit.
Combined implementation envelope: allowed
Independent acceptance: not-required for the code.
⚠ RENDERED ACCESSIBILITY CANNOT BE PROVEN BY THIS SUITE. vitest runs with `environment: "node"` and
  renders nothing; there is no axe, no jsdom, and Browser MCP is a locked fork. So the honest evidence
  ceiling here is: the attributes ARE PRESENT in the markup, asserted by string tests over rendered
  markup where a component can be string-rendered, plus Cooperator keyboard observation. State that
  ceiling in your report rather than implying an audit happened. This is the same blindness that let
  `uii-01-F04` ship, and naming it is the required behaviour.
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: i18n.test.ts, GameLanguagePanel.test.ts, PremiumPicker.test.ts
New causal regression: the rack-tile plural naming and the dialog/status attribute presence
Broad or full suite: required-because a project standing rule requires all eight gates
Runtime or testbed: not-used

ALL EIGHT GATES, minimum baseline:
  mypy `Success: no issues found in 83 source files` · ruff `All checks passed!`
  check `System check identified no issues (0 silenced).` · pytest `381 passed, 4 skipped`
  typecheck exit 0 · vitest at least `405 passed | 3 skipped` plus your new tests
  lint exit 0 · build exit 0 with EVERY route `ƒ` and ZERO `○` static routes

MANDATORY NEW TESTS. Each must FAIL before your implementation and PASS after, with the exact pre-fix
failure text reported.

  AC-RACKTILE-4     `a11y.rackTile` renders correctly in all four locales for points = 1, 2, 4, 5 and 10.
                    Assert the exact Slovak strings `Písmeno A, 1 bod`, `Písmeno A, 2 body` and
                    `Písmeno A, 5 bodov`. Assert the Czech uses `Kámen` and NOT `Písmeno`, and the Polish
                    uses `Płytka`. This is the fifth live use of the plural helpers and the first for
                    `bod`; `2 bodov` would be broken Slovak and the test must forbid it.
  AC-RACKBLANK-4    `a11y.rackBlank` renders the authored string in all four locales and is NOT equal to
                    any `a11y.rackTile` output. A blank must never be announced as a lettered tile.
  AC-A11Y-COPY-4    The remaining `a11y.*` keys render the exact authored string in all four locales.
  AC-DIALOG-PRESENT For every component you can string-render in a node environment, assert that the
                    dialog markup carries `role="dialog"` and `aria-modal="true"` and either an
                    `aria-labelledby` whose target id exists in the same markup or an `aria-label`.
                    ⚠ If a component cannot be string-rendered without a DOM, say so explicitly and do
                    NOT fake the assertion. Name which components you could and could not cover.
  AC-STATUS-NOT-DIALOG  A NEGATIVE test: the toast and AI-progress markup must NOT contain
                    `role="dialog"` or `aria-modal`. This pins the section 5 distinction so a later
                    slice cannot "improve" a toast into a modal.
  AC-EXHAUST4 and AC-NO-TELEMETRY-KEY  ALREADY EXIST and must keep passing. Do not weaken either.

⛔ No test in this project has ever been weakened, xfailed, skipped, or deleted, except by naming the
assertion and showing the property is still covered. Do not be the first to do it silently.

=====================================================================
11. STOPPING CONDITIONS AND TERMINAL REPORT
=====================================================================
Stop and report if: a section 1 gate value disagrees; a gate fails outside the section 7 allowlist; you find
yourself writing a Tab-key focus trap; a dialog has no visible heading AND no suitable key; resolving the
nested `aria-live` in `AIThinkingOverlay` would require changing visible behaviour; you conclude a
dependency is required; the backend gates fail; `git ls-remote` shows main advanced; any instruction here
conflicts with AGENTS.md, .ap/AP.md, or observed repository truth; or you find yourself weakening a test
without naming the assertion.

If you stop, use `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and give the ONE causal blocker,
the smallest authority expansion that would resolve it, and the exact first error text.

Begin the report with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 12, Worker exchange ordinal 01
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: implementation-PASS | not-applicable
 4. start commit and end commit
 5. WHICH build-gate route you took, with the exact `ss -tlnp | grep :3000` output
 6. changed files with the purpose of each
 7. THE DIALOG/STATUS TABLE: every one of the six overlays, which treatment it got, and one sentence of
    why. If you classified any overlay differently from section 5, say so and justify it — you have read
    the markup and the Orchestrator has not.
 8. THE NESTED `aria-live` in AIThinkingOverlay: what was already there, what you found, what you did
 9. FOR EACH of the four dialogs: `aria-labelledby` or `aria-label`, and why
10. confirmation that the three ProfileModal inputs were NOT touched and are labelled by nesting
11. confirmation that NO focus trap was implemented, and what focus behaviour the dialogs DO have
12. the pre-fix / post-fix table for every mandatory new test, with exact pre-fix failure text
13. WHICH components you could string-render for AC-DIALOG-PRESENT and which you could not, with the
    honest evidence ceiling stated
14. gate results with the pytest summary quoted verbatim and the vitest counts. Quote only a summary you
    actually saw.
15. commit and push result with both refs quoted, or an explicit statement that the candidate is
    uncommitted and why
16. ANY icon-only control, unlabelled input, or overlay OUTSIDE the section 7 allowlist that you believe
    still lacks an accessible name. NAME it as a finding; do NOT fix it. The Orchestrator's section 4 map
    is a claim, and five previous slices found something an Orchestrator inventory had missed.
17. deviations, risks, or missing evidence
18. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
19. Pre-Existing Failure Classification: none | <complete classification>
20. one smallest next step or review request
21. report justification: new-mutation
22. authority-expiry statement

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may
close a logical whole. Your terminal report is your completion signal.
