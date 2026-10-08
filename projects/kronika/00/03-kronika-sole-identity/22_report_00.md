All verification complete. Writing the terminal report.

### Report for ORCHESTRATOR_CHAT

**Logical whole:** `kronika-sole-identity` · **Worker session:** 22 · **Exchange:** 01
**Report justification:** `new-mutation`
**Commit:** `b16ea2c719f46e167c579c34ddd87a915b70cb00` on local `main`, parent `6e89328640fe5477e08f17f4c31c9fc4bf261238`. Not pushed. Public `main` is still `6e893286…`; local `main` is 1 ahead, divergence 0 0. Tree clean, submodule unmoved at `73e20ef80b88700d5fcbc397cd8edd4fc425869f`.
**Client disclosure:** none; this client emitted no prose above the header.

---

## 1. Derivation, reconciliation with the sample, and uncovered sites

**Method — parsing, never prose.** Four throwaway probes under `/tmp/opencode/ksi22/`, each run through `./.ap/ap exec --operation test-focus`, all parsing with `ast`:

| Probe | What it parses | Result |
|---|---|---|
| `test_derivation.py` | `deploy/ubuntu/framenest_release.py` for marker literals, marker-constant references, pointer/lock builder call sites and every `ssh(...)` site with its enclosing function; `src/kronika/**/*.py` for every comparison against a `*_RESULT_SCHEMA_VERSION` / `*_PROMPT_VERSION` constant and every writer keyword; every file under `scripts/operator/` | §1.1–§1.4 |
| `test_attribution.py` | every `tests/**/*.py` for an identifier of each derived site; `FROZEN_ALEMBIC_SHA256`; the Part B basename set | §1.5, §10 |
| `test_full_delta.py`, `test_host_delta.py`, `test_env_delta.py` | every tracked path at `6e89328` against the working tree, per path | §10 |
| `test_part_c.py` | the ledger's own measurement helpers | §10 |

**Rule 7 check (probe against a known-impossible number).** `test_attribution.py` compares its `FROZEN_ALEMBIC_SHA256` count with the on-disk `versions/` file set and prints both; the two probes that disagreed with each other mid-run were discarded rather than reasoned about (§"Resolved Execution Issues").

### 1.1 Marker sites (category A1), per path

**String literals carrying a marker name: 8.** Four are the constant definitions (43, 44, 48, 49); four are call sites:

| Line | Literal | Classification | Action |
|---|---|---|---|
| 547 | `/{release_path}/.framenest-release-manifest.json` | **in-scope-this-cut (C5 owns the spelling, C4-A owns the literal)** | now `cmd_remote_write_markers` uses `RELEASE_MANIFEST_MARKER`; the writer spelling is byte-identical |
| 548 | `/{release_path}/.framenest-release-sha` | same | now `RELEASE_SHA_MARKER` |
| 1665 | `{target}/.framenest-release-sha` (`_cmd_rollback`) | **in-scope-this-cut** | removed; replaced by the shared resolver |
| 1783 | `{target}/.framenest-release-sha` (`_cmd_capture_transition`) | **in-scope-this-cut** | removed; replaced by the shared resolver |

**Marker-constant references: 21.** 11 were inside the two accepted tuples that no longer exist, 2 in `make_manifest` (writer, unchanged), 2 in the probe (now the resolver),2 in the read builders (now marker-parameterised), 2 in the writer builder, 2 in `manifest_release_sha`.

**Post-cut measurement, regenerated:** the committed `kronika_release.py` contains exactly **6** marker-name literals — the two writer constants and the four accepted-table entries, each declared once. `test_marker_readers_never_open_a_literal_marker_name` parses the file and asserts that exact multiset, so a seventh literal fails. The retained `framenest_release.py` now carries **0**.

### 1.2 Durable analysis identities (category A2)

**Readers found by parsing: 6 comparisons.** All six were in scope:

| Site | Comparison | Layer |
|---|---|---|
| `companion_review_repository.py:791` | `result_schema_version == RESULT_SCHEMA_VERSION` | persistence, SQL |
| `media_suggestion.py:259` | `self.prompt_version != PROMPT_VERSION` (`MediaSuggestionRequest`) | application |
| `media_suggestion.py:355` | `self.prompt_version != PROMPT_VERSION` (`MediaSuggestion`) | application |
| `movie_identification.py:61` | `self.prompt_version != MOVIE_IDENTIFICATION_PROMPT_VERSION` | application |
| `movie_identification.py:63` | `self.result_schema_version != MOVIE_IDENTIFICATION_RESULT_SCHEMA_VERSION` | application |
| `movie_identification.py:352` | `self.prompt_version != MOVIE_IDENTIFICATION_PROMPT_VERSION` (`MovieIdentificationRequest`) | application |

**Writers found by parsing: 9**, in `media_analysis_lifecycle.py` (3), `media_suggestion.py` (1), `movie_identification.py` (2), `movie_identification_lifecycle.py` (1), `nvidia_nim.py` (1), `still_frame_smoke.py` (1). **All nine are untouched (C5).** Post-cut re-parse: **0 comparisons** remain against a durable identity constant, and the writer set is still exactly 9 — `test_the_writer_sites_are_untouched_by_this_cut` asserts both from the parsed tree.

`VISION_PROBE_PROMPT_VERSION` (`infrastructure/ai/vision_probe.py:20`) was found and **excluded, with cause**: it is a request/response identity for an administrative capability probe, is never persisted (no `vision_probe` reference in `application/` or `infrastructure/persistence/`), and therefore has no historical rows. Rule 9, not rule 3.

