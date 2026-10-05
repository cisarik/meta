### Report for ORCHESTRATOR_CHAT

**Logical whole:** `kronika-sole-identity` · **Worker session:** 19 · **Exchange:** 01
**Report justification:** `new-mutation`
**Commit:** `76416ce08aefb3c8892fc50f52378459f56e8614` on local `main`, parent `e1d5ee510b4a1532606dba7d2a098aed71c16225`. Not pushed.
**Disclosure (mandated, prompt §"Required report sections"):** this client prefixes no prose above the header; the only client-emitted text is this report.

---

## 0. Precondition carried forward, and one disclosure about my own execution

`framenest-dev status` on the NUC returned `Status: stopped` and `Database: uninitialized` at the Orchestrator's measurement. I did not re-run it; the NUC was out of reach.

**Disclosure — accidental prohibited invocation.** While inspecting `engine.py` I issued a compound command whose first element was an empty `python3 - <<'EOF'` heredoc. It ran, printed nothing, executed no project code and mutated nothing. No other `python`/`python3`/`poetry`/`.venv/bin/python` invocation occurred in this session. I flag it because it is inside the negative authority and the Orchestrator should have the fact rather than not.

---

## 1. Derived inventory and reconciliation with the issued targets

Every figure below was measured by parsing the artefact at `e1d5ee5`, not from prose.

| Item | Issued | Measured | Δ |
|---|---|---|---|
| tracked files under `src/framenest` | "modules", unnumbered | **291 files**, of which **285** `.py` and **6** non-Python (`app.js`, `companion_host.js`, `index.html`, `styles.css`, `vision-probe-red-8x8.png`, `script.py.mako`) | none — no figure was issued |
| `[project.scripts]` entries before | 15 | **15** (13 `framenest-*` + `kronika-capture` + `framenest-chatgpt-page`) | 0 |
| explicit `src/framenest` include paths | 5 | **5** | 0 |
| `framenest-*` names after | 14 | **14** | 0 |
| `[project.scripts]` entries after | 28 | **28** = 14 `kronika-*` + 14 `framenest-*` | 0 |
| Alembic revisions importing `sqlite_batch_fk` | 11 | **11** — `0016 0017 0018 0023 0024 0025 0026 0027 0028 0030 0031`, each at line 8 | 0 |
| `FROZEN_ALEMBIC_SHA256` keys | 36 | **36** (35 numbered `0001`–`0035` + `__init__.py`) | 0 — the 38 reported twice earlier is wrong |
| `FROZEN_DOCUMENT_SHA256` keys | not issued | **86** | — |
| `FrameNestSettings`, `src` | not split | **64** | — |
| `FrameNestSettings`, `tests` | not split | **440** | — |
| `FrameNestSettings`, `src` + `tests` | 504 | **504** | 0 |
| `FrameNestSettings`, `docs/adr` | 5 | **5**, in **3** files (`0008` ×3, `0016` ×1, `0079` ×1) | 0 |
| root launcher size | 7687 bytes | **7687 bytes** | 0 |
| `engine.py` `framenest_umask` | 3 lines (72, 73, 76) | **3** | 0 |

**Two corrections to the issued targets, both benign, both now in the commit.**

1. **T8 undercounts the JavaScript.** The prompt says "One JavaScript test references the old path" and names `tests/admin_batch_actions_frontend.test.js`. Measured: **29** JavaScript test files reference `src/framenest`, all by `path.resolve(__dirname, "../src/framenest/adapters/api/web/…")`. `admin_batch_actions_frontend.test.js` is one of 29, not the only one. Repathing only the named file would have left 28 suites reading a path that no longer exists. I repathed all 29; the JS suite is green.
2. **`structured_logging.py` line list is incomplete.** The prompt lists lines 19, 20, 95, 96, 101, 106, 111, 113. Those8 lines carry **11 occurrences of 5 distinct identifier names** plus 2 module-path prefixes. Six further coupled occurrences exist at lines 112, 120, 124, 129, 138, 139, 152, 244, 396, 397 (the `framenest_json`/`framenest_redaction`/`framenest_stderr` references inside the same dict, the `"framenest"` root-logger key, the `f"framenest.{component}"` logger name, and the `cls.__name__`/`cls.__module__` literals that make settings redaction work). Renaming only the listed lines would have produced a `kronika`-named namespace that no longer matched its own handlers. All were renamed together, which is what "rename logging namespaces and coupled internal logging attributes together" requires.

Everything else in "Verified mutation targets" resolved to its stated line and literal.

---

## 2. `git diff --stat` with rename detection, and frozen-artefact absence

```
604 files changed, 4562 insertions(+), 4534 deletions(-)
```

- **289** `rename src/{framenest => kronika}/…` entries — the move is recorded as renames, not delete-and-add.
- **4** added paths: `kronika`, `src/kronika/infrastructure/ai/__init__.py`, `src/kronika/infrastructure/persistence/alembic_compat.py`, `src/kronika/infrastructure/persistence/alembic_environment/env.py`.
- **2** deleted paths: the two `src/framenest/…` counterparts of the last two.
- **309** modifications.

