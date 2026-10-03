### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: kronika-sole-identity
Worker session ordinal: 09
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session profile: Fresh Independent Re-Audit
Task identity: KSI-AUDIT-C1c — independent re-audit of correction C1c and of C1/C1b non-regression
Status: PASS with findings
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none, by design
Start commit: 24bea56daca28603d81cac8d7ed7e3888ba90671
End commit:   24bea56daca28603d81cac8d7ed7e3888ba90671
Changed files: none. `git status --porcelain` empty before and after every step.
Report justification: new-material-risk
```

`PASS` for acceptance of C1c: no confirmed trust-boundary or parity defect.
Three findings, none of which blocks. One is a **false safety claim in the
docstring of the function that defines the resolver's precedence** — that is the
material risk this audit was chartered to look for, and it needs a small bounded
follow-up before a later cut reads that docstring as truth.

I found no contradiction in C1c, and no regression of any C1 or C1b property.

## Repository gate

Read-only at `/home/agile/Projects/kronika`, matched exactly as issued:

- Branch `feat/kronika-identity-dual-read`, HEAD `24bea56daca28603d81cac8d7ed7e3888ba90671`, subject `fix(identity): restore pre-cut process-environment parity for old spellings`, parent `c02c675…`, lineage `18c357c → 90c93ea → c02c675 → 24bea56`. Tree clean before and after.
- `git ls-remote origin` → `refs/heads/main = 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`; the branch is unpublished, as declared. Not a finding.
- `.ap` gitlink and submodule HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`.
- `./.ap/ap project check --baseline 24bea56…`: **PASS**, governing variant stable. The `SSH_AUTH_SOCK VIRTUAL_ENV_DISABLE_PROMPT PATH` warning is a sanitized-env notice, not a failed gate.

No stopping condition triggered. The probe that first tried to reproduce the
`c02c675` reversion by rewriting `src/framenest/configuration.py` on disk was
discarded before execution as a negative-authority breach; all reversions were
redone in memory by rebinding module attributes.

## Measurements: reproduced vs contradicted

| Given measurement | Result |
|---|---|
| Python `4347 passed, 8 skipped, 3 warnings, 0 failed` | **Reproduced exactly** (667.34 s, one full run, same eight named skips) |
| JavaScript `554 total, 549 passed, 0 failed, 5 skipped` | **Reproduced exactly** (10.18 s) |
| `git diff c02c675..24bea56` empty outside the six declared paths | **Reproduced** — exactly `configuration.py`, `identity_env.py`, `development.py`, and the three test files; 642 insertions / 20 deletions |
| CPython 3.13.9 | **Reproduced** |
| pydantic-settings 2.14.2 | **Reproduced** — installed `2.14.2`, and `poetry.lock` carries exactly one `pydantic-settings` entry, also `2.14.2` |
| Node v26.8.2 | **Reproduced** |
| `poetry.lock` and `pyproject.toml` byte-identical at 18c357c and 24bea56 | **Reproduced** (both `True`) |
| Reversion counts 773 / 742 / 773 | **Reproduced exactly** (773 / 742 / 773) |
| Parity matrix covers "every field (39) … 1170 per channel, 2340 in total, 4680 constructions" | **CONTRADICTED.** `FrameNestSettings.model_fields` has **38** entries. Measured1140 comparisons per channel, **2280 total**, 4560 constructions. Structure is honest; the arithmetic is wrong by one field |
| Retention ledger: six Part C movements | **Reproduced exactly**, all six, independently recomputed |

Nothing else was contradicted.

## Findings

