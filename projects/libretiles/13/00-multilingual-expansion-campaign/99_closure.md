# Closure-readiness record — logical whole `multilingual-expansion-campaign` (Meta 13/00)

**Logical-whole closure: NOT-CLOSED.**

⛔ **This file is deliberately NOT a closure declaration.** ⭐ TEN of the eleven closure conditions are now
satisfied — conditions 1 and 9 were closed by C1 landing and passing fresh independent acceptance, recorded
in section 3.1. ⛔ ONE remains and it is the Cooperator's act, not an engineering task: condition 8's
deferred acceptance batch is DELIVERED and UNANSWERED. A successor Orchestrator that reads this as "closed"
would be wrong, and one that reads the remaining condition as work would also be wrong.

```text
State commit at this record   3d7eae96d567a7004a927de45f53e16e2baf108f
AP pin                        9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   (detached, correct)
Public refs/heads/main        3d7eae96d567a7004a927de45f53e16e2baf108f   equal
Working tree                  git status --porcelain=v1 EMPTY
C1 slices                     cbb2865 (A) → 3d7eae9 (B), sequential, parent b50f84a
C1 independent acceptance     session 26, PASS, `26_report_00.md`
Written 2026-09-05, revised after the C1 acceptance, by the era-13 continuation Orchestrator.
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
    ✔ SATISFIED. ⭐ C1 LANDED WITH TESTS as two E3 slices, `cbb2865` and `3d7eae9`, and PASSED FRESH
      INDEPENDENT ACCEPTANCE (session 26, `26_report_00.md`). C4 is not-needed-with-measurement. C5 is
      landed-with-tests in the sense the condition asks — `variant_name` exists and carries eleven
      `display_label` test lines — with the honest caveat that zero of twelve manifests declare it, so its
      composed branch is untested by a shipped variant. C2 and C3 are re-dispositioned: C2 is absent and no
      shipped language needs it; C3's problem was solved IN THE LEXICON at build time for all eight new
      languages, which is the measurement the condition asks for, and it does NOT cover Turkish I/İ.
      ⚠ THE HONEST RESIDUE: Turkish remains unschedulable until `canonicalize_tile_token`'s plain `.upper()`
      is measured against Turkish casing. That is recorded, not hidden. See section 3.1.

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
    ✔ SATISFIED at the closing commit `3d7eae9`, and ⭐ TWICE INDEPENDENTLY: once by me and once by the
      session-26 acceptor, whose numbers matched mine exactly. Ruff, mypy 85 files, `manage.py check`, and
      `validate_lexicons` 13/0 re-run by me at `3d7eae9`; the acceptor additionally recorded pytest
      **813 passed / 4 skipped** in 362.77s, vitest **504 passed / 3 skipped / 507**, typecheck and lint
      exit 0, and a production build with ELEVEN dynamic routes and ZERO static.
      ⚠ `makemigrations --check --dry-run` exits 1 and is PRE-EXISTING — §3.4 establishes it is older than
      this campaign's first commit, with all four outputs hashing identically.
      ⚠ Superseded values from the earlier revision of this record, kept so the numbers are traceable:
      at `84ddf1f` the same gates gave pytest 745/4 and vitest 475/3/478. The rise is C1's two slices.

 8  the deferred acceptance batch delivered ONCE, at the end, per his autonomy grant
    ⚠ DELIVERED, UNANSWERED. `91_deferred-acceptance-batch.md` holds B1-B21, complete. B16-B21 were
      appended late and are marked honestly as reconstructed from commit bodies and fresh measurement
      rather than from contemporaneous notes, because the file's own "append at the moment it lands" rule
      was broken by seven commits during a run of provider failures.
      ⇒ ⭐ THIS IS THE ONLY REMAINING CONDITION AND IT IS THE COOPERATOR'S OBSERVATION, not an engineering
        task. Open for him: B13-3 (`chat` vs `chatt`), B10-3 (badge length), B7-3 (German terminology),
        plus four wording questions from later slices. ⚠ B21's DECISION is spent — he chose to build C1,
        it landed, it passed. §3.2.

 9  fresh independent acceptance for C1
    ✔ SATISFIED. Session 26, a separately launched session that implemented neither slice and was not the
      ORCHESTRATOR's subagent, returned **PASS** for C1 as a capability and for each slice individually.
      All six risk claims accepted. ⭐ ALL SIX NEGATIVE CONTROLS BEHAVED AS REQUIRED — a mutated scratch
      oracle failed its pinned-digest assertion, a missing `authority` raised `TypeError`, an unstructured
      multigraph context raised `UnstructuredMultigraphContextError`, a malformed `"?"` cell returned
      `malformed_board_cell` while staying occupied, no live caller of the deleted helper survives, and no
      language-slug branch controls game rules. ⇒ The oracle is an EXACT BASELINE COPY, not a
      reconstruction, verified by independent extraction and byte comparison. See `26_report_00.md`.

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

## 3. ⭐ WHAT C1 CLOSED, AND THE ONE THING THAT STILL BLOCKS CLOSURE

### 3.1 C1 landed and passed independent acceptance

```text
SLICE A  cbb2865  canonical cells and ONE formed-word authority. 27 paths. `Cell` storage inverted onto
         token/blank_as; `evaluate_scoring_move` requires a keyword `authority`; all SIX production authority
         sites re-pointed, including the human persisted-move verdict loop that never called the evaluator;
         two surviving one-character guards removed; `_word_passes_dictionary` DELETED.
