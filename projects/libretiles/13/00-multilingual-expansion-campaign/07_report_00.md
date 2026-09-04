> ⚠ **ORCHESTRATOR ARCHIVAL NOTE, and it is mine, not the Worker's.** This report is archived
> verbatim as it was returned. It is `BLOCKED`, and the block was **correct**: prompt `07/01`
> declared an outcome of 316 keys while forbidding any change to `i18n.test.ts` outside AC-LEX-4,
> and `i18n.test.ts:159` hardcodes that total. The prompt was unsatisfiable and the defect was mine.
> The correction — `300` → `316`, split into its two components with a comment — was made
> orchestrator-direct, all four frontend gates were re-run by me, and the eleven-path diff landed as
> `cfd1215`, pushed, public readback equal. Reconciliation and my own re-measurement of this report's
> claims are in `./00_notes.md` §38. Nothing below this line was edited.

### Report for ORCHESTRATOR_CHAT

Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 07, Worker exchange ordinal: 01

**Status: BLOCKED.** All sixteen keys, eight helpers, the new test, the switch arms, the picker map, the re-export and the glossary rows are implemented and validated. **I did not commit and did not push**, because the prompt is internally unsatisfiable and AP requires me to escalate rather than resolve it. Detail in the first MEASURED finding; the fix is one integer.

Phase-qualified result: Implementation complete in the working copy, unpublished. Start commit `32312ba6c95017efb44934616e28c5241e548cbc`; end commit **the same** — HEAD, `origin/main` and `HEAD:.ap` are all byte-identical to the baseline.

## The blocker, precisely

```text
i18n.test.ts:159   expect(textKeys.length + fnKeys.length).toBe(300);
                   → AssertionError: expected 316 to be 300
```

Section 2 states my outcome as "296 text keys plus 20 function keys". Measured: 296 + 20 = **316**. `i18n.test.ts:159` is the only place in the codebase that number is written down, and section 7.3 declares everything in `i18n.test.ts` beyond AC-LEX-4's `IDS` READ-ONLY. The stage gate requires green vitest before the commit. So the prompt's stated outcome and the prompt's own prohibition cannot both hold.

Section 7.3's stated *reason* for the read-only rule does not cover `:159`: it names `ownName` `:983`, `HEADER_EXPECTED` `:1118` and `OVERLAY_EXPECTED` `:1187` as locale-keyed maps that grow when `LOCALES` grows. `:159` is text-key-keyed and grows with **this** slice, not the wiring slice — so changing it merges nothing. But that is my reading of your rationale, not your authority, and `AP.md:917-932` is explicit that omitted permission is not implied permission; here it is denied outright, not omitted. `AP.md:2466-2486` requires a stop when "completion would require out-of-scope changes", and your line 66 requires the conflict to come back to you rather than be resolved by me.

Authorize `300` → `316` at `i18n.test.ts:159` and everything else is already green.

## Changed files and purpose (10 modified + 1 new, all inside the eleven-path allowlist; nothing staged)

| Path | Purpose |
|---|---|
| `plural.ts` | +78/−0. Eight CLDR helpers, five separate bodies for af/nl/de/da/sv, `one → other → many` parameter order, CLDR rule per function. Existing three helpers and the `pluralCs` alias byte-identical. |
| `plural.test.ts` | NEW. Explicit slot→category map per language, twelve helpers × 3005 counts, runtime `supportedLocalesOf` skip guard, failure message carries `process.version` + `process.versions.icu`. |
| `index.ts` | The one export statement now carries twelve alphabetical names. Nothing else touched. |
| `messages.en.ts` | +40/−0. Eight variant names, eight lexicon strings before `unknown`, eight switch arms before `default`. |
| `messages.sk.ts` / `.cs.ts` / `.pl.ts` | +18/+19/+19, **−0 each** — no existing value changed. Sixteen keys each, located by key not line. |
| `GameLanguagePanel.tsx` | +8/−0. `VARIANT_NAME_KEYS` four → twelve. `VARIANT_FLAG_SRC` untouched. |
| `i18n.test.ts` | AC-LEX-4 `IDS` four → twelve, Czech special case generalized to "every id but `collins2019` must not contain Collins". Test title left byte-identical. |
| `GLOSSARY.md` | +70/−4. Twelve-id parenthesis, the derivation and the `unknown` reachability note, eight `game.lexicon.*` rows, eight Settings rows, D7 extended to twelve helpers plus the three translator facts. |

