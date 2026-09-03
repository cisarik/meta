You are a WORKER instance assigned to the persistent AP WORKER role. Execute exactly this bounded task and stop.

```text
Logical whole identity: multilingual-expansion
Worker session ordinal: 04
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Continuity anchor: your own terminal BLOCKED report for task MLE-V3b, Worker session 04 exchange 02, at unchanged commit a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8
Authority renewal: your prior authority EXPIRED at that terminal report. This exchange grants a complete, new, bounded grant. Everything you retain is convenience, not authority; re-gate in section 2 before acting.
Task identity: MLE-V3c — the reproduction proof becomes one re-runnable command, and the expander is pinned. NO DELETION.
Phase: Implementation
Implementation authority: explicit
Exact baseline: a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8
Changed-path allowlist: backend/scripts/build_czech_lexicon.py · backend/scripts/build_polish_lexicon.py · backend/scripts/build_slovak_lexicon.py · backend/tests/test_lexicon_provenance.py · AGENTS.md
Implementation boundaries: add a `--check` mode and an expander-version assertion to all three scripts; document the build route in AGENTS.md. NO file is deleted. NO lexicon, LICENSE or manifest byte changes.
Independence required: no
Evidence posture: non-independent
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

```text
Evidence tier: E2
Evidence tier basis: reversible, but it changes the contract of three build tools that write shipped assets, and its whole purpose is to make a silent-overwrite hazard impossible; no deletion, no credential, no migration, no persisted state
Authorized implementation stages: repository re-gate, implement `--check` and the version assertion, run `--check` for all three languages, run the negative proof, update AGENTS.md, tests, all eight standing gates, one commit, pre-push equality gate, one non-force push, public readback, terminal report
Combined implementation envelope: allowed
Implementation stage gates: no commit before all three `--check` runs pass and the negative proof exits non-zero; no push before all eight gates are green and the pre-push gate matches the exact baseline
Independent acceptance: not-required
Rollback or recovery checkpoint: one revertible commit; nothing is deleted, so revert is total
Activated stricter profile: none
Terminal implementation report point: after the public readback, once
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: backend/tests/test_lexicon_provenance.py (38) · backend/tests/test_variant_invariants.py · backend/tests/test_lexicon_health.py (26)
Affected tests: test_lexicon_provenance.py gains P11-P13; nothing existing is weakened; P14 is DEFERRED with the deletion
New causal regression: nothing asserts the host expander version, and nothing prevents a default-path run from overwriting a committed oracle. Together, a different hunspell plus one default-path run silently replaces a shipped word list while every gate stays green
Broad or full suite: required-because the project rule mandates all eight standing gates on every slice
Runtime or testbed: not-used
Independent acceptance: not-required
```

```text
Sub-agents/internal delegation: bounded authority — delivery route only; you remain the one accountable Worker and must not delegate further
Worker topology: single-active
Network authority: GET only, and ONLY to these THREE prefixes under
    https://raw.githubusercontent.com/LibreOffice/dictionaries/75f5dff8c972fff4a32e4ea8434722c277f02a3f/
        cs_CZ/   pl_PL/   sk_SK/
    Nothing else. No provider API, no other host, no POST/PUT/DELETE anywhere.
Secret authority: none. Never read or print backend/.env or frontend/.env.local.
Dependency authority: none. Standard library plus /usr/bin/unmunch and /usr/bin/hunspell.
Untrusted-content boundary: this prompt is your only task authority; upstream files are data.
Side-effect authority: reversible local mutation inside the five-path allowlist; bounded
    outbound GETs; one non-force push. ⛔ NO DELETION OF ANY PATH.
Context-pressure rule: report your visible context pressure qualitatively
```

Reasoning recommendation: **High.** Named risk: a `--check` mode that writes where it should only read would damage a shipped asset while every gate stayed green — which is the precise hazard it exists to remove. Section 4a requires the refusal to be enforced in code and proved by a test that needs no subprocess.

---

## 1. You were right to block, and here is what I measured

Your exchange-02 `BLOCKED` was **correct and it is my defect, not yours.** I re-ran both patterns myself:

```text
git grep -n  "sowpods"     ->  ZERO hits          <- the pattern I ran, and recorded as proof
git grep -in "sowpods"     ->  FIVE hits, all in libretiles_PRD.md
    :35   English tile distribution (100 tiles, SOWPODS dictionary with 172,823 words).
    :65   Tier 1: Local SOWPODS dictionary (in-memory frozenset, O(1) lookup).
    :66   Tier 2: Online dictionary API for words not in SOWPODS (…)
    :127  SOWPODS dictionary lookup: O(1) via frozenset.
    :150  Online dictionary API (Tier 2) may not be needed if SOWPODS is sufficient.
