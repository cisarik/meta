You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 11
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: R1 — the two premium language pickers the Cooperator asked for
Implementation authority: explicit
Independence required: no
Reasoning recommendation: high. Basis — this is the only NEW INTERACTIVE COMPONENT in this whole. It
  needs a combobox with keyboard navigation, diacritic-insensitive search, and the first images this
  codebase has ever had. It is genuinely new UI, not string extraction.
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

  git rev-parse HEAD                     -> 8f440221b757bc142cb26391875c1361492da419
  git rev-parse HEAD:.ap                 -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                         -> ## main...origin/main
  git status --porcelain=v1              -> EMPTY
  git ls-remote origin refs/heads/main   -> 8f440221b757bc142cb26391875c1361492da419

STOP if any value disagrees.

=====================================================================
2. MANDATORY READING, IN THIS ORDER
=====================================================================
1. /home/agile/Projects/libretiles/AGENTS.md
2. /home/agile/Projects/libretiles/frontend/AGENTS.md — this Next.js version has breaking changes versus
   your training data. The installed docs ARE present at `frontend/node_modules/next/dist/docs/`.
   ⛔ Read `frontend/node_modules/next/dist/docs/01-app/03-api-reference/02-components/image.md` BEFORE
   deciding how to render the flag images, and quote the sentence that decided your choice.
   ⛔ ALSO KNOW: an App Router `page.tsx` may export ONLY the Next.js-enumerated set. Any other named
   export from a page file is a `tsc` error. `settings/page.tsx` is a page file.
3. .ap/AP.md sections 5, 8, 9, 12, 18, 19
4. .ap/AP_WORKER.md
5. frontend/src/lib/premiumSurface.ts — the shared premium chrome. The new control MUST use it; the
   Cooperator asked for eye candy matching the existing panels, "not a plain white input".
6. frontend/src/app/settings/page.tsx — `SettingsPanel` at ~86, `InterfaceLanguagePanel` at ~350-402
7. frontend/src/components/settings/GameLanguagePanel.tsx — IN FULL, and its test
8. frontend/src/lib/i18n/messages.en.ts and messages.sk.ts — the shape you extend

=====================================================================
3. GOAL — ONE COHERENT OUTCOME
=====================================================================
Replace the two 2x2 button grids in Settings with the two premium searchable pickers the Cooperator
described, and ship the first images this codebase has ever contained.

His words, recorded in the handout: *"a flag image left of the language name, a search input with
diacritic-insensitive autocomplete ('cestina' must match 'Čeština'), and an arrow at the input edge that
opens the dropdown. TWO of them — one for the interface locale, one for the game variant. He wants them
eye candy, matching the existing premium chrome, not a plain white input."*

This is **closure condition 2** of this logical whole. It is the last feature work; everything after it is
accessibility and backend residuals.

=====================================================================
4. WHAT ALREADY EXISTS — do not rebuild any of it
=====================================================================
```text
frontend/public/en.png sk.png cs.png hu.png pl.png    committed at 61c9f09, 48x32 each, 5230 B total,
                                                      currently referenced NOWHERE
settings.uiLanguage.{en,sk,cs,pl}                     the four ENDONYMS, byte-identical in all four
                                                      catalogs: English · Slovenčina · Čeština · Polski
settings.gameVariant.{english,slovak,czech,polish}    translated EXONYMS per locale
GameLanguagePanel.variantDisplayName(variant, t)      resolves a slug to a display name with a
                                                      display_name fallback; /play imports it
VariantSummary { slug, display_name, language_code, readiness }   readiness is "playable" | "unavailable"
PREMIUM_PANEL_STYLE, handlePremiumSurfacePointer      the pointer-reactive gold chrome
```

⛔ `hu.png` exists and Hungarian is NOT a shipped interface locale and NOT a playable variant. It must
stay unreferenced. Do not add a Hungarian row to either picker.

=====================================================================
5. THE COMPONENT CONTRACT — one shared component, two instances
=====================================================================
CREATE `frontend/src/components/settings/PremiumPicker.tsx`, a client component used twice.