Zero deleted lines in all six code files. Deletions exist only in `GLOSSARY.md` (4, prose growth), `i18n.test.ts` (4, the one authorized block) and `index.ts` (1, the one export statement). `locales.ts`, `translate.ts`, `frontend/public/`, `package.json`, `.ap` and every backend path untouched. No new catalog. `GameLanguagePanel.test.ts` needed no edit.

## Tests and validation

```text
typecheck  clean — and this is the key-set completeness proof: Record<TextKey, string>
           made every missing key in sk/cs/pl a compile error until all sixteen landed.
vitest     baseline at 32312ba: 454 passed / 3 skipped (457)  ← reproduces your inherited
           number from 529e691 exactly, no disagreement to report.
           after:              466 passed / 1 failed / 3 skipped (470)
           +13 new tests, all green. The single failure is i18n.test.ts:159 above.
           plural.test.ts alone: 13/13. prompts.test.ts green (MOVE CORE hash unchanged).
           AC-LEX-UNK green. GameLanguagePanel.test.ts green, unedited.
lint       clean (npm run lint project-wide, and eslint on the four changed TS/TSX files).
build      SUCCEEDS — a separate claim from typecheck. ELEVEN dynamic routes, ZERO static,
           matching the inherited count. Port 3000 and 8000 checked empty first; no pkill.
```

Negative controls, both as required:

```text
BROKEN    pluralIs modulus 10 → 100. Exactly one test failed and it named the language:
          "pluralIs (Icelandic, locale "is") disagrees with CLDR at 240 of 3005 sampled
          counts on node v26.4.0 / ICU 78.3. Either the helper is wrong or CLDR changed."
          First mismatches n=21,31,41,51,61,71,81,91. The other eleven stayed green.
RESTORED  13/13 again, and `git diff --numstat` on plural.ts reads 78/0 — purely additive,
          so the restoration is proved by the absence of any deleted line.
```

Section 6.1 re-derived on my runtime (`node v26.4.0 / ICU 78.3`) before writing anything: **your table reproduced exactly**, every row. af/nl/de/da/sv zero divergences from `en` over 0..3000; `is` 270 `one` values matching `i%10===1 && i%100!==11` at every one of them, 269 divergences; `it` `many` only at exact millions with `1000001` → other and `0` → other; `pt` `one` including 0 as its single divergence; `pl` 0 → `many`; sk/cs no `many` over the integers; `da` 0.5 → `one` while `en` 0.5 → `other`, which is what justifies five bodies instead of five aliases. All twelve locales in `supportedLocalesOf`.

## The twenty-four Slavic strings, for the Cooperator read that is the only real check

```text
        sk (noun / v+locative)        cs (noun / v|ve+loc)          pl (adj / w|we+loc)
af      Afrikánčina  v afrikánskom    Afrikánština  v afrikánském   Afrykanerski  w afrykanerskim
it      Taliančina   v talianskom     Italština     v italském      Włoski        WE włoskim
nl      Holandčina   v holandskom     Nizozemština  v nizozemském   Niderlandzki  w niderlandzkim
de      Nemčina      v nemeckom       Němčina       v německém      Niemiecki     w niemieckim
pt      Portugalčina v portugalskom   Portugalština v portugalském  Portugalski   w portugalskim
da      Dánčina      v dánskom        Dánština      v dánském       Duński        w duńskim
sv      Švédčina     v švédskom       Švédština     VE švédském     Szwedzki      w szwedzkim
is      Islandčina   v islandskom     Islandština   v islandském    Islandzki     w islandzkim
```

Trap 1 — Czech `ve`: **exactly one, `ve švédském`. Your LEAD was right.** Basis: the same initial š/s + consonant cluster that produces the shipped `ve slovenském` at `messages.cs.ts:237`, and `ve Švédsku` / `ve švédském` is the standard vocalized form. The other seven begin a, i, n, n, p, d, i and take plain `v`.

Trap 2 — Slovak `vo`: **zero of the eight**, stated as a measurement rather than left silent. Slovak vocalizes only before v- and f-; the eight locative adjectives begin a, t, h, n, p, d, š, i. The three shipped rows are also plain `v`, consistent.

