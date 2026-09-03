### Report for ORCHESTRATOR_CHAT

**1. Coordinates**
Logical whole `multilingual-expansion`, Worker session ordinal `01`, Worker exchange ordinal `01`.

**2. Status:** PASS

**3. Phase-qualified result:** `implementation-PASS`

**4. Result artifact or commit:** `3878847d367490217c4b1b3d3a2af763aaad1a32`

**5. Result evidence:** one new test module, `backend/tests/test_variant_invariants.py` (428 lines, 62 collected cases, all passing); all eight standing gates green with the pytest count rising by exactly 62 and every other gate numerically unchanged; eleven predicted `VariantManifestError` codes measured and all matched; class B/C failure text captured against deliberately broken input; one non-force fast-forward push with public readback equal to local `HEAD`.

**6. Start and end commit**
- start: `47ed8bff5a6548d2d954c68d9ea13f05a2222e4a`
- end: `3878847d367490217c4b1b3d3a2af763aaad1a32`

**7. Repository gate (section 3), verbatim measured values**

| Check | Measured | Expected | Verdict |
|---|---|---|---|
| `git rev-parse HEAD` | `47ed8bff5a6548d2d954c68d9ea13f05a2222e4a` | same | match |
| `git rev-parse HEAD:.ap` | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | same | match |
| `git -C .ap rev-parse HEAD` | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | same | match (detached HEAD, correct topology) |
| `git status -sb` | `## main...origin/main` | same | match |
| `git status --porcelain=v1` | *(empty)* | EMPTY | match |
| `git ls-remote origin refs/heads/main` | `47ed8bff5a6548d2d954c68d9ea13f05a2222e4a	refs/heads/main` | same | match |
| `ss -tlnp \| grep -E ':(3000\|8000)'` | no match (grep exit 1) | no listener | match |

The port check was confirmed against the full `ss -tlnp` table, not just the grep exit code: no listener on 3000 or 8000 at task start, and re-verified after the frontend gates and after the push. No recovery class was needed — nothing differed. `.ap` was never attached or updated.

