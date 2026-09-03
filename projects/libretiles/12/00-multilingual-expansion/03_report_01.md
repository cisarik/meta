### Report for ORCHESTRATOR_CHAT

logical whole multilingual-expansion, Worker session ordinal 03, Worker exchange ordinal 02

Status: **PASS**
Phase-qualified result: `implementation-PASS`
Result artifact or commit: `21f0a149bd5591bac492d6f024ddd6a46998c0cf`
Result evidence: readiness is now content-aware and fails closed (T13 proves a present-but-corrupt lexicon reads `unavailable` through the real endpoint); the non-canonical-filename hazard you re-measured is rejected with the reused `slug_stem_mismatch` code (G28); the omit branch carries a private discriminator with no public change (T14); `manage.py validate_lexicons` exits 0 on all five shipped assets; the cheap tier reads 262 730 bytes total instead of 154 MB; all eight gates green (`491 passed, 4 skipped in 229.12s`, mypy 85 files, every frontend number unchanged); one non-force push with matching readback.

Start commit: `1f39ff4da678ffb519222e6cd97a90117298a371`
End commit: `21f0a149bd5591bac492d6f024ddd6a46998c0cf`

## Section 3 re-gate — verbatim values

```text
git rev-parse HEAD                    1f39ff4da678ffb519222e6cd97a90117298a371   MATCH
git rev-parse HEAD:.ap                9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   MATCH
git -C .ap rev-parse HEAD             9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   MATCH (detached, correct)
git status -sb                        ## main...origin/main                      MATCH
git status --porcelain=v1             (empty)                                    MATCH
git ls-remote origin refs/heads/main  1f39ff4da678ffb519222e6cd97a90117298a371   MATCH
ss -tlnp | grep -E ':(3000|8000)'     no output, grep exit 1  -> no listener
git diff 5f63e0d 1f39ff4 --stat       backend/tests/test_variant_invariants.py | 7 ++++--- (4 insertions, 3 deletions)
git log --oneline -3                  1f39ff4 docs(variants): correct the G26a docstring after slug_stem_mismatch landed
                                      5f63e0d fix(variants): reject a manifest whose declared slug disagrees with its filename
                                      61720aa test(variants): pin manifest stem/slug agreement and reject a declared total_tiles
```

Nothing conflicted with retained context, so no recovery class was engaged. I re-read the amended `G26a` docstring at `test_variant_invariants.py:363-380` before touching the file and confirmed it is the exact one-line replacement from my exchange-01 report plus a sentence about keeping the shipped manifests honest; it is now accurate and I left it untouched. `.ap` was never attached or updated, and its gitlink is unchanged after my commit. `:3000` was re-checked immediately before `npm run build`: still free, nothing killed.

End-of-task porcelain re-confirmation:

```text
git status --porcelain=v1   (empty)
git status -sb              ## main...origin/main
git diff --name-only 1f39ff4..HEAD   the seven allowlisted paths, nothing else
```

## Changed files and purpose

| Path | Purpose |
|---|---|
| `backend/gamecore/lexicon_health.py` (NEW, 250 lines) | pure two-tier lexicon health, no Django import: cached bounded `check_lexicon` for readiness, whole-file `audit_lexicon` for the command |
| `backend/gamecore/variant_store.py` | second `slug_stem_mismatch` condition on the raw filename; the false exchange-01 sentence deleted and replaced with what is true |
| `backend/game/views.py` | `_variant_resources_ready` consults the cheap tier; `_omit_reason` discriminator on the omit branch; the 5e one-line comment |
| `backend/game/management/commands/validate_lexicons.py` (NEW, 105 lines) | read-only expensive-tier audit, non-zero exit on failure, not wired into boot or any request path |
| `backend/tests/test_lexicon_health.py` (NEW, 372 lines) | N1-N12, the filter-agreement test, the audit tier, and the two command tests |
| `backend/tests/test_variant_invariants.py` | G28 only; `G26a` and `G26b` assertions untouched |
| `backend/tests/test_czech_polish_variants.py` | T13, T14, plus a synthetic-asset-root helper; T7/T9/T10/T12 untouched |

