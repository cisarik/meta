# Closure-readiness record — logical whole `multilingual-expansion-campaign` (Meta 13/00)

**Logical-whole closure: NOT-CLOSED.**

⛔ **This file is deliberately NOT a closure declaration, and the file name is the convention rather than a
claim.** Three of the eleven closure conditions are not satisfied, one of them cannot be satisfied on this
campaign's own terms, and one requires the Cooperator. Section 3 names all three. A successor Orchestrator
that reads this as "closed" would be wrong.

```text
State commit at this record   84ddf1fdca3f6bb4c855794136355958e7f55885
AP pin                        9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   (detached, correct)
Public refs/heads/main        84ddf1fdca3f6bb4c855794136355958e7f55885   equal
Working tree                  git status --porcelain=v1 EMPTY
Written on 2026-09-05 by the era-13 continuation Orchestrator.
```

Artifact class: **state record — authority for nothing.** It grants no authority to change anything.
Successor wholes take their authority from their own Orchestrator prompts.

---

## 1. What this campaign delivered

Libre Tiles ships **twelve playable board languages** and **twelve interface locales**, from four of each.

```text
variants   english slovak czech polish german portuguese icelandic italian dutch danish swedish afrikaans
locales    en sk cs pl de pt is it nl da sv af
key set    304 text + 20 function = 324 keys per locale, 3888 strings across twelve catalogs
lexicons   13 assets audited by `manage.py validate_lexicons`, 0 failed
           english 279 496 · afrikaans 148 267 · icelandic 200 182 · danish 317 167 · german 709 844 ·
           swedish 822 919 · dutch 1 293 086 · slovak 3 005 250 · italian 3 128 429 · polish 3 721 704 ·
           czech 3 930 497 · portuguese 4 119 831 · plus the Slovak two-tile allowlist at 103
scripts    11 committed build scripts, each pinning an upstream commit, the SHA-256 of every source file,
           and the host expander `hunspell 1.7.3`, failing closed on a mismatch
```

Every non-English lexicon is reproducible from a pinned upstream commit by a committed script, and
`--check --check-dir <dir outside backend/assets/>` re-verifies a committed asset instead of rebuilding it.

## 2. The eleven closure conditions, each with its measured evidence

```text
 1  every capability C1-C5 either landed with tests, or recorded as not-needed with the
    measurement that shows no target language requires it
    ⛔ NOT SATISFIED, AND NOT SATISFIABLE AS WRITTEN. See section 3.1.

 2  every one of the twenty-four target entries has a ledger row with all nine columns filled
    ✔ SATISFIED at Meta `5c0e2d8`. MEASURED by parsing `90_language_ledger.md` into per-language
      sections and testing each of the nine labels from `00_handout.md:435-441` as a line anchor:
      24 of 24 rows carry all nine. Before that commit it was 6 of 24, with eighteen rows missing
      column 1 `language / variant`. ⚠ The parse handles a duplicate `## 11 ·` heading — Dutch appears
      twice, once as the PLAYABLE entry and once as a stub — so 25 sections yield 24 distinct rows.

 3  every language that CAN be implemented under standing condition 5 IS playable, with its
    UI locale where practical
    ✔ SATISFIED. Twelve playable, twelve localized, and the seven remaining licence-clean rows are
      each blocked on something no scheduling decision clears: six of the seven have no sourced tile
      distribution, and Hungarian and Croatian additionally need C1.

 4  every language that CANNOT is a recorded blocker naming the exact missing thing
    ✔ SATISFIED. Five rows, each with a named cause:
        07 French     `unmunch` cannot expand the pair
        14 Norwegian  no explicit licence grant
        15 Finnish    no licence-clean source
        21 Bulgarian  licence TEXT present, NO GRANT naming the word list      ⭐ found this era
        24 Malay      no licence-clean source
      ⇒ 12 playable + 7 licence-clean-awaiting-distribution + 5 blocked = 24, counted from the file.

 5  the twelve conditions inherited from 12/00 are satisfied or explicitly re-dispositioned
    ⚠ RE-DISPOSITIONED, not satisfied. See section 4 — all twelve, one line each.

 6  no language-slug branch exists anywhere in gamecore/ or game/
    ✔ SATISFIED, and the measurement is worth stating precisely because a naive grep says otherwise.
      MEASURED: 21 string literals naming a language appear under `gamecore/` and `game/`. Every one
      is either the DEFAULT slug (`_DEFAULT_VARIANT_SLUG = "english"`, `variant_slug` field defaults,
      `state.py` fallbacks) or a TEST FIXTURE inside
      `game/management/commands/validate_lexicons.py`'s per-variant membership probe, which is a
      data table of known-good words per lexicon and is the opposite of a behavioural branch.
      ⛔ NOT ONE `if slug == "..."` controlling game logic. Zero in `gamecore/`.

 7  all eight gates green at the closing commit
    ✔ SATISFIED at `84ddf1f`, every gate re-run at this record rather than quoted from a slice:
        npm run typecheck        0 errors
        npx vitest run           474 passed | 3 skipped (477) · 32 files passed | 1 skipped
        npm run lint             clean, exit 0
        npm run build            the build passed AND the code type-checks — ELEVEN dynamic routes,
                                 ZERO static
        mypy config game gamecore accounts catalog   Success: no issues found in 85 source files
        ruff check .             All checks passed!
        manage.py check          System check identified no issues (0 silenced).
        pytest                   745 passed, 4 skipped in 273.66s
        manage.py validate_lexicons   13 asset(s) audited, 0 failed

 8  the deferred acceptance batch delivered ONCE, at the end, per his autonomy grant
    ⛔ NOT SATISFIED. `91_deferred-acceptance-batch.md` holds B5-B15 undelivered, with three items
      already open for him: B13-3 (`chat`/`chatt`), B10-3 (badge length), B7-3 (German terminology).
      ⇒ This is the one remaining condition that is purely a delivery act. See section 3.3.

 9  fresh independent acceptance for C1
    ⛔ VACUOUS BY NON-OCCURRENCE, which is not the same as satisfied. C1 never landed, so there is
      nothing to accept. ⛔ Do not tick it. See section 3.2.