| # | Sev | Finding | Exact reproduction | Observed | Expected | Smallest correction | Blocks C1c |
|---|---|---|---|---|---|---|---|
| A1 | **Low-Med** | **The docstring of `lookup_field_value` states its own precedence backwards, and session 08's report repeats the inversion.** `src/framenest/identity_env.py:197-201` claims "the compatible spelling is consulted first, so **the identity spelling cannot be shadowed by a case variant of the compatible one**". That is false: consulting layer 2 first is exactly what lets layer 2 win. | `kronika_port=9998` + `framenest_port=9999`, hermetic `env -i`, `FrameNestSettings(_env_file=None)`; also `kronika_host=10.0.0.2` + `framenest_host=127.0.0.1`; also `env FRAMENEST_DATABASE_PATH=<tmp> kronika_port=9998 framenest_port=9999 .venv/bin/framenest-db status` | port **9999** (identity case variant evicted, no conflict); host **127.0.0.1** (`10.0.0.2` silently dropped); CLI exit 0, no diagnostic | A case-exact `KRONIKA_<S>` cannot be shadowed. A **case-variant** identity spelling can be | Rewrite the last docstring paragraph to say: layer 1 short-circuits, so a *case-exact* identity spelling cannot be shadowed; when **both** spellings are case variants, the compatible spelling wins because layer 2 precedes layer 3. Correct the same sentence in the next report. Add one test pinning the observed order | **No** — behaviour is pre-C1-preserving (pre-C1 read `framenest_port`, i.e. 9999). The defect is the claim, on the trust boundary, where a later cut would read it |
| A2 | **Low-Med, needs decision** | **The conflict rule is per-channel, so the same logical conflict is fatal in one channel and silent in the other.** `lookup_env` runs once per source over that source's mapping only. `KRONIKA_<S>` in the process environment and `FRAMENEST_<S>` in the environment file — or the reverse — raise nothing, and the process environment silently wins. | `KRONIKA_PORT=9998` in process + file `FRAMENEST_PORT=9999` → 9998, no conflict. `FRAMENEST_PORT=9999` in process + file `KRONIKA_PORT=9998` → **9999**, identity value discarded, no conflict. Same-channel pair → `IdentityEnvironmentConflictError`. Four differing cross-channel combinations measured; all four silent | Silent cross-channel override; within the file channel the pair conflicts | Either a stated per-channel rule, or a cross-channel conflict check | **No** — outside C1c's old-spelling-only scope and outside the oracle's scope. ADR-0085 states no conflict rule at all (grep: no `conflict`/`fail closed` in the ADR); the table lives only in `identity_env.py`'s docstring, which does not mention channels. **Orchestrator decision**, not a code defect |
| A3 | Low, latent | **The dual-prefix sources silently drop every `_env_*` constructor override.** `settings_customise_sources` constructs `_DualPrefixEnvSettingsSource(settings_cls)` and `_DualPrefixDotEnvSettingsSource(settings_cls, env_file=…)`, passing none of `case_sensitive`, `env_prefix`, `env_prefix_target`, `env_nested_delimiter`, `env_nested_max_split`, `env_ignore_empty`, `env_parse_none_str`, `env_parse_enums`, `env_file_encoding`. The parity matrix therefore cannot see this dimension. | `FrameNestSettings(_env_prefix="KRONIKA_", _env_file=None)` with `FRAMENEST_PORT=9999`: stock reference **8000**, current **9999**. `_case_sensitive=True` with `FRAMENEST_PORT=9999`: stock **8000**, current **9999** | Current honours overrides the pre-C1 class ignored | Reachability: `git grep` over `src`, `tests`, `deploy` shows **no** caller passes any `_env_*` override — every construction uses `_env_file` only. Unreachable today | Pass the overrides through in `settings_customise_sources`. Report only; no correction needed now |

### Highest-value missing test

**A cross-channel conflict test**: `KRONIKA_PORT` in one channel and
`FRAMENEST_PORT` in the other. It is the only addition that closes a currently
open, silent divergence on this trust boundary, it is two lines, and no test in
the repository covers it. Second: a test pinning the identity-prefix precedence
against case variants, which is what turns A1 from a comment into a checked
invariant.

## Priority-area verdicts

**P1 — is the oracle a faithful reference? YES, faithful; the licence is
half-tested.** Independently established, not read:

1. *The hook is the library's own.* `STOCK_SOURCE_HOOK = BaseSettings.__dict__["settings_customise_sources"]`. Intercepting it and recording the constructed classes yields `['InitSettingsSource', 'EnvSettingsSource', 'DotEnvSettingsSource', 'SecretsSettingsSource']` — no `_DualPrefix*` class participates, and `main.py:384-423` shows the library itself builds the stock sources before the hook runs.
2. *The reference path never touches project code.* Spying on `configuration.lookup_field_value` **and** `configuration.lookup_env` during an oracle build recorded **zero** calls. The oracle is not derived from the implementation.
3. *Patching the hook equals having no override.* `_settings_init_sources` builds the four sources unconditionally and the default hook returns `(init_settings, env_settings, dotenv_settings, file_secret_settings)`; the class then appends `default_settings`. The reference file contains no `settings_customise_sources`, no `_DualPrefix`, and no `identity_env` import at all. Faithful for **every** input class, not only the tested ones, because the reference side is the unmodified library assembly.
4. *The model half of the licence holds and is checkable.* Extracting the block from `host: str = Field(` to `class FrameNestConfigurationError` from both commits gives 13 866 bytes each and an identical result. `model_config` is character-identical (`env_prefix="FRAMENEST_"`, `env_file_encoding="utf-8"`, `hide_input_in_errors=True`, `extra="ignore"`). The pre-cut `ENV_FILE` read was `os.environ.get(ENV_FILE_ENVIRONMENT_VARIABLE, "").strip()` — case-exact, which is what `lookup_env` still is.
5. *The licence test cannot be passed with a differing lockfile.* `_git_blob(RESTORATION_REFERENCE, "poetry.lock") == _git_blob("HEAD", "poetry.lock")` with `check=True`; a synthetic 40-zero revision raised `CalledProcessError`, so an unreachable reference fails loudly rather than weakening.
6. **Gap.** The licence test pins only `poetry.lock` and `pyproject.toml`. The *other* half of the claim — that `FrameNestSettings` is byte-identical at the reference — is asserted in the module docstring and **never tested**. I could not construct a case where the lockfile differs and the test passes; the honest statement is that the lockfile half is enforced and the model half is prose. Note also that `pydantic_settings.VERSION` is a plain string, not a content digest: an edited install reporting the right version would pass. Low risk, worth naming.
7. **This gap does not undermine the test.** The parity test's soundness as a *differential* (stock sources vs dual sources, same model) is independent of `18c357c` entirely. `18c357c` only licenses the narrative "this restores pre-C1 behaviour".

**P2 — does the parity test catch the defects? YES, and F1 and F2 separately.**

- Reversion counts reproduced exactly by in-memory rebinding: `_resolved_field_values` reverted to its `c02c675` body → **773**; folding removed → **742**; `lookup_field_value` → `lookup_env` → **773**. Baseline 0/0. All three fail the committed test.
- Better than reported: I also built an **F2-only** reversion (folding kept, only the raw empty value dropped) → **93 mismatches**, and an **F1-only** reversion → **742**. 93 ≠ 742, so the two defects are detected **independently**, not merely as a union. That question is answered with better evidence than session 08 supplied.
- Builds per comparison: instrumented subclass counted **2280** builds for 1140 process-channel comparisons — exactly two per comparison. Honest.
- The message carve-out hides nothing material. `SettingsError` text embeds `self.__class__.__name__` (`base.py:546, 554`), which *must* differ between `_DualPrefixEnvSettingsSource` and `EnvSettingsSource` — comparing messages would produce guaranteed false positives, so the carve-out is forced, not convenient. What it does hide is a message-only regression in a non-conflict validation error. That is covered elsewhere: `hide_input_in_errors` is asserted by `test_hide_input_in_errors_is_preserved`; the conflict message is pinned separately (values absent, suffix present, `exit_status == 2`) and I observed the exact text through a real console script; `SecretStr` is masked in `model_dump` and the parity module compares it **unmasked**, so two different synthetic secrets do not collapse to equality.
- Uncovered simultaneous combinations, named precisely: (i) two case variants of one old name — covered by `test_both_cases_of_one_old_name_resolve_to_the_later_value`; (ii) two different fields at once — I measured **11** targeted two-field combinations (host+port, two case variants of one name, overlapping storage roots, `ingress_mode`+`external_origin`, `ingress_mode`+non-loopback host, `identity_map`+`local_owner_login`, `host`+`companion_extension_origins`, `port`+empty `api_key`, out-of-range `upload_max_total_bytes`, empty `uds_path`+`external_origin`) and found **zero** divergence from the stock reference; (iii) cross-channel, where both a process and a file variable are set — all seven pure-old-spelling cross-channel cases match the reference exactly (process beats file, empty process beats file and fails closed on both sides, case-variant process beats file); (iv) `_env_*` constructor overrides — see A3. The claim "only the prefix pairs changed behaviour, and those have dedicated tests" **holds**; the four identity-prefixed cross-channel cases are new-behaviour territory that the oracle deliberately does not cover, and one of them is finding A2.
- Soundness verdict: the oracle is faithful, the test is not tautological, and the test is capable of failing.