No change to `game/serializers.py`, `game/services.py`, `gamecore/fastdict.py`, `gamecore/legality.py`, `backend/assets/**`, `test_dictionary_validation.py`, or any frontend file. No third readiness value, no second error code, no new dependency, no network, no secret. Staging was explicit seven-path, never `-A`/`.`.

## The cheap-tier rule list as implemented, quoted

`backend/gamecore/lexicon_health.py:128-149` (`_check_uncached`, reached only through the cached `check_lexicon`):

```python
def _check_uncached(path: Path, *, size: int) -> LexiconHealth:
    if size == 0:
        return LexiconHealth(ok=False, reason="empty")
    try:
        with path.open("rb") as handle:
            head = handle.read(MAX_PREFIX_BYTES)
    except OSError:
        return LexiconHealth(ok=False, reason="unreadable")
    if head.startswith(_UTF8_BOM):
        return LexiconHealth(ok=False, reason="bom", bytes_read=len(head))
    text = _decode_bounded(head, truncated=len(head) < size)
    if text is None:
        return LexiconHealth(ok=False, reason="invalid_utf8", bytes_read=len(head))
    survivors = sum(1 for line in text.splitlines() if surviving_word(line) is not None)
    if survivors == 0:
        return LexiconHealth(ok=False, reason="no_surviving_word", bytes_read=len(head))
    return LexiconHealth(
        ok=True,
        reason="ok",
        surviving_words_in_prefix=survivors,
        bytes_read=len(head),
    )
```

The existence and regular-file rule sits in `check_lexicon` at `:152-172` (`path.is_file()` → `missing`). `MAX_PREFIX_BYTES = 65_536` at `:47`. The cut-character tolerance is `_decode_bounded` at `:104-126`: when — and only when — the read stopped short of EOF, the prefix is trimmed at the last `b"\n"`, and if there is no newline the trailing incomplete sequence (at most 3 bytes) is discarded before a second strict decode. The surviving-line filter is `surviving_word` at `:86-101`: comment test against the RAW line, `strip`, NFC-casefold, `str.isalpha`, `len >= 2`. It mirrors `gamecore/fastdict.py:_read_words` and adds only the two-code-point floor the product itself applies at `game/services.py:216`; a test asserts that the only difference from the real index is the single-code-point token.

## The cache key I chose, and why

`backend/gamecore/lexicon_health.py:166`:

```python
    key = (str(path.resolve()), info.st_size, info.st_mtime_ns)
```

`resolve()` collapses symlinks and relative forms so two spellings of one asset share an entry. `st_size` and `st_mtime_ns` together mean a lexicon rebuilt in place invalidates instead of being trusted for the life of the process — keying on the path alone would have made a corrupt-then-repaired file permanently `unavailable`, and a repaired-then-corrupted file permanently `playable`. Size is carried alongside mtime deliberately: mtime granularity is filesystem-dependent, so two writes inside one tick can share `st_mtime_ns`, and N12 changes both. A file that cannot be stat-ed produces no key and is therefore not cached at all, so an asset that appears later is picked up without a restart. The module-level dict follows the existing precedent at `gamecore/fastdict.py:_INDEX_CACHE`.

## Test table

| Test | Class | Pre-change evidence |
|---|---|---|
| T13 `test_t13_present_but_corrupt_lexicon_reads_unavailable` | **B (headline)** | `E AssertionError: assert [{'display_na...': 'corrupt'}] == [{'display_na...': 'corrupt'}]` / `At index 0 diff: {'slug': 'corrupt', 'display_name': 'Corrupt', 'language_code': 'xx', 'readiness': 'playable'} != {... 'readiness': 'unavailable'}` at `tests/test_czech_polish_variants.py:391`; `1 failed in 0.81s`. Captured before `_variant_resources_ready` was touched. |
| T14 `test_t14_omit_branch_reason_discriminates_the_failure_class` | B | `E AssertionError: assert [{'display_na...ug': 'de-ch'}] == []` / `Left contains one more item: {'display_name': 'Divergent', 'language_code': None, 'readiness': 'playable', 'slug': 'de-ch'}` at `tests/test_czech_polish_variants.py:444`, with `Captured stderr call: ERROR game variant_list_omitted` — the bare, reason-less line. |
| G28 `test_g28_a_non_canonical_manifest_filename_is_rejected` | B | `E Failed: DID NOT RAISE <class 'gamecore.variant_store.VariantManifestError'>` at `tests/test_variant_invariants.py:445`; `1 failed in 0.14s`. |
| N1-N6, N12, the audit cases, the two command cases (26 cases in the new module) | B | Collection-time `E ModuleNotFoundError: No module named 'gamecore.lexicon_health'` at `tests/test_lexicon_health.py:30`; `1 error in 0.17s`. That is the only possible pre-change state for a module that does not exist; the behavioural pre-change failure of the rule they encode is T13, which fails at the HTTP boundary. |
| N7, N8, N9, N10, N11 | A | pin correct behaviour; all pass on first run, N8 over every installed variant. |
| G26a, G26b, T7, T9, T10, T12 | A | unchanged and still passing; `G26a`/`G26b` assertions were not edited. |

