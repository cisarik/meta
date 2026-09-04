# Deferred Cooperator acceptance batch — `13/00 multilingual-expansion-campaign`

Artifact class: **accumulating acceptance script. Evidence, not authority.**
Owned by the Orchestrator. Appended to at the moment each slice lands, never reconstructed
at the end.

## Why this file exists, and why it is owed

The Cooperator's standing instruction of 2026-09-03:

> *NECHCEM ABY SOM TU BOL AKO COOPERATOR POUZIVANY NA TESTOVANIE … CHCEM ABY SI PRACOVAL
> AUTONOMNE. OVEROVANIE … AZ NA KONCI VYVOJA. PROSIM PRETO MA NEVYRUSUJ.*

His observation is **deferred to the end of development**, delivered ONCE. The obligation
that creates: an acceptance step not run when it is generated must still be **written down**
when it is generated, or it will be reconstructed from memory at the end and be wrong.
`12/00` named this file as owed and did not open it. It is now open.

⛔ **Three things the autonomy grant does NOT waive, and protecting them is the
Orchestrator's job:**

```text
1  it does NOT lower an evidence tier. E3 still requires FRESH INDEPENDENT ACCEPTANCE, and
   that acceptance is a WORKER function, not a Cooperator function. Only his OBSERVATION is
   deferred. C1 is the only E3 slice in this campaign.
2  it does NOT remove the rendered-output rule: `for anything that renders, render it, or do
   not claim it`. Deferring his observation makes the Orchestrator's own loopback probe MORE
   necessary — production build, `next start` on a loopback port, HTTP client, stop by exact
   PID.
3  it does NOT touch decision 10 — he has no screen reader and will not install one.
   Accessibility claims are closed BY INSPECTION ONLY, permanently.
```

## Format

One entry per landed slice, appended at the moment it lands. Steps are labelled `B<n>-<m>`
so he can report a single failing step by name.

```text
slice        the internal identifier
commit       the exact SHA that landed it
what changed one line
steps        B<n>-<m>, each an EXACT observable expectation — what he does, and what he must
             see. Never "check that it works".
```

---

## B1 · exchange 01/01 — the deferred documentation chain

```text
slice        V9a + V9b
commits      4904e29  docs(prd): Collins 2019 replaces the stale SOWPODS references
             a199d0e  docs(env): document PRIMARY_DICTIONARY_FILE, the undocumented Tier-1 override
             pushed; public readback equals local HEAD at a199d0e
what changed libretiles_PRD.md stops naming SOWPODS as the Tier-1 dictionary;
             backend/.env.example documents the PRIMARY_DICTIONARY_FILE knob; one new test
             module mechanically guards both claims.
```

```text
B1-1  Open libretiles_PRD.md. Search it for `SOWPODS`, case-insensitively.
      EXPECT: zero matches.
B1-2  Read FR-01 (section 5). EXPECT: it names the Collins 2019 dictionary and the word
      count 279,496 — not SOWPODS and not 172,823.
B1-3  Read FR-05 Tier 1 and Tier 2. EXPECT: Tier 1 names the local Collins 2019 list;
      Tier 2 no longer argues from SOWPODS being comprehensive.
B1-4  Read NFR-02. EXPECT: the O(1) frozenset lookup claim is about the Collins list.
B1-5  Read Known Gaps. EXPECT: the Tier-2 line no longer says "if SOWPODS is sufficient".
B1-6  Open backend/.env.example. EXPECT: a commented block explaining
      PRIMARY_DICTIONARY_FILE — that it repoints the English Tier-1 dictionary, that the
      default is collins2019.txt, that a value bypasses the variant manifest and the
      provenance machinery, and that it should normally be left unset. EXPECT the variable
      itself to be COMMENTED OUT, so copying the example changes no behaviour.
B1-7  ⛔ NEGATIVE STEP. Confirm backend/assets/dicts/sowpods.txt is STILL PRESENT.
      This exchange deliberately does not delete it. Its deletion is a later slice, and a
      prompt that both establishes an asset is unreferenced and deletes it in one exchange
      is the exact defect class that nearly destroyed a referenced asset in era 12.
B1-8  Run, from the repository root:
        cd backend && env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest \
            tests/test_documentation_dictionary_claims.py
      EXPECT: 2 passed. This is the mechanical half — if someone reintroduces the stale
      dictionary name or changes the shipped lexicon without updating the PRD, this fails.
```

⚠ **What this batch cannot show him.** Documentation changes render nothing in the running
product. B1 is a read-and-confirm batch by nature. The first entry with a rendered
expectation will be the first language slice, and it will carry the loopback-probe evidence
the rendered-output rule requires.

