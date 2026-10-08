Everything verified. Writing the terminal report.

### Report for ORCHESTRATOR_CHAT

**Logical whole:** `kronika-sole-identity` · **Worker session:** 21 · **Exchange:** 01
**Report justification:** `new-mutation`
**Commit:** `6e89328640fe5477e08f17f4c31c9fc4bf261238` on local `main`, parent `0eb6e8e562e6c22c3de4038105b84689e9b1c76b`. Not pushed. Local `main` is 3 ahead of public `main` (`e1d5ee5`). Tree clean, submodule unmoved at `73e20ef80b88700d5fcbc397cd8edd4fc425869f`.

**Client disclosure:** none; this client emitted no prose above the header.

---

## 1. The derivation, and its reconciliation with the confirmed inventory

**Method — parsing, not reading.** Four throwaway pytest probes under `/tmp/opencode/ksi21/`, all run through `./.ap/ap exec --operation test-focus`. Each parses all **300** tracked Python modules under `tests/` with `ast`, collects every string literal and f-string containing the retired word case-insensitively, and classifies it by the rule below. Two of the four probes were discarded as defective; §"Resolved Execution Issues" records both.

**The rule, stated in full, applied mechanically:**

```text
moved-name   (a) in a logging context -- a logging.getLogger(...) or
 caplog.at_level(..., logger=...) argument, or a value compared
                against a record .name attribute -- and the value is exactly
                "framenest" or starts with "framenest.";
            (b) the key of a subscript into a formatters / handlers / filters /
                loggers section;
            (c) names a path under src/ -- "src/framenest..." anywhere in the
                value, or "framenest/..." as a Path/glob argument.
frozen-name  the value names a FrameNest* class.
unrelated    everything else.
```

| Category | Before (HEAD `0eb6e8e`) | After (`6e89328`) |
|---|---|---|
| moved-name | **16** | **0** |
| frozen-name | **75** | **75** |
| unrelated | 1092 | 1092 |
| total literal sites | 1183 | 1167 |

**Occurrence reconciliation, independent of the rule** (rule 8 — regenerated, not transcribed):

```text
Python modules under tests/, ledger excluded   1564 -> 1548   (-16)
JavaScript files under tests/                    277 ->   277   (unchanged)
tests/browser/*.sh, tests/support/*.json|html     10 ->    10   (unchanged)
                                                         -------
tests-tree total 1851 -> 1835
```

That is **exactly** the ledger's Part C `tests` pin, 1851, and exactly my new pin, 1835. The file count reconciles the same way: 162 Python + 20 JavaScript + 2 fixture files = **184**, the old `tests` file pin.

**16 moved sites → 37 failures.** Sites and the failures each one actually causes:

| # | Site | Old → new | Failures |
|---|---|---|---|
| 1 | `unit/test_structured_logging.py:24` | `Path("src/framenest")` → `Path("src/kronika")` | **0 — latent** |
| 2 | `unit/test_structured_logging.py:40` | `getLogger("framenest")` → `"kronika"` | 23 |
| 3 | `unit/test_configuration.py:297` | `getLogger("framenest")` → `"kronika"` | 1 |
| 4 | `unit/test_server_runtime.py:25` | `Path("src/framenest")` → `Path("src/kronika")` | **0 — latent** |
| 5 | `unit/test_server_runtime.py:185` | `["framenest_json"]` → `["kronika_json"]` | 1 |
| 6 | `contract/test_uvicorn_logging.py:77` | `["framenest_json"]` → `["kronika_json"]` | 1 |
| 7 | `contract/test_uvicorn_logging.py:78` | `["framenest_redaction"]` → `["kronika_redaction"]` | **0 — masked by #6** |
| 8 | `contract/test_uvicorn_logging.py:89` | `["framenest_stderr"]` → `["kronika_stderr"]` | 1 |
| 9 | `contract/test_uvicorn_logging.py:150` | `["framenest_json"]` → `["kronika_json"]` | 1 |
| 10 | `contract/test_public_published_uds.py:620` | `record.name == "framenest.public_published_api"` → `kronika.` | 1 |
| 11 | `contract/test_public_published_uds.py:636` | `at_level(..., logger="framenest.public_published_application")` → `kronika.` | 1 (shared) |
| 12 | `contract/test_public_published_uds.py:641` | `record.name == "framenest.public_published_application"` → `kronika.` | (shared) |
| 13 | `contract/test_workspace_media.py:632` | `/ "src/framenest"` → `/ "src/kronika"` | 1 |
| 14 | `contract/test_kronika_product_string_agreement.py:22` (module docstring) | ``src/framenest`` → ``src/kronika`` | **0 — prose** |
| 15 | `contract/test_kronika_product_string_agreement.py:163` | `glob("framenest/**/*.py")` → `kronika/**` | 4 |
| 16 | `contract/test_kronika_product_string_agreement.py:378` | `glob("framenest/**/alembic_environment/versions/*.py")` → `kronika/**` | 1 (shared) |

