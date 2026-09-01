Artifact class: **Orchestrator handout.** First handout for logical whole
`atomic-tile-token-foundation`, and the carrier of the unfinished state of
`ui-internationalization`. It grants **no** repository, implementation, deployment, production, account,
external-service, credential, or Git mutation authority by itself. Verify everything yourself.

Written by the Orchestrator that localized the UI to Slovak and accepted the tile-token plan, at the
Cooperator's explicit request (`B13-1 A`), for a fresh Orchestrator running **Claude Opus 5 Thinking with
write access to the repository**. It is written to the same model, so section 3 names failure modes that
model actually exhibited in the era that just ended rather than generic advice.

---

## Handoff capsule

```text
Two logical wholes are live. Read this whole handout before issuing anything.
  10/00  ui-internationalization                OPEN, ~60% done, no active mutation
  11/01  atomic-tile-token-foundation           OPEN, planning-PASS accepted, ready for slice F1
  11/02  czech-polish-hungarian-variant-activation   NOT STARTED, blocked on dictionaries

Verified state: main = 1b7b05d0de854d7936c5fcd2b0d55a5cc5d14cfd, published, porcelain empty except
                ten deliberately untracked files in frontend/public (five source JPEGs, five
                normalized PNGs). .ap gitlink 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656.
                All EIGHT standing gates measured green at that commit by the Orchestrator:
                mypy 80 files, ruff, manage.py check, pytest 328 passed / 4 skipped,
                npm run typecheck exit 0, npx vitest run 342 passed / 3 skipped,
                npm run lint exit 0, npm run build exit 0.
Active mutation: none. No Worker is active.
Next owner and bounded next action: YOU. Verify state, then issue slice F1 of
                atomic-tile-token-foundation to a FRESH Worker session, whose first action is the
                read-only destructive-migration preflight and NOT migration execution.
Repeated blocker: none open.
Planning budget: the initial planning cycle for 11/01 is CONSUMED. One targeted revision remains.
Audit budget: no audit has been performed for either whole.
This handoff grants no new mutation authority.
```

---

## 0. Required reading, in this order

1. `/home/agile/meta/projects/libretiles/PROJECT_CONTEXT.md` — **in full, first.** Identity, the
   Cooperator profile and his communication rules, the emoji signals, the eight standing gates, the
   mandatory execution deviation, the eleven locked forks, the formed-word invariant, the central
   product fact, the security state, the instruments, twelve lessons, the environment traps, and
   sections 12 and 13 which carry his admin-console product intent and the seven `ui-internationalization`
   decisions.
2. `/home/agile/meta/projects/libretiles/DEFECT_LEDGER.md` — the running inventory. **Do not re-test
   what is recorded as verified.** Its era-10 section and its
   "pre-planning evidence for the multilingual tile-token whole" section are the technical spine of
   this handout.
3. `11/01-multilingual-tile-token-foundation/90_orchestrator-plan-acceptance.md` — the acceptance
   verdict, the three corrections, and the eight decisions.
4. `10/00-ui-internationalization/00_handout.md`, `90_orchestrator-restoration.md`,
   `91_orchestrator-decisions.md`, `92_orchestrator-glossary-and-plan.md`.
5. `09/00-backend-security-hardening/99_closure.md` — the closed security era and its seven lessons.
6. `/home/agile/Projects/libretiles/AGENTS.md` and `frontend/AGENTS.md`.
7. `.ap/AP.md` — RF-01, RF-02, RF-03, RF-04, RF-07, RF-08, RF-12, RF-16, RF-18, RF-19, the Finite
   Convergence Contract, the Continuation Bootstrap.
8. `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md`.
9. `.ap/PROMPT_CONTRACTS.md` — **read the "Planning Record" section at line 89 and the
   "Implementation Authority Record" at line 156 BEFORE writing any prompt.** The previous Orchestrator
   issued a planning prompt missing all six Planning Record fields and a Worker correctly blocked. Do
   not repeat it. `PROMPT_CONTRACTS.md` owns exact field spellings; `AP_ORCHESTRATOR.md` prose does not.
10. `.ap/INFOSEC.md` sections 3, 4.1, 4.2, 4.3, 4.10, 4.11, 5, 6, 7, 8, 14 — an irreversible destructive
    migration plus an AI-boundary change activates the profile at **R4** with **E4** staging.

---

## 1. Stage 1 — verify before you plan

```text
cd /home/agile/Projects/libretiles
git rev-parse HEAD                      -> expect 1b7b05d0de854d7936c5fcd2b0d55a5cc5d14cfd
git rev-parse HEAD:.ap                  -> expect 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD               -> expect the same
git status -sb                          -> expect ## main...origin/main
git status --porcelain=v1               -> expect ONLY the ten untracked files below
git ls-remote origin refs/heads/main    -> expect 1b7b05d0de854d7936c5fcd2b0d55a5cc5d14cfd
git log --oneline -6
```

Expected untracked, and **none of it is a defect**:

```text
frontend/public/en.jpeg sk.jpeg cz.jpeg hu.jpeg pl.jpeg   Cooperator-supplied flag sources
frontend/public/en.png  sk.png  cs.png  hu.png  pl.png    Orchestrator-normalized, 48x32, 5230 B total
```

They are deliberately uncommitted: committing image assets before the code that uses them would leave
orphans in the tree. They belong to `10/00`, not to `11/01`. `cz.jpeg` became `cs.png` because the
selector chooses a LANGUAGE and the Czech language code is `cs`.