```ts
export interface PremiumPickerOption {
  value: string;
  label: string;              // already-resolved, already-localized display text
  flagSrc?: string;           // e.g. "/sk.png"; omitted when an option has no flag
  disabled?: boolean;         // an unavailable game variant
}

export function PremiumPicker(props: {
  id: string;                       // needed for label/listbox wiring
  options: readonly PremiumPickerOption[];
  value: string;
  onChange: (value: string) => void;
  searchPlaceholder: string;
  emptyText: string;                // shown when a query matches nothing
  ariaLabel: string;
}): JSX.Element;
```

BEHAVIOUR, and every point is required:

```text
closed state   shows the SELECTED option: its flag image then its label, with a trailing arrow glyph at
               the input's right edge. Clicking anywhere on it, or the arrow, opens the list.
open state     a text input for the query, plus the filtered option list below it. The input receives
               focus when the list opens.
filtering      diacritic-insensitive AND case-insensitive, both directions. See section 6.
selection      click an option, or press Enter on the highlighted one, calls onChange and closes.
keyboard       ArrowDown / ArrowUp move the highlight, Home / End jump to first / last, Enter selects the
               highlighted option, Escape closes WITHOUT changing the value and returns focus to the
               trigger. Tab must not be hijacked.
disabled       a `disabled` option is rendered, visibly muted, NOT selectable by click or Enter, and
               SKIPPED by arrow navigation.
outside click  closes without changing the value.
```

ACCESSIBILITY, and this matters because the product currently has ZERO `aria-label` and ZERO `role`:

```text
trigger   role="combobox"  aria-expanded  aria-controls={listboxId}  aria-label={props.ariaLabel}
list      role="listbox"   id={listboxId}
option    role="option"    aria-selected  aria-disabled for a disabled row
active    aria-activedescendant on the input, pointing at the highlighted option's id
images    every flag <img> or <Image> needs alt text — see section 7.4. These are the FIRST images in
          this codebase, so there is no existing convention to follow; establish a correct one.
```

⛔ Do NOT install a combobox library, a headless-UI package, or a fuzzy-search package. The prompt
forbids any new dependency and this control is ~150 lines of ordinary React.

=====================================================================
6. THE DIACRITIC FOLD — the one algorithmic decision, and it has a trap
=====================================================================
Add to `frontend/src/lib/i18n/locales.ts`:

```ts
export function foldForSearch(value: string): string {
  return value.normalize("NFD").replace(/\p{Diacritic}/gu, "").toLowerCase();
}
```

Filter with `foldForSearch(option.label).includes(foldForSearch(query))`.

⚠ **THE TRAP, and you must handle it rather than discover it.** NFD decomposition plus diacritic
stripping does NOT fold Polish `ł`, because `ł` (U+0142) is a distinct letter with a stroke, not a base
letter plus a combining mark. So `foldForSearch("Polski")` is fine, but a user typing `lot` would not
match a hypothetical `Łot`. For THIS product the four labels are `English`, `Slovenčina`, `Čeština`,
`Polski` and the variant exonyms, none of which begins with `ł` — so the gap is not reachable today.

Handle it honestly rather than silently: add an explicit character map for the letters NFD cannot fold,
at minimum `ł -> l` and `Ł -> l`, applied before or after the NFD pass. Slovak, Czech and Polish also
use `đ`/`Đ` and `ø` in loanwords; adding those costs nothing. Then say in your report which characters
NFD handles and which needed the explicit map, and verify with the test in section 10.

MANDATORY behaviour, all four of which the Cooperator's own example implies:
```text
"cestina"  matches "Čeština"       the example he gave verbatim
"CESTINA"  matches "Čeština"       case-insensitive too
"Čeština"  matches "Čeština"       an accented query still matches
"slovencina" matches "Slovenčina"
"polski"   matches "Polski"
""         matches everything      an empty query must not hide the list
```