Trap 3 — adjective not noun: held throughout. Note the two deliberate sk/cs divergences that a "they agree on some cells" reading would have flattened: Slovak uses the **Talian-** stem (`taliančina` / `talianskom`) where Czech uses **Ital-** (`italština` / `italském`), and Slovak `holandčina` / `holandskom` against Czech `nizozemština` / `nizozemském`.

## Orchestration critique

**MEASURED**

1. **The prompt is internally unsatisfiable** — section 2's 296+20 outcome versus section 7.3's blanket read-only versus the green-vitest stage gate. Full detail above. This is the only reason this report is BLOCKED, and the fix is one integer. Your enumeration reached the sixteen keys and the plural table but not the one assertion that counts them.
2. **Section 5.3 omits the Polish `w`/`we` alternation.** You named Czech `v/ve` and Slovak `v/vo` and not Polish. Polish vocalizes `w` → `we` before an initial w-/f- consonant cluster, and one of the eight triggers it: `Nie ma we włoskim leksykonie`. Measured in-repo: unlike Czech, **no shipped Polish row triggers it** (`w słowackim` / `w czeskim` / `w polskim`), so the file offered no precedent to copy — which makes this omission more consequential than the Czech trap you did flag, not less. Following only the named traps ships `w włoskim`.
3. **Section 7.2's measurement was correct.** `GameLanguagePanel.test.ts` needed no edit and stayed green. It sat on the allowlist unused.
4. **Section 6.1's table and section 8's frontend-only premise both reproduced.** Both backend greps return 0 lines. I agree with the backend-gate deviation and did not run the backend five: `git status` proves the diff is confined to `frontend/`.
5. **The eight lexicon ids and the byte-identity claim both confirmed independently.** Every `dictionary_file` stem under `backend/assets/variants/` gives your twelve ids with `english → collins2019`; `views.py:162` sets `display_name` from the manifest `language` field, which is byte-identical to my eight English values. The English UI cannot change.
6. **No pre-existing plural defect.** All four already-exported helpers pass the new CLDR pin.
7. **`GLOSSARY.md`'s Settings table was already incomplete** — it listed only `settings.gameVariant.english` and `.slovak`; `czech` and `polish` were never documented. I added exactly the eight I was told to and left the two pre-existing gaps.

**LEAD**

1. **A seventeenth key family exists and I did not add it, as instructed.** `settings.uiLanguage.*` has four entries, and the wiring slice that grows `LOCALES` to twelve needs eight new endonym keys plus eight `ownName` rows. So freezing at sixteen does **not** save the eight catalogs from being reopened — the wiring slice will reopen all twelve files anyway, which partially undercuts section 2's justification. Counter-argument, which is why this is a LEAD and why I would not add it even if authorized: those keys are endonyms identical in every catalog, so it is one mechanical 8×12 pass, whereas each of my sixteen carries four distinct language values.
2. **The slice boundary is otherwise right, for a reason stronger than the one you gave.** The `plural.ts` dependency is *hard* — `messages.da.ts` cannot typecheck without `pluralDa` — while the `settings.uiLanguage.*` dependency is soft. Sequencing on the hard dependency is correct even given LEAD 1.
3. **`prompts.ts:198` and `:208` special-case only `lexicon_id === "slovak"`**, so ten of the twelve playable lexicons get the English CORE prompt. Same four-vs-twelve shape as the UI gap this slice closes, in a file firmly outside the allowlist. I read the two call sites and did not trace the full assembly.
4. **Section 3 item 4 forbids the only local corpus that could have checked my declensions.** No word list, no lexicon, no dictionary file, and no network — so twenty-four Slavic strings rest on my knowledge plus three shipped rows. That is the right rule for word lists, but it means section 5.3's mitigation really is only "you know the risk is there". Schedule the Cooperator read of the table above **before** the eight catalogs, not after: the same declension patterns get copied into them.
5. **`plural.test.ts` is silent outside its window** — 0..3000 plus four millions. A CLDR change between 3001 and 999999, or on fractions the helpers truncate away, would not turn it red. Strong where the product counts, silent elsewhere.

## Enumeration widened

