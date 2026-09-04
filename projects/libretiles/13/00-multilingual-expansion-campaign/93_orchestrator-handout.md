# Orchestrator handout — continuing `13/00 multilingual-expansion-campaign`

Artifact class: **continuation handout. Evidence, not authority.** It grants **no** repository,
implementation, Git, deployment, production, account, filesystem, or external-service mutation
authority. Task authority comes only from your own prompts; material product decisions come only from
the Cooperator.

Written 2026-09-04 by the Orchestrator that executed this whole from `ad4ce03` to `529e691`, at a
coherent boundary: porcelain empty, public readback equal, no Worker in flight, one E3 acceptance
handed to the Cooperator and outstanding.

⭐ **Revised the same day, twice, by the session that held that boundary.** (1) The E3 acceptance ran
and returned `acceptance-PASS` with zero corrections, so C1a is ACCEPTED and C1b is unblocked with a
nineteen-item scope — sections 3, 3b, 6 and `00_notes.md` §32. (2) The UI-localization product decision
was put to the Cooperator and ANSWERED — option A, no flags — and he assigned the translations to a
fresh Orchestrator, which is section 5 and `00_notes.md` §33. **The tree is still clean at `529e691`;
nothing of that objective is implemented.**

---

## 0. Read exactly these four things, in this order, and nothing else first

```text
1  /home/agile/meta/AP_DESTILLED.md          942 lines. The protocol, indexed by line number against
                                             the PINNED .ap. Read once, then work from the citations.
2  /home/agile/meta/AP_DEFECTS.md            847 lines. ⭐ NEW, and it is why this handout is short.
                                             Twelve MEASURED defects of AP itself, from this session,
                                             each with its fix. Section 3 of it is the workflow that
                                             produced everything good here. ⛔ READ IT BEFORE YOU
                                             WRITE YOUR FIRST PROMPT.
3  ./00_notes.md                             the decision record of this whole, thirty sections. It is
                                             the file this handout compresses. Do not read it front to
                                             back; use section 1's index and the pointers below.
4  ./90_language_ledger.md                   twenty-four candidate languages, nine columns, and the
                                             two source questions already answered.
```

⛔ **Do NOT read the rest of `/home/agile/meta`.** It is tens of thousands of lines and this handout
plus those four files is the whole of what you need. The one exception is named in section 8.

⚠ **`AP_DEFECTS.md` changes how you should work, and the Cooperator asked for it explicitly.** Its
short form: the ORCHESTRATOR reads the protocol; a WORKER gets **line citations, not documents**;
trivial work is **orchestrator-direct with no Worker at all**; a Worker's job includes **critiquing
your prompt and your approach**, and you correct your orchestration from what it says. Do not
re-derive that. It is measured.

---

## Handoff capsule

```text
project            Libre Tiles — Next.js 16.3.4 + Django 5.2.17 Scrabble-like web app
repository         https://github.com/cisarik/libretiles
working copy       /home/agile/Projects/libretiles
main               529e6910ddf57dfbb4a9671bbab668b975067cf8
public readback    git ls-remote origin refs/heads/main == 529e691   verified 2026-09-04
porcelain          EMPTY
AP pin             .ap gitlink 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656, submodule HEAD equal
Meta repo          /home/agile/meta at c091d63, pushed
active Worker      none
active mutation    none
your next Worker session ordinal   07     (sessions 01-06 all consumed and archived; 06 is the
                                           C1a independent acceptance, PASSED — see section 3)

playable today     12 of 24    english slovak czech polish afrikaans italian dutch german
                               portuguese danish swedish icelandic
UI locales today    4 of 24    en sk cs pl        ⇐ THIS IS YOUR NEXT OBJECTIVE, section 5
lexicon assets     13 audited, 0 failed
gates at 529e691   mypy 85 · ruff · manage.py check · pytest 745 passed 4 skipped · 749 collected ·
                   validate_lexicons 13/0 · typecheck 0 · vitest 454 passed 3 skipped · lint 0 ·
                   build 0 with ELEVEN dynamic routes and ZERO static
```

## The twelve commits of this whole, in order

```text
4904e29  docs(prd)      Collins 2019 replaces the stale SOWPODS references
a199d0e  docs(env)      document PRIMARY_DICTIONARY_FILE, the undocumented Tier-1 override
4f6f38d  chore(dicts)   remove obsolete SOWPODS dictionary file          ⛔ COOPERATOR'S OWN COMMIT
86ec39e  test(lexicons) no unclaimed file may sit in the shipped dictionary directory
7a3899d  chore(public)  drop five unreferenced Next.js scaffolding assets
153ead7  feat(variants) Afrikaans is the fifth playable variant
dab6d0d  feat(variants) Italian and Dutch are the sixth and seventh
0deac4a  feat(variants) German is the eighth, on a PARTIAL fold
1eed5ed  feat(variants) Portuguese is the ninth — 120 tiles and THREE blanks
51e08fe  feat(variants) Danish is the tenth, and it caught an expander defect
8a50ded  feat(variants) Swedish and Icelandic are the eleventh and twelfth
529e691  feat(wire)     a multi-code-point tile crosses the wire losslessly    ⭐ E3, ACCEPTED
```

⛔ **Eleven of those twelve are ORCHESTRATOR-DIRECT and their evidence is permanently
NON-INDEPENDENT.** Only `529e691` went through a Worker, and only it carries an independent
acceptance. **Do not present any of the eleven as independently verified.**

---

