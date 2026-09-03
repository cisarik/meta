### Report for ORCHESTRATOR_CHAT

logical whole multilingual-expansion-campaign, Worker session ordinal 01, Worker exchange ordinal 01

**Status:** PASS

**Phase-qualified result:** implementation-PASS

**Result artifact or commit:** `a199d0e4086231a5f39853cbca0a94e7c734a37a` (two commits: `4904e29` then `a199d0e`)

**Result evidence:** both new tests proven failing against the unmodified files then passing after the change; five PRD lines corrected exactly as enumerated; one commented block appended to `backend/.env.example`; `git grep -in "sowpods" -- libretiles_PRD.md` → ZERO; `sowpods.txt` still present; `backend/assets/` byte-untouched; all eight standing gates green with only the two expected pytest counts moved; non-force fast-forward push with public readback equal to local `HEAD`.

**Start commit:** `ad4ce038e1bd3511bdd5b7431eb9c163d4788130`
**End commit:** `a199d0e4086231a5f39853cbca0a94e7c734a37a`

---

## Section 2 repository gate — verbatim values

```text
git rev-parse HEAD                    ad4ce038e1bd3511bdd5b7431eb9c163d4788130   MATCH
git rev-parse HEAD:.ap                9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   MATCH
git -C .ap rev-parse HEAD             9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   MATCH (detached, correct)
git status -sb                        ## main...origin/main                      MATCH
git status --porcelain=v1             (empty)                                    MATCH
git ls-remote origin refs/heads/main  ad4ce038e1bd3511bdd5b7431eb9c163d4788130   MATCH
ss -tlnp | grep -E ':(3000|8000)'     no match, grep exit 1                      no listener
ls backend/assets/dicts/sowpods.txt   present, 1743531 bytes, aug 23 16:03       PRESENT
```

No recovery class was activated: every gate value matched on the first measurement.

### End-of-task re-confirmation

```text
git status --porcelain=v1                       (empty)
git status --porcelain=v1 -- backend/assets/    (empty)
ls backend/assets/dicts/sowpods.txt             backend/assets/dicts/sowpods.txt   PRESENT
git rev-parse HEAD:.ap                          9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD                       9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git status -sb                                  ## main...origin/main
ss -tlnp | grep -E ':(3000|8000)'               no match (before build and at end)
```

`.ap` was never attached, updated, or written. No path was deleted. No temporary file was created anywhere (`/tmp/opencode/mec-v9ab/` was never needed and does not exist).

---

## Changed files and purpose

| Path | Purpose |
|---|---|
| `libretiles_PRD.md` | five enumerated lines only: SOWPODS → Collins 2019, `172,823` → `279,496` |
| `backend/.env.example` | one appended commented `# Game assets` block documenting `PRIMARY_DICTIONARY_FILE` |
| `backend/tests/test_documentation_dictionary_claims.py` | NEW: two-assertion mechanical guard (D1, D2) |

Exactly the three allowlisted paths. No other path in the tree was read-modified. `backend/config/settings.py` was read at lines 355–394 and not changed.

---

## `git grep` counts for `sowpods` — all four numbers

```text
BEFORE the edit
  git grep -n  "sowpods"                          0   (exit 1)
  git grep -in "sowpods"                          5   (all uppercase, all in libretiles_PRD.md)

AFTER the edit
  git grep -n  "sowpods"                          0
  git grep -in "sowpods"                          0
  git grep -in "sowpods" -- libretiles_PRD.md     0   (the stopping-condition measurement)
```

The five pre-edit hits were exactly `libretiles_PRD.md:35,65,66,127,150` — identical to the prompt's enumeration, verified line-for-line before editing.

⚠ **The tree-wide count is no longer zero after the commit, and this matters to the later deletion slice.** Measured at `a199d0e`:

```text
git grep -n  "sowpods"    2   both in backend/tests/test_documentation_dictionary_claims.py
git grep -in "sowpods"    3   all three in that same new file (lines 3, 34, 38)
git grep -in "sowpods" -- . ':!backend/tests/test_documentation_dictionary_claims.py'    0
```

