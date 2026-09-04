> ⚠ **ORCHESTRATOR ARCHIVAL NOTE, mine and not the Worker's.** Archived verbatim. Status `PASS`,
> `Phase-qualified result: not-applicable`, D1–D8 all produced. **ACCEPTED as advisory with four
> corrections and five confirmations, recorded in `./00_notes.md` §41.** Its own `Orchestration
> critique` corrected three defects in my prompt — the plural-slot arithmetic, the impossibility of a
> byte-identical repository-gate section across sequential prompts, and the incompleteness of my
> locale-keyed-map inventory — and it found a stale sentence in `AGENTS.md` that my own `cfd1215` had
> invalidated two commits after `32312ba` wrote it, repaired in `ad49532`. Nothing below this line was
> edited.

### Report for ORCHESTRATOR_CHAT

Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 09, Worker exchange ordinal: 01
Status: PASS
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: decision-complete, repository-grounded D1–D8 planning report below
Start commit: cfd12158a6d9929892c7c7fa8989d6b921881109
End commit: cfd12158a6d9929892c7c7fa8989d6b921881109
Changed files and purpose: none — this exchange mutates nothing
Tests and validation: exact repository/AP gates reproduced; 296 text keys, 20 function keys, 21 prefixes, 14 glossary sections, and three existing `pluralSk` call sites reproduced. Static dependency, hardcoded-cardinality, catalog-import, layout, and locale-consumer searches completed. No broad frontend gate was run because this E0 exchange changed no file and the prompt supplied the measured four-gate orphan evidence. Final porcelain remained empty.
Commit/push result: not-applicable
Deviations, risks, or missing evidence: rendered overflow remains unmeasured until catalogs are wired; German-pilot human readability is an explicit assumption; detailed prompt defects are recorded under Orchestration critique.
Smallest next step: ORCHESTRATOR accepts or rejects this advisory plan, then issues the German single-file implementation prompt from D4 against the then-current exact public baseline. Acceptance itself grants no implementation authority.
Report justification: new-evidence
Logical-whole closure: not-closed
Context pressure: moderate and healthy; the full required protocol and repository evidence remained available.

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: the per-language decomposition of eight `frontend/src/lib/i18n/messages.XX.ts` interface catalogs — sequencing, per-language specification, key grouping against the existing glossary, the invariant/variant split of the eight implementation prompts, per-slice path disjointness, and the wiring dependencies discovered along the way. ⛔ Repository-grounded only: no product decision, no protocol decision, and not one translated string.
Plan disposition: advisory
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1

Planning cycle: targeted-revision
Prior planning report: ./08_report_00.md — Worker session 08 exchange 01, terminal, status BLOCKED, D1-D8 not produced
Targeted revision basis: new-repository-or-external-evidence
Changed decision boundary: three corrections to the prompt, all mine — the Slovak plural call sites are now KEY-ANCHORED instead of line-addressed; the Portuguese European-versus-Brazilian question is now a SUPPLIED FACT instead of a task that required a file another section forbade reading; and the orphan-catalog validation premise is now PROVEN across all four frontend gates instead of being three open questions
Preserved unaffected decisions: every enumeration session 08 reproduced stands and is not to be re-derived — 296 text keys across 21 prefixes, 20 function keys across 10 prefixes, exactly three plural call sites per catalog; and the ESLint finding that no rule in this project can flag an unimported module
Automatic targeted revisions used: 1

Resolved Execution Issues / Near-Misses: two compound `rg` commands initially had shell-quoting defects around embedded quote/bracket patterns. Neither command mutated state or supplied evidence. Both questions were rerun with simpler bounded patterns; residual risk: none.
Pre-Existing Failure Classification: none

## D1 — Order of the eight catalogs

