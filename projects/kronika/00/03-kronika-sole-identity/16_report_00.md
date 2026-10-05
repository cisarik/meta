### Report for ORCHESTRATOR_CHAT

**Logical whole:** `kronika-sole-identity` · **Session:** `16` · **Exchange:** `01` · **Status:** `PASS` · **Result:** `new-mutation`
**Commit:** `d5955d5c0478ef7fa025fa9f8cba26ef56656883` on `main`, parent `77bcb81c8a5f84e91ec4b31dd12f8ad2204016a8`, **not pushed**. Tree clean. Local `main` is three commits ahead of public `main`.

No client preamble was emitted above this header.

---

## 1. Repository gate

All green before editing, and nothing was edited until both baselines had reproduced. Branch `main`, HEAD `77bcb81c8a5f84e91ec4b31dd12f8ad2204016a8`, working tree clean, submodule `73e20ef80b88700d5fc397cd8edd4fc425869f` matching the superproject gitlink, `git ls-remote origin main` = `9c71bfb0a06cb30c5d747816e9067f6a25350c58` (local `main` two commits ahead, as stated). `ap doctor`: **PASS** (governing variant stable). `ap project check --baseline 77bcb81c8a5f84e91ec4b31dd12f8ad2204016a8`: **PASS**.

## 2. My derivation — 96 occurrences, and the full classification

Method: the issued standalone-word derivation, `rg -n -P '(?<![A-Za-z_])FrameNest(?![A-Za-z])' src/framenest`, untruncated. **My count is 96, identical to yours.** Every hit was then classified by opening the line.

**96 = 49 in scope + 47 out of scope.** The 47 out-of-scope residuals are enumerated in full in §7, so a later cut can pick them up knowingly.

In-scope breakdown by carrier: 12 domain validation constants, 6 API/application error-payload occurrences, 18 runtime/CLI message occurrences, 5 argparse help/description strings, 1 configuration error, 1 Alembic-environment error, 1 device display-name default, 2 externally sent AI prompts, 3 further operator-facing strings in `adapters/cli/development.py` and `adapters/cli/youtube.py`.

I also ran a supplementary sweep for the lowercase standalone `framenest` in `src/framenest`, on the C2c principle that a deterministic identifier can be user-visible without carrying the capitalized brand. It produced no additional in-scope prose: the hits are import paths, the env-prefix/host-path keys and the three `framenest-movie-identification-*` / `framenest-media-suggestion-*` schema-version strings, all machine-read and all belonging to C5/C7.

## 3. Reconciliation against the issued list — six sites you missed, one mis-attribution

Your count of 96 was right. Your **list** was short by seven occurrences across three files, and one line was attributed to the wrong string.

| # | Site you did not list | Class | Why it is in scope |
|---|---|---|---|
| 1 | `src/framenest/infrastructure/ai/prompts.py:7` — `f"""You are FrameNest's media metadata assistant.` | **externally sent AI prompt** | Item 8 names only the movie-identification prompt. This is a **second** system prompt, imported at `nvidia_nim.py:57` and embedded in the request body at `nvidia_nim.py:192`, and at `openai_chat_completions.py:49/115`. It leaves the host to two providers. |
| 2 | `adapters/cli/youtube.py:213` — `"The loopback FrameNest operator API is unavailable."` | operator output | Item 3 lists `youtube.py:187` as this string. It is not. |
| 3 | `adapters/cli/youtube.py:219` — identical sentence, second occurrence | operator output | Same. |
| 4 | `adapters/cli/development.py:35` — `description="Control the local FrameNest browser-development server."` | argparse output | This is the **fifth** help/description string. Item 4 lists four sites and your prose says "five"; the fifth is this one, in `adapters/cli/`, not in either runtime file. |
| 5 | `adapters/cli/development.py:82` — `print(f"FrameNest launcher error: {exc}", file=sys.stderr)` | operator stderr | Item 3 lists `server.py:147` but not the sibling launcher stderr line. |
| 6 | `adapters/cli/development.py:115` — `print("FrameNest development log is not yet available.")` | operator stdout | Same file, same class. |

**Mis-attribution, disclosed:** `youtube.py:187` carries `"FrameNest configuration could not be loaded."`, not the loopback-operator sentence. Your item 3 therefore both mislabels line 187 and omits the two lines that actually hold the sentence it names. The practical consequence: had I followed your list literally, the loopback message would have survived this cut entirely.

**One site you classified as neither in nor out of scope:** `src/framenest/infrastructure/ai/configuration.py:173`, `/ "FrameNest"` inside `~/Library/Application Support/FrameNest/ai/config.json`. Your Excluded 7 splits `development.py` but names no other file. I classified it the same way as `development.py`'s paths — a default path expression whose rename orphans an existing file rather than migrating it — and left it for **C4** alongside them. It is not a string, it is a path component.