Then independently confirm all eight gates. **Do not run `npm run build` without first checking
`ss -tlnp | grep :3000`** — the Cooperator runs a dev server there and `next build` shares
`frontend/.next` with `next dev`. If it is occupied, ask him to stop it. **Never** use a broad pattern
kill such as `pkill -f next-server`; that pattern matches his own server and a previous Orchestrator
survived doing it only by luck.

If a gate this handout calls green comes back red, that is your first finding: stop, present the
contradiction, and issue nothing.

---

## 2. The two objectives, and what they are not

### 2.1 `10/00 ui-internationalization` — finish and close it

Landed and Cooperator-accepted:

```text
a5aff12  a dependency-free typed two-locale message system (en, sk), locale persisted on-device with
         first-visit browser detection, dynamic <html lang> and generateMetadata via a cookie read in
         the root layout, the landing/auth page, the api.ts error map, an Interface language panel, and
         the Game variant panel relabelled so it no longer claims "the interface stays English"
f26e92a  game-variant button descriptions removed at his request
1b7b05d  the starting-draw screen explained and localized, plus a latent tf() contract fix
```

He verified in his own browser: the whole logged-out landing/auth page in Slovak, all seven items
individually; diacritics `ľ ť í ž` render correctly in the gold gradient; console clean after a hard
reload; no flash of English.

**Remaining in `10/00`:**

```text
R1  the two "fancy" Settings dropdowns he described in detail: a flag image left of the language name,
    a search input with diacritic-insensitive autocomplete ("cestina" must match "Čeština"), and an
    arrow at the input edge that opens the dropdown. TWO of them — one for the interface locale, one
    for the game variant. He wants them eye candy, matching the existing premium chrome, not a plain
    white input. The five 48x32 PNGs are ready.
R2  the game-variant dropdown must read a DYNAMIC installed-variant list from Django, not a hardcoded
    union. That endpoint is designed in the 11/01 plan (section 12 of the planning report) — coordinate
    so it is built once. Today it shows two languages; after 11/02 it shows five, with no frontend change.
R3  the remaining ~330 English strings extracted into the en catalog with their Slovak counterparts.
    Areas: play, queue, draw (done), waiting, game, controls, board, overlay, chat, history, profile,
    prompt, settings, error, a11y.
R4  cs, pl, hu UI translations. Additive: one `messages.<locale>.ts` per locale typed
    `Record<TextKey, string>`, and `tsc` names every missing key. The `Locale` union grows from 2 to 5.
R5  the LocaleProvider for `uii-01-F04` — the server renders the body in English while <html lang> and
    <title> follow the Slovak cookie. Severity is LOW (he measured no console error and no flash), but
    it grows with R3: after R3 the entire server HTML would be English inside a lang="sk" document.
R6  remove the player-facing model picker AND the prompt-preset picker, so a player sees only a model
    name. NO database change: leave accounts.User.preferred_ai_model_id, its migrations, its admin
    field, and its is_selectable_model validation, and simply stop writing it from the player UI. That
    makes it admin-settable only, in the direction he wants. Locked fork 11 is NOT engaged.
R7  backend localization: Django USE_I18N + LocaleMiddleware after SessionMiddleware and before
    CommonMiddleware, axes ordering preserved and test_admin_login_brake.py re-run, Accept-Language
    sent by the API client from the store.
R8  uii-01-F01 — read the numeric Retry-After header instead of parsing "seconds" out of Django's
    English 429 body.
R9  orch-02-D11 — add SECURE_HSTS_INCLUDE_SUBDOMAINS, do NOT add SECURE_HSTS_PRELOAD.
R10 orch-01-F18 — the nonce CSP. This is the ONLY remaining proxy.ts touch in the whole, and it is a
    header concern, so the slice-07 constraint "it sets headers and nothing else" is NEVER reopened.
    Full loopback header re-proof afterwards against the audit-03 baseline.
R11 audit-01-F06 — the catalog proxies stop swallowing failures into an empty HTTP 200.
R12 uii-01-F02 accessible names (the product has ZERO aria-label, role, alt, tabIndex, sr-only) and
    uii-01-F03 dates taking the active locale instead of a hardcoded "en-US".
R13 his acceptance batch, including the three deferred S7b behaviours and the new-game-modal defect.
```

**There are NO URL locale prefixes.** Cooperator decision 7, 2026-09-01, permanent: no `/sk/`, no
`/en/`, no subdomain, not now and not later. He reasoned it himself and he was right — see
`PROJECT_CONTEXT.md` section 13 for the full cost analysis. That decision is what keeps `proxy.ts`
touched exactly once in this era.

### 2.2 `11/01 atomic-tile-token-foundation` — the engine architecture

One board cell holds exactly one atomic tile token; that token may contain one or more Unicode code
points. Hungarian is the forcing function: `SZ GY NY CS LY ZS TY` are single physical tiles, and today's
loader silently accepts **91 of 100** Hungarian tiles.

**What it is NOT:** it is not adding Czech, Polish, or Hungarian as playable variants. That is `11/02`
and it is blocked on dictionary files the Cooperator sources manually. It is not a general Unicode
framework, a plugin system, grapheme-cluster segmentation, RTL, or CJK. It is not Catalan, Welsh, or
Spanish — those are architecture counterexamples and one test-only canary.

---

## 3. You are Claude Opus 5 Thinking. These are your failure modes.

The previous two Orchestrators were the same model. Across the last two eras, **seven times** someone
other than the Orchestrator was right about a claim it was confident in — five Workers, once the
Cooperator, once a Worker again. The pattern is worth more than any generic caution.

