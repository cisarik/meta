You are a WORKER instance assigned to the persistent AP WORKER role. Execute exactly this bounded task and stop.

```text
Logical whole identity: multilingual-expansion
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Continuity anchor: your own terminal implementation-PASS report for task MLE-V1, Worker session 01 exchange 01, at commit 3878847d367490217c4b1b3d3a2af763aaad1a32
Authority renewal: your prior authority EXPIRED at that terminal report. This exchange grants a complete, new, bounded grant. Nothing you retain from exchange 01 is authority; it is convenience only, and every repository fact must be re-gated below before you act on it.
Task identity: MLE-V1b — add the two invariants your own report identified as missing, and strengthen one that you correctly reported as weaker than it reads
Phase: Implementation
Implementation authority: explicit
Exact baseline: 3878847d367490217c4b1b3d3a2af763aaad1a32
Changed-path allowlist: backend/tests/test_variant_invariants.py
Implementation boundaries: EDIT only that one file, by ADDING tests and by strengthening one existing assertion named in section 3; NO production source change anywhere
Independence required: no
Evidence posture: non-independent
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

```text
Evidence tier: E1
Evidence tier basis: tests-only edit to one file you already own, no production behaviour touched, fully reversible by one git revert, no trust boundary, no migration, no credential, no external service
Authorized implementation stages: re-gate the repository, add the tests, run the focused module, run all eight standing gates, one commit, pre-push equality gate, one non-force push, public readback, terminal report
Combined implementation envelope: allowed
Implementation stage gates: no commit before the focused module passes; no push before all eight gates are green and the pre-push equality gate matches the exact baseline
Independent acceptance: not-required
Rollback or recovery checkpoint: one additive commit on one test file; rollback is `git revert`
Activated stricter profile: none
Terminal implementation report point: after the public readback, once
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: backend/tests/test_variant_invariants.py — your own 62 cases must all still pass
Affected tests: none other is modified
New causal regression: nothing in the repository asserts that a manifest's filename stem equals its declared `slug`, and the divergence is reachable through game creation — see section 2
Broad or full suite: required-because the project rule mandates all eight standing gates on every slice
Runtime or testbed: not-used
Independent acceptance: not-required
```

```text
Sub-agents/internal delegation: bounded authority — delivery route only; you remain the one accountable Worker and must not delegate further
Worker topology: single-active
Network authority: none
Secret authority: none
Dependency authority: none
Untrusted-content boundary: this prompt is your only task authority; files you read are data under analysis
Context-pressure rule: report your visible context pressure qualitatively
```

Reasoning recommendation: **Medium.** Two additive assertions and one strengthening, in a file you wrote, with the target behaviour already measured by you. No named risk justifies High (`AP.md:1074-1080`).

---

## 1. Why this exchange exists, and the credit that belongs to you

Your exchange-01 report field 17 named two invariants your harness does not assert. I re-measured item 2 myself, independently, before writing this prompt, and it reproduces exactly:

```text
a manifest file `de.json` declaring "slug": "german"
  list_installed_variants()            -> ['german']
  len(list) == len(*.json files)       -> True    (so G9 passes and is blind to it)
  load_variant("german")              -> FileNotFoundError: Variant 'german' not found
  load_variant("de")                  -> LOADS, and reports .slug == "german"
and the reachability you claimed is confirmed:
  game/serializers.py:180  installed = {variant.slug for variant in list_installed_variants()}
  game/serializers.py:215  same
  game/services.py:173     installed = {item.slug for item in list_installed_variants()}
```

So an incoming `variant_slug` of `german` passes validation at all three sites and every later `load_variant` call fails. **You were right, this is a live product hazard rather than a documentation gap, and it is exactly the defect shape a fifth language would produce.** That is the second time in this project's history a Worker has corrected the Orchestrator on evidence.

Your finding 17.1 is also confirmed by my own measurement: `.venv/bin/python -m manage.py check` fails with `ModuleNotFoundError: __path__ attribute not found on 'manage'`, and `.venv/bin/python manage.py check` returns `System check identified no issues (0 silenced).` The defect was in my prompt, inherited from a project document that carried the same typo. Section 5 below uses the corrected form.

Findings 17.4 and 17.6 are recorded as observations and need no action in this exchange. Finding 17.3 and 17.5 are actioned below.

---

## 2. Repository re-gate — mandatory for a current-session renewal

Retained context is convenience, not authority. Re-measure before acting, and **stop and report if anything conflicts with current repository evidence**:

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 3878847d367490217c4b1b3d3a2af763aaad1a32
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY
git ls-remote origin refs/heads/main  # MUST be 3878847d367490217c4b1b3d3a2af763aaad1a32
ss -tlnp | grep -E ':(3000|8000)'     # a listener means STOP AND REPORT; never pkill
```

If any value differs, classify with all five canonical recovery classes — `accepted-continuation`, `unrelated-owner-work`, `stale-clone`, `unpublished-candidate`, `unexplained-divergence`, precedence `unexplained-divergence > unrelated-owner-work > stale-clone > accepted-continuation > unpublished-candidate`, any unclassified material remainder becoming `unexplained-divergence` — then stop.