## 1. Stage 1 — verify before you plan

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # expect 529e6910ddf57dfbb4a9671bbab668b975067cf8
git rev-parse HEAD:.ap                # expect 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # expect the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # expect ## main...origin/main
git status --porcelain=v1             # expect EMPTY
git ls-remote origin refs/heads/main  # expect 529e6910...
ls backend/assets/variants/ | wc -l   # expect 12
ls backend/scripts/ | grep -c lexicon # expect 11 build scripts
ss -tlnp | grep -E ':(3000|8000)'     # a listener means his dev server is up — do NOT build
cd /home/agile/meta && git rev-parse HEAD   # expect c091d63b170c8c9a5163cf138d55e1c4a77a0eba
```

Any difference: classify with all five canonical recovery classes — `accepted-continuation`,
`unrelated-owner-work`, `stale-clone`, `unpublished-candidate`, `unexplained-divergence`, precedence
`unexplained-divergence > unrelated-owner-work > stale-clone > accepted-continuation >
unpublished-candidate` — and stop. **The Cooperator commits to `main` himself; `4f6f38d` in this
whole's own history is his.** ⛔ Never attach or update `.ap`.

⚠ **Do NOT re-run the full eight-gate ladder just to greet the tree.** `AP_DEFECTS.md` D-03 records
that two exchanges in this whole spent a complete ladder on trees nobody touched. Run the repository
gate. Run the ladder when you change something.

One extra verification worth twenty seconds, because it re-proves the central claim of two eras:

```bash
cd backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python scripts/build_afrikaans_lexicon.py \
    --check --check-dir /tmp/opencode/<your-slug>/af
# expect: both digests IDENTICAL, "CHECK all artifacts identical", exit 0
```

## 2. The corrected execution route — the one thing that has broken every era

```bash
cd backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py validate_lexicons
cd ../frontend && npm run typecheck ; npx vitest run ; npm run lint ; npm run build
```

```text
⛔ `manage.py check` takes NO `-m`. `.venv/bin/python -m manage.py check` is a hard ModuleNotFoundError.
⛔ backend/pyproject.toml sets addopts = "-q". A SECOND -q silently suppresses the summary.
⛔ mypy on the FULL documented scope, never narrowed, never widened. It is 85 files.
⛔ Check `ss -tlnp | grep :3000` before `npm run build`. A listener means STOP. Never pkill.
⛔ "the build passed" and "the code type-checks" are TWO SEPARATE CLAIMS. State both.
```

## 3. ⭐ RESOLVED — C1a is independently ACCEPTED. C1b is unblocked.

```text
report    ./06_report_00.md      status PASS · acceptance-PASS · 0 corrections
verdict   R1-R6 HOLD · P1-P5 held · N1-N6 FAILED as required
owner     a session that did not design, implement or author the candidate and is not a subagent of
          the previous Orchestrator. Acceptance independence: required-fresh-independent — SATISFIED.
```

⛔ **TWO DISCLOSURES THE AUDIT MADE THAT YOU MUST CARRY FORWARD.** Both are in `00_notes.md` §32.1:

```text
Q2  R1 IS NOT CERTIFIED FOR PIXELS. There is NO Board render test in the repository — measured, and
    the audit independently confirmed it. Board.tsx consumes the new shape correctly, but that is a
    COMPILE-TIME contract, not a render test. The only pixel evidence that will ever exist for this
    slice is B4-2 of ./91_deferred-acceptance-batch.md — the Cooperator's own eyes.
    ⇒ If you want pixel certification, a Board render test is its own slice and nothing today provides it.
Q3  VERSION SKEW IS USER-SILENT, and FRONTEND AND BACKEND OF 529e691 MUST DEPLOY TOGETHER.
    A refused payload gives console.error plus EMPTY_BOARD — no toast, no banner. And old client +
    new backend has NO refusal at all, because the guard is introduced in that very commit.
    ⇒ Carry this into the deployment whole. It is not a defect of the slice; it is a deploy constraint.
```

⭐ **And it returned a NINETEEN-ITEM one-code-point inventory that is now C1b's complete scope** —
`00_notes.md` §32.2 and `06_report_00.md`'s required field. Seven items were new to the previous
Orchestrator, including `legality.py:28`, `move_search.py:33`, `prompts.ts:267` and — ⚠ importantly —
`test_atomic_tile_tokens.py:532`, which asserts `len(row) == 15` on the AI grid. **That file is the
L·L canary's host, the one file three consecutive prompts forbade touching, and C1b must now edit it.**

## 3b. Historical — what the obligation was, for anyone reading the archive

**`529e691` was E3 and its fresh independent acceptance was outstanding when this handout was first
written.**

```text
prompt        ./06_acceptance_00.md          written, committed, delivered to the Cooperator
route         ⛔ COPY-PASTE, by the Cooperator, into a session that is NOT a subagent of yours
why           AP.md:1395-1405. The implementing Worker was a subagent of the previous Orchestrator
              and that Orchestrator authored the design and the prompt. Neither is independent.
              That acceptance session is the ONLY independent evidence this slice will ever get.
session       06 is RESERVED for it. Your first fresh session is 07.
```

**What the previous Orchestrator had to do about it, in order — ALL FOUR NOW DISCHARGED:**

```text
1  ASK the Cooperator whether the acceptance ran and what it returned. Do not assume, and do not
   proceed as though it passed.                                          ⇒ DONE. It ran.
2  If it PASSED: archive its report as ./06_report_00.md, record the verdict in ./00_notes.md, and
   only then treat C1a as accepted.                                      ⇒ DONE. §32, §32.1, §32.2.