All seven sites above are changed and reported individually in §5. No stopping condition fired: none of them is machine-read, docstring or deliberately dual.

## 4. The assertion inventory — thirteen is right, but composed wrongly

Your measured total of **thirteen** is numerically correct and **compositionally wrong in two places that happen to cancel**.

Reconciling by opening every candidate line and establishing presence versus absence:

```text
 7  "Invalid Kronika ..." test_media.py:24,25,26  test_libraries.py:25,26
                            test_identities.py:39   test_devices.py:15
 2  "Kronika Server"       test_library_workflow.py:212,227
 2  "Kronika configuration could not be loaded."
                            test_operator_cli_hygiene.py:155,176
 1  "Kronika startup failed. Check logs for details."
                            test_development_runtime.py:235
 1  "Kronika is running"   test_development_launcher.py:51<-- MISSED by the table
--  ------
13  genuine assertion pins        (the domain count is exactly 7, as you measured)

 1  test_x_request_api.py:282 names the category-conflict sentence
 but is NOT an assertion      <-- counted by the table as a pin
```

**Two corrections, netting to your thirteen.**

1. **`test_development_launcher.py:51` is a pin your table omits.** `assert "FrameNest is running" in started.stdout` is a positive presence assertion on `development.py:296`/`468`, which your own in-scope item 3 lists. Your table's row "0 every other in-scope string" therefore contradicts your own item 3. **Your table should have read14.**
2. **`test_x_request_api.py:282` is not a pin.** It is the `raise` argument inside a local `_ConflictService` fake:

```python
class _ConflictService:
    def submit(self, url, login_key, alias=None, content_category=None):
        raise XAcquisitionCategoryConflictError(
            "Requested category conflicts with the existing Kronika save."
        )
...
assert response.status_code == 409
assert response.json()["error"]["code"] == "X_REQUEST_CATEGORY_CONFLICT"
```

The test asserts a status code and an error **code**. It never reads `error["message"]`. `x_request_api.py:204` catches the exception **by class** and substitutes its own literal at `:207`, so the fake's text is discarded. This literal is fixture data, and **the "scoped comparison of an API error payload" your brief describes does not exist.**

**Net effect: fourteen test-side literals repointed, thirteen of which are genuine pins, and the fourteenth (`:282`) changed only to keep the fixture faithful to the product string.** Had I trusted the table literally, `test_development_launcher.py` would have shipped red.

Two false-positive hits examined and correctly left alone, per your Lesson 2 — both **negative**: `test_local_web_application.py:1228` (`assert "FrameNest is running locally" not in html`) and `test_development_launcher.py:64` (`assert b"FrameNest" not in served_root`). The second is now a live tripwire proving the served root carries no retired spelling.

## 5. Before-and-after of every renamed string — 49 occurrences, 23 files

