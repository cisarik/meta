### Report for ORCHESTRATOR_CHAT

logical whole multilingual-expansion, Worker session ordinal 04, Worker exchange ordinal 03

**Status: PASS**

`Phase-qualified result:` implementation-PASS
`Result artifact or commit:` ad4ce038e1bd3511bdd5b7431eb9c163d4788130
`Result evidence:` `--check` exits 0 for all three languages on **twelve agreeing digests**; exits 1 on an altered comparison target; **refuses** an assets-tree working directory with exit 2 in three distinct forms while writing nothing; the expander is pinned to `hunspell 1.7.3` and fails closed; `AGENTS.md` carries the one addition; `backend/assets/` is byte-for-byte untouched and nothing was deleted; all eight standing gates green; one non-force push with matching public readback.

Start commit `a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8` → end commit `ad4ce038e1bd3511bdd5b7431eb9c163d4788130`.

---

## Section 2 repository re-gate (verbatim)

```text
git rev-parse HEAD                    a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8
git rev-parse HEAD:.ap                9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   (detached, matching pin)
git status -sb                        ## main...origin/main
git status --porcelain=v1             <empty>
git ls-remote origin refs/heads/main  a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8	refs/heads/main
ss -tlnp | grep -E ':(3000|8000)'     no match (grep exit 1) — no listener
command -v unmunch hunspell           /usr/bin/unmunch
                                      /usr/bin/hunspell
```

Every value matched and agreed with my retained context; no recovery class applied. `.ap` was never attached or updated.

### End-of-task re-confirmation

```text
git rev-parse HEAD                                     ad4ce038e1bd3511bdd5b7431eb9c163d4788130
git rev-parse HEAD:.ap / git -C .ap rev-parse HEAD     9c5cc44… / 9c5cc44…  (unchanged)
git status -sb                                         ## main...origin/main
git status --porcelain=v1                              <EMPTY>
git status --porcelain=v1 -- backend/assets/           <EMPTY>
git diff --stat a3ed00f HEAD -- backend/assets/        <EMPTY — no asset byte changed, nothing deleted>
git ls-files backend/assets/dicts/sowpods.txt          backend/assets/dicts/sowpods.txt   (still tracked)
ss -tlnp | grep -E ':(3000|8000)'                      no match
```

## Changed files and purpose (5 paths, exactly the allowlist)

| Path | Purpose |
|---|---|
| `backend/scripts/build_czech_lexicon.py` | `--check` + `--check-dir`, `is_inside_assets`, `require_check_dir_outside_assets`, `_require_expander`, `_compare_against_committed`, `build_parser` seam, `--hunspell` |
| `backend/scripts/build_polish_lexicon.py` | same six additions |
| `backend/scripts/build_slovak_lexicon.py` | same six additions |
| `backend/tests/test_lexicon_provenance.py` | P11, P12, P13 (+7 test items); `_EXPECTED_EXPANDER`; `import os` |
| `AGENTS.md` | three Key-files rows and one paragraph — nothing else |

Nothing deleted. `libretiles_PRD.md` untouched. No manifest, no `gamecore/**`, no `game/**`, no `config/**`, no frontend file, no dependency.

---

## The twelve `--check` digests

All three runs exited **0**. Every line is the script's own `CHECK` output, printing both digests per artifact.

| Language | Artifact | Reproduced | Committed | Verdict |
|---|---|---|---|---|
| slovak | `slovak.txt` | `edca5453c7766cfcd4c0a0b3b7e53abaeb0d640cc541b628dbaab497ff8f0a5d` | `edca5453c7766cfcd4c0a0b3b7e53abaeb0d640cc541b628dbaab497ff8f0a5d` | **IDENTICAL** |
| slovak | `slovak.LICENSE` | `f3ad399bbebd143a7f2ccc95af2799813a6b9312426a8038230ce34bef483837` | `f3ad399bbebd143a7f2ccc95af2799813a6b9312426a8038230ce34bef483837` | **IDENTICAL** |
| czech | `czech.txt` | `919d6bac41b0938bc1955685b826857aa21543d4dd45a4035c1fa08aa4cc5bdc` | `919d6bac41b0938bc1955685b826857aa21543d4dd45a4035c1fa08aa4cc5bdc` | **IDENTICAL** |
| czech | `czech.LICENSE` | `bde41b518094f12ea79bdfc1396a6b9562bc1d994da1fd37a07a06fd71f185a8` | `bde41b518094f12ea79bdfc1396a6b9562bc1d994da1fd37a07a06fd71f185a8` | **IDENTICAL** |
| polish | `polish.txt` | `605d5a43d5d5dcd1b386ab9f9f62b72eb964882f6a9ccbe244a826e0baa06aab` | `605d5a43d5d5dcd1b386ab9f9f62b72eb964882f6a9ccbe244a826e0baa06aab` | **IDENTICAL** |
| polish | `polish.LICENSE` | `869efadec82ae6aba8270ca5a3eaa6fce4bfd2336824548f03acae037b5aa9c3` | `869efadec82ae6aba8270ca5a3eaa6fce4bfd2336824548f03acae037b5aa9c3` | **IDENTICAL** |

