### Report for ORCHESTRATOR_CHAT

**Coordinates:** logical whole multilingual-expansion, Worker session ordinal 01, Worker exchange ordinal 02

**Status:** PASS

**Phase-qualified result:** `implementation-PASS`

**Result artifact or commit:** `61720aa701132085809a9012ee29e446c622bd4f`

**Result evidence:** three changes landed in the single allowlisted file — `G26a` (4 cases, stem/slug agreement over every installed manifest), `G26b` (1 characterization case pinning the divergence and G9's blindness to it), `G27` (4 cases, no manifest may declare a derived property) — plus the strengthened `G13` `fetched_at` assertion. Module rose from 62 to 71 cases, all passing; full suite rose from 456 to 465 collected, exactly +9; all eight standing gates green; every class B failure text captured against genuinely broken input; one non-force fast-forward push with public readback equal to local `HEAD`.

**Start and end commit**
- start: `3878847d367490217c4b1b3d3a2af763aaad1a32`
- end: `61720aa701132085809a9012ee29e446c622bd4f`

**Section 2 re-gate, verbatim**

| Check | Measured | Required | Verdict |
|---|---|---|---|
| `git rev-parse HEAD` | `3878847d367490217c4b1b3d3a2af763aaad1a32` | same | match |
| `git rev-parse HEAD:.ap` | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | same | match |
| `git -C .ap rev-parse HEAD` | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | same | match (detached HEAD, correct) |
| `git status -sb` | `## main...origin/main` | same | match |
| `git status --porcelain=v1` | *(empty)* | EMPTY | match |
| `git ls-remote origin refs/heads/main` | `3878847d367490217c4b1b3d3a2af763aaad1a32	refs/heads/main` | same | match |
| `ss -tlnp \| grep -E ':(3000\|8000)'` | no match (grep exit 1) | no listener | match |

Nothing differed, so no recovery class was engaged, and nothing conflicts with retained context. `backend/.venv/bin/python` present (symlink → `python3.12`). I treated retained exchange-01 facts as convenience only: the slug/stem divergence, the derived-property set, and the `fetched_at` behaviour were all re-measured in this exchange before any assertion was written.

End-of-task re-confirmation: `git status --porcelain=v1` → *(empty)*; `git status -sb` → `## main...origin/main`; both `.ap` values still `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; `git diff --name-only 3878847 HEAD` → `backend/tests/test_variant_invariants.py` and nothing else.

**Changed files and purpose**

| Path | Change | Purpose |
|---|---|---|
| `backend/tests/test_variant_invariants.py` | modified, +114 / −1 | added `G26a`, `G26b`, `G27`; strengthened `G13`'s `fetched_at` check from bare `fromisoformat` to a round-tripping calendar date with a 10-character floor |

One path. No production source, no other test file, no manifest, no asset, no lockfile, no `pyproject.toml`, no frontend file. No production fix to the slug/stem divergence, per the 3a warning. `git status --porcelain=v1 -- backend/assets/` was empty throughout, confirming no real manifest was touched even temporarily.

**Section 1 re-measurement, before writing G26b**

All four claimed facts reproduce exactly on the current checkout:

```text
list_installed_variants() slugs : ['german']
len(list) == len(*.json)        : True (1 vs 1)   → G9 passes and is blind to it
load_variant('german')          -> FileNotFoundError: Variant 'german' not found
load_variant('de')              -> OK  .slug = 'german'
stem/slug pairs for that dir    : {'de': 'german'}
```

The divergence is real and reachable, so no stopping condition fired and I did not have to force a test to match a claim.

**New-test table**

| ID | Test name | Class | Cases | Captured failure text against broken input |
|---|---|---|---|---|
| G26a | `test_g26a_manifest_stem_equals_declared_slug` | A | 4 (czech, english, polish, slovak) | Passes immediately — the four shipped stems already equal their slugs. This is invariant pinning, not a caught regression. Teeth proven separately against a divergent manifest: `AssertionError: manifest de.json declares slug 'german' but its filename stem is 'de'; list_installed_variants() would advertise 'german' as selectable while load_variant('german') raises FileNotFoundError` / `assert 'german' == 'de'` |
| G26b | `test_g26b_a_stem_slug_divergence_is_reachable_today` | B | single | With the manifest renamed to `german.json` (stem == slug) the literal body fails at the pair-mapping assertion: `AssertionError: assert {'german': 'german'} == {'de': 'german'}`. With the bookkeeping expectation adjusted so the substantive assertion is the one under test: `AssertionError: no stem/slug divergence found; G26b would pass vacuously` / `assert False`. And the load asymmetry disappears: `Failed: DID NOT RAISE <class 'FileNotFoundError'>`. `de.json` was restored (the rename existed only in a throwaway module; the committed test writes `de.json`). |
| G27 | `test_g27_no_manifest_declares_a_derived_property` | B | 4 (czech, english, polish, slovak) | With `"total_tiles": 100` added to a synthetic `tmp_path` manifest: `AssertionError: manifest declared.json declares derived key(s) ['total_tiles']; each is a computed property of VariantDefinition, so a declared value is silently ignored by the loader while looking authoritative to a reader` / `assert not ['total_tiles']`. The synthetic manifest was confined to `tmp_path` and the key was never added to a real manifest. |
| G13 | `test_g13_metadata_shape_tolerates_the_declared_asymmetry` (strengthened) | B | 4 (unchanged case count) | See the correction below; captured texts quoted there. |

New cases: 4 + 1 + 4 = **9**. G26b additionally asserts `len(listed) == len(files)` to document, in the test itself, that G9's count comparison cannot see this defect class.

Supporting non-failure measurement for G27: a manifest declaring `"total_tiles": 7` loads with `variant.total_tiles == 100`, confirming the loader silently ignores the key — which is the whole reason G27 is a raw-JSON assertion rather than a loader assertion.

**G27's forbidden key set, derived from measurement not assumption**

I confirmed on `VariantDefinition` that `total_tiles`, `distribution`, `tile_points`, and `playable_letters` are all genuine `property` objects with no declared counterpart, so all four are in `_FORBIDDEN_DERIVED_KEYS`. I confirmed none of the four shipped manifests declares any of them. `dictionary_file` and `two_tile_words_file` are deliberately excluded: they are legitimate declared inputs whose derived twins are `dictionary_path` and `two_tile_words_path`. I invented no forbidden key without a derived twin.

**Correction to your section 3c premise, and to my own exchange-01 finding 17.5**

Both are wrong on this interpreter, and I am reporting the measurement rather than the claim. On Python 3.12.12:

```text
datetime.fromisoformat("2026")      -> ValueError: Invalid isoformat string: '2026'
datetime.fromisoformat("2026-09")   -> ValueError: Invalid isoformat string: '2026-09'
```

A bare year does **not** pass the old check — it raises. My exchange-01 field 17.5 asserted it succeeds; that was reasoning from memory, not a measurement, and it was incorrect. Your section 3c inherited it.

The hole is nonetheless real, and larger than a bare year. What the old bare-`fromisoformat` check genuinely admitted, measured:

```text
'20260901'    (ISO basic format)  old=PASS   new=FAIL (len 8 < 10)
'2026W364'    (basic week date)   old=PASS   new=FAIL (len 8 < 10)
'2026-W36-4'  (ISO week date)     old=PASS   new=FAIL (raw[:10]='2026-W36-4' != '2026-09-03')
'2026-09-01'                      old=PASS   new=PASS
'2026-09-01T00:00:00'             old=PASS   new=PASS
'2026-09-01T00:00:00+02:00'       old=PASS   new=PASS
```

So the strengthening has real, demonstrated teeth — just against different inputs than either of us predicted. `2026-W36-4` is the sharpest case: ten characters, so it defeats the length floor and is caught only by the calendar round-trip. Captured class B texts:

- literal section 4 input `fetched_at="2026"`, **old** check: `ValueError: Invalid isoformat string: '2026'` — it fails too, so "the old one passed" is not what happens.
- same input, **new** check: `AssertionError: y: fetched_at '2026' is too short to carry a YYYY-MM-DD calendar date` / `assert 4 >= 10`.
- measured input where old passes and new fails, basic format: `AssertionError: b: fetched_at '20260901' is too short to carry a YYYY-MM-DD calendar date` / `assert 8 >= 10`.
- measured input where old passes and new fails on round-trip, week date: `AssertionError: w: fetched_at '2026-W36-4' does not begin with the calendar date it parses to (2026-09-03)` / `assert '2026-W36-4' == '2026-09-03'`.

The implementation follows 3c exactly: `len(raw) >= 10`, parse, then require `raw[:10]` to equal the parsed `YYYY-MM-DD`. `None` stays acceptable and no timezone is required; the timezone-bearing form still passes, so the four naive shipped values are safe.

**Case count before and after**

| Scope | Before | After | Delta |
|---|---|---|---|
| `tests/test_variant_invariants.py` | 62 | **71** | +9 |
| full suite collected | 456 | **465** | +9 |

All 62 pre-existing cases still pass; none was removed, weakened, or renamed.

**The eight standing gates**

| # | Gate | Output | Baseline at `3878847` | Verdict |
|---|---|---|---|---|
| 1 | `mypy config game gamecore accounts catalog` | `Success: no issues found in 83 source files` (exit 0) | identical | unchanged |
| 2 | `ruff check .` | `All checks passed!` (exit 0) | identical | unchanged |
| 3 | `manage.py check` | `System check identified no issues (0 silenced).` (exit 0) | identical | unchanged |
| 4 | `pytest` | **`461 passed, 4 skipped in 217.91s (0:03:37)`** | `456 tests collected` → 465 collected now | +9 collected, +9 passed, skips unchanged at 4 |
| 5 | `npm run typecheck` | exit 0 (`tsc --noEmit --incremental false`) | exit 0 | unchanged |
| 6 | `npx vitest run` | `Test Files  31 passed \| 1 skipped (32)` / `Tests  450 passed \| 3 skipped (453)` (exit 0) | identical | unchanged |
| 7 | `npm run lint` | exit 0 | exit 0 | unchanged |
| 8 | `npm run build` | exit 0 | exit 0 | unchanged |

Trap compliance: the pytest summary is quoted verbatim from a plain `-m pytest` run with no second `-q`; mypy ran the full documented five-package scope (83 files), never narrowed; `ss -tlnp | grep -E ':(3000|8000)'` returned no listener immediately before `npm run build` and again after, and nothing was ever killed.

Both frontend claims, stated separately as trap 4 requires:
- **The build passed.** `npm run build` exited 0, with the route table showing **11 dynamic routes (`ƒ`) and ZERO static routes**, plus `ƒ Proxy (Middleware)` — byte-identical in shape to the baseline.
- **The code type-checks.** This is a separate claim, established by gate 5 running `tsc --noEmit --incremental false`, which disables cache reuse and therefore cannot inherit a stale `incremental: true` result from `next build`.

Full suite wall clock: `217.91s` after, against `215.19s` measured at the previous baseline — inside run-to-run noise. The new module in isolation still runs `71 passed in 19.92s`, essentially all of it cold lexicon loading; its in-suite contribution remains negligible because `fastdict._INDEX_CACHE` is already warm.

**Git**

- staged: `backend/tests/test_variant_invariants.py` only. `git status --porcelain=v1` after staging → `M  backend/tests/test_variant_invariants.py`, exactly one modified path. `git diff --cached --stat` → `1 file changed, 114 insertions(+), 1 deletion(-)`. Staged explicitly; no `git add .`, no `git add -A`.
- commit: `61720aa701132085809a9012ee29e446c622bd4f`, subject `test(variants): pin manifest stem/slug agreement and reject a declared total_tiles`.
- pre-push equality gate: `git ls-remote origin refs/heads/main` → `3878847d367490217c4b1b3d3a2af763aaad1a32	refs/heads/main`, equal to the exact baseline, so the push was permitted.
- push: `3878847..61720aa  main -> main`, exit 0. One non-force fast-forward push. No force, amend, rebase, reset, clean, stash, branch, or tag at any point in this exchange.
- public readback: `git ls-remote origin refs/heads/main` → `61720aa701132085809a9012ee29e446c622bd4f`; `git rev-parse HEAD` → `61720aa701132085809a9012ee29e446c622bd4f`. **Equal.**

**Deviations, risks, missing evidence**

Deviations: the section 5 RF-16 route was used exactly as declared, including the corrected `manage.py check` without `-m`. No ambient `python3` and no `poetry run` was used. No other deviation.

Judgement calls recorded for visibility:
1. **G26a is parameterized over manifest paths, not over loaded `VariantDefinition` objects.** Section 3a asks for both "parameterized over every installed variant" and "build the mapping `{path.stem: loaded.slug}` and assert every pair is equal". Parameterizing over paths satisfies both: each case is one pair of the mapping, ids are the stems, and every pair is asserted across the case set. Loading inside the test rather than at module level is deliberate — a malformed manifest then fails only its own G26a case instead of raising at collection and taking G9 down with it.
2. **`display_label` is a genuine derived property but is not in `_FORBIDDEN_DERIVED_KEYS`.** Section 3b named exactly `distribution`, `tile_points`, and `playable_letters` to check; `display_label` is outside that named set, so I did not silently expand the assertion. It is reported below instead.
3. **`load_variant` was added to the import block** for G26b's characterization assertions. No other import changed.

Risks: none material. One additive commit to one test file; rollback is `git revert` of `61720aa`. No production behaviour, schema, asset, dependency, credential, or external service was touched, and no network request was made.

Missing evidence: the frontend gates 5–8 were measured only after the change, as in exchange 01. `git diff --name-only 3878847 HEAD` returning a single backend test path is the evidence that the frontend tree is byte-identical, so a before-measurement would add nothing.

**Resolved Execution Issues / Near-Misses**

1. *Issue:* section 4's G13 instruction rests on a false premise — `fetched_at="2026"` does not pass the old check, so "confirm the strengthened assertion now fails where the old one passed" cannot be satisfied by that input. *Cause:* my own unmeasured exchange-01 claim, which your prompt inherited in good faith. *Resolution:* I ran the literal instruction and captured both results honestly, then searched for and captured measured inputs that genuinely separate the two checks (`20260901`, `2026W364`, `2026-W36-4`). *Residual risk:* none to the code; the residual is that the recorded rationale for the strengthening must be the measured one, not the bare-year one.
2. *Issue:* the literal G26b body, run with the manifest renamed to `german.json`, fails first at the pair-mapping bookkeeping assertion rather than at the substantive divergence assertion, which would have been a weak teeth demonstration. *Cause:* assertion ordering inside the test. *Resolution:* captured both the literal failure and a second run with the bookkeeping expectation adjusted so the substantive `any(slug != stem ...)` assertion is the one that fires, plus the `DID NOT RAISE <class 'FileNotFoundError'>` capture. *Residual risk:* none; the committed test's assertion order is fine because in the committed direction every assertion holds.
3. *Issue:* G27's Class B capture required a manifest declaring `total_tiles`, and the temptation is to edit a real manifest. *Cause:* convenience. *Resolution:* the synthetic manifest was written only into `tmp_path` inside a throwaway module; `git status --porcelain=v1 -- backend/assets/` was verified empty before and after. *Residual risk:* none.

Temporary state: `/tmp/opencode/mle-v1b/` was created and removed; absence verified by `ls`. `pytest`'s own `/tmp/pytest-of-agile/` roots remain, rotated by pytest itself as for any suite run.

**Pre-Existing Failure Classification:** none. All eight gates were green at `3878847` and are green at `61720aa`.

**What you can still see that this prompt did not anticipate**

1. **The loader, not only the harness, should change — and the cheapest correct fix is not the obvious one.** You said this is the decision you take next, so here is the evidence shape. The divergence has two halves and they are not symmetric:
   - `list_installed_variants` (`:433-440`) advertises the *declared* `slug`;
   - `load_variant` (`:407-411`) resolves a *filename* via `_variant_path` → `f"{slugify(slug)}.json"` (`:178-179`).

   Making `load_variant` search declared slugs would mean reading and parsing every manifest on every call — `list_installed_variants` already does exactly that, so the cost is a full directory parse per load, where today it is one `stat` plus one parse. The cheaper and, I think, more correct fix is to close the divergence at *ingest*: have `_load_variant_from_path` reject a manifest whose declared `slug` does not equal `slugify(path.stem)`, raising a new `VariantManifestError` code such as `slug_stem_mismatch`. That makes a divergent manifest unloadable rather than half-loadable, so `list_installed_variants` skips it (logged, per `:438-439`), no serializer can ever advertise it, and `load_variant` needs no change at all. It also composes with the harness already in place: G9 would then catch the skip and G26a would catch the file, giving two independent detections instead of one.
   - Cost if you take it: `G26b` is a characterization test of behaviour that would then no longer exist, so it must be rewritten in the same slice — probably inverted into "a stem/slug mismatch is rejected with code `slug_stem_mismatch`". Flagging that now so it is priced in rather than discovered.
   - One caveat worth checking before you commit to it: `_load_variant_from_path` is called from `game/views.py:118` inside `list_variant_summaries`, which currently distinguishes `FileNotFoundError` (→ readiness `unavailable`) from every other exception (→ omitted entirely). A new `VariantManifestError` would fall into the omit branch, so a divergent manifest would vanish from `GET /api/game/variants/` rather than appear as `unavailable`. That is probably the behaviour you want, but it is a public-response change and not merely an internal one.

2. **`display_label` is a fifth derived property with no declared twin, and it is outside G27's coverage.** It is a real `property` (`variant_store.py:79-83`) composed from `language` and `variant_name`. Section 3b named only three keys to check, so I stayed bounded, but a manifest declaring `"display_label": "German (Wrong)"` would today be silently ignored while reading as authoritative — the exact hazard G27 exists to prevent. Adding it to `_FORBIDDEN_DERIVED_KEYS` is a one-token change.

3. **`slugify` makes the stem/slug divergence *reachable in both directions*, which G26a does not fully cover.** `_variant_path` applies `slugify(slug)`, so `load_variant("Ger man")` and `load_variant("german")` resolve to the same file. G26a asserts `loaded.slug == path.stem`, and since G13 already requires `slug == slugify(slug)`, the pair is tight for the declared slug. But a manifest *filename* that is not itself in canonical slug form — say `De_Ch.json` — would produce `path.stem == "De_Ch"` while `slugify("De_Ch") == "de-ch"`, so even a manifest whose declared slug equals its stem could be unloadable. G26a would catch that only if the declared slug also failed G13. Asserting `path.stem == slugify(path.stem)` would close it in one line. I did not add it because section 3 did not name it.

4. **`variant_name` is accepted by the loader and declared by no shipped manifest.** `_load_variant_from_path:318-323` reads `variant_name` (or `variant`) and `display_label` folds it in as `f"{language} – {variant_name}"`. None of the four manifests uses it, so the entire `variant_name` code path and its em-dash display form are unexercised by any test in the repository. The first language that uses it will be the first to test it. Not in scope here; worth a G-number when a variant actually declares one.

5. **Your section 1 credit is accurate and I want to be precise about what it credits.** Finding 17.2 (the divergence) was a measurement, and it held under independent re-measurement by you and again by me. Finding 17.5 (`fetched_at`) was *not* a measurement, and it did not hold. The two arrived in the same report field with the same confidence tone, which they did not deserve equally. I have separated them above; treat unmeasured field-17 items as leads rather than findings.

**One smallest next step**

Take the loader decision as described in item 1: add a `slug_stem_mismatch` `VariantManifestError` in `_load_variant_from_path`, and in the same slice invert `G26b` from a characterization test into a rejection test and add the `path.stem == slugify(path.stem)` assertion from item 3. That is one bounded production change with its harness consequence priced in, and it converts the last remaining "selectable but unloadable" state into an ingest-time failure.

**Report justification:** `new-mutation`

**Logical-whole closure:** not-closed

**Authority expiry:** my authority expires with this terminal report. This `PASS` is non-independent implementation evidence produced by the same session that wrote the tests, and it closes nothing; independent acceptance, if required, needs a fresh Worker that did not materially implement this candidate. I emit no logical-whole closure signal and have stopped autonomous work pending a new complete prompt.

**Context pressure:** Moderate to high, but not limiting. This exchange added a second full backend suite, a second full frontend gate set, and the pre-write re-measurements on top of exchange 01's context; no compaction occurred, and I re-verified repository state directly rather than from memory at every gate.