T14's pre-change failure is worth naming separately: at the baseline the public payload actually advertised `{'slug': 'de-ch', 'display_name': 'Divergent', 'readiness': 'playable'}` for a manifest no code path can load. Your section 2 hazard was not merely internal — it reached the public catalog as `playable`.

Post-change focused runs: `tests/test_lexicon_health.py` **26 passed in 10.65s**; `test_variant_invariants.py + test_czech_polish_variants.py + test_atomic_tile_tokens.py + test_dictionary_validation.py + test_slovak_variant.py` **128 passed in 25.75s**.

## The four shipped lexicons under the cheap tier

Measured through the shipped code path after the change (`MAX_PREFIX_BYTES = 65536`):

```text
  slug     asset       ok    reason  file_size    bytes_read  fraction   survivors_in_prefix
  czech    dictionary  True  ok      54 105 021   65 536      0.001211   5306
  english  dictionary  True  ok       3 103 812   65 536      0.021115   5939
  polish   dictionary  True  ok      51 607 141   65 536      0.001270   5450
  slovak   dictionary  True  ok      45 456 204   65 536      0.001442   4294
  slovak   two_tile    True  ok             586      586      1.000000    103
  TOTAL bytes read across all five assets: 262 730
  _variant_resources_ready: czech True, english True, polish True, slovak True
```

262 730 bytes against 154 272 565 bytes of shipped lexicon: no request path reads a whole file, and the largest asset is touched for 0.12 % of its length. The two-tile file is read in full only because it is 586 bytes, i.e. smaller than the bound. No shipped asset reports not-ok, so no trap fired and no shipped asset was relaxed. Every shipped manifest still loads under the extended 5a check (stems `czech`, `english`, `polish`, `slovak` are all identical to their own `slugify`).

## Section 5e, measured

**Unreachable.** A manifest that is both stem/slug divergent and names an absent lexicon (`de.json` declaring `"slug": "german"` with `dictionary_file: "definitely_absent_lexicon.txt"`) reaches the `except Exception` branch, not `_summary_from_payload`:

```text
_load_variant_from_path -> VariantManifestError code='slug_stem_mismatch'
PUBLIC BODY: []
game log records: ['variant_list_omitted reason=slug_stem_mismatch']
branch: except Exception -> omitted
```

The ingest check runs before `validate_dictionary_file`, so `VariantManifestError` wins and `FileNotFoundError` is never raised for this input. There is no leak of a declared slug, so no stop was required. Per 5e's instruction the finding is recorded as a one-line comment in the branch itself, `game/views.py:141-142`. My exchange-01 LEAD 1 was therefore correct, and it is now measured rather than believed.

## Public payload and log discipline

The four keys, their values and their ordering are unchanged. `VariantSummary`, `_summary_from_payload`, the summary dict literal and the `summaries.sort` key were not edited; only the boolean input to `readiness` changed. T7 (exact key set and full row equality for english/czech/polish/slovak, all `playable`), T9 (`unavailable` for a missing lexicon), T10 (omission with no leak) and T12 (omission of a divergent manifest) all pass unmodified, and T13 asserts the four-key set again for the new `unavailable` case.

