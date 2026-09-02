You are a WORKER instance assigned to the persistent AP WORKER role. Execute exactly this bounded task and stop.

```text
Logical whole identity: czech-polish-hungarian-variant-activation
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Evidence Probe
Task identity: CPH-DICT — acquire and expand the Czech, Polish and Hungarian lexicons
Phase: Preflight
Implementation authority: NONE for the repository
Independence required: no
Evidence posture: non-independent
Exact baseline: 8c00a331560f16b7d27eae04dc789a5124dd4497
Logical-whole closure: not-closed
```

Reasoning recommendation: **Medium.** This is a bounded, well-specified acquisition task with an existing reference implementation in the repository. Escalate to High only if a licence turns out not to permit redistribution, which is a material decision rather than a mechanical one.

## 1. What this task is

Produce **candidate** Czech, Polish and Hungarian playable lexicons, with complete licensing and provenance evidence, by reproducing the exact route this project already used for Slovak.

⛔ **This task is READ-ONLY with respect to the repository.** You create no file, edit no file, delete no file, stage nothing, commit nothing, push nothing inside `/home/agile/Projects/libretiles`. Every artifact you produce lands under `/tmp/opencode/cph-dicts/`. A later, separately authorized slice commits them. That separation is deliberate: another Worker may be mutating the repository while you run, and two Workers committing to `main` would collide.

## 2. The recipe already exists — read it first, do not invent one

`backend/scripts/build_slovak_lexicon.py` is the reference implementation. Read it in full before doing anything. It is not imported by Django and is a host tool.

What it does, and what you will reproduce for three more languages:

```text
1  pins one LibreOffice dictionaries commit: 75f5dff8c972fff4a32e4ea8434722c277f02a3f
2  downloads four files from
     https://raw.githubusercontent.com/LibreOffice/dictionaries/<commit>/sk_SK/
     sk_SK.dic, sk_SK.aff, LICENSE.txt, README_en.txt
3  verifies the SHA-256 of every downloaded file against a pinned value
4  requires the tri-licence sentence (GPL + LGPL + MPL) in README_en.txt
5  runs `unmunch <dic> <aff>` to expand the affix-compressed dictionary
6  filters each expanded line: NFC normalize -> strip -> casefold -> keep only
     `word.isalpha() and len(word) >= 2` -> deduplicate
7  bounds-checks the unique count into [80_000, 5_000_000]
8  writes a sorted lexicon with a two-line provenance header
9  writes <lang>.LICENSE = an attribution block plus the verbatim upstream LICENSE.txt
```

The shipped Slovak evidence you are matching in kind:

```text
backend/assets/dicts/slovak.txt       45 456 204 B, 3 005 252 lines, sorted, 2 header comment lines
backend/assets/dicts/slovak.LICENSE   67 811 B, SPDX "GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1"
```

`unmunch` is present at `/usr/bin/unmunch` and `hunspell` at `/usr/bin/hunspell`. Verified.

## 3. Repository gate — read-only

```text
Working directory: /home/agile/Projects/libretiles
git rev-parse HEAD                   == 8c00a331560f16b7d27eae04dc789a5124dd4497
git status --porcelain=v1            == exactly the ten untracked frontend/public flag images
```

Those ten flag images belong to another logical whole. Do not touch them. If porcelain shows anything else, report it and continue read-only — you are mutating nothing either way, so it is a finding, not a blocker.

The repository must still be at `8c00a33` with the same porcelain when you finish.

## 4. Mandatory reading

- `AGENTS.md`; `.ap/AP.md`; `.ap/AP_WORKER.md`; `.ap/INFOSEC.md` sections 3, 9, 10, 11, 12, 16
- `backend/scripts/build_slovak_lexicon.py` **in full** — the reference implementation
- `backend/assets/dicts/slovak.LICENSE` first 10 lines — the attribution shape you must match
- `backend/assets/variants/slovak.json` — the manifest shape a later slice will mirror
- `backend/gamecore/variant_store.py` `validate_dictionary_file` and `load_two_tile_words`

## 5. The three languages, and what you must discover rather than assume

Use the **same pinned commit** as Slovak — `75f5dff8c972fff4a32e4ea8434722c277f02a3f` — so all four languages share one provenance. If a language's directory does not exist at that commit, **report and stop for that language**; do not silently switch to a different commit or to `master`.

Directory names to **verify, not assume**. These are leads from the standard LibreOffice dictionaries layout:

```text
Czech      cs_CZ       expect cs_CZ.dic / cs_CZ.aff
Polish     pl_PL       expect pl_PL.dic / pl_PL.aff
Hungarian  hu_HU       expect hu_HU.dic / hu_HU.aff
```