**P3 — the declared divergence. Safe as a behaviour, unsafe as stated.**
- *Can a case variant of the compatible spelling evade a value the identity spelling selected?* **Yes — when the identity spelling is itself a case variant.** Measured: `KRONIKA_PORT=9998` + `framenest_port=9999` → 9998 (no evasion); `kronika_port=9998` + `framenest_port=9999` → **9999** (evasion, no conflict). Same for `kronika_host=10.0.0.2` + `framenest_host=127.0.0.1` → `127.0.0.1`. The launcher is **not** an exposure path: `drop_identity_environment_spellings` compares case-insensitively, so it strips `KRONIKA_*`, `kronika_*` and every mixed variant before writing. Verified by enumeration, not by the report: the drop removed all eight spellings of the three suffixes and left `KRONIKA_HOSTNAME`, bare `KRONIKA`, bare `FRAMENEST`, bare `HOST`, `PATH` and the two `DEVELOPMENT_*` variables untouched.
- *Can a case variant of the identity spelling interact badly with layer ordering?* Yes, and this is finding A1. A case-exact identity spelling short-circuits at layer 1 and is immune. A case-variant identity spelling is only consulted at layer 3, after layer 2, so a case variant of the compatible spelling evicts it. Empty identity values are handled consistently: `KRONIKA_PORT=""` + `framenest_port=9999` → 9999; `kronika_port=""` + `FRAMENEST_PORT=9999` → 9999.
- *Is "the input contains the new spelling, so it is not old-spelling-only" sound?* **Sound as a scope boundary, insufficient as a safety argument.** It correctly places `KRONIKA_PORT=9998` + `framenest_port=9999` outside the restoration claim, and correctly notes that a case-insensitive conflict rule is forbidden. But it does not establish that the resulting behaviour is safe, and it is paired with a docstring claim that asserts the opposite of what the code does (A1). The trade-off is defensible; the reasoning offered for it is not.

**P4 — non-regression of C1 and C1b: re-established at 24bea56, nothing undone.**