End-of-task re-confirmation: `git status --porcelain=v1` → *(empty)*; `git status -sb` → `## main...origin/main`; `git rev-parse HEAD:.ap` and `git -C .ap rev-parse HEAD` both still `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.

**8. Changed files and purpose**

| Path | Change | Purpose |
|---|---|---|
| `backend/tests/test_variant_invariants.py` | added (428 lines) | one parameterized harness over `list_installed_variants()` asserting the structural invariants that hold for any language, guarding the parameterization against an empty or silently-shortened list, and proving a malformed synthetic manifest fails with its exact error code |

Exactly one path. No production source, no existing test, no asset, no manifest, no lockfile, no frontend file was touched.

**9. Test inventory table**

| ID | Test name | Class | Cases | Observed failure text against broken input |
|---|---|---|---|---|
| G1 | `test_g1_installed_list_is_non_empty_and_contains_the_shipped_slugs` | A | single | n/a (invariant pinning) |
| G9 | `test_g9_installed_count_matches_manifest_file_count` | C | single | `AssertionError: list_installed_variants() logs and SKIPS a manifest it cannot load; 3 manifest files produced 2 variants (loaded=['alpha', 'beta'], files=['alpha.json', 'beta.json', 'broken.json'])` / `assert 2 == 3` — plus the captured loader log `ERROR libretiles.variants:variant_store.py:439 variant_load_failed path=…/broken.json error=Expecting property name enclosed in double quotes: line 1 column 2 (char 1)` |
| G9c | `test_g9c_installed_count_detects_a_manifest_the_loader_skips` | C | single | this test *is* the committed demonstration; it asserts `len(loaded) != len(files)` in a `tmp_path` dir with one malformed manifest, monkeypatching `gamecore.variant_store._variants_dir` (the LOADER list, distinct from `game.views._variant_json_dir` at `test_czech_polish_variants.py:201`) |
| G2 | `test_g2_declared_tokens_are_canonical` | A | 4 (czech, english, polish, slovak) | n/a |
| G3 | `test_g3_tile_tokens_are_pairwise_distinct` | A | 4 | n/a |
| G4 | `test_g4_exactly_one_blank_record` | A | 4 | n/a |
| G5 | `test_g5_derived_arithmetic_is_consistent` | A | 4 | n/a |
| G6 | `test_g6_alphabet_order_is_well_formed` | A | 4 | n/a |
| G7 | `test_g7_every_tile_token_appears_once_in_alphabet_order` | A | 4 | n/a |
| G8 | `test_g8_playable_letters_is_the_tile_set_in_alphabet_order` | A | 4 | n/a |
| G10 | `test_g10_declared_asset_references_resolve` | A | 4 | n/a |
| G11 | `test_g11_extension_points_are_identity_today` | A | 4 | n/a |
| G12 | `test_g12_starting_draw_order_is_blank_first_then_alphabet` | A | 4 | n/a |
| G13 | `test_g13_metadata_shape_tolerates_the_declared_asymmetry` | A | 4 | n/a |
| G14 | `test_g14_inflected_form_membership_probe` | A | 4 | n/a |
| G15 | `test_g15_duplicate_alphabet_order_token_is_rejected` | B | single | broken input raises `duplicate_alphabet: alphabet_order contains duplicate token 'A' at index 1`; with the duplicate removed the same test yields `Failed: DID NOT RAISE <class 'gamecore.variant_store.VariantManifestError'>` |
| G16 | `test_g16_blank_in_alphabet_order_is_rejected` | B | single | raises `blank_in_alphabet: alphabet_order must not contain the blank token`; asserting a wrong code yields `AssertionError: assert 'blank_in_alphabet' == 'duplicate_alphabet'` |
| G17 | `test_g17_absent_alphabet_order_key_is_rejected` | B | single | `missing_alphabet_order: alphabet_order is required and must be declared, not derived from letters` |
| G18 | `test_g18_tile_token_outside_alphabet_order_is_rejected` | B | single | `tile_not_in_alphabet: every non-blank tile token must appear exactly once in alphabet_order; missing ['B']` |
| G19 | `test_g19_decomposed_tile_token_is_rejected` | B | single | `non_nfc: tile token 'Á' is not NFC; expected 'Á'` |
| G20 | `test_g20_overlong_tile_token_is_rejected` | B | single | `too_long: tile token 'AAAAAAAAAAAAAAAAA' exceeds 16 code points` |
| G21 | `test_g21_reserved_blank_alias_tile_token_is_rejected` | B | single | `blank_alias: tile token 'JOKER' is reserved for a physical blank; use '?'` |
| G22 | `test_g22_duplicate_tile_token_is_rejected` | B | single | `duplicate_token: duplicate tile token 'A'` |
| G23 | `test_g23_whitespace_in_a_tile_token_is_rejected` | B | single | `whitespace: tile token contains whitespace: 'A B'` |
| G24 | `test_g24_dictionary_file_guard_keeps_two_exception_classes_apart` | B | single | `ValueError: dictionary_file must be a basename: '../collins2019.txt'` / `… 'dicts/collins2019.txt'` / `ValueError: dictionary_file has invalid shape: 'no_ext'` / `FileNotFoundError: dictionary file not found: …/assets/dicts/definitely_absent_lexicon.txt` (confirmed NOT a `ValueError`) |
| G25 | `test_g25_manifest_without_tiles_raises_plain_value_error` | B | single | `ValueError: Variant …/no-letters.json contains no tiles`, `type(exc) is ValueError` confirmed `True`; with tiles restored the same test yields `Failed: DID NOT RAISE <class 'ValueError'>` |

Totals: 3 single guards + 12 parameterized × 4 variants (48) + 11 negative singles = **62 cases**, matching the pytest delta exactly.

G9c is my own sub-id: section 8 mandates the Class C demonstration as a real test but assigns it no number, so I numbered it under G9 rather than inventing a new top-level id. The Class B "did not raise" / "wrong code" demonstrations were produced in a throwaway module under `/tmp/opencode/mle-v1/`, which was removed (verified absent); nothing outside the allowlisted path was committed.

**10. Measured error codes for G15–G25**

| ID | Expected (section 6d) | Actually raised | Differed? |
|---|---|---|---|
| G15 | `duplicate_alphabet` | `duplicate_alphabet` | no |
| G16 | `blank_in_alphabet` | `blank_in_alphabet` | no |
| G17 | `missing_alphabet_order` | `missing_alphabet_order` | no |
| G18 | `tile_not_in_alphabet` | `tile_not_in_alphabet` | no |
| G19 | `non_nfc` | `non_nfc` | no |
| G20 | `too_long` | `too_long` | no |
| G21 | `blank_alias` | `blank_alias` | no |
| G22 | `duplicate_token` | `duplicate_token` | no |
| G23 | `whitespace` | `whitespace` | no |
| G24 | `ValueError` ×3, `FileNotFoundError` ×1 | `ValueError` ×3, `FileNotFoundError` ×1 (not a `ValueError`) | no |
| G25 | plain `ValueError` | `ValueError`, `type(exc) is ValueError` → `True` | no |

**Nothing differed.** All eleven codes were measured in a throwaway probe *before* the assertions were written, then re-confirmed by the committed tests passing. Every synthetic manifest sets `dictionary_file` to `"collins2019.txt"`, so the `variant_store.py:333`-before-`:343` ordering trap could not mask an intended code.

**11. The eight standing gates**

| # | Gate | Output | Baseline | Verdict |
|---|---|---|---|---|
| 1 | `mypy config game gamecore accounts catalog` | `Success: no issues found in 83 source files` (exit 0) | identical | unchanged |
| 2 | `ruff check .` | `All checks passed!` (exit 0) | identical | unchanged |
| 3 | `manage.py check` | `System check identified no issues (0 silenced).` (exit 0) | identical | unchanged |
| 4 | `pytest` | **`452 passed, 4 skipped in 213.30s (0:03:33)`** | `390 passed, 4 skipped in 215.19s (0:03:35)` (re-measured by me at the baseline commit, not trusted from the prompt) | +62 passed, skips unchanged |
| 5 | `npm run typecheck` | exit 0 (`tsc --noEmit --incremental false`) | exit 0 | unchanged |
| 6 | `npx vitest run` | `Test Files  31 passed \| 1 skipped (32)` / `Tests  450 passed \| 3 skipped (453)` (exit 0) | identical | unchanged |
| 7 | `npm run lint` | exit 0 | exit 0 | unchanged |
| 8 | `npm run build` | exit 0 | exit 0 | unchanged |

The pytest summary line is quoted verbatim; plain `-m pytest` was used, so no second `-q` suppressed it. mypy ran on the full documented scope `config game gamecore accounts catalog` (83 files), not a narrowed set.

Both frontend claims stated separately, as trap 4 requires:
- **The build passed.** `npm run build` exited 0.
- **The code type-checks.** This is a *separate* claim established by gate 5, which runs `tsc --noEmit --incremental false` — cache reuse disabled, so it cannot inherit a stale `incremental: true` result from `next build`.

`npm run build` route table: **11 routes, all `ƒ (Dynamic)`, ZERO static** — `/`, `/_not-found`, `/api/ai/judge`, `/api/ai/move`, `/api/models`, `/api/prompts`, `/draw/[id]`, `/game/[id]`, `/play`, `/settings`, `/waiting/[id]`, plus `ƒ Proxy (Middleware)`. Matches the stated baseline exactly. Because I touched no frontend file, gates 5–8 were run once (after the change); their unchanged counts are the evidence that the change stayed inside the allowlist.

Baselines for gates 1–4 were re-measured by me at `47ed8bff` before writing the module.

**12. Timing (section 9d)**

- **(a) full suite before / after:** before `215.19s` (shell wall clock 223 s); after `213.30s` (shell wall clock 221 s). Delta **−1.89 s**, i.e. the new module's in-suite cost is inside run-to-run noise and nowhere near the +60 s stop threshold.
- **(b) new module in isolation:** `62 passed in 19.99s` (shell wall clock 28 s).
- **(c) yes, dramatically slower in isolation, and that confirms cache sharing.** Direct cold-load measurement of the four lexicons: czech 6.88 s, polish 6.36 s, slovak 5.45 s, collins 0.22 s = **18.91 s of the isolated 19.99 s**. In-suite the contribution is ~0 because `test_czech_polish_variants.py`, `test_dictionary_validation.py`, and `test_slovak_engine.py` collect earlier in alphabetical file order and warm all four `fastdict._INDEX_CACHE` keys with default keyword arguments — which is exactly why G14 calls `load_prefix_index(variant.dictionary_path)` with defaults only. No fixture change or probe narrowing was needed.

**13. Git**

- staged path list: `backend/tests/test_variant_invariants.py` (staged explicitly; no `git add .`, no `git add -A`). `git status --porcelain=v1` after staging: `A  backend/tests/test_variant_invariants.py` — exactly one entry. `git diff --cached --stat`: `1 file changed, 428 insertions(+)`.
- commit: `3878847d367490217c4b1b3d3a2af763aaad1a32`, subject `test(variants): generic per-variant invariant harness over every installed variant`. `git show --name-status HEAD` → `A	backend/tests/test_variant_invariants.py`, nothing else.
- pre-push equality gate: `git ls-remote origin refs/heads/main` → `47ed8bff5a6548d2d954c68d9ea13f05a2222e4a	refs/heads/main` — equal to the exact baseline, so the push was permitted.
- push result: `47ed8bf..3878847  main -> main`, exit 0. One non-force fast-forward push. No force, amend, rebase, reset, clean, stash, branch, or tag at any point.
- public readback: `git ls-remote origin refs/heads/main` → `3878847d367490217c4b1b3d3a2af763aaad1a32`; `git rev-parse HEAD` → `3878847d367490217c4b1b3d3a2af763aaad1a32`. **Equal.**

**14. Deviations, risks, missing evidence**

Deviations:
1. **RF-16 route used as declared** for every Python tool: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m <tool>` and `.venv/bin/ruff`. `backend/.venv/bin/python` exists (symlink → `python3.12`, resolved 3.12.12). No ambient `python3` and no `poetry run` was used as a parallel route at any point.
2. **The `manage.py check` command in section 9b is literally broken and I corrected it.** As written, `.venv/bin/python -m manage.py check` fails: `Error while finding module specification for 'manage.py' (ModuleNotFoundError: __path__ attribute not found on 'manage' …)`, exit 1. I ran `.venv/bin/python manage.py check` (same interpreter, same env sanitization, dropped only the erroneous `-m`), which produced the prompt's own stated baseline `System check identified no issues (0 silenced).` This is a within-route typo correction, not a route deviation and not a fallback.
3. **I imported the private `_BLANK_ALIASES`** from `gamecore.variant_store`, which is not in section 5's import list. G4's "no tile token other than `?` is a reserved blank alias" cannot be single-owner without it; the alternative was duplicating the reserved set into the test module, creating a second semantic owner. The prompt already establishes the precedent for private names (`_load_variant_from_path` per section 5, `_variants_dir` per section 8 Class C).