=====================================================================
7. EXACT WIRING AND STRINGS
=====================================================================
--- 7.1 the interface-locale picker, in settings/page.tsx ---
Replace the `grid grid-cols-2` block inside `InterfaceLanguagePanel` with one `PremiumPicker`.
  options: the four `LOCALES` in the order en, sk, cs, pl
  label:   `t("settings.uiLanguage.<locale>")` — the ENDONYMS, unchanged
  flagSrc: `/en.png` `/sk.png` `/cs.png` `/pl.png`
  value:   `useLocale()`
  onChange: `setUiLocale(v)` followed by `router.refresh()`, exactly as the current buttons do
Keep the surrounding `SettingsPanel`, its title and description keys, and `className="xl:col-span-2"`.

--- 7.2 the game-variant picker, in GameLanguagePanel.tsx ---
Replace its `grid grid-cols-2` block with one `PremiumPicker`.
  options: `variants` in the order the server returns them — do NOT re-sort
  label:   `variantDisplayName(variant, t)` — reuse the existing export, do not duplicate it
  flagSrc: map slug to flag: english -> /en.png, slovak -> /sk.png, czech -> /cs.png, polish -> /pl.png.
           A slug with no mapping gets NO flag rather than a wrong one or a placeholder.
  disabled: `variant.readiness !== "playable"`
  value:   `selected`;  onChange: `onSelect`
⛔ `variantDisplayName` MUST remain exported with its current signature — `frontend/src/app/play/page.tsx`
imports it for the `uii-01-F14` queue label. Breaking it would silently reintroduce a corrected defect.

--- 7.3 FOUR new copy keys ---
key                          en                        sk                      cs                      pl
picker.search                Search                    Hľadať                  Hledat                  Szukaj
picker.noMatch               No match                   Žiadna zhoda            Žádná shoda             Brak dopasowania
picker.uiLanguageLabel       Interface language         Jazyk rozhrania         Jazyk rozhraní          Język interfejsu
picker.gameVariantLabel      Game variant               Variant hry             Varianta hry            Wariant gry

`picker.uiLanguageLabel` and `picker.gameVariantLabel` are the `ariaLabel` values. They intentionally
duplicate the text of `settings.uiLanguage.title` and `settings.gameVariant.title`: the visible panel
heading and a control's accessible name are different roles, and a later designer may reword the heading
without silently renaming what a screen reader announces. Do not collapse them.

--- 7.4 FOUR new alt-text keys, parameterized ---
picker.flagAlt   params { language: string }
  en (p) => `${p.language} flag`
  sk (p) => `Vlajka: ${p.language}`
  cs (p) => `Vlajka: ${p.language}`
  pl (p) => `Flaga: ${p.language}`

⚠ Colon-label again in the Slavic locales, for the established reason: `"Slovenská vlajka"` would need
the adjective to agree with each language name in gender and number, and the names arrive as nominative
labels. A colon-label is inert. Fourth use of this pattern in this whole.

⚠ ALSO CONSIDER, and state your choice with a reason: a flag next to its own label may be PURELY
DECORATIVE, in which case `alt=""` plus `aria-hidden="true"` is MORE correct than a redundant name,
because a screen reader would otherwise announce "Vlajka: Slovenčina, Slovenčina". The prompt authors
`picker.flagAlt` so you have a real string if you need one — but if you conclude the images are decorative
and use `alt=""`, that is ACCEPTABLE and arguably better. Say which you chose and why. If you choose
`alt=""`, still add the four keys to the catalogs so the decision is reversible without a new slice, and
say that you did.

--- 7.5 GLOSSARY.md ---
Add all FIVE new keys — four plain (`picker.search`, `picker.noMatch`,
`picker.uiLanguageLabel`, `picker.gameVariantLabel`) plus one parameterized (`picker.flagAlt`). A first
draft of this prompt said eight; the Orchestrator's own key-count check corrected it before issuing. If
any prose number here disagrees with the enumerated table, THE TABLE WINS. Record that `picker.uiLanguageLabel` / `picker.gameVariantLabel` deliberately
duplicate the panel titles because a heading and an accessible name are different roles, and record your
`alt` decision from 7.4 with its reason.