For each language, establish by observation:

```text
- the exact directory name at that commit
- the exact .dic and .aff filenames — they may not follow the pattern above
- every licence and readme file actually present. Slovak had LICENSE.txt and README_en.txt;
  another language may have README.txt, COPYING, a differently named licence, or several.
  ⛔ Report what IS there. Do not assume the Slovak file set.
- the SHA-256 of every file you download
- the licence identity, quoted from the file rather than inferred
```

⛔ **Do not assume the tri-licence.** Slovak is `GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1`. Czech, Polish and Hungarian may differ. Quote the actual licence text and derive the SPDX expression from it. If a licence does **not** clearly permit redistribution and modification, that language is **BLOCKED** — report it as such and do not produce a lexicon for it. That is a material decision for the Cooperator, not a judgement for you.

## 6. Procedure, per language

```text
1  download into /tmp/opencode/cph-dicts/<lang>/upstream/ and record every URL, HTTP status,
   byte size and SHA-256
2  quote the licence identity and the relevant licence sentence
3  run: unmunch <dic> <aff>  > /tmp/opencode/cph-dicts/<lang>/raw.txt
   Record the exit code, the stdout byte size, and any stderr. Hunspell prints `parsing line:` for
   .aff comments; that is noise, not failure.
4  apply the SAME filter as the Slovak script: NFC -> strip -> casefold -> keep only
   `isalpha() and len >= 2` -> deduplicate -> sort
5  write /tmp/opencode/cph-dicts/<lang>/<lang>.txt with a two-line provenance header in the Slovak
   shape, then the sorted words, newline-terminated, UTF-8, LF only
6  write /tmp/opencode/cph-dicts/<lang>/<lang>.LICENSE = attribution block + verbatim upstream licence
7  record: unique word count, output byte size, line count, output SHA-256, the first and last ten
   words, and a sample of ten random mid-list words
```

Target filenames, matching the existing English and Slovak assets: `czech.txt`, `polish.txt`, `hungarian.txt`, and `czech.LICENSE`, `polish.LICENSE`, `hungarian.LICENSE`.

### The bound is a report-and-stop, not a knob

The Slovak script bounds unique words to `[80_000, 5_000_000]` and Slovak produced 3 005 252. **Polish hunspell is known to expand very large, and Hungarian uses aggressive compounding.** If any language falls outside that range:

⛔ **Report the exact count and STOP for that language. Do not raise the bound, do not truncate, do not sample, do not filter more aggressively to fit.** An out-of-range count is evidence the Orchestrator needs, not a problem for you to make disappear. State whether the excess looks like legitimate inflected forms or like compound explosion, and give ten example words that illustrate which.

Also report, per language, so the Orchestrator can judge quality without re-running anything:

```text
- how many unique words have length exactly 2, and list up to 50 of them.
  This matters: two-letter words are the highest-risk category in this product, and the Slovak
  hunspell expansion contained enough junk that a separate curated two-letter filter was needed.
- the longest word, and the count of words longer than 15 characters (unplayable on a 15x15 board)
- whether any word contains a character outside that language's expected alphabet
```

## 7. Two-letter authority files are explicitly OUT of scope

Do **not** attempt to source or synthesize Czech, Polish or Hungarian two-letter word lists.

The reason, so you do not treat it as an omission: `VariantDefinition.two_tile_words_file` is **optional**. English ships without one, and when it is absent the word authority routes two-tile words to the main dictionary. Czech, Polish and Hungarian will ship the same way. Your length-2 report above is exactly the evidence the Orchestrator needs to decide later whether a curated filter is worth adding.

## 8. Negative authority

```text
NO repository mutation of any kind. No file created, edited, renamed, deleted, or staged inside
   /home/agile/Projects/libretiles. No commit. No push. No git write of any kind.
NO variant manifest. czech.json / polish.json / hungarian.json are a later slice.
NO change to backend/scripts/build_slovak_lexicon.py. Read it; do not generalize it in the repo.
   If you write a script, it lives under /tmp/opencode/cph-dicts/ only.
NO re-running the Slovak build. slovak.txt and slovak.LICENSE must not be touched or regenerated.
NO database access. No manage.py of any kind. No migration.
NO scraping of a site other than the pinned raw.githubusercontent.com paths for that one commit.
NO synthesis, generation, translation, or model-authored word lists. Not one word may come from a
   language model. Every word must be traceable to the pinned upstream .dic/.aff through unmunch.
NO reading or printing of backend/.env or frontend/.env.local.
NO killing, restarting, or signalling any process. No pkill, ever.
NO dependency, lockfile, runtime, or toolchain change. No pip, no apt, no npm.
NO writes anywhere outside /tmp/opencode/cph-dicts/.
```