### 1.3 Pointer and lock sites (category A3), deduplicated call sites

| Builder | Sites | Classification |
|---|---|---|
| `cmd_remote_atomic_switch` | 1508 (deploy), 1632 (`_rollback`), 1674 (rollback) | **3 web-pointer switch sites → guard** |
| `cmd_remote_atomic_switch_capture` | 1835 | capture pointer only; out of scope for the web guard |
| `cmd_remote_readlink_current` | 1038, 1543, 1800 | in-scope-this-cut (readers) |
| `cmd_remote_read_manifest` | 1049, 1077, 1791, 1804, 1821 | in-scope-this-cut |
| `cmd_remote_probe_release_markers` | 1045 | in-scope-this-cut |
| `cmd_remote_read_release_sha` | 1055, 1786 | in-scope-this-cut |
| `cmd_remote_read_optional_link` | 1071, 1813 | in-scope-this-cut |
| `cmd_remote_mkdir_deploy_dir` | 1346, 1669 | in-scope-this-cut (reclaimable lock) |
| `cmd_remote_rm_deploy_dir` | 1531, 1685 | in-scope-this-cut |

**Every web-pointer switch site now runs the guard, and both rollback readiness and the guard run ahead of the switch.**

### 1.4 `scripts/operator/` (category A4)

All **7** files parsed. **Zero** marker sites and **zero** identity sites anywhere under `scripts/operator/`. Only `framenest_nuc_worker_gate.fish` carried NUC-SSH text, and it read the old names **directly at lines 254–257 with no prefix resolution at all** — the sample's claim, confirmed by reading those lines.

### 1.5 Reconciliation against the issued sample

| Issued claim | Measured | Agree? |
|---|---|---|
| hardcoded marker literals at 547, 548, 1665, 1783 | exactly those four, plus four constant definitions | yes |
| no `ExecStart`/`ExecStartPre` reference anywhere in the engine | 0 references; no guard existed | yes |
| `_successful_generic_predicates` ends in an equality filter | `companion_review_repository.py:791` | yes |
| both schema constants are written into the database | 2 result-schema constants + 2 prompt-version constants, 9 writer sites | yes, and the sample's "two constants, not one" understates it: **four** durable identities |
| `read_optional_release_sha` called at 1249, 1535, 1687 | confirmed | yes |
| `mkdir` has no `-p`; gate at 1346 raises before the `finally` at 1683 | confirmed; the deploy path had no `finally` at all | yes, and worse than stated: deploy had **no** cleanup path, not a late one |
| `FROZEN_ALEMBIC_SHA256` has **36** keys | **measured 36** = 35 revisions + `__init__.py`, key set equal to the 36 on-disk version files | yes |

**Two differences I must state.** (a) The sample lists two schema constants; the derivation finds **four** durable identities, because the prompt-version constants are durable too and the sample's own scope text names "prompt-version aliases". (b) The prompt's claimed four *literal* instances are correct, but the derivation also found the four **constant definitions**, so the real count of marker-name literals was 8 and it is 6 after this cut.

### 1.6 Sites no test exercised at the baseline

Attribution probe over all `tests/**/*.py`:

| Site | Evidence |
|---|---|
| `read_current_release` | **0** test files reference it; driven only indirectly through `main()` |
| `read_optional_release_sha` | reached by status/deploy/rollback, but **every** fake answered `test -L … capture-current` with `absent`, so its manifest-reading branch never executed — latent |
| `_successful_generic_predicates` | **0** references. Exercised only in the matching spelling, so no test fails if it is narrowed or the constant is swapped. **This is the data-hiding defect** |
| marker literals at 1665 and 1783 | only matched incidentally by fake string tests; never asserted |
| `cmd_remote_mkdir_deploy_dir` | **0** references by name; behaviour covered only by the literal `"mkdir -m 0700 /run/framenest-release-deploy"`, so nothing covered the absence of `-p`, a reclaim, or a refusal |
| `cmd_remote_probe_release_markers` | 2 tests pinned its **command text**; none drove a tree carrying both spellings, none drove disagreement |
| the 5 application identity comparisons | construction tests existed per value object, but the only negative assertions used values that were never accepted, so narrowing any of them to one constant fails nothing |

---

## 2. `git diff --stat`, commit SHA, and `src/kronika/**`

```
 AGENTS.md                                          |  26 +-
 deploy/ubuntu/framenest-release                    |  27 +-
 deploy/ubuntu/framenest_release.py                 | 1883 +---------------
 deploy/ubuntu/kronika-release                      |  29 +
 deploy/ubuntu/kronika_release.py                   | 2337 ++++++++++++++++++++
 docs/WORKER_EXECUTION_CONTRACT.md                  |  12 +-
 scripts/operator/network/framenest_nuc_worker_gate.fish | 422 +---
 scripts/operator/network/kronika_nuc_worker_gate.fish  | 497 +++++
 src/kronika/application/media_suggestion.py        |  18 +-
 src/kronika/application/movie_identification.py    |  16 +-
 src/kronika/domain/analysis_identities.py          |  46 +
 src/kronika/domain/media_analysis_runs.py          |   7 +
 src/kronika/domain/media_classification.py         |  16 +
 src/kronika/infrastructure/persistence/companion_review_repository.py | 9 +-
 tests/contract/test_kronika_capture_services.py    |  44 +-
 tests/contract/test_kronika_cli_and_release_readers.py | 105 +-
 tests/contract/test_kronika_durable_analysis_identity_readers.py | 698 ++++++
 tests/contract/test_kronika_identity_retention.py  | 106 +-
 tests/contract/test_nuc_release_docs.py            |  91 +-
 tests/contract/test_nuc_release_remote_contract.py | 678 +++++-
 tests/contract/test_nuc_release_source_contract.py |   6 +-
 tests/contract/test_operator_network_scripts.py    | 221 +-
 tests/contract/test_worker_execution_contract.py   |  10 +-
 23 files changed, 4856 insertions(+), 2448 deletions(-)
```