1. **You state conclusions more precisely than your evidence supports.** The last Orchestrator predicted
   a guaranteed hydration mismatch and a visible flash of English, with "confidence: high", from code
   reading. The Cooperator opened his console and both predictions were false. Before you write
   "verified", name the command and what it would have missed.
2. **You approximate a contract instead of reading it.** It issued a planning prompt missing all six
   `Planning Record` fields because it had read the "Common Worker Task Fields" table and the report
   header but never opened `PROMPT_CONTRACTS.md:89`. The Worker blocked and was right. **Read the exact
   structural section for the exact artifact you are issuing.**
3. **A negative grep is not a conclusion.** Three instances in one week: `selection.py` provider
   constants; the Django password validators, which live in `django/contrib/auth/locale/sk/` and not
   `django/conf/locale/sk/`; and `rest_framework/locale/sk/`, which ships a compiled `.mo` with no
   `.po`. When a search returns suspiciously few results, widen the pattern and **state the exact
   pattern that failed to match.**
4. **Your own reconnaissance will be incomplete and a Worker will find the gap.** The last Orchestrator
   grepped `models.py` for `board_state|bag_tiles|variant_slug` and therefore never saw
   `GameSession.blanks` at `models.py:30` — an entire persistence surface, read and written at seven
   places in `services.py`. The planning Worker found it. Assume your file list is missing something and
   ask for a repository-wide sweep, classified.
5. **A green gate set is not a correct product.** Eight green gates — including typecheck, lint, build,
   and 342 frontend tests — coexisted with a document declaring `<html lang="sk">` and a Slovak
   `<title>` around an entirely English body. vitest runs with `environment: "node"` and nothing renders
   a page. **For anything that renders, render it, or do not claim it.** The technique: production build,
   `next start` bound to loopback on a non-default port, probe with an HTTP client, stop the server by
   **exact PID**.
6. **A faithfully executed prompt can still produce a defective product, and then the prompt is the
   defect.** `uii-01-F04` came from the Orchestrator's own contract, which made the client store the
   source of truth for the locale and called the server-readable cookie "a routing hint only". Classify
   that honestly as an Orchestrator design defect, not a Worker execution defect.
7. **Allowlists are too narrow.** Scope by what the **gates** will touch, not only what the change
   touches. Include the test files that the store or API type change can break.
8. **You read a remedy's shape but not its defaults.** `django-axes[ipware]` with default settings would
   have been a no-op, and one plausible half-step would have converted a DoS weakness into a full
   authentication-brake bypass. Read the installed `conf.py` before you name a fix.
9. **You let a shared reference go stale while carefully updating everything else.** When a fact
   changes, grep the whole file for the old value, not the section you were thinking about. Four stale
   claims were found in `PROJECT_CONTEXT.md` in one pass.

---

## 4. The accepted plan for `11/01`, with three corrections

The planning report is `planning-PASS`, accepted. Its verbatim text is **in the chat transcript and NOT
yet archived** — see section 9. `90_orchestrator-plan-acceptance.md` records the acceptance, the
verifications, and everything a future reader needs first.

### 4.1 Preserve these design decisions verbatim into the implementation prompt

```text
- the four-concept contract: atomic tile token / lexical contribution / container structure /
  code-point length. State for every layer which one it handles.
- lexical_contribution(token) and tile_display(token) as named IDENTITY extension methods now. No rich
  tile objects. Future Catalan-style behaviour changes behind those interfaces without touching
  containers.
- Cell = {token, blank_as} with realized_token. A regular cell is {token:"SZ", blank_as:null}; a blank
  playing CS is {token:"?", blank_as:"CS"}. This preserves physical blank identity AND removes the
  separate GameSession.blanks store.
- WordFound carries lexical `word`, realized `tokens`, and `coords`. Physical length is len(tokens),
  never a string length.
- ONE central gamecore.word_authority owning dictionary membership, two-tile authority, prefix checks,
  and optional forbidden physical sequences.
- evaluate_scoring_move becomes the SOLE authoritative legality path for both human and AI submissions.
- keep the wire placement key `letter` as a documented legacy name holding one atomic token. Do not
  duplicate the schema with a parallel `token` key; the pinned MOVE CORE uses `letter`.
- prefix probes over the UNION of main-dictionary prefixes and all prefixes of two-tile authority
  words, so ÁCS is reachable with no reverse segmentation anywhere.
- rename the concept with no alias: manifest key two_tile_words_file, loader load_two_tile_words,
  assets slovak_two_tile_words.txt / czech_… / polish_… / hungarian_…
- optional forbidden_token_sequences, checked against COMPLETE formed words, EMPTY for Hungarian. No
  prohibition is inferred for any language without evidence.
- readiness split: structural manifest parsing separate from playable loading. A manifest whose
  dictionary is absent stays discoverable but is `unavailable`, cannot create or queue a game, and
  never borrows English or Slovak resources. No dummy dictionaries, no silent fallback.
- GET /api/game/variants/ returning ONLY {slug, display_name, language_code, readiness}. No file
  paths, no filenames, no dictionary contents, no filesystem metadata, no readiness reasons.
- migrations 0008_purge_legacy_game_state and 0009_atomic_token_state_schema after leaf 0007.
- save-state schema "4"; restore accepts only 4 and rejects older versions clearly.
- E4 staging with fresh independent acceptance, and an R4 application audit because an R3 AI-boundary
  change is combined with an irreversible migration.
```

### 4.2 Correction 1 — the AI board grid must NOT use `#`