| Position | Catalog | Reason |
|---|---|---|
| 1 | German (`de`) | Pilot. It combines an English-adjacent two-slot plural rule with highly visible noun-capitalization and compound-length constraints, so structural, terminology, and compact-control defects are easy to notice without beginning with the hardest plural system. This assumes German is the most readily sanity-checkable new language for the human reviewers. |
| 2 | European Portuguese (`pt`) | Exercises the zero-in-`one` rule, four-argument helper, and mandatory pt-PT/pt-BR boundary while only one prior catalog would need correction if the skeleton mishandles them. |
| 3 | Icelandic (`is`) | Exercises the structurally distinct `1/21/101` singular rule and the highest inflection/compound risk before the template propagates further. |
| 4 | Italian (`it`) | Confirms that the stabilized template handles a second four-argument helper without importing Portuguese-specific register or progressive-construction rules. |
| 5 | Dutch (`nl`) | Returns to a two-slot Germanic catalog while testing informal address, closed compounds, article/gender consistency, and resistance to copying German capitalization. |
| 6 | Danish (`da`) | Starts the closely related Nordic pair with its own common/neuter agreement and compounds; its helper remains distinct even though integer results match English. |
| 7 | Swedish (`sv`) | Follows Danish so the prompt can explicitly guard against Danish lexical or orthographic bleed while retaining the same structural skeleton. |
| 8 | Afrikaans (`af`) | Lowest structural plural risk and comparatively direct English-adjacent syntax; safest catalog to leave until the skeleton has already survived every special plural signature and the principal layout risks. |

The pilot must teach one thing: whether the prompt skeleton reliably produces a one-file, 316-key, type-complete orphan with a stable eight-term game vocabulary and concise compact-control copy without drifting into wiring.

If the Cooperator cannot meaningfully sanity-check German, swap only positions 1 and 8 with the new language the Cooperator can actually read best; do not otherwise reopen the technical order.

## D2 — Per-language specification sheets

Common to all eight:

- Copy the structural shape of `messages.sk.ts`, but take the frozen key set and parameter types from `messages.en.ts`.
- Use key and symbol anchors, never line numbers.
- The only plural-helper call sites are:
  - `a11y.rackTile` — point noun;
  - `error.throttled.minutes` — minute noun;
  - `controls.tilesSelected` — tile noun.
- A two-slot helper therefore requires six helper string arguments across the three sites; Italian and Portuguese require nine. The prompt's "nine/twelve words" arithmetic is incorrect.
- `game.toast.invalidWordHeading` is separately count-sensitive. Its reachable invalid-word list is positive and board-bounded, so a singular-versus-plural branch is sufficient for these eight catalogs and does not require a fourth helper call.
- Keep `history.showing` and the three overlay statistics noun-free or label-like where agreement with arbitrary counts would otherwise require another plural surface.
- Before filling the catalog, choose one canonical target-language term for each of tile, letter, rack, blank, bag, board, pass, and points; reuse it consistently throughout.
- Preserve these exact English tokens wherever their concepts occur: `provider`, `model`, `prompt`, `fallback`, `token`, `chat`, `API`.
- Keep runtime values such as names, model IDs, words, room codes, statuses, previews, and variant display names uninflected where declining them would corrupt or guess their form.

### Afrikaans

- Locale/file/exports: `af`; `messages.af.ts`; `afText`, `afFn`.
- Helper: `pluralAf(n: number, one: string, other: string): string`.
- `many`: not applicable.
- Register: informal singular `jy/jou`; avoid formal `u`. This matches the direct informal product voice and the existing catalogs.
- Orthography: common nouns lowercase; preserve Afrikaans diacritics; use closed compounds; apply the language's paired-negation rule to full negative clauses rather than copying English word order; keep imperative labels concise.
- Layout risk: medium. Closed compounds can lengthen settings, history, and game-status labels; flag unusually long action labels.

### Dutch

- Locale/file/exports: `nl`; `messages.nl.ts`; `nlText`, `nlFn`.
- Helper: `pluralNl(n: number, one: string, other: string): string`.
- `many`: not applicable.
- Register: informal `je/jij/jouw`; avoid formal `u/uw`. Do not mix the two systems.
- Orthography: common nouns lowercase; write compounds closed; preserve required diaereses/hyphens at vowel boundaries; capitalize initial `IJ` correctly when it begins a sentence or label; keep `de/het` choice and grammatical reference consistent.
- Layout risk: medium-high, especially closed compounds in header, settings, and history controls.

