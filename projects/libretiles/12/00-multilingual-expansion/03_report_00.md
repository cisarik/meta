### Report for ORCHESTRATOR_CHAT

logical whole multilingual-expansion, Worker session ordinal 03, Worker exchange ordinal 01

Status: **PASS**
Phase-qualified result: `implementation-PASS`
Result artifact or commit: `5f63e0da2a4c0aba0edcd905e488c0f7a32163e9`
Result evidence: new fail-closed loader check `slug_stem_mismatch` at `backend/gamecore/variant_store.py:337-344`; T12 proves the divergent manifest is OMITTED from `GET /api/game/variants/` with no leak; G26b inverted; all eight gates green (`pytest 462 passed, 4 skipped`, +1 versus baseline, every frontend gate numerically unchanged); one non-force fast-forward push with matching public readback.

Start commit: `61720aa701132085809a9012ee29e446c622bd4f`
End commit: `5f63e0da2a4c0aba0edcd905e488c0f7a32163e9`

## Section 3 repository gate — verbatim values

```text
git rev-parse HEAD                    61720aa701132085809a9012ee29e446c622bd4f   MATCH
git rev-parse HEAD:.ap                9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   MATCH
git -C .ap rev-parse HEAD             9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   MATCH (detached, correct)
git status -sb                        ## main...origin/main                      MATCH
git status --porcelain=v1             (empty)                                    MATCH
git ls-remote origin refs/heads/main  61720aa701132085809a9012ee29e446c622bd4f   MATCH
ss -tlnp | grep -E ':(3000|8000)'     no output, grep exit 1  -> no listener
```

Re-checked `:3000` immediately before `npm run build`: no listener (grep exit 1). `.ap` never attached or updated; gitlink after the commit is still `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` and the submodule worktree is clean.

End-of-task porcelain re-confirmation:

```text
git status --porcelain=v1   (empty)
git status -sb              ## main...origin/main
git diff --name-only 61720aa..HEAD
  backend/gamecore/variant_store.py
  backend/tests/test_czech_polish_variants.py
  backend/tests/test_variant_invariants.py
```

## Changed files and purpose

| Path | Purpose |
|---|---|
| `backend/gamecore/variant_store.py` | one new fail-closed ingest check plus error code `slug_stem_mismatch`, placed before `validate_dictionary_file` (+20 lines, no other production change) |
| `backend/tests/test_variant_invariants.py` | G26b inverted from characterization to rejection; two docstring `file:line` references corrected for the lines my own insertion shifted |
| `backend/tests/test_czech_polish_variants.py` | new T12 proving the public omission and the absence of a leak |

No change to `game/views.py`, `game/serializers.py`, `game/services.py`, `slugify`, `_variant_path`, `load_variant`, `list_installed_variants`, `backend/assets/**`, or any frontend file. No new error code other than `slug_stem_mismatch`; no third readiness value; no dependency, network, or secret access. Staging was explicit three-path (`git add <paths>`), never `-A`/`.`.

## The exact new code path, quoted

`backend/gamecore/variant_store.py:324-344` (slug still computed at `:324`, so every existing `variant_store.py:324` reference stays valid):

```python
    slug = slugify(str(data.get("slug") or path.stem))
    # Fail closed when the declared slug disagrees with the manifest's own filename:
    # ``list_installed_variants`` advertises this computed slug while ``load_variant``
    # resolves ``_variant_path`` -> ``f"{slugify(slug)}.json"``, so a divergent manifest
    # would be selectable and unloadable at the same time. Compare against
    # ``slugify(path.stem)``, never the raw stem: ``slugify("De_Ch") == "de-ch"``, a pair
    # ``load_variant`` already handles correctly today. Comparing two canonical values also
    # closes the reverse direction for free — a filename that is not itself in canonical
    # slug form can no longer be loaded even when its declared slug equals its raw stem.
    # That second property is deliberate, not redundant. Keep this check BEFORE
    # ``validate_dictionary_file`` below: that call raises ``FileNotFoundError``, which
    # ``game/views.py`` reports as readiness "unavailable", whereas an unloadable variant
    # must be omitted from the public catalog entirely.
    stem_slug = slugify(path.stem)
    if slug != stem_slug:
        raise VariantManifestError(
            "slug_stem_mismatch",
            f"manifest {path.name} declares slug {slug!r} but its filename resolves to "
            f"{stem_slug!r}; load_variant() resolves the filename, so only {stem_slug!r} "
            "could ever be loaded",
        )
```

Placement evidence: `validate_dictionary_file(...)` is now at `:353` and `_parse_alphabet_order(...)` at `:363`, both strictly after the new check, so the ordering trap in section 5a cannot fire.