The plan proposes fifteen fixed-width occupancy rows using `.` and `#`. Measured:
`frontend/src/lib/prompts.ts:190` is `const GRID_ROW = /^[\p{L}.]{15}$/u`, so an occupied cell must
match `\p{L}` and `#` would be **rejected**; and `prompts.ts:136` tells the model the board renders as
`row 00 |...............| through row 14`.

`GRID_ROW` is not part of the hashed bytes — the hash is over `MOVE_SYSTEM_PROMPT`, i.e.
`moveSystemPromptFor(englishMoveSpec)` — so widening it would not break Lock B. But it would leave the
CORE telling the model one thing while the runtime sends another, which is the plan's own risk 13.

**Do this instead:** render an occupied cell as the **first code point** of its token. That is a letter,
so `GRID_ROW` matches unchanged, the CORE prose stays literally true, and rows stay fifteen characters.
The full token lives only in the sparse exact map the plan already designs — `(07,08)=SZ`,
`(08,08)=?→CS` — which is authoritative and resolves `S` versus `SZ`. No validator change, no new marker
the model was never told about, no tension with Lock B.

### 4.3 Correction 2 — do NOT delete the `AEIOU` leave term

The plan recommends removing the vowel-imbalance component of ranked leave quality
(`move_search.py:536` and `:540`) rather than adding variant vowel metadata.

**Rejected.** `PROJECT_CONTEXT.md` section 6 records that **the engine authors every move in this
product**: across a dozen counted live provider invocations the free LLM authored zero backend-valid
placements, and every completed live turn used `completion_source: backend_ranked_candidate`. Ranked
ordering is therefore not a secondary heuristic — it is literally what the player watches the AI play,
and the measured engine numbers (520–560 per side, ~29 plies, all 17 single-copy diacritic tiles
consumed) were produced under the current ranking.

Deleting the term changes shipped English and Slovak AI behaviour to fix a problem that exists only for
the new languages. **Add an optional variant `vowels` field defaulting to `"AEIOU"`.** Byte-identical
behaviour for English and Slovak, correct behaviour for the new variants, one field, nothing deleted.

### 4.4 Correction 3 — the alphabet invariant is a SUBSET, not set equality

The plan requires "an explicit `alphabet` whose set must equal all nonblank distribution tokens".
**That is impossible, and it would fail on the already-shipped Slovak variant.** Measured against the
authoritative orders the Cooperator sourced (section 5) and the real variant assets:

```text
locale  alphabet_order tokens   non-blank tile kinds   tiles missing from order   letters with no tile
en              26                     26                     none                (0)  —
sk              46                     41                     none                (5)  DZ DŽ CH Q W
cs              42                     39                     none                (3)  CH Q W
pl              32                     32                     none                (0)  —
hu              44                     38                     none                (6)  DZ DZS Q W X Y
```

`PROJECT_CONTEXT.md` locked fork 1 states outright that the Slovak set has **no CH/DZ/DŽ tiles**, so
`DZ`, `DŽ`, and `CH` are Slovak alphabet letters that will never be tiles. Hungarian's official
alphabet has 40 native letters including the three-character letter `DZS`, plus defined positions for
`Q W X Y`, none of which are in the standard Scrabble set.

**The correct invariant, in both directions:**

```text
REQUIRED   every non-blank tile token MUST appear exactly once in alphabet_order
FORBIDDEN  requiring the reverse. A letter with no tile is normal and expected.
ALSO       alphabet_order must be duplicate-free and NFC-normalized, and must be declared rather than
           derived from letters[]
```

And a consequence the plan does not state: **blank targets must come from the TILE SET ordered by
alphabet index, not from `alphabet_order`.** Otherwise a Slovak player could assign a blank to `CH`,
which is not a tile in that variant. `playable_letters` and the BlankPicker must both use tile tokens
sorted by alphabet position.

The Cooperator supplied this insight himself, before any code existed:
`alphabet_order = jazykové poradie tokenov; letters = fyzické Scrabble tiles`.

### 4.5 The eight decisions from planning-report section 21 — recorded verdicts

```text
1  two-whole split                        ACCEPTED  atomic-tile-token-foundation, then
                                                    czech-polish-hungarian-variant-activation
2  ALLOW_DESTRUCTIVE_GAME_STATE_RESET      ACCEPTED  default false, fail-closed, five named tables,
   fail-closed irreversible purge                    no blanket flush, no-op on an empty database
3  explicit alphabets required in manifest ACCEPTED  data now supplied — section 5
4  two_letter -> two_tile_words, no alias  ACCEPTED  renames a SHIPPED asset; assert rename + content hash
5  optional forbidden_token_sequences      ACCEPTED  empty for Hungarian
6  remove the AEIOU leave term             REJECTED  see 4.3
7  Lock B stays closed                     ACCEPTED  with correction 4.2 applied
8  activation blocked until dicts+licence  ACCEPTED  no dummy dictionaries, no fallback
```

---

## 5. Authoritative alphabet orders — Cooperator-sourced, Orchestrator-validated

He sourced these through language authorities and supplied primary references: JÚĽŠ SAV *Pravidlá
slovenského pravopisu* for Slovak; Ústav pro jazyk český AV ČR for Czech; Rada Języka Polskiego PAN for
Polish; MTA *A magyar helyesírás szabályai* for Hungarian. The Orchestrator validated all five for
duplicates, NFC, and the tile-subset invariant. All pass.