```text
domain/media.py:11            "Invalid FrameNest media."                    -> "Invalid Kronika media."
domain/media.py:12            "Invalid FrameNest media location."           -> "Invalid Kronika media location."
domain/media.py:13            "Invalid FrameNest media relative path."      -> "Invalid Kronika media relative path."
domain/media_cover.py:11      "Invalid FrameNest accepted cover."           -> "Invalid Kronika accepted cover."
domain/media_cover.py:12      "Invalid FrameNest cover source observation." -> "Invalid Kronika cover source observation."
domain/media_metadata.py:20   "Invalid FrameNest media metadata."           -> "Invalid Kronika media metadata."
domain/media_user_alias.py:22 "Invalid FrameNest media user alias."         -> "Invalid Kronika media user alias."
domain/identities.py:9        "Invalid FrameNest identity."                 -> "Invalid Kronika identity."
domain/devices.py:9           "Invalid FrameNest device."                   -> "Invalid Kronika device."
domain/libraries.py:11        "Invalid FrameNest library."                  -> "Invalid Kronika library."
domain/libraries.py:12        "Invalid FrameNest library root."             -> "Invalid Kronika library root."
domain/uploads.py:14          "Invalid FrameNest upload session."           -> "Invalid Kronika upload session."

adapters/api/media_alias_api.py:40   ALIAS_INVALID_MESSAGE = "Invalid FrameNest media user alias."
 -> "Invalid Kronika media user alias."
adapters/api/x_request_api.py:185    "Invalid FrameNest media user alias.", 422
                                                         -> "Invalid Kronika media user alias.", 422
adapters/api/x_request_api.py:207    "Requested category conflicts with the existing FrameNest save."
                                                         -> "... existing Kronika save."
application/x_acquisition.py:370     same sentence        -> "... existing Kronika save."
application/x_acquisition.py:374     same sentence        -> "... existing Kronika save."
application/x_acquisition.py:379     same sentence        -> "... existing Kronika save."

development.py:222   f"FrameNest is already running at {self.url}"        -> f"Kronika is already running at {self.url}"
development.py:273   "FrameNest did not become healthy in time."         -> "Kronika did not become healthy in time."
development.py:286   "FrameNest startup failed. Check logs for details."  -> "Kronika startup failed. ..."
development.py:296   f"FrameNest is running at {self.url}"                -> f"Kronika is running at {self.url}"
development.py:314   "FrameNest is stopped."                             -> "Kronika is stopped."
development.py:316   "FrameNest is stopped."                             -> "Kronika is stopped."
development.py:338   "FrameNest stopped."                                -> "Kronika stopped."
development.py:355   "FrameNest is not running."                         -> "Kronika is not running."
development.py:418   "FrameNest is stopped."                             -> "Kronika is stopped."
development.py:468   f"FrameNest is running at {_url(state.port)}"        -> f"Kronika is running at {_url(state.port)}"
development.py:479   "Managed FrameNest process is running but health is not ready."
 -> "Managed Kronika process is running but ..."
development.py:619   "Another FrameNest runtime operation is in progress." -> "Another Kronika runtime operation ..."

runtime/production.py:86    "FrameNest health check failed."               -> "Kronika health check failed."
adapters/cli/ai.py:720      "FrameNest configuration could not be loaded." -> "Kronika configuration could not be loaded."
persistence/cli.py:70       same sentence,2nd occurrence                 -> "Kronika configuration could not be loaded."
adapters/cli/youtube.py:187 "FrameNest configuration could not be loaded." -> "Kronika configuration could not be loaded."
adapters/cli/youtube.py:213 "The loopback FrameNest operator API is unavailable." -> "... Kronika operator API ..."
adapters/cli/youtube.py:219 same sentence, 2nd occurrence                 -> "... Kronika operator API ..."
server.py:147              f"FrameNest configuration error: {exc}"        -> f"Kronika configuration error: {exc}"

adapters/cli/development.py:35   description="Control the local FrameNest browser-development server."
                                                        -> "... local Kronika browser-development server."
adapters/cli/development.py:82   f"FrameNest launcher error: {exc}"          -> f"Kronika launcher error: {exc}"
adapters/cli/development.py:115  "FrameNest development log is not yet available."
                                                        -> "Kronika development log is not yet available."

runtime/production.py:114  help="Verify the FrameNest listener answers a local /health request."
                                                   -> "Verify the Kronika listener ..."
runtime/production.py:118  help="Run the production FrameNest server in the foreground."
                                                   -> "Run the production Kronika server ..."
persistence/cli.py:85      help="Upgrade the FrameNest database to head."   -> "... the Kronika database to head."
persistence/cli.py:86      help="Inspect the FrameNest database revision."  -> "... the Kronika database revision."

configuration.py:461 "FrameNest private storage paths must not overlap" -> "Kronika private storage paths must not overlap"
alembic_environment/env.py:11  "FrameNest migration connection is unavailable."
 -> "Kronika migration connection is unavailable."
library_workflow.py:21  SERVER_DEVICE_DISPLAY_NAME = "FrameNest Server"  -> "Kronika Server"

movie_identification.py:236  f"You are FrameNest's movie identification assistant."
 -> f"You are Kronika's movie identification assistant."
infrastructure/ai/prompts.py:7  f"""You are FrameNest's media metadata assistant.
                                                          -> f"""You are Kronika's media metadata assistant.
```

Every constant **name**, position and non-brand wording is preserved; every placeholder, punctuation mark and `{...}` field is intact. Machine-checked over the whole diff: **49 added lines, all carrying `Kronika`; 0 added lines carrying the retired brand; 49 removed lines, all carrying the retired brand.**

## 6. The external AI prompts — reported as their own item

**Two** strings in this cut leave the host, not one. Both are string edits; **no provider was contacted** and network authority is `none`.

1. **`application/movie_identification.py:236`** — `You are FrameNest's movie identification assistant.` The site named by item 8.
2. **`infrastructure/ai/prompts.py:7`** — `You are FrameNest's media metadata assistant.` **Absent from the issued list.** It is `MEDIA_SUGGESTION_PROMPT`, imported by `nvidia_nim.py:57` and `openai_chat_completions.py:49`, and joined into the outbound request body at `nvidia_nim.py:192` and `openai_chat_completions.py:115`.

Neither was restructured, no instruction other than the brand word changed, and no f-string placeholder was touched. Both now name Kronika to the provider. This is the only externally visible consequence of the cut and the Cooperator must be told about both.

## 7. Residual enumeration — zero user-visible or operational occurrences remain

`src/framenest` standalone-word derivation after the change: **47**, and all 47 are out of scope. **Zero user-visible, operator-facing or API-reachable occurrences of the retired brand remain.**

