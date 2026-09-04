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