No log record carries a path or a filename. T14 asserts, for both records, that the message starts with the preserved greppable token `variant_list_omitted` and contains no `/`, no `.json`, no `.txt`, no `De_Ch`, no `broken`, and not `str(tmp_path)`. The two reasons differ and are exactly `{"JSONDecodeError", "slug_stem_mismatch"}`. All five omit sites now carry a token (`directory_unreadable`, the exception discriminator, `incomplete_manifest`, `unnamed_variant`, the exception discriminator); giving the JSON-parse site one was necessary because a `{not json` file never reaches the `except Exception` branch, so T14 could not otherwise exist.

## Eight standing gates

```text
1  mypy config game gamecore accounts catalog   Success: no issues found in 85 source files
2  ruff check .                                 All checks passed!
3  manage.py check                              System check identified no issues (0 silenced).
4  pytest                                       491 passed, 4 skipped in 229.12s (0:03:49)
   pytest --collect-only                        495 tests collected in 6.76s
5  npm run typecheck                            exit 0
6  npx vitest run                               Test Files  31 passed | 1 skipped (32)
                                                Tests  450 passed | 3 skipped (453)
7  npm run lint                                 exit 0
8  npm run build                                exit 0
```

mypy rose from 83 to **85** source files, exactly the two new production modules, as anticipated. pytest rose from 462 to 491 passed (+29 = 26 new cases in `test_lexicon_health.py` + G28 + T13 + T14), collection 466 → 495, skips unchanged at 4. Every frontend number is identical to baseline: vitest `450 passed | 3 skipped`, and `npm run build` produced **eleven dynamic (`ƒ`) routes and zero static routes**.

Two separate claims: **the production build passed** (`next build --webpack`, exit 0) and **the code type-checks** (`npm run typecheck` = `tsc --noEmit --incremental false`, exit 0). Trap discipline: plain `-m pytest` with no second `-q` and the summary quoted verbatim; mypy on the full five-package scope; `:3000` verified free before the build and never killed.

RF-16 route used exactly as declared (`env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m …`, `.venv/bin/ruff`, `manage.py check` with no `-m`); `backend/.venv/bin/python` present; no ambient `python3`, no `poetry run`.

## Wall clock

```text
before  220.23s   ORCHESTRATOR-measured at 1f39ff4 (section 7); my own independent
                  pre-change measurement of the same code in exchange 01 was 214.29s
after   229.12s   my measurement, this session (shell wall clock 237s including startup)
growth  +8.89s against the section 7 baseline; +14.83s against the conservative 214.29s
```

Well inside the 60-second ceiling, so no mitigation was needed and the validation is intact. The dominant new cost is the command test that streams all five shipped assets: `manage.py validate_lexicons` measured standalone at **11.1 s real** for 154 MB. If that ever needs shrinking, the smallest change that keeps the validation is to give the shipped-set command test its own bounded scope (audit one large lexicon plus English per run, rotating) rather than weakening any rule — I did not do this, because it is not needed at +8.89 s.

For completeness, the expensive tier's own measurements (the numbers the duplicate policy rests on): czech 3 930 497 surviving tokens, english 279 496, polish 3 721 704, slovak 3 005 250, slovak two-tile 103 — **zero duplicates and zero non-NFC lines everywhere**, peak RSS ~504 MB during the largest file. The command's real output:

```text
czech dictionary ok reason=ok words=3930497 duplicates=0 non_nfc=0
english dictionary ok reason=ok words=279496 duplicates=0 non_nfc=0
polish dictionary ok reason=ok words=3721704 duplicates=0 non_nfc=0
slovak dictionary ok reason=ok words=3005250 duplicates=0 non_nfc=0
slovak two_tile ok reason=ok words=103 duplicates=0 non_nfc=0
validate_lexicons: 5 asset(s) audited, 0 failed
exit=0
```

## Git sequence

```text
git add <seven explicit paths>
git status --porcelain=v1   A  backend/game/management/commands/validate_lexicons.py
                            M  backend/game/views.py
                            A  backend/gamecore/lexicon_health.py
                            M  backend/gamecore/variant_store.py
                            M  backend/tests/test_czech_polish_variants.py
                            A  backend/tests/test_lexicon_health.py
                            M  backend/tests/test_variant_invariants.py   (exactly seven)
git diff --cached --stat    7 files changed, 953 insertions(+), 24 deletions(-)
git commit                  [main 21f0a14] feat(variants): readiness fails closed on an invalid lexicon; close the filename-slug hazard
pre-push  git ls-remote origin refs/heads/main   1f39ff4da678ffb519222e6cd97a90117298a371   == exact baseline, gate satisfied
git push origin main        To https://github.com/cisarik/libretiles
                               1f39ff4..21f0a14  main -> main             (non-force fast-forward, exit 0)
readback  git ls-remote origin refs/heads/main   21f0a149bd5591bac492d6f024ddd6a46998c0cf
          git rev-parse HEAD                     21f0a149bd5591bac492d6f024ddd6a46998c0cf   EQUAL
```