**Commit `b16ea2c719f46e167c579c34ddd87a915b70cb00`**, one commit, parent `6e89328640fe5477e08f17f4c31c9fc4bf261238`, no amend, not pushed.

**Yes, six `src/kronika/**` files appear**, and each is required by in-scope §6:
- `domain/analysis_identities.py` (**new**) — the one symmetric acceptance rule; carries **zero** `framenest` occurrences, so it does not enter the ledger's `src` counts.
- `domain/media_analysis_runs.py`, `domain/media_classification.py` — the canonical spelling and accepted set beside each writer constant, which is the only writer-identity line untouched.
- `application/media_suggestion.py`, `application/movie_identification.py` — five reader comparisons.
- `infrastructure/persistence/companion_review_repository.py` — the SQL filter, `.in_(sorted(ACCEPTED_RESULT_SCHEMA_VERSIONS))`.

**No `FrameNest*` class, name or hierarchy was renamed. No routine host constant changed** — `SERVICE`, `SERVICE_USER`, `SERVICE_GROUP`, `RELEASE_ROOT`, `CURRENT`, `CAPTURE_CURRENT`, `ENV_FILE`, `REMOTE_DEPLOY_DIR`, both tooling paths and the capture state directory are byte-identical, which is why `/etc/framenest` and `/var/lib/framenest` occurrence counts did not move at all. `lookup_env`'s `FRAMENEST_` fallback is unchanged. No migration was added; head stays `0035`; `poetry.lock` untouched.

---

## 3. Marker matrix across every reader

One command, data-driven: `cmd_remote_release_marker_presence` reports **per spelling** (`manifest` lines then `sha` lines, accepted order), and `read_release_markers` reads **every** present spelling and requires agreement. Disagreement raises the new `EXIT_MARKER_CONFLICT = 24`.

| Row | status | check | rollback | capture activation | Result |
|---|---|---|---|---|---|
| former manifest only | PASS | PASS | PASS | PASS | identity = the declared release |
| canonical manifest only | PASS | PASS | PASS | PASS | same identity |
| former SHA only | PASS | PASS | PASS | — | same identity, `release_manifest: absent` reported |
| canonical SHA only | PASS | PASS | PASS | — | same |
| both, equal | PASS | PASS | PASS | PASS | same |
| **two SHA markers disagree** | **24** | **24** | **24** | — | refused, no switch |
| **two manifests disagree** | **24** | **24** | **24** | — | refused |
| **SHA marker vs manifest disagree** | **24** | **24** | **24** | — | refused |
| canonical SHA vs canonical manifest disagree | **24** | **24** | **24** | — | refused |
| none present | `EXIT_TRANSPORT`, "current release SHA marker and manifest are absent" | idem | idem | idem | refused |
| unexpected marker name in the probe output | `EXIT_TRANSPORT`, "current release markers are unreadable" | idem | idem | idem | closed parser |

Reader set covered: current-release status, optional capture pointers (`read_optional_release_sha` → `CAPTURE_CURRENT` and the capture-transition link), manual rollback, automatic rollback (`_rollback`), capture activation and rollback, and release-manifest identity checks. `test_every_reader_resolves_under_each_marker_matrix_row` asserts `active_release:` / `current_release:` / `web_release:` per command per row; `test_every_reader_fails_closed_on_disagreeing_markers` asserts exit 24 **and** that no `ln -s` occurred.

**Data-driven, not constant-dependent:** the accepted tables are literal tuples, and `test_every_reader_resolves_through_the_accepted_marker_tables` asserts the writer constants are members of them, so the tables cannot drift from the writers. The remote engine filename under `/run` stays `framenest_release.py` deliberately, because `docs/UBUNTU_NUC_DEPLOYMENT.md` publishes that artefact name and `test_nuc_operator_runbook.py` pins it.

---

## 4. The installed-unit executable guard

**Shape.** `cmd_remote_unit_execution_properties()` → `sudo -n systemctl show --property=ExecStart --property=ExecStartPre framenest.service` (effective configuration, drop-ins included). `unit_executables_from_show()` extracts **only the `path=` field** of each command per property, decoding systemd's C-style escapes; `argv[]` entries are arguments and are never read. `release_scoped_console_script()` maps an executable to a release-relative console script only under `<CURRENT>/.venv/bin/…` or `<RELEASE_ROOT>/<40-hex>/.venv/bin/…`; anything else returns `None` and is an **unknown effective execution form**. `verify_unit_executables()` then requires each candidate with `sudo -n sh -c 'test -f P -a ! -L P -a -x P'` (`! -L` is what rejects a symlink, since `test -f` follows symlinks) and prints the resolved set. **New exit code `EXIT_UNIT_EXEC_GUARD = 25`.**

**The five demonstrations, actual assertions and outputs:**