3  If it FAILED or found something: ONE smallest coherent correction, and ⛔ the corrector may not
   self-certify it (AP.md:393-420). Scoped re-acceptance is valid only if the correction changes none
   of a semantic owner, authority/routing/convergence, an exact structural field, validator
   semantics, runtime behaviour, an independence assumption, or a security boundary.
                                                                         ⇒ NOT NEEDED. Zero corrections.
4  If it never ran: ⛔ do NOT substitute your own subagent for it and do NOT proceed to C1b as though
   the foundation were accepted.                                         ⇒ NOT NEEDED.
```

⭐ **C1a IS ACCEPTED. C1b is unblocked (section 6). Its two disclosures survive acceptance and are
live constraints, not history: R1 is NOT certified for pixels, and version skew is USER-SILENT so the
frontend and backend of `529e691` must deploy together.** `00_notes.md` §32.1.

---

## 4. What this whole learned about adding a language — the part you can reuse verbatim

**Twelve languages ship and NOT ONE required an engine change.** Every rule any of them needed was
expressible in the ASSET at build time. That claim is measured, not asserted, and here is the whole of
it in one table.

### 4.1 The tile-face rule taxonomy — eight shapes, all in data

```text
NO RULE             slovak · czech · polish · icelandic     every accented letter IS a tile
TOTAL FOLD          afrikaans · italian                    no marked letter has a tile
TOTAL + LIGATURE    dutch                                   ĳ -> ij; ⛔ NFD walks PAST a ligature
PARTIAL FOLD        german (ä ö ü) · portuguese (ç) ·        the marked letters that HAVE tiles survive
                    danish (æ ø å) · swedish (å ä ö)
FOLD WITH CARVE-OUT swedish                                 Ü is neither folded NOR a tile face
SHAPE FILTER        danish (þ ð) · swedish (ü ł æ ø μ) ·     a letter no fold can remove and no tile
                    icelandic (c w z q)                     bears -> DROP the word, bounded
FREE FROM CASEFOLD  german ß -> ss · greek ς -> σ            ⭐ Unicode full case folding already does it
TOOL-DEFECT GUARD   danish: 11 lines unmunch truncated       decode per line, count, bound
                    mid-character; all others assert ZERO
```

⚠ **Two of those eight were found by a GUARD FIRING, not by design.** Dutch's ligature by a probe word
that was measurably absent; Danish's truncation by `errors="strict"` refusing to decode where my own
exploratory pass had used `errors="replace"` and seen nothing. **A guard that never fires is
indistinguishable from no guard until the day it does.**

### 4.2 The friction, measured: one build script plus three test inventories

```text
AUTOMATIC   ~25 parametrized cases enrol themselves per language, with NO new test file. The generic
            harness, P1-P15 and G1-G25 all pick a variant up from its manifest.
DELIBERATE  exactly THREE hardcoded inventories, all in tests, ZERO in production code:
              backend/tests/test_variant_invariants.py     the G14 probe row
              backend/tests/test_lexicon_provenance.py     P10b's build-script inventory
              backend/tests/test_czech_polish_variants.py  test_t7's exact catalog order
            ⚠ P13 used to be a fourth. It hardcoded "three scripts" and defeated the point of a
              derived claim set; it now owns DRIFT and leaves the inventory to P10b.
```

### 4.3 ⛔ The five rules that are not negotiable, and why

```text
1  READ THE LICENCE BEFORE WRITING A BYTE. Standing condition 5 makes an unclear licence a
   DISQUALIFICATION and a recorded BLOCKER, never a footnote and never a judgement.
   ⇒ Norwegian is BLOCKED on exactly this and it is the sharpest precedent in the campaign: the asset
     is fine, both written standards ship, and the ONE explicit licence line in the directory is
     titled "Myspell hyphenation" and grants for the hyphenation files. A directory convention is a
     convention, not a grant. `00_notes.md` "### 23.3".
2  THE LICENCE EVIDENCE MUST COME FROM THE SAME PINNED COMMIT AS THE ASSET. Fetching a grant from a
   Debian copyright file or a project website proves terms for a DIFFERENT artifact than the one
   `--check` reproduces. ⛔ A pin that covers the words but not the terms is not a pin.
3  DETERMINACY, NOT PERMISSIVENESS, MAKES A LICENCE SHIPPABLE. Icelandic's mixed provenance SHIPS as
   CC-BY-SA-3.0 — public-domain base plus CC BY-SA morphological additions, indistinguishable inside
   the .dic, so share-alike propagates. ⚠ Claiming public domain for the whole would UNDER-state a
   real obligation, which is the mirror of over-claiming and just as wrong. `00_notes.md` "### 25.3".
4  NEVER COPY A DISTRIBUTION FROM A NEIGHBOUR LANGUAGE. Czech and Slovak are linguistically close and
   share NOTHING here.
5  NOT ONE WORD FROM A LANGUAGE MODEL. No synthesis, generation, translation or model-authored word
   list, ever. ⚠ This one bites in section 5 — read it there.
```

### 4.4 The sources, both already answered

```text
TILE DISTRIBUTION   https://en.wikipedia.org/wiki/Scrabble_letter_distributions — and this is not a
                    guess: ALL THREE previously shipped non-English manifests already declare it as
                    their `source_url`. Its "Official editions" section contains all 24 targets.
                    The national authorities (JÚĽŠ SAV, ÚJČ, RJP, MTA) sourced `alphabet_order`, NOT
                    the distribution.
