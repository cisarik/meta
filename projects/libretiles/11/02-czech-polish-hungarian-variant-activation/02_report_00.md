Lexikóny sú overené, kód je na `main` a report ide Orchestrátorovi.

### Report for ORCHESTRATOR_CHAT

logical whole `czech-polish-hungarian-variant-activation`, Worker session `02`, Worker exchange `01`

**status:** `PASS`  
**Phase-qualified result:** Implementation PASS (bounded candidate produced and validated). Evidence is **non-independent**. Independent acceptance was not required and was not performed.  
**Start commit:** `8c00a331560f16b7d27eae04dc789a5124dd4497`  
**End commit:** `2917251aba19706e59aea5d50df8cbf353cea7ad`

## Section 3 gate (quoted)

```text
Working directory: /home/agile/Projects/libretiles
Expected branch: main
git rev-parse HEAD                   == 8c00a331560f16b7d27eae04dc789a5124dd4497
git rev-parse HEAD:.ap               == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD            == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git status -sb                       == ## main...origin/main
git ls-remote origin refs/heads/main == 8c00a331560f16b7d27eae04dc789a5124dd4497	refs/heads/main
git status --porcelain=v1            == exactly the ten untracked Cooperator flag images
ss -tlnp | grep -E ':(3000|8000)'    == empty (no listeners)
```

Porcelain at gate and after commit/push remained exactly:

`frontend/public/{cs.png,cz.jpeg,en.jpeg,en.png,hu.jpeg,hu.png,pl.jpeg,pl.png,sk.jpeg,sk.png}`. Untouched.

## Changed paths and purpose

| Path | Purpose |
|---|---|
| `backend/assets/dicts/czech.txt` | Verified Czech lexicon, byte-for-byte copy |
| `backend/assets/dicts/czech.LICENSE` | Upstream Czech licence text, byte-for-byte copy |
| `backend/assets/dicts/polish.txt` | Verified Polish lexicon, byte-for-byte copy |
| `backend/assets/dicts/polish.LICENSE` | Upstream Polish licence text, byte-for-byte copy |
| `backend/assets/variants/czech.json` | Czech manifest (alphabet, tiles, no two-tile file) |
| `backend/assets/variants/polish.json` | Polish manifest (alphabet, tiles, no two-tile file) |
| `backend/game/views.py` | `GET` listing: four public fields, readiness, omit-malformed |
| `backend/game/urls.py` | `variants/` **before** `<str:game_id>/` |
| `backend/tests/test_czech_polish_variants.py` | T1–T11 |
| `frontend/src/lib/types.ts` | `VariantSummary` four-field type |
| `frontend/src/lib/api.ts` | authenticated `getVariants()` on existing `request()` |
| `frontend/src/lib/variants.ts` | slug syntax + fetch-time reconcile |
| `frontend/src/hooks/useGameStore.ts` | `SelectedVariantSlug = string`; persist v4 |
| `frontend/src/lib/i18n/messages.en.ts` / `messages.sk.ts` | Czech/Polish variant-name keys only |
| `frontend/src/components/settings/GameLanguagePanel.tsx` | discovered list; unavailable disabled |
| `frontend/src/app/settings/page.tsx` | fetch + persist reconcile |
| `frontend/src/app/play/page.tsx` | block create/join if fetch fails or no playable row |
| `frontend/src/hooks/useGameStore.test.ts` | T12 persist v4 |
| `frontend/src/lib/variants.test.ts` | T12 reconcile |
| `frontend/src/components/settings/GameLanguagePanel.test.ts` | T13 |
| `frontend/src/lib/api.test.ts` | bearer `getVariants()` |

No Hungarian assets. `backend/gamecore/` unchanged. Wire format / F2b adapter unchanged. No migration, no database write, no `.env` read/write.

## Post-copy SHA-256 vs section 5

All four matched after `cp` and `cmp`:

| File | Bytes | SHA-256 |
|---|---|---|
| `czech.txt` | 54 105 021 | `919d6bac41b0938bc1955685b826857aa21543d4dd45a4035c1fa08aa4cc5bdc` |
| `czech.LICENSE` | 72 790 | `bde41b518094f12ea79bdfc1396a6b9562bc1d994da1fd37a07a06fd71f185a8` |
| `polish.txt` | 51 607 141 | `605d5a43d5d5dcd1b386ab9f9f62b72eb964882f6a9ccbe244a826e0baa06aab` |
| `polish.LICENSE` | 30 427 | `869efadec82ae6aba8270ca5a3eaa6fce4bfd2336824548f03acae037b5aa9c3` |

Staged Git blob SHA-1 (ordinary blobs, not LFS): `czech.txt` `dd7f0970f8c63d138a3d3baa74c27e10f8a348c1`; `czech.LICENSE` `8ebdc4242ebfc0d95541455d75d59d78f1e7eef9`; `polish.txt` `a2267069e12b6f05be993ab8931bf2e710039e32`; `polish.LICENSE` `7e39dd505da5d61b15ed5305af9b7c4926d656ed`.

## Sourced tile distributions

**Source:** `https://en.wikipedia.org/wiki/Scrabble_letter_distributions`  
**Retrieval date:** 2026-09-01  
**Sections used:** `### Czech` (“Czech-language sets use the following 100 tiles”, **not** Písmenkovka) and `### Polish` (“Polish-language editions of Scrabble use these 100 tiles”, current set since 2000; **not** old/Literaki/Scriba).

JSON does not permit comments. Czech `alphabet_order` is a **deterministic engine total order** (tile order, starting draw, blank picker), **not** ČSN 97 6030 dictionary collation (which folds `Á Ď É Ě Í Ň Ó Ť Ú Ů Ý` to the base letter at the primary level).

### Czech — `load_variant("czech")` succeeded (no `VariantManifestError`)

`language=Czech`, `slug=czech`, `language_code=cs`, `two_tile_words_file=None`.

| Invariant | Value |
|---|---|
| total tiles | 100 |
| letter entries | 40 |
| blanks | 2 |
| nominal points (`sum count*points`) | 205 |
| non-blank kinds | 39 |
| tileless alphabet letters | `{CH, Q, W}` |
| multi-char **tiles** | NONE (`CH` is alphabet-only, not a tile) |

Tiles (count × points): `?` 2×0; 1pt: O×6 A×5 E×5 N×5 I×4 S×4 T×4 V×4 D×3 K×3 L×3 P×3 R×3; 2pt: C×3 H×3 Í×3 M×3 U×3 Á×2 J×2 Y×2 Z×2; 3pt: B×2 É×2 Ě×2; 4pt: Ř×2 Š×2 Ý×2 Č×1 Ů×1 Ž×1; 5pt: F×1 G×1 Ú×1; 6pt: Ň×1; 7pt: Ó×1 Ť×1; 8pt: Ď×1; 10pt: X×1.

Points: 52+46+18+36+15+6+14+8+10 = **205**. `playable_letters[0:2] == (A, Á)`.

### Polish — `load_variant("polish")` succeeded (no `VariantManifestError`)

`language=Polish`, `slug=polish`, `language_code=pl`, `two_tile_words_file=None`. **No Q, V, X tiles.**

| Invariant | Value |
|---|---|
| total tiles | 100 |
| letter entries | 33 |
| blanks | 2 |
| nominal points | 190 |
| non-blank kinds | 32 |
| tileless alphabet letters | `{}` |
| multi-char tiles | NONE |

Tiles: `?` 2×0; 1pt: A×9 I×8 E×7 O×6 N×5 Z×5 R×4 S×4 W×4; 2pt: Y×4 C×3 D×3 K×3 L×3 M×3 P×3 T×3; 3pt: B×2 G×2 H×2 J×2 Ł×2 U×2; 5pt: Ą Ę F Ó Ś Ż ×1; 6pt: Ć×1; 7pt: Ń×1; 9pt: Ź×1.

