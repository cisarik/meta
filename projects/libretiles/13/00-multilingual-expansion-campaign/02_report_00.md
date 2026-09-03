### Report for ORCHESTRATOR_CHAT

logical whole multilingual-expansion-campaign, Worker session ordinal 02, Worker exchange ordinal 01

**Status:** PASS. Two tests added, both proven to have teeth, P15 proven tolerant in the direction that protects Hungarian, one commit pushed non-force, public readback equal.

**Phase-qualified result:** implementation-PASS
**Result artifact or commit:** `86ec39e08cfe28caa2919279a6123b0814e6032d`
**Result evidence:** one commit touching one test file (+97 lines, 0 deletions); P14 and P15 each shown failing against a constructed violating state and passing against the real tree; P15 shown NOT failing on a claimed-but-absent file; all standing gates green with only the two expected pytest counts moved (542 passed / 546 collected); `validate_lexicons` still 5 assets, 0 failed; `git status --porcelain=v1 -- backend/assets/` empty at every checkpoint.

**Start commit:** `4f6f38d09ec3c0b1cc671b7df752b3f713b52506`
**End commit:** `86ec39e08cfe28caa2919279a6123b0814e6032d`

---

## Section 2 repository gate, verbatim

```text
git rev-parse HEAD                    4f6f38d09ec3c0b1cc671b7df752b3f713b52506
git rev-parse HEAD:.ap                9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git status -sb                        ## main...origin/main
git status --porcelain=v1             (empty)
git ls-remote origin refs/heads/main  4f6f38d09ec3c0b1cc671b7df752b3f713b52506	refs/heads/main
ss -tlnp | grep -E ':(3000|8000)'     no match (grep exit 1) — no listener on either port
```

`ls backend/assets/dicts/` — EIGHT files, no `sowpods.txt`:

```text
collins2019.txt
czech.LICENSE
czech.txt
polish.LICENSE
polish.txt
slovak.LICENSE
slovak_two_tile_words.txt
slovak.txt
```

Every gate line matched the prompt's expected value exactly, so no recovery class was activated. `.ap` was neither attached nor updated; the detached-HEAD-equals-gitlink topology was left as found.

End-of-task re-confirmation (after commit and push):

```text
git status -sb                                   ## main...origin/main
git status --porcelain=v1                        (empty)
git status --porcelain=v1 -- backend/assets/     (empty)
git rev-parse HEAD                               86ec39e08cfe28caa2919279a6123b0814e6032d
git rev-parse HEAD:.ap                           9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD                        9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
ls backend/assets/dicts/                         the same eight files, still no sowpods.txt
```

The assets porcelain was checked before the edit, after the ephemeral proof block was appended, after it was removed, before staging, before commit, and after push. It was empty every time. No file was ever created under `backend/assets/`, and nothing was deleted anywhere.

---

## Changed files and purpose

| Path | Purpose |
|---|---|
| `backend/tests/test_lexicon_provenance.py` | append P14 (the named absence of the unclaimed English word list) and P15 (present ⇒ claimed, one direction only) plus the one shared claim-gathering helper they and the negative proofs call. +97 lines, no deletions, no existing test touched. |

Nothing else was modified. The module docstring, imports, and P1-P13 are byte-identical to the baseline: the two new tests needed no new import (`json`, `Path`, `pytest`, `_DICTS_DIR`, `_VARIANTS_DIR` were all already there), so the import block is unchanged.

---

## My own measured claim table

Measured by a raw JSON scan of `backend/assets/variants/*.json` against `backend/assets/dicts/`, independently of the test:

```text
present file                  claimed by
collins2019.txt               english.json  dictionary_file
czech.LICENSE                 czech.json    lexicon_provenance.license_file
czech.txt                     czech.json    dictionary_file
polish.LICENSE                polish.json   lexicon_provenance.license_file
polish.txt                    polish.json   dictionary_file
slovak.LICENSE                slovak.json   lexicon_provenance.license_file
slovak.txt                    slovak.json   dictionary_file
slovak_two_tile_words.txt     slovak.json   two_tile_words_file

orphans: NONE            claimed-but-absent: NONE
present count: 8         distinct claims: 8
```