LEXICON             LibreOffice/dictionaries at pinned commit
                    75f5dff8c972fff4a32e4ea8434722c277f02a3f — the SAME commit all eleven scripts use.
                    22 of 24 targets have a .dic/.aff pair there. The two that do not are recorded
                    blockers, not gaps.
EXPANDER            hunspell 1.7.3, asserted by every script, fails closed on a mismatch.
```

### 4.5 The four blocker classes, named separately on purpose

```text
NO SOURCE          finnish (no plain affix pair — Voikko) · malay (no ms_MY; ⛔ Indonesian is NOT
                   Malay and must not be substituted)
EXPANDER FAILS     french — unmunch emits 1 168 520 lines of UNEXPANDED FLAG DATA and yields ~77 000
                   playable words against an official lexicon of order 400 000. A variant that
                   rejects most valid French words is a defect that looks like a feature.
                   ⇒ ROUTE OUT: Spylls 0.1.7, already proven on Hungarian.
NO LICENCE GRANT   norwegian — see 4.3 rule 1
SIZE               hungarian — ~301 M forms at the tightest bound. Decision D is TAKEN and CONFIRMED:
                   committed build script, output GITIGNORED, generated locally at setup, readiness
                   reports `unavailable` until it runs. ⛔ Three alternatives are REJECTED; do not
                   re-propose them. `00_notes.md` section 5 of the previous handout and the ledger row.
```

⚠ **Twelve of twenty-four with four well-evidenced blockers is a SUCCESS.** Twenty-four claimed by
shipping a lexicon nobody can license, or a distribution nobody sourced, is a failure that looks like
a success — and the Cooperator is presenting this at a job interview.

---

## 5. ⭐ YOUR NEXT OBJECTIVE — UI localization, and the Cooperator named it himself

> *Na zaklade lokalizacie gameplay budem chciet aby sa uderne efektivne lokalizovalo aj UI do vsetkych
> jazykov variant hry ktore budu implementovane.*

⇒ **Twelve languages are PLAYABLE. Four have a UI.** Close that gap, punchily, for the eight that
ship without one — and then for every language a later batch adds.

⭐ **The material product decision is ALREADY TAKEN (§5.2: option A, no flags) and the Cooperator
assigned the translations to a FRESH Orchestrator — you. Nothing is implemented; the tree is clean at
`529e691`.**

### 5.1 What exists, measured at `529e691`

```text
frontend/src/lib/i18n/locales.ts:1     export const LOCALES = ["en", "sk", "cs", "pl"] as const;
frontend/src/lib/i18n/locales.ts:3     DEFAULT_LOCALE = "en"
frontend/src/lib/i18n/locales.ts:4     LOCALE_COOKIE_NAME = "libretiles_locale"
frontend/src/lib/i18n/messages.{en,sk,cs,pl}.ts    ~300 keys each · 280 text + 20 fn · 1 200 strings
frontend/src/lib/i18n/plural.ts        pluralEn · pluralSk · pluralCs (= pluralSk, DELIBERATELY) · pluralPl
frontend/src/lib/i18n/i18n.test.ts     test-enforced key-set AND interpolation parity across LOCALES
                                       :956-961 INSTALLED_VARIANTS = english slovak czech polish
                                       :983     ownName: per-variant display name per locale
frontend/src/lib/i18n/GLOSSARY.md      the translation glossary. :51-53 records that pluralSk is WRONG
                                       for Polish at 22, 23, 24, 122 — which is why pluralPl exists.
frontend/public/                        cs.png en.png hu.png pl.png sk.png drevo.jpeg
                                       ⚠ hu.png ships for a language with no manifest and no locale.
                                       Keep it; the Hungarian slice CLAIMS it. `00_notes.md` §14.
frontend/src/components/settings/GameLanguagePanel.tsx:12-24
                                       VARIANT_NAME_KEYS and VARIANT_FLAG_SRC, four entries each.
                                       ⭐ variantDisplayName() FALLS BACK to the server display_name
                                       and flagSrc is OMITTED when absent — which is why eight
                                       backend variants appear in the picker with no UI edit at all.
```

### 5.2 ⭐ THE DECISION IS TAKEN — OPTION A, NO FLAGS. Do not re-ask it.

The previous handout priced this in three options and named the choice as the Cooperator's. **It was
put to him and he answered.** Full record in `00_notes.md` §33.

```text
SCOPE   A — eight FULL catalogs, ~300 keys each, every one carrying a header declaring it
        machine-authored and unreviewed. Not C, not B. He accepted the stated risk with the interview
        named: eight languages of unreviewed copy in the piece he is presenting.
FLAGS   NONE — names only. `GameLanguagePanel.tsx:51` already OMITS `flagSrc` for a slug with no
        entry, so the picker is correct without them and takes real PNGs later with no code change.
        ⛔ He declined hand-drawn national flags. Do not generate any.
```

⚠ **Standing condition 5 still stands and still means what it said.** A UI string is presentation and
may be model-authored; **a lexicon is game DATA and may not be, ever.** Option A does not soften that
by one word. The header on every catalog is what keeps the distinction visible to a reader.

⛔ **And the Cooperator ruled on WHO does it: `PREKLADY MA ROBIT FRESH ORCHESTRATOR`.** The previous
session began slice 1 after reading `Pokracuj` as authority to implement, and was corrected. It
reverted to `529e691` — porcelain empty, verified — and wrote §33 instead. **That is why you are
reading this: the objective is YOURS, unimplemented, with the reconnaissance already paid for.**

### 5.3 ⭐ The free win that decides your slicing, measured

```text
messages.{sk,cs,pl}.ts are `Record<TextKey, string>` plus `{ [K in FnKey]: (typeof enFn)[K] }`.
⇒ A NEW CATALOG FILE TYPECHECKS AGAINST `messages.en.ts` ALONE. `tsc --noEmit` catches a missing key,
  an extra key, and a wrong interpolation parameter — with the locale NOT yet in LOCALES, and without
  `i18n.test.ts` running at all.