Points: 52+50+36+30+6+7+9 = **190**. `playable_letters[0:2] == (A, Ą)`.

## Endpoint JSON (authenticated, shipped assets)

`GET /api/game/variants/` returns exactly:

```json
[
  {"slug": "english", "display_name": "English", "language_code": null, "readiness": "playable"},
  {"slug": "czech", "display_name": "Czech", "language_code": "cs", "readiness": "playable"},
  {"slug": "polish", "display_name": "Polish", "language_code": "pl", "readiness": "playable"},
  {"slug": "slovak", "display_name": "Slovak", "language_code": "sk", "readiness": "playable"}
]
```

Order: `english` first, then display name, then slug. Four keys only. Unauthenticated: HTTP 401. Default `IsAuthenticated` was **not** overridden.

## Eight standing gates

RF-16 route: `env -u APPIMAGE -u ARGV0 -u APPDIR -u PYTHONHOME backend/.venv/bin/python …` (not `poetry run`). `.venv/bin/python` was present.

```text
mypy               Success: no issues found in 83 source files
ruff               All checks passed!
manage.py check    System check identified no issues (0 silenced).
pytest             381 passed, 4 skipped in 215.44s (0:03:35)
npm run typecheck  exit 0
npx vitest run     352 passed | 3 skipped   (28 files passed | 1 skipped)
npm run lint       exit 0
npm run build      exit 0
```

**The code type-checks** (`tsc --noEmit --incremental false`, exit 0). **The build passed** (`next build --webpack`, exit 0). Those are separate claims. Port 3000 had no listener at build time.

**Frontend test count:** baseline 342 → **352** (+10): persist v4 keep/reset/accept-slug (3); reconcile + slug syntax (5); GameLanguagePanel disabled (1); `getVariants` bearer (1). Backend 370 → **381** (+11 = T1–T11).

## T1–T13 pre-fix / post-fix

| ID | Pre-fix (absence before this slice) | Post-fix |
|---|---|---|
| T1 | no `czech.json`/`polish.json`; `load_variant` FileNotFound | both load with no `VariantManifestError` |
| T2 | no manifests | czech 100/40/2/205; polish 100/33/2/190 |
| T3 | n/a | tileless `{CH,Q,W}` vs `{}`; 39 / 32 non-blank kinds |
| T4 | n/a | `Á` after `A`; `Ą` after `A` in `playable_letters` |
| T5 | n/a | every **tile** token has `len==1` (Czech `CH` remains alphabet-only) |
| T6 | lexicons not in tree | `domu`/`knihy` and `domach`/`książki` pass; `qxqxqxqxq` fails via `_word_passes_dictionary` |
| T7 | no endpoint | exact key set `{slug, display_name, language_code, readiness}` |
| T8 | n/a | unauthenticated GET → 401 |
| T9 | n/a | synthetic missing dict → `unavailable`; no path/filename in body |
| T10 | n/a | malformed omitted; not listed as `unavailable` |
| T11 | `unknown_variant` for czech | create `czech` 201; `klingon` `unknown_variant` |
| T12 | union `"english"\|"slovak"`; persist v3 | string slug; v4 keeps `czech`/`hungarian`; resets malformed; reconcile to first playable |
| T13 | two hardcoded buttons | unavailable renders `disabled` + `aria-disabled="true"` |

## Repository size, LFS, gitignore

Before: **1 237 843 739** B. After: **1 338 017 904** B (Δ ≈ 100.2 MB).  
`git check-ignore` on the four new dict files: not ignored. No `.gitattributes`. `git lfs ls-files` empty after add/commit. LFS was **not** introduced. GitHub printed a **warning** that `czech.txt` is 51.60 MB (over the 50 MB *recommendation*); push still succeeded as an ordinary blob. Polish is under 50 MB.

## Per-variant AI prompt specs (measured, not inferred)