All six match the digests you verified in section 5, so the reproduction has **not** regressed since exchange 01 — and it is now a command rather than a procedure reconstructed from prose. Each run also re-asserted its upstream SHA-256 pins, its affix `SET` line (`SET UTF-8` for cs_CZ, `SET ISO8859-2` for pl_PL), its licence sentence, and its version evidence; word counts were 3 005 250 / 3 930 497 / 3 721 704 as before.

## Negative proof N-A — altered comparison target, in `/tmp` only

I copied the committed `czech.txt` to `/tmp/opencode/mle-v3c/altered/czech.txt` and changed exactly one word, `aachen` → `aachex`, in that copy. Same byte length, so a size check would not have noticed.

```text
sha256 backend/assets/dicts/czech.txt              919d6bac41b0938bc1955685b826857aa21543d4dd45a4035c1fa08aa4cc5bdc
sha256 /tmp/opencode/mle-v3c/altered/czech.txt     c9fc859fc9e0516ee5753b921c50a8074526bd871bc53543849051fb15978c31

CHECK czech.txt     reproduced=919d6bac41b0938bc1955685b826857aa21543d4dd45a4035c1fa08aa4cc5bdc
                    committed=c9fc859fc9e0516ee5753b921c50a8074526bd871bc53543849051fb15978c31  MISMATCH
CHECK czech.LICENSE reproduced=bde41b518094f12ea79bdfc1396a6b9562bc1d994da1fd37a07a06fd71f185a8
                    committed=bde41b518094f12ea79bdfc1396a6b9562bc1d994da1fd37a07a06fd71f185a8  IDENTICAL
stderr: ERROR --check found 1 mismatching artifact(s)
EXIT = 1
```

The check has teeth: one word in 3 930 497 produced a non-zero exit, and the unaffected artifact still reported `IDENTICAL`, so the failure is localised rather than blanket. No committed asset was altered to obtain this.

## Negative proof N-B — the refusal, three ways

```text
assets porcelain BEFORE:  git status --porcelain=v1 -- backend/assets/   <EMPTY>

N-B1  --check --check-dir assets/dicts/rebuild              (relative, inside dicts)   EXIT = 2
      ERROR refused by require_check_dir_outside_assets: --check work directory
      assets/dicts/rebuild resolves to /home/agile/Projects/libretiles/backend/assets/dicts/rebuild,
      which is inside the read-only assets tree /home/agile/Projects/libretiles/backend/assets.
      --check never writes under backend/assets/ because the committed asset is the comparison
      oracle; pass a directory outside it.

N-B2  --check --check-dir scripts/../assets                 (`..` traversal)           EXIT = 2
      ERROR refused by require_check_dir_outside_assets: --check work directory
      scripts/../assets resolves to /home/agile/Projects/libretiles/backend/assets, which is
      inside the read-only assets tree … (same message)

N-B3  --check with NO --check-dir                                                      EXIT = 2
      ERROR --check requires --check-dir DIRECTORY. It has no default because the only default
      it could have would sit under backend/assets/, which is exactly where --check must never write.

assets porcelain AFTER:   git status --porcelain=v1 -- backend/assets/   <EMPTY>
ls backend/assets/dicts/  collins2019.txt  czech.LICENSE  czech.txt  polish.LICENSE  polish.txt
                          slovak.LICENSE  slovak.txt  slovak_two_tile_words.txt  sowpods.txt
```

