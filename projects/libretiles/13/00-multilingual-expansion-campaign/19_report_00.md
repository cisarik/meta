> ⚠ **ORCHESTRATOR ARCHIVAL NOTE, mine and not the Worker's.** Archived verbatim. Status `PASS`;
> `a944e76`, fourteen files, +117/−6, pushed, readback equal. **ACCEPTED.**
> ✔ **Verified by me:** twelve occurrences and one distinct form for each of the eight keys, `LOCALES`
> still four, and the tree green.
> ⭐ **ALL FOUR OF ITS MEASURED FINDINGS ARE CORRECT AND I VERIFIED EACH:** `messages.en.ts` said "these
> four strings" above a twelve-entry group · `GLOSSARY.md` said a missing key in "en/sk/cs/pl" is a type
> error when it is any of ELEVEN · CLDR already capitalizes `af de nl`, so my decision changed FIVE of
> eight rather than eight · and §5's identity loop **cannot detect a missing file**, because `sort -u`
> collapses occurrences — so it supplied the occurrence count itself.
> ⭐ **AND IT REFUSED THE TWO STALE-PROSE REPAIRS BECAUSE THEY WERE OUTSIDE ITS GRANT**, citing
> `AP.md:917-932`, while naming the asymmetry that made the refusal necessary: my §4.1 required fixing
> exactly that class of staleness in `i18n.test.ts` and was silent about the identical staleness four
> lines above the keys it was adding. **That asymmetry is my defect.** Both lines repaired
> orchestrator-direct as `779aa55`. Rulings in `00_notes.md` §52. The report as returned follows.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 19, Worker exchange ordinal: 01
```

**1. Status:** PASS

**2. Phase-qualified result:** Implementation complete — MEC-UIL-W1 delivered. Eight `settings.uiLanguage.*` endonym keys added to all twelve catalogs, three `AC-EXHAUST` counts and their comment prose updated, GLOSSARY inventory sentence + table updated and the capitalization decision recorded. `LOCALES` is still `["en","sk","cs","pl"]`; nothing added is reachable.

**3. Start and end commit:**
- start `c9078f2aa2b3a34c5ac51931b063f1330d49704b`
- end `a944e763311a7c5065a012ac7c512b422c94bb8a`

**4. Changed files and purpose** — fourteen, all inside the allowlist, `git show --stat` = `14 files changed, 117 insertions(+), 6 deletions(-)`:

| Path | Diff | Purpose |
|---|---|---|
| `messages.{en,sk,cs,pl,de,pt,is,it,nl,da,sv,af}.ts` | +8 / −0 each | the eight endonym keys, inserted immediately after `settings.uiLanguage.pl` |
| `i18n.test.ts` | +3 / −3 | `296→304`, `20` unchanged, `316→324`, plus the comment's "296 text keys" → "304 text keys" |
| `GLOSSARY.md` | +18 / −3 | opening paragraph names twelve endonyms; eight table rows; one sentence recording the capitalization decision |

Purely additive in the catalogs: **+8/−0 in all twelve**, so no existing key's value changed and none was removed or renamed. `AC-EXHAUST`'s four key-set equality assertions across en/sk/cs/pl are untouched. `locales.ts`, `translate.ts`, `index.ts`, `plural.ts` and every component are unmodified.

**5. Repository gate** — all seven checks matched before any mutation: `HEAD`=`c9078f2…`, `HEAD:.ap`=`9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`, `git -C .ap rev-parse HEAD`= same (detached), `## main...origin/main`, `--porcelain=v1` empty, `ls-remote` = baseline, no listener on 3000/8000.

**6. ⭐ The cross-catalog identity output — section 5's loop, verbatim:**

```text
  uiLanguage.af: "settings.uiLanguage.af": "Afrikaans",|
  uiLanguage.da: "settings.uiLanguage.da": "Dansk",|
  uiLanguage.de: "settings.uiLanguage.de": "Deutsch",|
  uiLanguage.is: "settings.uiLanguage.is": "Íslenska",|
  uiLanguage.it: "settings.uiLanguage.it": "Italiano",|
  uiLanguage.nl: "settings.uiLanguage.nl": "Nederlands",|
  uiLanguage.pt: "settings.uiLanguage.pt": "Português",|
  uiLanguage.sv: "settings.uiLanguage.sv": "Svenska",|
```

Exactly one distinct form per key. Because the loop as written pipes through `sort -u` (and strips indentation with `sed`), it proves *one distinct form* but cannot show the *twelve occurrences* it asks you to confirm — see MEASURED-6. Two companion measurements close that gap:

```text
  uiLanguage.af  occurrences=12 distinct_raw=1     uiLanguage.it  occurrences=12 distinct_raw=1
  uiLanguage.da  occurrences=12 distinct_raw=1     uiLanguage.nl  occurrences=12 distinct_raw=1
  uiLanguage.de  occurrences=12 distinct_raw=1     uiLanguage.pt  occurrences=12 distinct_raw=1
  uiLanguage.is  occurrences=12 distinct_raw=1     uiLanguage.sv  occurrences=12 distinct_raw=1
```

`distinct_raw` is over **unstripped** lines, so indentation is identical too. And the md5 of the inserted eight-line block is `2353c688ae87ca3fea9eca4f732e78f3` in all twelve files — one hash, twelve files, byte-identical block. Per-file presence is `8/8` in each of the twelve.

**7. Tests and validation** — four frontend gates, all post-dating the last edit:

- `npm run typecheck` → exit 0. **The code type-checks.** Eleven catalogs are declared `Record<TextKey, string>` (verified: only `enText` is unannotated, as the type source), so a missing key in any of them is a compile error — this is the completeness proof for all twelve files.
- `npx vitest run` → exit 0, **467 passed / 3 skipped** in 32 files passed / 1 skipped. Baseline measured **before** editing: identical, 467/3. No test case added.
- `npm run lint` → exit 0.
- `npm run build` → exit 0, "Compiled successfully", its own TypeScript pass finished. **The build passed** — separate claim from the typecheck above. Route table is **eleven dynamic routes, zero static** (`/`, `/_not-found`, `/api/ai/judge`, `/api/ai/move`, `/api/models`, `/api/prompts`, `/draw/[id]`, `/game/[id]`, `/play`, `/settings`, `/waiting/[id]`). Port 3000 was checked clear immediately before the build; nothing was killed.