Judgement calls inside section 6, recorded for visibility:
- G5 asserts exactly the five listed properties and no more; no per-variant total appears anywhere in the module.
- G7 asserts `tiles <= set(alphabet_order)` and `order.count(token) == 1` and carries an inline comment stating the reverse is *not* an invariant, naming the shipped Slovak and Czech tileless sets.
- No assertion of `len(token) == 1` exists anywhere in the module; G2 asserts `1 <= len(token) <= MAX_TILE_TOKEN_CODEPOINTS` with a comment naming it a resource bound.

Risks: none material. The change is one additive test file; rollback is `git revert` of one commit. No schema, asset, persisted state, dependency, credential, or external service was touched. No network request was made.

Missing evidence: gates 5–8 have no *before* measurement taken by me at `47ed8bff` (see the reasoning in field 11 — the frontend tree is byte-identical before and after, proven by the single-path commit). I relied on the prompt's stated frontend baselines for the comparison while measuring the after values myself.

One clarification about apparent network activity: `npx vitest run` prints `[libretiles-provider-failure] openrouter generate_text null AI_APICallError No endpoints found for stealth/example:free` in a fully passing run. I verified these are locally-constructed `Error` objects in test fixtures (`frontend/src/lib/ai-runtimes.test.ts:398`, `frontend/src/app/api/ai/judge/route.test.ts:199`, `frontend/src/lib/ai-turn-simulation.test.ts:724`), not real provider responses. No outbound request occurred.