This agrees with section 5.1 row for row (my listing is sorted, so the licence rows interleave; the pairs are identical). `english.json` declares `two_tile_words_file` absent and `lexicon_provenance.license_file`/`build_script` null, which is why it claims exactly one file. `build_script` was deliberately excluded from the claim set: all three values (`build_czech_lexicon.py`, `build_polish_lexicon.py`, `build_slovak_lexicon.py`) name files under `backend/scripts/`, and P3/P10b own them.

---

## P14 and P15 as committed

`backend/tests/test_lexicon_provenance.py:465-559`:

```python
# --- P14, P15: nothing unclaimed may sit in the shipped dictionary directory --------------
#
# ``backend/assets/dicts/sowpods.txt`` sat in this repository for the whole life of the
# project claimed by NO manifest, carrying NO provenance, and audited by NOTHING:
# ``validate_lexicons`` walks the MANIFESTS, so a file that no manifest names is invisible to
# it by construction. It has since been deleted. P14 names that one file forever; P15 is the
# rule that makes the whole CLASS of defect impossible, which is the part that matters,
# because this directory is about to receive many more lexicons and their licence files.
#
# ⛔ Neither test reads Git history — the deleted blob deliberately survives there, which is
# exactly what made the deletion reversible — and neither greps the tree for that file's name.
# ``test_documentation_dictionary_claims.py`` owns the documentation claim and necessarily
# contains the name in order to forbid it.

# The manifest fields that CLAIM a file under ``assets/dicts/``. ⚠ ``build_script`` is NOT one
# of them: it names a file under ``backend/scripts/``, and P3 and P10b already own it.
_DIRECT_CLAIM_FIELDS = ("dictionary_file", "two_tile_words_file")
_PROVENANCE_CLAIM_FIELD = "license_file"


def _claimed_dictionary_filenames(variants_dir: Path) -> dict[str, list[str]]:
    """Map every ``assets/dicts/`` name a manifest CLAIMS to the manifests that claim it.

    ⛔ A RAW JSON scan, deliberately NOT ``list_installed_variants()``. That helper wraps each
    load in ``try/except Exception``, logs the failure and CONTINUES, so a manifest that fails
    to load contributes NO claims — and P15 would then report that manifest's perfectly
    legitimate lexicon and licence file as orphans, pointing the reader at the wrong files
    entirely. A raw scan sees the claim regardless of loader health, and loader health is
    owned by P1-P8 and ``variant_store``.

    Read defensively for the same reason: a missing key, a null, or a non-string value
    contributes no claim rather than raising, because P15's job is to find orphans, not to
    re-validate manifest shape. An unparseable manifest is the one exception — a tree where a
    manifest cannot be read is a tree where P15 cannot honestly claim anything.
    """
    claims: dict[str, list[str]] = {}
    for manifest in sorted(variants_dir.glob("*.json")):
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise AssertionError(f"{manifest.name} is not parsable JSON: {exc}") from exc
        if not isinstance(data, dict):
            continue
        declared = [data.get(field) for field in _DIRECT_CLAIM_FIELDS]
        provenance = data.get("lexicon_provenance")
        if isinstance(provenance, dict):
            declared.append(provenance.get(_PROVENANCE_CLAIM_FIELD))
        for value in declared:
            if isinstance(value, str) and value:
                claims.setdefault(value, []).append(manifest.name)
    return claims


def test_p14_the_unclaimed_english_word_list_is_not_shipped() -> None:
    """The named absence. One file, one assertion, and the message says WHY it is unwanted."""
    orphan = _DICTS_DIR / "sowpods.txt"
    assert not orphan.exists(), (
        f"{orphan} is back. It is claimed by no manifest, so it carries no lexicon_provenance "
        f"and validate_lexicons — which walks the manifests — never audits it. The shipped "
        f"Tier-1 English list is collins2019.txt, claimed by english.json"
    )


def test_p15_every_present_dictionary_file_is_claimed_by_a_manifest() -> None:
    """ONE DIRECTION: a file that is PRESENT must be CLAIMED. Never the reverse.

    ⛔ Do not "tighten" this into "every claimed file is present". A future variant is already
    designed to claim a lexicon that is legitimately ABSENT from a fresh checkout: Hungarian's
    expansion is far past any committable size, so its committed build script generates the
    word list locally and that output stays out of Git. Until the local build runs,
    ``hungarian.json`` will claim a ``dictionary_file`` that does not exist, and fail-closed
    readiness reports the variant unavailable — ``gamecore/lexicon_health.py`` owns that, and
    it is correct behaviour rather than a test failure. The loader already enforces the
    alphabet invariant the same way round: every tile token must appear in ``alphabet_order``,
    while ``alphabet_order`` may legitimately carry letters that are not tiles (Slovak ``CH``).
    Reversing either direction fails on an asset that is deliberately shipped or deliberately
    planned.

    ⛔ NO EXEMPTION LIST — not for dotfiles, not for a README, not for ``.gitkeep``. An
    exemption list is precisely where the next orphan would hide. If an unclaimed file is ever
    genuinely needed here, that should cost a deliberate decision, and this test failing is
    that decision's trigger.
    """
    claims = _claimed_dictionary_filenames(_VARIANTS_DIR)
    present = sorted(path for path in _DICTS_DIR.iterdir() if path.is_file())
    orphans = [path.name for path in present if path.name not in claims]
    assert orphans == [], (
        f"unclaimed file(s) under {_DICTS_DIR}: {orphans}. Every file shipped there must be "
        f"claimed by an installed manifest through dictionary_file, two_tile_words_file, or "
        f"lexicon_provenance.license_file; an unclaimed asset carries no provenance and "
        f"validate_lexicons never audits it. Check the manifests as well: a renamed claim, a "
        f"claim written as a path rather than a basename, or a manifest that no longer parses "
        f"presents here as an orphan of the file it used to claim. Currently claimed: "
        f"{sorted(claims)}"
    )
```