## Test table

| Test id | Class | Pre-fix failure text (verbatim) |
|---|---|---|
| T12 `tests/test_czech_polish_variants.py::test_t12_stem_slug_divergent_manifest_is_omitted` | B | `E       AssertionError: assert 'german' not in ['german', 'valid']` at `tests/test_czech_polish_variants.py:317`; summary `1 failed in 0.78s`. Captured with `variant_store.py` still at the exact baseline content (T12 was written and run **before** the 5a edit, so no file backout or Git restore was needed). |
| G26b `tests/test_variant_invariants.py::test_g26b_a_stem_slug_divergence_is_rejected_at_ingest` | B (by construction) | `E       Failed: DID NOT RAISE <class 'gamecore.variant_store.VariantManifestError'>` at `tests/test_variant_invariants.py:403`; summary `1 failed, 4 passed, 66 deselected in 0.14s` (the 4 passing were the G26a parameterizations). |
| G26a `test_g26a_manifest_stem_equals_declared_slug` | A | unchanged, byte-identical, 4/4 shipped manifests pass before and after. |

Post-fix focused runs: `tests/test_variant_invariants.py` **71 passed** (unchanged count — G26b was inverted, not added), `tests/test_czech_polish_variants.py` **12 passed** (was 11), `tests/test_atomic_tile_tokens.py` **24 passed**, `tests/test_slovak_variant.py` included in a combined **115 passed** run.

Measured error code: the raised code is exactly **`slug_stem_mismatch`**, asserted twice in G26b (`_load_variant_from_path` route and `load_variant("de")` route). No deviation from the specified code.

## Shipped manifests under the new rule

**None of the four shipped manifests would have been rejected.** Measured in this checkout with the venv interpreter:

```text
czech.json:   stem='czech'   declared='czech'   computed='czech'   slugify(stem)='czech'   match=True
english.json: stem='english' declared='english' computed='english' slugify(stem)='english' match=True
polish.json:  stem='polish'  declared='polish'  computed='polish'  slugify(stem)='polish'  match=True
slovak.json:  stem='slovak'  declared='slovak'  computed='slovak'  slugify(stem)='slovak'  match=True
```

No manifest under `backend/assets/variants/` was edited or read-modified; `git diff 61720aa..HEAD -- backend/assets` is empty. I also re-measured every synthetic slug used by the existing suites (`synthetic`, `no-alpha`, `nfd`, `ghost`, `bad`, `escape`, `alpha`, `beta`, `g15`–`g25`): all are canonical and equal to their filename stems, which is why no existing negative test changed class.

Section 2 divergence facts re-measured before implementing (all reproduced exactly as stated): `list_installed_variants() -> ['german']`, `len(list) == len(*.json) -> True`, `load_variant('german') -> FileNotFoundError: Variant 'german' not found`, `load_variant('de').slug -> 'german'`, and `slugify`: `'de'->'de'`, `'De_Ch'->'de-ch'`, `'Ger man'->'ger-man'`, `'árvíz'->'arviz'`.

## Public-payload evidence

Exact JSON body T12 observed for the two-manifest directory (`de.json` declaring `german` with a real lexicon, plus a valid `valid.json`), HTTP **200**:

```json
[{"slug": "valid", "display_name": "Valid", "language_code": "xx", "readiness": "playable"}]
```

- the divergent variant appears under **neither** slug: `assert "german" not in slugs`, `assert "de" not in slugs`, `assert slugs == ["valid"]`;
- the valid variant survives and is still `playable` (asserted by whole-row equality);
- the four-key set survived: `set(row.keys()) == {"slug", "display_name", "language_code", "readiness"}` for every surviving row — independently confirmed as `['display_name', 'language_code', 'readiness', 'slug']`;
- no leak: `"german"` (case-insensitive), `"de.json"`, `str(tmp_path)`, `".txt"`, `"mismatch"`, `"slug_stem_mismatch"`, `"VariantManifestError"` are all absent from the serialized body.

Branch analysis confirmed rather than assumed: `VariantManifestError` is a `ValueError`, so it reaches `game/views.py:126-128` (`except Exception` → `variant_list_omitted` → `continue`), **not** the `FileNotFoundError` branch at `:119-125`. Direct instrumentation of `list_variant_summaries()` over the same directory emitted exactly one log record, `variant_list_omitted`, with no path, filename, or exception text. The omission outcome — not `unavailable` — is therefore measured on both the HTTP path and the function path.

## Eight standing gates