=====================================================================
8. POSITIVE AUTHORITY — exact paths
=====================================================================
CREATE:
  frontend/src/components/settings/PremiumPicker.tsx
  frontend/src/components/settings/PremiumPicker.test.ts
MODIFY:
  frontend/src/app/settings/page.tsx
  frontend/src/components/settings/GameLanguagePanel.tsx
  frontend/src/components/settings/GameLanguagePanel.test.ts
  frontend/src/lib/i18n/locales.ts                  (foldForSearch only)
  frontend/src/lib/i18n/messages.en.ts
  frontend/src/lib/i18n/messages.sk.ts
  frontend/src/lib/i18n/messages.cs.ts
  frontend/src/lib/i18n/messages.pl.ts
  frontend/src/lib/i18n/GLOSSARY.md
  frontend/src/lib/i18n/i18n.test.ts

⚠ `GameLanguagePanel.test.ts` is on the list because replacing the button grid will change what it
asserts. You may UPDATE it to assert the new control's behaviour. You may NOT weaken it: whatever it
proves today about readiness and `display_name` fallback must still be proved. If you delete an
assertion, say exactly which and why the property is still covered.

⚠ vitest runs with `environment: "node"` and nothing in the suite renders a component. So
`PremiumPicker.test.ts` must test the PURE parts — `foldForSearch`, and any filter/highlight helper you
extract — rather than pretending to test the DOM. Extract the filtering and the arrow-navigation
index arithmetic into pure exported functions so they ARE testable. That is the whole reason to extract
them.

=====================================================================
9. NEGATIVE AUTHORITY — forbidden, no exceptions
=====================================================================
- NO NEW DEPENDENCY. Not a combobox library, not a headless UI kit, not a fuzzy matcher, not a flag-icon
  package. `frontend/package.json` and `package-lock.json` are forbidden. `audit-02` found three high
  findings in this dependency tree the first time anyone looked; a picker is not worth new supply chain.
- Do NOT reference `frontend/public/hu.png`. Hungarian is neither a shipped interface locale nor a
  playable variant. It stays unreferenced.
- Do NOT change `variantDisplayName`'s name, signature, or export. `app/play/page.tsx` imports it for the
  `uii-01-F14` fix.
- Do NOT re-sort the `variants` array. Server order is deliberate.
- Do NOT touch `frontend/src/lib/i18n/plural.ts`, `translate.ts`, `LocaleProvider.tsx`, `index.ts`, or
  `messages.*` beyond adding the eight keys. `locales.ts` gains `foldForSearch` and NOTHING else.
- Do NOT add a named export to `settings/page.tsx`. It is a page file; see section 2.
- Do NOT touch any other settings panel — board surface, shiny, premium look, the rival panel, the two
  choice grids. They are correct and already localized.
- `frontend/src/lib/api.ts` — its 401 branch is a security property. `frontend/src/lib/constants.ts` —
  TW/DW/TL/DL is the BOARD. `frontend/src/proxy.ts` and `security-headers.ts` — the nonce CSP is a later
  slice.
- `frontend/src/lib/types.ts`, `ai-move-stream.ts`, `api/ai/move/route.ts`, `prompts.ts` and its pinned
  SHA-256. Locked fork 2 plus the telemetry deferral. `{humanState}` stays English and
  `AC-NO-TELEMETRY-KEY` must keep passing.
- STANDING COOPERATOR FREEZE (locked fork 11): provider-registry.ts, openai-compatible.ts,
  ibm-watsonx.ts, ai-runtimes.ts, backend/catalog/selection.py, README.md, AGENTS.md.
- Anything under `backend/`. Django localization is a later slice.
- Do NOT add aria-label, role or alt ANYWHERE OUTSIDE the new picker and its two call sites. The
  product-wide accessibility pass is the NEXT slice and mixing it in would make both diffs unreviewable.
  Inside the picker they are required; outside it they are forbidden.
- Do not bump the persist version. Do not reformat or "tidy" beyond the named edits.
- Do not create BOOT_*, NEXT_*, WORKERS.md, or HANDOFF files.