No force, amend, rebase, reset, clean, stash, branch, or tag at any point.

## Deviations, risks, missing evidence

- **One instruction in 5b is internally inconsistent and I resolved it explicitly.** It says to mirror `fastdict._read_words` "exactly" *and* to apply `len >= 2`. `_read_words` has no length floor; the floor lives in `game/services.py:216`. I implemented the conjunction (which is what the product actually accepts as a word, and what N6 demands), and said so in the module docstring and in a dedicated test that asserts the only difference from the real index is the single-code-point token. Had I mirrored `_read_words` literally, N6's single-character file would have reported `ok`.
- **Five omit sites carry a reason, not one.** 5c named the `except Exception` branch; T14's JSON-syntax case is caught at a different site, so the discriminator had to reach it. Leaving three of five bare would have preserved exactly the ambiguity 5c exists to remove.
- **Bounded checks are bounded.** If a lexicon larger than 64 KiB has its only invalid UTF-8 after the last newline inside the prefix, the cheap tier will not see it; the expensive tier will. This is inherent to a per-request bound and is documented in the module.
- **`min_words` is a floor, not a per-language datum.** The default 100 sits three orders of magnitude below the smallest shipped dictionary; the two-tile allowlist is audited with its own floor of 1, because 103 entries is by design and I refused to leave a shipped asset three units above a threshold.
- Risk of the shipped behaviour change: any deployment whose lexicon is truncated, BOM-prefixed, mojibake or header-only now advertises `unavailable` instead of `playable`. That is the intended fail-closed direction and is what makes the change E2. Fully reversible by reverting one commit; two files simply disappear.
- Missing evidence, stated plainly: this is **non-independent** evidence — I wrote the production change and its tests. The "before" wall clock at this exact baseline is ORCHESTRATOR-measured, not re-measured by me, because measuring it myself would have required restoring baseline code over my own working tree; I compensated by also comparing against my own 214.29 s measurement of the same pre-change code and reporting the larger growth. No browser, deployed-environment, or frontend-rendering check was performed; the frontend's reaction to a variant flipping to `unavailable` was verified only through unchanged frontend gates.