```text
en  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

sk  A Á Ä B C Č D Ď DZ DŽ E É F G H CH I Í J K L Ĺ Ľ M N Ň O Ó Ô P Q R Ŕ S Š T Ť U Ú V W X Y Ý Z Ž

cs  A Á B C Č D Ď E É Ě F G H CH I Í J K L M N Ň O Ó P Q R Ř S Š T Ť U Ú Ů V W X Y Ý Z Ž

pl  A Ą B C Ć D E Ę F G H I J K L Ł M N Ń O Ó P R S Ś T U W Y Z Ź Ż

hu  A Á B C CS D DZ DZS E É F G GY H I Í J K L LY M N NY O Ó Ö Ő P Q R S SZ T TY U Ú Ü Ű V W X Y Z ZS
```

Two caveats he flagged, both important:

- **Polish deliberately excludes `Q V X`.** They appear in loanwords but are not part of the 32-letter
  Polish alphabet, and the standard Polish Scrabble distribution has no such tiles. Do not add them.
- **Czech `alphabet_order` is NOT a dictionary collation.** Normed Czech sorting per ČSN 97 6030 treats
  `Á Ď É Ě Í Ň Ó Ť Ú Ů Ý` as their base letter at the primary level with diacritics deciding only
  secondarily. The array above is a deterministic total order for the game engine — tile order, starting
  draw, blank picker — and must be documented as such so nobody later reuses it as a universal word
  sorter. Czech is the only one of the five where that confusion is possible.

### Why this matters: a live defect it fixes

`uii-01-F07`, reproduced dynamically against the real Slovak variant through the real loader:
`_perform_starting_draw` decides who opens the board with `slot0_value <= slot1_value` on raw tile
strings, so `('Á' <= 'Z')` is `False` (code points 193 vs 90). All seventeen single-copy Slovak diacritic
tiles sort **after Z**, and a player drawing `Á` is treated as further from A than one drawing `Z`. In
the Slovak alphabet `Á` is second. This is shipped, today.

Note the instructive asymmetry: naive code-point order happens to place the Hungarian **digraphs**
correctly (`SZ` < `T`, `CS` < `D`, `GY` < `H`, `ZS` > `Z`) while being wrong for **every accented vowel**
in all four non-English languages. A plan that only thinks about digraphs misses this entirely.

---

## 6. The verified technical baseline for `11/01`

Every line measured at `1b7b05d`. Give these to the implementation Worker as confirmed leads that still
require its own inspection, and demand a classified repository-wide sweep beyond them.

```text
backend/gamecore/variant_store.py:177   if letter != "?" and len(letter) != 1: continue
backend/gamecore/variant_store.py:193   letters sorted by lt.letter — declared order discarded
backend/game/models.py:26               board_state = JSONField (list of 15 strings)
backend/game/models.py:30               blanks = JSONField — a SEPARATE blank-coordinate store
backend/game/models.py:32               bag_tiles = TextField(default="")
backend/game/services.py:272            grid.append("".join(row_chars))
backend/game/services.py:279 and :485   session.bag_tiles = "".join(bag.tiles)
backend/game/services.py:248            tiles=list(session.bag_tiles)  <- CHARACTER split
backend/game/services.py:372 and :558   bag_remaining = len(session.bag_tiles)   <- a COUNT from a length
backend/game/services.py:167            "alphabet": list(variant.playable_letters)
backend/game/services.py:237,258,267,274,370,482,497   the blanks store, read and written
backend/gamecore/state.py:44,49,111,120,121   save-state joins grid rows, racks, bag
backend/gamecore/state.py:160-193       restore_bag_from_save parses a bag string
backend/game/serializers.py:248         exchange child=CharField(max_length=1)
backend/game/serializers.py:269-277     _nfc_uppercase_letter requires len(nfc)==1 AND isalpha() AND upper
backend/gamecore/move_search.py:536,540 hardcoded "AEIOU"
frontend/src/app/api/ai/move/route.ts:123,127   Zod .length(1)
frontend/src/app/api/ai/move/route.ts:329       /^[\p{L}?]$/u
frontend/src/app/api/ai/move/route.ts:334,341   blankAs single code point
frontend/src/lib/prompts.ts:12          MOVE_PROMPT_VERSION = "pfr-s2-core-1"
frontend/src/lib/prompts.ts:136         the CORE's 15-row board description
frontend/src/lib/prompts.ts:190         GRID_ROW = /^[\p{L}.]{15}$/u
frontend/src/lib/prompts.test.ts:22,81  CORE_SHA256 = c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60
frontend/src/components/game/AIThinkingOverlay.tsx:70   word.toUpperCase().split("")
frontend/src/lib/types.ts:48            board: string[]
frontend/src/lib/rack.ts                isPlausibleRack, called at game/[id]/page.tsx:541 and :1541
frontend/src/hooks/useGameStore.ts      SelectedVariantSlug = "english" | "slovak"; persist version 3
backend/game/migrations/               leaf is 0007_consumedwsticket
db_table names                          game_session game_player_slot game_move
                                        game_chat_message game_consumed_ws_ticket
```

**Precision that matters:** `"SZ".isalpha()` is **True**. What blocks Hungarian is the `len(nfc) == 1`
half, not `isalpha()`. `isalpha()` blocks only a token containing punctuation, i.e. the Catalan `L·L`
case. A remedy aimed at `isalpha()` fixes nothing for Hungarian.

**Three defects live in one field.** `bag_tiles` is joined on write, split BY CHARACTER on read, and its
string LENGTH is reported as the number of remaining tiles. One `SZ` would store fine, restore as
`S` + `Z`, and count as two. `BAG_EMPTY_AND_PLAYER_OUT` is a real game-end reason that reads that count.

