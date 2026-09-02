You are a WORKER instance assigned to the persistent AP WORKER role. Execute exactly this bounded task and stop.

```text
Logical whole identity: czech-polish-hungarian-variant-activation
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: CPH-A1 — activate Czech and Polish as playable variants
Phase: Implementation
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Exact baseline: 8c00a331560f16b7d27eae04dc789a5124dd4497
Logical-whole closure: not-closed
```

Reasoning recommendation: **High.** Named risk: this slice adds two new **playable game variants** to a shipped product. A wrong tile distribution or a wrong alphabet order is not caught by a type checker and would be visible to a player as a broken game.

```text
Evidence tier: E2
Evidence tier basis: cross-cutting across assets, a new read-only endpoint, and the frontend, but fully
  reversible. No migration, no schema change, no database write, no destructive operation, no
  credential, no provider call.
Combined implementation envelope: allowed — assets, code, tests, one commit, one non-force push
Activated stricter profile: INFOSEC.md at R1 + R2, inline, non-independent. The new endpoint is a
  public-facing read surface, so section 6c's redaction rules are mandatory.
Independent acceptance: not-required for this slice
Validation ladder: selected. Inspection; the affected backend and frontend suites; new causal
  regressions per section 8; the full backend suite because a new variant loads through shared code.
```

## 1. The outcome, in one sentence

When you are done, the Cooperator opens Settings, sees **English, Slovak, Czech and Polish** in the game-variant control, picks Czech, starts a game, and plays Czech words that the engine validates against a real Czech lexicon.

That is three of the four Visegrád languages playable. Hungarian is deliberately **not** in this slice — its lexicon is a stem list and is blocked on a separate acquisition task.

## 2. Why this is reachable now — two measured facts

```text
1  backend/game/serializers.py:178-183 and :213-218 validate variant_slug against
   list_installed_variants(), which globs backend/assets/variants/*.json. Dropping a manifest into
   that directory makes the BACKEND accept the slug with ZERO code change.
2  Czech (40 tile entries) and Polish (33) have NO multi-character tokens. They are single-code-point
   languages exactly like Slovak, so the F2b temporary wire adapter carries them losslessly, the
   `Zod .length(1)` guard in the AI move route passes them, and the serializers.py one-code-point
   placement filter does not block them.
```

Consequence: Czech and Polish need **neither** the wire-v4 slice **nor** the AI-boundary slice. Those remain required for Hungarian alone.

The only thing in the way is the frontend, which hardcodes the variant union at `frontend/src/hooks/useGameStore.ts:25`.

## 3. Repository gate

```text
Repository checkout topology: standalone checkout
Working directory: /home/agile/Projects/libretiles
Expected branch: main
Expected HEAD: 8c00a331560f16b7d27eae04dc789a5124dd4497
Expected .ap gitlink and submodule HEAD: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

Verify and quote `git rev-parse HEAD`, `git rev-parse HEAD:.ap`, `git -C .ap rev-parse HEAD`, `git status -sb`, `git ls-remote origin refs/heads/main`, `git status --porcelain=v1`.

Porcelain must be **exactly** the ten untracked Cooperator flag images and nothing else. Do not touch them. Anything else: classify with all five AP recovery classes; stop if the primary class is `unexplained-divergence`.

Also confirm, read-only: `ss -tlnp | grep -E ':(3000|8000)'` shows nothing. ⛔ Kill nothing, ever, and never `pkill` under any pattern — those patterns match the Cooperator's own servers.

## 4. Mandatory reading

- `AGENTS.md`, `frontend/AGENTS.md`; `.ap/AP.md`; `.ap/AP_WORKER.md`; `.ap/PROMPT_CONTRACTS.md`; `.ap/INFOSEC.md` sections 3, 5, 6, 11, 12, 16
- `backend/assets/variants/slovak.json` and `english.json` — the exact manifest shape you must mirror
- `backend/gamecore/variant_store.py` in full — `_load_variant_from_path`, `_parse_asset_token`, `_parse_alphabet_order`, the subset invariant, `validate_dictionary_file`, `list_installed_variants`
- `backend/game/views.py`, `backend/game/urls.py`, `backend/game/serializers.py` lines 170-220
- `frontend/src/hooks/useGameStore.ts`, `frontend/src/lib/api.ts`, `frontend/src/lib/types.ts`, `frontend/src/app/settings/page.tsx` `GameLanguagePanel`
- `frontend/src/lib/i18n/messages.en.ts` and `messages.sk.ts` — the `Record<TextKey, string>` contract

## 5. The prepared lexicons — copy, do not regenerate

Worker session 01 exchange 01 produced these read-only and the Orchestrator verified every hash, line count, sort order and inflection sample independently. **Copy them byte-for-byte. Do not re-run `unmunch`. Do not regenerate, re-filter, re-sort, or edit one byte.**

```text
/tmp/opencode/cph-dicts/czech/czech.txt        54 105 021 B  3 930 499 lines
  SHA-256  919d6bac41b0938bc1955685b826857aa21543d4dd45a4035c1fa08aa4cc5bdc