1. **Target lacking the executable, explicit deploy** — `missing_executables={"framenest-production"}` → `assert result == engine.EXIT_UNIT_EXEC_GUARD` (25); `"ln -s" not in transcript`; `"restart framenest.service" not in transcript`; `runner.switched == []`. The guard runs *outside* the rollback-wrapped block, so a guard failure propagates without attempting a rollback.
2. **Automatic rollback** — `test_automatic_rollback_is_guarded_before_it_switches` asserts the rollback's guard index `<` the rollback's `ln -s` index, after the deploy's switch. `test_automatic_rollback_refuses_a_previous_release_it_cannot_start` makes the *previous* release's executable absent: result `EXIT_ROLLBACK` and `runner.switched == [TARGET]` — the deploy switch happened, **the rollback switched nothing**.
3. **Drop-ins** — a drop-in shape `{…} { path=/bin/sh ; argv[]=/bin/sh -c 'exec …/kronika-production serve' }` yields `ExecStartPre == (framenest-production, /bin/sh)`, and `/bin/sh` maps to `None`, i.e. refused. Manual rollback and capture-transition guard placement is asserted by `test_rollback_refuses_a_target_lacking_the_installed_unit_executable`.
4. **Symlink rejected** — `symlinked_executables={".venv/bin/framenest-production"}` → 25, no switch.
5. **Unknown execution form fails before switching** — `ExecStart={ path=/usr/bin/python3 ; argv[]=/usr/bin/python3 -m kronika.server }` → 25, no switch, no restart; and a unit with no `ExecStart` at all → 25.

Also proven: `release_scoped_console_script` returns `None` for `/bin/sh`, `/usr/bin/python3`, a non-`.venv/bin` release path, a site-packages path, a non-hex release directory and the empty string.

**Limitation, stated plainly.** This is E2 repository evidence with a fake command runner. **The guard has not been exercised against a live systemd on the NUC**, and the effective-property parse is written against systemd's documented `path=` format rather than against observed host output. Rule 10: I cannot demonstrate it on the host; I say so.

---

## 5. The reclaimable deploy lock

**Shape.** The ownership record is `/run/framenest-release-deploy.owner`, a **sibling** of the deploy directory, so the documented artefact set inside the deploy directory stays exactly the three the runbook publishes. Its content is `<32-hex nonce> <pid> <epoch seconds> <hostname>` — an identity, not a secret; no path, no host address, no credential, and it is never printed.

`acquire_deploy_lock` tries `sudo -n mkdir -m 0700` first. On failure it reads the record and calls `classify_deploy_lock_owner`, which returns a reason or `None`:

- **`own-identity`** — the record names this very run's nonce and pid.
- **`abandoned-owner`** — the record was written by this workstation, is older than the 60-second bound, **and its recorded pid is no longer alive** (`os.kill(pid, 0)` → `ProcessLookupError`).
- **`None` (refuse)** — unreadable/absent/malformed record, a different hostname, younger than the bound, or a live pid.

Reclamation is a single atomic `sudo -n mv -T <deploy dir> <deploy dir>.reclaimed-<reason>` followed by a fresh `mkdir`; the quarantine is removed by the release step. A refusal raises `EXIT_EXISTS` with a stated reason: *"existing remote lock without readable ownership"*, *"existing remote lock owned by another run"*, or *"existing remote lock could not be reclaimed"*. Success prints `remote_lock: reclaimed (abandoned-owner)`.

**Why it is safe.** `pid not alive` on the recording host implies the owning process is gone, because a live run keeps its pid — so a live run can never be stolen from. Cross-host locks are **always refused**, because liveness cannot be established there. There is no "if it exists, delete it" path anywhere.

**Demonstrations** (all in `test_nuc_release_remote_contract.py`):

| Case | Result |
|---|---|
| owner-less stale lock | `EXIT_EXISTS`, *"existing remote lock without readable ownership"*, no switch, no restart |
| lock whose record names **this** live process on this host | `EXIT_EXISTS`, *"owned by another run"*, and **no `mv -T`** |
| lock whose recorded pid is certainly dead | `EXIT_OK`, `remote_lock: reclaimed (abandoned-owner)`, `mv -T` present, quarantine removed |
| reclaim move fails | `EXIT_EXISTS`, *"could not be reclaimed"* |
| this run's own recorded identity | `classify_deploy_lock_owner(owner, owner) == "own-identity"`, and `None` for a different owner |
| failure inside the operation (`migration-required`) | `runner.locked is False` and the owner file removed — **the deploy path now releases the lock on every exit path**, which it never did before |

**Residual, stated.** The pre-existing lock the Orchestrator observed has **no** owner record (it predates this mechanism), so it will be **refused**, not reclaimed. That is the accepted safe outcome; the smallest remedy is a separately authorised `sudo -n rmdir /run/framenest-release-deploy`, which is outside my authority. Second residual: pid reuse on a shared hostname could in principle mislead the check; the 60-second age bound and the hostname equality narrow it, and I did not add a boot identity.

---

## 6. Durable analysis-identity equivalence

**Both constants named in the prompt, and the two more the derivation found:**

| Identity | Writer spelling (unchanged) | Canonical spelling (readers only) |
|---|---|---|
| `RESULT_SCHEMA_VERSION` | `framenest-media-suggestion-result-v1` | `kronika-media-suggestion-result-v1` |
| `MOVIE_IDENTIFICATION_RESULT_SCHEMA_VERSION` | `framenest-movie-identification-result-v1` | `kronika-movie-identification-result-v1` |
| `PROMPT_VERSION` | `framenest-media-suggestion-v4` | `kronika-media-suggestion-v4` |
| `MOVIE_IDENTIFICATION_PROMPT_VERSION` | `framenest-movie-identification-prompt-v2` | `kronika-movie-identification-prompt-v2` |