The guard test must name the string it forbids, so the string necessarily survives in the guard. The PRD-scoped count — the one the stopping condition names — is ZERO.

---

## The exact diff of all five PRD lines

```diff
@@ -35 +35 @@ FR-01
-- English tile distribution (100 tiles, SOWPODS dictionary with 172,823 words).
+- English tile distribution (100 tiles, Collins Scrabble Words 2019 dictionary with 279,496 words).
@@ -65,66 +65,66 @@ FR-05
-- Tier 1: Local SOWPODS dictionary (in-memory frozenset, O(1) lookup).
-- Tier 2: Online dictionary API for words not in SOWPODS (optional, SOWPODS is comprehensive).
+- Tier 1: Local Collins 2019 dictionary (in-memory frozenset, O(1) lookup).
+- Tier 2: Online dictionary API for words not in the Collins 2019 list (optional; the local list is comprehensive).
@@ -127 +127 @@ NFR-02
-- SOWPODS dictionary lookup: O(1) via frozenset.
+- Collins 2019 dictionary lookup: O(1) via frozenset.
@@ -150 +150 @@ Known Gaps
-- Online dictionary API (Tier 2) may not be needed if SOWPODS is sufficient.
+- Online dictionary API (Tier 2) may not be needed if the local Collins 2019 list is sufficient.
```

Line `:33` (`FR-01: Game Core (English Variant)`), line `:149` (multiplayer deferred to v2), and every other line of the file are byte-identical: the committed diff shows five changed lines and no others.

## The exact diff of the `.env.example` block

```diff
@@ -66,3 +66,15 @@ DYNAMIC_FREE_MODEL_CATALOG_ENABLED='false'
  # Spelling must match backend/config/settings.py exactly.
  # A pre-existing .env overrides code defaults and is read once at process start.
  ALLOW_DESTRUCTIVE_GAME_STATE_RESET='false'
+
+# Game assets
+# PRIMARY_DICTIONARY_FILE repoints the ENGLISH Tier-1 dictionary at a different
+# basename under backend/assets/dicts/. Default: collins2019.txt (279,496 words).
+# Normally leave this unset.
+# A value here BYPASSES the variant manifest and the lexicon-provenance
+# machinery: backend/assets/variants/english.json still declares
+# dictionary_file collins2019.txt, and manage.py validate_lexicons still audits
+# the manifest's file, so an override is invisible to both.
+# Consumed by backend/config/settings.py as PRIMARY_DICTIONARY_PATH.
+# A pre-existing .env overrides code defaults and is read once at process start.
+# PRIMARY_DICTIONARY_FILE='collins2019.txt'
```

The variable stays commented out. The appended block is pure ASCII (verified: `awk 'NR>=69' | grep '[^ -~\t]'` exits 1). Single quotes on the commented value. `# Game assets` matches the file's bare-comment section style. File went 68 → 80 lines, trailing newline preserved. `backend/.env` and `frontend/.env.local` were never read or printed.

---

## Manifest value read, and the string asserted

```text
backend/assets/variants/english.json
  dictionary_file                       "collins2019.txt"
  lexicon_provenance.entry_count        279496          type: int
  f"{entry_count:,}"                    "279,496"       <- the exact needle D2 asserts
```

I did not re-derive the number by counting the file. The manifest is the authority, and it agrees with the two independent sources the prompt names: `validate_lexicons` reported `english dictionary ok reason=ok words=279496`, and the asset's own header line declares 279,496.

---

## Test table, with both Class B pre-fix failures verbatim

| ID | Test | Before the fix | After the fix |
|---|---|---|---|
| D1 | `test_d1_prd_never_names_a_dictionary_the_product_does_not_ship` | FAILED | passed |
| D2 | `test_d2_prd_word_count_equals_the_english_manifest_entry_count` | FAILED | passed |