---

## B2 · exchange 02/01 — the orphan-asset guard

```text
slice        MEC-V3d-guard
commits      4f6f38d  chore(dicts): remove obsolete SOWPODS dictionary file   ⛔ COOPERATOR'S OWN
             86ec39e  test(lexicons): no unclaimed file may sit in the shipped dictionary directory
             pushed; public readback equals local HEAD at 86ec39e
what changed the deleted orphan can never silently return, and no other unclaimed file may sit
             in backend/assets/dicts/ either. P14 names the one file; P15 is the class rule.
```

```text
B2-1  Confirm backend/assets/dicts/ contains exactly EIGHT files and no sowpods.txt:
        collins2019.txt  czech.LICENSE  czech.txt  polish.LICENSE  polish.txt
        slovak.LICENSE   slovak.txt     slovak_two_tile_words.txt
B2-2  Run, from backend/ :
        env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest \
            tests/test_lexicon_provenance.py -k "p14 or p15"
      EXPECT: 2 passed.
B2-3  ⛔ THE ONE THAT MATTERS, and it is a NEGATIVE step. Read the docstring of
      test_p15_every_present_dictionary_file_is_claimed_by_a_manifest and confirm it states
      that the invariant runs ONE DIRECTION ONLY — present implies claimed, never the reverse.
      EXPECT the docstring to name Hungarian as the reason. If a future contributor
      "tightens" P15 into a symmetric check, the Hungarian variant can never ship, because its
      lexicon is deliberately claimed-and-absent until a local build runs.
B2-4  Optional, and it is the fastest way to see the guard work: create an empty file
        backend/assets/dicts/zzz_delete_me.txt
      run B2-2 again, EXPECT P15 to FAIL naming zzz_delete_me.txt, then DELETE that file and
      confirm `git status --porcelain=v1 -- backend/assets/` is empty again.
      ⚠ Delete it. Leaving it there leaves the suite red.
B2-5  Confirm `manage.py validate_lexicons` still reports FIVE assets, 0 failed. The deleted
      file was never one of the five — that is precisely why it could rot unnoticed.
```


---

## B3 · eight new playable languages — `153ead7` · `dab6d0d` · `0deac4a` · `1eed5ed` · `51e08fe` · `8a50ded`

```text
slices       Afrikaans · Italian · Dutch · German · Portuguese · Danish · Swedish · Icelandic
what changed twelve variants ship where four did. Every one has a committed build script pinned to
             one upstream commit, a licence read before a byte was written, and a byte-exact --check
             reproduction. ZERO engine changes across all eight.
```

⚠ **This is the batch with rendered output, and the rendered-output rule applies:** *for anything that
renders, render it, or do not claim it.* B3-1 is therefore the load-bearing step.

```text
B3-1  ⭐ THE ONE THAT MATTERS. Start both servers (backend on 8000, frontend on 3000), open Settings,
      and look at the game-language picker.
      EXPECT: TWELVE entries — English, Afrikaans, Czech, Danish, Dutch, German, Icelandic, Italian,
      Polish, Portuguese, Slovak, Swedish. English first, then the rest alphabetically by display name.
      EXPECT: the four original languages show their flag; the eight new ones show NO flag and their
      server-provided English name. That is BY DESIGN — variantDisplayName() falls back to the server
      display_name and flagSrc is omitted when absent, so a backend variant never needs a UI edit to
      appear. Confirm it looks acceptable rather than broken.
B3-2  Pick Afrikaans, start a game, play one word. EXPECT: it is accepted. 148 267 words.
B3-3  Pick German, and try to play a word containing Ä, Ö or Ü. EXPECT: accepted — those are 6-, 8-
      and 6-point TILES and 155 641 words keep one. ⛔ If an umlaut is rejected, the partial fold
      became total and roughly that many playable words were destroyed.
B3-4  Pick Portuguese. EXPECT the bag to be 120 tiles with THREE blanks, and a Ç tile worth 3 points.
      ⇒ This is the step that proves bag size and blank count are data-derived, not hardcoded.
B3-5  Pick Icelandic and play a word containing Ð, Þ or Æ. EXPECT: accepted. All ten of Icelandic's
      non-ASCII letters are tiles and NOTHING is folded.
B3-6  Confirm the four original languages are unchanged: English, Slovak, Czech, Polish all still
      playable, and a Slovak word with Á still accepted (Slovak does NOT fold diacritics).
B3-7  ⛔ NEGATIVE STEP. Confirm Norwegian, Finnish, French, Malay and Hungarian are ABSENT from the
      picker. Each is a recorded blocker with a named cause, not an oversight:
        norwegian  no explicit upstream licence grant for the word list
        finnish    no plain affix pair upstream (Voikko)
        french     the expander yields ~77k of ~400k words
        malay      no ms_MY source; Indonesian must not be substituted
        hungarian  ~301 M forms; needs an opt-in local build
B3-8  From backend/: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py validate_lexicons`
      EXPECT: `13 asset(s) audited, 0 failed`.