⇒ Eight catalogs are eight INDEPENDENT Workers, each gated on typecheck, before one wiring file is
  touched. The parity test the previous handout called the obstacle is not the gate on the catalogs;
  it is the gate on the WIRING, which is one small slice after them.
```

Wiring, when the catalogs are green — each of these is a type error if half-done, so it cannot
half-land: `locales.ts:1` LOCALES 4→12 · `translate.ts:7-18` TEXT and FN, 8 entries each ·
`index.ts:24` 8 plural re-exports. ⛔ `translate.ts:20-40`'s single cast stays untouched; its comment
explains why it is safe, and the mapped type above is the reason.

### 5.4 ⭐ The plural rules are DERIVED AND VERIFIED. Take them; do not re-guess them.

`Intl.PluralRules` IS CLDR, and it is already in the test runtime — so the rule can be pinned
EXECUTABLY instead of by citation, and a CLDR change becomes a red test instead of a wrong string.
Measured on `node v26.4.0 / ICU 78.3`; full table and method in `00_notes.md` §33.2.

```text
af nl de da sv   one/other, and over integers 0..3000 each is IDENTICAL to `en` — measured, zero
                 divergences. ⛔ Identical is NOT the same rule: Danish CLDR accepts a fraction as
                 `one` (da 0.5 → one, en 0.5 → other). The helpers TRUNCATE, which is what makes the
                 identity real. ⇒ FIVE FUNCTIONS, NOT FIVE ALIASES. `pluralCs = pluralSk` is an alias
                 only because those two agree over the WHOLE domain, fractions included — which is
                 the distinction the old §5.4 was reaching for.
is               ⛔ `i % 10 == 1 && i % 100 != 11`. 21, 31, 101, 121 are `one`; 11 and 111 are
                 `other`. Diverges from `en` at 269 integers in 0..3000.
it               THREE categories one/many/other. `many` is integer-reachable at 1 000 000.
pt               THREE categories, AND ⛔ ZERO IS SINGULAR (CLDR `one: i = 0..1`). "0 ponto".
                 ⭐ A passed turn and an empty score both display zero, so a copied English rule is
                 visibly wrong on a real board — not in a corner case.
⚠ pluralSk's third parameter is NAMED `many` but is CLDR `other` over integers. Every shipped Slovak
  and Czech string is CORRECT (the slot holds the genitive plural, right for 0 and 5+). Polish is
  different: pluralPl's third slot really is CLDR `many`. ⇒ A comparison test must declare the
  slot→category mapping per language. ⛔ Do not fix that parameter NAME in the same slice as eight
  new languages.
```

### 5.5 🐞 Two gaps this objective walks into. Both measured, neither in the old handout.

```text
1  `lexiconRejectionKey()` switches on collins2019 · slovak · czech · polish only. EIGHT playable
   variants' lexicons fall through to `game.lexicon.unknown`, so a rejected Danish word cannot name
   what rejected it. ⇒ A REAL gap that exists TODAY at four locales, independent of adding eight.
2  `i18n.test.ts:983` `ownName` becomes 144 CELLS if both axes go to twelve, and it asserts each
   label contains its own variant's name and NO other variant's name in that locale.
   ⛔ ICELANDIC IS THE TRAP: "Enska" is a substring of "Hollenska" AND of "Svenska". It survives today
   only because `toContain` is case-sensitive and the cells are capitalised. Luck, not design.
   ⇒ Do NOT weaken that test to land the matrix. Both naming axes are their own slice, AFTER the
     catalogs, diagnosed against four locales of known-good data first.
