Everything verified. Final report.

### Report for ORCHESTRATOR_CHAT

**Logical whole:** `kronika-sole-identity` · **Worker session:** 20 · **Exchange:** 01
**Report justification:** `new-mutation`
**Commit:** `0eb6e8e562e6c22c3de4038105b84689e9b1c76b` on local `main`, parent `76416ce08aefb3c8892fc50f52378459f56e8614`. Not pushed. Local `main` is 2 ahead of public `main` (`e1d5ee5`), unchanged.

**Client disclosure:** this client emitted no prose above the header.

---

## 1. The re-derived defect, the element count, and the diff

Re-derived before editing, from the file itself:

```
444:[EXPECTED_FRAMENEST_CONTENT_PATHS: frozenset[str] = frozenset(]
445:[        ".gitignore",]
...
951:[        "tests/youtube_request_cockpit.test.js",]
952:[)]
```

| Measurement | Value |
|---|---|
| Line opening the call | **444** |
| Element lines | **445–951** |
| Total lines in that range | **507** |
| Of those, lines matching `^        "` | **507** (every line is an element; no stray lines) |
| Distinct elements | **507** (no duplicates) |
| Bare closing parenthesis | **952** |

**Element count measured: 507.** Matches the issued figure, so I proceeded.

The neighbouring set shows the intended shape, and I matched it structurally rather than by eye — it closes as `}` then `)`, at 4-space then 0-space indentation:

```
166:[EXPECTED_FRAMENEST_BASENAME_PATHS: frozenset[str] = frozenset(]
167:[    {]
168:[        "deploy/systemd/framenest-ai-credential-nvidia-nim.conf",]
187:[        "scripts/operator/network/framenest_nuc_worker_gate.fish",]
188:[    }]
189:[)]
```

After the edit the repaired set has exactly that shape at 444/445/953/954.

`git diff --numstat` = **`2	0`** — exactly two added lines, **zero deletions**. No existing line modified, reordered, deduplicated or removed:

```diff
@@ -442,6 +442,7 @@ PER_TREE_FRAMENEST_OCCURRENCE_COUNT = {
 # token was dropped, and no file that no longer carries it was retained.
 EXPECTED_FRAMENEST_CONTENT_PATHS: frozenset[str] = frozenset(
+    {
         ".gitignore",
@@ -949,6 +950,7 @@ EXPECTED_FRAMENEST_CONTENT_PATHS: frozenset[str] = frozenset(
         "tests/youtube_request_cockpit.test.js",
+    }
 )
```

## 2. My own `FROZEN_ALEMBIC_SHA256` key count

**36.** Measured by parsing the dict body (lines 127–164) of the file, not from prose:

```
dict body lines: 127..164
pin rows matching ^    "key": "<64hex>"  = 36
distinct keys                            = 36
numbered revisions = 0001 0002 … 0034 0035   plus "__init__.py"
revisions on disk: numbered = 35, total files = 36
```

This confirms session 19's 36 and refutes the 38 previously reported twice. Independently, I SHA-256'd all 36 blobs with `sha256sum`: **36 verified, 0 mismatches**, and the on-disk name set is byte-identical to the pinned key set (no key added or missing). `FROZEN_DOCUMENT_SHA256` likewise: **86 pins, 86 verified, 0 mismatches**.

## 3. Retention module outcome, and the re-pin question

**`15 passed in 0.37s`.** All fifteen tests, listed in §4's sibling modules and reproduced against both baselines (`76416ce` and my own `0eb6e8e`).

**No ledger value moved, because none was wrong.** I did not take the green as proof. A passing module is the module's own measurement, so I re-derived every pin by an independent method (`git grep` for the occurrence and file measures, `sha256sum` for Part A, `grep -E/-P` over an independently built counted-file list) and compared:

| Pin | Committed | My measurement | Method |
|---|---|---|---|
| `PER_TREE_FRAMENEST_FILE_COUNT` src/tests | 186 / 184 | **186 / 184** | `git grep -I -i -l`, ledger excluded |
| …deploy/scripts/docs/extension | 19 / 7 / 88 / 8 | **19 / 7 / 88 / 8** | same |
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT` src/tests | 1695 / 1851 | **1695 / 1851** | `git grep -I -i -o`, ledger excluded by path prefix |
| …deploy/scripts/docs/extension | 212 / 104 / 1216 / 145 | **212 / 104 / 1216 / 145** | same |
| `EXPECTED_FRAMENEST_CONTENT_PATHS` | 507 | **507, set-identical** | textual extraction of the literal vs `git grep -l`; `diff` empty |
| `ENV_PREFIX_TOKEN_COUNT` / `_DISTINCT_NAME_COUNT` | 641 / 100 | **641 / 100** | `grep -o -E 'FRAMENEST_[A-Z0-9_]+'` |
| `ENV_PREFIX_BARE_SPELLING_COUNT` | 21 | **21** | `grep -o -P 'FRAMENEST_(?![A-Z0-9_])'` |
| `MUTATION_HEADER_OCCURRENCE_COUNT` / `_FILE_COUNT` | 73 / 30 | **73 / 30** | `grep -F` |
| `CAPITALIZED_OCCURRENCE_COUNT` / `_FILE_COUNT` | 2742 / 394 | **2742 / 394** | `grep -o -F FrameNest` |
| `HOST_PATH_OCCURRENCE_COUNT` (5) | 204/76/94/21/13 | **204/76/94/21/13** | `grep -o -F` per literal |
| `UNIT_ACCOUNT_OCCURRENCE_COUNT` | 5 / 5 | **5 / 5** | `grep -o -F` |
| `CONSOLE_SCRIPT_ENTRY_COUNT` | 14 | **14** | `grep -o -E 'framenest-[a-z0-9-]+' pyproject.toml` |
| `EXPECTED_FRAMENEST_BASENAME_PATHS` | 20 | **20, set-identical** | `git ls-files` + basename filter |

**There is no old-value/new-value table, because nothing was re-pinned.** All three surviving `FrameNestSettings` provenance comments (lines 1046, 1057, 1066) keep the historical spelling, as required.

Two of my own probes were wrong before the pins were, and both were caught by bounds rather than by the pins (details in *Resolved Execution Issues*). The important one: my first occurrence measurement read **1980** against the pin 1851. Rule 7 applies — 1980 is implausible, so I suspected the probe, and the probe was wrong.

## 4. The seven C3-B verification items

All seven produced with real output. Items 2, 5 and 6 through `ap exec --operation test-focus` with throwaway probes under `/tmp/opencode/`; no probe file is in the repository.

**Item 1 — wheel listing.** Built a real wheel with the repository's own declared tool into a throwaway directory:

```
poetry build returncode = 0
poetry stdout = 'Building kronika (0.1.0)\nBuilding wheel\n  - Built kronika-0.1.0-py3-none-any.whl'
artefacts produced      = ['kronika-0.1.0-py3-none-any.whl']
total archive members   = 329
members starting kronika/   = 292
members starting framenest/ = 0  []
members starting vendor/    = 0  []
dist-info METADATA members  = ['kronika-0.1.0.dist-info/METADATA']
five repathed resources, presence and byte identity vs the checkout:
    present=True   kronika/infrastructure/persistence/alembic_environment/script.py.mako
    present=True   kronika/adapters/api/web/index.html
    present=True   kronika/adapters/api/web/styles.css
    present=True   kronika/adapters/api/web/app.js
    present=True   kronika/infrastructure/ai/fixtures/vision-probe-red-8x8.png
console_scripts entries in the built artefact = 28
repository dist/ exists after build = False
```

`kronika/` present, `framenest/` absent, `vendor/` absent, all five resources present **and byte-identical to the checkout**, and `dist/` was not created in the repository.

**Item 2 — import-level proof.**

```
== part one: no alias installed ==
'framenest' in sys.modules at probe start = False
import framenest                -> ModuleNotFoundError: No module named 'framenest'
import framenest.infrastructure                                   -> ModuleNotFoundError
import framenest.infrastructure.persistence                       -> ModuleNotFoundError
import framenest.infrastructure.persistence.sqlite_batch_fk       -> ModuleNotFoundError
== part two: ADR-0085 alias installed ==
retired names now in sys.modules = ['framenest', 'framenest.infrastructure',
  'framenest.infrastructure.persistence',
  'framenest.infrastructure.persistence.sqlite_batch_fk']