```

## B4 · C1a, the wire format — `529e691`

```text
slice        MEC-C1a-third
what changed a multi-code-point tile now crosses the game-state wire losslessly, on both the
             placement and the exchange path. The temporary adapter is gone.
```

⛔ **This slice is NOT accepted yet.** It is E3 and its fresh independent acceptance
(`06_acceptance_00.md`) had not returned when this entry was written. **If that acceptance has not
happened, do B4-1 and stop — do not treat the rest as confirmation.**

> ⭐ **RECONCILIATION, 2026-09-04, prospective and not a rewrite.** The acceptance HAS since run. It
> returned `status PASS · acceptance-PASS · zero corrections`, archived as `./06_report_00.md`, from a
> session that neither designed nor implemented the candidate and was not a subagent of the
> Orchestrator. ⇒ **B4-1 is SATISFIED and B4-2 through B4-4 are live.** The paragraph above is kept
> exactly as written because it was true when written — `AP.md:322-336`: historical artifacts stay
> interpretable and are never retroactively rewritten.
> ⚠ **B4-2 remains the ONLY pixel evidence this slice will ever get.** The acceptance independently
> confirmed that no test in the repository renders the board component. Your eyes are the instrument.

```text
B4-1  ⛔ FIRST: confirm the independent acceptance of 529e691 exists and PASSED. If it does not
      exist, this entry is not ready and nothing below it counts.
B4-2  Open any game and confirm the board renders normally — tiles in the right squares, blanks
      shown as blanks. ⚠ No test in the repository renders the board component, so YOUR EYES are the
      only evidence for the visual path. The independent acceptance prompt asks about exactly this.
B4-3  Place a word, submit it, reload the page. EXPECT: the board is unchanged after reload. That
      exercises the new structured payload end to end.
B4-4  ⛔ KNOWN LIMIT, so you are not surprised: no shipped language has a digraph tile yet, so
      nothing you can play today needs the new wire format. Hungarian is its first real consumer.
      B4-2 and B4-3 confirm the change did not BREAK anything; they cannot confirm it ENABLED
      anything. That is honest, not a gap in your testing.
```

## B5 · two Orchestrator-direct repairs, session 07 — `fffc613` · `32312ba`

```text
slice        two independent one-file repairs. ⛔ NEITHER is part of the UI-localization
             objective; both are measured defects the continuation handout named as cheap.
commits      fffc613  fix(lexicons) the audit's positive probes cover all twelve variants, not four
             32312ba  docs(agents) "Not done yet" said live Slovak play is not enabled, and it plays today
             pushed; public readback equals local HEAD at 32312ba
what changed `validate_lexicons` now probes real word membership for all twelve dictionaries
             instead of four, so "13 asset(s) audited, 0 failed" finally means presence, shape
             AND membership; and AGENTS.md no longer states that Slovak play is disabled.
⛔ ORCHESTRATOR-DIRECT, so this evidence is PERMANENTLY NON-INDEPENDENT: no Worker saw either
   change and no independent session verified it. Mechanical gates are the only corroboration.
```

```text
B5-1  From backend/: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py validate_lexicons`
      EXPECT: `13 asset(s) audited, 0 failed` — exactly what B3-8 already expects.
      ⚠ THE OUTPUT IS DELIBERATELY UNCHANGED, and that is the whole point: the number was
      already green while eight of the twelve dictionaries had no membership probe at all. A
      passing audit cannot show you the difference, so B5-2 is the step that does.
B5-2  ⛔ THE STEP THAT ACTUALLY TESTS IT. Open
      backend/game/management/commands/validate_lexicons.py and read `_PRESENT_PROBES`.
      EXPECT: TWELVE rows, one per shipped variant — not four.
      Then, if you want to watch the guard fire, temporarily add `"madur"` to the `icelandic`
      row and re-run the command. EXPECT it to FAIL with
      `icelandic dictionary FAILED reason=probe_absent ... missing_probes=madur`. Remove it
      again. (`madur` is `maður` with a fold applied, and the Icelandic edition folds nothing,
      so its ABSENCE is the assertion. The same trick with `"musli"` on the `swedish` row also
      fails — Swedish ignores diacritics EXCEPT Ü.)
B5-3  Open AGENTS.md, section "Not done yet". EXPECT: no sentence claiming live Slovak play is
      not enabled. EXPECT instead one line stating that twelve variants ship playable and four
      have an interface locale. Cross-check the twelve against the Settings variant picker.
B5-4  ⛔ KNOWN LIMIT, stated so you are not surprised: README.md and libretiles_PRD.md STILL
      describe an English-only product and name no language other than English anywhere. That
      is campaign closure condition 11, deliberately deferred until the UI-localization work
      fixes the final numbers at twelve variants and twelve locales. Recorded debt, not an
      oversight.
```