Nine files before, the same nine after — no `rebuild/` directory, no stray artifact, nothing written. Each refusal fired before any expansion, so no work was even attempted against the assets tree.

## The refusal guard, quoted from the code

`backend/scripts/build_czech_lexicon.py:99-130` (identical at `build_polish_lexicon.py:106-137` and `build_slovak_lexicon.py:71-102`):

```python
def is_inside_assets(path: Path) -> bool:                     # czech:99  polish:106  slovak:71
    """True when ``path`` resolves inside ``backend/assets/``.

    Both sides are ``resolve()``d FIRST, so a relative path, a ``..`` traversal and a symlink
    whose own name looks harmless all collapse to the same answer. A textual prefix test
    would let every one of those three straight through.
    """
    resolved = path.resolve()
    assets = _ASSETS_ROOT.resolve()
    return resolved == assets or assets in resolved.parents


def require_check_dir_outside_assets(path: Path) -> Path:      # czech:111 polish:118 slovak:83
    """Refuse a ``--check`` working directory inside the assets tree; return the resolved dir.

    ⛔ This is the guard the whole ``--check`` mode exists for. The committed asset is the
    comparison ORACLE, so a mode that reproduced into the assets tree would overwrite the
    very file it claims to verify and then report agreement with itself.
    """
    resolved = path.resolve()
    if is_inside_assets(path):
        print(
            "ERROR refused by require_check_dir_outside_assets: --check work directory "
            f"{path} resolves to {resolved}, which is inside the read-only assets tree "
            f"{_ASSETS_ROOT.resolve()}. --check never writes under backend/assets/ because "
            "the committed asset is the comparison oracle; pass a directory outside it.",
            file=sys.stderr,
        )
        raise SystemExit(2)
    return resolved
```

Both sides resolve before comparing, and the equality arm catches `backend/assets` itself while the `parents` arm catches everything beneath it. The message names the function that refused, the path as given, what it resolved to, and why.

## Measured host expander version, both routes

```text
route 1   hunspell -vv < /dev/null   ->  @(#) International Ispell Version 3.2.06 (but really Hunspell 1.7.3)
                                         exit 0, banner on stdout
route 2   pacman -Qo /usr/bin/unmunch  ->  /usr/bin/unmunch is owned by hunspell 1.7.3-1.1
          pacman -Qo /usr/bin/hunspell ->  /usr/bin/hunspell is owned by hunspell 1.7.3-1.1
control   unmunch <no args>          ->  correct syntax is: / unmunch dic_file affix_file   (no version, as you measured)
```

**hunspell 1.7.3**, so the section 8 condition did not fire. Each script prints `expander=hunspell 1.7.3 confirmed: @(#) International Ispell Version 3.2.06 (but really Hunspell 1.7.3)` before expanding, and `_require_expander` `raise SystemExit(1)` on a mismatch or on unreadable output — never a warning. An absent `hunspell` is a `return 1` failure with the message that an unverified expander is not a pass. Matching is case-insensitive against the banner because the banner capitalises `Hunspell`, which lets one constant serve both the pin and the probe.

## Upstream sources: cache-hit, zero GETs

**All twelve pinned files were cache hits; I re-downloaded nothing and made ZERO network requests.** The exchange-01 caches survived at `/tmp/opencode/mle-v3/cache-{cs_CZ,pl_PL,sk_SK}` and I passed each as `--cache-dir`. Each run still recomputed and compared **every** cached file's SHA-256 against its pin — 5 files for Czech, 4 for Polish, 4 for Slovak across the three passing runs plus 5 more in N-A — so the pins were verified 18 times without a single GET. A `GET ` line is printed unconditionally on download and none appeared in any run.

---

## Test table

| ID | Class | Result | Note |
|---|---|---|---|
| P11 ×3 | **B** | pass | `--check` present, `--check-dir` has **no default**, guard callable, expander pinned |
| P12 ×3 | **B** | pass | six refusal routes each proven, one permit proven, no subprocess |
| P13 | **B** | pass | one constant, identical across all three scripts |
| P1–P10b (38) | A | pass | unchanged, nothing weakened |
| P14 | — | **deferred by decision** | no test asserts `sowpods.txt` absent; it is present on purpose |