**Validated variant data:**

```text
variant     tiles  kinds  nominal pts  multi-char tokens          today's loader accepts
czech        100    40       205       none                        100
polish       100    33       190       none                        100
hungarian    100    39       235       SZ GY NY CS LY ZS TY (9)     91  <- drops 9
slovak       100    42       267       none                        100  (shipped)
```

The three Cooperator-supplied JSONs are arithmetically sound: 100 tiles, exactly 2 blanks, no duplicate
entries, NFC-clean, uppercase. Their exact text is in the chat transcript and in his message; the
implementation prompt must carry it verbatim.

---

## 7. The destructive migration — his authorization and its exact limits

Cooperator decision 2026-09-01, in his own words:
`obetovatelne - vsetky rozohrate vymazat predsa, su to len testovacie hry`.

```text
AUTHORIZED   deleting development game state through these five tables, in this order:
             game_chat_message, game_move, game_player_slot, game_session, game_consumed_ws_ticket
NOT AUTHORIZED  accounts.User rows, credentials, password_changed_at, the JWT blacklist,
             catalog_ai_model, catalog_ai_prompt, or ANY other table
NOT AUTHORIZED  manage.py flush, a raw DELETE without a named historical model, or anything on a
             database other than his development one
REQUIRED     a fail-closed setting ALLOW_DESTRUCTIVE_GAME_STATE_RESET defaulting to false, documented
             in backend/.env.example; abort before deletion if any row exists and the flag is false;
             return without requiring the flag if all five tables are already empty; record pre/post
             counts; assert all five empty afterwards; assert the protected tables unchanged; reverse
             raises IrreversibleError
REQUIRED     the plan must still document, in one short subsection, what a PRODUCTION deployment would
             have required — verified backup and restore rehearsal, maintenance window, exact counts,
             explicit opt-in — so a future reader without a throwaway database is not misled
```

⛔ Remember `PROJECT_CONTEXT.md` section 3: **never ask him for a destructive action.** He authorized
the migration's behaviour; the Worker executes it under an explicit flag. Do not ask him to run
`DELETE`, drop a database, or reset anything by hand.

Note what this simplification does NOT cover: `frontend/src/hooks/useGameStore.ts` persists to the
user's **localStorage** and no Django migration can clear it. It is at persist version 3 with a
`migrate` function. Decide whether version 4 is needed and what it does with a stale
`selectedVariantSlug`.

---

## 8. The locks, the invariant, and the traps

### Eleven locked forks — `PROJECT_CONTEXT.md` section 5 is authoritative. The four that bite here:

```text
LOCK A  the nine AI providers are FROZEN. No change to any provider list, constant, tier, exact model
        tuple, or provider documentation in provider-registry.ts, openai-compatible.ts,
        ibm-watsonx.ts, ai-runtimes.ts, backend/catalog/selection.py, README.md, or AGENTS.md.
LOCK B  ONE parameterized MOVE CORE with a pinned SHA-256, version pfr-s2-core-1, and ONE SSE route.
        No second CORE, no second route, no version bump. See correction 4.2 for how to satisfy this.
LOCK C  DEFAULT_MAX_ELAPSED_MS = 2000 and DEFAULT_RANKED_MAX_ELAPSED_MS = 750. Variant-specific bounds
        are explicit call kwargs, never changed defaults.
LOCK D  exactly six completion_source values. No seventh.
```

### The formed-word invariant — the most misread rule in this project

```text
Illegal iff a COMPLETE formed dictionary-word produced by a placement has length 2 and is outside the
variant two-letter lexicon. NEVER illegal because a LONGER formed word CONTAINS a two-letter string.
```

`OSAMENIU` is legal even though it contains `AM`. Generalizing this rule from "length 2 in code points"
to "two physical tiles" is the single easiest place in `11/01` to reintroduce a substring test. If any
part of the work implies `"am" not in word`, scanning the board for a letter pair, or enumerating pairs
to reject a longer word, that part has failed. Reference: `backend/tests/test_slovak_ranked_search.py`,
`_REJECTED_CROSSES` and `isdisjoint`.

### Execution route — the mandatory bounded deviation

`AGENTS.md` documents `poetry run ...`. **That route is not usable in a Worker boundary**: the Cursor
AppImage environment intercepts `python*` through inherited `APPIMAGE` / `ARGV0` / `APPDIR` /
`PYTHONHOME`. Every prompt must express the alternate as an explicit bounded deviation per RF-16:

```text
from backend/:
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
```

Never present ambient `python`, `python3`, or `poetry run` as a parallel canonical route. `poetry`
itself IS usable once the same variables are unset, so a dependency change uses
`env -u APPIMAGE -u ARGV0 -u APPDIR poetry add ...`.

### Four traps that have each cost a real session

```text
1  backend/pyproject.toml sets addopts = "-q". Another -q SILENTLY suppresses the pytest summary count
   line. Require plain -m pytest and require the summary quoted verbatim.
2  Running mypy on a NARROWED path set once hid 62 real errors behind a reported 12 for six consecutive
   Worker sessions. Always require the full documented scope.
3  npm run build and npm run dev share frontend/.next. Check ss -tlnp | grep :3000 first and STOP
   rather than killing anything. NEVER pkill -f next-server.
4  npm run build can report success while type errors exist, because tsconfig sets incremental: true.
   "The build passed" and "the code type-checks" are two separate claims. Say both.
```

### Git pattern, delegated by the Cooperator