Both tests pass against the real tree:

```text
tests/test_lexicon_provenance.py ..                                      [100%]
======================= 2 passed, 45 deselected in 0.09s =======================
```

---

## Class B proofs

**How all four were constructed without writing into the assets tree.** P14 and P15 read the module globals `_DICTS_DIR` and `_VARIANTS_DIR` at call time. Four temporary proof tests were appended to the same allowlisted module, each building a violating or tolerant tree under pytest's `tmp_path`, swapping those globals with `monkeypatch.setitem(globals(), ...)` (auto-restored per test), then calling the real committed test function directly so its own assertion — not a paraphrase of it — produced the failure. Nothing was written under `backend/assets/` at any point; `git status --porcelain=v1 -- backend/assets/` was verified empty while the proofs were in place. The proof block was then removed, and the staged diff was inspected to confirm the committed change is exactly the helper plus P14 plus P15 (`--collect-only` moved by exactly +2).

Run summary:

```text
PASSED tests/test_lexicon_provenance.py::test_zzproof_c_p15_tolerates_a_claimed_but_absent_file
FAILED tests/test_lexicon_provenance.py::test_zzproof_a_p14_fails_when_the_orphan_is_present
FAILED tests/test_lexicon_provenance.py::test_zzproof_b_p15_fails_on_an_unclaimed_file
FAILED tests/test_lexicon_provenance.py::test_zzproof_d_p15_names_an_unparseable_manifest
3 failed, 1 passed, 47 deselected in 0.14s
```

### Proof 1 — P14 has teeth

Violating state: a `sowpods.txt` created in `tmp_path`, with `_DICTS_DIR` pointed at that directory.