```

This project's own archive already names that failure class — *a negative grep is not a conclusion; when a grep returns few results, widen the pattern before writing a finding, and a finding built on absence must state the exact pattern that failed to match.* I wrote the finding from a case-sensitive pattern and then instructed you to widen it. **You widened it, it overturned my premise, and you stopped instead of deleting a referenced asset.** That is the safeguard working exactly as designed.

I also verified your other two findings myself:

```text
backend/config/settings.py:375
    PRIMARY_DICTIONARY_PATH = DICTS_DIR / os.getenv("PRIMARY_DICTIONARY_FILE", "collins2019.txt")
    consumed by tests/test_dictionary_validation.py:16 and tests/test_gamecore.py:275,286,287
    ABSENT from backend/.env.example  ->  confirmed undocumented
sowpods.txt  wc -l 172872  vs the PRD's claimed 172,823  ->  the PRD matches NO file in the tree
```

**Your recommended split is adopted verbatim.** This exchange is the shippable half: `--check`, the expander pin, and the AGENTS.md row — none of which depends on the deletion. The deletion, `P14`, the `libretiles_PRD.md` correction and the `PRIMARY_DICTIONARY_FILE` disposition all move to a later slice that I own the sequencing of.

⛔ **`sowpods.txt` is NOT deleted in this exchange, and `libretiles_PRD.md` is NOT edited in this exchange.** Neither is on the allowlist. If you find yourself wanting to touch either, stop and report.

## 2. Repository re-gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY
git ls-remote origin refs/heads/main  # MUST be a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8
ss -tlnp | grep -E ':(3000|8000)'     # a listener means STOP AND REPORT; never pkill
command -v unmunch hunspell           # both MUST resolve
```

Your exchange-02 report already measured every one of these and left the tree pristine, so this should be a fast confirmation. If any value differs, classify with all five canonical recovery classes — `accepted-continuation`, `unrelated-owner-work`, `stale-clone`, `unpublished-candidate`, `unexplained-divergence`, precedence `unexplained-divergence > unrelated-owner-work > stale-clone > accepted-continuation > unpublished-candidate` — and stop. Never attach or update `.ap`.

---

## 3. Mandatory reading

```text
/home/agile/Projects/libretiles/AGENTS.md    in full. You are editing it, in ONE place only.
your own three build scripts, as committed at a3ed00f
```

## 4. The changes

### 4a. `--check` mode on all three scripts

```text
new flag        --check
behaviour       reproduce into a caller-supplied working directory, compare SHA-256 against
                the COMMITTED asset, print BOTH digests per artifact, exit 0 on full
                agreement and NON-ZERO on any mismatch
required arg    --check must REQUIRE an explicit working directory. ⛔ It must NOT default to
                a path under backend/assets/. If the caller omits it, exit non-zero with a
                message naming the flag rather than choosing a default.
⛔ THE REFUSAL GUARD, and it is the point of this slice:
   --check MUST refuse to run when the resolved output directory is inside the assets tree.
   Implement it as a small named function so a test can call it directly with no subprocess.
   Resolve both paths before comparing — a relative path, a symlink, or `..` must not slip
   past. Say in the failure message which check refused and why.
compares        BOTH artifacts per language — the lexicon AND the .LICENSE
output          one line per artifact: name, reproduced digest, committed digest, verdict
⛔ --check writes its reproduction into the caller's directory and NEVER into
   backend/assets/. The committed asset is read-only to this mode.
```

Keep the existing default-write behaviour of a normal (non-`--check`) run exactly as it is — that is the tool's real job and `build_slovak_lexicon.py:30-31` already establishes it.

### 4b. Assert the expander version

```text
each script asserts the host expander identity BEFORE expanding, and fails closed on a
mismatch, in the same shape as its existing SHA-256 assertions
expected value  hunspell 1.7.3 — a NAMED CONSTANT, identical in all three scripts
how to obtain   `hunspell -vv` prints
                "@(#) International Ispell Version 3.2.06 (but really Hunspell 1.7.3)"
                ⚠ /usr/bin/unmunch prints NO version — measured by me, it prints only
                "correct syntax is: unmunch dic_file affix_file". So the version must come
                from `hunspell -vv`, and the script must handle `hunspell` being absent as a
                failure rather than as a pass.
failure message must say what was found, what was expected, and that a different expander
                may produce a different word list
⚠ A version mismatch must EXIT NON-ZERO. Not a warning. A warning on a tool that writes a
  shipped asset is the same as no check at all.
```