```

⚠ **Slicing, prompts and Worker count are YOURS.** My recommendation is catalogs first (they
parallelise and self-verify), wiring second, the two naming axes third — a recommendation only, and
the 144-cell matrix is exactly what a fresh session should price against `AP_DEFECTS` D-02 rather
than inherit as a plan.

GATES the frontend only: `npm run typecheck`, `npm run test`, `npm run lint`, `npm run build`.
      ⛔ This objective touches NO backend file, so running the Django suite over it is D-03. Say so
      in the prompt.

---

## 6. The rest of the campaign, ordered by leverage

```text
C1b  ⭐ UNBLOCKED — C1a is accepted. Its scope is now the NINETEEN-ITEM inventory the independent
     audit returned; see `06_report_00.md`'s required field and `00_notes.md` §32.2. The sites the
     previous Orchestrator had already measured:
       backend/gamecore/state.py:44   grid.append("".join(row_chars))
                                      a 16-char row SHIFTS EVERY COLUMN to its right
       backend/gamecore/state.py:48   ai_rack="".join(ai_rack) collapses a digraph rack
       frontend/src/lib/prompts.ts:190  GRID_ROW = /^[\p{L}.]{15}$/u
                                      ⛔ a 16-char row does not misalign — it FAILS the regex and is
                                      SILENTLY DROPPED, so the model gets a SHORT BOARD
       frontend/src/lib/prompts.ts:250 :254   suspected, to measure
       frontend/src/lib/rack.ts:1     UNICODE_TILE = /^[\p{L}?]$/u
       frontend/src/components/game/BlankPicker.tsx:8
                                      ⛔ "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("")
                                      A BLANK CAN NEVER BE ASSIGNED A DIGRAPH FROM THE PRODUCT.
                                      `GameState.alphabet` already ships on the wire — the fix has a
                                      source of truth waiting.
       frontend/src/components/game/AIThinkingOverlay.tsx:72   word.toUpperCase().split("")
     ⭐ AND SEVEN THE AUDIT ADDED, each verified by the previous Orchestrator at 529e691:
       backend/gamecore/legality.py:28    LETTERS = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
       backend/gamecore/legality.py:143   error copy says "A-Z" while the CHECK is set membership
       backend/gamecore/move_search.py:33 _BLANK_LETTERS = string.ascii_uppercase
       frontend/src/lib/prompts.ts:267    rows[row][col] — one column per UTF-16 unit
       frontend/src/lib/constants.ts      TILE_POINTS is A-Z plus "?" only
       frontend/src/lib/ai-turn-simulation.test.ts:119 · rack.test.ts:4
       ⚠ backend/tests/test_atomic_tile_tokens.py:532   asserts len(row) == 15 on the AI grid.
         ⛔ THAT FILE IS THE L·L CANARY'S HOST — the one file three consecutive prompts forbade
         touching. C1b MUST edit it, so its prompt must say so explicitly and must not simply
         inherit the old prohibition.
     ⚠ THE AUDIT LABELLED ITS OWN INVENTORY: "it is a search, not a proof of absence." Treat it as
       R-J tells you to — a HYPOTHESIS — and make widening it a required field again.
     ⭐ AND THE GOOD NEWS, measured: the MOVE CORE hash covers only `MOVE_SYSTEM_PROMPT`
       (`prompts.test.ts:79-84`), NOT the three grid functions — so C1b can repair them WITHOUT
       moving the pinned hash. And `gamecore/state.py:63,104-125` already carries a structured
       `grid: list[list[str | None]]` for the save file, beside the lossy one.
C1c  dictionary authority, ENLARGED by a finding: `evaluate_scoring_move` at `legality.py:112`
     already accepts `authority: WordAuthority | None`, so the seam exists and the work is to PASS
     one at five call sites (`services.py:862`, `:1649`, `diagnostics.py:476`, `move_search.py:373`,
     `:585`), delete `_word_passes_dictionary`, and fix four `diagnostics.py` guards.
     ⛔ PLUS: `services.py:216-218` `not w.isalpha()` means `L·LA` CANNOT PASS THE DICTIONARY today,
     and `lexicon_health.py:95` has the identical test. Same defect class as the serializer's.
B1   HUNGARIAN. Needs C1a+C1b. Inherits six conditions from two eras: two DIFFERENT multi-character
     tokens in the fixture, the L·L canary, `unavailable` without crashing before the local build,
     the code-point ceiling DERIVED and justified, the six-word gate as a build post-condition, an
     `unavailable` variant made UNSELECTABLE at the three server sites (⚠ MEASURED STILL OPEN:
     `serializers.py` CreateGame and QueueJoin, and `services.py` `_unknown_variant_payload`, all
     three test installed-ness only, never readiness), and a STREAMING audit — the current duplicate
     check holds 3.9 M tokens at ~500 MB, and 301 M would need ~40 GB.
B4/B6 hr · sl · es · el · bg · ru. All six unlock on C1b. ⚠ Greek and Cyrillic are EASIER than
     Hungarian once `[A-Z]` and `len == 1` are gone; do not treat non-Latin as the hard part.
     es needs C5 (ruleset identity) for its 23 country .dic files.
C2   variant-declared blank targets, and ⛔ IT WAS SCOPED BACKWARDS. The handout specified a
     RESTRICTION of the derived set. Measured, three shipped editions need the OPPOSITE:
       afrikaans  blank MAY become X or Z, which have no tile   (source: citation-needed)
       italian    blank MAY become J K W X Y, none of which has a tile   (source: stated)
       danish     blank MAY become Q                            portuguese: K W Y
       swedish    blank MAY become Q W Ü Æ
       turkish    blank may NOT become Q W X                    ← the only true restriction
     ⇒ C2 must be an EXPLICIT DECLARED SET able to name alphabet letters without tiles. Absent means
       derive from the tile set exactly as today, which keeps all twelve byte-unchanged.
C3   ⛔ NARROWED TO TURKISH ONLY, and this is a measured scope collapse worth knowing:
       german  'ß'.casefold() == 'ss' ALREADY. Nothing to build.
       greek   'ς'.casefold() == 'σ' ALREADY.
       fr/da/sv/no/is  at most a partial ASSET fold, German's shape.
       turkish ⛔ THE ONE REAL CASE: 'İ'.casefold() -> 'i' + U+0307, TWO code points, and
               `isalpha()` on that is FALSE — so `_filter_words` would SILENTLY DROP every Turkish
               word containing İ. `00_notes.md` "### 19.1".
C4   face-versus-lexical realization. NO language on the target list needs it. Design so
     multi-realization is not PRECLUDED and BUILD NOTHING.
C5   ruleset identity. `variant_name` exists at `variant_store.py:82`, feeds `display_label` at
     `:108-112`, and is declared by NO shipped manifest — so that branch is still untested. Needed by
     es, and candidates exist for pt (pt_BR), no (Bokmål/Nynorsk), nl (the pre-1998 IJ tile) and
     is (Krafla, which is tournament-sanctioned but explicitly independent of the brand).