- 361 focused tests across the identity, mutation-header, ingress-security, reader-routing, durable-artifact, configuration-ingress, launcher and retention modules: **all pass**. Full suite green (§Measurements).
- Mutation gate and writer invariance are untouched by this diff: `git diff 18c357c..24bea56 -- src deploy | grep '^+' | grep KRONIKA_` yields only `IDENTITY_ENVIRONMENT_PREFIX = "KRONIKA_"` (src and the deploy mirror), `PRIMARY_ENVIRONMENT_PREFIX = "KRONIKA_"` in `identity_env.py`, and docstrings. The one other `KRONIKA_` literal in `src`, `RESEARCH_CREDENTIAL_IDENTIFIER = "KRONIKA_RESEARCH_OPENAI_API_KEY"`, is **pre-existing at `18c357c`** and unchanged by the branch. No `KRONIKA_` writer introduced.
- `lookup_env` remains the single case-exact conflict authority: instrumented, it is called **76 times per settings build = 38 fields × 2 sources**, 38 distinct suffixes = the full field set, and it is called before any layer returns (`identity_env.py:205` precedes 206–214).
- No conflict path leaks a value or returns a partial result. Observed: type `IdentityEnvironmentConflictError`; string and `.args` name only the two variables and the suffix; `"9998" in str` and `"9999" in str` both `False`.
- Exit 2 at the entry point, suffix-only, no traceback, observed through the installed console script under `env -i`: `KRONIKA_PORT=9998` + `FRAMENEST_PORT=9999` → `{"error_code":"FRAMENEST_DB_CONFIGURATION_FAILED","message":"Conflicting environment variables KRONIKA_PORT and FRAMENEST_PORT are set to different values."}`, **exit 2**. Same-value pair → exit 0. Eleven further cases behaved as declared: `framenest_port=9999` and `Framenest_Port=9999` exit 0; `FRAMENEST_PORT=` and `framenest_port=` **exit 1** (`FRAMENEST_DB_COMMAND_FAILED`) — F2 closed; `framenest_port=not-a-port` exit 1; `FRAMENEST_PORT=" 8123 "` exit 0; `kronika_port=9999` exit 0. Every run created **no** files (`new=none`).
- Installed env-file shape still works, and only case-exact key styles ever did: uppercase `FRAMENEST_ENV_FILE` selects the file (7106); `framenest_env_file` and `FrAmeNeSt_EnV_FiLe` are ignored (8000) — identical to pre-C1 `os.environ.get`; `KRONIKA_ENV_FILE` selects it; `kronika_env_file` ignored; both spellings equal → 7106; both different → `IdentityEnvironmentConfigurationError`; either empty → unset. File *keys*: uppercase, lowercase and mixed all still read (parity module, 0 mismatches over 1140 file-channel comparisons).
- `hide_input_in_errors=True`, `extra="ignore"` (`FRAMENEST_TOTALLY_UNRELATED` absent from the dump), `env_file_encoding="utf-8"` (a Latin-1 file raises `UnicodeDecodeError` on **both** the current and the stock reference), retained `env_prefix="FRAMENEST_"`, and process-over-environment-file precedence are all intact. Source order observed as `['InitSettingsSource', 'EnvSettingsSource', 'DotEnvSettingsSource', 'SecretsSettingsSource']` — the library default.

**P5 — the launcher normalisation: correct, and the enumeration claims are verified.**

- `drop_identity_environment_spellings` cannot remove too much or too little **for this model**, and I checked the two ways it could. No settings field name is a prefix of another (`p5_suffix_prefix_relationships: []`), and no two field names collide case-insensitively (`p5_case_collisions: {}`), so dropping suffix `HOST` cannot affect another setting and no name differs only by case between two settings. Its construction is a set comprehension over the given suffixes × both prefixes, upper-cased, then exact-match on `name.upper()` — so it cannot match a superset.
- With a conflicting or case-variant parent, the child receives **exactly one name per injected suffix**. Nine new launcher tests cover primary/lower/mixed × host/port/database_path; my own enumeration of `env=` constructions in `src/framenest` finds `development.py:523` (the fixed mapping), `youtube/downloader.py:537`, `x/downloader.py:119` and `:392` — the last three are `_subprocess_environment()`, which sets only `PATH`, `LANG`, `LC_ALL`, `PYTHONIOENCODING`, `PYTHONUTF8`, `PYTHONNOUSERSITE`, `NO_COLOR`. `git grep -E '^\s*env\["' src/framenest` returns **nothing**, so there is no other hand-written identity-prefixed assignment.
- `development.py` **is** the only place in `src/framenest` that builds a child environment containing an identity-prefixed name: **verified**, not taken from the report.
- The launcher injects **three** names, not four: `SPAWNED_SETTING_SUFFIXES == ('HOST', 'PORT', 'DATABASE_PATH')`, and `_spawn_server_process` writes `HOST_ENV`, `PORT_ENV`, `DATABASE_ENV`. `RUNTIME_DIR_ENV` and `LOG_DIR_ENV` are read-only overrides through `_resolve_override`. **Verified**: `git show 18c357c:…/development.py` wrote the same three names.