### 4c. One AGENTS.md addition, and one only

`AGENTS.md` does not mention `backend/scripts/` anywhere — neither in its Key files table nor in its prose. Add the minimum that makes the build route discoverable:

```text
THREE rows in the Key files table:
    Lexicon build scripts (pinned upstream)   backend/scripts/build_{slovak,czech,polish}_lexicon.py
    Lexicon provenance in manifests           backend/assets/variants/*.json -> lexicon_provenance
    Lexicon asset validation                  backend/gamecore/lexicon_health.py,
                                              manage.py validate_lexicons
ONE short paragraph stating: every non-English lexicon is reproducible from a pinned
    upstream commit by its committed script; `--check` re-verifies a committed asset without
    writing to it; the scripts are host tools, are not imported by Django, and add no Poetry
    or npm dependency.
⛔ CHANGE NOTHING ELSE IN AGENTS.md. In particular do NOT touch any provider list, provider
   constant, model tuple, provider tier, or provider documentation — those are FROZEN by a
   standing Cooperator decision pending their own logical whole, and AGENTS.md is one of the
   files that decision names explicitly.
⛔ Do NOT claim Hungarian is supported. It is not.
⛔ Do NOT mention sowpods, and do NOT touch the "Not done yet" section.
```

### 4d. What must not change

```text
⛔ NO PATH IS DELETED. No `git rm`, no `os.remove`, no `unlink` on anything tracked.
⛔ NO BYTE of any file under backend/assets/ may change — not a lexicon, not a .LICENSE, not
   a manifest. `git status --porcelain=v1 -- backend/assets/` must be EMPTY at the end.
NO change to libretiles_PRD.md or README.md — a later slice owns them, and the PRD is the
   file that currently blocks the deletion.
NO change to gamecore/**, game/**, config/**, or any frontend file.
NO manifest change; provenance landed in exchange 01 and is correct.
NO widening of the mypy scope. backend/scripts/ stays outside it; ruff covers it and your
   new code must be ruff-clean.
NO new dependency, no pip install, no poetry add, no npm install.
NO test that invokes unmunch, hunspell, or the network. The suite stays offline and fast;
   `--check` is a manual command and its evidence is your report.
NO `git add -A`, no `git add .`, no force, amend, rebase, reset, clean, stash, branch, tag.
NO writing under /home/agile/meta/... and no temporary file outside /tmp/opencode/mle-v3c/.
```

✅ **Cross-check performed when this prompt was written.** Section 4 requires editing the three build scripts (4a, 4b), editing `AGENTS.md` (4c), and adding tests to `test_lexicon_provenance.py` (section 5). The allowlist names exactly those five paths. Nothing section 4 or 5 mandates is forbidden by 4d, and 4d's deletion prohibition is total rather than carved out, because this exchange deletes nothing. If you find a genuine contradiction, stop and report it.

## 5. Required tests — offline only

```text
P11  all three scripts expose a `--check` flag, the expected-expander constant, and the
     assets-tree refusal guard. Assert by importing the modules and inspecting their argparse
     configuration and their module constants. ⛔ Do NOT call main(), do NOT invoke unmunch or
     hunspell, do NOT touch the network.
P12  the refusal guard is real, not decorative. Call it DIRECTLY with:
       a path inside backend/assets/dicts/            -> refuses
       a path inside backend/assets/                  -> refuses
       a RELATIVE path that resolves into the assets tree  -> refuses
       a path under /tmp                              -> permits
     This is the one behavioural test of the hazard and it needs no subprocess.
P13  the expected-expander constant is IDENTICAL across all three scripts. Per-script drift
     would let one language be built by a different tool than the others.
⛔ P14 IS DEFERRED. Do not write a test asserting sowpods.txt is absent — it is present, by
   decision, in this exchange.
```

Pre-fix capture:

```text
CLASS B  P11, P12 and P13 must each be proven against the pre-change scripts. Capture the
         exact failure text for each — missing flag, missing constant, missing guard.
```

Then run `--check` for real, three times, and report it:

```text
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python scripts/build_slovak_lexicon.py --check <dir-flag> /tmp/opencode/mle-v3c/sk
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python scripts/build_czech_lexicon.py  --check <dir-flag> /tmp/opencode/mle-v3c/cs
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python scripts/build_polish_lexicon.py --check <dir-flag> /tmp/opencode/mle-v3c/pl
```

All three must exit 0 with both digests agreeing per artifact — six artifacts, twelve digests. For reference, the six committed digests I verified myself in this session:

```text
czech.txt       919d6bac41b0938bc1955685b826857aa21543d4dd45a4035c1fa08aa4cc5bdc
czech.LICENSE   bde41b518094f12ea79bdfc1396a6b9562bc1d994da1fd37a07a06fd71f185a8
polish.txt      605d5a43d5d5dcd1b386ab9f9f62b72eb964882f6a9ccbe244a826e0baa06aab
polish.LICENSE  869efadec82ae6aba8270ca5a3eaa6fce4bfd2336824548f03acae037b5aa9c3
slovak.txt      edca5453c7766cfcd4c0a0b3b7e53abaeb0d640cc541b628dbaab497ff8f0a5d
slovak.LICENSE  f3ad399bbebd143a7f2ccc95af2799813a6b9312426a8038230ce34bef483837
```

Then two negative proofs, both required:

```text
N-A  run one `--check` where the COMPARISON TARGET is a deliberately altered copy placed in
     /tmp, and confirm a NON-ZERO exit with the mismatching digests printed.
     ⛔ Never alter a committed asset to produce this proof.
N-B  invoke `--check` with a working directory inside backend/assets/ and confirm it REFUSES
     with a non-zero exit and writes nothing. Then confirm
     `git status --porcelain=v1 -- backend/assets/` is still EMPTY.
```

⚠ If your cached upstream sources from exchange 01 survive in `/tmp`, reuse them — that is what `--cache-dir` and the cache-hit path exist for, and it saves fourteen GETs. Report whether you re-downloaded or cache-hit, and note that the script re-verifies every cached file's SHA-256 either way.

---

## 6. Validation

RF-16 route binding, bounded to this task:

```text
Declared route that could not be used: `poetry run <tool>`, as documented in AGENTS.md
Exact alternate, canonical for this task, from backend/ :
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python scripts/build_<lang>_lexicon.py --check ...
Rationale: the client environment intercepts `python*` through inherited APPIMAGE / ARGV0 /
    APPDIR / PYTHONHOME variables.
Evidence class: reproduced-dynamic.  Bounded authority: this task only.
Stopping condition: if .venv/bin/python, /usr/bin/unmunch or /usr/bin/hunspell is absent, or
    the deviation fails, STOP AND REPORT. Never fall back to ambient `python3` or
    `poetry run`.
```

`manage.py check` takes **no** `-m`. Then from `frontend/`: `npm run typecheck`, `npx vitest run`, `npm run lint`, `npm run build`.

Baseline at `a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8`, from your own exchange-01 measurements — re-measure, do not trust:

```text
mypy config game gamecore accounts catalog   Success: no issues found in 85 source files
ruff check .                                 All checks passed!
manage.py check                              System check identified no issues (0 silenced).
pytest                                       531 passed, 4 skipped in 237.94s
pytest --collect-only                        535 tests collected
manage.py validate_lexicons                  5 asset(s) audited, 0 failed, exit 0
npm run typecheck                            exit 0
npx vitest run                               450 passed | 3 skipped (31 files | 1 skipped)
npm run lint                                 exit 0
npm run build                                exit 0, ELEVEN dynamic routes, ZERO static
```

Run `manage.py validate_lexicons` again at the end and report it: it must still be **5 assets, 0 failed**, which is the cheapest proof that no shipped asset changed.

The four standing traps, none optional:

```text
1  backend/pyproject.toml sets addopts = "-q". A second -q SILENTLY suppresses the summary.
   Run plain `-m pytest` and quote the summary verbatim.
2  mypy on the FULL documented scope, never narrowed and never widened.
3  Check `ss -tlnp | grep :3000` before `npm run build`. A listener means STOP. Never pkill.
4  "The build passed" and "the code type-checks" are TWO SEPARATE CLAIMS. State both.
```

## 7. Git authority