DEBT eleven build scripts share ~350 near-identical lines. ⚠ RE-DISPOSITIONED, and read the reason
     before you "fix" it: the per-script differences are LOAD-BEARING and heavily commented — Danish's
     truncation guard, Swedish's Ü carve-out, Icelandic's anti-fold assertions, German's latin-1 pair,
     Portuguese's per-file encodings. A shared module risks making exactly those LESS visible.
     ⇒ TRIGGER, concrete rather than a count: extract it when one rule must change in THREE OR MORE
       scripts at once. `--check` on all eleven makes it byte-verifiable whenever that happens.
```

## 7. The nine prompt-defect rules, and the three this whole added

R-A through R-F are inherited and still hold. R-G through R-J are mine and every one was paid for.

```text
R-A  A "do not change X" instruction must name WHY.
R-B  Prohibitions get written LAST, then read against the obligations in ONE pass.
     ⚠ AND THE PASS MUST COVER TEST HOSTS. Mine did not, and a stage gate became unsatisfiable.
R-C  When you tell a Worker to correct stale comments, ENUMERATE them from your own grep.
R-D  `exactly`, `identical`, `mirror` are grep targets in your OWN draft.
R-E  AN ABSENCE CLAIM IS NOT A FINDING UNTIL IT NAMES ITS PATTERN, AND THAT PATTERN IS
     CASE-INSENSITIVE. Run `git grep -in` AND `git grep -n`; report both counts.
R-F  NEVER AUTHORIZE A DELETION IN THE SAME EXCHANGE THAT ESTABLISHES THE ASSET IS UNREFERENCED.
R-G  ⛔ NEVER copy a `file:line` from a handout, notes file, or prior prompt. Re-measure it in the
     session that writes the prompt. MEASURED: eight of nine line references in the PREVIOUS handout
     were stale at the very commit it was written against — and I then did it AGAIN twice, attributing
     a line to a file only 208 lines long. `00_notes.md` "### 3.2" and "### 30.3".
R-H  When a document states a COUNT, reconcile it against the artifact by CONSTRUCTION before
     repeating it. `wc -l collins2019.txt` is 279 497 and the word count is 279 496 — a header line, a
     blank line, CRLF endings and no final newline.
R-I  A claim about a file's ENCODING or BYTE CONTENT must come from a byte-level command, never from
     having read the file. `LC_ALL=C grep -n '[^ -~\t]' <file>` costs one second.
R-J  ⛔ AN ENUMERATION HANDED TO A WORKER IS A HYPOTHESIS, NOT A SPECIFICATION. Say so in the prompt.
     Give the commands. Give the classification. Then make "name any site my commands cannot reach"
     an OBLIGATION with its own report field.
     ⚠ THIS RULE COST THREE EXCHANGES AND WENT THROUGH THREE VERSIONS. Three consecutive attempts at
     one slice each found a spelling my inventory could not reach: a `^…$`-anchored `\p{L}` regex, a
     DRF `max_length=1`, and a `"ABC…Z".split("")`. **The fourth attempt will find a fourth. Expect it.**
```

Two mechanical habits, both non-negotiable:

```text
python3 /home/agile/meta/projects/libretiles/apfieldcheck.py <prompt.md>   exit 0, EVERY prompt
⛔ NEVER build a prompt by string-patching the previous one. Regenerate the coordinate-bearing region
   whole, then let the tool check it.
⛔ WRITE LARGE ARTIFACTS IN SMALL APPENDS AGAINST A SENTINEL, never as one generation. The Cooperator
   diagnosed this and I reproduced the failure twice — a broken delivery channel cost one dispatch.
```

---

## 8. The Cooperator — the parts that change how you work

`PROJECT_CONTEXT.md:303-356` is authoritative and it is the ONE file outside section 0 you may need.
What matters most here:

```text
language     to him Slovak, masculine forms; your self-reference feminine; Worker prompts and reports
             professional English; every terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`
emoji        begin every message with the signal, and END every message with an explicit
             emoji-annotated block of what HE must do. Label manual test steps B1-1, B1-2.
his stake    MATERIAL — a job interview. A fresh clone that crashes, a control that does nothing, or a
             number that does not mean what it claims is a FIRST-CLASS DEFECT in his frame.
his replies  terse: A · Pokracuj · ano · suhlas · moment. Confirm an ambiguous one-word instruction in
             ONE LINE before spending a session on it — or better, MEASURE it. When he wrote
             "sowpods.txt vymazane" I could not tell whether it meant "it is deleted" or "delete it",
             and one `git log` answered it. `00_notes.md` section 10.
never        read or print backend/.env or frontend/.env.local; let a credential value, prefix, length
             or hash reach chat, a report or Meta; ask him for a destructive action; create permanent
             BOOT_*/NEXT_*/WORKERS.md/ORCHESTRATOR_HANDOFF.md files.
```

### 8.1 ⛔ THE TWO STANDING GRANTS, and what they do NOT waive

```text
AUTONOMY (2026-09-03, verbatim)
    "NECHCEM ABY SOM TU BOL AKO COOPERATOR POUZIVANY NA TESTOVANIE … CHCEM ABY SI PRACOVAL AUTONOMNE.
     OVEROVANIE … AZ NA KONCI VYVOJA. PROSIM PRETO MA NEVYRUSUJ."
    "AK MI BUDES CHCIET DAT OTAZKY PROSTE POUZI ODPOVEDE KTORE DOPORUCUJES. ABSOLUTNE TI DOVERUJEM."
PUNCHY EXECUTION (2026-09-03, verbatim)
    "Na trivialne ulohy nepotrebujes Workerov, si Agent Orchestrator a mas write pristup … vela vela
     vela zbytocnych tokenov. Chceme uderny vyvoj."
```