### German

- Locale/file/exports: `de`; `messages.de.ts`; `deText`, `deFn`.
- Helper: `pluralDe(n: number, one: string, other: string): string`.
- `many`: not applicable.
- Register: informal singular `du/dein`, not `Sie/Ihr`; lowercase the informal pronoun except at sentence start.
- Orthography: capitalize every noun and nominalized form; preserve umlauts and `ß`; use standard German rather than Swiss spelling; write compounds closed; maintain case, gender, and article agreement; choose one consistent label style for buttons.
- Layout risk: high. Prefer the shortest idiomatic standard UI term when alternatives are equivalent, especially for game controls, header buttons, picker labels, and table headings.

### Danish

- Locale/file/exports: `da`; `messages.da.ts`; `daText`, `daFn`.
- Helper: `pluralDa(n: number, one: string, other: string): string`.
- `many`: not applicable.
- Register: informal `du/din`, not formal `De/Deres`.
- Orthography: common nouns lowercase; preserve `æ/ø/å`; write compounds closed; maintain common/neuter gender, definite suffixes, and adjective agreement; do not import Swedish or Norwegian lookalikes.
- Layout risk: medium, mainly compound settings and game-status nouns.

### Swedish

- Locale/file/exports: `sv`; `messages.sv.ts`; `svText`, `svFn`.
- Helper: `pluralSv(n: number, one: string, other: string): string`.
- `many`: not applicable.
- Register: informal `du/din`; avoid formal or distancing `Ni/Er`.
- Orthography: common nouns lowercase; preserve `å/ä/ö`; write compounds closed; maintain common/neuter agreement and definite suffixes; do not copy Danish vocabulary merely because the structures align.
- Layout risk: medium, mainly compound labels and status text.

### Icelandic

- Locale/file/exports: `is`; `messages.is.ts`; `isText`, `isFn`.
- Helper: `pluralIs(n: number, one: string, other: string): string`.
- Rule: `one` when `i % 10 === 1 && i % 100 !== 11`; therefore 21 and 101 use the singular slot while 11 and 111 use `other`.
- `many`: not applicable.
- Register: informal singular `þú/þinn`; do not switch to formal, honorific, or plural address.
- Orthography: preserve `ð/þ/æ` and accented letters; never ASCII-normalize them in catalog copy; write compounds closed; maintain four-case, three-gender, article, adjective, and verb agreement. Phrase interpolation templates so opaque runtime values do not need guessed case endings.
- Layout risk: high. Long compounds and inflected phrases particularly threaten controls, header tooltips, history columns, and overlay statistics.

### Italian

- Locale/file/exports: `it`; `messages.it.ts`; `itText`, `itFn`.
- Helper: `pluralIt(n: number, one: string, other: string, many: string): string`.
- `many`: reachable at nonzero exact millions. Recommendation: use the same noun form as `other` at all three helper sites unless an independently justified grammatical distinction exist informal singular `tu/tuo`, never formal `Lei/Suo`; omit the subject pronoun where idiomatic while keeping second-person agreement.
- Orthography: maintain gender and number agreement; preserve accented final vowels; apply article elision before vowels and required euphonic article forms; put no space around an apostrophe; use one consistent imperative/infinitive convention for controls.
- Layout risk: medium. Elided phrases are usually compact, but descriptive settings and authentication copy can expand.

### European Portuguese