One commit per slice, staged by **explicit path** (never `git add -A` or `git add .`), an explicit
pre-push `git ls-remote origin refs/heads/main` equality gate against the exact baseline, one non-force
fast-forward push, and a public readback comparing `ls-remote` with `git rev-parse HEAD`. Never force,
amend, rebase, reset, clean, stash, branch, or tag. Exactly one Orchestrator is active at a time.

---

## 9. Meta duties, and an incomplete archive you must finish

You have write access to `/home/agile/meta`. **The Cooperator commits Meta himself; write files, do not
commit or push Meta.** Follow `/home/agile/meta/README.md` exactly: filenames
`<worker-session>_<phase>_<meta-exchange-index>.md` and `<worker-session>_report_<meta-exchange-index>.md`,
Meta exchange index = AP exchange ordinal − 1, `<phase>` lowercase kebab-case and never `report`.
Archive a prompt/report pair only after the report exists. Contents are exact historical evidence —
**never edit a report to read better.**

✅ **The `11/01` archive is COMPLETE.** An earlier draft of this section said otherwise. That was true
when it was written at 18:08; the Cooperator completed the archive at 18:29. All four verbatim files are
on disk and were verified by size and hash:

```text
01_plan_00.md     35274 B   exchange 01 prompt   "You are a planning-only WORKER instance…"
01_report_00.md    4803 B   exchange 01 report   BLOCKED, carries the correct report header
01_plan_01.md     38557 B   exchange 02 prompt   "You are the SAME planning-only WORKER…"
01_report_01.md   40147 B   exchange 02 report   the accepted plan
```

Two recorded deviations, neither of which is a problem, both preserved as archived rather than silently
repaired, because Meta contents are exact historical evidence:

- `01_report_01.md` genuinely does NOT begin with `### Report for ORCHESTRATOR_CHAT`, and omits the
  coordinate echo, `status:`, and `phase-qualified result:`. It starts at
  `## 1. Repository and AP preflight evidence`. The Orchestrator initially suspected a paste boundary;
  the archived file proves the Worker omitted them. `01_report_00.md` carries all of them correctly. The
  report content is complete and was accepted; the header gap is recorded so a future reader does not
  conclude the file was truncated.
- `01_report_01.md` line 165 reads a mangled `bag_tiles` row where the source said
  `ordered string[]`. A truncation artifact of the same class already recorded for the `audit-02` report
  and the era-10 handout. Content is recoverable from the surrounding migration matrix.

A duplicate misfiled copy of all four files existed under `10/02-ui-locales-visegrad/` with `00_`
prefixes. It was verified content-identical, then deleted by exact path at the Cooperator's instruction
(`B15-1 zmaž`), after the survivors in `11/01` were confirmed present and hashed. **That directory no
longer exists, and there is no `ui-locales-visegrad` logical whole** — the Czech, Polish, and Hungarian
UI translations are section 2.1 R4 of `10/00`, not a whole of their own. If you see that name referenced
anywhere, it is stale.

Directory-numbering note so it is not read as an error: `11/01` is `01` rather than `00` because
`11/00-admin-provider-model-console/` was created earlier. Meta's `<logical-whole-sequence>` is an
archive-ordering key assigned at creation time, not a priority ranking. Execution order is `10/00`,
then `11/01`, then `11/02`, then `11/00`.

Orchestrator-authored non-exchange artifacts in these wholes use a `9N_` prefix — `90_`, `91_`, `92_` —
so they can never collide with a Worker-session ordinal. That mirrors the `99_closure.md` precedent.
It is a documented local deviation; Meta naming is storage policy, not AP meaning.

⛔ **Do NOT read the handouts in `10/00-product-acceptance-sweep/`, `10/01-player-model-choice-removal/`,
or `11/00-admin-provider-model-console/`.** Explicit Cooperator instruction, to avoid a loop — they are
handout prompts. Everything you need from them is already in `PROJECT_CONTEXT.md` sections 12 and 13,
`DEFECT_LEDGER.md`, and section 2.1 R6 of this handout. `product-acceptance-sweep` is superseded; its
items folded into `10/00`.

Keep `PROJECT_CONTEXT.md` and `DEFECT_LEDGER.md` current as you go. They are why downstream handouts do
not each carry a drifting copy of the same facts, and they rot quietly if you only update the section
you are thinking about.

---

## 10. The Cooperator

Read `PROJECT_CONTEXT.md` section 2 in full. The short version, because it changes how you write:

Address **Michal** in **Slovak**, masculine forms; refer to yourself in **feminine** forms. Worker
prompts and reports are professional **English**. Begin every message with the emoji signal that tells
him what to do, and **end every message with an explicit, emoji-annotated block of what he must do** —
never bury his action in prose. Label manual test steps with a batch prefix (`B14-1`, `B14-2`, …); plain
`1.)` collides with your own numbered list and has caused confusion.

His stake is material: he is preparing to present Libre Tiles at a **job interview** as evidence that he
can integrate AI into a real product. Presentability and correctness are first-class requirements.

He has granted full trust and asks for initiative. He is also emphatic that he is not the expert.
Neither transfers authority: RF-01 still reserves material product, cost, irreversibility, and
residual-risk decisions to him. **He has explicitly asked to be asked LESS.** His words:
`ja nebudem manualne tu testovat nic ... Chapeme sa, ze mi zadas len ked narazis na nieco problematicke`,
confirmed as option A — do not ask him to approve wording or small choices, decide and show the
reasoning; he will still report what he sees in the product and he remains the acceptance owner for
rendered output. Browser MCP is a locked fork, so **his eyes are the only instrument for rendered
acceptance** and asking him to look is the right tool, not a burden.