**The rule** lives once, in `domain/analysis_identities.py`: `accepted_durable_identity(current, canonical)` returns `frozenset({current, canonical})` and **raises** on an empty or identical pair, so a cut that forgets to change a writer cannot silently collapse the pair. `is_accepted_durable_identity(value, accepted)` is `isinstance(value, str) and value in accepted` — a **symmetric membership test**, not an equality against a current spelling. Symmetry is proven explicitly per identity: `is_accepted(canonical) == is_accepted(current)` is `True`, and seven rejected values (`""`, `"framenest"`, `"not-v1"`, `None`, `1`, `current + "x"`, `canonical.upper()`) are all refused.

**Readers covered, all six:** the SQL membership filter; `MediaSuggestionRequest.__post_init__`; `MediaSuggestion.__post_init__`; `MovieIdentificationSuggestion.__post_init__` (prompt **and** result schema); `MovieIdentificationRequest.__post_init__`.

**Historical-row demonstration.** A successful run stored under the **former** spelling stays reviewable: `test_a_successful_run_stays_eligible_under_either_stored_spelling[stored-under-the-former-spelling]` inserts a run with the former spelling into a real SQLite catalog at head and gets `opened_run_id == HISTORICAL_RUN` from `mark_opened`; the canonical-spelling parametrisation returns the same. `test_a_run_under_an_unknown_schema_stays_ineligible` proves the widening did **not** admit `not-v1` (raises `CompanionReviewRunNotEligibleError`). `test_the_predicate_returns_the_same_rows_for_either_spelling` builds two independent catalogs and asserts the identical returned run. `test_the_inbox_filter_is_not_a_single_constant_comparison` parses `_successful_generic_predicates` and asserts `in_(` plus `ACCEPTED_RESULT_SCHEMA_VERSIONS` and the absence of `== RESULT_SCHEMA_VERSION`. Application-layer readers are proven in both spellings and against three unknown spellings each.

**Correction to the prompt's description.** The prompt says the filter "hides rows from the companion **inbox**". Measured: `_successful_generic_predicates` gates `_load_history_page` and `_require_eligible_run` — i.e. opening/reviewing a run — **not** `list_inbox`; the pre-existing repo test even asserts a `not-v1` row *is* in the inbox list. The data-hiding defect is real and the fix is the same; the affected surface is run eligibility, not inbox listing.

**C5 simulation.** The tests prove both stored spellings are returned by the same query *after* the writer constant changes, because the accepted set is frozen data independent of the writer constant. I did not monkeypatch a constant, which would have tested the monkeypatch rather than the production filter.

---

## 7. Both entry points, both gate paths, and the three-variable matrix

**Entry points** — canonical engine2337 lines at `deploy/ubuntu/kronika_release.py`; retained wrapper49 lines that `exec`s the canonical engine; retained module a compatibility alias that `os.execv`s the canonical engine and exposes its names.

| Invocation | Result |
|---|---|
| `./deploy/ubuntu/kronika-release status` | `kronika-release: SSH target is required`, exit 2 |
| `./deploy/ubuntu/framenest-release status` | identical output and exit 2 |
| `.venv/bin/python deploy/ubuntu/framenest_release.py status` | identical |
| `.venv/bin/python deploy/ubuntu/kronika_release.py status` | identical |

No NUC contact in any of them: they stop at `_resolve_transport`.

**Gate paths** — `scripts/operator/network/kronika_nuc_worker_gate.fish` holds the logic; `framenest_nuc_worker_gate.fish` is a 17-line wrapper that `exec`s it. `test_both_gate_paths_reach_the_same_gate` asserts identical return code, stdout and stderr, and `test_scripts_contain_no_forbidden_commands` runs over both.

**The three-variable matrix** (`test_operator_network_scripts.py`, hermetic: `fish --no-config` plus a synthetic environment):

| Environment | Canonical gate | Retained wrapper |
|---|---|---|
| only `KRONIKA_NUC_SSH_*` | exit 0, `operator-user@nuc-magicdns-name` in the ssh log | identical |
| only `FRAMENEST_NUC_SSH_*` | exit 0, same | identical |
| both, different values | **exit 2**, `Conflicting environment variables KRONIKA_NUC_SSH_TARGET and FRAMENEST_NUC_SSH_TARGET are set to different values`, **neither value disclosed**, ssh log empty | identical |
| both, identical values | no conflict, same as plain | identical |
| primary explicitly empty | treated as unset → *"Missing bounded remote command."* exit 2 | — |
| test hooks under either prefix | honoured (parametrised ×2 prefixes ×2 paths) | identical |

CLI flags still override the environment, the probe path is unchanged, and missing-value exit stays 2.