alias     __name__ = kronika.infrastructure.persistence.sqlite_batch_fk
alias is canonical = True
parent framenest       __name__='framenest' has __path__=False
unrelated framenest.infrastructure.persistence.engine -> ModuleNotFoundError
unrelated framenest.domain -> ModuleNotFoundError
unrelated framenest.server -> ModuleNotFoundError
unrelated framenest.adapters -> ModuleNotFoundError
src/framenest exists on disk = False
```

The alias installs idempotently (called twice, no error) and the helper is the *same object*, not a copy.

**Item 3 — fresh migration and populated fixture.**

```
script directory head            = 0035
revisions walk_revisions() count = 35
first / last revision            = 0001 / 0035
fresh database exists before     = False
upgrade_database_to_head status  = at_head / current=0035 / head=0035
alembic_version row              = [('0035',)]
table count in the fresh schema = 37
re-inspect = MigrationStatus(state='at_head', current_revision='0035', head_revision='0035')
---
after first migration, version row   = [('0035',)]
populated devices rows              = [('00000000-0000-4000-8000-000000000001', 'Populated Fixture Device')]
after second migration, status      = at_head / 0035
after second migration, version row = [('0035',)]
version row unchanged                = True
devices rows after second migration = [('00000000-0000-4000-8000-000000000001', 'Populated Fixture Device')]
repository versions dir file count = 36
```

Head stays `0035`, no new migration, 36 revision files untouched.

**Item 4 — synthetic alarm.** With the alias installed, a synthetic revision importing an unrelated retired module **fails**; a control importing the bridged name **succeeds**:

```
synthetic revision load -> ModuleNotFoundError: No module named
  'framenest.infrastructure.persistence.engine'; 'framenest.infrastructure.persistence'
  is not a package
  exc.name = 'framenest.infrastructure.persistence.engine'
control revision using the bridged name loaded, revision = '0036_synthetic_alarm'
  and it imported <function disable_sqlite_foreign_keys_for_batch_rebuild at 0x...>