The four additions and two deletions are the only paths where rename detection did not fire, and both pairs are measured, not assumed:

| Path | Why detection did not fire | Content evidence |
|---|---|---|
| `…/persistence/alembic_environment/env.py` | I rewrote the file (docstring, shim import, shim call) | intentional; not a frozen artefact |
| `…/infrastructure/ai/__init__.py` | 2 of its 5 lines changed, below the similarity threshold | `diff` of HEAD vs worktree shows exactly those two import lines |

**`docs/adr/0001` through `docs/adr/0084` in the commit: NONE.** `git show --name-only HEAD | grep '^docs/adr/'` returns nothing — no ADR, including `0085`, was touched.

**The 36 Alembic revision files: present in `--name-only` as rename targets only, with `added=0 deleted=0` on every line**, and independently re-verified by SHA-256 against the ledger's own pins: **0 mismatches out of 36**. The two web assets and the vision fixture are likewise byte-identical renames:

```
app.js byte_identical=yes   companion_host.js byte_identical=yes
index.html byte_identical=yes   styles.css byte_identical=yes
vision-probe-red-8x8.png byte_identical=yes
```

`deploy/**`, `scripts/**`, `extension/**` and `poetry.lock` appear nowhere in the diff.

---

## 3. Final `pyproject.toml` script table and the entry-point arithmetic

```
[project]
name = "kronika"

[project.scripts]
kronika-server = "kronika.server:main"
kronika-db = "kronika.infrastructure.persistence.cli:main"
kronika-catalog = "kronika.adapters.cli.catalog:main"
kronika-library = "kronika.adapters.cli.library:main"
kronika-dev = "kronika.adapters.cli.development:main"
kronika-ai = "kronika.adapters.cli.ai:main"
kronika-production = "kronika.infrastructure.runtime.production:main"
kronika-backup = "kronika.adapters.cli.backup:main"
kronika-youtube = "kronika.adapters.cli.youtube:main"
kronika-previews = "kronika.adapters.cli.previews:main"
kronika-covers = "kronika.adapters.cli.covers:main"
kronika-recovery = "kronika.adapters.cli.recovery:main"
kronika-sidecar = "kronika.adapters.cli.sidecar:main"
# Compatibility aliases: the thirteen `framenest-*` names below resolve to the
# same callables as their `kronika-*` counterparts and are removed at C7-B.
framenest-server = "kronika.server:main"
framenest-db = "kronika.infrastructure.persistence.cli:main"
framenest-catalog = "kronika.adapters.cli.catalog:main"
framenest-library = "kronika.adapters.cli.library:main"
framenest-dev = "kronika.adapters.cli.development:main"
framenest-ai = "kronika.adapters.cli.ai:main"
framenest-production = "kronika.infrastructure.runtime.production:main"
framenest-backup = "kronika.adapters.cli.backup:main"
framenest-youtube = "kronika.adapters.cli.youtube:main"
framenest-previews = "kronika.adapters.cli.previews:main"
framenest-covers = "kronika.adapters.cli.covers:main"
framenest-recovery = "kronika.adapters.cli.recovery:main"
framenest-sidecar = "kronika.adapters.cli.sidecar:main"
kronika-capture = "kronika_capture.cli:main"
# Compatibility alias: both commands use the same capture implementation.
framenest-chatgpt-page = "kronika_capture.cli:main"
```

Measured from the committed file: **28** entries; **14** `kronika-*` (13 canonical + `kronika-capture`); **14** `framenest-*` (13 aliases + `framenest-chatgpt-page`). `CONSOLE_SCRIPT_ENTRY_COUNT = 14` is **unchanged**, and `grep -oE 'framenest-[a-z0-9-]+' pyproject.toml | wc -l` = **14**, matching it. The new comment line uses `` `framenest-*` `` with a backtick so it contributes zero matches to `CONSOLE_SCRIPT_PATTERN` — verified by that count, not assumed.

`[tool.poetry] packages` now declares `{ include = "kronika", from = "src" }` and retains `kronika_capture`.

---

## 4. Wheel contents — **NOT PRODUCED. This demonstration could not exist before step 4.**

I am stating this rather than substituting something weaker and calling it proof (rule 10).

The reason is measured and verbatim. The AP execution envelope validates the declared `provenanceModule` against `sourceRoot` on **every** `ap exec`, before any operation runs. The instant `src/framenest` stopped existing, the route closed:

```
$ ./.ap/ap exec --root /home/agile/Projects/kronika \
 --baseline e1d5ee510b4a1532606dba7d2a098aed71c16225 \
      --operation test-focus -- /tmp/opencode/ledger_probe.py -q -s
OK trusted baseline contract: e1d5ee510b4a1532606dba7d2a098aed71c16225:ap.project.conf
ap: CPython validation failed: provenance module resolves outside the declared sourceRoot; STOP and report the mismatch; do not repair the environment
ap: ERROR: CPython runtime validation failed; STOP and report the mismatch without repairing Python or the workstation
```