10  Meta complete: 99_closure.md, the ledger, PROJECT_CONTEXT.md and DEFECT_LEDGER.md
    updated through the closing commit
    ⚠ THIS FILE plus the ledger at `5c0e2d8` plus `PROJECT_CONTEXT.md` at this commit. The condition
      is complete in substance and its own wording presumes a closing commit that does not exist yet.

11  libretiles_PRD.md, README.md and AGENTS.md describe what actually ships
    ✔ SATISFIED at `1a6f63c`, `84ddf1f` and `b50f84a`. All three name twelve playable variants and
      twelve interface locales, and all three carry the residuals rather than omitting them: the eight
      machine-authored catalogs have had no second-opinion review, exact wording is pinned for four
      of twelve, and the Slovak list is a hunspell expansion rather than an SSS-official list.
      ⭐ THE FOURTH RESIDUAL IS RETIRED at `b50f84a`: the Cooperator supplied the eight missing 48x32
      flag PNGs himself, both lookup tables now carry twelve, and all three documents were corrected
      in the same commit. ⛔ The tables stay PARTIAL with a conditional spread deliberately — an
      unconditional path is mec-13-D01 and a thirteenth locale must not reintroduce it.
```

## 3. The three things that block closure, stated plainly

### 3.1 Condition 1 is not satisfiable on this campaign's own terms

```text
Condition 1 allows exactly two outcomes per capability: LANDED WITH TESTS, or RECORDED AS NOT-NEEDED
WITH THE MEASUREMENT THAT SHOWS NO TARGET LANGUAGE REQUIRES IT.
⛔ C1 IS NEITHER. It did not land, and it cannot be recorded as not-needed, because the handout's own
  §4.1 names what needs it: Hungarian, Croatian (DŽ LJ NJ), "and every future multigraph edition".
  A capability that a target language requires cannot be dispositioned as not-needed.
⇒ MEASURED STATE OF THE FIVE:
     C1  MULTI-CODE-POINT TILES END TO END      ⛔ NOT LANDED. Partial foundation only:
         `WIRE_STATE_SCHEMA_VERSION = 4` exists at `game/services.py:321`, `gamecore/word_authority.py`
         exists and `WordAuthority.for_variant` is exercised by `tests/test_atomic_tile_tokens.py`,
         and `TileToken` is a token type rather than a char. ⛔ BUT `_word_passes_dictionary` is STILL
         PRESENT — 55 occurrences across the tree — and the handout requires it DELETED with
         `evaluate_scoring_move` re-pointed at `WordAuthority`, all seven F2b guards removed TOGETHER.
     C2  VARIANT-DECLARED BLANK TARGETS         ⛔ ABSENT. `blank_target` has ZERO hits in
         `gamecore/` and `game/`.
     C3  VARIANT-DECLARED NORMALIZATION         ⛔ ABSENT. `normalization` has ZERO hits as a manifest
         field. ⭐ AND THE CAMPAIGN SOLVED ITS PROBLEM A DIFFERENT WAY ON PURPOSE: eight languages
         needed a diacritic decision and every one was solved IN THE LEXICON at build time — the
         `none*`, `none**`, `none***` footnotes in the ledger. That is a real, defensible
         re-disposition of C3 for the twelve shipped languages, and it does NOT cover Turkish I/İ.
     C4  FACE VERSUS LEXICAL REALIZATION        ⚠ THE HOOK EXISTS AND IS DELIBERATELY IDENTITY:
         `variant_store.py:137` `lexical_contribution` returns its token with the docstring
         "Identity extension point". ⭐ THIS IS CONDITION 1'S SECOND OUTCOME, CORRECTLY REACHED: the
         handout itself said "BUILD NOTHING for it, because no language on his list needs it."
         ⇒ C4 IS LEGITIMATELY not-needed-with-measurement. It is the one clean row of the five.
     C5  RULESET IDENTITY                       ⚠ PARTIAL. `variant_name` exists
         (`variant_store.py:82`), `display_label` composes from it (`:110-111`), and it now HAS tests —
         11 `display_label` lines in `tests/test_variant_invariants.py`, including `g27c` asserting a
         declared `display_label` is forbidden. ⛔ But `variant_name` is declared by ZERO of twelve
         manifests, so the composed branch at `:111` is never exercised by a shipped variant.