**15. Resolved Execution Issues / Near-Misses**

1. *Issue:* section 9b's `manage.py check` invocation is broken. *Cause:* a spurious `-m` before a file path. *Resolution:* ran the corrected form on the same declared interpreter and verified it reproduces the prompt's stated baseline. *Residual risk:* the prompt's stated baseline for this gate must have been produced by a silently-corrected command in a previous session, so any future prompt copying that line verbatim will hit the same defect.
2. *Issue:* the section 6d ordering trap — `validate_dictionary_file` at `variant_store.py:333` runs before `alphabet_order` at `:343`, so a synthetic manifest naming an absent lexicon raises `FileNotFoundError` and the intended `VariantManifestError` never fires. *Cause:* structural, in the loader. *Resolution:* the `_synthetic` builder hardcodes `"dictionary_file": "collins2019.txt"` with an inline comment citing those line numbers, and all eleven codes were measured empirically before any assertion was written. *Residual risk:* a future test author overriding `dictionary_file` in `_synthetic` re-opens the trap; the comment is the only guard.
3. *Issue:* Class B tests could have been written to assert a code that is never raised and still "pass" by catching the wrong exception. *Cause:* `pytest.raises` alone does not pin the code. *Resolution:* I ran deliberately weakened copies and captured `Failed: DID NOT RAISE …` and `AssertionError: assert 'blank_in_alphabet' == 'duplicate_alphabet'`, proving both the raise and the code assertion have teeth. *Residual risk:* none.