**P6 — the retention ledger. All six movements are arithmetically honest; Part A and Part B did not move. Part C must be strengthened before C3.**

My independent recomputation, per changed file, from `git show` at `c02c675` and `24bea56` — the six ledger lines are the *only* changed lines in the file:

| Pin | Was | Now | My recomputation | Report08 | Verdict |
|---|---|---|---|---|---|
| `PER_TREE_FRAMENEST_FILE_COUNT["tests"]` | 320 | 321 | +1: the new parity module contains `framenest` | +1 | ✓ |
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["src"]` | 2983 | 2981 | `src` lowercase **−2** (`development.py` 35→33; `configuration.py` net 0) | −2 | ✓ |
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["tests"]` | 4401 | 4434 | `tests` lowercase **+33** (parity module +27, launcher tests +6) | +33 | ✓ |
| `ENV_PREFIX_BARE_SPELLING_COUNT` | 16 | 18 | **+2**, both in the launcher tests | +2 | ✓ |
| `CAPITALIZED_OCCURRENCE_COUNT` | 3364 | 3379 | **+15** (parity +13, launcher +2) | +15 | ✓ |
| `CAPITALIZED_FILE_COUNT` | 481 | 482 | +1: the parity module contains `FrameNest` | +1 | ✓ |

The two unchanged pins also check out. `ENV_PREFIX_TOKEN_COUNT` 642: `src` −2 tokens, parity module +2 tokens (both `"FRAMENEST_PORT"`, at lines 293 and 299), launcher tests ±0 → net 0. `ENV_PREFIX_DISTINCT_NAME_COUNT` 101: the only new distinct name is `FRAMENEST_PORT`, which already exists globally (`development.py:47`), so the global distinct set is unchanged. Mutation-header, host-path, unit-account and console-script pins: zero changed lines.

**Decision: yes, strengthen Part C before C3's grant is written — one literal plus one test.**

The reason is not preference. ADR-0085 lines 114–115 promise that "a premature or missed rename **fails loudly at the cut that owns it rather than at the end**". Session 07 established that Part C's scalars do not deliver that. C3 is the cut that moves every file to `kronika.*`, so C3 is where the promise is first tested at scale.

Propose exactly this, and nothing more:

> Add `EXPECTED_FRAMENEST_CONTENT_PATHS: frozenset[str]` — the exact pinned set of tracked text paths (excluding the ledger file itself) whose decoded content contains `framenest` case-insensitively — plus one test asserting set equality against the working tree, in the same style and with the same "deliberately not recomputed" reasoning as the existing Part B path ledger.

Why this and not a per-file count map: membership is per path, so **no compensating swap is possible**. A count map still lets file X go 12→10 while file Y goes 3→5. A pinned content-path set fails if a file that should have been renamed still carries the token, *and* if a file that should not have been renamed no longer does. It mirrors a design decision the file already documents ("a content-only rename inside an already matching file leaves the file counts unchanged, so these are the measures that actually detect a missed content rename") — the file identified the right measure and then pinned the weaker form of it. C3 already pays a full re-pin, so the size cost is not incremental.

Two accuracy notes for the C3 grant: the ledger's `_ALEMBIC_VERSIONS_GLOB = "src/*/infrastructure/persistence/alembic_environment/versions"` is wildcarded and **does not** change shape when `src/framenest` becomes `src/kronika`; and `FROZEN_ALEMBIC_SHA256` pins by basename, so it survives the move. The prompt's premise that "C3 changes the ledger's own `src/*/…` glob" is not what the file contains.

## Also assess