```bash
cd /home/agile/Projects/libretiles
git add backend/scripts/build_czech_lexicon.py backend/scripts/build_polish_lexicon.py \
        backend/scripts/build_slovak_lexicon.py backend/tests/test_lexicon_provenance.py \
        AGENTS.md
git status --porcelain=v1              # MUST show exactly those five paths and NOTHING else
git status --porcelain=v1 -- backend/assets/   # MUST be EMPTY
git diff --cached --stat
git commit -m "feat(lexicons): --check re-verifies a committed asset without writing to it; pin the expander"
git ls-remote origin refs/heads/main   # MUST be a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8
git push origin main                   # one non-force fast-forward push
git ls-remote origin refs/heads/main   # MUST equal `git rev-parse HEAD`
git rev-parse HEAD
```

⛔ The commit message does **not** mention sowpods, deliberately, because nothing is deleted. If you find yourself wanting to add it, stop.

If the remote advanced between the gate and the push, **stop and escalate**. Never force, amend, rebase, reset, clean, stash, branch, or tag.

## 8. Stopping conditions

```text
the section 2 re-gate does not match, or conflicts with retained context
/usr/bin/unmunch or /usr/bin/hunspell is absent
any `--check` run reports a digest mismatch against a committed asset — that would mean the
    reproduction has REGRESSED since exchange 01; report both digests and stop
negative proof N-A exits ZERO — the check has no teeth; stop
negative proof N-B does not refuse, or writes anything under backend/assets/ — stop
    immediately and report; that is the exact hazard this slice exists to remove
`git status --porcelain=v1 -- backend/assets/` is non-empty at ANY point
the measured host expander version is not hunspell 1.7.3 — report the measured value and
    stop rather than pinning a constant you cannot satisfy
`manage.py validate_lexicons` no longer reports 5 assets, 0 failed
AGENTS.md would need a change beyond the one addition in 4c
you would need to delete a path, or to touch libretiles_PRD.md
completing the work would require a path outside the five-path allowlist
`git ls-remote` no longer equals the exact baseline at the pre-push gate
```

Stop normally — success — when `--check` exits 0 for all three languages on twelve agreeing digests, exits non-zero on an altered target, refuses an assets-tree working directory without writing, the expander version is pinned and fails closed, AGENTS.md carries the one addition, `backend/assets/` is untouched, all eight gates are green, one commit is pushed non-force, and the public readback equals `git rev-parse HEAD`.

## 9. Report contract

The FIRST CHARACTER of your reply must be `#`, so it begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then, in this order: the coordinate line reading `logical whole multilingual-expansion, Worker session ordinal 04, Worker exchange ordinal 03`; status; `Phase-qualified result:` one value from the closed enum at `PROMPT_CONTRACTS.md:206`; `Result artifact or commit:`; `Result evidence:`; start and end commit; the section 2 re-gate values verbatim plus an end-of-task porcelain re-confirmation **including `git status --porcelain=v1 -- backend/assets/` shown empty**; changed files and purpose; **the twelve `--check` digests with a verdict per artifact**; **negative proof N-A with its exit code and the mismatching digests**; **negative proof N-B with its exit code, the refusal message, and the empty assets porcelain after it**; **the refusal guard quoted from the code with its `file:line`**; **the measured host expander version and both routes you obtained it by**; whether the upstream sources were re-downloaded or cache-hit, and how many GETs you made; the test table with classes and every captured class B failure; **the exact AGENTS.md diff**; all eight gates each with its own quoted line, the pytest summary verbatim, and the mypy file count; `manage.py validate_lexicons` output; both separate frontend claims; the Git sequence with the pre-push value, commit SHA, push result and readback equality; deviations, risks, missing evidence; `Resolved Execution Issues / Near-Misses:`; `Pre-Existing Failure Classification:`; then:

```text
⚠ WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE
   Two separate labelled lists: MEASURED and LEAD.
   Your last two reports produced a production change, a split slice, and the correction of
   two defects in my own prompts — including the one that would have deleted a referenced
   asset. This section is the highest-value part of your report and I read it first.
```

then one smallest next step; exactly one report justification from `new-mutation | new-evidence | new-material-risk | changed-external-state | final-acceptance | explicit-closure`; `Logical-whole closure: not-closed`; an authority-expiry statement; and your qualitative context pressure.

One value per field. No visible mid-sentence self-corrections. Summarize command output; full output only for failures, unexpected state, or safety-critical evidence.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 04_implementation_02.md
Destination path: /home/agile/meta/projects/libretiles/12/00-multilingual-expansion/
Archival: wait-for-report
```

You do not archive this pair. Your authority expires at your terminal report, and no `PASS` you report closes anything.