versions directory file count = 36 (must stay 36)
```

Both synthetic files live in `/tmp/opencode/synthetic_alarm/`. **Nothing was added to the repository**, and the versions directory still holds exactly 36 files with no `0036*`.

**Item 5 — entry-point identity.**

```
[project.scripts] entries declared in pyproject.toml = 28
console_scripts entries installed in the venv      = 28
names carrying the retired spelling                = 14
kronika-server      kronika.server:main                    alias framenest-server      same_object=True
kronika-db          kronika.infrastructure.persistence.cli:main  alias framenest-db      same_object=True
kronika-catalog     kronika.adapters.cli.catalog:main      alias framenest-catalog     same_object=True
kronika-library     kronika.adapters.cli.library:main     alias framenest-library     same_object=True
kronika-dev         kronika.adapters.cli.development:main alias framenest-dev         same_object=True
kronika-ai          kronika.adapters.cli.ai:main          alias framenest-ai          same_object=True
kronika-production  kronika.infrastructure.runtime.production:main  alias framenest-production  same_object=True
kronika-backup      kronika.adapters.cli.backup:main     alias framenest-backup      same_object=True
kronika-youtube     kronika.adapters.cli.youtube:main    alias framenest-youtube     same_object=True
kronika-previews    kronika.adapters.cli.previews:main   alias framenest-previews    same_object=True
kronika-covers      kronika.adapters.cli.covers:main     alias framenest-covers      same_object=True
kronika-recovery    kronika.adapters.cli.recovery:main   alias framenest-recovery    same_object=True
kronika-sidecar     kronika.adapters.cli.sidecar:main    alias framenest-sidecar     same_object=True
distinct callables behind the 13 canonical names = 13
kronika-capture is framenest-chatgpt-page        = True
```

All thirteen pairs resolve to one identical callable object; total 28; `framenest-*` names 14.

**Item 6 — capture identity.**

```
kronika_capture imported from = /home/agile/Projects/kronika/src/kronika_capture/__init__.py
APP_NAME                       = 'kronika-capture'
STATE_DIR_NAME                 = 'framenest-chatgpt-page'
kronika_capture.cli:main       = <function main at 0x...>
```

**Item 7 — the retention module executes and passes.** `15 passed`, against both baselines.

## 5. Full Python counts and JavaScript counts

**Python baseline established for the first time at this tree** (there was none: the suite could not collect):

```
37 failed, 4362 passed, 8 skipped, 2 warnings in 693.01s (0:11:33)
```

This is a real baseline and it is **red**. The full output was not truncated in any classification below; each failing module was re-run individually to obtain its actual assertion output.

**JavaScript — unchanged**, exactly as the Orchestrator measured:

```
ℹ tests 583   ℹ pass 578   ℹ fail 0   ℹ skipped 5
```

## 6. Every failure, individually classified

Two causes, not thirty-seven.

### Cause 1 — caused-by-C3-B — 36 failures, **not fixed**, see §9

**Single root cause: C3-B renamed the production logging namespaces and the `dictConfig` keys, and moved the package, but left a specific class of *test-side* literal naming the old spelling.** Session 19 repathed 29 JavaScript files completely and missed these Python references.

Attribution is not inferred from the failure text. It is established against the commit itself: `git show 76416ce -- src/kronika/structured_logging.py` shows the production additions `"kronika_json"`, `"kronika_stderr"`, `"kronika":`, `getLogger(f"kronika.{component}")`, `logger_name.startswith("kronika")` — while the resolved source lines below still index the old keys. The same commit **did** edit each of these test files (`e1d5ee5..76416ce` numstat: 25/25, 6/6, 18/18, 6/6, 55/55, 13/13, 79/79), so these are partial edits with missed literals — the Python counterpart of the JS repath, not a pre-existing condition. Within `tests/unit/test_structured_logging.py` the smoking gun is that line 23 (`ALLOWED_LOGGING_MODULE = Path("src/kronika/structured_logging.py")`) was repointed while line 24 (`SOURCE_ROOT = Path("src/framenest")`) was not, one line apart.

| # | Test | Stale literal, resolved to its text | Cause |
|---|---|---|---|
| 1–23 | `tests/unit/test_structured_logging.py` (23) | L40 `logging.getLogger("framenest")` → `IndexError: list index out of range`, because `build_uvicorn_log_config()` configures `"kronika"`; L24 `SOURCE_ROOT = Path("src/framenest")` is a **latent** second defect on the same file, unmasked while L40 fails first | logger namespace renamed; adjacent constant repointed, sibling missed |
| 24 | `tests/unit/test_configuration.py::test_database_path_absent_from_settings_repr_logs_api_and_openapi` | L297 `logging.getLogger("framenest")` → same `IndexError` | same |
| 25–26 | `tests/contract/test_public_published_uds.py` (2) | L620 `record.name == "framenest.public_published_api"`, L636 `caplog.at_level("WARNING", logger="framenest.public_published_application")`, L641 → `assert 0 == 1`. Captured log proves production now emits `ERROR kronika.public_published_api` | logger namespace renamed |
| 27–29 | `tests/contract/test_uvicorn_logging.py` (3) | L77/L78 `config["formatters"]["framenest_json"]`, `config["filters"]["framenest_redaction"]`, L89 `config["handlers"]["framenest_stderr"]`, L150 → `KeyError: 'framenest_json'` | dictConfig keys renamed to `kronika_*` |
| 30 | `tests/unit/test_server_runtime.py::test_create_server_passes_framenest_log_config_and_disables_access_log` | L185 `server.config.log_config["formatters"]["framenest_json"]` → `KeyError`; L25 `SOURCE_ROOT = Path("src/framenest")` latent | dictConfig key renamed |
| 31 | `tests/contract/test_workspace_media.py::test_workspace_attribution_modules_are_read_only` | L632 `Path(__file__).resolve().parents[2] / "src/framenest"` → `FileNotFoundError` | package moved |
| 32–36 | `tests/contract/test_kronika_product_string_agreement.py` (5) | L163 `SOURCE_ROOT.glob("framenest/**/*.py")` and L378 `glob("framenest/**/alembic_environment/versions/*.py")`. One stale glob empties `MEASURED`, so `len(MEASURED) == 0` against pinned 50, all 50 inventory rows read as `missing`, duplicates read `{}`, and `versions` reads `[]` | package moved |

Per rule 3, literals inside fixtures were classified separately and are **not** defects: `test_structured_logging.py:343,390` `name="framenest.test"` (synthetic foreign record names), `test_server_runtime.py:310` `"framenest.sock"` (the sidecar suffix, which the ledger comment at lines 380–384 explicitly records as *not* owned by C3-B), and `test_kronika_product_string_agreement.py:22` docstring prose. None of these is an assertion about current identity, and none was touched.

### Cause 2 — not-a-defect, an Orchestrator decision — 1 failure, **not fixable mechanically**

`tests/contract/test_kronika_settings_parity.py::test_the_settings_library_is_unchanged_since_the_restoration_reference`:

```
assert _git_blob(RESTORATION_REFERENCE, "poetry.lock") == _git_blob("HEAD", "poetry.lock")   # passes
assert _git_blob(RESTORATION_REFERENCE, "pyproject.toml") == _git_blob("HEAD", "pyproject.toml")
E   At index 18 diff: b'f' != b'k'
E   - name = "kronika"
E   + name = "framenest"
```

`RESTORATION_REFERENCE = "18c357cf6f8c5ff9cc3b2c28e638510fc73a3672"` is a pinned historical commit, and the docstring states the premise: *"The oracle is licensed only while the library matches the older commit."* C3-B renamed `[project] name`, so a legitimate identity change broke a **licensing anchor**, not a stale reference. Both available "fixes" destroy the oracle: repointing `RESTORATION_REFERENCE` at a post-rename commit makes the comparison HEAD-versus-near-HEAD and re-licenses on a moving target — precisely the tautology the retention module's own docstring refuses at lines 13–14 and 400–402. Choosing a new anchor is an Orchestrator decision above this correction.

**Nothing was suppressed.** No test skipped, xfailed, marked, disabled or deleted by me. The 8 skips are the pre-existing real-tool/NVIDIA gates (`FRAMENEST_RUN_REAL_MEDIA_TOOLS`, `FRAMENEST_RUN_NVIDIA_NIM_SMOKE`).

## 7. `git diff --stat` and the commit SHA

```
$ git diff --stat HEAD~1 HEAD
 tests/contract/test_kronika_identity_retention.py | 2 ++
 1 file changed, 2 insertions(+)