```text
    def test_p14_the_unclaimed_english_word_list_is_not_shipped() -> None:
        """The named absence. One file, one assertion, and the message says WHY it is unwanted."""
        orphan = _DICTS_DIR / "sowpods.txt"
>       assert not orphan.exists(), (
            f"{orphan} is back. It is claimed by no manifest, so it carries no lexicon_provenance "
            f"and validate_lexicons — which walks the manifests — never audits it. The shipped "
            f"Tier-1 English list is collins2019.txt, claimed by english.json"
        )
E       AssertionError: /tmp/pytest-of-agile/pytest-45/test_zzproof_a_p14_fails_when_0/sowpods.txt is back. It is claimed by no manifest, so it carries no lexicon_provenance and validate_lexicons — which walks the manifests — never audits it. The shipped Tier-1 English list is collins2019.txt, claimed by english.json
E       assert not True
E        +  where True = exists()
E        +    where exists = PosixPath('/tmp/pytest-of-agile/pytest-45/test_zzproof_a_p14_fails_when_0/sowpods.txt').exists

tests/test_lexicon_provenance.py:521: AssertionError
```

### Proof 2 — P15 has teeth

Violating state: `tmp_path/dicts` holding `collins2019.txt` (claimed), `sowpods.txt` and `README` (unclaimed); `tmp_path/variants/english.json` claiming only `collins2019.txt`. `README` is included on purpose to demonstrate that there is no exemption list.

```text
E       AssertionError: unclaimed file(s) under /tmp/pytest-of-agile/pytest-45/test_zzproof_b_p15_fails_on_an0/dicts: ['README', 'sowpods.txt']. Every file shipped there must be claimed by an installed manifest through dictionary_file, two_tile_words_file, or lexicon_provenance.license_file; an unclaimed asset carries no provenance and validate_lexicons never audits it. Check the manifests as well: a renamed claim, a claim written as a path rather than a basename, or a manifest that no longer parses presents here as an orphan of the file it used to claim. Currently claimed: ['collins2019.txt']
E       assert ['README', 'sowpods.txt'] == []
E         
E         Left contains 2 more items, first extra item: 'README'
E         Use -v to get more diff

tests/test_lexicon_provenance.py:551: AssertionError
```

Every orphan is listed by name, as required.

### Proof 3 — P15 tolerates a claimed-but-absent file (the direction proof)

Tolerant state: `tmp_path/dicts` holding only `czech.txt`; `tmp_path/variants` holding `czech.json` (claims the present `czech.txt`) and `hungarian.json` (claims `hungarian.txt` as `dictionary_file` and `hungarian.LICENSE` as `lexicon_provenance.license_file`, **both absent**, asserted absent inside the proof before P15 ran). The real P15 body was then invoked.

```text
PASSED tests/test_lexicon_provenance.py::test_zzproof_c_p15_tolerates_a_claimed_but_absent_file
```

P15 does not fail on a claimed-but-absent file. The Hungarian slice — committed build script, gitignored output, `lexicon_health` reporting the variant unavailable until a local build runs — will not be blocked by this invariant.

### Proof 4 (extra, not required) — an unparseable manifest fails and is named

`tmp_path/variants/czech.json` containing `{ this is not json`, with `czech.txt` present:

```text
E               AssertionError: czech.json is not parsable JSON: Expecting property name enclosed in double quotes: line 1 column 3 (char 2)

tests/test_lexicon_provenance.py:505: AssertionError
```

The message names the manifest rather than blaming the lexicon it claims. This is the failure mode the raw-JSON-scan decision exists to avoid: had the claim set come from `list_installed_variants()`, this tree would instead have reported the perfectly legitimate `czech.txt` as an orphan.

---

## Gates

RF-16 bounded deviation used exactly as authorized: `poetry run <tool>` was not used; every backend command ran as `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/…` from `backend/`. `.venv/bin/python` was present, and every deviated invocation succeeded, so the stopping condition never triggered. No fallback to ambient `python3` or to `poetry run` occurred. Evidence class: reproduced-dynamic, this task only.

