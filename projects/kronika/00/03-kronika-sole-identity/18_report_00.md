### Report for ORCHESTRATOR_CHAT

**Logical whole:** `kronika-sole-identity` · **Worker session:** 18 · **Exchange:** 01 · **Task:** KSI-IMPL-C3-A
**Report justification:** `new-mutation`

No preamble was forced by my client surface.

## 1. Repository gate and baselines

| Check | Result |
|---|---|
| Branch / HEAD at start | `main` / `d5955d5c0478ef7fa025fa9f8cba26ef56656883` — matches |
| Working tree at start | clean |
| Submodule | `73e20ef80b88700d5fcbc397cd8edd4fc425869f` |
| Public `main` | `9c71bfb0a06cb30c5d747816e9067f6a25350c58` (local 4 ahead after this commit; **not pushed**) |
| `ap doctor` | PASS, governing variant stable |
| `ap project check --baseline d5955d5` | **PASS** |
| Python baseline, before any edit | **4359 passed, 8 skipped, 3 warnings** (675.11s) — reproduces exactly |
| JavaScript baseline, before any edit | **583 total, 578 pass, 0 fail, 5 skipped** — reproduces exactly |

No stopping condition fired.

## 2. Independent derivation, and the reconciliation you need

Derived by AST parse (not by your enumeration, not by session 16's list), through `./.ap/ap exec --operation test-focus` on a `/tmp` probe: every string node in `src/framenest/**/*.py` was resolved, docstrings excluded, f-string fragments collapsed into their parent `JoinedStr`, and the frozen `versions/` directory excluded.

```text
brand-bearing runtime AST string nodes under src/framenest50
  distinct literals                                            40
  literals occurring more than once                             5
```

Classification of all 50:

```text
 13  already pinned by a behavioural assertion (session 16 §4, confirmed)
  1  deliberately dual-spelled mutation header (tailscale_ingress.py:869)
  2  externally sent AI prompt bodies  -> out of scope, pinned by opening line
 34  UNGUARDED  = your 19 + 15 more
```

**Your count19 is correct and every site is at the line you gave, with the text you gave. Your list is short by fifteen literals**, each brand-bearing, operator- or API-visible, with no assertion of any kind anywhere in `tests/`:

```text
media_alias_api.py:40      "Invalid Kronika media user alias."
x_request_api.py:185       "Invalid Kronika media user alias."
cli/development.py:82 f"Kronika launcher error: {exc}"
cli/development.py:115     "Kronika development log is not yet available."
cli/youtube.py:213 "The loopback Kronika operator API is unavailable."
cli/youtube.py:219         same, second occurrence
configuration.py:461 "Kronika private storage paths must not overlap"
domain/media_cover.py:11   "Invalid Kronika accepted cover."
domain/media_cover.py:12   "Invalid Kronika cover source observation."
domain/media_metadata.py:20 "Invalid Kronika media metadata."
domain/media_user_alias.py:22 "Invalid Kronika media user alias."
domain/uploads.py:14       "Invalid Kronika upload session."
alembic_environment/env.py:11 "Kronika migration connection is unavailable."
production.py:86           "Kronika health check failed."
server.py:147 f"Kronika configuration error: {{exc}}"
```

**Cause, evidenced.** Session 16 §9/§10 demonstrated red-on-revert only for the three categories it was pointed at. It never attempted these fifteen, and every one is genuinely unasserted: `test_production_health.py` asserts `error_code` three times and never `message`; `test_youtube_cli.py` never mentions `YOUTUBE_LOOPBACK_UNAVAILABLE`; `test_cli_sanitizes_runtime_errors` asserts only the exception text, not the `Kronika launcher error:` prefix; `test_cli_missing_log_is_clean` asserts only `"not yet available"`. Per your decision the cut covers all 34.

## 3. AST resolution and measured duplicate counts

Key = `(path, enclosing function, node kind, occurrence index within that function)`. Indices count brand-bearing literals only, so an unrelated edit cannot shift them. Line numbers are never selectors.

Confirmed exactly as you stated: `"Kronika is stopped."` ×**3** in `development.py` (`stop`#0, `stop`#1, `_status_with_state`#0); category-conflict ×**3** in `x_acquisition.py` (`_reject_category_conflict`#0/#1/#2) and ×**1** in `x_request_api.py` (`submit_x_request`#1). Also measured: alias-invalid ×3 (three files), configuration-error ×3 (three files), loopback-refusal ×2 (`youtube.main`#1/#2).

## 4. Where the coverage lives, and why

| File | Content | Why there |
|---|---|---|
| `tests/support/kronika_identity.py` *(new)* | derived brand + independent display-name pin + `expected()` | Mirrors `tests/support/tooling.py`; the only place the derivation lives, shared by eleven files |
| `tests/contract/test_kronika_product_string_agreement.py` *(new)* | 50-entry structural inventory, duplicate and per-file counts, display-name pin, manifest drift, the 5 argparse sites, `env.py:11` | Needs no existing harness; owns the identity source and the whole-tree view |
| `test_development_runtime.py` | 8 branches | Reuses `_runtime`, `_state`, and the established `monkeypatch.setattr(runtime, …)` idiom |
| `test_x_category_conflict.py` | 3 branches | Reuses `_RaceRepository`, `_SuccessfulMixedRepository`, `_MixedMetadata` |
| `test_x_request_api.py`, `test_media_alias_api.py`, `test_development_cli.py`, `test_youtube_cli.py`, `test_production_health.py`, `test_configuration.py`, `test_server_runtime.py`, `test_media_cover.py`, `test_media_metadata.py`, `test_media_user_alias.py`, `test_upload_sessions.py` | 1 site each | Behavioural guards sit next to the machinery that already reaches the branch |

**Alternative rejected:** one monolithic new file. It would have duplicated ~40 lines of runtime machinery and put assertions far from the branches they describe.

## 5. The derived identity source and its independent pin

Mirrors the browser precedent exactly. `BRAND = manifest["name"].split()[0]`; `DISPLAY_NAME = "Kronika X Companion"` is a **separate literal in a separate assertion**. `test_the_extension_display_name_is_pinned_independently_of_the_derived_brand` and the derivation are distinct tests, so a guard that only derived would not be a tautology.

Drift demonstrated **in memory**, no file altered: a manifest named `"Zonet X Companion"` derives `Zonet`, so **zero** of the 50 resolved occurrences match and `require_display_name` raises `AssertionError: the display name is the single product identity`. Both halves proved live against the shipped functions.

## 6. Guard table — all 34 sites, with per-occurrence failure result

Every row: one occurrence mutated alone, focused owning guard run, file restored, `git diff` verified clean. **Two independent mutation kinds were run over all 34.**

| # | Site | Kind | Own guard | Mutation A (`Kronika`→`Zoneta`) | Mutation B (`Kronika`→`FrameNest`) |
|---:|---|---|---|---|---|
| 1 | `cli/development.py:35` | behavioural | agreement description | FAILED 1 | FAILED 1 |
| 2 | `production.py:114` | behavioural | check-health help | FAILED 1 | FAILED 1 |
| 3 | `production.py:118` | behavioural | serve help | FAILED 1 | FAILED 1 |
| 4 | `persistence/cli.py:85` | behavioural | migrate help | FAILED 1 | FAILED 1 |
| 5 | `persistence/cli.py:86` | behavioural | status help | FAILED 1 | FAILED 1 |
| 6 | `development.py:222` | behavioural | already-running | FAILED 1 | FAILED 1 |
| 7 | `development.py:273` | **structural only** | occurrence inventory | FAILED 1 | FAILED 1 |
| 8 | `development.py:314` | behavioural | `stop` **status.message** (line 552) | FAILED 1 | FAILED 1 |
| 9 | `development.py:316` | behavioural | `stop` **result.message** (line 553) | FAILED 1 | FAILED 1 |
| 10 | `development.py:338` | behavioural | stop-after-terminate | FAILED 1 | FAILED 1 |
| 11 | `development.py:355` | behavioural | open-when-stopped | FAILED 1 | FAILED 1 |
| 12 | `development.py:418` | behavioural | status-absent-state | FAILED 1 | FAILED 1 |
| 13 | `development.py:468` | behavioural | status-healthy | FAILED 1 | FAILED 1 |
| 14 | `development.py:479` | behavioural | status-unhealthy | FAILED 1 | FAILED 1 |
| 15 | `development.py:619` | behavioural | held operation lock | FAILED 1 | FAILED 1 |
| 16 | `x_acquisition.py:370` | behavioural | `live is None` | FAILED 1 | FAILED 1 |
| 17 | `x_acquisition.py:374` | behavioural | `len(live) != 1` | FAILED 1 | FAILED 1 |
| 18 | `x_acquisition.py:379` | behavioural | active-claim mismatch | FAILED 1 | FAILED 1 |
| 19 | `x_request_api.py:207` | behavioural | sanitized 409 | FAILED 1 | FAILED 1 |
| 20 | `media_alias_api.py:40` | behavioural | alias API 422 | FAILED 1 | FAILED 1 |
| 21 | `x_request_api.py:185` | behavioural | alias 422 on X route | FAILED 1 | FAILED 1 |
| 22 | `cli/development.py:82` | behavioural | sanitized launcher error | FAILED 1 | FAILED 1 |
| 23 | `cli/development.py:115` | behavioural | log-unavailable | FAILED 1 | FAILED 1 |
| 24 | `cli/youtube.py:213` | behavioural | `_ProtocolError` refusal | FAILED 1 | FAILED 1 |
| 25 | `cli/youtube.py:219` | behavioural | bare `Exception` refusal | FAILED 1 | FAILED 1 |
| 26 | `configuration.py:461` | behavioural | overlapping storage roots | FAILED 1 | FAILED 1 |
| 27 | `domain/media_cover.py:11` | behavioural | rejected cover | FAILED 1 | FAILED 1 |
| 28 | `domain/media_cover.py:12` | behavioural | rejected source observation | FAILED 1 | FAILED 1 |
| 29 | `domain/media_metadata.py:20` | behavioural | rejected metadata | FAILED 1 | FAILED 1 |
| 30 | `domain/media_user_alias.py:22` | behavioural | rejected alias | FAILED 1 | FAILED 1 |
| 31 | `domain/uploads.py:14` | behavioural | rejected session id | FAILED 1 | FAILED 1 |
| 32 | `env.py:11` | behavioural | migration without connection | FAILED 1 | FAILED 1 |
| 33 | `production.py:86` | behavioural | check-health failure | FAILED 1 | FAILED 1 |
| 34 | `server.py:147` | behavioural | configuration error | FAILED 1 | FAILED 1 |

**68 of 68 demonstrations red. Zero sites undemonstrated.**

**The decisive evidence, and a finding you should have.** Under mutation A (`Kronika`→`Zoneta`) the **retention ledger stayed GREEN in all 34 cases** — it counts the *retired* spelling, not the current one, so a wrong-brand rename moves no counter at all. Under mutation B the counter fired in all 34. So the aggregate counter is not merely uninformative about *which* occurrence moved, as session 16 established; for any rename to an equally plausible wrong brand it is **entirely silent**. The per-occurrence guards caught all 68 with the counter contributing nothing.

## 7. Sibling independence (Property 1) and the deleted-duplicate check (Property 2)

Each occurrence of an identical-literal family mutated alone, whole family run:

| Family | Mutated | Failing guards | Failing assertion line |
|---|---|---|---|
| stopped | 314 | **1** | `test_development_runtime.py:552` (`status.message`) |
| stopped | 316 | **1** | `test_development_runtime.py:553` (`result.message`) |
| stopped | 418 | **1** | `test_development_runtime.py:602` (separate test) |
| conflict | 370 / 374 / 379 | **1 / 1 / 1** | three distinct tests |
| loopback | 213 / 219 | **1 / 1** | two distinct tests |
| alias | 22 / 40 / 185 | **1 / 1 / 1** | three distinct tests |

Rows 314 and 316 are the sharpest result: one test owns both, yet each mutation fails a **different assertion line**, so the two identical literals are independently pinned.

Deleted-duplicate demonstration (line removed, not edited):

| Deleted | Structural checks that failed |
|---|---|
| `development.py:314` | **5** — inventory, occurrence count, duplicate counts, per-file counts, no-unpinned-value |
| `x_acquisition.py:374` | **4** — same set |
| `cli/youtube.py:213` | **3** — inventory, occurrence count, duplicate counts |

The count check fails in **either direction**; adding a fourth duplicate fails identically.

## 8. Fixture repair and the fate of every assertion that depended on it

`test_development_cli.py:175` now builds `expected("{brand} is running at {url}", url=_RUNNING_URL)` — the real `:296` shape. Nothing asserted on it before. `test_cli_status_open_and_logs` now asserts `Status: running`, `URL: <url>`, the **derived message**, `opened` and `two`, so the fake is read rather than merely printed. Two other substring assertions became exact-equality (`"not yet available"`, `"sanitized failure"` → full stderr lines). `test_category_conflict_maps_to_sanitized_409` keeps both original assertions; its fake now raises a text the router **discards**, so the assertion can only pass through the router's own literal — this repairs the §4 finding directly. `test_put_alias_maps_unknown_tag_and_invalid_content` and `test_check_health_fails_closed_without_listener` keep every original assertion and gain one.

**No assertion was deleted or weakened.** Every removed line in the diff is one of: the two fixture lines, the fake's discarded text, two substring assertions replaced by exact equality, one assertion restructured to `payload` with its check intact, one import extended.

## 9. The two negative assertions

`tests/integration/test_development_launcher.py:64` and `tests/contract/test_local_web_application.py:1228` — **byte-unchanged**; `git diff HEAD -- ` on both files is **0 lines**.

## 10. Counts, with the arithmetic

| Route | Baseline | Final |
|---|---|---|
| Python declared `test` | 4359 passed / 8 skipped / 3 warnings (675.11s) | **4399 passed, 8 skipped, 3 warnings** (689.12s) — **+40, 0 failed** |
| `node --test tests/*.test.js` | 583 / 578 / 0 / 5 | **583 / 578 / 0 / 5 — identical** |
| Retention module | 15 passed | **15 passed** |
| `ap project check` | PASS at `d5955d5` | **PASS at `e1d5ee5`** |
| Tree | clean | clean |

`+40 = 38` new test functions `+ 2` extra items from the one 3-way parametrised per-file duplicate check. Per file: agreement 19 items (17 defs + 2), `test_development_runtime.py` 8, `test_x_category_conflict.py` 3, `test_youtube_cli.py` 2, `test_media_cover.py` 2, and 1 each in `test_x_request_api.py`, `test_media_metadata.py`, `test_media_user_alias.py`, `test_upload_sessions.py`, `test_configuration.py`, `test_server_runtime.py`. Six existing tests were strengthened without changing their count.

**The JavaScript count did not move**, as required for a cut touching no JavaScript.

## 11. Ledger movement — Part A and Part B did not move

| Entry | Was | Now | Δ |
|---|---:|---:|---:|
| `FROZEN_DOCUMENT_SHA256` (Part A) | 86 keys | 86 keys | **0** |
| `FROZEN_ALEMBIC_SHA256` (Part A) | 38 keys | 38 keys | **0** |
| `EXPECTED_FRAMENEST_BASENAME_PATHS` (Part B) | 20 paths | 20 paths | **0** — no path renamed |
| `PER_TREE_FRAMENEST_FILE_COUNT["tests"]` | 321 | 322 | +1 |
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["tests"]` | 4478 | 4580 | +102 |
| `CAPITALIZED_OCCURRENCE_COUNT` | 3252 | 3264 | +12 |
| `CAPITALIZED_FILE_COUNT` | 474 | 474 | **0** |
| `EXPECTED_FRAMENEST_CONTENT_PATHS` | — | — | +1 path |
| env-prefix / mutation-header / host-path / unit-account / console-script | — | — | **all 0** |

Causes, per file, all attributed in the ledger comment: agreement **+84** (its inventory names all 50 nodes by production path, its imports, and the one dual-spelled header sentence); `test_development_runtime.py` **+4**; `test_server_runtime.py` **+4**; `test_x_request_api.py` **+3**; `test_youtube_cli.py` **+2**; `test_media_cover.py` **+2**; four files **+1** each; `test_development_cli.py` **−1**.

**Part A and Part B explicitly did not move.** The capitalized +12 is eleven Python **class names and import paths** (`FrameNestMediaCoverError`, `FrameNestSettings`, `FrameNestMediaUserAliasError`, `FrameNestConfigurationError`, `FrameNestUploadSessionError`, `FrameNestMediaMetadataError`) that C2d deliberately did not rename and C3-B owns, plus the one dual-spelled header sentence. **No product prose was retired spelling and reintroduced.** The capitalized *file* count is a genuine swap: the repaired fake left it, the new inventory entered it.

## 12. `git diff --stat` and product-file confirmation

```text
16 files changed, 1207 insertions(+), 13 deletions(-)
```

`git diff --cached --name-only HEAD | grep -v '^tests/'` → **empty. Zero product files. Zero `src/`, `extension/`, `deploy/`, `scripts/`, `docs/`, `pyproject.toml`, `ap.project.conf`, ADR or root Markdown.**

## 13. Commit, deviations, risks, next step

**Commit:** `e1d5ee510b4a1532606dba7d2a098aed71c16225` on local `main`, parent `d5955d5c0478ef7fa025fa9f8cba26ef56656883`, subject `test(identity): guard every retired product string occurrence`. Not pushed.

**Deviations, deliberate:** 1. Scope widened from 19 to 34 on your decision. 2. `development.py:273` is **structural only** — its `raise` sits inside the `try` whose own `except Exception:` swallows it and substitutes the fixed `:286` message, so it is **not observable through the public API**. Stated, not faked. 3. The two AI prompt bodies are pinned by their brand-carrying **opening line** plus a pinned exclusion list, not verbatim — a 1000-character body is not product prose, but a one-sided rename inside one still fails here. 4. Six existing tests strengthened; none weakened. 5. Mutation demonstrations used mutate-and-restore-in-tree, because `ap exec` runs under `env -i` with `PYTHONPATH` pinned to the repository `src`, making a mutated `/tmp` copy unreachable through the authorised command.

**Risks.** The structural inventory is line-sensitive by design: a future edit inserting a brand-bearing literal *before* an existing one in the same function shifts the occurrence index and fails loudly. That is intended, but it will read as churn to a later cut. The 13 pins session 16 demonstrated still spell `"Kronika"` literally; this cut did not convert them, so they are covered but not derived. `tailscale_ingress.py:869` and the two prompts remain out of scope by ADR-0085 and by your decision.

**Missing evidence.** No rendered acceptance, no browser, no extension load, no real profile — browser authority `none`. No provider call; the prompt guards are string reads. No NUC contact, no deploy. **The nineteen and fifteen strings are now guarded but still not observed in a terminal**; until C3-B, C4-B, C6 and C8 land, the `nettestované reťazce` C2d left remain read by hand from the release, which is the mitigation you accepted.

**Smallest next step:** accept C3-A and issue C3-B, the atomic package move, on this base — the identity is now enforced rather than merely renamed, and C3-B can move `src/framenest` to `src/kronika` with a guard that will follow the rename automatically because the brand is derived.

## Resolved Execution Issues / Near-Misses

- **The retired-brand mutation pass silently proved nothing on its first run.** My driver verified the mutation with `case "$mutated" in *Zoneta*)`, inherited from the first pass; after I changed the substitution to `FrameNest` every iteration hit `SETUP-ERROR`, so **no test ran** and 15 `src/` files were left mutated. Caught because the per-site progress lines were absent while the TSV had 34 rows — all four fields blank after the first, which is a known-impossible shape. Resolution: corrected the probe to match the substitution actually made, added `< /dev/null` to every `ap exec` invocation so no child can consume the driver table on stdin, re-ran all 34, and `git checkout -- src/` first to clear the residue. Residual risk: none. This is the **fourth** mechanical probe in this logical whole needing a sanity check against a known-impossible output.
- **My first AST probe over-counted 50 nodes as 78**, because it counted module and function docstrings and each f-string's literal fragments separately. A docstring is prose about the code, not a contract, and `"Kronika is running at "` appeared twice for one message. Caught because the count exceeded the 66 raw occurrences in `src/framenest` — impossible. Resolution: excluded docstrings by identity and skipped `Constant` nodes parented by a `JoinedStr`; re-derived 50 and re-checked against the raw grep total. Residual risk: none.
- **`env.py` cannot be imported**: it calls `run_migrations_online()` at module scope, so a plain import attempted a migration and failed collection. Resolution: load the real file with `ast`, withhold only the trailing call — and *assert* that the file still ends with an `Expr` — then `exec` the rest. The guard runs against the shipped source, not a copy.
- **The argparse `help=` text is not in the child's own `--help`.** My first reader asserted on `check-health --help` and got only the usage line. `add_parser(help=…)` renders in the **parent's** subcommand listing. Resolution: read the parent listing with `COLUMNS` pinned, and handle both layouts — proven by a self-check on `check-database-ready`, the one entry argparse wraps.
- **New test files were untracked, so the ledger measured stale counts.** `_counted_paths()` uses `git ls-files`. Resolution: staged the two new files before measuring, then re-measured every Part C entry. Residual risk: none.
- **34 in-place worktree mutations** across three drivers (two mutation passes, one deletion pass), each backed up to `/tmp` and restored, with `cmp` plus `git diff --quiet` verified per site and `git diff --stat -- src/` audited empty at the end of each driver. No suite ran concurrently with a mutation.

## Pre-Existing Failure Classification

**none.** Both baselines reproduced exactly before any edit. Every failure observed during the task is attributable to this cut and expected: the four retention failures after staging were Part C counters correctly detecting my own test-side additions; the `SETUP-ERROR` rows were my driver's probe defect, classified above; and the 68 `FAILED-AS-REQUIRED` results are the *presence* of a failure in guards I was auditing — that presence is the finding. No pre-existing defect was observed, masked or introduced.

```text
Orchestration critique:
MEASURED: the issued list of nineteen is complete and correct as far as it goes,
but the true unguarded set is thirty-four. Evidence: an AST parse of every string
node in src/framenest resolves 50 brand-bearing runtime literals, of which 13 are
already pinned, 1 is the deliberately dual-spelled mutation header, 2 are
externally sent prompt bodies, and 34 carry no assertion anywhere in tests/ --
the issued 19 plus 15 the list omits, including both alias API error payloads,
both loopback-operator refusals, the launcher-error and log-unavailable operator
strings, five domain validation constants, the health-check failure message, the
server configuration error, the storage-overlap refusal and the Alembic connection
error. Cause: session 16 §9/§10 demonstrated red-on-revert only for the three
categories it was pointed at, and `test_production_health.py` asserts error_code
three times without ever reading message. Effect: a Worker trusting the list
literally ships fifteen operator- and API-visible brand strings permanently
unguarded, with a green suite throughout. Second measured finding, larger and
new: the retention ledger is not merely unable to say *which* occurrence moved --
under a rename to an equally plausible wrong brand (`Kronika` -> `Zoneta`) it
stayed GREEN in all 34 cases, because it counts the retired spelling rather than
the current one, while each site's own behavioural guard failed. The aggregate
counter is therefore silent, not merely ambiguous, for the most likely class of
real mistake.
LEAD: none outstanding; the two remaining coverage gaps are classificationdecisions rather than open questions -- the 13 pins session 16 demonstrated still
spell "Kronika" literally instead of using the derived brand, so they are covered
but not rename-following. Cheapest useful check: run one of them, for example
`test_operator_cli_hygiene.py`, through the same mutate-and-restore driver used
here to confirm it fails on a single-occurrence mutation before deciding whether
converting it belongs in C3-B.
```