- **The redundant work is a performance observation, not a correctness one, and it does not matter at this scale.** Precisely: `main.py:384-407` constructs the stock `EnvSettingsSource` and `DotEnvSettingsSource` before the hook runs, and `settings_customise_sources` discards both. Census of one `load_settings(env_file=None)`: `EnvSettingsSource` (discarded), `DotEnvSettingsSource` (discarded), `_DualPrefixEnvSettingsSource`, `_DualPrefixDotEnvSettingsSource`, `SecretsSettingsSource` (used). The library's `parse_env_vars(os.environ)` runs **once** per build, inside the discarded source; the project's own `folded_identity_environment` runs **twice** — once over `os.environ` (`['FRAMENEST_PORT']`) and once over the canonicalised file values (`[]`). The dominant waste is that **the environment file is read and parsed twice per build** (`DotEnvSettingsSource._read_env_files` called twice, once per class). Correctness: outcome-identical to the stock reference for a good file, a malformed file and a binary file (`['good=ok:7106','bad=ok:8000','binary=ok:8000']` on both sides, `match: True`), so the discard raises nothing, leaks nothing and changes nothing. Scale: one full `load_settings` is **1.68 ms**; one extra fold is **0.0001 ms**, i.e. **0.008 %** of a build. Report 08's phrasing "folds `parse_env_vars(os.environ)` twice" is imprecise — `parse_env_vars` runs once and the project fold runs twice — but the substance is right. **Do not spend a cut on it.**
- **`FrameNestSettings` in the parity test is a mechanical rename, with one value coupling.** Eleven occurrences: one docstring, one import, and nine code references (two annotations, three `model_fields`, two constructions, two `mock.patch.object` targets). All are name references to the project class; the `mock.patch.object` target keeps working under any class name. `RESTORATION_REFERENCE`, `REPOSITORY_ROOT`, `_git_blob` and the licence test are all independent of the class name and survive C3 unchanged. **The hidden coupling is a value, not a name**: `_spelled()` builds its variable names from `COMPATIBLE_ENVIRONMENT_PREFIX`. If C3 or C7 changes that constant's *value*, the matrix silently changes its subject and the parity claim becomes vacuous without any test failing. Smallest guard, one line in the parity module: assert `COMPATIBLE_ENVIRONMENT_PREFIX == "FRAMENEST_"` and `FrameNestSettings.model_config["env_prefix"] == "FRAMENEST_"`.

## Resolved Execution Issues / Near-Misses

- My first draft of the reversion probe rewrote `src/framenest/configuration.py` on disk to install the `c02c675` method body. That is a negative-authority breach. **I discarded it before running it** and rebuilt all four reversions as in-memory `mock.patch.object` rebinds of `_IdentityResolverFieldMixin._resolved_field_values`, `configuration.folded_identity_environment` and `configuration.lookup_field_value`. No repository file was written at any point in this session.
- My first `_env_*` override probe set the wrong variable: with `_env_prefix="KRONIKA_"` I supplied `KRONIKA_PORT`, which both sides honoured (9999/9999) and which therefore showed no divergence. The divergence only appears with the *old* spelling under a *new* prefix, or with `_case_sensitive`. The probe was corrected, the finding stands.
- Two probes measured nothing and I discarded both rather than reporting them: `census_parse_env_vars_per_build: 0` (I patched `pydantic_settings.sources.utils.parse_env_vars`, but `sources/providers/env.py` binds the name at import, so the patch never took effect — redone against `sources.providers.env`); and `q_order_first_four: []` (I patched `identity_env.lookup_field_value`, but `configuration.py` imported that name at import time, so the dual-source path was unaffected — the ordering claim rests on reading `identity_env.py:205` preceding 206–214, plus the 76-call census).
- `p4_api_key_present: False` was my own nested `mock.patch.dict(..., clear=True)` wiping the outer environment. Redone in isolation: `FRAMENEST_API_KEY` honoured, `SecretStr('**********')` in the dump, `KRONIKA_API_KEY` honoured.
- One census measurement was inherently double-counting: `DotEnvSettingsSource` subclasses `EnvSettingsSource`, so patching both `__init__`s records some constructions twice. The class names in the census remain correct; only the count of entries is inflated. I re-derived the true per-build set from the `cls=` labels.
- `--operation test` rejects trailing argv (`ap: ERROR: operation test does not allow trailing argv`); I re-ran it with no extra arguments. One full Python run and one JavaScript run were used, within the grant.

## Pre-Existing Failure Classification