Temporary state: `/tmp/opencode/mle-v1/` (and a second short-lived probe dir) were created and both removed; absence verified by `ls`. `pytest`'s own `/tmp/pytest-of-agile/` roots remain, managed and rotated by pytest itself, as they are for every suite run — I did not create or delete them.

**16. Pre-Existing Failure Classification:** none. All eight gates were green at the baseline and are green after the change.

**17. What you can still see that this prompt did not anticipate**

1. **The prompt's own `manage.py check` gate command cannot run.** `-m manage.py` is a hard error. Stated plainly because section 12 invites contradiction with a measurement: the section 9b block, as written, cannot have produced the baseline recorded in the same section.

2. **A real "adding a language" trap this harness does *not* catch — `slug` versus filename stem.** `list_installed_variants()` derives a variant's slug from the manifest's `slug` key (`variant_store.py:324`), but `load_variant(slug)` resolves the file as `_variants_dir() / f"{slugify(slug)}.json"` (`:178-179`). I measured the divergence: a manifest file `de.json` declaring `"slug": "german"` is listed as `german`, while `load_variant("german")` raises `FileNotFoundError: Variant 'german' not found`. G9 **passes** on that directory (one file, one variant), so my harness is blind to it. It is not merely theoretical: `game/serializers.py:180` and `:215` and `game/services.py:173` all validate an incoming `variant_slug` against `{v.slug for v in list_installed_variants()}` and every later load goes through `load_variant`, so such a manifest would pass game creation and queue join and then fail at load. Nothing in the repository asserts stem/slug agreement. This is the single most valuable invariant missing from section 6, and it is exactly the defect shape a fifth language would produce.