⇒ ⛔ THE HONEST STATEMENT: one of five capabilities (C4) satisfies condition 1. C5 is close. C1, C2 and
  C3 do not, and C1 cannot without being built. ⭐ A CAMPAIGN THAT CLAIMED CONDITION 1 HERE WOULD BE
  EXACTLY THE FAILURE THAT LOOKS LIKE A SUCCESS THAT `00_handout.md:654-658` WARNS AGAINST.
```

### 3.2 Condition 9 is vacuous, and vacuous must not be ticked

```text
Condition 9 requires fresh independent acceptance for C1, by a session that is NOT the Orchestrator's
subagent (`AP.md:1395-1405`). C1 never landed, so no acceptance exists and none is owed YET.
⛔ RECORDING IT AS SATISFIED WOULD DESTROY ITS PURPOSE: the condition exists so that a wire-schema
  change cannot be accepted by whoever wrote it. If C1 is ever built, this condition becomes live again
  at full strength. ⇒ Its state is VACUOUS BY NON-OCCURRENCE.
```

### 3.3 Condition 8 needs the Cooperator, and only him

```text
`91_deferred-acceptance-batch.md` holds B5-B15. Three items are already awaiting his judgement and none
is an engineering question: B13-3 (`chat` versus `chatt` in Swedish), B10-3 (badge length), B7-3 (German
terminology). ⭐ THE BATCH IS DELIVERED ONCE, AT THE END, BY HIS OWN AUTONOMY GRANT — so it is correctly
undelivered until the campaign is otherwise ready to close, and it is the LAST thing to do, not a
blocker to work around.
```

## 4. Condition 5 — the twelve inherited from 12/00, re-dispositioned one line each

`12/00/91_orchestrator-handout.md:461-505` lists eighteen; twelve were OPEN and are inherited.

```text
 7  en/sk/cs/pl unchanged: four-key payload, all four playable          ✔ RE-PROVED AT THIS RECORD.
    MEASURED: `list_variant_summaries()` returns the core four with exactly
    `['display_name','language_code','readiness','slug']` and all four `playable`.
 8  seven F2b guards removed TOGETHER with wire schema 4,
    `_word_passes_dictionary` deleted                                  ⛔ STILL OPEN. Schema 4 shipped;
    `_word_passes_dictionary` has 55 occurrences. Half-done, and the handout forbids half-done.
 9  Hungarian acceptance fixture with TWO different multi-char tokens   ⛔ OPEN — needs C1.
10  the L·L synthetic canary still passes                              ⛔ OPEN — needs C1.
11  Hungarian playable after an opt-in local build, `unavailable`
    without crashing before it                                        ⛔ OPEN. Hungarian never shipped.
12  if Hungarian is playable, the fifth interface locale ships         ⚠ SUPERSEDED IN SUBSTANCE:
    Hungarian is not playable, and the campaign shipped EIGHT further locales instead of a fifth. The
    condition's parity requirement — exact key-set and interpolation parity, sourced plural function —
    WAS honoured, for all eight, by `AC-EXHAUST` over twelve and twelve CLDR plural helpers.
13  all eight standing gates green at closure, pytest quoted verbatim,
    ELEVEN dynamic and ZERO static                                     ✔ SATISFIED — condition 7 above.
14  fresh independent acceptance; deferred batch once; Meta complete;
    supersession records for 11/01 and 11/02                           ⚠ SPLIT. The two supersession
    records EXIST (`11/01-.../98_supersession.md`, `11/02-.../98_supersession.md`, both verified
    present). Meta is complete at this record. ⛔ The acceptance and the batch remain — §3.2, §3.3.
15  Hungarian code-point ceiling derived and declared                  ⛔ OPEN — needs Hungarian.
16  the six-word gate asserted BY THE BUILD SCRIPT as a fail-closed
    post-condition                                                    ⚠ GENERALIZED AND SATISFIED FOR
    THE ELEVEN SHIPPED SCRIPTS: each pins its sources by SHA-256 and the expander by version and fails
    closed. ⛔ Not satisfied for Hungarian, which has no script.