/tmp/opencode/cph-dicts/czech/czech.LICENSE       72 790 B
  SHA-256  bde41b518094f12ea79bdfc1396a6b9562bc1d994da1fd37a07a06fd71f185a8
/tmp/opencode/cph-dicts/polish/polish.txt     51 607 141 B  3 721 706 lines
  SHA-256  605d5a43d5d5dcd1b386ab9f9f62b72eb964882f6a9ccbe244a826e0baa06aab
/tmp/opencode/cph-dicts/polish/polish.LICENSE     30 427 B
  SHA-256  869efadec82ae6aba8270ca5a3eaa6fce4bfd2336824548f03acae037b5aa9c3
```

Destination: `backend/assets/dicts/`. Verify the SHA-256 of every file **after** copying and report both. If any hash differs from the value above, **stop and report** — do not proceed with a lexicon you cannot prove is the verified one.

⛔ **Do NOT copy `hungarian.txt` or `hungarian.LICENSE`.** They are a stem list, not a playable lexicon: `ház` is present but `házat`, `házban`, `házakat`, `kutyát`, `kutyák` and `asztalon` are all absent. Shipping it would tell a Hungarian player that ordinary words are invalid. Hungarian is blocked on a separate acquisition task.

⛔ Do not touch `/tmp/opencode/mtt-f2a-checkpoint/` or `/tmp/opencode/mtt-f2b-checkpoint/`. Those are the Cooperator's database recovery checkpoints.

## 6. The four changes

### 6a. Two manifests: `backend/assets/variants/czech.json` and `polish.json`

Mirror `slovak.json`'s key set exactly. `two_tile_words_file` is **omitted** for both — it is optional, English ships without one, and the word authority then routes two-tile words to the main dictionary. That is deliberate and is not an omission to fix.

**`alphabet_order`, verbatim.** These are Cooperator-sourced from Ústav pro jazyk český AV ČR and Rada Języka Polskiego PAN, and Orchestrator-validated for duplicates, NFC, and the subset invariant. Do not reorder, extend, or "correct" them.

```text
czech   (42 tokens)
A Á B C Č D Ď E É Ě F G H CH I Í J K L M N Ň O Ó P Q R Ř S Š T Ť U Ú Ů V W X Y Ý Z Ž

polish  (32 tokens)
A Ą B C Ć D E Ę F G H I J K L Ł M N Ń O Ó P R S Ś T U W Y Z Ź Ż
```

⚠️ **Polish deliberately excludes `Q`, `V` and `X`.** They appear in loanwords but are not part of the 32-letter Polish alphabet and the standard Polish Scrabble set has no such tiles. **Do not add them.**

⚠️ **Czech `alphabet_order` is NOT a dictionary collation.** Normed Czech sorting per ČSN 97 6030 treats `Á Ď É Ě Í Ň Ó Ť Ú Ů Ý` as their base letter at the primary level. The array above is a deterministic total order for the **engine** — tile order, starting draw, blank picker. Czech is the only one of the five where that confusion is possible, so say so in a comment if the JSON permits one, and in your report regardless.

**The tile distribution (`letters`) you must source.** The Cooperator supplied these JSONs in an earlier session and a previous Orchestrator arithmetically validated them, but their exact text is not in this Orchestrator's context. Source the standard Czech and Polish Scrabble distributions from the **same source `slovak.json` already cites** — its `source_url` is `https://en.wikipedia.org/wiki/Scrabble_letter_distributions`. Record the exact retrieval date and the section you used.

⛔ **Do not trust that page. Verify arithmetic yourself against these invariants**, which come from the Cooperator's own supplied data and are your acceptance test. If your sourced distribution does not reproduce them exactly, **stop and report the difference** — do not adjust the data to fit and do not adjust the invariant to fit the data.

```text
                 total tiles   letter entries   of which blank   nominal points   multi-char tokens
czech                100            40             exactly 2          205               NONE
polish               100            33             exactly 2          190               NONE
```

Two further invariants that must hold, and which cross-check the alphabet arrays independently:

```text
czech    39 non-blank tile kinds, and exactly THREE alphabet letters have no tile: CH, Q, W
polish   32 non-blank tile kinds, and EVERY alphabet letter has a tile (zero without)
```