- Locale/file/exports: `pt`; `messages.pt.ts`; `ptText`, `ptFn`.
- Helper: `pluralPt(n: number, one: string, other: string, many: string): string`.
- Rule: `one` includes 0 and 1; `many` is a nonzero exact million.
- `many`: recommendation identical to `other` for all three counted nouns unless grammar genuinely demands otherwise.
- Register: European informal singular `tu` with consistent second-person verb, object, and possessive agreement. Do not mix it with Brazilian-default `você` or formal address.
- Orthographic/lexical boundary:
  - use current European Portuguese orthography and Portugal punctuation/capitalization conventions;
  - use the European progressive construction `estar a` plus infinitive for loading/in-progress copy, not the Brazilian gerund construction;
  - follow European clitic placement rather than mechanically copying Brazilian proclisis;
  - choose and freeze Portugal-specific equivalents for the source concepts user/username, password, sign-in/sign-out, registration, settings/configuration, save/saved/resume, and drag-and-drop;
  - choose Portugal board-game terminology for tile, letter, rack, blank, bag, board, pass, points, match/game, draw, and rival/opponent; do not use Brazilian defaults;
  - do not copy the English comma grouping in the fixed dictionary-count footnote; use the locale-appropriate nonbreaking grouping separator.
- Layout risk: high. Several standard Portugal computing concepts are multiword constructions, and progressive status text is longer than a gerund form.

## D3 — Key grouping

All 21 prefixes are covered exactly once. No prefix lacks a governing glossary section.

| Group | Exact prefixes | Counts | Governing glossary section | Translator must not get wrong |
|---|---|---:|---|---|
| Accessibility | `a11y` | 8 text + 1 fn | Accessibility | Preserve control purpose and dialog/status distinctions; distinguish tile, letter, and blank; retain `{letter}` and pluralized `{points}`. |
| Landing and authentication | `landing`, `auth`, `meta` | 23 text | Landing and auth | Preserve Libre Tiles, AI, Collins Scrabble Words 2019, the fixed dictionary count, and the informal voice; do not turn metadata into different product claims. |
| API errors | `error` | 10 text + 1 fn | API errors | Login failure must not reveal whether a user exists; keep session-expired, forbidden, conflict, throttling, unavailable, and generic states distinct; pluralize minutes. |
| Settings and opening draw | `settings`, `draw` | 69 text + 1 fn | Settings panels in this slice | Distinguish interface language from game variant and running from new games; retain the four current endonyms byte-identically; distinguish bag/tile/blank; preserve `{winner}` and `{loser}`. |
| Lobby and waiting room | `nav`, `play`, `queue` | 29 text + 2 fn | Lobby and waiting room | Keep empty catalog distinct from unreachable catalog; `queueFor` receives a display name, never a slug; preserve room codes and direct action voice. |
| Saved boards | `history` | 38 text + 2 fn | Saved-board history | Preserve outcome and end-reason meanings; do not translate backend enum values; preserve all pagination parameters and avoid a counted noun where agreement would be wrong. |
| Profile | `profile` | 16 text | Profile modal | Keep visible field labels and placeholders as separate keys even when identical; preserve password-security meaning and informal address. |
| Turn controls | `controls`, `board`, `rack`, `blank`, `chat` | 19 text + 1 fn | Turn chrome | Apply the canonical eight game terms; distinguish pass from exchange and blank from letter; keep compact controls concise; use the locale helper for selected tiles. |
| Game screen | `game` | 67 text + 8 fn | Game screen | Keep interface locale independent from game lexicon; cover all 12 lexicon IDs plus unknown; preserve AI/rival, pass/exchange, toast/status, and route-failure distinctions and every interpolation parameter. |
| Header and AI progress | `header`, `overlay` | 13 text + 3 fn | Header cluster and AI overlay | Distinguish give-up from logout/back; author `bestBadge` in uppercase; do not localize `{humanState}` here; use invariant label-style overlay statistics. |
| Premium pickers | `picker` | 4 text + 1 fn | Premium language pickers | Keep accessible labels separate from visible headings; preserve `{language}`; the flag-alt function remains even though current flag images are decorative. |

Prefixes with glossary section `NONE`: none.

## D4 — Invariant/variant split for eight implementation prompts

### INVARIANT sections

The following section bodies should be reused verbatim, with only the explicitly listed variant fields substituted:

1. **Persistent role, phase, profile, and Plan-to-Execution boundary**
   - WORKER role, Fresh Implementation Worker, implementation phase, explicit implementation authority, native planning mode not used, non-independent evidence, no automatic continuation after the terminal report.