Independent supporting measurements: the eight values reproduce exactly from `Intl.DisplayNames([code],{type:"language"}).of(code)` on this host (`node v26.4.0`, `ICU 78.3`, `unicode 17.0` — the prompt's stated toolchain), and all eight fold to pure ASCII through the project's real `foldForSearch` (`Afrikaans→afrikaans · Dansk→dansk · Deutsch→deutsch · Íslenska→islenska · Italiano→italiano · Nederlands→nederlands · Português→portugues · Svenska→svenska`), so `EXPLICIT_SEARCH_FOLDS` needed nothing. `Í` = U+00CD and `ê` = U+00EA confirmed at codepoint level.

**Gate deviation, recorded:** the backend five were not run. The diff is confined to `frontend/src/lib/i18n`, pytest collects only `backend/`, and mypy's scope is `config game gamecore accounts catalog`, so none of them observes this change.

**8. Commit and push result** — one commit, one push, both non-force:
- commit `a944e76` `feat(i18n) twelve interface-language endonyms`, fourteen paths staged individually (no `git add .`/`-A`), hooks not skipped
- pre-push gate: `HEAD~1` = `c9078f2aa2b3a34c5ac51931b063f1330d49704b` and `ls-remote origin refs/heads/main` still `c9078f2aa2b3a34c5ac51931b063f1330d49704b` at that moment
- push: `c9078f2..a944e76  main -> main` (fast-forward)
- readback: local `HEAD` = `a944e763311a7c5065a012ac7c512b422c94bb8a`, remote `refs/heads/main` = `a944e763311a7c5065a012ac7c512b422c94bb8a` — **equal**
- post-push `git status -sb` = `## main...origin/main`, working tree clean. `HEAD:.ap` still `9c5cc44…`; nothing under `.ap` touched.

**9. The GLOSSARY sentence added**, quoted:

> All twelve are capitalized although CLDR returns `dansk`, `íslenska`, `italiano`, `português` and `svenska` lowercase: a picker row is sentence-initial by position, and twelve rows that match scan faster than five lowercase plus seven capitalized. The choice is identical in every catalog and is never a per-catalog judgement.

The opening paragraph's parenthetical now reads `English`, `Slovenčina`, `Čeština`, `Polski`, `Afrikaans`, `Dansk`, `Deutsch`, `Íslenska`, `Italiano`, `Nederlands`, `Português`, `Svenska` — wording otherwise unchanged, only rewrapped.

**10. Resolved Execution Issues / Near-Misses:**

1. My first `git commit` invocation carried an invalid flag (`--no-verify=false`). Git rejected it with ``option `no-verify' takes no value`` and made **no** commit — HEAD unchanged, staging intact. Re-ran plain `git commit -F`, so hooks ran normally. Reporting it because the malformed flag names a forbidden behaviour: hooks were never bypassed, and no amend or recovery was needed.
2. An attempt to count keys by importing `messages.en.ts` under node type-stripping failed on the extensionless `./plural` import (`ERR_MODULE_NOT_FOUND`). Read-only, no mutation. Fell back to a structural count: 296 text + 20 fn pre-edit, cross-checked by the then-passing `toBe(296)`/`toBe(316)` assertions, giving the 304/324 arithmetic.

**11. Pre-Existing Failure Classification:** none. All four gates were green before and after. The `[libretiles-provider-failure] …` lines in vitest output are intentional fixture logging and appear identically in the pre-edit baseline run.

**Orchestration critique:**

MEASURED

1. `messages.en.ts:92` now contradicts its own group. Its comment reads "Do not translate these **four** strings back into exonyms" and the group holds twelve. I did **not** touch it: the Implementation boundary is "ADD eight keys per catalog", which does not cover comment edits, and `AP.md:917-932` — omitted permission is not implied permission. **Assumption stated, continued.** Narrow scope: the other eleven catalogs say "identical in every catalog" with no number, so only `en.ts` is numerically stale. Note the asymmetry — section 4.1 explicitly required fixing exactly this class of stale prose in `i18n.test.ts` but did not extend that to `en.ts`.
2. `GLOSSARY.md:4-5` says "a missing key in any of `en` / `sk` / `cs` / `pl` is a TypeScript error". Measured: eleven catalogs are `Record<TextKey, string>`, so a missing key in **any of the twelve** is a TypeScript error. Pre-existing staleness from the eight-catalog slices, outside the "one inventory sentence and one table" grant. Left alone.
3. Section 4's capitalization framing is broader than the change it makes. Measured on the stated toolchain, CLDR already returns `Afrikaans`, `Deutsch` and `Nederlands` capitalized, so the decision actually alters five of eight values, not eight. The prompt's own count ("five of the eight LOWERCASE") is correct; the surrounding framing ("the values above are CAPITALIZED" as a decision over all eight) overstates its reach.
4. Section 5's identity loop cannot detect a missing file. `sort -u` collapses occurrences, so a slice that added the block to eleven of twelve catalogs prints byte-identical output to a correct one; `sed 's/^ *//'` additionally hides an indentation error. This is the one check the prompt calls its real evidence. I supplied the occurrence count on unstripped lines plus the per-file block md5 above; suggest the loop carry `wc -l` in future prompts.
5. Everything else in the prompt that I could check was correct as written: section 3's cross-catalog measurement (12 catalogs, 1 distinct value for each of the four existing endonyms, verified **pre**-edit); the 296/20/316 baseline; the vitest baseline 467/3; eleven dynamic routes and zero static; the fold-safety table; the `Í` U+00CD and `ê` U+00EA warnings; the `.ap` gitlink; and section 4.2's pre-existing gap — the Settings table does list only ten `settings.gameVariant.*` rows and omits `czech` and `polish`, which all twelve catalogs define. Left untouched as instructed.
6. On correctness of the values themselves: all eight are the right endonyms for their languages, and I would not change any of them. The capitalization decision is right for the surface it is for — a scanning list — and its three reasons hold.

LEAD

1. The capitalized forms are correct for a standalone picker row and wrong for running prose in at least Icelandic and Portuguese, where language names are ordinary common nouns and not capitalized mid-sentence. If any later surface renders these values inline in a sentence rather than as a list item, that surface will read wrong to a native reader. **Unverified** — I did not inspect any planned rendering, and today no code path reads these keys at all. Not a reason to change this slice.
2. The two stale-prose items (MEASURED-1, MEASURED-2) plus the ten-row `gameVariant` gap could plausibly be folded into the wiring slice's diff at near-zero cost, since that slice edits this directory. **Unverified assumption** about the next slice's file set.

**Report justification:** `new-mutation`

**Logical-whole closure:** not-closed

**Authority expiry:** My authority ends with this report. I hold no further mandate on this repository — no wiring, no `LOCALES` change, no Meta write, no follow-up commit.

**Smallest next step:** the wiring half — extend `LOCALES` to twelve and make the interface-language picker render the now-existing key family — with the two stale-prose lines (`messages.en.ts:92` "four strings", `GLOSSARY.md:5` "any of en/sk/cs/pl") folded into that same diff if the ORCHESTRATOR grants them.

**Context pressure:** low — roughly a third of the window used, comfortable margin throughout.