Resolved Execution Issues / Near-Misses:
1. **`**kwargs` expansion into a frozen dataclass, caught before any gate.** `audit_lexicon` first built its counters in a dict and expanded them into `LexiconAudit(**counters)`, which mypy strict cannot verify field-by-field. I rewrote it with explicit keyword arguments before running mypy, so the gate never saw it. Residual risk: none.
2. **Synthetic-word generator that its own filter would have rejected.** The healthy-synthetic command test first generated `word0000 … word0099`; those contain digits and do not survive `str.isalpha`, so the test would have asserted a pass on a lexicon the audit correctly fails. I replaced it with 100 distinct three-letter alphabetic tokens before the first run. This is exactly trap T1 in miniature and it very nearly bit the test rather than the code. Residual risk: none.
3. **`caplog` cannot see the `game` logger by default.** `config/settings.py:412-417` sets `propagate: False`, so T14 attaches `caplog.handler` to the `game` logger directly and removes it in a `finally`, mirroring `tests/test_multiplayer_ws.py:232-241`. Without this the test would have collected zero records and passed vacuously against the pre-change code.
4. **Cleanup outcome.** All scratch work stayed inside `/tmp/opencode/mle-v2b/` this time (no repeat of exchange 01's `tempfile.mkdtemp` near-miss); the directory and its five artifacts were deleted after the evidence was transcribed, and `ls` confirms the path is gone. `/tmp/opencode`, which I did not create, was left in place. No shipped asset was written to at any point.

Pre-Existing Failure Classification: none. Every baseline gate value reproduced or improved as predicted; the 4 pytest skips and 3 vitest skips are pre-existing and unchanged; no existing case was weakened, and no existing case failed for a reason outside sections 5a-5c.

```text
⚠ WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE
```

**MEASURED**

1. **The hazard was public, not internal.** T14's pre-change run shows the baseline endpoint returning `{'slug': 'de-ch', 'display_name': 'Divergent', 'language_code': None, 'readiness': 'playable'}` for `De_Ch.json`. Section 2 framed the defect through `list_installed_variants` and the three validation call sites; the same manifest also reached `GET /api/game/variants/` and read `playable`. The fix covers it, but the blast radius was one step wider than the prompt stated.
2. **`collins2019.txt` is CRLF, and nothing in the repository said so.** Line 1 is `Collins Scrabble Words (2019). 279,496 words. Words only.^M$`, line 2 is `^M$`, line 3 is `AA^M$`. `str.strip` absorbs the `\r`, so both the loader and the new filter are correct today — but any future rule that uses `line.rstrip("\n")`, `splitlines(keepends=True)`, or a byte comparison would break English only, and English is the default variant. N9 now pins the CRLF shape deliberately.
3. **The Collins header is self-certifying and it checks out.** The prose line claims 279 496 words; the expensive tier counted exactly 279 496 surviving tokens. That makes the header a free integrity oracle for the English asset, and nothing currently compares them.
4. **`_variants_dir()` mutates the filesystem from a read-shaped helper.** `gamecore/variant_store.py:172-175` calls `path.mkdir(parents=True, exist_ok=True)` on every list, so merely listing variants creates a directory. It is why a synthetic assets root works so cleanly in tests, and it is also a side effect nobody would expect from a function named like an accessor.
5. **`test_dictionary_validation.py:61` builds its own fourth copy of the line filter** (`ln.strip().casefold() for ln in text.splitlines() if ln.strip() and not ln.startswith("#")`) and, unlike the other three, drops the `isalpha` step. It is correct for what it asserts, and I did not touch the file per section 4, but it means the repository now has one canonical filter plus one ad-hoc reimplementation living next to it.
6. **The audit's exact duplicate count costs ~500 MB peak RSS on `czech.txt`** (a `set` of 3 930 497 tokens). Harmless here — 21.5 GB free, and the command is manual — but it is the one number in this slice that scales with vocabulary rather than with file size, and it now runs inside the pytest process.

**LEAD** (unmeasured, offered as leads only)

1. `_summary_from_payload`'s `FileNotFoundError` path is now, as far as I can tell, reachable only through a *missing lexicon on a manifest that is otherwise perfect* — every other route into it is pre-empted by the ingest check. If that is right, the branch has exactly one live input class and could eventually be narrowed to `except FileNotFoundError` from `validate_dictionary_file` alone. I did not enumerate the alternatives, so this is a hypothesis.
2. Readiness is per-request and now cached per file identity, but the *manifest* is still re-parsed on every request (`json.loads` plus a full `_load_variant_from_path` per file per call). A manifest-level cache keyed the same way as `check_lexicon` would remove more work than this slice did, and the three serializer/service call sites would benefit most. Unmeasured.
3. If a shipped lexicon ever flips to `unavailable`, a client holding that `variant_slug` in its persisted store has no repair path analogous to the model-catalog repair; the create/queue serializers validate against `list_installed_variants()`, which does not consult readiness at all, so an `unavailable` variant is still *selectable* server-side. I did not read the frontend selection code and did not test a create call against an `unavailable` variant.

Smallest next step: decide whether `unavailable` should also become unselectable at `game/serializers.py:180`/`:215` and `game/services.py:173` — today readiness is advisory to the client while those three sites still accept any installed slug, which is the last remaining gap of the shape this whole has been closing.

Report justification: `new-mutation`
Logical-whole closure: not-closed

Authority expiry: this terminal report expires my authority for exchange 02. I have stopped all autonomous work. Commit `21f0a14` is a candidate carrying non-independent implementation evidence only; it is not accepted, published, or closed by anything here. Any continuation requires a new complete prompt explicitly targeting this session.

Context pressure: moderate — roughly half the window consumed, mostly by the mandatory reading plus the four measurement rounds; no compaction occurred and headroom remained throughout.