2. **Single-file objective and acceptance**
   - Create exactly one complete catalog containing 296 `TextKey` entries and 20 `FnKey` entries.
   - No other file may change.
   - The catalog remains intentionally orphaned until the wiring slice.

3. **Mandatory reading**
   - Root and frontend `AGENTS.md`;
   - AP Worker protocol references;
   - `GLOSSARY.md`;
   - `messages.en.ts`, `messages.sk.ts`, `plural.ts`, and `plural.test.ts`;
   - the existing targeted locale file only when validating a prior sequential baseline;
   - Next 16's local `node_modules/next/dist/docs/01-app/02-guides/internationalization.md` before writing code, satisfying the frontend rule without web access.

4. **Repository gate procedure**
   - Exact root, AP gitlink equality, active `main`, remote-tracking state, empty porcelain, no lock/operation, and exact public-parent check before Git mutation.
   - The procedure is invariant; its expected SHA/ref values are variant fields.

5. **Exact machine-authored header placement**
   - The supplied byte-identical seven-line warning is the first content in every new file, before imports.

6. **Catalog shape**
   - Header;
   - type imports and `enFn` from `messages.en`;
   - the assigned helper import from `plural`;
   - `xxText: Record<TextKey, string>`;
   - `xxFn: { [K in FnKey]: (typeof enFn)[K] }`;
   - key order copied from `messages.en.ts`;
   - no weakening through casts, optional keys, spreading `enText`, or fallback-to-English values.

7. **Key-anchored authoring rule**
   - Address every edit/check by exported symbol and exact key, never line number.
   - Copy structure, not Slovak prose.

8. **Area-by-area execution**
   - Carry D3's eleven groups and per-group constraints verbatim.
   - Freeze a per-catalog eight-term terminology inventory before translating the 316 entries and check it again afterward.

9. **Fixed terminology**
   - Keep exactly these words in English in every catalog: `provider`, `model`, `prompt`, `fallback`, `token`, `chat`, `API`.
   - Preserve AI, Libre Tiles, Collins Scrabble Words 2019, model IDs, statuses, previews, names, words, room codes, and variant display names.

10. **Plural/count surface**
    - Exactly the three key-anchored helper call sites named in D2.
    - `game.toast.invalidWordHeading` remains a separate binary positive-count branch.
    - Use noun-free/label-like formulations for arbitrary-count functions not assigned a helper.
    - Never copy a one-character English `s` suffix.

11. **Semantic and security invariants**
    - Invalid credentials remain non-enumerating.
    - UI strings never override backend game/lexicon verdicts.
    - `game.lexicon.*` covers the frozen 12 IDs plus unknown.
    - Do not localize telemetry `{humanState}`.
    - Preserve every function parameter exactly.

12. **Negative scope**
    - No changes to `messages.en.ts`, existing catalogs, `plural.ts`, tests, wiring, `GLOSSARY.md`, settings, layout, `frontend/public`, backend, manifests, lexicons, build scripts, dependencies, lockfiles, flags, or AP.
    - No network corpus, translation service, dictionary, lexicon, provider call, secret, or environment-file access.
    - No generated word list or gameplay-rule alteration.

13. **Layout discipline**
    - Use concise idiomatic labels in `controls`, `header`, `overlay`, `picker`, history headings, and settings choice labels.
    - Do not use numeric character budgets.
    - Report any likely overflow rather than abbreviating away meaning.

14. **Validation**
    - Confirm exact header bytes and one changed path.
    - Confirm 296/20/316 keys.
    - Confirm exactly three assigned-helper calls and no wrong-locale helper.
    - Review all parameter occurrences and fixed-English tokens.
    - Run `git diff --check`, typecheck, lint, full Vitest, and build.
    - Inspect final diff and porcelain.

15. **Git authority**
    - Stage only the exact new catalog.
    - One normal commit with the assigned subject.
    - Normal non-force push only after all gates and the exact public-parent gate pass.
    - No broad add, fetch/pull unless expressly granted, reset, clean, stash, branch, tag, force, or configuration mutation.