Pre-fix run against the unmodified `libretiles_PRD.md`, `2 failed in 0.06s`:

```text
E       AssertionError: libretiles_PRD.md names 'sowpods' (case-insensitive) on line(s)
        [35, 65, 66, 127, 150]; the shipped Tier-1 dictionary is
        backend/assets/dicts/collins2019.txt (Collins Scrabble Words 2019)
E       assert 'sowpods' not in '# libre til...imization.\n'
E         'sowpods' is contained here:
E           00 tiles, sowpods dictionary with 172,823 words).
```

```text
E       AssertionError: libretiles_PRD.md does not publish the English word count 279,496
        declared by backend/assets/variants/english.json
E       assert '279,496' in '# Libre Tiles — Product Requirements Document\n\nUpdated: August 25,
        2026\n\n## 1. Product in One Sentence\n\nLibre T...r this product direction.\n8. **Phase
        8**: CI/CD (GitHub Actions), E2E tests (Playwright), performance optimization.\n'
```

D1's failure message lists the five 1-based line numbers, as required. Post-fix: `2 passed in 0.01s`.

The module is standard library only (`json`, `pathlib`), no Django database, no network, no subprocess, no new dependency. D2 reads the manifest, never `settings.PRIMARY_DICTIONARY_PATH`. It does not re-assert `entry_count` against the real lexicon word count — `test_lexicon_provenance.py` P4 owns that. No test asserts anything about `sowpods.txt`'s presence or absence.

---

## The eight standing gates

RF-16 route binding used as authorized: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/…` from `backend/`. `.venv/bin/python` and `.venv/bin/ruff` both present; the deviation worked on first use; ambient `python3` and `poetry run` were never used. `manage.py check` and `manage.py validate_lexicons` were invoked without `-m`.

| # | Gate | Quoted result | vs baseline |
|---|---|---|---|
| 1 | `mypy config game gamecore accounts catalog` | `Success: no issues found in 85 source files` | identical, **85 files** |
| 2 | `ruff check .` | `All checks passed!` | identical |
| 3 | `manage.py check` | `System check identified no issues (0 silenced).` | identical |
| 4 | `pytest` | `540 passed, 4 skipped in 241.89s (0:04:01)` | 538 + **N=2**, skips unchanged |
| 5 | `npm run typecheck` | exit 0, no diagnostics | identical |
| 6 | `npx vitest run` | `Test Files  31 passed \| 1 skipped (32)` / `Tests  450 passed \| 3 skipped (453)` | identical |
| 7 | `npm run lint` | exit 0, no output | identical |
| 8 | `npm run build` | exit 0, `✓ Compiled successfully`, **ELEVEN ƒ dynamic routes, ZERO static** | identical route table |

`pytest --collect-only` → **`544 tests collected in 6.77s`** = 542 + the same **N=2**. Exit 0.

Plain `-m pytest` was used with no second `-q`, so the summary is the real one. mypy ran the full documented scope, neither narrowed nor widened; `backend/tests/` is outside mypy scope and the new module is ruff-clean under `line-length = 100`. `ss -tlnp | grep -E ':(3000|8000)'` returned no match immediately before `npm run build`.

Wall-clock: 241.89 s against the recorded 242.04 s on an identical count. Machine noise, not a finding.

`manage.py validate_lexicons`, run after all edits:

```text
czech dictionary ok reason=ok words=3930497 duplicates=0 non_nfc=0
english dictionary ok reason=ok words=279496 duplicates=0 non_nfc=0
polish dictionary ok reason=ok words=3721704 duplicates=0 non_nfc=0
slovak dictionary ok reason=ok words=3005250 duplicates=0 non_nfc=0
slovak two_tile ok reason=ok words=103 duplicates=0 non_nfc=0
validate_lexicons: 5 asset(s) audited, 0 failed        exit 0
```

Five assets, zero failed — the cheapest proof no shipped asset changed, corroborating the empty `git status --porcelain=v1 -- backend/assets/`.

**Both frontend claims, stated separately:** the frontend **type-checks** (`npm run typecheck` exit 0, and `next build` independently reported `Finished TypeScript in 1567ms` with no error), and the frontend **builds** (`npm run build` exit 0, eleven dynamic routes, zero static).

---

## Git sequence

```text
git add libretiles_PRD.md backend/tests/test_documentation_dictionary_claims.py
  staged set: A backend/tests/test_documentation_dictionary_claims.py
              M libretiles_PRD.md                       exactly the two paths