$ git diff --numstat HEAD~1 HEAD
2	0	tests/contract/test_kronika_identity_retention.py
```

Only the reported path. Nothing under `src/kronika/**`, no Alembic revision, no `docs/adr/**`, no `pyproject.toml`, no `poetry.lock`, no new branch, push, tag, merge, rebase or amend. Working tree clean.

**Commit:** `0eb6e8e562e6c22c3de4038105b84689e9b1c76b`

## 8. Post-commit gate

```
$ ./.ap/ap project check --root /home/agile/Projects/kronika --baseline 0eb6e8e562e6c22c3de4038105b84689e9b1c76b
OK project identity: cisarik/kronika
OK environment policy: sanitized-v1
ap project check --baseline: PASS

$ ./.ap/ap exec --baseline 0eb6e8e562e6c22c3de4038105b84689e9b1c76b --operation runtime-info
/home/agile/Projects/kronika/.venv/bin/python
3.13.9 (main, Nov 19 2025, 22:47:49) [Clang 21.1.4 ]
/home/agile/Projects/kronika/src/kronika/__init__.py
```

Both PASS, and `runtime-info` resolves **`src/kronika/__init__.py`**, the renamed provenance module. `ap doctor` PASS throughout; submodule unchanged at `73e20ef80b88700d5fc397cd8edd4fc425869f`. Retention module re-run against my own SHA: `15 passed`.

---

## 9. The one judgement call in this cut, stated plainly

**I did not fix the 36 caused-by-C3-B failures, although the prompt authorises it.** I am flagging this as a deliberate, reversible decision so you can overturn it cheaply.

Reasoning: the prompt's own Completion criteria ask for *a full Python baseline established* and *every failure classified* — not for a green suite — and your acceptance note is written on the premise that this commit changes exactly two lines of one file. Repairing the 36 is not a two-line change: it touches **7 test files and 15 literals**, and because the retention ledger excludes only itself, it forces **three further pins** to move. I sized that cascade rather than guessing:

| Ledger value | Now | After a faithful repoint | Why |
|---|---|---|---|
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["tests"]` | 1851 | **1836** | 15 lowercase occurrences leave the `tests` tree |
| `PER_TREE_FRAMENEST_FILE_COUNT["tests"]` | 184 | **183** | `test_workspace_media.py` has exactly **one** `framenest` occurrence, the stale path at L632, so it leaves the content set |
| `EXPECTED_FRAMENEST_CONTENT_PATHS` | 507 | **506** | same file leaves the set |
| `CAPITALIZED_*`, `ENV_PREFIX_*`, `MUTATION_HEADER_*`, `HOST_PATH_*`, `UNIT_ACCOUNT_*` | — | **unchanged** | every stale literal is lowercase; no `FRAMENEST_`, no `FrameNest`, no header or path marker among them |

The decisive point is that Cause 2 **cannot** be fixed mechanically, so the suite cannot be made green in this cut by any means available to me. Repairing 36 to leave 1 delivers no accepted end state, while making this commit a seven-file test repoint plus a second consecutive ledger re-pin — and its own subject line, *"restore the content-path set literal lost by the C3-B re-pin"*, would become a false description of it. That mismatch, plus your retained sequencing authority over cuts, is why I stopped and reported. Rule 10 cuts the same way: state what cannot be done here rather than fabricate a green run.

**Deviations.** `git add` was used to stage the single authorized file; a commit grant implies staging, and it is the only Git command outside the read-only enumeration. Four probe files were written under `/tmp/opencode/` and one throwaway synthetic revision under `/tmp/opencode/synthetic_alarm/`; nothing else outside the repository changed. The wheel probe invoked `poetry build` as a subprocess — the same mechanism `tests/contract/test_chatgpt_page_packaging.py:84` already uses — writing to a throwaway directory, and I verified `dist/` was not created in the repository. No interpreter was invoked directly by me; every Python result came through `ap exec`.

**Risks.** The suite is red at 37, and 36 of those are C3-B's, so C3-B is not verifiable-green until the follow-up lands. Nothing in the 36 touches production behaviour, so there is no runtime risk, only a broken gate. My independent measurements agree with the module on all 22 pins, so the ledger itself is sound; the residual doubt is Cause 2's intended resolution, which is a decision, not a measurement.

**Missing evidence.** None of the seven items is missing; all seven are in §4 with real output. What is missing is a green Python baseline, for the reason above.

**Smallest next step.** Commission a bounded **C3-C test-side repoint**: 7 files, 15 literals, listed line-by-line in §6 — repoint logger names to `kronika.*`, dictConfig keys to `kronika_json`/`kronika_redaction`/`kronika_stderr`, `src/framenest` → `src/kronika`, `framenest/**` → `kronika/**` — then re-pin exactly three ledger values to 1836 / 183 / 506 from its own measurement, leaving the fixture literals and `framenest.sock` untouched. In the same cut, decide Cause 2. That is one commit with a small, reviewable diff.

## Resolved Execution Issues / Near-Misses

1. **Near-miss, caught by rule 7 — my occurrence probe read 1980 against the pin 1851.** I had excluded the ledger from `git grep -I -i -o` output with `grep -vxF`, which is correct for `-l` (bare paths) but wrong for `-o`, whose lines are `path:match`. The ledger's own 129 occurrences were counted. A 129 gap is suspicious rather than damning, so I measured the ledger directly: `grep -o -i framenest <ledger>` = **129**, and 1980 − 129 = 1851, exactly the pin. Fixed by cutting the path prefix before excluding; all six per-tree counts then matched. **Resolved; the pin was never wrong.**
2. **Near-miss, rule 7 applied twice more — the counted-file list collapsed to 5 entries.** I tested for a NUL byte with `grep -qU $'\0'`, but `$'\0'` expands to the empty string in bash, so the pattern matched everything. **Resolved** by rebuilding the list with `wc -c` against `tr -d '\000' | wc -c`. It then returned **827** files, which I reconciled exactly: 833 tracked − 1 (`.ap` is a gitlink directory, filtered by the module's `is_file()`) − 1 (the ledger) − 4 PNG binaries = 827. The four NUL-bearing files are `icon16/48/128.png` and the vision fixture, all `image/png` by `file`. No text file was wrongly excluded.
3. **Near-miss — my extraction range overran a set literal.** Seeking the closing `}` of the basename set with `/^}/` skipped the 4-space `    }` on line 188 and stopped at line 228, sweeping 40 lines of `PER_TREE_FRAMENEST_FILE_COUNT` into a "60-path" set that then diffed against 20 measured paths. **Resolved** by deriving the range structurally — element lines 168–187, brace 188, paren 189 — and confirming it against the neighbouring set. Part B then matched exactly, 20 paths.
4. **Near-miss — two of my own assertions were wrong before the code was.** I asserted alembic's head was `0035_research_requests_and_accounting`; it is `0035`, because the revision id is the 4-character prefix and the slug lives only in the filename. And my synthetic control revision imported a name `sqlite_batch_fk` that the helper module does not define, raising `ImportError`; I replaced it with `disable_sqlite_foreign_keys_for_batch_rebuild`, the symbol the eleven real revisions actually import. **Both resolved before any claim was made**, and the `alembic_version` row `[('0035',)]` independently confirmed the short form.
5. **Near-miss — a stale code path could have been reported as a second live defect.** `test_structured_logging.py:24` and `test_server_runtime.py:25` still read `Path("src/framenest")`, but no test failed on them, because `getLogger("framenest")` fails first in every affected test. I classified both as **latent** rather than reporting them as observed failures, and confirmed they are genuine C3-B residue from the same partial edit that repointed their adjacent constants.
6. **Disclosure — probe scripts spawn subprocesses.** The wheel probe runs `poetry build` and the ledger's own contract test runs `sys.executable -I -S -B`, both inside the `test-focus` operation. No interpreter was invoked by me directly, and no environment was repaired.

## Pre-Existing Failure Classification

**none.** No failure in this run is pre-existing in the sense of predating C3-B, and I can say so with evidence rather than assertion: Cause 1's 36 failures are all *newly* red because `76416ce` renamed production namespaces and moved the package while leaving those test literals behind, which is visible in the commit's own diff to `src/kronika/structured_logging.py`. At `e1d5ee5` the tests referenced `framenest` and production emitted `framenest`, so they passed. Cause 2's single failure is not pre-existing either — it became red when C3-B renamed `[project] name` — but it is **not-a-defect** rather than a repairable one, because it encodes a licensing anchor whose re-establishment is an Orchestrator decision. The 8 skips are pre-existing, deliberate, environment-gated integration tests and are untouched. No failure was skipped, marked, xfailed, disabled, deleted or suppressed by me.

---

```text
Orchestration critique:
MEASURED: The correction prompt's own risk model was wrong about the Python suite in one direction and right in another. Wrong: it predicted that the two step-4-dependent failures "should now pass" and that the rest of a full-suite run would be "failures that are NOT caused by this cut", so a two-line commit was expected; measured, the suite is 37 red and 36 of those trace to a single C3-B cause — the commit renamed the production logger namespaces (`getLogger(f"kronika.{component}")`, `logger_name.startswith("kronika")`) and the dictConfig keys (`kronika_json`, `kronika_stderr`) and moved the package, but missed the test-side literals naming the old spelling, the exact Python counterpart of the 29 JavaScript files it did repath. Evidence: `git show 76416ce -- src/kronika/structured_logging.py` against the resolved stale lines, plus `e1d5ee5..76416ce` numstat showing each failing test file was edited (25/25, 6/6, 18/18, 6/6, 55/55, 13/13, 79/79) with named literals left behind, and within `test_structured_logging.py` line 23 repointed while line 24, one line away, was not. Effect: C3-B can never be verified green, and the ledger's correctness was asserted by a module that could not be executed, so the first execution had to re-derive all 22 pins independently. Right: rule 7 earned its place — the only reason the Orchestrator saw this defect at all is that 507 positional arguments is an impossible `frozenset` signature, and it earned it again here, since my own probe reported 1980 against a pinned 1851 and the probe, not the pin, was wrong by exactly the ledger's own 129 occurrences. Smallest correction: before commissioning any further identity cut, have the Orchestrator derive the test-side literal inventory mechanically rather than per-file, the way T8's 29 JavaScript files had to be derived after session 19 found the prompt's "one JavaScript test" was wrong by 28.
LEAD: `tests/contract/test_kronika_settings_parity.py` pins `RESTORATION_REFERENCE = 18c357cf...` and asserts HEAD's `pyproject.toml` is byte-identical to it, so any distribution rename permanently breaks a licensing anchor; repointing the anchor makes the oracle tautological, which the retention module's own docstring refuses elsewhere. I did not touch it because I cannot verify which re-anchor the Cooperator intends, and I did not classify it as a defect because it is not one. Cheapest useful check: ask Michal directly whether the settings-library oracle's licence survives the `framenest` → `kronika` distribution rename, or whether it needs re-establishing against a named post-rename commit; that single sentence decides the only failure no mechanical cut can close.
```