16. **Stopping conditions**
    - Stop for baseline/ref/cleanliness disagreement, another required path, missing helper/type/key, secret risk, forbidden network/corpus need, unresolved validation failure, unauthorized Git effect, or any attempt to enter wiring.

17. **Terminal report**
    - Standard AP header and compact core;
    - exact path/key/helper evidence;
    - validation and push/public-readback evidence;
    - translation/terminology/layout risks;
    - logical whole remains not closed;
    - authority expires at report.

### VARIANT fields

Only these values change between prompts:

- locale code;
- English language name;
- file path;
- text/function export names;
- plural helper name, exact signature, category rule, and `many` recommendation;
- T–V/register decision;
- orthographic, grammatical, and language-specific layout rules from D2;
- implementation position and task identity;
- Worker-session/exchange coordinates;
- exact starting/public baseline and expected AP pin at issuance;
- exact commit subject and resulting candidate SHA.

The repository-gate section cannot literally be byte-identical across sequential prompts because each accepted commit becomes the next exact baseline. Its procedure is invariant; its immutable values are substitutions. Likewise, coordinates cannot be prefilled once for all eight.

## D5 — Layout risk and owner

Measured fixed or constrained surfaces:

- `GameControls`: mobile uses two or three equal fractional columns, fixed heights, and `whitespace-nowrap`; desktop action buttons also use nowrap and minimum widths.
- `ScorePanel`: header actions are in nonwrapping flex clusters; icon tooltips use `whitespace-nowrap`; the back button is exactly `3.08rem` wide; score-name columns have approximately five-rem minima.
- `PremiumPicker`: the trigger and list rows are panel-width constrained and explicitly truncate labels.
- `AIThinkingOverlay`: `96vw`, `max-w-lg`, `max-h-[80vh]`; status prose has `max-w-xs`, and three statistics share one horizontal row.
- Toasts/blockers use `max-w-sm`/`max-w-md`; the blank dialog is capped at `28rem`.
- Saved-board desktop history uses a full-width table inside `overflow-hidden`; mobile switches to cards.
- Settings choice grids use `minmax(132px,1fr)`, `minmax(170px,1fr)`, and fixed two-column groups.

Disposition:

- Do not impose numeric per-group character budgets: glyph widths, compounds, font weight, and breakpoints make them misleading.
- Catalog prompts own concise, idiomatic copy and must flag likely overflow.
- Catalog workers cannot perform honest rendered validation while their files are orphaned.
- The wiring slice owns making the locales reachable and resolving missing-flag/truncation behavior.
- Named final owner: the Cooperator's rendered acceptance after wiring, at:
  1. the game screen at narrow-mobile and XL widths, covering header, action strip, AI overlay, toasts, and profile/history modals;
  2. the settings screen, covering language/variant pickers and all compact option cards;
  3. the landing/play/waiting flow at narrow-mobile and desktop widths.

German and Icelandic receive priority inspection, followed by European Portuguese and Dutch.

## D6 — Per-catalog validation ladder

| Gate | Can observe the new orphan? | Evidence value |
|---|---|---|
| Structural/key audit | Yes | Confirms header placement, single path, 296/20/316, exact exports, three helper calls, and fixed parameter names. |
| `git diff --check` | Yes | Cheapest repository gate; catches whitespace errors in the exact new file. |
| `npm run typecheck` | Yes, completely | `tsconfig` includes every `.ts`; mapped types prove every text key and every function signature. |
| `npm run lint` | Yes | Parses/lints the orphan. It cannot flag that it is unimported because this project has no such rule. |
| `npx vitest run` | Only marginally | Locale/catalog assertions import only the four wired catalogs. A generic product-source scan does read every non-test `.ts/.tsx`, including an orphan, but does not validate its translations or key set. Primarily re-attests shared behavior and helpers. |
| `npm run build` | Partially | Its TypeScript/project validation can see the file; the bundler and route graph cannot because nothing imports it. The supplied probe showed an unchanged eleven-route dynamic table. |

Recommendation: run all four frontend gates for every catalog commit, plus the structural audit and `git diff --check`.