| Class | Count | Sites |
|---|---|---|
| Docstrings (Excluded 4) | 33 | `__init__.py:1`; `configuration.py:1`; `server.py:1`; `infrastructure/__init__.py:1`; `domain/__init__.py:1`; `domain/identities.py:1,104,110`; `domain/devices.py:34`; `media_analysis/process.py:1`; `ai/nvidia_nim.py:689`; `application/__init__.py:1`; `persistence/cli.py:1`; `upload_validation_coordinator.py:78`; `persistence/migrations.py:1`; `alembic_environment/__init__.py:1`; `persistence/errors.py:1`; `catalog_backup_offdevice.py:591`; `catalog_schema.py:1`; `versions/__init__.py:1`; `env.py:1`; `cli/development.py:1`; `cli/backup.py:1`; `runtime/__init__.py:1`; `cli/recovery.py:1`; `structured_logging.py:1,148`; `cli/catalog.py:1`; `persistence/__init__.py:1`; `runtime/development.py:1`; `web/__init__.py:1`; `tailscale_ingress.py:3`; `api/application.py:1` |
| Comment (Excluded 4) | 1 | `adapters/api/upload_api.py:605` |
| Path expressions (Excluded 7 / C4) | 7 | `development.py:720,726,741,747,758,763`; **`ai/configuration.py:173`** (unclassified by the brief) |
| Frozen revisions (Excluded 5) | 3 | `versions/0001:17`, `0002:30`, `0003:56` |
| Alembic scaffolding (Excluded 6) | 1 | `script.py.mako:19` |
| Deliberately dual-spelled (Excluded 1) | 1 | `tailscale_ingress.py:869` |
| Mutation header (Excluded 2) | 1 | `adapters/api/web/app.js:437` |
| **Total** | **47** | |

## 8. Revert demonstrations — 13 of 13 genuine pins demonstrated Method: back the file up under `/tmp`, revert **only that one line's** brand word, run the focused test that owns it, restore, verify the diff. No suite was running while the worktree was mutated.

| Site | Focused test result on revert |
|---|---|
| `domain/media.py:11` | **8 failed**, 38 passed |
| `domain/media.py:12` | **11 failed**, 35 passed |
| `domain/media.py:13` | **12 failed**, 34 passed |
| `domain/libraries.py:11` | **8 failed**, 33 passed |
| `domain/libraries.py:12` | **23 failed**, 18 passed |
| `domain/identities.py:9` | **88 failed**, 38 passed |
| `domain/devices.py:9` | **18 failed**, 8 passed |
| `library_workflow.py:21` → pin `:212` | **1 failed** |
| `library_workflow.py:21` → pin `:227` (persisted row) | **1 failed** |
| `persistence/cli.py:70` → pin `:155` | **1 failed** |
| `youtube.py:187` → pin `:176` | **1 failed** |
| `development.py:286` → `test_development_runtime.py:235` | **1 failed**, 32 passed |
| `development.py:296` → `test_development_launcher.py` | **1 failed** |

**13 of 13 demonstrated red. `test_library_workflow.py:227` passes, so the new default genuinely reaches the persisted `devices.display_name` row through `devices.list_all()[0]` — the most valuable assertion in the cut, as you said.**

## 9. The category-conflict sentence — four of four unpinned, not three of four

Your brief instructs: "show that reverting **only one of the four** occurrences turns its pin red." **That demonstration is impossible, and I am reporting that rather than performing a fake one.** Measured, one occurrence reverted at a time against `test_x_request_api.py`:

```text
occurrence 1/4  x_acquisition.py:370    17 passed     <-- green
occurrence 2/4  x_acquisition.py:374    17 passed     <-- green
occurrence 3/4  x_acquisition.py:379    17 passed     <-- green
occurrence 4/4  x_request_api.py:207    17 passed     <-- green
```

**All four revert green, including the one your brief calls the scoped pin.** The cause is §4: `test_x_request_api.py:277-289` asserts only `status_code == 409` and `error["code"] == "X_REQUEST_CATEGORY_CONFLICT"`, and `x_request_api.py:204` catches by class and substitutes its own literal. There is **no behavioural assertion on this sentence at any of its four sites** — the true figure is **four of four unpinned**, not three of four.

Running the wider suite with occurrence 1/4 reverted does produce `2 failed`, and both failures are the **retention ledger's own counters** (`{'src': 2920} != {'src': 2919}` and `3253 != 3252`). That is a mechanical whole-tree occurrence **count**, not a behavioural pin: it notices that *an* occurrence moved, it cannot tell a correct rename from a wrong one, and it says nothing about the other three. This is the weak-pin defect class in its purest form.

**Enumeration proof that all four were changed**, since no red test can establish it:

```text
x_acquisition.py:370  "Requested category conflicts with the existing Kronika save."
x_acquisition.py:374  "Requested category conflicts with the existing Kronika save."
x_acquisition.py:379  "Requested category conflicts with the existing Kronika save."
x_request_api.py:207  "Requested category conflicts with the existing Kronika save."

retained spelling anywhere in src/framenest: 0 occurrences
```

## 10. The five argparse help/description strings — no demonstration is possible