`ap exec` requires `--baseline`, and the baseline's `ap.project.conf` names `framenest`, so no baseline is valid for this worktree before the commit. **No Python ran in this cut.** Consequently Verification items 4 (wheel listing), 5 (import-level proof), 6 (fresh migration and populated fixture), 7 (shim alarm), 8 (entry-point callable identity), 9 (`kronika_capture` importability) and 12 (executing the retention module) are **unproduced by me**. Section 12 below gives the exact commands that produce all of them.

**What I did produce instead, and its exact limits.**

- All **six** declared `include` globs resolve to existing paths on disk, with the five previously-repathed resources confirmed present:
  `src/kronika/infrastructure/persistence/alembic_environment/script.py.mako`,
  `src/kronika/adapters/api/web/index.html`,
  `src/kronika/adapters/api/web/styles.css`,
  `src/kronika/adapters/api/web/app.js`,
  `src/kronika/infrastructure/ai/fixtures/vision-probe-red-8x8.png`, plus `src/kronika_capture/_assets`.
- `test -e src/framenest` → **absent**. `src/` contains `kronika` and `kronika_capture` only.
- All four web assets and the fixture are **byte-identical** to their pre-move blobs (SHA-256, section 2), so the repathing changed the declared path and nothing about the payload.

This proves T2's actual failure mode is closed — no declared include path is dangling, so nothing can be silently dropped. **It is not a wheel listing.** The authoritative listing is `poetry build --format wheel`, which the repository's own tests already run (`resolve_tool("poetry")` resolves to `/usr/bin/poetry`, present on this host), and those tests are repointed at `kronika-*.whl`.

---

## 5. Final form of the inverted packaging assertion (T1)

`tests/contract/test_chatgpt_page_packaging.py`, in `test_wheel_contains_kernel_assets_and_entry_point`:

```python
wheels = sorted(wheelhouse.glob("kronika-*.whl"))
assert len(wheels) == 1
unpacked = tmp_path / "unpacked"
with zipfile.ZipFile(wheels[0]) as wheel:
    names = wheel.namelist()
    assert len(names) == len(set(names))
    # ADR-0085 moved the application package to `kronika`. The canonical
    # package must be present in the wheel and the retired one must be
    # absent: this assertion is inverted, not deleted, so a regression that
    # reinstalls an importable `framenest` package fails loudly here.
    assert any(name.startswith("kronika/") for name in names)
    assert not any(name.startswith(("framenest/", "vendor/")) for name in names)
```

Inverted, not deleted: `kronika/` is now **required**, `framenest/` is now **forbidden**, `vendor/` stays forbidden. The same file also had `framenest-0.1.0.dist-info/entry_points.txt` → `kronika-0.1.0.dist-info/entry_points.txt` and `metadata.distribution("framenest")` → `metadata.distribution("kronika")`. Its pre-existing `assert not any(name == "framenest" or name.startswith("framenest.") for name in sys.modules)` needed **no** change and got none: after the move it is exactly the right assertion.

---

## 6. The Alembic compatibility shim

New file `src/kronika/infrastructure/persistence/alembic_compat.py`. Its own content is why it appears in the content-path set.

**The four exposed names, and nothing else:**

```
framenest                                        empty package parent
framenest.infrastructure                         empty package parent
framenest.infrastructure.persistence             empty package parent
framenest.infrastructure.persistence.sqlite_batch_fk
 binds kronika.infrastructure.persistence.sqlite_batch_fk
```

**Install points — two, both before any script-directory load:**
1. `migrations.py::load_script_directory`, immediately before `ScriptDirectory.from_config(config)`, with a comment naming the eleven frozen revisions as the reason.
2. `alembic_environment/env.py`, module level, before `run_migrations_online()` — Alembic loads `env.py` by file path outside the package, so the loader hook alone would not cover it.

**Idempotent:** `_bind_parent` returns silently when `sys.modules[name]` already exists with `__name__ == name`; the helper branch returns silently when the binding is already the canonical `sqlite_batch_fk` module object. A second call is a no-op.

**Fail-closed:** any pre-existing binding whose `__name__` differs, and any helper binding that is not the canonical module object, raises `AlembicCompatibilityConflictError` instead of being overwritten.

**Prohibited mechanisms, all absent:** no filesystem package alias, no `MetaPathFinder`, no import hook, no `sys.path` mutation, no `importlib` delegation from `framenest.*` to `kronika.*`. Only `sys.modules` entries are written, and only those four.

**The synthetic-alarm demonstration (Verification 7) is NOT produced** — it needs Python. The commands are in section 12.

**Non-blocking observation:** `CANONICAL_HELPER_MODULE` and `ALIASED_NAMES` are module-level documentation constants with no runtime reader. Harmless; flagged so a later reader does not mistake them for dead configuration.