git commit -> 4904e29  "docs(prd): Collins 2019 replaces the stale SOWPODS references"
              2 files changed, 77 insertions(+), 5 deletions(-)

git add backend/.env.example
  staged set: M backend/.env.example                     exactly that one path
git commit -> a199d0e  "docs(env): document PRIMARY_DICTIONARY_FILE, the undocumented Tier-1 override"
              1 file changed, 12 insertions(+)

git status --porcelain=v1                    (empty)
git status --porcelain=v1 -- backend/assets/ (empty)
PRE-PUSH GATE  git ls-remote origin refs/heads/main
               ad4ce038e1bd3511bdd5b7431eb9c163d4788130   equals the exact baseline
git push origin main
               To https://github.com/cisarik/libretiles
                  ad4ce03..a199d0e  main -> main          non-force fast-forward, exit 0
READBACK       git ls-remote origin refs/heads/main
               a199d0e4086231a5f39853cbca0a94e7c734a37a
               git rev-parse HEAD
               a199d0e4086231a5f39853cbca0a94e7c734a37a   EQUAL
git log --oneline -3
  a199d0e docs(env): document PRIMARY_DICTIONARY_FILE, the undocumented Tier-1 override
  4904e29 docs(prd): Collins 2019 replaces the stale SOWPODS references
  ad4ce03 feat(lexicons): --check re-verifies a committed asset without writing to it; pin the expander
```

No force, amend, rebase, reset, clean, stash, branch, or tag. No `git add -A` or `git add .`. Network use was exactly the three authorized operations: two `git ls-remote` and one `git push`.

---

## Deviations, risks, missing evidence

**Deviations:** one, and it is the authorized RF-16 route binding in section 8 — `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/…` instead of `poetry run`. Bounded to this task; it did not become a second standing route.

**Risks:** the guard is a substring guard on prose, so it constrains the two exact claims it names and nothing wider. It cannot detect a future PRD sentence that misdescribes the dictionary without using the word `sowpods` or a wrong formatted number. D2 asserts the correct string is *present somewhere* in the document; it would not catch a second, contradictory count added elsewhere in the file.

**Missing evidence:** none for this task's claims. Not attempted, by scope: any reference to `sowpods.txt` from an operator's uncommitted `backend/.env` — that surface is unreadable to me by prohibition and unsettleable by any source grep, which is exactly why section 5 documents the override instead of relying on a grep.

**Resolved Execution Issues / Near-Misses:** the section 4 quotes matched the file byte-for-byte, so no interpretation was needed. One near-miss worth naming: I ran the tree-wide `git grep` again at the end and it returned 3 rather than 0. That is not a regression — the guard test must contain the string it forbids — but a later slice that re-runs the prompt's original tree-wide command and reads a non-zero result as "still referenced" would draw the wrong conclusion. It is recorded under MEASURED below.

**Pre-Existing Failure Classification:** not applicable. Zero failures at any gate. Comparison baseline `ad4ce038e1bd3511bdd5b7431eb9c163d4788130` (predating this whole logical whole) was green on all eight gates as the Orchestrator recorded, and every gate is green at `a199d0e` with the two expected count movements and no others.

---

⚠ **WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE**

**MEASURED**

1. **`backend/.env.example` is not ASCII-only, contrary to section 5's stated premise.** `LC_ALL=C grep -n '[^ -~\t]'` returns three pre-existing hits — lines 2, 12 and 45, all U+2014 EM DASH (`# Libre Tiles — Backend…`, `…process start — review it…`, `# CORS — frontend origins…`). The instruction "The file has no non-ASCII byte and no emoji; match it" rests on a false measurement. I obeyed the operative half — my appended block is pure ASCII — and left the three existing em-dashes untouched under the "beyond appending the one block" prohibition. A future prompt should not reuse that premise as fact.