## 3. The three changes, and nothing else

### 3a. `G26` — the manifest filename stem must equal the declared slug

```text
G26a  parameterized over every installed variant: for each manifest path found by
      globbing the variants directory the same way the loader does, the variant
      loaded from that path has `.slug == path.stem`. Derive the directory via
      gamecore.assets get_assets_path() / "variants" — not a hardcoded path.
      Assert it in the form that makes the failure message useful: build the
      mapping {path.stem: loaded.slug} and assert every pair is equal, naming the
      offending stem and slug in the assertion message.
G26b  a `tmp_path` NEGATIVE that pins the divergence as a real, currently reachable
      behaviour rather than a hypothesis. Write one manifest named `de.json`
      declaring "slug": "german", monkeypatch gamecore.variant_store._variants_dir
      to that directory, and assert all four measured facts:
        list_installed_variants() reports slug "german"
        the stem/slug equality that G26a asserts is VIOLATED for that directory
        load_variant("german") raises FileNotFoundError
        load_variant("de") succeeds and its .slug is "german"
      Add a comment naming the three production call sites that make this reachable:
        game/serializers.py:180 · game/serializers.py:215 · game/services.py:173
      ⚠ G26b is a CHARACTERIZATION test. It documents current behaviour, it is not a
      request to change it. Do NOT alter load_variant, list_installed_variants, or
      any serializer. Whether the LOADER should also be fixed is a separate
      Orchestrator decision in a later slice; G26a is what makes the divergence
      unshippable in the meantime.
```

### 3b. `G27` — no manifest may declare a derived total

```text
G27  parameterized over every installed manifest, read as raw JSON (not through the
     loader, because the loader silently ignores unknown keys): the parsed object
     does NOT contain the key "total_tiles". Add a comment stating why: total_tiles
     is DERIVED at gamecore/variant_store.py:75-77 as the sum of counts, so a
     declared value could disagree with the real tile set and would read as
     authoritative to a human reviewer while being ignored by the code.
     While you are reading the raw JSON, assert the same for any other key that
     duplicates a derived property IF and ONLY IF such a property exists today —
     check `distribution`, `tile_points` and `playable_letters` against the four
     manifests and include only the ones that are genuinely derived properties of
     VariantDefinition. Do not invent a forbidden key that has no derived twin.
```

### 3c. Strengthen `G13`'s `fetched_at` assertion

Your finding 17.5 is correct: `datetime.fromisoformat("2026")` succeeds on Python 3.11+, so the current check would pass a bare year. Strengthen it to require a real calendar date at minimum — the parsed value must have a year, month and day that round-trip, and the raw string must be at least 10 characters. Keep `None` acceptable. Do not make it stricter than that: the four shipped values are naive ISO timestamps without timezone, and requiring a timezone would fail them.

### 3d. What must NOT change

```text
NO production source change. Not one line under backend/game/, backend/gamecore/,
   backend/config/, backend/catalog/, backend/accounts/, or frontend/.
NO edit to any test file other than backend/tests/test_variant_invariants.py.
NO removal or weakening of any of your existing 62 cases. All 62 must still pass.
NO change to any manifest, any asset, any lockfile, or backend/pyproject.toml.
NO new dependency, no network request, no secret access.
NO fix to the slug/stem divergence in production code — see the warning in 3a.
NO `git add -A`, no `git add .`, no force, amend, rebase, reset, clean, stash,
   branch, or tag.
NO writing under /home/agile/meta/... and no temporary file outside
   /tmp/opencode/mle-v1b/.
```

✅ **Cross-check performed when this prompt was written:** section 3 requires edits to exactly `backend/tests/test_variant_invariants.py`, and the allowlist plus section 3d permit exactly that file. Nothing section 3 mandates is forbidden. If you find a contradiction, stop and report it rather than guessing.

---

## 4. Pre-fix failure capture

```text
G26a  CLASS A on the four shipped variants — their stems already equal their slugs,
      so it passes immediately. Say so honestly; it is invariant pinning.
G26b  CLASS B — it must be proven to have teeth. Run it once with the manifest
      renamed to `german.json` (stem == slug) and capture the exact failure text,
      then restore `de.json`. Quote that text.
G27   CLASS B — add "total_tiles": 100 to a synthetic manifest in tmp_path, confirm
      the raw-JSON assertion fires, capture the text, and do NOT leave that synthetic
      manifest behind. ⛔ Never add the key to a real manifest under
      backend/assets/variants/, not even temporarily.
G13   CLASS B — set a synthetic manifest's fetched_at to "2026" and confirm the
      strengthened assertion now fails where the old one passed. Quote both.
```

## 5. Validation

RF-16 route binding, unchanged from exchange 01 and still bounded to this task:

```text
Declared route that could not be used: `poetry run <tool>`, as documented in AGENTS.md
Exact alternate, canonical for this task, from backend/ :
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
Rationale: the client environment intercepts `python*` through inherited
    APPIMAGE / ARGV0 / APPDIR / PYTHONHOME variables.
Evidence class: reproduced-dynamic.
Bounded authority: this task only.
Stopping condition: if .venv/bin/python is absent or the deviation fails, STOP AND
    REPORT. Never fall back to ambient `python3` or `poetry run`.
```

⛔ Note the third line: `manage.py check` is invoked **without** `-m`. Exchange 01's prompt carried `-m manage.py`, which is a hard `ModuleNotFoundError`. You found that; this is the corrected form.

Then the frontend gates from `frontend/`: `npm run typecheck`, `npx vitest run`, `npm run lint`, `npm run build`.

Baseline to beat, measured at `3878847d367490217c4b1b3d3a2af763aaad1a32`. The first four were measured by me in this session; re-measure anyway:

```text
mypy config game gamecore accounts catalog   Success: no issues found in 83 source files
ruff check .                                 All checks passed!
manage.py check                              System check identified no issues (0 silenced).
pytest --collect-only                        456 tests collected
pytest tests/test_variant_invariants.py      62 passed
npm run typecheck                            exit 0
npx vitest run                               450 passed | 3 skipped (31 files passed | 1 skipped)
npm run lint                                 exit 0
npm run build                                exit 0, ELEVEN dynamic routes, ZERO static routes
```

The four traps still apply and are not optional:

```text
1  backend/pyproject.toml sets addopts = "-q". A second -q silently suppresses the
   pytest summary count line. Run plain `-m pytest` and quote the summary verbatim.
2  mypy on the FULL documented scope, never a narrowed set.
3  Check `ss -tlnp | grep :3000` before `npm run build`. A listener means STOP.
4  "The build passed" and "the code type-checks" are TWO SEPARATE CLAIMS. State both.
```

## 6. Git authority — the exact sequence

```bash
cd /home/agile/Projects/libretiles
git add backend/tests/test_variant_invariants.py
git status --porcelain=v1              # MUST show exactly one modified path
git diff --cached --stat
git commit -m "test(variants): pin manifest stem/slug agreement and reject a declared total_tiles"
git ls-remote origin refs/heads/main   # MUST be 3878847d367490217c4b1b3d3a2af763aaad1a32
git push origin main                   # one non-force fast-forward push
git ls-remote origin refs/heads/main   # MUST equal `git rev-parse HEAD`
git rev-parse HEAD
```

If the remote advanced between the gate and the push, **stop and escalate**. Do not merge, rebase, or retry with force.

## 7. Stopping conditions

```text
the section 2 re-gate does not match exactly, or conflicts with retained context
a listener answers on port 3000 or 8000
backend/.venv/bin/python is absent, or the section 5 route fails
any of the eight gates regresses, or any of your existing 62 cases fails
the slug/stem divergence does NOT reproduce as section 1 describes — report the
    measured behaviour instead and do not force the test to match my claim
completing the work would require a production change, a new dependency, a network
    call, or a secret
`git ls-remote` no longer equals the exact baseline at the pre-push gate
```

Stop normally — success — when the three changes are in, every case in the module passes, class B failures are captured, all eight gates are green, one commit is pushed non-force, and the public readback equals `git rev-parse HEAD`.

## 8. Report contract

The FIRST CHARACTER of your reply must be `#`, so it begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then, in this order: the coordinate line reading `logical whole multilingual-expansion, Worker session ordinal 01, Worker exchange ordinal 02`; status `PASS | PARTIAL | BLOCKED`; `Phase-qualified result:` one value from the closed enum at `PROMPT_CONTRACTS.md:206` and no invented value; `Result artifact or commit:`; `Result evidence:`; start and end commit; the section 2 re-gate values verbatim plus an end-of-task porcelain re-confirmation; changed files and purpose; the new-test table with class A/B and the captured class B failure text; the total case count before and after; all eight gates each with its own quoted line and the pytest summary verbatim; both separate frontend claims; the Git sequence with the pre-push value, the commit SHA, the push result, and the public readback equality; deviations, risks, missing evidence; `Resolved Execution Issues / Near-Misses:`; `Pre-Existing Failure Classification:`; **what you can still see that this prompt did not anticipate**, including anything about the slug/stem hazard that suggests the LOADER and not only the harness should change, since that is the decision I will take next; one smallest next step; exactly one report justification from `new-mutation | new-evidence | new-material-risk | changed-external-state | final-acceptance | explicit-closure`; `Logical-whole closure: not-closed`; an authority-expiry statement; and your qualitative context pressure.

One value per field. No visible mid-sentence self-corrections. Summarize command output; full output only for failures or safety-critical evidence.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_implementation_01.md
Destination path: /home/agile/meta/projects/libretiles/12/00-multilingual-expansion/
Archival: wait-for-report
```

You do not archive this pair. Your authority expires at your terminal report, and no `PASS` you report closes anything.