Stated plainly, as instructed. **All five have zero coverage; there is no assertion on any of them, so none can be demonstrated failing on revert.** Verified by reverting each and re-running the owning suite:

```text
help 1/5  production.py:114 check-health      10 passed   <-- green
help 2/5  production.py:118 serve             10 passed   <-- green
help 3/5  persistence/cli.py:85 migrate       10 passed   <-- green
help 4/5  persistence/cli.py:86 status        10 passed   <-- green
help 5/5  cli/development.py:35 description   43 passed   <-- green
```

`test_operator_cli_hygiene.py` asserts only that `--help` **succeeds**; it never reads the text. These five renames are free **and unverified**: no test will catch a mistake, and no test will fail if one is forgotten. The only evidence they carry is the enumeration in §5 and the diff review in §11.

**Same class, found independently:** `development.py:468` (`f"Kronika is running at {_url(state.port)}"`) also reverts **green** under the launcher's own pin (`1 passed`), because `test_development_launcher.py` exercises the `start` path at `:296`, not the status/restart path at `:468`. So of the twelve in-scope `development.py` messages, **2 are pinned (`:286`, `:296`) and 10 are unpinned** (`:222`, `:273`, `:314`, `:316`, `:338`, `:355`, `:418`, `:468`, `:479`, `:619`).

## 11. Exact diff of every path — 33 paths, all reported

`git diff --stat 77bcb81..HEAD` — no path outside this table.

| Path | ± | Purpose |
|---|---|---|
| `domain/media.py` | +3 −3 | item 1 |
| `domain/media_cover.py` | +2 −2 | item 1 |
| `domain/libraries.py` | +2 −2 | item 1 |
| `domain/media_metadata.py` | +1 −1 | item 1 |
| `domain/media_user_alias.py` | +1 −1 | item 1 |
| `domain/identities.py` | +1 −1 | item 1 |
| `domain/devices.py` | +1 −1 | item 1 |
| `domain/uploads.py` | +1 −1 | item 1 |
| `adapters/api/media_alias_api.py` | +1 −1 | item 2 |
| `adapters/api/x_request_api.py` | +2 −2 | item 2 |
| `application/x_acquisition.py` | +3 −3 | item 2, 3 of 4 occurrences |
| `adapters/cli/youtube.py` | +3 −3 | item 3 (+2 missed) |
| `adapters/cli/development.py` | +3 −3 | **missed**, incl. help 5/5 |
| `adapters/cli/ai.py` | +1 −1 | item 3 |
| `server.py` | +1 −1 | item 3 |
| `infrastructure/runtime/development.py` | +12 −12 | item 3, messages only |
| `infrastructure/runtime/production.py` | +3 −3 | items 3 and 4 |
| `infrastructure/persistence/cli.py` | +3 −3 | items 3 and 4 |
| `infrastructure/persistence/alembic_environment/env.py` | +1 −1 | item 6 |
| `infrastructure/ai/prompts.py` | +1 −1 | **missed**, external prompt |
| `application/movie_identification.py` | +1 −1 | item 8 |
| `application/library_workflow.py` | +1 −1 | item 7 |
| `configuration.py` | +1 −1 | item 5 |
| `tests/unit/domain/test_media.py` | +3 −3 | 3 repoints |
| `tests/unit/domain/test_libraries.py` | +2 −2 | 2 repoints |
| `tests/unit/application/test_library_workflow.py` | +2 −2 | 2 repoints |
| `tests/contract/test_operator_cli_hygiene.py` | +2 −2 | 2 repoints |
| `tests/unit/domain/test_identities.py` | +1 −1 | 1 repoint |
| `tests/unit/domain/test_devices.py` | +1 −1 | 1 repoint |
| `tests/unit/infrastructure/runtime/test_development_runtime.py` | +1 −1 | 1 repoint |
| `tests/contract/test_x_request_api.py` | +1 −1 | fixture, **not a pin** |
| `tests/integration/test_development_launcher.py` | +1 −1 | **the missed14th literal** |
| `tests/contract/test_kronika_identity_retention.py` | +57 −2 | ledger re-pin |

**Product diff is 49 lines and nothing but the brand word.** No executable statement, condition, signature, import, constant name, path expression or schema changed. `extension/**`, `adapters/api/web/**`, all 36 Alembic revisions, `script.py.mako`, `pyproject.toml`, `ap.project.conf`, `AGENTS.md`, `docs/**`, `deploy/**`, `scripts/**`, `.gitmodules` and `.gitignore` **do not appear in the diff at all.**

## 12. Excluded 1 through 7 — byte-identity totals, every one `+0`

Occurrence multisets compared `77bcb81` against the working tree, one occurrence per line so nothing collapses:

```text
TOKEN 77bcb81  WORK  DELTA
X-FrameNest-Request                              71     71     +0   (Excl 2, header)
FrameNest or Kronika mutation header             1      1     +0   (Excl 1, dual)
framenest-companion.v1                             7      7     +0   (Excl 2)
framenest-companion.web.v1                        14     14     +0   (Excl 2)
FrameNest migration downgrades ...                4      4     +0   (Excl 5 x3 + Excl 6)
FrameNestSettings                                505    505     +0   (Excl 3)
FrameNestConfigurationError                       29     29     +0   (Excl 3)
FrameNestJsonFormatter                            15     15     +0   (Excl 3)
FrameNestIdentityError                           110    110     +0   (Excl 3)
FrameNestDeviceError                              20     20     +0   (Excl 3)
FrameNestLibraryError                             25     25     +0   (Excl 3)
SERVER_DEVICE_DISPLAY_NAME                         2      2     +0   (name preserved)
```

**Excluded 1 verified textually** — `tailscale_ingress.py:869` still reads `"The FrameNest or Kronika mutation header is required "`, carrying **both** spellings. Untouched.

**Excluded 5 verified byte-identical**, all 36 revisions compared individually by SHA-256: **`compared=36 changed=0`**. Independently, **no file under `versions/` appears in the diff at all** (`git diff --name-only` count `0`), and the only `alembic_environment` path in the diff is `env.py` (item 6).

**Excluded 6 verified byte-identical**: `script.py.mako` = `ffc02af24b1a60fb64fcabf5f99e886d5bd28c8adaa85059d2cc2c0855182c61`, base and work. Not in the diff.

**Excluded 7 verified**: `development.py:720,726,741,747,758,763` all still carry `FrameNest` as a path component. Machine-checked over the whole product diff for `Library|xdg|Application Support|/ "|Logs`: **no path expression appears anywhere.**

## 13. Ledger movement, with cause

Measured with the ledger's own helpers — values read out of its assertion diffs — then cross-checked per file.

| Pin | Was | Now | Cause, verified |
|---|---|---|---|
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["src"]` | 2968 | **2919** | **−49**, exactly my 49 product occurrences, one per changed line |
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["tests"]` | 4492 | **4478** | **−14**, exactly my 14 repointed literals |
| `CAPITALIZED_OCCURRENCE_COUNT` | 3315 | **3252** | **−63** = −49 product − 14 tests; **no offset**, because this cut added no guard, no negative assertion and no comment inside a counted path |
| `CAPITALIZED_FILE_COUNT` | 477 | **474** | **−3**, the three files that lost their last capitalized name (§14) |
| `PER_TREE_FRAMENEST_FILE_COUNT` | — | **unmoved** | no tree gained or lost a file |
| `EXPECTED_FRAMENEST_CONTENT_PATHS` | — | **unmoved** | **no path left the set**; the three files in `CAPITALIZED_FILE_COUNT` all still carry lowercase `framenest` in an import path, so they remain correctly present |

**Part A and Part B did not move.** Part A's `FROZEN_DOCUMENT_SHA256` (86 entries) and `FROZEN_ALEMBIC_SHA256` (38 entries) passed untouched. Part B's `EXPECTED_FRAMENEST_BASENAME_PATHS` is unmodified and passed — **no path was renamed.** `extension`, `deploy`, `scripts` and `docs` occurrence counts are unmoved because this cut touches no JavaScript and no document.

Provenance comments added for every movement, in the file's existing convention, including the per-file arithmetic. Retention module: **15 passed** after re-pin and **15 passed** after commit.

## 14. Baseline and final counts

| Route | Baseline | Final |
|---|---|---|
| Python declared `test` | 4359 / 8 / 3 (660.09s) | **4359 passed, 8 skipped, 3 warnings** (660.90s) — **+0 tests** |
| `node --test tests/*.test.js` | 583 / 578 / 0 / 5 | **583 total, 578 passed, 0 failed, 5 skipped** — **unchanged** |
| Retention module | 15 passed | **15 passed** |
| `ap project check --baseline d5955d5…` | — | **PASS** |
| `ap doctor` | PASS | PASS |
| Tree | clean | clean |

**The JavaScript count did not change**, as required for a cut that touches no JavaScript. The Python count not moving is itself evidence: no test was added or removed, and this is a pure string substitution.

## 15. Deviations, risks, missing evidence

**Deviations, deliberate:**

1. **Changed seven occurrences your list omits**, reported individually in §3: `infrastructure/ai/prompts.py:7`, `adapters/cli/youtube.py:213,219`, `adapters/cli/development.py:35,82,115`. All are operator-facing or externally sent prose and fall under the membership test. The `prompts.py` one is the significant addition.
2. **Repointed 14 literals, not 13**, and classified one of them as fixture data rather than a pin.
3. **Used line-targeted `sed` rather than in-place edits** for the 49 product and 14 test substitutions, driven by a script carrying the enumerated line numbers. Chosen because `x_acquisition.py` holds the identical sentence three times, which makes whole-string replacement unsafe, and because line targeting makes it structurally impossible to touch a docstring, comment or path expression. Every hunk was then read back in full (§11) and machine-checked (49/49 brand-word-only).
4. **Left `test_development_cli.py:175` unchanged.** It holds `message="FrameNest is running."` inside a fake `RuntimeStatus`. It is test fixture data, not product prose and not an assertion, so it is outside the membership test; nothing fails without changing it, and changing it would buy no verification. **It is now an unrepresentative fake** and is listed below as a residual.
5. **Corrected my own ledger provenance comment mid-task.** My first version predicted `CAPITALIZED_FILE_COUNT` would not move; it moved by −3. Replaced with the measured value and the three named files.