SLICE B  3d7eae9  lossless AI context and truthful candidates. 13 paths, backend and frontend in ONE commit.
         A 15x15 cell grid and an ordered rack array replace a concatenated `list[str]` that reported row
         length 18 where it must be 15 and a rack string `'SZDZS?'` that rendered as SIX tiles from THREE.
         An unstructured multigraph context is REJECTED rather than reverse-segmented.
⭐ THE PROOF OBLIGATION AND HOW IT WAS MET. The old authority path was deleted, so nothing can compare
  against it any more except a frozen copy — and a frozen copy the implementer may edit is worthless. The
  discipline: freeze the baseline helper as a byte copy with a pinned digest, verify it agrees with the LIVE
  helper BEFORE deleting anything, compare it against the new authority over real lexicons, and keep it
  afterwards so an acceptor can diff it against the baseline git object.
     oracle digest   260bfe15306f4785eb015c3357e5b596cfe72eecd9f54807fdf0a88da2a36461
     re-derive       git show b50f84a:backend/game/services.py | sed -n '209,222p' | head -c -1 | sha256sum
     corpus          10 457 ordered tile pairs · 328 685 triples · 21 676 672 lexicon entries visited ·
                     17 245 796 realizable compared as real token sequences · 25 public queries x 12 variants
     result          ZERO shipped formed-word verdict differences · ZERO public-query differences
⭐ AND THE RULING THAT MAKES IT MEANINGFUL: verdict equivalence is required over SHIPPED legal tile
  configurations, NOT universally, because universal equivalence would preserve known multigraph defects.
  Five synthetic cases deliberately change verdict and one deliberately agrees; each new verdict is the
  correct one and each is a separate test.
✔ FRESH INDEPENDENT ACCEPTANCE: session 26, PASS, all six risk claims accepted, all twelve controls reported.
  Byte parity re-derived independently at all three commits — the three user prompts and the CORE digest
  `c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60` unchanged — plus 36 seeded draws and
  the deterministic witness and ranked-search results identical across baseline, Slice A and the candidate.
⛔ AND THE LIMIT BOTH COMMIT BODIES STATE: C1 MAKES NO NEW LANGUAGE PLAYABLE. Hungarian and Croatian still
  need tile distributions sourced, and Hungarian needs a lexicon `unmunch` cannot produce. Runtime readiness
  still reports exactly twelve playable variants. ⭐ The capability exists; the content does not.

### 3.2 ⛔ CONDITION 8 IS THE ONLY THING LEFT, and it is not engineering

`91_deferred-acceptance-batch.md` holds B1-B21, complete and delivered. ⛔ It is UNANSWERED. Three items
already await the Cooperator — B13-3 (`chat` versus `chatt` in Swedish), B10-3 (badge length), B7-3 (German
terminology) — plus four wording questions raised by later slices and B21, the only DECISION in the batch.
⭐ B21 IS NOW MOOT IN ITS ORIGINAL FORM: it asked him to choose between building C1, re-dispositioning
condition 1, or leaving the campaign open. He chose to build it, C1 landed, and it passed. ⇒ What remains of
condition 8 is his OBSERVATION of B1-B20, which his own autonomy grant defers to the end of development.

### 3.3 The three record corrections the acceptor found

```text
⭐ ALL THREE ARE MINE, ALL THREE ARE NON-BLOCKING, AND ALL THREE ARE VERIFIED:
 1  INFO. My acceptance prompt §9 said the user prompt for a given board is "pinned nowhere in the test
    suite". ⛔ STALE AT THE CANDIDATE. `prompts.test.ts` now holds `BASELINE_USER_PROMPT_SHA256` with all
    three digests plus a legacy/structured equivalence test — Slice B's Worker acted on its own LEAD and
    added the permanent pin. ⇒ I wrote that section from the exchange-01 report's world while the final tree
    was in front of me.
 2  LOW. Both commit bodies say `playerslot.rack` "diverges the same way" as `board_state` — a qualified
    default-path mismatch. ⛔ MEASURED: `0001_initial.py:52` says `help_text='Current rack letters as list of
    strings'` and `models.py:86` says `'…rack tokens…'`. It is a HELP_TEXT drift, letters versus tokens.
    Only `board_state` has the default mismatch. ⇒ I repeated a Worker's framing without measuring it.
 3  INFO. "Six synthetic disagreements", which I propagated into two prompts, two commit bodies and the
    notes, overstates by one: `test_case_3_three_tiles_in_main_dictionary_both_true` deliberately asserts
    AGREEMENT. ⇒ FIVE disagreements plus ONE agreement control, and the agreement control is the more
    interesting of the two shapes because it proves the routing does not over-trigger.