```text
1  mypy config game gamecore accounts catalog   Success: no issues found in 83 source files
2  ruff check .                                 All checks passed!
3  manage.py check                              System check identified no issues (0 silenced).
4  pytest                                       462 passed, 4 skipped in 214.29s (0:03:34)
   pytest --collect-only                        466 tests collected in 6.56s
5  npm run typecheck                            exit 0
6  npx vitest run                               Test Files  31 passed | 1 skipped (32)
                                                Tests  450 passed | 3 skipped (453)
7  npm run lint                                 exit 0
8  npm run build                                exit 0
```

Delta versus the section 7 baseline: pytest `461 -> 462` passed (+1 = T12), skips unchanged at 4, collection `465 -> 466`. Every frontend number is identical to baseline, which is the independent evidence that I stayed inside the allowlist. `npm run build` reported **eleven dynamic (`ƒ`) routes and zero static routes**, matching baseline.

Trap discipline: (1) `pytest` was run as plain `-m pytest` with no second `-q`, and the summary line is quoted verbatim above; (2) mypy ran the full documented five-package scope, 83 source files; (3) `:3000` was verified free immediately before `npm run build`, nothing was killed; (4) two separate claims — **the production build passed** (`next build --webpack`, exit 0) **and the code type-checks** (`npm run typecheck` = `tsc --noEmit --incremental false`, exit 0).

RF-16 route binding used exactly as declared: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m …` / `.venv/bin/ruff`, `manage.py check` with **no** `-m`. `backend/.venv/bin/python` present (symlink to `python3.12`). No ambient `python3`, no `poetry run`. Evidence class reproduced-dynamic; authority bounded to this task.

## Git sequence

```text
git add backend/gamecore/variant_store.py backend/tests/test_variant_invariants.py backend/tests/test_czech_polish_variants.py
git status --porcelain=v1   M  backend/gamecore/variant_store.py
                            M  backend/tests/test_czech_polish_variants.py
                            M  backend/tests/test_variant_invariants.py      (exactly three, nothing else)
git diff --cached --stat    3 files changed, 120 insertions(+), 20 deletions(-)
git commit                  [main 5f63e0d] fix(variants): reject a manifest whose declared slug disagrees with its filename
pre-push  git ls-remote origin refs/heads/main   61720aa701132085809a9012ee29e446c622bd4f   == exact baseline, gate satisfied
git push origin main        To https://github.com/cisarik/libretiles
                               61720aa..5f63e0d  main -> main            (non-force fast-forward, exit 0)
readback  git ls-remote origin refs/heads/main   5f63e0da2a4c0aba0edcd905e488c0f7a32163e9
          git rev-parse HEAD                     5f63e0da2a4c0aba0edcd905e488c0f7a32163e9   EQUAL