P12's six refusal candidates are deliberately different routes to the same directory: the assets root itself, `assets/dicts`, a deeper non-existent path, a `..` traversal built from `scripts/`, a CWD-relative path computed at runtime via `os.path.relpath`, and a **symlink under `tmp_path` named `looks-like-a-safe-tmp-dir` pointing into `assets/dicts`**. Each asserts `is_inside_assets(...) is True` and that the raiser exits non-zero; the permit case asserts the resolved path is returned. Suite total 531 → 538 passed (+7), collected 535 → 542.

### Captured CLASS B failures, against the pre-change scripts

Missing **flag** (parser seam absent — captured with P11's parser assertion temporarily moved first, then reverted):

```text
>       parser = module.build_parser()  # CAPTURE-REORDER
E       AttributeError: module '_libretiles_build_script_build_czech_lexicon' has no attribute 'build_parser'
tests/test_lexicon_provenance.py:398: AttributeError
```

Missing **constant** (P11, all three parametrisations):

```text
>       assert module.EXPECTED_EXPANDER == _EXPECTED_EXPANDER, (
E       AttributeError: module '_libretiles_build_script_build_polish_lexicon' has no attribute 'EXPECTED_EXPANDER'
E       AttributeError: module '_libretiles_build_script_build_slovak_lexicon' has no attribute 'EXPECTED_EXPANDER'
FAILED …test_p11…[czech]  FAILED …test_p11…[polish]  FAILED …test_p11…[slovak]     3 failed in 0.14s
```

Missing **guard** (P12, all three):

```text
>           assert module.is_inside_assets(candidate) is True, (
E           AttributeError: module '_libretiles_build_script_build_slovak_lexicon' has no attribute 'is_inside_assets'
tests/test_lexicon_provenance.py:444: AttributeError
FAILED …test_p12…[czech]  FAILED …test_p12…[polish]  FAILED …test_p12…[slovak]     3 failed in 0.08s
```

P13 against the pre-change scripts:

```text
>       values = {script: _load_script(script).EXPECTED_EXPANDER for _, script in _SCRIPT_CLAIMS}
E       AttributeError: module '_libretiles_build_script_build_czech_lexicon' has no attribute 'EXPECTED_EXPANDER'
1 failed in 0.07s
```

## The exact `AGENTS.md` diff

```diff
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -100,6 +100,11 @@ npm run build
 | Fallback attempt pills | `frontend/src/components/game/AIThinkingOverlay.tsx` |
 | Header / game chrome | `frontend/src/components/game/ScorePanel.tsx`, `frontend/src/components/game/GameControls.tsx` |
 | Shared premium UI effect + ping-pong motion | `frontend/src/lib/premiumSurface.ts` |
+| Lexicon build scripts (pinned upstream) | `backend/scripts/build_slovak_lexicon.py`, `backend/scripts/build_czech_lexicon.py`, `backend/scripts/build_polish_lexicon.py` |
+| Lexicon provenance in manifests | `backend/assets/variants/*.json` → `lexicon_provenance` |
+| Lexicon asset validation | `backend/gamecore/lexicon_health.py`, `manage.py validate_lexicons` |
+
+Every non-English lexicon is reproducible from a pinned upstream commit by its committed script: each pins the upstream commit and the SHA-256 of every source file it fetches, pins the host expander (`hunspell 1.7.3`) and fails closed on a mismatch, and writes the lexicon plus its `.LICENSE`. Adding `--check --check-dir <dir outside backend/assets/>` re-verifies a committed asset instead of rebuilding it: the reproduction goes into that directory, both digests are printed per artifact, the exit code is non-zero on any mismatch, and the run refuses outright if its working directory resolves inside `backend/assets/`. The scripts are host tools — not imported by Django, and they add no Poetry or npm dependency.
 
 ## Current product state (August 2026)
```

Five added lines, zero removed, zero modified. No provider list, provider constant, model tuple, provider tier or provider documentation touched. No Hungarian claim. No mention of sowpods. "Not done yet" untouched.

---

## The eight standing gates

```text
1  mypy config game gamecore accounts catalog   Success: no issues found in 85 source files
2  ruff check .                                 All checks passed!
3  manage.py check                              System check identified no issues (0 silenced).
4  pytest                                       538 passed, 4 skipped in 238.52s (0:03:58)
   pytest --collect-only                        542 tests collected in 6.50s
5  npm run typecheck                            exit 0
6  npx vitest run                               Test Files  31 passed | 1 skipped (32)
                                                Tests  450 passed | 3 skipped (453)
7  npm run lint                                 exit 0
8  npm run build                                exit 0 — ELEVEN dynamic (ƒ) routes, ZERO static
```

Baseline comparison: 531 → **538** passed (+7, all new), 4 skipped unchanged, 535 → 542 collected, wall clock 237.94 s → 238.52 s (+0.6 s). `pytest` was run plain with no second `-q`, so the summary is the unsuppressed one. mypy ran the full documented scope, neither narrowed nor widened — `backend/scripts/` stays outside it while `ruff check .` does cover it, and all three modified scripts are ruff-clean. `ss -tlnp | grep :3000` was re-checked immediately before `npm run build`: free, nothing killed.

`manage.py validate_lexicons` — still **5 assets, 0 failed**, the cheapest proof no shipped asset moved:

```text
czech dictionary ok reason=ok words=3930497 duplicates=0 non_nfc=0
english dictionary ok reason=ok words=279496 duplicates=0 non_nfc=0
polish dictionary ok reason=ok words=3721704 duplicates=0 non_nfc=0
slovak dictionary ok reason=ok words=3005250 duplicates=0 non_nfc=0
slovak two_tile ok reason=ok words=103 duplicates=0 non_nfc=0
validate_lexicons: 5 asset(s) audited, 0 failed          exit 0
```

**Two separate frontend claims, stated separately:** (1) **the build passed** — `npm run build` exited 0, eleven dynamic routes and zero static; (2) **the code type-checks** — `npm run typecheck` (`tsc --noEmit --incremental false`) exited 0 independently of the build's bundled TypeScript step.

## Git sequence

```text
git add <5 allowlisted paths>
git status --porcelain=v1              M AGENTS.md · M build_czech · M build_polish · M build_slovak
                                       M test_lexicon_provenance.py   — exactly five, nothing else
git status --porcelain=v1 -- backend/assets/    <EMPTY>
git diff --cached --stat               5 files changed, 555 insertions(+), 18 deletions(-)
git commit                             [main ad4ce03] feat(lexicons): --check re-verifies a committed
                                       asset without writing to it; pin the expander
git ls-remote origin refs/heads/main   a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8   (pre-push gate = exact baseline)
git push origin main                   a3ed00f..ad4ce03  main -> main   (fast-forward, non-force)
git ls-remote origin refs/heads/main   ad4ce038e1bd3511bdd5b7431eb9c163d4788130
git rev-parse HEAD                     ad4ce038e1bd3511bdd5b7431eb9c163d4788130   → READBACK EQUAL
```

No `git rm`, no deletion, no `git add -A/.`, no force, amend, rebase, reset, clean, stash, branch or tag. The commit message does not mention sowpods.

---

## Deviations, risks, missing evidence

**Deviations**

1. **`--check-dir` is the directory flag** (the prompt wrote `<dir-flag>` as a placeholder). Two flags rather than one value-taking `--check` is what makes "if the caller omits it, exit non-zero with a message naming the flag" reachable at all — with a single value-taking flag, argparse would error first and the required message could never be printed. N-B3 is the proof.
2. **`build_parser()` extracted as a public seam** in all three scripts. P11 inspects the CLI "by importing the modules and inspecting their argparse configuration" as section 5 requires; without a seam that is only possible through `parser._actions` after calling `main()`, and calling `main()` is forbidden. The seam also let P11 assert `get_default("check_dir") is None` through public API, which *is* the no-default invariant rather than a proxy for it.
3. **`--hunspell` added** alongside the existing `--unmunch`, for symmetry and so a host with hunspell elsewhere can still satisfy the pin. Absence is a failure, never a pass.
4. **P12 tests six refusal routes, not the four listed**, adding a `..` traversal and a symlink decoy. Section 4a names symlinks as a way past a naive check, so I proved that specific case rather than describing it.
5. **`--output-dict` / `--output-license` become the read-only comparison target in `--check` mode** (they remain the write target in a normal run). This is what makes N-A possible without touching a committed asset, and it keeps the flag count down. One meaning per mode, stated in the `--check` banner line the script prints.

**Risks**

- **The pin is host-wide, not per-language.** One `EXPECTED_EXPANDER` in three files is what P13 guards, but three copies of the same constant is still three places to edit. A shared module would fix that and was outside the allowlist; duplication also matches the existing template-per-language style.
- **`--check` costs a full expansion** (about 8 s per language plus roughly 245 MB of intermediate `unmunch` stdout). It is a manual command, not a gate, so nothing regresses — but nothing runs it automatically either. Whether re-verification should ever be scheduled is a decision, not an omission.
- **The pin is on the expander, not on `libhunspell`.** `hunspell -vv` reports the CLI's version; a rebuilt `libhunspell-1.7.so.0.1.0` with different affix behaviour under the same version string would pass. The digest comparison is what would actually catch that, which is another argument for running `--check` after any hunspell package change.
- **`sowpods.txt` and the `libretiles_PRD.md` reference both remain**, by decision. The blocker recorded in exchange 02 is unchanged and still owned by your sequencing.

**Missing evidence**

- No `--check` run was made against a **mismatching LICENSE**; N-A altered the lexicon only. The `_compare_against_committed` loop is shared, and N-A shows the per-artifact verdict is independent (`MISMATCH` beside `IDENTICAL`), so the LICENSE arm is exercised on every passing run and its failure arm is the same code path.
- The expander **mismatch** branch was not executed, because the host version matches and section 8 forbids pinning a constant I cannot satisfy. Only the success branch is demonstrated; the failure branch is `raise SystemExit(1)` on the same function, four lines below the success print.
- The `PRIMARY_DICTIONARY_FILE` disposition and the deployed `.env` value remain unknown by design (secret authority: none).

`Resolved Execution Issues / Near-Misses:`
1. **The refusal guard nearly had a textual implementation.** A `str(path).startswith(str(assets))` test is the obvious form and it passes exactly the three cases that matter — relative path, `..`, symlink. Resolved by resolving both sides first and by proving all three routes in P12 plus two of them as live CLI refusals (N-B1, N-B2). Residual risk: none measured.
2. **`hunspell -vv` could have hung.** It prints a banner and then, in other invocations, reads stdin; a `subprocess.run` without stdin redirection can block a build script indefinitely. Caught before writing, resolved with `stdin=subprocess.DEVNULL`, and verified out-of-band that `hunspell -vv < /dev/null` exits 0. Residual risk: none.
3. **The CLASS B "missing flag" capture was initially indistinguishable from "missing constant."** P11 asserts the constant first, so all three parametrisations failed on `EXPECTED_EXPANDER` and the flag was never reached. Resolved by temporarily moving the parser assertion to the top of P11, capturing the distinct `no attribute 'build_parser'` failure, and reverting immediately — so all three required captures are genuinely distinct rather than three views of one.
4. **`build_slovak_lexicon.py:_run_unmunch` never created its output parent** (unlike the Czech and Polish copies I wrote in exchange 01). In `--check` mode the raw dump goes into the work directory, so I `mkdir` that directory before use rather than editing the shared helper. Residual risk: none; the asymmetry is now benign but remains a small inconsistency between the three scripts.

`Pre-Existing Failure Classification:` none. Every gate was green at `a3ed00f` and is green at `ad4ce03`; no pre-existing failure was inherited, masked or worked around.

---

⚠ **WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE**

**MEASURED**

1. **`--check` proves the reproduction is stable across process runs and across a day, not just repeatable within one session.** Exchange 01 reproduced these six artifacts once; this exchange reproduced them again from the same pinned sources in fresh processes with different working directories, and all twelve digests agree. That is a stronger claim than "the script worked" — it is "the pipeline is deterministic," and it is the claim the provenance in the manifests actually depends on.
2. **The `..` refusal fired on `scripts/../assets`, which resolves to the assets root itself** — the equality arm of the guard, not the `parents` arm. Both arms are load-bearing and I found no test that would have distinguished them; P12's "assets root itself" case is the only thing covering that branch, and it exists because I enumerated the arms rather than the examples.
3. **A same-length alteration is invisible to every check except the digest.** N-A's altered copy is byte-for-byte the same length as the committed file (`aachen` → `aachex`) and `validate_lexicons` would still have reported `words=3930497 duplicates=0 non_nfc=0`. Word counts, sizes and the audit all agree on a file with a corrupted word; only SHA-256 disagreed. That is the concrete reason section 5c of exchange 01 forbade a word-count comparison.
4. **Zero GETs were needed, and the pins were still verified eighteen times.** Cache reuse does not weaken the evidence because `_ensure_pinned_sources` re-hashes on the cache-hit path too — the `cache hit` line is followed by a `SHA-256` line and a comparison every time. Cheap re-verification and strong re-verification turn out not to be in tension here.
5. **`--check` writes roughly 245 MB of intermediate `unmunch` stdout per full sweep** (135 MB Slovak, 58 MB Czech, 51 MB Polish) into the caller's directory. Harmless in `/tmp`, but a caller who points `--check-dir` at a small volume will fill it, and nothing warns. I removed those intermediates after measuring; the total footprint of this exchange was 537 MB before cleanup, 197 MB after.
6. **The refusal message is emitted before the expander banner in the terminal**, because stderr is unbuffered while stdout is block-buffered. The guard genuinely fires before any expansion, but the interleaving reads backwards, which could mislead someone diagnosing a refusal from a captured log.

**LEAD**

1. **Nothing schedules `--check`, so the reproduction claim can still silently rot.** The manifests assert `expander: "unmunch (hunspell 1.7.3)"` and an `entry_count`, and P4 verifies the count on every suite run — but the *byte* claim is only ever verified when a human runs the command. A CI or cron route that runs the three `--check`s after any hunspell package change would close the last gap between "documented as reproducible" and "known to be reproducible."
2. **The three scripts now share about 90 duplicated lines** (`is_inside_assets`, `require_check_dir_outside_assets`, `_require_expander`, `_compare_against_committed`). P13 guards the one constant; nothing guards the four function bodies. A fourth language will copy them a fourth time. A `backend/scripts/_lexicon_build.py` shared helper with the per-language scripts importing it would collapse that, and P13 would become unnecessary rather than merely satisfied.
3. **`--check` verifies the asset against its script; nothing verifies the manifest against the asset's digest.** `lexicon_provenance` records `entry_count` but not a SHA-256. Adding a digest field would let one test assert the shipped bytes are the exact bytes the provenance describes, without reading 154 MB — a strictly cheaper and stricter check than P4.
4. **The deferred half is now the only thing standing between this whole and a clean close**: the `libretiles_PRD.md` correction (five lines), the `sowpods.txt` deletion behind it, and the `PRIMARY_DICTIONARY_FILE` disposition. All three are small; the PRD edit is the one that unblocks the other two, and it is also the fix for the "PRD matches no file in the tree" finding you verified.
5. **`hunspell` is now a hard build-time dependency of all three scripts, and `AGENTS.md` says so only as a version.** A contributor on a host without `hunspell` installed gets a clear failure, which is correct — but the Quick start section never mentions installing `hunspell`/`unmunch`, because until now nothing in the documented flow needed them. Whether that belongs in Quick start or stays a build-tool-only concern is a documentation-slice decision.

---

`Smallest next step:` land the deferred half in one exchange — correct the five `SOWPODS` lines in `libretiles_PRD.md` to Collins 2019, then `git rm backend/assets/dicts/sowpods.txt` with P14, requiring the `PRIMARY_DICTIONARY_FILE` value to be confirmed or explicitly accepted as unknown before the deletion.

`Report justification:` new-mutation

`Logical-whole closure: not-closed`

**Authority expiry:** my authority expires with this terminal report, and this `PASS` is non-independent implementation evidence that closes nothing — acceptance, publication and closure remain separate and ORCHESTRATOR-owned. I archived nothing and wrote nothing under `/home/agile/meta/`. No path was deleted; `backend/assets/` is byte-identical to the baseline and `sowpods.txt` is still tracked. No secret was read, no `.env` inspected, zero network requests were made, and no delegation occurred. Temporary state is confined to `/tmp/opencode/mle-v3c/` (537 MB → 197 MB after removing the four `unmunch` dumps and the altered copy; the six reproduced artifacts, three build logs and four CLASS B captures were kept as re-verifiable evidence), plus the reused read-only caches under `/tmp/opencode/mle-v3/`.

**Context pressure:** moderate. Three full prompt reads, one `AGENTS.md` read, three script edit passes and two full backend suites are held comfortably; no compaction occurred and there is clear headroom for the deferred exchange.