none — no repository test failed at any point. All 15 + 10 + 4 + 3 + 5 + 5 = 42 probe tests passed; the 361 focused identity tests passed; the full suite is `4347 passed, 8 skipped, 3 warnings, 0 failed`; the JavaScript route is `549 passed, 0 failed, 5 skipped`. The probe failures listed above were defects in my own throwaway probes under `/tmp`, not repository failures, and are recorded because three of them would otherwise have become false findings.

## Commands beyond the declared routes

All Python evidence went through
`./.ap/ap exec --root /home/agile/Projects/kronika --baseline 24bea56… --operation test-focus -- <path>`,
plus `./.ap/ap exec … --operation test` and `./.ap/ap project check --baseline 24bea56…`.
JavaScript used `node --test tests/*.test.js`; `node --version` for the version.
Read-only Git only: `status`, `rev-parse`, `log`, `show`, `diff`, `ls-files`,
`ls-remote`, `ls-tree`, `submodule status`, `grep`. Library sources under
`.venv/…/pydantic_settings/` (`main.py`, `sources/base.py`,
`sources/providers/env.py`, `sources/providers/dotenv.py`, `sources/utils.py`)
were **read** with the read tool and never imported by an interpreter I
launched. Console-script probes ran under `env -i` with `HOME` and `TMPDIR`
under `/tmp/opencode/ksi09/exit`, one synthetic database path per run, no
inherited identity variable; the before/after file tree was captured and every
run created **no** files. Throwaway probe modules and scratch files exist only
under `/tmp/opencode/ksi09/`. Nothing outside `/tmp` was written; `git status
--porcelain` is empty; no NUC, provider, capture, network, dependency or
credential action occurred.

## Smallest next step

Accept C1c. Then issue **one** bounded correction for A1 only — rewrite the
last paragraph of `lookup_field_value`'s docstring to match the code and add the
one test that pins the observed layer order — and record A2 as an explicit
Orchestrator decision on whether the conflict rule is per-channel or global.
Settle the Part C strengthening (the pinned content-path set) as a separate small
grant **before** C3's grant is written. Do not bundle A3, the redundant-work
removal, or anything from F3/F5/H1–H3/D1, which remain out of scope. Publication
of the branch and the routine NUC refresh each remain separate bounded grants
regardless of the outcome.

Authority expiry: on submission of this report all authority under this prompt
expires. No remediation, no push, no publication, no NUC refresh and no later cut
is authorized by it, whatever the findings say.

```text
Orchestration critique:
MEASURED: the issued measurement "1170 comparisons per channel, 2340 in total" and its supporting "every field of FrameNestSettings (39)" are both wrong; evidence: `len(FrameNestSettings.model_fields) == 38` and `len(list(parity._matrix())) == 1140`, with an instrumented subclass counting exactly 2280 builds for the 1140 process-channel comparisons, so the real totals are 1140 per channel / 2280 total / 4560 constructions; effect: an Orchestrator sizing the parity matrix or checking C3's re-pin cost from 2340 is working from a number that does not exist, and the "every field" claim cannot be reconciled with the repository; smallest correction: state 38 fields, 1140 comparisons per channel, 2280 total, 4560 constructions. Separately, session 08's stated cause for `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["src"]` (2983→2981) is right in net but its components do not match the file: I measure `development.py` lowercase 35→33 and env-token 9→7, i.e. −2 on both measures rather than "−3 +1", with `configuration.py` net 0; effect: an auditor re-deriving the re-pin line by line cannot reproduce the stated split; smallest correction: give the per-file net (−2, −2) instead of a −3/+1 decomposition.
LEAD: `settings_customise_sources` rebuilds both dual-prefix sources with only `settings_cls` (and `env_file`), so every `_env_*` constructor override is dropped; I confirmed the divergence and confirmed no in-repository caller uses one, but the parity test cannot see this dimension at all; cheapest useful check: at the cut that renames the package, add one parity case that passes `_case_sensitive=True` and one that passes a non-default `_env_prefix`, and record the outcome as the deliberate or accidental answer, so the blind spot becomes a decision instead of an omission.
```