**Risks:**

- **Fifteen in-scope strings are renamed with zero test coverage**: the 5 argparse help/description strings, the 10 unpinned `development.py` messages, and the 4 category-conflict occurrences. **19 of the 49 product changes are unverified by any behavioural test.** The enumeration in §5 and the diff review in §11 are the only evidence. A later cut should add a per-site agreement guard of the kind session15 built for the browser surfaces.
- **The retention ledger's occurrence counter is a weak pin** for exactly this cut: it fires on *that* something moved, never on *what* it moved to, and one of four occurrences trips it as readily as four of four.
- **`ai/configuration.py:173` remains an unclassified default path** that no exclusion class names. It now sits beside `development.py`'s paths as C4 work, but it is not written down anywhere in the cut sequence. It should be added to the C4 scope.
- **`test_development_cli.py:175`'s stale fake** will diverge further from the real message at C3/C4.
- **The stored NUC device name is still `FrameNest NUC`.** Unchanged by this cut, as you stated: the code default was never used on that host. The separate operator data operation remains yours and must follow the deploy.

**Missing evidence:**

- **No rendered acceptance, no browser, no extension load, no real profile** — browser authority is `none`. Nothing in this cut is pixel-proven.
- **No provider call.** Both AI prompt edits are string edits. Neither prompt has been seen by a model.
- **No NUC contact and no deploy**, by design. The NUC still serves a pre-C2c revision and `main` is now three commits ahead of public `main`.
- **`FrameNest Server` as a *displayed* device name is not proven on any real host**, only through the fake repository in `test_library_workflow.py`.
- Scratch files under `/tmp/opencode/c2d` only: `edit.sh`, `repoint.sh`, `revert-demo.sh`, `unpinned-demo.sh`, `backup/`, `base-tokens.txt`. Nothing in the worktree or the commit depends on any of them. `rm` is unavailable in this environment, so nothing was deleted; all scratch state is confined to that directory.

## Resolved Execution Issues / Near-Misses

- **A defective revision-comparison probe would have reported all 36 frozen Alembic revisions as changed.** I compared `git show <rev>:<f> | sha256sum` against `sha256sum <f>`, which yields `<hash>  -` versus `<hash>  <path>` — the trailing filename field differed, so all 36 printed `CHANGED` despite being untouched. Caught because 36/36 is an implausible result for a cut that provably does not touch them. Resolution: re-ran with `cut -d' ' -f1` on both sides, giving **`compared=36 changed=0`**, then confirmed independently that `git diff --name-only` over `versions/` returns zero paths. Residual risk: none. This is the third time in this logical whole that a mechanical probe needed a sanity check against a known-impossible number.
- **My first ledger provenance comment asserted a file-count movement of zero and was wrong.** `CAPITALIZED_FILE_COUNT` moved 477 → 474. I had reasoned that every touched file still carries a capitalized name somewhere; three did not. Resolution: measured which three by per-file before/after counts (`prompts.py` 1→0, `test_operator_cli_hygiene.py` 2→0, `test_library_workflow.py` 2→0), re-pinned, and rewrote the comment to name them and to explain why all three remain in `EXPECTED_FRAMENEST_CONTENT_PATHS`. Residual risk: none — and it is the reason the content-path test still passes while the capitalized count moved.
- **The revert driver's `sub`/`demo` helpers each had one shell defect that a first run would have hidden**: `sed -i -e "$@"` double-prefixed `-e`, and `sed -n "24,25,26p"` is not a valid address list. Both surfaced immediately as `SETUP-ERROR`/usage output rather than as a silent wrong edit, because the driver asserts the revert took before running anything. Resolution: corrected both. Residual risk: none.
- **13 in-place worktree mutations across two drivers** (revert demos, unpinned demos). Each was backed up under `/tmp` and restored. I verified restoration after each driver by re-counting the diff (`33 files, 49 product lines, 0 added lines carrying the retired brand`) and again after commit (tree clean). Residual risk: none.
- **A `test_library_workflow.py` test name I guessed for the revert demo did not exist**; I looked it up and used `test_declined_add_plan_leaves_all_state_unchanged_before_confirmation`, which owns the `:212` pin. Had I not looked it up, pytest would have errored on an unknown node id and I might have misread that as a demonstration failure.
- **I did not run a Python enumeration probe for the inventory.** `ap exec` exposes only `runtime-info`, `test` and `test-focus`, none of which runs arbitrary Python, so the derivation was done by regex plus reading each file. Stated so the method is not mistaken for a parse.