`frontend/src/lib/prompts.ts`: `MovePromptLexiconId` / `JudgePromptLexiconId` are `"collins2019" | "slovak"`. `movePromptSpecFromContext` / `judgePromptSpecFromBody` return the Slovak spec only when `lexicon_id` or `variant` is `"slovak"`; **otherwise English/Collins**. Czech (`lexicon_id=czech`) and Polish (`lexicon_id=polish`) therefore receive the **English CORE**. That degrades prompt quality, not engine playability. Out of this slice.

## Explicit confirmations

- Hungarian was **not** added (no `hungarian.txt` / `.LICENSE` / `.json`).
- `backend/gamecore/` and the wire format / F2b adapter are unchanged.
- No migration, no `makemigrations`, no database write.
- Formed-word invariant: Czech/Polish have no two-tile file; two-letter words route to the main dictionary (English pattern). No `"am" not in word` logic was added.

## INFOSEC (R1 + R2, inline, non-independent)

**Threat model:** assets = variant metadata and lexicon files; trust boundary = authenticated `GET /api/game/variants/`; no attacker-controlled request body; security properties = fail-closed `IsAuthenticated`, four-field response, omit-malformed without reasons; abuse case = filesystem path / filename / word-count / exception leak.  
**R2 self-review:** response construction never interpolates `exc`, paths, or dictionary names; T7/T9/T10 lock the key set and redaction. No candidate above `low`. This review does not certify.

## Deviations, risks, missing evidence

- RF-16 AppImage python route, as authorized.
- GitHub large-file **warning** on `czech.txt` (51.60 MB). Residual operational risk if GitHub later tightens the 50 MB recommendation; LFS remains forbidden here.
- Play page still labels the human queue “English queue” unless the slug is exactly `slovak`. Left untouched (`ui-internationalization`).
- Browser/Cooperator click-through of a live game was not this Worker’s validation ladder.

## Resolved Execution Issues / Near-Misses

1. Duplicate empty `_action_error_status` after a patch (ruff SyntaxError). Removed the empty def. Residual: none.  
2. First T5 draft asserted `len==1` on `alphabet_order`, which fails on Czech tileless `CH`. Corrected to **tiles only**, matching the F2b wire-adapter claim. Residual: none.  
3. `api.test.ts` `as [string, RequestInit]` failed `tsc`; recast via `unknown`. Residual: none.  
4. T13 used `toContain("disabled")` on a playable button that has `aria-disabled="false"`. Tightened to the HTML `disabled` token vs `aria-disabled`. Residual: none.

## Pre-Existing Failure Classification

none

## Commit and push

```text
git commit  2917251aba19706e59aea5d50df8cbf353cea7ad
            feat(variants): activate Czech and Polish as playable variants
pre-push    origin/main still 8c00a331560f16b7d27eae04dc789a5124dd4497
git push    origin main  (non-force)
            8c00a33..2917251  main -> main
readback    ls-remote origin refs/heads/main
            == 2917251aba19706e59aea5d50df8cbf353cea7ad
            == git rev-parse HEAD
```

## Smallest next step

Hungarian remains blocked on a real inflection lexicon (not the stem list). Optionally a later slice can add Czech/Polish MOVE/JUDGE specs so the free LLM is not primed on Collins while the engine scores Czech/Polish.

**Report justification:** `new-mutation`  
**Logical-whole closure:** not-closed  
**Authority:** expires at this terminal report. This Worker will not continue autonomously.

---

## COOPERATOR ACCEPTANCE STEPS

1. Sign in. Open **Settings**.  
2. In **Game variant**, you should see **English, Slovak, Czech, and Polish** (not Hungarian). Names follow the UI language (English catalog vs Čeština/Poľština).  
3. Select **Czech**. Back to the play screen. Start a new AI (or human) game.  
4. On the Czech board, a legal opening can use **`DOMU`** or **`KNIHY`** — both are in the shipped Czech lexicon.  
5. Start another game, select **Polish**, and play **`DOMACH`** or **`KSIĄŻKI`** — both are in the shipped Polish lexicon.  
6. A two-letter Czech/Polish word is accepted or rejected by the **main dictionary**, the same way English works (there is no separate two-tile file).