⇒ ⛔ COMMIT BODIES ARE IMMUTABLE. These corrections live here and in `00_notes.md` §65, which is the only
  honest place for them.
```

### 3.4 The `makemigrations` failure predates the whole campaign — now established

```text
The acceptor confirmed exit 1 with identical output at the baseline, Slice A and the candidate, all three
hashing to `3cfe882f326d61c161955b459a4f2ed14d5c406572cde93bde0871a4e8e76067`, and correctly noted it had
NOT established that the failure predates the whole campaign.
✔ I ESTABLISHED IT. Migration `0008_atomic_token_state_schema` was added by `8c00a33`, which
  `git merge-base --is-ancestor` confirms is an ancestor of `fffc613`, this campaign's FIRST commit. Running
  the gate against a `git archive` export of `8c00a33` gives exit 1 and the SAME digest
  `3cfe882f326d61c161955b459a4f2ed14d5c406572cde93bde0871a4e8e76067`.
⇒ ⭐ SO THE DRIFT IS OLDER THAN THE CAMPAIGN AND UNTOUCHED BY IT. Cause: `0008` defines a local
  `default_structured_board` instead of importing the model's, and Django compares a JSONField default by
  qualified path. Aligning it is a separate change with its own risk and no campaign condition requires it.
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
    present). Meta is complete at this record. ✔ The C1 acceptance is DONE (§3.1). ⛔ Only the batch
    remains — §3.2.
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
· ⭐ ADDED BY THE C1 INDEPENDENT ACCEPTOR, session 26, and each verified by it directly:
    · `backend/tests/diagnostics/test_turn_probe.py:137` still writes joined-string board rows, which the
      structured loader SKIPS ⇒ those scenarios replay on an EMPTY board and pass for the wrong reason.
      ⭐ A green test that exercises nothing is worse than a red one.
    · `backend/gamecore/lexicon_health.py:16` retains an obsolete `services.py:216` authority citation;
      that line no longer holds the two-code-point floor after Slice A.
    · `frontend/src/lib/prompts.ts:480` prints a PREMIUM LEGEND while the AI projection carries no premium
      locations at all — a different lossiness from tile boundaries, and closing it would move prompt bytes
      for twelve shipped languages, so it needs its own slice and its own byte-parity oracle.
· ⚠ migration `0008`'s local `default_structured_board` versus the model's, which keeps
  `makemigrations --check` at exit 1 forever. Established (§3.4) as older than this campaign's first commit.
```

## 7. Successor obligations

```text
⛔ THIS CAMPAIGN IS OPEN, on ONE condition and it is not engineering:
  1  condition 8 — the Cooperator's OBSERVATION of `91_deferred-acceptance-batch.md` B1-B20, delivered
     once, at the end, by his own autonomy grant. ⛔ NOT an implementation task and not a successor's to
     discharge. ⚠ B21's decision is spent: he chose to build C1, it landed, it passed.
✔ CONDITIONS 1 AND 9 ARE CLOSED. C1 landed as `cbb2865` + `3d7eae9` and PASSED fresh independent
  acceptance in session 26. ⛔ Do not reopen them; do not re-audit them. `AP.md:1395-1405` — an audit
  finding never authorizes recursive audit.
⇒ THE REAL REMAINING WORK, WHICH IS NOT A CLOSURE CONDITION:
  ·  six of the seven licence-clean rows need TILE DISTRIBUTIONS sourced from a language authority.
     Neither code nor law, and the campaign's actual bottleneck.
  ·  TURKISH is unschedulable until `canonicalize_tile_token`'s plain `.upper()` is measured against
     Turkish casing — `I` and `İ` are different letters and Turkish casing is not Unicode default casing.
  ·  second-opinion review of the eight machine-authored interface catalogs.
  ·  the ledger candidates in §6, including the three the C1 acceptor added.
⭐ AND THE NUMBER TO PRESENT, WHICH IS A SUCCESS AT TWELVE RATHER THAN A FAILURE AT TWENTY-FOUR:
  twelve playable board languages with twelve interface locales, seven more licence-clean and waiting on
  data, five blocked with named and evidenced causes. Every one of the twenty-four is dispositioned.
```