## Pre-Existing Failure Classification

**none.** Both baselines reproduced exactly before any edit: Python `4359 passed, 8 skipped, 3 warnings` and JavaScript `583 total, 578 passed, 0 failed, 5 skipped`. Every failure observed during the task is attributable to this cut and was expected: the 2 initial retention failures were the ledger correctly detecting my own renames, the 2 failures during the category-conflict probe were that same ledger's counters, and the `DID-NOT-FAIL` entries in §9 and §10 are the *absence* of a failure in tests I was auditing — that absence is the finding, not a broken test. No pre-existing defect was observed, masked or introduced.

## 16. Smallest next step

Before C3, add one Python agreement guard in the shape session 15 built for the browser surfaces: derive the expected brand from the single identity rather than spelling it, and assert that each of the **19 currently unverified in-scope sites** — the five argparse help strings, the ten unpinned `development.py` messages and the four category-conflict occurrences — carries it, with the category-conflict check counting **all four** occurrences so a partial rename fails. That converts the three measured coverage gaps in this cut from an enumeration argument into a test, and it is the same per-site discipline §8 already relies on.

---

Orchestration critique:
MEASURED: The issued site list was short by seven occurrences across three files, and one line was attributed to the wrong string. Evidence: `src/framenest/infrastructure/ai/prompts.py:7` is a **second externally sent system prompt** (`MEDIA_SUGGESTION_PROMPT`, imported at `nvidia_nim.py:57` and `openai_chat_completions.py:49`, embedded in the outbound request bodies at `nvidia_nim.py:192` and `openai_chat_completions.py:115`), entirely absent from an item 8 that declares itself the only site leaving the host; `adapters/cli/youtube.py:213` and `:219` hold `"The loopback FrameNest operator API is unavailable."`, which item 3 assigned to line `187` — a line that actually carries `"FrameNest configuration could not be loaded."`, so the loopback message would have survived the cut intact; and `adapters/cli/development.py:35,82,115` supply the fifth argparse description plus two operator strings, which item 4's four-line list omits even though the prose says "five". Separately, `infrastructure/ai/configuration.py:173` is a default path expression belonging to C4 that no exclusion class names. Effect: a Worker trusting the list literally ships two externally-visible prompts unrenamed and a loopback-operator error message unchanged, with green tests throughout. Second measured finding, larger: **the assertion inventory's total of thirteen is right but its composition is wrong in two cancelling ways.** `tests/integration/test_development_launcher.py:51` (`assert "FrameNest is running" in started.stdout`) is a genuine positive pin on `development.py:296/468`, which item 3 itself lists, so the table's row "0 every other in-scope string" contradicts the brief's own scope and the real figure is fourteen; while `tests/contract/test_x_request_api.py:282` is not a pin at all but the `raise` argument of a local fake, in a test that asserts only `status_code == 409` and `error["code"]`, with `x_request_api.py:204` catching by class and substituting its own literal at `:207`. Consequently **all four** category-conflict occurrences lack a behavioural assertion, not three of four: reverting each one individually leaves `test_x_request_api.py` at `17 passed`, and the only red signal in the wider suite is the retention ledger's whole-tree occurrence *count*, which cannot distinguish a correct rename from a wrong one. The brief's step-6 instruction to "show that reverting only one of the four turns its pin red" is therefore impossible as written. Smallest correction: for every remaining identity cut, derive the site list by parsing each artefact rather than by reading a prose enumeration, **resolve every listed line to its literal text before classifying it** (that one read would have caught `youtube.py:187`), and when counting pins require the counted line to sit in an assertion context — a literal in a fixture is not a pin; then re-pin per occurrence, never per file or per function.

LEAD: The Cooperator will run `framenest-dev start` and `framenest-db --help` for the first time since the rename, and both the banner and the subcommand help are among the fifteen strings this cut changed with **zero test coverage** — so if either was mistyped the failure is a typo in a terminal he reads, discovered by him rather than by the suite. Evidence: all five argparse help/description strings revert green (`10 passed`, `43 passed`), and the ten unpinned `development.py` messages include every message `framenest-dev status`, `restart` and `logs` prints; `development.py:468` reverts green even under the launcher's own pin because the test exercises the `start` path at `:296` only. Effect: he sees `Kronika is running at …` in one code path and, if `:468` were wrong, a stale word in another, with no test able to say so; the ledger's occurrence counter would still read green. Cheapest useful check: before the deploy, print the five `--help` outputs and the four `framenest-dev` message paths from the release and read them, since the strings are short and this is the only surface no test reaches — and, if the Orchestrator accepts the extra cost, add the §16 guard so the next cut in this family is not verified by enumeration.