Reason: the slices are large machine-authored user-facing files; the full sequence is deterministic, the commits accumulate sequentially, and both Vitest's broad source scan and build's compilation stage can technically observe an orphan even though neither adds translation-quality evidence. This avoids inventing a special cheaper validation class for catalogs 2–8. No frontend gate is skipped. The final wiring slice must run the same four again because it changes runtime reachability and test matrices.

## D7 — Path disjointness

Claim: proven for the eight catalog implementation slices.

| Slice | Sole changed path |
|---|---|
| Afrikaans | `frontend/src/lib/i18n/messages.af.ts` |
| Dutch | `frontend/src/lib/i18n/messages.nl.ts` |
| German | `frontend/src/lib/i18n/messages.de.ts` |
| Danish | `frontend/src/lib/i18n/messages.da.ts` |
| Swedish | `frontend/src/lib/i18n/messages.sv.ts` |
| Icelandic | `frontend/src/lib/i18n/messages.is.ts` |
| Italian | `frontend/src/lib/i18n/messages.it.ts` |
| Portuguese | `frontend/src/lib/i18n/messages.pt.ts` |

Evidence:

- All paths are distinct new files.
- `GLOSSARY.md` is language-agnostic enough for these slices: it already owns UI-area semantics, the English-retained word list, counted-noun rules, and helper names. Per-language decisions travel in the prompt; no glossary pre-land is required.
- Catalog consumers use explicit imports. No catalog glob, directory import, or dynamic catalog loader exists.
- `i18n.test.ts` explicitly imports only the four wired catalogs and iterates `LOCALES`; it does not enumerate a catalog set. Its generic product-source accessibility scan does traverse every non-test TypeScript file but requires no shared edit.
- Literal `296` and `316` occur only in `AC-EXHAUST`, which counts `enText`/`enFn`, not the number of catalog files. Adding an orphan does not change them.
- Shared prerequisites `TextKey`, `FnKey`, and all eight plural helpers are already landed.
- No shared surface needs a preliminary commit.
- Because execution is sequential, each prompt must bind to the accepted predecessor SHA even though its changed path is disjoint.
- The later wiring slice deliberately reopens all twelve catalogs to add eight endonym keys; that later cost does not refute disjointness of the initial eight one-file slices.

## D8 — Wiring dependencies only

Required mutation dependencies:

- `frontend/src/lib/i18n/locales.ts`
  - Extend `LOCALES`.
  - Reassess `EXPLICIT_SEARCH_FOLDS` for non-NFD characters introduced by authored labels, particularly `æ/Æ`, `ð/Ð`, `þ/Þ`, `ß`, and possibly `ĳ/Ĳ`.

- `frontend/src/lib/i18n/translate.ts`
  - Add eight imports and eight rows in each of `TEXT` and `FN`.

- Al- Add `settings.uiLanguage.af`, `.nl`, `.de`, `.da`, `.sv`, `.is`, `.it`, `.pt`.
  - Values are endonyms and byte-identical across all catalogs.
  - This changes the frozen total from 296/20/316 to 304/20/324 during wiring.

- `frontend/src/app/settings/page.tsx`
  - Extend `localeLabelKey`.
  - Replace unconditional ``flagSrc: `/${value}.png` `` with omission for the eight locales that have no authorized flag asset.

- `frontend/src/lib/i18n/i18n.test.ts`
  - Import and exhaustively compare all eight new catalogs.
  - Update hardcoded counts to 304 text, 20 function, 324 total after endonym-key addition.
  - Extend locale acceptance/detection tests.
  - Extend every locale-indexed fixture, not only `ownName`, `HEADER_EXPECTED`, and `OVERLAY_EXPECTED`. Additional affected families include rack-tile, rack-blank, accessibility copy, catalog-unavailable copy, profile, history, pagination, settings choices, toggles, date/fallback behavior, statistics, picker copy, invalid-word headings, route failures, and end-reason coverage.
  - The separate installed-variant naming-axis expansion remains outside this wiring slice as instructed.

- `frontend/src/components/settings/PremiumPicker.test.ts`
  - Expand the endonym/search fixture and its "four locales" claims.
  - Add coverage for any new explicit search folds and for options without flags.