⚠ **Numbering note for whoever appends next:** the eight interface catalogs get their own
entries from **B7 onward**, one per locale as it lands, per the standing obligation that an
acceptance step is written when it is generated and never reconstructed at the end.

## B6 · S1, the frozen interface key set and the CLDR plural pin — `cfd1215`

```text
slice        MEC-UIL-S1. The slice that had to come before the eight catalogs.
commit       cfd1215  feat(i18n) freeze the interface key set and pin twelve plural rules to CLDR
             pushed; public readback equals local HEAD at cfd1215
what changed the eight not-yet-localized variants now show a TRANSLATED NAME in Settings and in the
             human-queue label in all four existing locales, a rejected word finally names which of
             the twelve lexicons rejected it, and plural.ts carries a CLDR-correct helper for all
             twelve target languages with an executable test pinning each rule.
⛔ ORCHESTRATOR-DIRECT FINISH, so this evidence is PERMANENTLY NON-INDEPENDENT: a subagent Worker
   authored the implementation under prompt 07/01, correctly returned BLOCKED because that prompt was
   unsatisfiable, and I made the one-integer correction and landed it. No independent session saw it.
⛔ AND NO NEW INTERFACE LANGUAGE EXISTS YET. The chrome is still English for those eight. If you
   expect to find Danish menus, that is the NEXT slice, not this one.
```

```text
B6-1  Open Settings and look at the GAME VARIANT picker with the interface language on ENGLISH.
      EXPECT: twelve entries, and they read EXACTLY as before — Afrikaans, Italian, Dutch, German,
      Portuguese, Danish, Swedish, Icelandic among them, with no flag beside those eight.
      ⚠ THE ENGLISH VIEW MUST BE UNCHANGED. The eight new English values are byte-identical to the
      server names they replaced, so any visible difference here is a defect. Nothing to admire; this
      step exists to prove nothing broke.
B6-2  ⭐ NOW SWITCH THE INTERFACE LANGUAGE TO SLOVENČINA and look at the same picker.
      EXPECT: Afrikánčina · Taliančina · Holandčina · Nemčina · Portugalčina · Dánčina · Švédčina ·
      Islandčina, instead of the eight English names that were there before. That is the visible
      product change in this slice.
      Then switch to Čeština and to Polski and confirm the same eight are translated there too.
B6-3  Start a game in one of the eight — Danish is a good pick — and play a word that is NOT in that
      lexicon, with the interface on English.
      EXPECT: "Not in the Danish lexicon".  ⛔ NOT "Not in the game lexicon", which is what every one
      of those eight said before this commit.
      Repeat with the interface on Slovenčina. EXPECT: "Nie je v dánskom lexikóne".
B6-4  ⛔ THE ONE STEP ONLY YOU CAN ANSWER, and it is a QUESTION rather than a check.
      With the interface on Slovenčina, play an invalid word in the SWEDISH variant.
      It will say: "Nie je v švédskom lexikóne".
      ⇒ SHOULD THAT BE "vo švédskom"?  Czech vocalizes (`ve švédském`) and Polish vocalizes
        (`we włoskim`), and both match their own shipped rows. Slovak was left as plain `v` ONLY to
        stay consistent with the pre-existing "Nie je v slovenskom lexikóne", which has shipped for
        some time.
      ⇒ If `vo` is correct, then the OLD Slovak row is wrong too and it is a separate two-string fix.
        If `v` is correct, nothing changes. ⛔ Neither I nor the Worker is a native speaker and
        neither of us would guess. One word from you settles it, and it needs settling BEFORE the
        eight catalogs copy the pattern.
B6-5  ⛔ KNOWN LIMITS, so you are not surprised:
      · No new interface language exists. LOCALES is still en · sk · cs · pl.
      · No flags for the eight. That is your decision, not an omission.
      · The AI prompt still names only Slovak and Collins: ten of the twelve lexicons get a prompt
        that identifies neither their language nor their word list. Measured this session, recorded
        as its own future slice, and NOT part of this commit.
```