=====================================================================
10. EVIDENCE AND VALIDATION
=====================================================================
Evidence tier: E2
Evidence tier basis: a new interactive component with keyboard handling replacing two working controls,
  plus the first images in the codebase; user-visible and the last feature work in this whole. No trust
  boundary, no durable data, no credential, no production effect. Rollback is `git revert` of one commit.
Combined implementation envelope: allowed
Independent acceptance: not-required for the code. ⚠ RENDERED acceptance is Cooperator-owned and is a
  CLOSURE CONDITION for this whole — he must accept these two controls himself, so expect a manual batch.
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: GameLanguagePanel.test.ts, i18n.test.ts
New causal regression: the diacritic fold and the pure filter/navigation helpers
Broad or full suite: required-because a project standing rule requires all eight gates
Runtime or testbed: not-used

ALL EIGHT GATES, minimum baseline:
  mypy `Success: no issues found in 83 source files` · ruff `All checks passed!`
  check `System check identified no issues (0 silenced).` · pytest `381 passed, 4 skipped`
  typecheck exit 0 · vitest at least `398 passed | 3 skipped` plus your new tests
  lint exit 0 · build exit 0 with EVERY route `ƒ` and ZERO `○` static routes

MANDATORY NEW TESTS. Each must FAIL before your implementation and PASS after, with the exact pre-fix
failure text reported.

  AC-FOLD          `foldForSearch` folds every diacritic these four locales use. Assert at minimum:
                   `Čeština` -> `cestina`, `Slovenčina` -> `slovencina`, `Poľština` -> `polstina`,
                   `Angličtina` -> `anglictina`, `Słowacki` -> `slowacki`, `Polski` -> `polski`,
                   `Zamietnuté` -> `zamietnute`. And assert the `ł` case EXPLICITLY: `Ł` folds to `l`,
                   which plain NFD does NOT do — that assertion is the point of the test.
  AC-FOLD-MATCH    The Cooperator's own example and its variants: `cestina`, `CESTINA`, `Čeština` and
                   `ceSTIna` all match `Čeština`; `slovencina` matches `Slovenčina`; an empty query
                   matches every option; `xyz` matches none.
  AC-PICKER-FILTER The pure filter helper returns the expected option subsets for those queries over the
                   real four-endonym list.
  AC-PICKER-NAV    The pure arrow-navigation helper SKIPS disabled options in both directions, wraps or
                   clamps consistently at both ends (state which you chose), and Home / End land on the
                   first / last ENABLED option. This is the part most likely to be subtly wrong and it is
                   the reason the arithmetic must be a pure function.
  AC-VARIANT-PANEL GameLanguagePanel still proves what it proved before: an `unavailable` variant is not
                   selectable, and an unknown slug falls back to `display_name`.
  AC-EXHAUST4 and AC-NO-TELEMETRY-KEY  ALREADY EXIST and must keep passing. Do not weaken either.

⛔ No test in this project has ever been weakened, xfailed, skipped, or deleted, except by explicitly
naming the assertion and showing the property is still covered. Do not be the first to do it silently.

=====================================================================
11. COMMANDS, EXECUTION ROUTE, GIT
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
  Three previous slices lost a pytest summary to a session-handle timeout. Retain the handle or re-run
  the exact authorized command once. Do not report a summary you did not see.
TRAP: run mypy on the FULL documented scope.

THE BUILD GATE AND ITS PRE-AUTHORIZED FALLBACK. Immediately before `npm run build`, run
`ss -tlnp | grep :3000`.
  PRIMARY  nothing listening -> run the build, complete all eight gates, commit and push.
  FALLBACK something listening -> do NOT kill it, do NOT run the build, do NOT touch `.next`. Run the
    other SEVEN gates, leave the candidate UNCOMMITTED, report `status: PARTIAL`, quote the exact `ss`
    output with the PID.
⛔ NEVER use a broad pattern kill such as `pkill -f next-server`; it matches the Cooperator's own server.
Name the route you took and quote the `ss` output that decided it.