23 + 1 + 1 + 3 + 2 + 1 + 5 = **36**, plus the settings-parity failure = **37**. Every failing test is attributed; no unexplained remainder. Three sites fail nothing and one is masked — the four the sample list could not have found.

**Sites the issued sample did not name:** #1 and #4 (both `SOURCE_ROOT` constants), #7, #14, and the whole product-string-inventory residue in §3.

## 2. What the two latent sites actually were — the strongest finding of this cut

`tests/unit/test_structured_logging.py:24` and `tests/unit/test_server_runtime.py:25` name a directory that no longer exists, and four whole-tree guards iterate it:

```text
tests/unit/test_structured_logging.py:419  test_no_third_party_structured_logging_module_imported
tests/unit/test_structured_logging.py:436  test_production_logging_imports_confined_to_structured_logging_module
tests/unit/test_server_runtime.py:295      test_production_uvicorn_imports_are_confined_to_server_module
tests/unit/test_server_runtime.py:367      test_fastapi_imports_remain_confined_to_adapters_api
```

None of the four is in the 37-failure list, because `rglob` over a missing directory yields nothing and the loops assert `violations == []` over zero files. **All four have been passing vacuously since C3-B.** They are green again for the right reason now, and they will fail for real if the confinement is ever broken.

## 3. A second C3-B residue, found by running the derivation to its conclusion

After the glob at site #15 was repointed, four tests in `test_kronika_product_string_agreement.py` stayed red for a **second, different** cause. Measured, not inferred:

```text
unexpected = [('src/kronika/configuration.py', 'validate_ingress_configuration', 'Constant', 0),
              ('src/kronika/configuration.py', 'validate_private_storage_roots',  'Constant', 1),
              ('src/kronika/structured_logging.py', '_is_kronika_settings',       'Constant', 0)]
missing    = []
changed    = []
measured total53 against pinned 50; duplicates gained {'KronikaSettings': 3}
```

All three measured values are `'KronikaSettings'`, and all three are consequences of C3-B's own class rename: two `-> "KronikaSettings"` return annotations, and `structured_logging.py:244`'s `cls.__name__ == "KronikaSettings"` redaction identity check. Before the rename they read `FrameNestSettings`, which does not contain the brand word, so the inventory never saw them. No pinned row moved — `missing` and `changed` are both empty.

**Judgement, stated plainly.** By that module's own stated rule — *"every brand-bearing runtime string node"* — these three are occurrences it owns, so I pinned them (three rows, `OCCURRENCE_COUNT` 50 → 53, `IN_SCOPE_OCCURRENCE_COUNT` 48 → 51, `EXPECTED_DUPLICATE_LITERALS` gains `"KronikaSettings": 3`) and documented the settings class name as a scope note. This strictly **increases** coverage: a later cut that renames the class without updating the redaction filter now fails here instead of silently changing which settings objects are redacted. **The alternative — teaching the guard to skip annotations and class-name literals — is a semantic change to a contract test and an Orchestrator decision I did not take.** It is the one thing in this cut I would expect you to overturn, and it is five lines to revert.

## 4. The narrowed settings-parity assertion

```python
# before
assert pydantic_settings.VERSION == locked.group(1)
assert _git_blob(RESTORATION_REFERENCE, "poetry.lock") == _git_blob("HEAD", "poetry.lock")
assert _git_blob(RESTORATION_REFERENCE, "pyproject.toml") == _git_blob("HEAD", "pyproject.toml")

# after
assert pydantic_settings.VERSION == locked.group(1)
assert _git_blob(RESTORATION_REFERENCE, "poetry.lock") == _git_blob("HEAD", "poetry.lock")
assert _declared_requirement(
    _git_blob(RESTORATION_REFERENCE, "pyproject.toml"), SETTINGS_LIBRARY
) == _declared_requirement(_git_blob("HEAD", "pyproject.toml"), SETTINGS_LIBRARY)
```