His replies are terse — `A`, `ano`, `hotovo`, `obetovatelne`. One one-word reply was once misread and
cost an entire Worker session, so **confirm an ambiguous short instruction in one line** before spending
a session on it. Every time he has been asked a sharp, well-evidenced question he has answered fast and
well, and twice his answer was better than the Orchestrator's recommendation — he rejected URL locale
prefixes and he supplied the `alphabet_order` / `letters` separation that section 4.4 is built on.

Two things he owes and has agreed to supply:

```text
- the full dictionary files czech.txt, polish.txt, hungarian.txt, sourced manually, with licensing
  and provenance evidence. 11/02 is blocked on them. Do NOT scrape, synthesize, or commit substitutes.
- nothing else. The alphabet orders are already supplied and validated.
```

Two artifacts **you** owe him, carried forward from two eras and requested three times:

```text
1  an expert Orchestrator handout for the VPS deployment whole, leading him step by step to a finished
   hardened deployment. He is a self-described complete novice at operations and named Prometheus and
   Grafana specifically as things he does not understand.
2  a prompt for a read-only Research Worker — he has ChatGPT Deep Research — for current VPS-hardening
   practice on Ubuntu Server 24.04, demanding versions and retrieval dates rather than unsourced "best
   practices", and framed so the researcher can honestly answer "this is disproportionate for a single
   demo VPS", particularly about Prometheus and Grafana.
```

The complete fact set those must carry — the Docker-Compose-plus-host-nginx topology decision, the exact
`DJANGO_NUM_PROXIES=1` and `$proxy_add_x_forwarded_for` arithmetic with both silent misconfigurations,
`audit-04-F01` and the trap in its obvious remedy, the `NEXT_PUBLIC_*` build-time inlining trap, and the
monitoring assessment — is written out in `10/00-ui-internationalization/00_handout.md` section 10 and
summarized in `PROJECT_CONTEXT.md` section 11. **Copy it from there; do not reconstruct it from memory.**
Deployment happens after the UI/UX work, by his decision 6.

---

## 11. Closure conditions

### `10/00 ui-internationalization`

```text
1  the interface is localized to Slovak with English retained and switchable, and to cs, pl, hu
2  both Settings dropdowns exist with flags, autocomplete, and the arrow, and he has accepted them
3  the player no longer chooses a model or a prompt preset
4  the three routed residuals are each corrected with evidence or re-recorded as accepted residuals
   with a complete Residual-Risk Decision record INCLUDING their existing Cooperator sign-off.
   Losing a sign-off at closure is a closure failure.
5  the security headers are re-proved on every document route and /api/ route after the nonce CSP
   change, by the loopback readback technique, against the audit-03 baseline
6  the two auth-message security properties (AC-SEC-1 and AC-SEC-2, in
   90_orchestrator-restoration.md section 7) hold in ALL locales
7  all eight standing gates green at the closing commit
8  his acceptance batch has been run and its results recorded
9  no active mutation, no active Worker
10 the Meta archive is complete, including a closure record
```

### `11/01 atomic-tile-token-foundation`

```text
1  the Hungarian acceptance fixture passes with at least TWO different multi-character tokens
2  the L·L synthetic canary passes, proving the implementation did not generalize only to
   len(token) <= 2 && isalpha()
3  English and Slovak gameplay regression suites unchanged, the Slovak two-tile behaviour preserved,
   the MOVE CORE hash and version proved unchanged, six completion sources intact
4  uii-01-F06 and uii-01-F07 corrected with regression tests that fail before the fix
5  the migration deleted exactly the five named tables and the protected tables are provably unchanged
6  fresh INDEPENDENT acceptance performed by a Worker that did not implement it, plus the R4
   application audit — mandatory, because persistence, migrations, request validation, wire format,
   core legality, and AI tool invocation all change
7  all eight gates green; no live provider probe was required
8  he has render-checked a single letter, SZ, GY, L·L, and a blank realized as CS on the board, the
   rack, the draw screen, the blank picker, and the AI candidate surface
9  Meta complete, including the four verbatim files named in section 9
```

---

## 12. What comes after you

```text
YOU    10/00  ui-internationalization  finish and close
       11/01  atomic-tile-token-foundation  slice F1 -> F4, then close
then   11/02  czech-polish-hungarian-variant-activation   blocked on his dictionaries
then   the deployment whole    handout and Research prompt STILL OWED — section 10
later  11/00  admin-provider-model-console   his stated single most important outcome:
              add providers and models and set the default from Django admin, with NO SSH, plus
              AI-vs-AI diagnostics in every variant and strength testing before promotion.
              PROJECT_CONTEXT.md section 12 carries his intent verbatim. Note the constraint recorded
              there: a strength metric must rest on the completion_source distribution and the
              provider_candidate rate, NEVER on final score, because final score is an engine number
              and is identical whichever model is plugged in.
later  de-hardcoding the nine AI providers   his declared future whole; LOCK A holds until then
```

The two wholes you hold are independent and can interleave: `10/00` is presentation and additive
localization at R1; `11/01` is an E4 engine and persistence change. Do not let one block the other, and
do not run two Workers mutating the tree at once — the one-commit-per-slice pattern plus the pre-push
equality gate makes concurrent mutation unsafe.

Sequencing recommendation, not a decision: land `11/01` slice F1 first. It is pure `gamecore` with no
app persistence, no frontend, and no provider surface, so it is the cheapest place to discover that the
architecture is wrong. Everything else in both wholes is reversible in a way F2's migration is not.