2. **The tree-wide `sowpods` grep is now 3 case-insensitive / 2 case-sensitive, all inside the new guard test** (`backend/tests/test_documentation_dictionary_claims.py:3,34,38`). The unreferenced-asset premise the deletion slice depends on is now proved by an *excluding* grep, not a bare one: `git grep -in "sowpods" -- . ':!backend/tests/test_documentation_dictionary_claims.py'` → 0. Given the era-12 history in section 1, the deletion prompt should specify that exact scoped form; a bare `git grep -in "sowpods"` returning 3 will otherwise read as "still referenced".

3. **`PRIMARY_DICTIONARY_FILE` has a fourth consumer class the prompt's set did not name: no lexicon-health or manifest-agreement gate reads it at all.** `validate_lexicons` audits `variant.dictionary_path` from the manifest and `test_lexicon_provenance.py` P4 audits the same manifest path. So an operator override changes what `submit_move` validates against while every asset gate keeps reporting `english dictionary ok words=279496`. The prompt described this as "invisible to both", which understates it: there is no gate anywhere that would notice. My `.env.example` block documents the hazard, as authorized; nothing detects it.

4. **`libretiles_PRD.md` still has one dictionary-adjacent inconsistency the five lines did not resolve.** `:33` names FR-01 "Game Core (English Variant)" and `:35` now says "Collins Scrabble Words 2019 dictionary with 279,496 words", but `validate_lexicons` audits **five** assets across four variants. The English line is now true; the section heading that contains it still implies English is the only variant. Out of scope by section 4.2 and deliberately not touched.

**LEAD**

5. `docs/architecture.md` and `README.md` were not read (both are prohibited paths). I have not measured whether either carries the same stale dictionary name or the `172,823` figure. The `172,823` number appeared nowhere else in a tracked file only per my own PRD-scoped measurement — I did not grep the tree for it. Unproven; a cheap first step for the campaign-closure PRD refresh is `git grep -n "172,823"` plus a case-insensitive dictionary-name sweep across `README.md` and `docs/`.

6. D2's needle is a formatted decimal string, so it would also be satisfied by an unrelated `279,496` appearing anywhere in the PRD. Today the only occurrence is the intended one at `:35`. Tightening it to require the number adjacent to a dictionary phrase is possible but would couple the guard to prose wording; I judged the looser form correct for a documentation guard and did not measure alternatives.

7. Section 4.2's other two stale items (`:33` FR-01 title, `:149` "multiplayer deferred to v2" while multiplayer is live per AGENTS.md) plus the file's total silence on variants, UI locales, lexicon provenance and readiness suggest the PRD is stale enough that a reader could take FR-10 "implementation planned for v2" as current. Suspected material for the campaign-closure refresh; not measured beyond re-reading the file.

---

**Smallest next step:** authorize the deletion slice for `backend/assets/dicts/sowpods.txt`, with its unreferenced-asset gate written as the path-excluding grep in MEASURED item 2 rather than a bare tree-wide grep.

**Report justification:** new-mutation

**Logical-whole closure:** not-closed

**Authority expiry:** my authority for MEC-V9ab expires with this terminal report. Nothing here closes the logical whole, and no `PASS` I report is acceptance, publication acceptance, or closure — those remain Orchestrator-owned. I will take no further autonomous action without a new complete authoritative prompt.

**Context pressure:** low. Roughly a fifth of the window consumed; the three allowlisted files plus the mandatory reading and the eight gate outputs fit comfortably, and no compaction occurred at any point.