```text
ruff check .                                 All checks passed!                                  (exit 0)
mypy config game gamecore accounts catalog   Success: no issues found in 85 source files         (exit 0)
manage.py check                              System check identified no issues (0 silenced).     (exit 0)
pytest                                       542 passed, 4 skipped in 243.78s (0:04:03)
pytest --collect-only                        546 tests collected in 7.04s
manage.py validate_lexicons                  validate_lexicons: 5 asset(s) audited, 0 failed     (exit 0)
npm run typecheck                            exit 0
npx vitest run                               Test Files  31 passed | 1 skipped (32)
                                             Tests  450 passed | 3 skipped (453)                 (exit 0)
npm run lint                                 exit 0
npm run build                                exit 0, ELEVEN dynamic routes, ZERO static
```

- **mypy file count: 85 source files**, the documented scope `config game gamecore accounts catalog` — neither narrowed nor widened. `backend/tests/` remains outside it; the new code is nevertheless ruff-clean with every line ≤ 100 characters.
- **pytest ran as plain `-m pytest`**, so the single `addopts = "-q"` from `backend/pyproject.toml` applied and the summary line was printed rather than silently suppressed. Summary verbatim: `542 passed, 4 skipped in 243.78s (0:04:03)`.
- **Expected movement, and only that:** 540 → 542 passed (N = 2), 544 → 546 collected (the same N = 2), skips unchanged at 4. Wall clock 243.78 s sits inside the observed 238–245 s band and is machine noise, not a finding.
- **`ss -tlnp | grep :3000` was checked immediately before `npm run build`** and matched nothing (grep exit 1). No process was killed.

`validate_lexicons`, full output, still FIVE assets:

```text
czech dictionary ok reason=ok words=3930497 duplicates=0 non_nfc=0
english dictionary ok reason=ok words=279496 duplicates=0 non_nfc=0
polish dictionary ok reason=ok words=3721704 duplicates=0 non_nfc=0
slovak dictionary ok reason=ok words=3005250 duplicates=0 non_nfc=0
slovak two_tile ok reason=ok words=103 duplicates=0 non_nfc=0
validate_lexicons: 5 asset(s) audited, 0 failed
```

Route table from `npm run build`, all eleven `ƒ` (dynamic), zero `○` (static): `/`, `/_not-found`, `/api/ai/judge`, `/api/ai/move`, `/api/models`, `/api/prompts`, `/draw/[id]`, `/game/[id]`, `/play`, `/settings`, `/waiting/[id]`, plus `ƒ Proxy (Middleware)`.

**Two separate frontend claims:**

1. **The build passed.** `npm run build` exited 0, compiled in 2.1 s, generated 10 pages, and produced the unchanged eleven-dynamic-route table above.
2. **The code type-checks.** `npm run typecheck` (`tsc --noEmit --incremental false`) exited 0 as its own independent run, and Next reported `Finished TypeScript in 1596ms` inside the build.

---

## Git sequence

```text
git add backend/tests/test_lexicon_provenance.py
git status --porcelain=v1                     M  backend/tests/test_lexicon_provenance.py   (that one path only)
git status --porcelain=v1 -- backend/assets/   (empty)
git diff --cached --stat                       1 file changed, 97 insertions(+)
git commit                                     [main 86ec39e] test(lexicons): no unclaimed file may sit in the shipped dictionary directory
PRE-PUSH GATE  git ls-remote origin refs/heads/main   4f6f38d09ec3c0b1cc671b7df752b3f713b52506   (equals the exact baseline)
git push origin main                           To https://github.com/cisarik/libretiles
                                                  4f6f38d..86ec39e  main -> main       (non-force fast-forward, exit 0)
READBACK       git ls-remote origin refs/heads/main   86ec39e08cfe28caa2919279a6123b0814e6032d
               git rev-parse HEAD                     86ec39e08cfe28caa2919279a6123b0814e6032d   → EQUAL
```