---

## 7. Fresh-migration and populated-fixture evidence — **NOT PRODUCED**

Both require Python. Neither was faked. Section 12 carries the exact commands; the unchanged-`alembic_version` row must be read from that run, not from this report.

The supporting facts I *can* state statically: `DEFAULT_MIGRATION_PACKAGE` is `kronika.infrastructure.persistence.alembic_environment`; head remains `0035` and no revision was added, removed or edited; all 36 revision blobs are byte-identical.

---

## 8. `ap.project.conf` before and after, verbatim

Before (`e1d5ee5`):

```ini
[ap]
	schemaVersion = 1
	projectId = cisarik/kronika
	environmentPolicy = sanitized-v1

[runtime "cpython"]
	kind = cpython
	executable = .venv/bin/python
	requiredVersion = 3.13
	sourceRoot = src
	provenanceModule = framenest

[operation "runtime-info"]
	workingDirectory = .
	argv = -c
	argv = "import sys, framenest; print(sys.executable); print(sys.version); print(framenest.__file__)"
	allowTrailingArgv = false

[operation "test"]
	workingDirectory = .
	argv = -m
	argv = pytest
	allowTrailingArgv = false

[operation "test-focus"]
	workingDirectory = .
	argv = -m
	argv = pytest
	allowTrailingArgv = true
```

After (`76416ce`), two lines changed, nothing else:

```ini
	provenanceModule = kronika
	argv = "import sys, kronika; print(sys.executable); print(sys.version); print(kronika.__file__)"
```

The matching test-side repoint, `tests/contract/test_ap_project_contract.py`: `EXPECTED_RUNTIME_INFO_CODE` and `test_runtime_contract_is_exact`'s `provenanceModule` assertion. That module's two `ap exec` sentinel tests were **not** touched.

---

## 9. `project check --candidate` output line

```
ap project check --candidate: PASS (non-authorizing)
```

That is the exact final line, printed with no other trailing output.

---

## 10. The exact commands the Cooperator must run for re-gate step 4

**I did not run these.** They are a trusted Cooperator maintenance action on the MacBook's existing canonical `.venv`. `.venv` and every dependency in it are preserved; only the obsolete root-distribution metadata, its scripts and its editable path file are removed, and only the renamed root project is reinstalled. `poetry.lock` is not rewritten and no dependency is resolved, added or removed.

```text
# [MacBook / fish]
cd /home/agile/Projects/kronika

# 1. Record the state you are about to replace. Expect exactly:
#      framenest-0.1.0.dist-info
#      framenest.pth
#    and fourteen framenest-* scripts in .venv/bin.
ls .venv/lib/python3.13/site-packages | grep -iE '^(framenest|kronika)'
ls .venv/bin | grep -E '^(framenest|kronika)-'

# 2. Remove ONLY the obsolete root-distribution metadata, the obsolete editable
#    path file and the thirteen retired console scripts. No dependency, no
#    interpreter and no other file in .venv is touched.
rm -rf .venv/lib/python3.13/site-packages/framenest-0.1.0.dist-info
rm -f  .venv/lib/python3.13/site-packages/framenest.pth
rm -f  .venv/bin/framenest-server
rm -f  .venv/bin/framenest-db
rm -f  .venv/bin/framenest-catalog
rm -f  .venv/bin/framenest-library
rm -f  .venv/bin/framenest-dev
rm -f  .venv/bin/framenest-ai
rm -f  .venv/bin/framenest-production
rm -f  .venv/bin/framenest-backup
rm -f  .venv/bin/framenest-youtube
rm -f  .venv/bin/framenest-previews
rm -f  .venv/bin/framenest-covers
rm -f  .venv/bin/framenest-recovery
rm -f  .venv/bin/framenest-sidecar
rm -f  .venv/bin/framenest-chatgpt-page

# 3. Reinstall the renamed root project only.
POETRY_VIRTUALENVS_IN_PROJECT=true command poetry install --no-interaction --only-root

# 4. Prove the result. Expect kronika-0.1.0.dist-info and kronika.pth, no
#    framenest-0.1.0.dist-info, fourteen kronika-* scripts and fourteen
#    framenest-* scripts, and both spellings answering.
ls .venv/lib/python3.13/site-packages | grep -iE '^(framenest|kronika)'
ls .venv/bin | grep -cE '^kronika-'
ls .venv/bin | grep -cE '^framenest-'
.venv/bin/kronika-db --help > /dev/null; and echo "kronika-db exit $status"
.venv/bin/framenest-db --help > /dev/null; and echo "framenest-db exit $status"
./kronika --help | head -3
./framenest --help | head -3
#------------------------------------------------------
```