`nominal points` is the sum over entries of `count * points`. The blank scores 0.

Sanity check you can run before writing anything: `40 entries − 1 blank entry = 39`, and `42 alphabet tokens − 3 tileless letters = 39`. Same for Polish: `33 − 1 = 32 = 32 − 0`. If those do not reconcile, the data is wrong.

The F1 loader enforces the subset invariant, canonical NFC uppercase tokens, duplicate-freedom, and a required `alphabet_order`. It will refuse a malformed manifest with a stable `VariantManifestError.code`. Use that as a first check: load both variants through `load_variant()` and quote the result.

### 6b. `GET /api/game/variants/` — a new read-only endpoint

The frontend cannot discover installed variants today. Add the minimal endpoint the plan designs, in `backend/game/views.py` with its route in `backend/game/urls.py`.

Response: a JSON array, one object per installed variant, with **exactly these four fields and no others**:

```text
{ "slug": "czech", "display_name": "Czech", "language_code": "cs", "readiness": "playable" }
```

```text
readiness    "playable"    the manifest parses AND its dictionary file exists and is readable
                           (and its two-tile file too, when the manifest declares one)
             "unavailable" the manifest parses but a referenced resource is absent
order        default `english` first, then a stable order by display name then slug
malformed    a manifest that fails to parse is OMITTED from the response and logged. It must not
             crash the endpoint and must not appear as "unavailable".
```

⛔ **INFOSEC 6c, mandatory redaction. The response must NEVER contain** a file path, a filename, dictionary contents, a word count, filesystem metadata, a readiness *reason*, an exception message, or anything derived from the host filesystem layout. Four fields, four values, nothing else. Write a test that asserts the exact key set so a future addition cannot leak by accident.

Permissions: DRF's project default is `IsAuthenticated` and it is fail-closed. **Do not override it.** Every page that needs this list is behind login. Add a test proving an unauthenticated request is rejected, and a test proving exactly which fields an authenticated request receives.

### 6c. Frontend: replace the hardcoded union with the discovered list

```text
frontend/src/hooks/useGameStore.ts:25   SelectedVariantSlug = "english" | "slovak"  ->  string
                                :285    the persist migration check that rejects any other value
frontend/src/lib/types.ts               a VariantSummary type matching the four response fields
frontend/src/lib/api.ts                 an authenticated getVariants() using the existing bearer
                                        pattern and the existing error mapping — do NOT invent a new
                                        fetch path and do NOT copy the older parseBackendJson shape
                                        that ignores HTTP status
frontend/src/app/settings/page.tsx      GameLanguagePanel renders the fetched list instead of two
                                        hardcoded buttons; an `unavailable` variant renders disabled
```

The persist version is currently 3 and F2b did not change it. Bump it to **4** with a `migrate` that keeps any non-empty syntactically valid slug, and resets a malformed value to `"english"`. It must **not** decide availability locally — after a successful fetch, a slug that is absent or `unavailable` reconciles to the first `playable` row and is persisted. If the fetch fails or no playable row exists, game creation is blocked rather than silently redirected to another language.

**Variant names must be localized, not left in English.** `settings.gameVariant.english` / `.slovak` keys already exist. Add keys for Czech and Polish in **both** `messages.en.ts` and `messages.sk.ts` — the `Record<TextKey, string>` contract makes a key present in only one catalog a `tsc` error, which is exactly the gate working. For a slug with no key, fall back to the server `display_name` and document that fallback in a comment.

### 6d. Do not localize anything else

⛔ The remaining ~330 English strings, the two "fancy" flag dropdowns with diacritic-insensitive autocomplete, and the cs/pl/hu UI translations belong to logical whole `10/00 ui-internationalization` and get their own Orchestrator. Add **only** the variant-name keys above. Do not touch the ten untracked flag images.

## 7. Negative authority

```text
NO Hungarian anything: no hungarian.txt, no hungarian.LICENSE, no hungarian.json. Blocked on lexicon.
NO regeneration of any lexicon. No unmunch. No download of dictionary sources. Copy the verified files.
NO change to backend/assets/dicts/slovak.txt, slovak.LICENSE, slovak_two_tile_words.txt,
   collins2019.txt, sowpods.txt, or to english.json / slovak.json.
NO migration, no makemigrations, no manage.py migrate, no schema change, no database row written or
   deleted. This slice has no database effect at all.
NO change to backend/gamecore/. F1 finished it; compute readiness in the view from
   variant.dictionary_path.is_file().
NO change to the wire format, no state_schema_version, and no deletion of the F2b temporary adapter.
NO change to backend/game/services.py, consumers.py, models.py, admin.py, diagnostics.py.
NO change to _word_passes_dictionary or to the serializers.py one-code-point placement filter.
NO change to backend/config/, accounts/, catalog/, billing/.
NO new dependency, lockfile, runtime, or toolchain change. No pip, no npm install, no apt.
NO write to backend/.env, and no read of it.
NO killing, restarting, or signalling any process. No pkill, ever.
NO network except the authorized git ls-remote, one git push, and the one documented retrieval of the
   tile distributions for the two manifests.
NO documentation change: not README.md, not AGENTS.md.
```