1. **A second render site of the eight names that the prompt did not name:** `src/app/play/page.tsx:69` calls the same `variantDisplayName`, feeding `play.humanQueue.queueFor`. It picks the eight up for free from the one map edit, so the human-queue label also becomes translated in sk/cs/pl — real product value beyond what section 2 claims. `GLOSSARY.md:215-218` documents that call site; section 7.2 mentions only the picker.
2. **A second `lexicon_id` consumer with the same four-vs-twelve gap:** `prompts.ts:198,208`, reached via `/api/ai/move` and `/api/ai/judge` (`judge/route.ts:237,244`). Untouched.
3. **The other `Record<string, TextKey>` in the tree** is `GAME_END_REASON_KEYS` at `GameHistoryPanel.tsx:77`; it keys on backend `game_end_reason`, not variant or locale, so it needs nothing. The four-entry surfaces the wiring slice must grow are the three you fenced off plus `settings/page.tsx:356`'s `localeLabelKey` and `translate.ts:7,13`.
4. **What my commands could not reach:** `AC-EXHAUST`'s hardcoded `300` — outside your enumeration and the thing that blocked me; the correctness of the twenty-four Slavic strings, for the reason in LEAD 4, since no command in my authority can check a declension; any hardcoded variant-name or lexicon-id list outside `frontend/src` and `backend/` (I did not search `docs/` or `scripts/`); and the `two_tile_words_path` lexicons, which `views.py` also health-checks — my twelve arms stay right because `_lexicon_id` returns the main stem regardless, but I did not enumerate those files.

## Resolved Execution Issues / Near-Misses

Three near-misses, all linguistic, all caught before they reached a file:

1. **Polish `we włoskim`.** Not in your trap list and with no in-repo precedent. `w włoskim` would have passed every gate.
2. **Slovak `taliančina` / `talianskom`, not the Czech `Ital-` stem.** Section 5.1's true note that sk and cs legitimately agree on some cells invites copying; Slovak uses `Talian-` for Italian while Czech uses `Ital-`.
3. **Slovak `holandčina` against Czech `nizozemština`** — the same divergence shape as `Slovenčina` / `Slovenština`, kept rather than harmonized.

One procedural near-miss avoided by following section 5's warning: every block was located by key. Confirmed after the fact — `pl`'s two blocks sit at `:103` / `:239` against sk/cs at `:101` / `:236`, so a line-addressed edit would have landed wrong in exactly one file.

## Pre-Existing Failure Classification

**none.** Baseline `npx vitest run` at `32312ba` reproduced your inherited 454 passed / 3 skipped exactly. The single red test is caused by my own diff.

## Deviations, risks, missing evidence

- **No commit, no push** — the only deviation from the authorized stage list, and it is the AP-mandated stop, not a shortfall in the work.
- **The canonical checkout at `/home/agile/Projects/libretiles` is left dirty**: 9 modified + 1 untracked, nothing staged, HEAD and `origin/main` still `32312ba`, `.ap` still `9c5cc44` detached and untouched. I did not restore or clean it — `AP_WORKER.md:192-199` forbids inferring authority for destructive recovery and your section 49 forbids deletion. **The next repository gate on this checkout will fail `git status --porcelain=v1` until you decide.** Preserving the work costs one line of authority; reverting costs the whole exchange.
- Missing evidence: none besides the commit, push and readback that the stop prevents.
- Untrusted content: `frontend/AGENTS.md` carries a Next.js reading rule. Its trigger is ABSENT — plain TypeScript modules, one Markdown file, and one `const` map in an existing client component; no route, no server-component boundary, no config, no data-fetching primitive. I agree with your reading and proceeded. No repository file attempted to instruct me. No secret was read or printed; `next build` loaded `.env.local` itself and no credential value, prefix, length or hash entered this report.
- Context pressure: low — roughly a third used, comfortable throughout.

**Report justification: new-material-risk**
**Logical-whole closure: not-closed**

**Smallest next step:** authorize `i18n.test.ts:159` `300` → `316` — one integer, the exact number section 2 already specifies — then the same eleven-path diff commits and pushes with all four gates green.

**Authority expiry:** my authority ended when I stopped before the commit and it ends completely with this report. I hold no authority to commit, to push, to touch `i18n.test.ts:159`, to restore or clean the working copy, to begin any catalog, to add a locale, or to archive this prompt or report into Meta.