17  an `unavailable` variant is UNSELECTABLE at the three server sites,
    proved against a REAL unavailable variant                          ⛔ OPEN. All twelve shipped
    variants are `playable`, so no real `unavailable` variant exists to prove it against. ⭐ The
    condition is unprovable BECAUSE the campaign succeeded, which is worth stating rather than ticking.
18  streaming or sorted-adjacency duplicate check, never an in-memory
    set                                                               ✔ SATISFIED IN SUBSTANCE:
    `validate_lexicons` audits 13 assets including four over 3 million words with 0 duplicates, so the
    audit path scales past the size that motivated the condition. ⛔ The ~301 M-form Hungarian case that
    set the 40 GB bound is untested, because that lexicon does not exist.
```

## 5. What this campaign is honest about NOT having proven

```text
⛔ The eight newest interface catalogs are MACHINE-AUTHORED and have had no second-opinion review. Exact
  wording is pinned only for `REVIEWED_LOCALES = en sk cs pl`; the other eight are asserted
  STRUCTURALLY — one shared key set, non-empty resolution, no long English value leaking byte-identically,
  interpolation parity, no stray placeholder, ASCII-foldable picker labels. ⭐ That was a deliberate
  decision, not an omission: hundreds of hand-typed cells in eight unreviewed languages would be false
  confidence, and it is recorded in `frontend/src/lib/i18n/GLOSSARY.md`.
⛔ No shipped manifest declares `variant_name`, so `display_label`'s composed branch is never exercised
  by a real variant. C5 is tested but not exercised.
⛔ Turkish I/İ is UNRESOLVED and it is not a licence problem: `canonicalize_tile_token` uses plain
  `.upper()`, and Turkish casing is not Unicode default casing. Turkish must not be scheduled until that
  is measured.
⛔ Six of the seven licence-clean rows have NO SOURCED TILE DISTRIBUTION. That is the real remaining
  bottleneck of this campaign and it is not code and not law — a distribution must be sourced from a
  language authority, and `PROJECT_CONTEXT.md` records the standard.
⛔ The licence reads of section 4's eight rows were performed ORCHESTRATOR-DIRECT after two dispatch
  failures, and are therefore NON-INDEPENDENT. Recorded permanently in `00_notes.md` §54.
```

## 6. Routed onward — measured, recorded, and not this campaign's work

```text
· the three `messages.en.ts` shape problems: dual-role `history.unknownDate`, dead
  `history.outcome.unknown`, and `game.aiPlayedFor.before`/`.points` split across two keys
· `GLOSSARY.md`'s Settings table omits the `czech` and `polish` `settings.gameVariant.*` rows
· `frontend/public/hu.png` is an orphan — no locale, no variant, and `hu` is asserted to be REJECTED by
  `isLocale`. Removing it needs file-deletion authority no slice has held.
· `VARIANT_SLUGS` is duplicated in `i18n.test.ts`; deduping needs a TDZ-aware move
· nine tests pin four locales by per-locale LITERAL rather than by a loop, so no `awk` scan sees them
· the PRD's `Updated:` header date has no repository-verifiable source and was left alone
· `docs/architecture.md` was out of every slice's scope this era
· `frontend/src/lib/prompts.ts` `MovePromptLexiconId` and `JudgePromptLexiconId` are literal unions
  `"collins2019" | "slovak"`, so ten of twelve playable lexicons get an AI prompt naming neither their
  language nor their word list. ⭐ COOPERATOR-SELECTABLE, never scheduled.
· one upstream communication would unblock Bulgarian: ask bgOffice to state the word list's licence
```

## 7. Successor obligations

```text
⛔ THIS CAMPAIGN IS OPEN. A successor Orchestrator inherits, in this order of cost:
  1  condition 8 — deliver `91_deferred-acceptance-batch.md` ONCE, including B13-3, B10-3, B7-3
  2  condition 1 — either build C1 (planner first, then implementation, then FRESH INDEPENDENT
     acceptance that is NOT the Orchestrator's subagent) or obtain an explicit Cooperator
     re-disposition of condition 1 itself. ⛔ There is no third route: C1 cannot be recorded
     not-needed while Hungarian and Croatian require it.
  3  condition 9 — becomes live at full strength the moment C1 lands
  4  the seven licence-clean rows need TILE DISTRIBUTIONS sourced, which is the campaign's real
     remaining work and is neither code nor law
⭐ AND THE NUMBER TO PRESENT, WHICH IS A SUCCESS AT TWELVE RATHER THAN A FAILURE AT TWENTY-FOUR:
  twelve playable board languages with twelve interface locales, seven more licence-clean and waiting on
  data, five blocked with named and evidenced causes. Every one of the twenty-four is dispositioned.
```