Network authority is exactly: `GET` on `https://raw.githubusercontent.com/LibreOffice/dictionaries/75f5dff8c972fff4a32e4ea8434722c277f02a3f/...` and, if needed to discover directory or file names at that commit, the GitHub API or tree view **for that same pinned commit only**. Nothing else. No POST, no authentication, no other host.

## 9. Execution route — mandatory bounded deviation under RF-16

```text
Declared route that could not be used:  poetry run <tool>, as documented in AGENTS.md
Exact alternate path, from backend/:    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python …
Rationale:  the Cursor AppImage environment intercepts python* through inherited APPIMAGE / ARGV0 /
            APPDIR / PYTHONHOME
Evidence class: reproduced-dynamic, established repeatedly in this project
Bounded authority: this task only
Stopping condition: if .venv/bin/python is absent or the deviation fails, STOP and report. Do not use
            ambient python, python3, or poetry run, and do not repair the environment.
```

`unmunch` and `hunspell` are ordinary host binaries at `/usr/bin/` and need no deviation.

## 10. Containment ledger — required in the report

```text
temporary root    /tmp/opencode/cph-dicts/
owner             you
mode              report the observed mode
contents class    public upstream dictionary sources, their licences, unmunch output, and candidate
                  lexicons. No secrets, no personal data, no repository content.
cleanup owner     the COOPERATOR, after the Orchestrator accepts this evidence and a later slice
                  commits the assets
cleanup outcome   retain-with-reason — these ARE the deliverable. ⛔ Do NOT delete them.
```

⛔ Do not touch `/tmp/opencode/mtt-f2a-checkpoint/` or `/tmp/opencode/mtt-f2b-checkpoint/`. Those are the Cooperator's database recovery checkpoints from another logical whole.

## 11. Stopping conditions

Stop and report: a language directory does not exist at the pinned commit; a licence does not clearly permit redistribution and modification; a SHA-256 you record cannot be reproduced on a second read; `unmunch` exits nonzero or produces empty output; a unique count falls outside `[80_000, 5_000_000]` **for that language**; a download returns anything other than HTTP 200; the work would require a repository write, a database access, a network target outside section 8, or a write outside the temporary root; the `.venv` route is unavailable.

A per-language stop is **partial, not fatal**. If Czech and Polish succeed and Hungarian is blocked, report `PARTIAL` with two complete languages and one exact blocker. That is a good and useful outcome — do not hold back two working languages waiting for a third.

## 12. Report contract

Begin **exactly** `### Report for ORCHESTRATOR_CHAT`. Echo the coordinates once: logical whole `czech-polish-hungarian-variant-activation`, Worker session `01`, Worker exchange `01`.

Then:

1. status `PASS` / `PARTIAL` / `BLOCKED`, and per language `ready` / `blocked` with the exact reason;
2. `Phase-qualified result: not-applicable` — this is a preflight evidence probe;
3. the repository gate quoted, plus confirmation that `HEAD` is still `8c00a33`, porcelain is unchanged, and **no repository file was created, edited, or staged**;
4. **per language**: the exact directory name, every filename downloaded with its URL, HTTP status, byte size and SHA-256; the licence identity quoted from the file; the derived SPDX expression; the `unmunch` exit code and stdout size; the unique word count; the output path, line count, byte size and SHA-256; first ten, last ten and ten mid-list words;
5. **per language**: the count of length-2 words with up to 50 examples; the longest word; the count of words longer than 15 characters; any character outside the expected alphabet;
6. a single comparison table of all four languages including shipped Slovak (`3 005 252` unique words), so the Orchestrator can see immediately whether Czech, Polish and Hungarian are the same order of magnitude;
7. any language whose count fell outside the bound, with your honest read on whether the excess is inflection or compound explosion;
8. the containment ledger of section 10, with `retain-with-reason`;
9. an explicit statement that **not one word came from a language model** and that every word is traceable to the pinned upstream sources through `unmunch`;
10. deviations, risks, and missing evidence, honestly — including anything about the licences that a lawyer rather than an engineer should read;
11. `Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>`;
12. `Pre-Existing Failure Classification: none`;
13. one smallest next step;
14. `Report justification: new-evidence`;
15. `Logical-whole closure: not-closed`;
16. an explicit authority-expiry statement.

⛔ Do not emit any logical-whole closure signal, and do not describe this evidence as authorizing the commit of any asset.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_dictionary-acquisition_00.md
Destination path: /home/agile/meta/projects/libretiles/11/02-czech-polish-hungarian-variant-activation/
Archival: wait-for-report
```

You do not archive this pair. The Cooperator does, after your report exists.

Your authority expires at your terminal report.