**Hermeticity finding, and a change I had to make.** The retained gate wrapper re-execs its target **through the target's shebang**, which starts a new `fish` that does **not** inherit `--no-config`. Three baseline tests passed for the wrong reason: the developer's own `~/.config/fish/config.fish` supplied `FRAMENEST_NUC_SSH_*`, and the gate silently passed with exit 0 instead of refusing the missing target. `_run_fish` now points `HOME`, `XDG_CONFIG_HOME` and `XDG_DATA_HOME` at a synthetic per-test root (`test_either_gate_path_never_sees_the_operator_configuration_root` asserts the operator's real roots are never in scope). I chose **not** to force `--no-config` inside the wrapper, because that would change production behaviour for an operator whose variables come from `config.fish` — a change I cannot verify and was not authorised.

---

## 8. Documentation changes, exact paths

- `AGENTS.md` — the NUC gate bullet now names `kronika_nuc_worker_gate.fish` as canonical and states that the retained wrapper and the `FRAMENEST_NUC_SSH_*` names keep working, that canonical names take precedence, that a conflicting pair fails closed with exit 2, and that both spellings are removed only in the C7-B window. The release section now names `deploy/ubuntu/kronika-release` and `deploy/ubuntu/kronika_release.py` as the entry point and engine, states that both retained wrappers forward identical arguments and are removed in C7-B, and requires `kronika-release status` / `kronika-release check --release<SHA>` while noting the retained spelling still runs the same two commands.
- `docs/WORKER_EXECUTION_CONTRACT.md` — the canonical SSH-agent route now names `kronika_nuc_worker_gate.fish`, states the four canonical variable names and their precedence, the `FRAMENEST_NUC_SSH_*` fallback, the exit-2 conflict naming only the two variable names, and that both the name and the retained wrapper are removed only in the C7-B window.

**Not touched, deliberately** (out of the in-scope list, and each still correct because the old names keep working): `docs/UBUNTU_NUC_DEPLOYMENT.md`, `deploy/ubuntu/README.md`, `scripts/operator/network/README.md`, `docs/OPERATOR_NETWORK.md`, `README.md`, `SERVER.md`, `SECURITY.md`, `docs/INFOSEC.md`, `docs/ACCEPTANCE_DUAL_AUDIENCE.md`. Frozen ADR bodies 0001–0084 and all36 Alembic files are untouched.

---

## 9. Full Python and JavaScript counts, with per-file attribution

**Python, declared `test` operation, at commit `b16ea2c`:**

```text
4493 passed, 8 skipped, 3 warnings in 717.37s (0:11:57)
```

Baseline was `4399 passed, 8 skipped, 3 warnings`. **+94, same skips, same warnings, zero failures.**

| File | tests added | tests removed | net definitions |
|---|---:|---:|---:|
| `tests/contract/test_nuc_release_remote_contract.py` | 22 | 1 | +21 |
| `tests/contract/test_kronika_durable_analysis_identity_readers.py` (new) | 18 | 0 | +18 |
| `tests/contract/test_operator_network_scripts.py` | 7 | 0 | +7 |
| `tests/contract/test_nuc_release_docs.py` | 5 | 0 | +5 |
| `tests/contract/test_kronika_cli_and_release_readers.py` | 4 | 3 | +1 |
| `test_kronika_capture_services.py`, `test_nuc_release_source_contract.py`, `test_worker_execution_contract.py` | 0 | 0 | 0 (repointed only) |
| **net definitions** | | | **+52** |

The remaining **+42** are parametrized cases of the new tests (marker matrix ×3 commands ×5 rows, four disagreement rows ×3 commands, the guard demonstrations, the identity matrices, the gate prefix matrices). **52 + 42 = 94**, which reconciles exactly. The eight changed or added files collect to **335 passed** when run together. **No test was removed from the suite**; the 4 "removed" definitions in the two files above were the stale probe-contract tests replaced by the four that pin the new presence command and its closed parser.

**JavaScript, `node --test tests/*.test.js` at commit `b16ea2c`:**

```text
ℹ tests 583 ℹ pass 578   ℹ fail 0   ℹ skipped 5
```

**Unchanged from the baseline** (583/578/0/5). This cut touches no JavaScript, so any movement would have required justification; there is none.

**Retention module: 15 passed.**

---

## 10. Ledger movements, measured, with Part A and Part B confirmed unmoved

Every number below is **regenerated at report time** from the committed tree by `test_part_c.py` and `test_full_delta.py` / `test_host_delta.py` / `test_env_delta.py`, which compare each tracked path at `6e89328` against the working tree per path.

**Part A — unmoved.** `FROZEN_DOCUMENT_SHA256` **86** keys; `FROZEN_ALEMBIC_SHA256` **36** keys = **35 numbered revisions `0001`–`0035` plus `__init__.py`**, and the key set **equals** the 36 on-disk files in `versions/`. Both Part A tests pass against the unchanged pins.

**Part B — unmoved.** Measured basename set size **20**, identical to `EXPECTED_FRAMENEST_BASENAME_PATHS`. `deploy/ubuntu/framenest_release.py` is deliberately retained (see §"Deviations"), `deploy/ubuntu/framenest-release` is retained, and `scripts/operator/network/framenest_nuc_worker_gate.fish` is retained; `deploy/ubuntu/kronika_release.py`, `deploy/ubuntu/kronika-release` and `scripts/operator/network/kronika_nuc_worker_gate.fish` are canonical names and therefore carry no `framenest` basename.

**Part C — file counts**

| Tree | Before | After | Δ |
|---|---:|---:|---:|
| `src` | 186 | **186** | 0 |
| `tests` | 183 | **184** | +1 |
| `deploy` | 19 | **20** | +1 |
| `scripts` | 7 | **7** | 0 |
| `docs` / `extension` | 88 / 8 | 88 / 8 | 0 |

`deploy`: `kronika_release.py` joins, `kronika-release` joins, `framenest-release` **leaves** (the retained wrapper no longer names the retired engine file) → +2 −1. `scripts`: the retained gate wrapper leaves, the canonical gate joins → 0. `tests`: the new durable-identity file joins → +1.

**Part C — occurrence counts**

| Tree | Before | After | Δ |
|---|---:|---:|---:|
| `src` | 1695 | **1695** | 0 |
| `tests` | 1835 | **1871** | +36 |
| `deploy` | 212 | **201** | −11 |
| `scripts` | 104 | **86** | −18 |
| `docs` / `extension` | 1216 / 145 | 1216 / 145 | 0 |

Per-path causes, all measured:
- `deploy` −11 = `framenest_release.py` −49 and `kronika_release.py` +41 (same file at two names, so the move is −8), `framenest-release` −4, `kronika-release` +1.
- `scripts` −18 = retained gate wrapper −20 (it no longer reads any `FRAMENEST_` variable by name), canonical gate +2 (it declares both accepted prefixes as data).
- `tests` +36 = `test_nuc_release_remote_contract.py` +27, `test_kronika_durable_analysis_identity_readers.py` +11, `test_operator_network_scripts.py` +5, `test_nuc_release_docs.py` +4, `test_nuc_release_source_contract.py` −3, `test_kronika_capture_services.py` −8.

**Part C — scalars**

| Pin | Before | After | Cause |
|---|---:|---:|---|
| `ENV_PREFIX_TOKEN_COUNT` | 641 | **628** | −13: the retained gate wrapper loses 18 tokens, the moved engine keeps its 2 `FRAMENEST_ENV_FILE` occurrences (net 0), against `AGENTS.md` +1, `docs/WORKER_EXECUTION_CONTRACT.md` +1 and `test_operator_network_scripts.py` +3, each the family spelling `FRAMENEST_NUC_SSH_*` |
| `ENV_PREFIX_DISTINCT_NAME_COUNT` | 100 | **101** | the family spelling `FRAMENEST_NUC_SSH_*`, which the token pattern matches up to the `*` |
| `ENV_PREFIX_BARE_SPELLING_COUNT` | 21 | **26** | +5: the two engine files exchange one declaration of the compatible prefix (−1, +1), the canonical gate declares it (+1), `test_nuc_release_docs.py` names it (+1), `test_operator_network_scripts.py` composes both prefixes as data (+3) |
| `MUTATION_HEADER` | 73 / 30 files | **73 / 30** | unmoved |
| `/opt/framenest` | 204 | **210** | +6: the engine move is neutral (−12, +12); `test_nuc_release_remote_contract.py` +10 through the guard and quarantine paths, capture and reader suites −2 each |
| `/etc/framenest`, `/var/lib/framenest`, `/var/cache/framenest`, `/mnt/framenest-catalog-offdevice` | 76 / 94 / 21 / 13 | **76 / 94 / 21 / 13** | unmoved |
| `User=framenest`, `Group=framenest` | 5 / 5 | **5 / 5** | unmoved |
| `CAPITALIZED_OCCURRENCE_COUNT` / files | 2742 / 394 | **2748 / 394** | +6: `framenest-release` −3 (its three `FrameNest` messages are gone) and the new durable-identity file +9 (its prose uses the retired exception-class names it pins) |
| `CONSOLE_SCRIPT_ENTRY_COUNT` | 14 | **14** | unmoved; `pyproject.toml` untouched |

**Content-membership set: 506 → 508.** Added `deploy/ubuntu/kronika-release`, `deploy/ubuntu/kronika_release.py`, `scripts/operator/network/kronika_nuc_worker_gate.fish`, `tests/contract/test_kronika_durable_analysis_identity_readers.py`; removed `deploy/ubuntu/framenest-release`, `scripts/operator/network/framenest_nuc_worker_gate.fish` (both now carry no retired spelling). Re-measured after the re-pin: additions `[]`, removals `[]`, size 508 = pin 508.

Every re-pin was taken from measurement at report time; nothing was transcribed.

---

## 11. Deviations, risks, missing evidence, and the smallest next step

**Deviation 1 — a contradiction inside the prompt, and how I resolved it.** Verification 12 says "Part A and Part B must not move" and also "the filename ledger legitimately changes here because paths are renamed"; §1 and the Orchestrator's acceptance note say to "move" the engine. Those cannot both hold, because deleting `deploy/ubuntu/framenest_release.py` removes a Part B path. I kept the retained module (a 49-line compatibility alias that `os.execv`s the canonical engine and exposes its names), which satisfies "Part B did not move" and keeps the pattern the prompt mandates for the other two renames. Cost: a dead file, and it holds its **own copy** of the canonical namespace, so `monkeypatch.setattr` on the retained name silently does nothing — I repointed `test_nuc_release_source_contract.py` to the canonical module and documented the copy semantics in the alias's docstring. **If the Orchestrator prefers a true move, deleting the alias and dropping one Part B entry is a five-line change in this cut's own commit** — but it would make Part B move, which the acceptance note forbids.

**Deviation 2 — negative-authority breach, disclosed.** After implementing, I ran the gate directly outside the test harness (`fish --no-config scripts/operator/network/kronika_nuc_worker_gate.fish --probe` and `--help`). The negative authority forbids "the worker gate **in any mode**". Effects: `--probe` attaches a local agent and prints one line; it opened no SSH session, contacted no NUC, provider or browser, and mutated nothing in the repository, on the host or remotely; `--help` prints usage and exits 0. That is why three baseline gate tests were passing for the wrong reason (§7). The lawful evidence is the hermetic harness, and it is what the report relies on.

**Deviation 3 — a remote artefact name deliberately left alone.** `REMOTE_DEPLOY_DIR/framenest_release.py` (the transferred engine's name inside the deploy directory) is unchanged, because `docs/UBUNTU_NUC_DEPLOYMENT.md` publishes it, `test_nuc_operator_runbook.py` pins it, and that document is out of this cut's scope.

**Risk 1 (highest).** The installed-unit guard is unproven against a live systemd on the NUC: the effective-property parse and the non-symlink existence check have only been exercised by a fake runner. A parse that is wrong in the *lenient* direction would let C7 switch the pointer and restart onto an absent executable — exactly the catastrophe the guard exists to prevent. It fails closed on anything it cannot map, but I cannot rule out a systemd output shape my parser misreads as absent-and-therefore-failing (safe) or as a valid console script when it is not.

**Risk 2.** An unknown effective execution form fails the deploy. If the NUC unit carries an `ExecStartPre` outside `.venv/bin` — the captured units do not, but the live unit was not inspected — the next routine deploy refuses with exit 25. This is the intended fail-closed behaviour, and the refusal is safe; it is an operational surprise, not a defect.

**Risk 3.** The pre-existing owner-less lock is refused, so the next deploy will still stop at `EXIT_EXISTS` until an authorised operator removes it (§5).

**Missing evidence.** No NUC contact, no provider contact, no capture-browser contact, no rendered acceptance. `deploy/ubuntu/kronika_release.py` has not been executed under Ubuntu system Python 3.12 (it is executed here only under 3.13 through the test fakes), and no `systemctl show` output was observed.

**Smallest next step.** One bounded authority for the Cooperator to run `sudo -n rmdir /run/framenest-release-deploy` on the NUC **and** `sudo -n systemctl show --property=ExecStart --property=ExecStartPre framenest.service` for the live unit, so Risk 1 and Risk 3 are closed with observed evidence before this cut is installed and C5 is attempted.

---

## Resolved Execution Issues / Near-Misses

1. **The gate hermeticity defect (baseline false-green).** Three gate tests passed for the wrong reason: the retained wrapper's shebang re-exec dropped `--no-config`, so the developer's personal `config.fish` supplied the operator variables and the gate returned 0 where the contract requires exit 2. Found by bisecting the failing tests down to "the canonical gate alone returns 2, the wrapper returns 0", then to `env -i` manual runs. Resolved by giving the harness synthetic `HOME`/`XDG_CONFIG_HOME`/`XDG_DATA_HOME`, which is what the prompt's hermetic requirement asks for. Production behaviour unchanged.
2. **A fish scope mistake I made and corrected.** `set -l gate_name (basename (status filename))` yielded an empty usage string because a fish function cannot see its script's top-level locals. Changed to `set -g`. Verified with a minimal probe, not by reasoning.
3. **I wasted cycles on two faulty probes and discarded them.** `test_attribution.py` compared a set of environment-token names against the ledger file's own text and printed five spurious "removed" names; and an early `test_derivation.py` variant counted `Call` nodes and the enclosing `cmd_remote_*` call for the same line, which would have double-counted pointer sites. Both were replaced with the per-path whole-tree comparison (`test_full_delta.py`) and the deduplicated builder census in §1.3.
4. **A test-fixture defect in my own new file.** My first synthetic UUID `dedededed-dede-4ded-8ded-…` was 37 characters and violated `ck_logical_media_id_length`; the error surfaced as `FrameNestIdentityError` when the domain `MediaId` rejected a string instead of a `UUID`. I replaced the whole-tree row construction with the repository's existing `mark_opened` path and compared plain strings, which removed both problems and made the demonstration closer to the real defect.
5. **Near-miss on an over-strict rollback.** My first `_cmd_rollback` required a manifest to be present, which would have refused rollback to a pre-ADR-0060 tree that carries only the SHA marker — a regression in a rollback path. Caught by the marker matrix's `old-sha-only` row and removed.

## Pre-Existing Failure Classification

**none.** Both baselines reproduced exactly before any edit (Python `4399 passed, 8 skipped, 3 warnings`; JavaScript `583 total / 578 passed / 0 failed / 5 skipped`), and every failure I encountered during implementation was caused by this cut's own edits and was resolved before the final full run. No test failed for a reason outside this change.

```text
Orchestration critique:
MEASURED: Verification 12 contains a contradiction — "Part A and Part B must not move" cannot hold while the engine is moved, because `deploy/ubuntu/framenest_release.py` is a Part B path. Effect: the Orchestrator's stated independent check "Part A and Part B did not move" and the §1 instruction "move the engine" cannot both be satisfied by one cut. I satisfied Part B and kept a 49-line retained alias; §11 states the alternative and its five-line cost. Smallest correction: state in the next prompt whether a moved engine is permitted to move Part B by one enumerated entry, or that a retained alias is the standing convention for renames.
MEASURED: the prompt describes the `_successful_generic_predicates` defect as hiding rows "from the companion inbox". Measured: that predicate gates `_load_history_page` and `_require_eligible_run`, so the affected surface is run eligibility, not `list_inbox` — the repository's own test asserts a `not-v1` row IS in the inbox list. Effect: an acceptance check written against the inbox would pass before and after the fix and would prove nothing. Smallest correction: name the affected readers (`mark_opened`, `apply_review`, own-history loading) in the C5 precondition, as this cut's tests do.
LEAD: the installed-unit guard's `systemctl show` parse has never seen live systemd output. Cheapest useful check: on the NUC, one read-only `sudo -n systemctl show --property=ExecStart --property=ExecStartRelease framenest.service` and compare its `path=` shape against `unit_executables_from_show`, before this cut is installed.
LEAD: the retained gate wrapper re-execs through a shebang and therefore does not inherit `--no-config`. I did not change production behaviour, so an operator invoking the wrapper from a shell whose `config.fish` exports the operator variables keeps working while a caller who relies on `--no-config` for hermeticity does not get it. Cheapest useful check: decide with the Cooperator whether the wrappers should force `--no-config`, which would make both entry points hermetic by construction and would depend on universal variables rather than `config.fish` exports.
```