`SETTINGS_LIBRARY = "pydantic-settings"`. The helper parses both manifests with `tomllib`, selects the one entry in `[project] dependencies` whose distribution name matches, asserts there is exactly one, and returns it verbatim — constraint, extras and markers included.

**Why the narrower form still proves the library is unchanged.** The library pin has three independent legs and all three remain: the lockfile is byte-identical, so every resolved version — including `pydantic-settings` — is fixed; the declared requirement is unchanged, so the manifest does not widen or narrow the range the lock may resolve; and the installed `pydantic_settings.VERSION` equals the locked version. The removed part pinned three things the test never claimed and ADR-0085 legitimately changed: `[project] name`, the console-script table and the packaging include list.

**Negative control — the pin is live, not tautological** (throwaway probe, real output):

```text
REFERENCE_REQUIREMENT                'pydantic-settings (>=2.14.2,<3.0.0)'
HEAD_REQUIREMENT                     'pydantic-settings (>=2.14.2,<3.0.0)'
WHOLE_MANIFEST_BYTE_IDENTICAL        False
MUTATED_REQUIREMENT (>=2.15.0)       NARROWED_PIN_REJECTS_BUMP          True
distribution-name-only change        NARROWED_PIN_ACCEPTS_DISTRIBUTION_RENAME  True
```

It rejects a version bump and accepts the rename C3-B made. A removed or renamed requirement is caught by the helper's own exactly-one assertion — that leg is code inspection plus the printed fact that the fixture removed the entry, not an executed demonstration.

## 5. Explicit confirmations

- **`RESTORATION_REFERENCE` untouched** — `git show HEAD:…` line 57: `RESTORATION_REFERENCE = "18c357cf6f8c5ff9cc3b2c28e638510fc73a3672"`. The diff contains no `+`/`-` line mentioning it.
- **`poetry.lock` byte-identity assertion untouched** — HEAD line 279 is the original statement verbatim; it is not in the diff.
- **First two assertions untouched** — HEAD line 278 `assert pydantic_settings.VERSION == locked.group(1)` and line 279 are unchanged; only line 280 onward differs. Nothing was deleted, skipped, marked or xfailed.
- **`FrameNest*` class names untouched** — the derivation counts **75** frozen-name sites before and after, and `git diff` contains no added or removed line containing a `FrameNest…(` reference. Deliberately left alone: `FrameNestJsonFormatter` at `test_uvicorn_logging.py:77,150` and `test_server_runtime.py:186`; `FrameNestRedactionFilter` at `test_uvicorn_logging.py:78` and the `test_public_published_uds.py` import; the deliberately dual-spelled `"The FrameNest or Kronika mutation header…"` row at `test_kronika_product_string_agreement.py:181`; the `X-FrameNest-Request` header literals (C7-A); the ledger's own `FrameNestSettings` provenance comments at lines 1046/1057/1066/378; and 72 bare `FrameNest` mentions in module docstrings.
- **Ledger token and pins untouched** — the 5 ledger sites my first rule over-collected (its own `"framenest"` search token at lines 1202/1231/1245/1261 and the Part B `"framenest"` launcher pin at 181) were opened and left alone.
- **Negative assertions left alone** — `test_media_content_api.py:169`, `test_local_web_media_playback.py:240`, `test_media_content_application.py:268`, `test_research_provider_contract.py:405`, `test_chatgpt_page_packaging.py:104,127`. **Deferred host and product names left alone** — 21 sites across the systemd unit contracts, `framenest.sock`, `framenest.env`, `.framenest.json`, the companion protocol and storage-key literals, `COMPATIBLE_APPLICATION_NAME`, `.framenest.pth`, `framenest.example`. **Fixture literals left alone** — `name="framenest.test"` at `test_structured_logging.py:343,390`, `framenest_alembic_environment_under_test` at line 535.

## 6. Full counts, before and after

```text
before   37 failed, 4362 passed, 8 skipped, 2 warnings in 700.97s (0:11:40)
after        0 failed, 4399 passed, 8 skipped, 3 warnings in 708.46s (0:11:48)
JavaScript  ℹ tests 583  ℹ pass 578  ℹ fail 0  ℹ skipped 5     (identical)
```