The remote gate was read twice — once before the commit and once immediately before the push — and both returned the exact baseline, so no escalation was needed. `git log --oneline -3`:

```text
86ec39e test(lexicons): no unclaimed file may sit in the shipped dictionary directory
4f6f38d chore(dicts): remove obsolete SOWPODS dictionary file
a199d0e docs(env): document PRIMARY_DICTIONARY_FILE, the undocumented Tier-1 override
```

No force, amend, rebase, reset, clean, stash, branch, or tag. No `git add -A` or `git add .`. Rollback is `git revert 86ec39e` and is total: one test file, no production code, no asset.

---

**Deviations:** one, the authorized RF-16 route deviation described above; no other. No path was deleted. No dependency, lockfile, manifest, asset, documentation, frontend file, provider constant, or mypy scope was touched. `backend/.env` and `frontend/.env.local` were never opened. Network was limited to two `git ls-remote` reads and one `git push`. The only file read under `/home/agile/meta/` was the delivery prompt itself; nothing there was listed, searched, or written. Temporary evidence lived only in `/tmp/opencode/mec-v3dguard/` and was removed at the end (directory now absent).

**Risks:** low and bounded. The one durable decision is P15's direction, and it is now proven by execution in both directions rather than asserted. The residual risk is that a future author reads the invariant as symmetric; that is mitigated by the in-test comment, which names Hungarian and the Slovak `CH` alphabet precedent as the reason.

**Missing evidence:** none for this task. Independence is not claimed — all evidence is same-session implementation evidence and therefore non-independent.

**Resolved Execution Issues / Near-Misses:**

- **Near-miss avoided by design, not luck.** The obvious way to prove P14 has teeth is to create `backend/assets/dicts/sowpods.txt` for two seconds. That would have dirtied the assets tree and tripped a stopping condition. Pointing the module global at `tmp_path` instead gives identical evidence with an empty assets porcelain throughout.
- **Cleanup verified rather than assumed.** The four ephemeral proof tests lived inside the allowlisted file. After removal I did not trust the edit: `git diff --cached --stat` (+97/−0), a full read of the staged diff, and `--collect-only` moving by exactly +2 all confirm the committed change contains no proof scaffolding.
- No command failed, no gate needed a rerun, and no repeated-blocker escalation applies.

**Pre-Existing Failure Classification:** none. Zero failures at the baseline and zero after the change. The four pytest skips and the three vitest skips are unchanged pre-existing skips, not failures. The `[libretiles-provider-failure] … rate limit` and `No endpoints found for stealth/example:free` lines in the vitest output are deliberate stderr from negative-path provider tests inside a passing run, exactly as at the baseline.

---

```text
⚠ WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE
```

**MEASURED**