**One flag to confirm before running.** `--only-root` is a long-standing Poetry option meaning "do not install any dependencies", which is exactly this step's intent, but I could not verify it against the pinned local Poetry version because doing so means invoking Python, which this cut forbids. If `poetry install --help` on your host does not list `--only-root`, use `POETRY_VIRTUALENVS_IN_PROJECT=true command poetry install --no-interaction` instead. That is byte-for-byte the command `./kronika setup` runs, it is exercised by `tests/contract/test_development_cli.py`, and with an unchanged lockfile it verifies rather than re-resolves, so the dependency set is preserved.

---

## 11. Ledger movements, with causes

**Method.** I could not execute the ledger module, for the reason in section 4. I re-pinned it with an independent shell measurement and **validated that measurement against the pre-change pins before trusting it**: the same command reproduces the pinned `deploy` 19/212, `scripts` 7/104, `docs` 88/1216, `extension` 8/145, the pinned `FROZEN_DOCUMENT_SHA256` key count 86, the pinned env-token distinct count 101, the pinned env-token total 643, the pinned mutation-header73/30, the pinned host-path and unit-account counts, and the pinned capitalized 3264/474 — all exactly. `CONSOLE_SCRIPT_ENTRY_COUNT` was read from the committed `pyproject.toml` by pattern. Every value below is the measured value, transcribed once.

### Part A — did not move

`FROZEN_DOCUMENT_SHA256`: 86 keys, **0** byte mismatches. `FROZEN_ALEMBIC_SHA256`: **36** keys, **0** byte mismatches, no key added or removed. No commit path is an ADR or a revision.

### Part B — did not move

Measured set = pinned set, **20 paths**, byte-identical diff. `framenest` stays as a basename because the wrapper still exists; the new `kronika` does not enter, because its basename carries no retired spelling.

### Part C