3. **Section 2 states an invariant that section 6 never assigns a G-number: "No manifest declares `total_tiles`, and none may."** I confirmed no manifest declares it and that it is derived at `:75-77`. I deliberately did *not* add the assertion, since section 6 is my boundary. The gap is real: the loader silently ignores an unknown `total_tiles` key, so a fifth manifest could declare `"total_tiles": 100` while shipping 98 tiles and read as authoritative to a human reviewer.

4. **`canonicalize_tile_token`'s documented `strip()` step is unreachable from manifest ingestion.** `_parse_asset_token` rejects any token containing whitespace at `:219-222`, *before* canonicalization at `:234`. So the trim half of the "trim → NFC → upper → NFC" contract advertised at `:148` can never fire for a manifest token — a token needing a strip is rejected as `whitespace`, never normalized. Benign today, but the docstring at `:148-152` describes a contract the loader is strictly stricter than, and anyone relying on the trim for a future ingest path (an admin form, a catalog import) would find it silently unreachable through this route.

5. **G13's `fetched_at` check is weaker than it reads.** `datetime.fromisoformat` on Python 3.11+ accepts very short inputs, including a bare `"2026"`. The four shipped values are full naive ISO timestamps, so the assertion passes, but it would also pass on `"2026"`. If the intent was "a real timestamp", the check does not deliver that; I implemented what section 6 specified rather than substituting my own stricter rule.

6. **Section 2's line-number map has minor drift** (immaterial, recorded for the next reader): `VariantDefinition` is at `:44-45` (decorator on 44), the log-and-skip branch is at `:438-439` rather than `:436-439`, and `_load_variant_from_path` — which section 5 authorizes without a line number — is at `:309`. Every load-bearing citation I checked (`:22`, `:24-26`, `:29`, `:147`, `:182`, `:193`, `:214`, `:253`, `:333`, `:338`, `:343`, `:356`, `:377`, `:380`, `:393`, `:407`, `:414`) is exact.

7. **Every measured fact in section 2 that I could verify was correct.** The four-variant table reproduced exactly (english 27/26/2/100/187/26/0, slovak 42/41/2/100/267/46/5, czech 40/39/2/100/205/42/3, polish 33/32/2/100/190/32/0); `grep -rn "list_installed_variants" backend/tests/` returned zero lines; `VARIANT_SLUGS = ("slovak", "english")` is at `test_endgame_policy_matrix.py:68`; english declares neither `language_code` nor `source_url`; slovak is the only variant with `two_tile_words_file`. All six probe words plus the negative probe were confirmed through the index's own `contains` before being written into the table.

**18. One smallest next step**

Add the two unasserted invariants from field 17 items 2 and 3 to the same module as `G26` (`variant.slug == manifest path stem`, parameterized over every installed variant, plus a `tmp_path` negative proving the `list`/`load_variant` divergence) and `G27` (no manifest declares `total_tiles`). Both are pure additions to the one allowlisted file, and item 2 closes a live product hazard rather than a documentation gap.

**19. Report justification:** `new-mutation`

**20. Logical-whole closure:** not-closed

**21. Authority expiry**

My authority expires with this terminal report. I emit no logical-whole closure signal, and this `PASS` closes nothing: it is non-independent implementation evidence produced by the same session that wrote the code. Independent acceptance, if required, needs a fresh Worker that did not materially implement this candidate. I have stopped all autonomous work and will not continue without a new complete prompt.

**22. Context pressure:** Moderate. I read the 654-line prompt in full plus roughly 2 000 lines of repository source, tests, manifests, and AP governance, and ran two full backend suites and four frontend gates. No compaction occurred; ample headroom remained at the terminal report.