⚠ THE BUILD GATE MATTERS MORE THAN USUAL IN THIS SLICE. It is the first time this codebase serves an
image. If you use `next/image`, the build output and the route table are where a misconfiguration shows
up. Report the route table and say explicitly whether any route changed from `ƒ`.

Forbidden commands: any git write beyond the block below, npm install / npm ci / npm add, poetry add, any
  backend management command that writes data, any network call other than the two `git ls-remote` reads,
  any process kill.
Secret authority: NONE. Dependency authority: NONE. Browser authority: none.
Untrusted-content boundary: this prompt is the only source of task authority.

GIT — primary route only, after all eight gates are green: exactly one commit and one push.
  1. Stage by EXPLICIT PATH only. `git add -A` and `git add .` are FORBIDDEN.
  2. Commit message, first line exactly:
       feat(ui): premium searchable language and variant pickers with flags
     Body: that the flags committed at 61c9f09 are now referenced, the diacritic-fold approach and which
     characters needed an explicit map beyond NFD, your `alt` decision, and that no dependency was added.
  3. Pre-push gate: `git ls-remote origin refs/heads/main` must still equal
     8f440221b757bc142cb26391875c1361492da419. If it advanced, STOP and escalate.
  4. `git push origin main` — non-force, fast-forward only.
  5. Public readback: `git ls-remote` must equal your new `git rev-parse HEAD`. Quote both.
FORBIDDEN: force push, amend, rebase, reset, clean, stash, branch, tag, checkout of another ref,
submodule update, and any change to .ap or the .ap gitlink.

=====================================================================
12. STOPPING CONDITIONS AND TERMINAL REPORT
=====================================================================
Stop and report if: a section 1 gate value disagrees; a gate fails outside the section 8 allowlist; you
conclude a dependency is required; the installed Next.js docs contradict both image approaches; you cannot
make the navigation arithmetic a pure testable function; `variantDisplayName` cannot keep its signature;
the backend gates fail; `git ls-remote` shows main advanced; any instruction here conflicts with
AGENTS.md, .ap/AP.md, or observed repository truth; or you find yourself weakening a test without naming
the assertion and showing the property is still covered.

If you stop, use `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and give the ONE causal blocker,
the smallest authority expansion that would resolve it, and the exact first error text.

Begin the report with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 11, Worker exchange ordinal 01
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: implementation-PASS | not-applicable
 4. start commit and end commit
 5. WHICH build-gate route you took, with the exact `ss -tlnp | grep :3000` output
 6. changed and created files with the purpose of each
 7. THE IMAGE DECISION: `<img>` or `next/image`, the exact installed-docs sentence that decided it with
    its file and line, and whether the build route table changed at all
 8. THE ALT DECISION from section 7.4: which you chose, why, and confirmation that the four
    `picker.flagAlt` keys are in all four catalogs either way
 9. THE DIACRITIC FOLD: which characters NFD handles, which needed the explicit map, and the exact
    behaviour for the Cooperator's `cestina` -> `Čeština` example
10. THE PURE HELPERS you extracted and their exported names, plus which wrap-or-clamp behaviour you chose
    for arrow navigation at the ends
11. the accessibility attributes the new control emits, listed exactly
12. whether `GameLanguagePanel.test.ts` lost any assertion; if so, which and why the property is still
    covered
13. the pre-fix / post-fix table for every mandatory new test, with exact pre-fix failure text
14. gate results with the pytest summary quoted verbatim and the vitest counts. Quote only a summary you
    actually saw.
15. commit and push result with both refs quoted, or an explicit statement that the candidate is
    uncommitted and why
16. any string or layout you believe is wrong or will overflow — NAME it, do not change it. Say how the
    closed state behaves at a narrow viewport with the longest label.
17. ANYTHING about this control you believe the Cooperator will want changed after he sees it. You are the
    only one who has read the finished markup; say what you would question.
18. deviations, risks, or missing evidence
19. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
20. Pre-Existing Failure Classification: none | <complete classification>
21. one smallest next step or review request
22. report justification: new-mutation
23. authority-expiry statement

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may
close a logical whole. Your terminal report is your completion signal.