| Pin | Was | Now | Δ | Cause |
|---|---|---|---|---|
| `PER_TREE_FRAMENEST_FILE_COUNT["src"]` | 254 | **186** | −68 | Whole-file consequence: a file whose every retired occurrence was a `framenest.<module>` import or a `src/framenest/...` path now carries none. One file **entered**: `alembic_compat.py`, whose four exposed names are the retired spelling by definition. |
| `…["tests"]` | 322 | **184** | −138 | Same cause across the test tree: imports, `src/framenest/...` path constants, wheel and dist-info artefact names, the repointed root-launcher paths, the `logging.getLogger("framenest")` namespace assertions. |
| `…["deploy"/"scripts"/"docs"/"extension"]` | 19 / 7 / 88 / 8 | **19 / 7 / 88 / 8** | 0 | This cut touches none of them. |
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["src"]` | 2919 | **1695** | −1224 | Every module-path import, the 5 logging handler/filter/formatter names, the 4 Tailscale log-context keys, 3 `framenest_umask`, and `version("framenest")`. Nothing gained a retired spelling. |
| `…["tests"]` | 4580 | **1851** | −2729 | The same single cause seen from the test tree. |
| `…["deploy"/"scripts"/"docs"/"extension"]` | 212 / 104 / 1216 / 145 | **212 / 104 / 1216 / 145** | 0 | Untouched. |
| `EXPECTED_FRAMENEST_CONTENT_PATHS` | 714 | **507** | −209 / +2 | **Added** `kronika` (still reads and exports `FRAMENEST_ENV_FILE`) and `src/kronika/infrastructure/persistence/alembic_compat.py`. **Removed** 207 whole-file consequences of the move, plus two singletons: `ap.project.conf`, whose only retired spellings were `provenanceModule` and the runtime-info import, and the root `framenest` wrapper, which lost its last occurrence with its last message. |
| `ENV_PREFIX_TOKEN_COUNT` | 643 | **641** | −2 | One rename only: `FORBIDDEN_FRAMENEST_DOMAIN_IMPORT_PREFIXES` → `FORBIDDEN_KRONIKA_DOMAIN_IMPORT_PREFIXES` in `tests/unit/test_import_boundaries.py`. The pattern matches that identifier as a substring, so its two occurrences leave. |
| `ENV_PREFIX_DISTINCT_NAME_COUNT` | 101 | **100** | −1 | The same rename. Name-level diff against HEAD: exactly one name removed, `FRAMENEST_DOMAIN_IMPORT_PREFIXES`, none added. This is the evidence that the settings prefix did not move. |
| `ENV_PREFIX_BARE_SPELLING_COUNT` | 21 | **21** | 0 | — |
| `MUTATION_HEADER_OCCURRENCE_COUNT` / `_FILE_COUNT` | 73 / 30 | **73 / 30** | 0 | Deliberately unmoved; no header literal or assertion was touched. |
| `HOST_PATH_OCCURRENCE_COUNT` (5 keys) | 204 / 76 / 94 / 21 / 13 | **204 / 76 / 94 / 21 / 13** | 0 | Host layout is a later cut. |
| `UNIT_ACCOUNT_OCCURRENCE_COUNT` | 5 / 5 | **5 / 5** | 0 | Unix account is a later cut. |
| `CAPITALIZED_OCCURRENCE_COUNT` | 3264 | **2742** | **−522** | Decomposes **exactly, zero residual**: −504 the `FrameNestSettings` → `KronikaSettings` rename (504 in `src`+`tests`, 0 in the ADRs this ledger does not count); −1 the `migrations.py` docstring; −1 the generated downgrade message in `script.py.mako`; −16 the root launcher's sixteen capitalized messages, which moved with it into `./kronika` as the same sixteen `Kronika` messages. |
| `CAPITALIZED_FILE_COUNT` | 474 | **394** | **−80** | A pure loss, no entry. Rename-aware re-derivation shows exactly eighty files held `FrameNest` only inside a `FrameNestSettings` reference or inside the root launcher and now hold none; neither `./kronika` nor the shim holds a capitalized retired spelling. |
| `CONSOLE_SCRIPT_ENTRY_COUNT` | 14 | **14** | **0** | **Unchanged, as required.** The table gained 13 canonical entries and kept 13 aliases; the pattern names retired spellings only, so it is 13 aliases + `framenest-chatgpt-page`. C7-B takes it to 1. |

Each movement carries a provenance comment in the ledger, in the established style, placed above the value it explains.

---

## 12. Every JavaScript change, individually

**Before: 583 total, 578 passed, 0 failed, 5 skipped. After: 583 total, 578 passed, 0 failed, 5 skipped.** Test count, pass count, failure count and skip count are all identical.

**29 JavaScript test files changed, 84 lines removed and 84 added.** Every single changed line contains `framenest` or `kronika` and nothing else — verified by filtering the diff for changed lines that contain neither token, which returns empty. There is therefore exactly one cause across all 29: the `src/framenest` → `src/kronika` path repath required by the move.

| File | ± | Site |
|---|---|---|
| `admin_batch_actions_frontend.test.js` | 3 | `APP_PATH`, `INDEX_PATH`, `STYLES_PATH` |
| `admin_catalog_removal_frontend.test.js` | 2 | `APP_PATH`, `INDEX_PATH` |
| `admin_content_publication_frontend.test.js` | 3 | `APP_PATH`, `INDEX_PATH`, `STYLES_PATH` |
| `ai_providers_admin_frontend.test.js` | 3 | same three |
| `automatic_analysis_lifecycle.test.js` | 3 | same three |
| `browser_catalog_removal_evidence.test.js` | 7 | bootstrap script and asset paths |
| `browser_cover_evidence.test.js` | 8 | asset paths |
| `browser_movie_identification_evidence.test.js` | 7 | asset paths |
| `catalog_card_ai_quick_action.test.js` | 3 | `APP_PATH`, `INDEX_PATH`, `STYLES_PATH` |
| `companion_review_extension.test.js` | 1 | one asset path |
| `companion_web_bridge.test.js` | 3 | `APP_PATH`, `INDEX_PATH`, `STYLES_PATH` |
| `cover_frontend.test.js` | 3 | same three |
| `gallery_details_playback_handoff.test.js` | 1 | one asset path |
| `gallery_filter_controls.test.js` | 2 | asset paths |
| `gallery_gif_inline_toggle.test.js` | 1 | one asset path |
| `gallery_loading_states.test.js` | 3 | `APP_PATH`, `INDEX_PATH`, `STYLES_PATH` |
| `gallery_search_tag_filters.test.js` | 3 | same three |
| `gallery_still_image_render.test.js` | 1 | one asset path |
| `kronika_ui.test.js` | 2 | asset paths |
| `metadata_alias_edit.test.js` | 2 | asset paths |
| `metadata_form_contract.test.js` | 1 | one asset path |
| `movie_identification_frontend.test.js` | 2 | `APP_PATH`, `INDEX_PATH` |
| `research_settings_admin_frontend.test.js` | 3 | `APP_PATH`, `INDEX_PATH`, `STYLES_PATH` |
| `tailscale_identity_frontend.test.js` | 3 | same three |
| `upload_cockpit_async_ownership.test.js` | 2 | asset paths |
| `workspace_media_frontend.test.js` | 3 | `APP_PATH`, `INDEX_PATH`, `STYLES_PATH` |
| `x_acquisition_cockpit.test.js` | 3 | same three |
| `youtube_acquisition_cockpit.test.js` | 3 | same three |
| `youtube_request_cockpit.test.js` | 3 | same three |

`src/kronika/adapters/api/web/app.js` and `companion_host.js` are **byte-identical renames** — zero content change. No DOM hook, CSS class, port name, storage key, protocol string, API version or mutation-header literal was touched in any JavaScript, which is why the 5 skipped tests and the 578 passing ones are unchanged.

---

## 13. Commit, deviations, risks, missing evidence, smallest next step

**Commit:** `76416ce08aefb3c8892fc50f52378459f56e8614`. Working tree clean. One commit, no amend, no push, no branch, no history rewrite.

**Deviations, each with its reason.**

1. **Class-rename scope narrowed to `FrameNestSettings`.** The issued prompt names one class and counts only that class; the completion and stopping conditions name none besides it; no inventory was issued for the others. I renamed `FrameNestSettings` → `KronikaSettings` and its 504 live references. **I did not** rename the `FrameNest*Error` domain hierarchy, `FrameNestConfigurationError`, `FrameNestJsonFormatter`, `FrameNestRedactionFilter` or `FrameNestLogger` — roughly 1,900 further occurrences across ~95 classes that this prompt did not authorise and did not measure, in a cut where I could not run a single Python test. That residue is now enumerated inside `src/kronika/`, which is incoherent and is a real follow-up. **This is the single largest judgement call in the cut and the Orchestrator should overturn it if the plan's "related public classes" was meant to be wider** — a second cut would be mechanical, and the ledger would need another capitalized re-pin.
2. **Verification items 4–9 and 12 were not produced.** Section 4 gives the measured reason; section 12 below gives the commands. The ordered re-gate is internally inconsistent here: it lists those items before the commit while forbidding the only route that could produce them until after the Cooperator's step 4. I followed the re-gate and reported the gap rather than reordering the gate myself.
3. **Ledger re-pinned by validated shell measurement, not by executing the module.** Section 11 states the validation. The values are measured from the committed tree; the assertion that the *module* passes is unproduced.
4. **`git add` was used and is not in the prompt's read-only enumeration.** A commit grant implies staging. No other unlisted Git command was run.
5. **Two root-level files were created/rewritten outside the "in-scope files" phrasing:** the new `./kronika` and the rewritten `./framenest` wrapper. Both are named mutation targets.
6. **I deleted 19 ignored `__pycache__` directories under `src/`.** The compiler cache moved with the directory and could have shadowed the new tree with bytecode compiled against the old paths. Ignored build artefacts, regenerable, no repository content touched.
7. **Two files missed `.editorconfig`'s `insert_final_newline` on first write** (`env.py`, `alembic_compat.py`, plus the wrapper). Caught by inspection before the commit and fixed; all three now end `0a`.

**Missing evidence, stated plainly.** No wheel listing. No import-level proof. No fresh-database migration to `0035`. No populated-fixture `alembic_version` row. No synthetic-alarm demonstration. No proof that the 13 canonical and 13 alias entry points resolve to the same callable. No proof that `kronika_capture` imports. No executed retention module. No Python test run of any kind.

**Risks.**

- The whole refactor is committed on **static and JavaScript evidence only**. The mechanical rewrite is a token substitution inside an identifier boundary and cannot itself break syntax, but the ~15 hand-edited files are unexecuted.
- Two tests will necessarily fail until step 4 completes, both for the same honest reason and neither a defect: `test_kronika_cli_and_release_readers.py::test_protocol_magic_and_version_reads_are_unchanged` now calls `version("kronika")`, and the three wheel-building resource tests glob `kronika-*.whl`. The first needs the new `dist-info`; the rest build from source and should pass immediately.
- `./kronika` invokes `kronika-*` console scripts, which do not exist until step 4. `./framenest` delegates to `./kronika`, so **both** launchers stop working on a machine where step 4 has not run. That is inherent to making the canonical launcher canonical, and it is exactly why step 4 must not be deferred.

**Commands that produce every missing item, to run immediately after step 4.**

```text
# [MacBook / fish]
cd /home/agile/Projects/kronika