⛔ **Three things neither grant waives, and protecting them is your job:**

```text
1  NEITHER LOWERS AN EVIDENCE TIER. C1 is E3 and still needs fresh independent acceptance from a
   session that is not your subagent. Only his OBSERVATION was deferred, never a Worker function.
2  NEITHER REMOVES THE RENDERED-OUTPUT RULE. `for anything that renders, render it, or do not claim
   it.` Deferring his observation makes YOUR loopback probe MORE necessary, not less: production
   build, `next start` on a loopback port, HTTP client, stop by exact PID.
3  NEITHER TOUCHES DECISION 10. He has no screen reader and will not install one. Accessibility
   claims are closed BY INSPECTION ONLY, permanently.
```

⚠ **And the obligation the autonomy grant creates: `./91_deferred-acceptance-batch.md` must be
appended to AT THE MOMENT each slice lands.** It now carries B1 through B4. **If you add a language
and do not add its steps, they will be reconstructed from memory at the end and be wrong.**

### 8.2 The naming problem — his, and he asked for it to be recorded

He raised it himself and it is in `AP_DEFECTS.md` as **D-05**:

```text
"Agent Orchestrator"   his term for you. ⛔ MEASURED ABSENT from the governing pin.
"Worker Orchestrator"  the previous era's term for an experimental profile. Also absent.
```

⇒ Neither exists in AP. **Use: ORCHESTRATOR, in `orchestrator-direct` or `worker-delegated` execution
mode.** That names what you DO rather than which agent runs you, and it keeps AP's three-role model
intact. If he uses either informal name, answer to it and record the mapping once — do not correct him
twice.

---

## 9. Restoration readiness review

```text
contradiction review      PASS. Nine stale claims in the two previous handouts are named explicitly:
                          section 5 of `92_c1_design.md` lists five for C1, and `00_notes.md` "### 3.2"
                          lists eight stale line references in the era-12 handout. Nothing is hidden.
omission review           PASS. NOTHING IS OWED. The C1a independent acceptance returned
                          `acceptance-PASS` and is archived as `06_report_00.md`. Every prompt/report
                          pair of this whole is archived.
stale-state review        PARTIAL BY DESIGN. Every number was measured 2026-09-04 at 529e691, and the
                          Cooperator commits to `main` himself. Section 1 exists so you re-measure.
                          ⚠ R-G says re-measure every `file:line` in this handout before quoting it.
                          I broke that rule twice in one session; the previous Orchestrator broke it
                          eight times. Assume this file has stale coordinates too.
authority review          PASS. This document grants nothing. Stated at the top.
active-mutation review    PASS. Porcelain empty, public readback equal, no Worker in flight.
active-Worker review      PASS. Sessions 01-06 all terminated and archived. Your first fresh session
                          is 07.
security-boundary review  PASS. Secret, host, network, browser, filesystem, account and Git boundaries
                          are stated in section 8.
strategic-direction
  review                  PASS. The objective is the Cooperator's verbatim text in section 5, and the
                          ONE material product decision inside it — how far to take UI localization —
                          is explicitly flagged as HIS, with three costed options and a recommendation.
next-step executability
  review                  PASS. Section 1 is executable immediately and read-only. Section 3 is one
                          question to the Cooperator. Section 5.3 is priced.

RESTORATION CLASSIFICATION: PASS
```

Reasoning recommendation for your first substantial prompt: **Medium** for one catalog under section
5.3 — 300 keys against a type that checks them for you, with the plural rule already derived in 5.4,
does not earn High, and `AP.md:740-746` names over-routing as an anti-pattern. **Medium** for the
wiring. **High** for the 144-cell `ownName` matrix in 5.5, where the failure is a substring collision
across twelve languages, and **High** for C1b, with its named risk already stated: it changes what the
MODEL sees, and it fails SILENTLY. **Extra High is not warranted anywhere.**

## 10. The one-paragraph version

Twelve of twenty-four languages are playable and every one of them landed without a single engine
change, because every rule any language needed turned out to be expressible in its build script — a
taxonomy of eight shapes is in section 4.1, and two of the eight were found by a guard firing rather
than by design. Four languages are blocked and each names its exact missing thing, which is the honest
form of this campaign rather than a shortfall. The one E3 slice, the wire format, landed at `529e691`
on its third attempt after two Workers correctly refused a defective grant, and its independent
acceptance has now returned `acceptance-PASS` with zero corrections — so C1a is accepted, C1b is
unblocked with a nineteen-item scope, and two disclosures ride along that are constraints rather than
history: no pixel certification, and a user-silent version skew that forces a joint deploy (section 3).
Your next objective is the Cooperator's own: twelve languages play and four have a UI, so close that
gap punchily — and the material product decision that section 5.2 used to reserve for him is TAKEN
(option A, eight full machine-authored catalogs, no flags), with the translations assigned to you
because he said so in as many words. Nothing of it is implemented, the plural rules are already derived
and verified for all eight, and each catalog typechecks alone — so eight Workers can run in parallel. Before you write your first prompt, read `AP_DEFECTS.md`: twelve measured defects of the
protocol itself, including the one that matters most here — that a Worker's job includes critiquing
your prompt and your approach, and that twelve of the previous Orchestrator's own defects were caught
that way and not one by its own review.

**This document grants no mutation authority. Verify repository and public truth independently before
you act.**