1. **`frontend/public/` is the next directory with no claim-and-audit relationship, and it already contains six unreferenced files.** I grepped every name in `frontend/public/` against `frontend/src`, `frontend/*.ts`, `frontend/*.json`, `frontend/*.mjs`. Referenced: `en.png`, `sk.png`, `cs.png`, `pl.png` (2 files each, via the `GameLanguagePanel` flag map and `PremiumPicker.test.ts`) and `drevo.jpeg` (1). **Zero references: `hu.png`, `file.svg`, `globe.svg`, `next.svg`, `vercel.svg`, `window.svg`.** Five are Next.js scaffolding leftovers. `hu.png` is not: a Hungarian flag is already shipped for a language that has no manifest, no lexicon and no entry in the flag map. This is the same shape of defect as the deleted orphan — an asset in the tree that nothing claims — and the campaign will add a flag per language, so the count only grows. A P15-analogue over `frontend/public/` would have to be scoped carefully (Next's `favicon.ico`/`robots.txt`/`sitemap.xml` conventions are claimed by the framework, not by source text), which is why I did not invent one here.
2. **`backend/assets/` has two more asset surfaces, both claimed only by code rather than by a manifest.** `premiums.json` is claimed by `gamecore/assets.get_premiums_path()`; `diagnostics/ai_play_report_v1.schema.json` and `diagnostics/ai_play_scenarios_v1.json` are claimed by `game/diagnostics.py` and its tests. Both are genuinely referenced today, so there is no orphan there now — but neither has a mechanical invariant, so a future unclaimed file in `backend/assets/diagnostics/` would rot exactly as `sowpods.txt` did. P15 is scoped to `dicts/` and does not see either directory.
3. **The `variants/` side of the P15 pair is already guarded, contrary to what I first suspected.** `test_variant_invariants.py` G1 fails if `list_installed_variants()` is empty, and G9 (`test_g9_installed_count_matches_manifest_file_count`) fails if the manifest file count and the loaded variant count disagree — which is precisely the silent-skip hazard behind P15's raw-JSON-scan decision. G9c proves G9 can fail. So a broken or renamed manifest cannot silently shrink the parametrized matrix; it fails G9 loudly. Worth stating explicitly because it means the campaign's twenty new manifests are automatically enrolled in P1-P13 and G1-G25 the moment they land.
4. **P15 would pass vacuously on an empty `dicts/` directory.** I did not add a non-emptiness assertion, because the prompt specified one direction and one comparison, and vacuity is already impossible in practice: P2 and P4 read `collins2019.txt` and every shipped lexicon by path, and `validate_lexicons` audits five assets. An empty directory fails loudly several tests earlier. Flagging it so the omission is a recorded decision rather than an oversight.
5. **P15's claim comparison is exact-string, deliberately fail-closed.** A manifest that ever wrote `"dicts/czech.txt"` instead of `"czech.txt"` would make P15 report `czech.txt` as an orphan rather than accepting the path form. The failure message says so, and P2 independently enforces basename-only for `license_file`. This is the right default for twenty incoming manifests, but a reviewer seeing that failure must read the message rather than assume a missing file.

**LEAD**

1. `hu.png` shipping ahead of the Hungarian slice suggests the flag assets may have been added for a planned language set as a batch. If so, the campaign will add flags for languages whose manifests land much later, and any `frontend/public/` invariant written now in the "present ⇒ referenced" direction would block that. Unverified: I did not look for a commit that introduced `hu.png` or for a design note listing the intended language set.
2. `backend/assets/dicts/` is enumerated by `iterdir()`, so a subdirectory placed there is skipped by P15 (`if p.is_file()`). If a future language ships a multi-file lexicon bundle in a subdirectory, it would be invisible to this invariant. I did not verify whether any planned language needs more than a flat `.txt` plus `.LICENSE`.
3. The `.gitignore` treatment of the planned Hungarian output is unverified. P15 tolerates the absence, but if the generated file lands under `backend/assets/dicts/` and is *not* gitignored, a developer who runs the local build would then have an untracked large file in a directory that P15 does claim-checks over — passing only because `hungarian.json` claims it. Worth pinning the ignore rule in the same slice that adds the script.

---

**Smallest next step:** extend the same present-must-be-claimed invariant to `frontend/public/`, scoped to the flag/image assets that source code is supposed to reference, and dispose of `hu.png` explicitly — either delete it or let the Hungarian slice claim it. That is one bounded test-plus-decision exchange, and doing it before twenty flags arrive is cheaper than after.

**Report justification:** new-mutation
**Logical-whole closure:** not-closed

My authority expires with this terminal report. Nothing here closes the logical whole, and no `PASS` I have reported is acceptance, publication, or closure — those remain Orchestrator- and Cooperator-owned. I will take no further action without a new complete authoritative prompt.

**Context pressure:** low-to-moderate. Roughly two thirds of the window remains; the largest consumers were `AP.md` and the 462-line baseline test module. No compaction occurred, and no evidence in this report was reconstructed from memory — every value above was read back from a command in this session.