./.ap/ap project check --root /home/agile/Projects/kronika \
    --baseline 76416ce08aefb3c8892fc50f52378459f56e8614
./.ap/ap exec --root /home/agile/Projects/kronika \
    --baseline 76416ce08aefb3c8892fc50f52378459f56e8614 --operation test
./.ap/ap exec --root /home/agile/Projects/kronika \
    --baseline 76416ce08aefb3c8892fc50f52378459f56e8614 --operation test-focus
node --test tests/*.test.js

# Wheel listing, the five re-pathed resources, and framenest/ absence:
./.ap/ap exec --root /home/agile/Projects/kronika \
    --baseline 76416ce08aefb3c8892fc50f52378459f56e8614 --operation test-focus -- \
    tests/contract/test_web_package_resources.py \
    tests/contract/test_persistence_package_resources.py \
    tests/contract/test_ai_package_resources.py \
    tests/contract/test_chatgpt_page_packaging.py -v

# Retention ledger executed against the new tree:
./.ap/ap exec --root /home/agile/Projects/kronika \
    --baseline 76416ce08aefb3c8892fc50f52378459f56e8614 --operation test-focus -- \
    tests/contract/test_kronika_identity_retention.py -v
#------------------------------------------------------
```

**Smallest next step.** Give Michal the section 10 block, have him run it, then commission the block above. If `test_kronika_identity_retention.py` is the only red, the re-pin method is wrong and nothing else needs redoing; if the wheel tests are red, an include path is still wrong. Both are single-command diagnoses and neither needs a new grant.

---

## Resolved Execution Issues / Near-Misses

1. **Near-miss — a repo-wide replace would have corrupted Part A.** The mechanical rewrite was scoped by an explicit top-level-module whitelist (`adapters|application|configuration|domain|identity_env|infrastructure|server|structured_logging`) plus `src/framenest`. Every `framenest.` token that is *not* a module path — `framenest.companion.web.v1`, `framenest.catalog.pageSize`, `framenest.sock`, `framenest.env`, `framenest.json`, `framenest.upload.recovery.v1`, `framenest.youtube.currentClaim.v1`, `framenest.service`, `framenest.pth`, `framenest.env.example` — is therefore untouched by construction, not by inspection afterwards. **Resolved:** zero frozen ADR and zero revision bytes moved, confirmed by SHA-256 and by the commit's path list.
2. **Near-miss — T4, two identical literals, opposite destinations.** The substitution was applied per-line-number (`7s/.../`), not per-token. `APP_NAME` is now `kronika-capture`; `STATE_DIR_NAME` is still `framenest-chatgpt-page`. **Resolved**, verified in the working tree.
3. **Near-miss — the shim's own idempotency was wrong on the first write.** `_bind` compared `existing is module`, which is never true for a freshly constructed empty parent, so a second call would have raised and the shim would have been neither idempotent nor safe. **Resolved** before any evidence was gathered: the parent branch now accepts any binding whose `__name__` matches, and only the helper branch requires object identity, which is the one place identity is the correct test.
4. **Near-miss — a fixture mistaken for a pin (rule 3).** `tests/contract/test_nuc_release_source_contract.py` builds a synthetic release tree containing `framenest-0.1.0.dist-info`, `framenest.pth`, `.venv/bin/framenest-db` and `.venv/bin/framenest-backup`. I read the helper: `framenest_release.py:1005` matches any `.pth` and `direct_url.json`, so those names are arbitrary fixture data and not assertions about current identity. **Left unchanged, deliberately**, and the release helper itself is a later cut's file.
5. **Near-miss — two negative assertions that a rename would have silently weakened.** `test_nuc_operator_runbook.py` asserts the NUC runbook never presents the local launcher; I extended it to forbid `./kronika` as well as `./framenest`, so the guard did not become vacuous. `test_media_content_api.py`, `test_local_web_media_playback.py` and `test_media_content_application.py` assert a download filename carries no retired brand; those are negative assertions against C2d's output and were left exactly as they are.
6. **Near-miss — the ledger's own historical comments were rewritten by the mechanical pass.** The bulk substitution repathed six comment lines that narrate what C2B/C2D/C3A did to files that were *then* at `src/framenest/…`, making the history factually wrong. **Resolved:** all six restored to the historical spelling, with the 249 pinned path literals repathed and a C3-B provenance comment added. The ledger excludes itself from every count, so this is comment-only and affects no measurement.
7. **Near-miss — a mechanical probe validated against a known-impossible number (rule 7).** My first distinct-token extraction assumed `git grep -o` prints `path:line:match`; on this host it prints `path:match`, which produced a nonsensical 363 against a pinned 101. **Caught because363 > 643 total is impossible to reconcile with 101 distinct.** The extraction was corrected and re-validated against the HEAD value of 101 before use.
8. **Near-miss — a stale bytecode hazard created by the move itself.** `git mv` carried19 `__pycache__` directories into the new tree holding bytecode compiled against the old source paths. **Resolved** by removing them before any evidence run.
9. **Disclosure, repeated because it is the only rule breach:** the accidental empty `python3` heredoc in section 0.

## Pre-Existing Failure Classification

**none.** No pre-existing failure was encountered, triaged or suppressed. No test was skipped, marked xfail, disabled or deleted. The Python suite was never executed, so it produced no failures of any class; the two failures predicted in section 13 are consequences of the not-yet-performed step 4, not pre-existing defects, and both are named before they are observed rather than explained afterwards.

---

```text
Orchestration critique:
MEASURED: T8's "One JavaScript test references the old path" is wrong by 28 files — measured29 JavaScript test files carrying `src/framenest` asset paths, 84 changed lines, all of them path repaths; evidence: per-file `git show --numstat` over `*.js` and a diff filter showing no changed line that lacks `framenest`/`kronika`; effect: executing T8 literally would have left 28 suites reading `src/framenest/adapters/api/web/app.js`, a path that does not exist, and the JS suite would have failed at the cut that owns the move; smallest correction: none needed, all 29 are repathed and the suite is green at 583/578/0/5, but the Orchestrator should stop issuing per-file targets for this class of change and issue the derivation rule instead.
LEAD: Verification items 4–9 and 12 cannot be produced before the Cooperator's step 4, because `ap exec` validates `provenanceModule` against `sourceRoot` on every invocation and `ap exec` requires a baseline whose `ap.project.conf` matches the worktree; the cheapest useful check is to run `ap exec --baseline 76416ce… --operation runtime-info` immediately after step 4 — it is one command, it proves the new provenance module resolves, and it is the cheapest possible confirmation that the AP contract change is coherent before commissioning the full suite.
```