Total collected is4407 in both runs: 37 + 4362 + 8 = 4407 and 4399 + 8 = 4407, so no test was lost or gained. **The warning count moved 2 → 3 and the cause is this cut, benignly:** the third is the same pre-existing `PydanticJsonSchemaWarning` from `pydantic/json_schema.py:2463`, now also emitted by `unit/test_configuration.py::test_database_path_absent_from_settings_repr_logs_api_and_openapi`, which at baseline died at line 297 and never reached its `app.openapi()` call. Same warning, same source line, one more test now runs to completion.

## 7. Ledger movements, with measurement and cause

Measured by the ledger's own code before I re-pinned anything (only its three Part C assertions were red; the other 12 were already green):

| Pin | Old | New | Measurement | Cause |
|---|---|---|---|---|
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["tests"]` | 1851 | **1835** | module-measured | −16 lowercase occurrences: 4 `src/framenest` paths, 5 `dictConfig` keys, 2 root-namespace arguments, 3 `framenest.public_published_*` names, 2 `framenest/**` globs |
| `PER_TREE_FRAMENEST_FILE_COUNT["tests"]` | 184 | **183** | module-measured | `contract/test_workspace_media.py` held exactly **one** occurrence in the whole file — the moved path literal — and correctly leaves the content set |
| `EXPECTED_FRAMENEST_CONTENT_PATHS` | 507 | **506** | element lines counted after the edit | the same single path removed |

Every movement is decomposed exactly with no residual, and each carries a provenance comment in the ledger's established style. **Part A and Part B did not move.** Part A: `FROZEN_DOCUMENT_SHA256` and `FROZEN_ALEMBIC_SHA256` have zero changed lines in the diff (grep for 64-hex on `^[+-]` returns 0). Part B: `EXPECTED_FRAMENEST_BASENAME_PATHS` untouched. **`FROZEN_ALEMBIC_SHA256` key count, measured by me from the file: 36** — 36 pin rows, 36 distinct keys, 36 tracked files on disk (`git ls-files`), revisions `0001`–`0035` plus `__init__.py`. The 38 reported twice earlier in this whole is wrong. The other pins — `CAPITALIZED_*`, `ENV_PREFIX_*`, `MUTATION_HEADER_*`, `HOST_PATH_*`, `UNIT_ACCOUNT_*`, `CONSOLE_SCRIPT_ENTRY_COUNT` — are unchanged, which is expected because every occurrence I removed was lowercase. Retention module against my own SHA: **15 passed**.

## 8. Diff and commit

```text
 tests/contract/test_kronika_identity_retention.py  | 31 ++++++++++++++++++--
 .../test_kronika_product_string_agreement.py       | 22 +++++++++++----
 tests/contract/test_kronika_settings_parity.py     | 33 ++++++++++++++++++++--
 tests/contract/test_public_published_uds.py        |  6 ++--
 tests/contract/test_uvicorn_logging.py             |  8 +++---
 tests/contract/test_workspace_media.py             |  2 +-
 tests/unit/test_configuration.py                   |  2 +-
 tests/unit/test_server_runtime.py                  |  4 ++--
 tests/unit/test_structured_logging.py              |  4 ++--
 9 files changed, 88 insertions(+), 24 deletions(-)
```

**Zero `src/` files appear** — `git diff --name-only HEAD~1 HEAD | grep "^src/"` is empty. No Alembic revision, no `docs/adr/**`, no `pyproject.toml`, no `poetry.lock`, no JS file. Commit `6e89328640fe5477e08f17f4c31c9fc4bf261238`, one commit, no amend, no push, no branch, no tag, no merge, no rebase.

## 9. Post-commit gate

```text
$ ./.ap/ap project check --root /home/agile/Projects/kronika --baseline 6e89328640fe5477e08f17f4c31c9fc4bf261238
OK project identity: cisarik/kronika
OK environment policy: sanitized-v1
ap project check --baseline: PASS

$ ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 6e89328640fe5477e08f17f4c31c9fc4bf261238 --operation runtime-info
/home/agile/Projects/kronika/.venv/bin/python
3.13.9 (main, Nov 19 2025, 22:47:49) [Clang 21.1.4 ]
/home/agile/Projects/kronika/src/kronika/__init__.py
```

Both PASS and `runtime-info` resolves `src/kronika/__init__.py`. `ap doctor` PASS before and after; submodule unmoved. Final post-commit derivation re-run: **moved-name 0, frozen-name 75**, `tests` occurrences 1548 in Python.

## 10. Deviations, risks, missing evidence, next step

**Deviations.** `git add` staged the nine authorized files — a commit grant implies staging, and it is the only Git command outside the read-only enumeration. Four probes and two runner scripts were written under `/tmp/opencode/ksi21/`; nothing outside the repository changed. No interpreter was invoked directly by me: every Python result came through `ap exec`. One disclosure: my **first** background suite run was killed by the shell tool's 120-second timeout taking the process group with it; I re-ran it detached under `setsid` and it completed normally. No repository or environment state was affected. `node --test`, `jq`, `grep`, `sed`, `ls` were used read-only.

**Risks.** Low. Nothing in this cut touches production behaviour:16 literals in test code, 3 ledger pins re-pinned from their own measurement, one assertion narrowed with a live negative control, and 3 inventory rows added. The one judgement I would expect you to overturn is §3 — pinning the settings class name as a product-string occurrence rather than teaching the guard to skip annotations.

**Notices reported, not fixed** (each outside the four moved-name classes or outside `tests/`):
1. `tests/unit/test_structured_logging.py:351` still sets `record.__dict__["framenest_structured_payload"]` and `:398` still sets `["framenest_sanitized_payload"]`. Production renamed both attributes (`structured_logging.py:19-20`). At `:351` this makes `test_malformed_context_does_not_crash_formatting` **vacuous** — the filter no longer finds the payload, falls back to the foreign-payload path, and the deliberately broken `_ReprRaises()` context is never traversed. At `:398` the literal is dead but the test still reaches its fallback through the patched `_encode_json`. Both pass. Not logger names, handler/formatter keys or `src/` paths, so not mine to change.
2. `test_public_published_uds.py`'s two logger-name assertions depend on `kronika` propagating to `caplog`. Any earlier `dictConfig(build_uvicorn_log_config())` sets `propagate: False` on that logger and starves them. Proven, not theorised: the file passes alone (18 passed) and in the suite's natural order, and fails when a dictConfig-applying file runs first. Pre-existing design, unchanged by me.
3. `docs/WORKER_EXECUTION_CONTRACT.md` still states `provenanceModule = framenest`, stale since C3-B. Outside `tests/`.
4. Test *identifiers* still carry the retired spelling (`test_config_uses_framenest_formatter_and_redaction_filter`, `test_create_server_passes_framenest_log_config`, `test_complete_framenest_settings_objects_…`). Identifiers, not literals.
5. Test runs created an ignored `__pycache__/` inside the frozen Alembic versions directory; 36 tracked files, 37 directory entries, no pin affected.

**Missing evidence.** None required. Two things I did not demonstrate and do not claim: that the product-string guard *should* count annotations (a judgement, §3), and that a removed `pydantic-settings` requirement is caught by the parity helper (code inspection, §4).

**Smallest next step.** Decide §3 — accept the three pinned `"KronikaSettings"` rows, or authorise a one-line exclusion in `product_string_nodes` plus a docstring note, which would drop `OCCURRENCE_COUNT` back toward 50. Nothing else in this cut blocks acceptance; the suite is green and C3-B is now verifiable.

## Resolved Execution Issues / Near-Misses

1. **Probe defect, caught by rule 7 — my first log-config subscript detector returned 0 hits** where five tests were failing with `KeyError: 'framenest_json'`. Zero is impossible for that tree, so the probe was wrong: for `A["formatters"]["framenest_json"]` the AST puts the *section* on `node.value.slice` and the *key* on `node.slice`; I had read them the other way round and inverted the test. Fixed; the corrected probe returned exactly the 5 real sites.
2. **Rule defect, caught by opening every hit — my first classifier reported 39 moved sites,24 of them false.** It classified *any* literal equal to `"framenest"` as a moved root-logger name, which swept in the systemd `User=`/`Group=`/`StateDirectory=` assertions, the deliberately superseded `/opt/framenest/.venv` and `/etc/framenest/ai/config.json` paths, three negative assertions, and the retention ledger's own search token. 39 − 24 = **16**. A mechanical rule is a candidate generator; only opening each hit produced the classification.
3. **Rule defect — the same classifier missed the one docstring site**, because my path regex required `src/framenest` to start the value or follow a `/`, and the literal sits inside backticks mid-sentence. Found by reading the module, fixed by matching `src/framenest` anywhere in the value; the rule then reported 16 before and 0 after.
4. **Near-miss, order-dependent false failure — I "broke" two tests by choosing the file order.** Running `unit/test_structured_logging.py` before `contract/test_public_published_uds.py` failed the latter's two logger-name tests, because an earlier `dictConfig` sets `propagate: False` on the `kronika` logger and starves `caplog`. Re-running in the suite's natural order gave 166 passed. **The failure was an artefact of my invocation, not a defect**, and I did not "fix" a green test to suit a bad measurement.
5. **Near-miss — the baseline run died before producing counts.** My first background invocation was killed by the tool timeout. Re-run detached; the exact baseline then reproduced. No state affected.
6. **Disclosure — `ls` on the frozen versions directory returns 37 entries, not 36.** The extra entry is an ignored `__pycache__` created by the test runs. The tracked set is 36 and matches the 36 pins exactly; I report both numbers rather than the flattering one.
7. **Disclosure — probe scripts spawn subprocesses.** The parity negative control and the inventory dump both call `git show` inside the `test-focus` operation, the same mechanism `test_kronika_settings_parity.py` itself uses. No interpreter was invoked by me directly; no environment was repaired.

## Pre-Existing Failure Classification

**none, and evidenced rather than asserted.** Every one of the 37 baseline failures is newly red because of C3-B, and each is attributable to a named moved-name site in §1; none predates it. The 36 caused-by-C3-B failures trace to the 13 code sites that a failing test reaches, and I confirmed the mechanism in the commit's own diff rather than inferring it. The 37th was caused by C3-B's `[project] name` rename and was an over-broad assertion, not a stale reference. The **4 vacuously-green guards** in §2 are not failures at all — they are the more serious residue, passing over an empty path — and this is the first execution that could see them. The 8 skips are the pre-existing `FRAMENEST_RUN_REAL_MEDIA_TOOLS` / `FRAMENEST_RUN_NVIDIA_NIM_SMOKE` environment gates, untouched. No test was skipped, marked, xfailed, disabled, deleted or suppressed by me.

---

```text
Orchestration critique:
MEASURED: The correction prompt's inventory is a sample in a second, more consequential way than the one it warns about — it names "hardcoded src/framenest paths" and counts eight, but the defect class also produced a *vacuous* guard and a *prose* site it could not see. Evidence: `SOURCE_ROOT = Path("src/framenest")` at tests/unit/test_structured_logging.py:24 and tests/unit/test_server_runtime.py:25 name a directory that does not exist, and the four whole-tree import-confinement guards built on them (test_structured_logging.py:419,436 and test_server_runtime.py:295,367) appear in none of the 37 failures because an empty loop asserts nothing; the module docstring path at test_kronika_product_string_agreement.py:22 fails nothing because it is prose. Effect: had I executed the issued list literally, four guards would have stayed silently green over zero files — a worse outcome than the 37 red tests the prompt set out to close, because a red test is visible and a vacuous guard is not. Second measurement: the prompt's expectation that the settings-parity assertion was the only non-mechanical failure is also incomplete — repairing the source-root glob in test_kronika_product_string_agreement.py exposed a further four failures from a mechanism no prompt anticipated, namely that C3-B's FrameNestSettings→KronikaSettings rename made three previously brand-free production literals brand-bearing (two `-> "KronikaSettings"` annotations and the redaction filter's `cls.__name__` check at structured_logging.py:244), so the occurrence-level inventory's total went 50→53 and its duplicate map gained a class name. Smallest correction: when commissioning a rename cut, state the derivation as a *predicate over literals* and require the worker to report the count on both sides of the cut, which is what surfaced both findings here; and treat "occurrences a cut creates" as a first-class review item, because a rename that introduces new occurrences breaks inventory pins in a way that a rename that only deletes them does not.
LEAD: tests/unit/test_structured_logging.py:351 and :398 still write `record.__dict__["framenest_structured_payload"]` and `["framenest_sanitized_payload"]`, which C3-B renamed to `kronika_structured_payload` / `kronika_sanitized_payload` at src/kronika/structured_logging.py:19-20; I left them because neither is a logger name, handler/formatter key nor `src/` path, but I did not execute a demonstration, so the size of the hole is unverified. Cheapest useful check: one throwaway probe that constructs the same LogRecord with each spelling and prints which branch `FrameNestRedactionFilter.filter` takes and whether the deliberately broken `_ReprRaises()` context is reached — if the old spelling routes to the foreign-payload fallback, `test_malformed_context_does_not_crash_formatting` is asserting nothing today and belongs to whoever owns the `FrameNest*` class-name deferral, since a third site class (record-dict attribute names) is now missing from the taxonomy this whole derives cuts from.
```