- `frontend/src/lib/api.test.ts`
  - Expand or reword the two "all four locales" 401-security cases; full twelve-locale coverage is needed so new invalid-credential strings remain non-enumerating and session-expired strings remain distinct.

- `frontend/src/lib/i18n/GLOSSARY.md`
  - Update the opening endonym inventory and settings table with the eight new endonym keys.

- Root `AGENTS.md`
  - Replace the four-locale/open-work statement after delivery.
  - Correct the already-stale statement that `GameLanguagePanel.tsx` lacks the eight variant-name keys.

Verification-only dependencies, with no code mutation currently justified:

- `frontend/src/lib/i18n/index.ts` already exports generic locale APIs and all eight plural helpers; it does not export individual catalogs.
- `frontend/src/app/layout.tsx` already derives metadata and `<html lang>` from generic `Locale`/`t` functions.
- `LocaleProvider.tsx`, `useGameStore.ts`, `api.ts`, `GameHistoryPanel.tsx`, and `ProfileModal.tsx` consume `Locale` generically.
- `GameLanguagePanel.tsx` already contains all twelve variant-name keys and conditionally omits absent flag sources.
- `frontend/public/` remains unchanged.

Orchestration critique:

MEASURED

- Section 4.2's plural-surface arithmetic is wrong: three two-slot calls expose six string-form slots, while three three-slot calls expose nine—not nine and twelve.
- D4 cannot make the complete repository-gate sections byte-identical in issued sequential prompts: exact baseline/public-ref values necessarily advance after each accepted commit. Only the procedure/template can be invariant.
- D8's "three locale-keyed maps" inventory is incomplete. Static use analysis found numerous additional locale-indexed fixture families in `i18n.test.ts`.
- The interface-language picker currently constructs a flag path for every `LOCALES` value. Adding eight locales without changing that line would request eight forbidden/missing assets.
- `GameLanguagePanel.tsx` already has all twelve `VARIANT_NAME_KEYS` and conditionally omits missing flags. The contrary statements in the task context and root `AGENTS.md` are stale.
- `index.ts` and `layout.tsx` are dependencies to verify, but current generic code gives no reason to mutate either.
- Vitest is not absolutely blind to an orphan catalog: `collectProductSource` recursively reads every non-test `.ts/.tsx`. It does not validate catalog completeness or language copy, but a catalog containing its searched accessibility-source literals could affect that test.
- The instruction to read only named portions of `i18n.test.ts` conflicts with D7/D8's requirement to enumerate all test consumers and locale-keyed fixtures. I resolved this toward the stated goal by using bounded mechanical name/usage searches plus one small source-scan excerpt, not a whole-file read.
- The supplied statement that every gate "fully checks" an orphan overstates Vitest and the bundle portion of build; only `tsc --noEmit` mechanically proves complete keys and function signatures.
- Eight sequential one-file exchanges remain the correct accountability shape. A single multi-language Worker would save prompt overhead but violate the Cooperator's chosen one-report-per-language boundary. The reusable D4 skeleton makes subsequent prompt issuance an instantiation rather than new reconnaissance.

LEAD

- German is the best technical pilot, but its human-sanity-check advantage depends on unprovided reviewer fluency. If that assumption is false, the Cooperator should identify the new language they can read best before implementation prompt 1.
- Exact rendered overflow and the final non-NFD fold set depend on strings that do not yet exist; static planning cannot close either question.
- The supplied successful build with a valid orphan does not by itself provide a negative malformed-orphan build probe. The plan conservatively treats build as an observing gate because project compilation uses the encompassing TypeScript configuration.

Enumeration widened: static searches cannot reach future authored lexical choices, font-specific rendered widths, browser line breaking, or dynamically constructed consumers absent from the current tree. Backend and Meta were intentionally outside authority. No catalog glob or dynamic loader was found in the authorized frontend surface.

Authority expired: this terminal PASS report ends all planning authority for Worker session 09 exchange 01. No implementation, wiring, Git mutation, publication, or further planning is authorized.