Four standing Cooperator locks, none of which this slice touches: the nine AI providers are frozen; MOVE CORE hash `c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60` and version `pfr-s2-core-1` are pinned; `DEFAULT_MAX_ELAPSED_MS = 2000` and `DEFAULT_RANKED_MAX_ELAPSED_MS = 750` are fixed; exactly six `completion_source` values.

⛔ **The formed-word invariant.** A move is illegal only when a **complete** formed word has physical length two and is outside the variant's two-tile lexicon — never because a longer formed word *contains* a two-letter string. Czech and Polish declare no two-tile file, so their two-letter words route to the main dictionary, exactly as English does. If any line you write implies `"am" not in word`, you have failed.

## 8. Required new tests

Every one needs a **pre-fix / post-fix** entry. For a new capability, "pre-fix" is the exact failure or absence you observed before the change.

```text
T1  both manifests load through load_variant() with no VariantManifestError
T2  arithmetic: czech 100 tiles / 40 entries / 2 blanks / 205 nominal points;
    polish 100 / 33 / 2 / 190. Assert the exact numbers, not ranges.
T3  the subset invariant, in both directions: every non-blank tile token appears exactly once in
    alphabet_order; and the tileless letters are exactly {CH, Q, W} for Czech and empty for Polish
T4  playable_letters comes back in alphabet_order, not code-point order. Assert a diacritic case
    for each language — Czech `Á` immediately after `A`, Polish `Ą` immediately after `A`.
T5  no multi-code-point token exists in either variant, so the F2b wire adapter cannot raise for them
T6  a real word from each new lexicon validates and a nonsense string does not, through the same
    dictionary path the game uses. Use inflected forms: Czech `domu` and `knihy`, Polish `domach`
    and `książki`. These are the forms that prove the lexicon is expanded rather than a stem list.
T7  the endpoint returns exactly the four documented keys, and NOTHING else. Assert the exact key set.
T8  the endpoint rejects an unauthenticated request
T9  a variant whose dictionary file is absent reports readiness "unavailable" and does not crash the
    endpoint. Use a synthetic manifest in a temporary location; do not remove a shipped asset.
T10 a malformed manifest is omitted from the response entirely and does not appear as "unavailable"
T11 game creation with variant_slug "czech" succeeds; with an unknown slug it is rejected as
    unknown_variant
T12 frontend: the store accepts an arbitrary slug string, persist v4 keeps a valid slug, resets a
    malformed one to "english", and reconciles an absent-or-unavailable slug to the first playable row
T13 frontend: an unavailable variant renders as disabled in the Settings panel
```

## 9. Validation — the eight standing gates

Baseline at `8c00a33`, Orchestrator-measured. Match or exceed:

```text
mypy               Success: no issues found in 83 source files
ruff               All checks passed!
manage.py check    System check identified no issues (0 silenced).
pytest             370 passed, 4 skipped in 197.79s
npm run typecheck  exit 0
npx vitest run     342 passed | 3 skipped   (26 files passed | 1 skipped)
npm run lint       exit 0
npm run build      exit 0
```

⚠️ **The frontend suite has been 342 for three consecutive slices, which was the standing proof that no frontend file had been touched. This slice breaks that streak deliberately** — it is the first to change the frontend. Report the new number and account for every added test.

Execution route — mandatory bounded deviation under RF-16:

```text
Declared route that could not be used:  poetry run <tool>, as documented in AGENTS.md
Exact alternate path, from backend/:    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python …
Rationale:  the Cursor AppImage environment intercepts python* through inherited APPIMAGE / ARGV0 /
            APPDIR / PYTHONHOME
Evidence class: reproduced-dynamic, established repeatedly in this project
Bounded authority: this task only
Stopping condition: if .venv/bin/python is absent or the deviation fails, STOP. Do not use ambient
            python, python3, or poetry run, and do not repair the environment.
```

Four traps that have each cost a real session here:

1. `backend/pyproject.toml` sets `addopts = "-q"`. A second `-q` **silently suppresses the pytest summary line.** Run plain `-m pytest` and quote the summary verbatim.
2. Run mypy on the **full** documented scope. A narrowed set once hid 62 errors behind a reported 12 for six consecutive sessions.
3. `npm run build` and `npm run dev` share `frontend/.next`. Run `ss -tlnp | grep :3000` first; **a listener means stop and report — do not build and do not kill it.**
4. `npm run build` can pass while type errors exist because `tsconfig.json` sets `incremental: true`. State **"the build passed"** and **"the code type-checks"** as two separate claims.

⚠️ **Two 50 MB text assets enter the tree.** Report the repository size before and after, confirm neither file is in `.gitignore`, and confirm Git stores them as ordinary blobs — there is no LFS in this project and you must not introduce one.

One thing you must **establish rather than assume**: whether a per-variant AI move/judge prompt spec exists for a newly installed variant, or whether a new variant falls back to the English spec. Report what you find. It bounds a risk rather than blocking the slice — `PROJECT_CONTEXT.md` section 6 records that the engine authors every move in this product and the free LLM has authored zero backend-valid placements, so a missing spec degrades prompt quality, not playability. Measure it, do not infer it.

## 10. Git authority and sequence

```text
Authorized: git status, diff, log, show, rev-parse, ls-remote, add <explicit paths>, commit,
            one non-force git push origin main
Forbidden:  git add -A, git add ., force push, amend, rebase, reset, revert, clean, stash, branch,
            tag, checkout of another ref, any remote or config modification
```

1. stage by **explicit path only**;
2. re-check porcelain and confirm the ten flag images are still untracked and unstaged;
3. review the complete staged diff — for the two lexicons confirm the staged blob hash rather than reading 100 MB of words;
4. commit: `feat(variants): activate Czech and Polish as playable variants`;
5. pre-push gate: `git ls-remote origin refs/heads/main` **must still equal** `8c00a331560f16b7d27eae04dc789a5124dd4497`. If it advanced, **stop, push nothing, report**;
6. one non-force `git push origin main`;
7. public readback: `ls-remote` compared with `git rev-parse HEAD`, both quoted.

## 11. Stopping conditions

Stop, preserve state, and report: any repository gate fails; a copied lexicon's SHA-256 does not match section 5; your sourced tile distribution does not reproduce the section 6a invariants exactly; a manifest is rejected by the F1 loader; the endpoint would need to expose a fifth field; port 3000 has a listener at build time; the pre-push gate does not match; the `.venv` route is unavailable; you find a pre-existing defect outside the allowlist — **record it, do not fix it**. If the same failing gate survives one correction attempt with an unchanged hypothesis and candidate, report `PARTIAL` or `BLOCKED` with exactly `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`.

## 12. Report contract

Begin **exactly** `### Report for ORCHESTRATOR_CHAT`. Echo the coordinates once: logical whole `czech-polish-hungarian-variant-activation`, Worker session `02`, Worker exchange `01`.

Then: status; `Phase-qualified result`; start and end commit; the section 3 gate quoted; every changed path with its purpose; the post-copy SHA-256 of all four asset files against the section 5 values; **the complete sourced tile distribution for each language with its arithmetic** — total tiles, entry count, blank count, nominal points, non-blank kinds, and the tileless-letter set — plus the exact retrieval source and date; the `load_variant()` result for both; the exact JSON body the endpoint returns for all four variants; the eight gates with pytest and vitest summaries verbatim, the two build claims separate, and the new frontend test count accounted for; the pre-fix / post-fix table for T1 through T13; the repository size before and after with confirmation of no LFS and no `.gitignore` entry; what you established about per-variant AI prompt specs; explicit confirmation that Hungarian was not added, that `gamecore/` and the wire format are unchanged, and that no migration or database write occurred; deviations, risks and missing evidence honestly; `Resolved Execution Issues / Near-Misses`; `Pre-Existing Failure Classification`; commit and push with the public readback; one smallest next step; `Report justification: new-mutation`; `Logical-whole closure: not-closed`; an explicit authority-expiry statement.

Finish with a short section titled **COOPERATOR ACCEPTANCE STEPS**: the exact numbered things the Cooperator should click to see Czech and Polish working, written for someone opening the running product — which page, which control, what to expect, and one Czech and one Polish word he can play that you have verified are in the lexicons.

⛔ Do not emit any logical-whole closure signal. Your evidence is **non-independent** — say so.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_implementation_00.md
Destination path: /home/agile/meta/projects/libretiles/11/02-czech-polish-hungarian-variant-activation/
Archival: wait-for-report
```

You do not archive this pair. The Cooperator does, after your report exists.

Your authority expires at your terminal report.