```

No force, amend, rebase, reset, clean, stash, branch, or tag was used at any point.

## Deviations, risks, missing evidence

- **Deviation from section 6's suggested mechanics, not its requirement.** Section 6 described capturing T12's pre-fix failure by checking `variant_store.py` back out to the parent commit. I obtained the same evidence more safely by writing T12 and the inverted G26b *first* and running them against the untouched baseline loader, so no Git restore/checkout of a production file was ever needed. The captured failure text is against baseline code by construction.
- **Local contradiction I did not resolve by mutation** (see the MEASURED list below): section 5c orders G26a to remain "exactly as it is", while the same section's ⚠ orders stale G9-blindness comments in that module to be corrected. G26a's docstring contains exactly such a now-false sentence. I chose the specific, stricter instruction: G26a is byte-identical, and I report the stale sentence instead of editing it.
- Risk of the shipped behaviour change: a third-party or hand-written manifest whose filename and declared slug disagree (or whose filename is not canonical slug form) now disappears from `GET /api/game/variants/` instead of appearing as `unavailable`. That is the intended fail-closed outcome; it is fully reversible by reverting one commit and touches no schema, asset, migration, or persisted state.
- Missing evidence, stated plainly: this is **non-independent** implementation evidence (I wrote both the production change and its tests). No live browser or deployed-environment check was performed; the frontend variant picker was verified only through the unchanged frontend gates, not by rendering the catalog against a divergent manifest.

Resolved Execution Issues / Near-Misses:
1. **Temp-path near-miss.** My first section 2 re-measurement created a scratch directory via `tempfile.mkdtemp()`, which landed in `/tmp/mle-v2a-measure-…` rather than the authorized `/tmp/opencode/mle-v2a/`. It was removed inside the same process (`tmp.exists() -> False` printed) and contained only a synthetic manifest, no repository or sensitive data. All later scratch work used `/tmp/opencode/mle-v2a/` exclusively. Residual risk: none; the path no longer exists.
2. **T12 placement, caught before any gate.** I first inserted T12 above T11, breaking the `T*` reading order. I reverted the edit (verified by an empty `git diff --stat`, i.e. the file returned byte-identical to baseline) and re-appended T12 after T11. Residual risk: none.
3. **Cleanup outcome.** `/tmp/opencode/mle-v2a/` (holding `prefix_t12.txt`, `prefix_g26b.txt`, `payload_readback.py` and a removed `payload-dir/`) was deleted after the evidence was transcribed into this report; `ls` confirms the path is gone. `/tmp/opencode` itself, which I did not create, was left in place.

Pre-Existing Failure Classification: none. Every baseline gate value in section 7 reproduced or improved exactly as predicted; the 4 pytest skips and 3 vitest skips are pre-existing and unchanged, and no test failed for a reason unrelated to section 5c.

```text
⚠ WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE
```

**MEASURED**

1. `G26a`'s docstring now contains a false sentence, and the prompt's two instructions about it conflict. `backend/tests/test_variant_invariants.py:369-371` still reads "When the two diverge, a variant is selectable and unloadable at the same time, and ``G9``'s count comparison cannot see it. ``G26b`` pins that divergence as measured behaviour." After this commit, all three claims are wrong: the divergence is rejected at ingest, `G9`'s count comparison *does* see it (measured: one manifest file now yields zero variants), and `G26b` pins rejection, not divergence. Section 5c says G26a "must remain exactly as it is"; its own ⚠ says to correct any comment in that module that claims G9 is blind. I honoured the byte-exact instruction and left it. Exact one-line replacement, ready to apply verbatim: `When the two diverge the loader now rejects the manifest with code ``slug_stem_mismatch``, so ``G9``'s count comparison sees the gap; ``G26b`` pins that rejection.`
2. My insertion shifted three `file:line` anchors that other comments cite. Inside the allowlist I corrected the two that my change invalidated (`variant_store.py:433-440 -> :453-460` in the module docstring, `:333/:343 -> :353/:363` in `_synthetic`'s docstring). I grepped the whole repository for `variant_store.py:` references and found **none outside** those two files, so no unfixable stale anchor was created. The `:324` and `:178-179` anchors are still exact because the check was inserted *after* line 324.
3. `game/views.py` now has a second, structurally different reason to omit a row, and its `except Exception` handler logs a single fixed string with no discriminator. Measured: the divergent manifest and a `{not json` file produce the *identical* operator log line `variant_list_omitted`. Diagnosability, not correctness — an operator cannot tell a slug/stem defect from a JSON syntax error without reading `libretiles.variants`, whose `variant_load_failed path=%s error=%s` line does carry the detail.
4. `list_installed_variants` is called three times per request path in the two serializers and one service, each time re-globbing and re-parsing every manifest. The new check adds one `slugify` call per manifest per call — negligible, but it confirms why section 5a's "do it at ingest" instruction matters: making `load_variant` search declared slugs would have multiplied that parse cost.

**LEAD** (unmeasured, offered as leads only)

1. `_summary_from_payload` at `game/views.py:73-90` still derives its public slug from the declared `slug` with a `slugify(stem)` fallback, so the surviving `FileNotFoundError` path can still advertise a *declared* slug for a manifest whose stem differs — a `de.json` declaring `german` **and** naming an absent lexicon would be rejected by the new ingest check first, so I believe this is unreachable today, but I did not construct a case that reaches `_summary_from_payload` with a divergent pair. Worth one bounded probe before anyone relies on the omission property holding for every ordering of defects.
2. `_variants_dir()` calls `path.mkdir(parents=True, exist_ok=True)` at `variant_store.py:174` — a read-shaped helper with a filesystem side effect on every list. Unrelated to this slice and untested by me.
3. The frontend variant picker consumes this payload; a variant silently vanishing (rather than showing as `unavailable`) may leave a stale persisted `variant_slug` in the Zustand store with no repair path analogous to the model-catalog repair. I did not read the frontend selection code, so this is speculation.

Smallest next step: apply the one-line G26a docstring correction quoted in MEASURED item 1 under an explicit micro-authority, or explicitly accept the stale sentence and record it in the ledger — nothing else in this slice is open.

Report justification: `new-mutation`
Logical-whole closure: not-closed

Authority expiry: this terminal report expires my authority for this exchange. I have stopped all autonomous work; the pushed commit `5f63e0d` is a candidate carrying non-independent implementation evidence only, and it is not accepted, published, or closed by anything in this report. Any continuation requires a new complete prompt.

Context pressure: low-to-moderate — roughly a third of the window consumed, dominated by the four mandatory source and test files; ample headroom remained throughout and no compaction occurred.

