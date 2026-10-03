I have all the evidence I need. Writing the terminal report.

### Report for ORCHESTRATOR_CHAT

Logical whole identity: `kronika-sole-identity`
Worker session ordinal: `07`
Worker exchange ordinal: `01`
Persistent role identity: WORKER
Worker session profile: Fresh Independent Audit
Task identity: KSI-AUDIT-C1
Status: **PARTIAL**
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none, by design
Start commit: `c02c6753694d5d4958045bb79f80b5eb94b9c75c`
End commit: `c02c6753694d5d4958045bb79f80b5eb94b9c75c`
Changed files: **none.** `git status --porcelain` empty before and after.
Report justification: `new-material-risk`

`PARTIAL`, not `PASS`: the mutation-authorization boundary and the fail-closed
resolver are sound on every attack I could construct, and all given measurements
reproduce. Four findings remain, two of which are confirmed behaviour defects on
the configuration trust boundary that both contradict explicit cut claims. The
audit cannot fix them; that is a bounded correction, not this report.

## Repository gate

Re-verified read-only at `/home/agile/Projects/kronika`:

- Branch `feat/kronika-identity-dual-read`, HEAD `c02c6753694d5d4958045bb79f80b5eb94b9c75c`, subject and parent `90c93ea…` exactly as issued; clean tree.
- `git ls-remote origin refs/heads/main` → `18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`. Branch unpublished, as declared.
- `.ap` gitlink and submodule HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`.
- `./.ap/ap project check --baseline c02c675…`: **PASS** (governing variant stable; `ap doctor` PASS; warning about sanitized inherited env classes `SSH_AUTH_SOCK VIRTUAL_ENV_DISABLE_PROMPT PATH` is not a failed gate).

Gate matches. No stopping condition triggered.

## Measurements: reproduced vs contradicted

| Given measurement | Result |
|---|---|
| Python `test`: 4314 passed, 8 skipped, 3 warnings, 0 failed | **Reproduced exactly** (697.51 s, one full run) |
| JavaScript `node --test tests/*.test.js`: 554 / 549 passed / 0 failed / 5 skipped | **Reproduced exactly** |
| `git diff 90c93ea..c02c675` empty for `ap.project.conf`, `pyproject.toml`, `deploy/**`, `deploy/systemd/**`, `docs/**`, root Markdown, `src/kronika_capture/**`, `tailscale_ingress.py` | **Reproduced** (empty; I added the 36 Alembic revision files — also empty) |
| `KRONIKA_` occurrences added outside tests: exactly three code tokens, all read-side prefix constants | **Reproduced in substance, corrected in detail.** Three assignments of the literal `"KRONIKA_"`: `identity_env.py:42`, `framenest_release.py:38`, `production_ai_deploy.py:24` — all read-side prefixes. A naive grep returns 8, because five more are in docstrings/prose and one is `KRONIKA_ENV_FILE` inside the `load_settings` docstring. Substance holds. |

Nothing was contradicted.

## Findings

| # | Sev | Finding | Exact reproduction | Observed | Expected | Smallest correction | Blocks C1/C1b |
|---|---|---|---|---|---|---|---|
| F1 | **Medium** | Process-environment **case-insensitive matching is lost**. `lookup_env` is case-exact; `pydantic-settings` `parse_env_vars` lower-cased every key. `_DualPrefixEnvSettingsSource._load_env_vars` *replaces* `env_vars` instead of merging, so a lower/mixed-case name that configured a field before C1 is now silently ignored and the model default applies. | `framenest_port=9999 .venv/bin/framenest-db status` (hermetic env, `FRAMENEST_DATABASE_PATH` under /tmp). Differential probe vs the stock `EnvSettingsSource`+`parse_env_vars` path that 18c357c used: `framenest_host`, `Framenest_Host`, `framenest_port`, `framenest_companion_extension_origins`, `framenest_automatic_media_analysis_enabled` all `old={'host':'10.0.0.2'} → new={}`, model still validates as `('127.0.0.1', 8000)`. | Setting silently ignored; valid settings object; exit 0 | Old-spelling process env honoured regardless of case | Resolve over a case-folded view inside the settings source, e.g. build `{k.upper(): v}` from `os.environ` and pass that mapping to `lookup_env` | **Yes — C1** |
| F2 | **Medium** | **Empty-string process-env values are now "unset"**, so a previously-rejected configuration is silently accepted. `parse_env_vars` keeps `""` (`env_ignore_empty` is not set); the resolver coerces `""` to `None`, and the env source no longer carries the raw key. | `FRAMENEST_PORT= .venv/bin/framenest-db status` → **exit 0**, `state uninitialized`. At 18c357c the same input was an `int`-coercion `SettingsError` → `FrameNestConfigurationError` → exit 1. `FRAMENEST_HOST=` likewise now exits 0. | Silent default | Fail closed on a value that cannot be parsed | Either keep the raw value for the old spelling, or restrict the empty-means-unset rule to the `ENV_FILE` selector where it is actually needed | **Yes — C1b** (breaks "no other exit status changed") |
| F3 | Low | `framenest-ai` had `default_ai_config_path()` / `_CliContext(...)` **moved inside the try**, so a pre-existing configuration failure changed exit status. | `env -i … FRAMENEST_AI_CONFIG_PATH=relative/config.json .venv/bin/framenest-ai status --no-write` → exit **2** + `AI configuration error: AI configuration path must be absolute.` `git show 18c357c:…/ai.py` shows both statements above the `try`, where `_validated_absolute_path` raises `AiConfigurationError` → uncaught → traceback → exit 1. | 1 → 2 | Unchanged, or an explicitly accepted deviation | Either revert the relocation (translate the conflict at the reader only) or amend the C1b goal; it also widens the exit-2 collision on this entry point | No — Orchestrator decision |
| F4 | Low-Med | The **development launcher manufactures a conflict for the server it spawns.** `_spawn_server_process` writes `FRAMENEST_HOST=127.0.0.1` / `FRAMENEST_PORT=str(self._port)` into the child env without removing or normalising an inherited `KRONIKA_*` spelling. | Captured the real child env through the injectable `spawn_process` hook (nothing spawned): `KRONIKA_HOST=0.0.0.0` → child gets `KRONIKA_HOST=0.0.0.0` + `FRAMENEST_HOST=127.0.0.1`; `KRONIKA_PORT=08000` and `KRONIKA_PORT=" 8123 "` → child `KRONIKA_PORT=08000`/`" 8123 "` + `FRAMENEST_PORT=8000`/`8123`. Feeding each captured env to `FrameNestSettings(_env_file=None)` raises the conflict. | Spawned dev server exits 2; launcher reports unhealthy | Child env carries no conflicting pair | Pop the alternate spelling (or write both) for the four injected suffixes before setting the resolved values | No (dev-only, no NUC exposure) — but fix in the same correction |
| F5 | Low, latent | Release-engine reader asymmetry: `cmd_remote_probe_release_markers` accepts both marker spellings, but `read_current_release` then calls `cmd_remote_read_manifest` / `cmd_remote_read_release_sha`, which `cat` **only** the `.framenest-*` names. | `deploy/ubuntu/framenest_release.py:400-405` vs `:385-389`. | A tree holding only `.kronika-release-sha` is probed as present, then read fails → generic transport error | Reader set matches probe set | No action now; **C5 must land the writer switch and this reader widening in one commit** | No |
| H1 | Medium | Exit-2 collision is real and larger than "ten entry points". | Measured per entry point: usage error vs conflict. Both exit 2 for `framenest-db`, `framenest-production`, `framenest-catalog`, `framenest-backup`, `framenest-ai`, `framenest-covers`, `framenest-library`, `framenest-previews`, `framenest-youtube`, `framenest-recovery`, `framenest-dev` (11). `framenest-sidecar` usage = 1. | Exit 2 ambiguous | — | Not a code defect. See judgement below | No |
| H2 | Low, pre-existing | Duplicate mutation headers: `_single_value` returns the **first** value, and the mutation header is not in `_SINGLETON_SECURITY_HEADERS`. `{x-kronika-request: [1, "1, 1"]}` authorises. | Fuzz probe, 4000 random maps. | Same as pre-C1 for the old spelling | — | Add both spellings to `_SINGLETON_SECURITY_HEADERS` | No |
| H3 | Low | A remote conflict is undiagnosable through the release engine: `subprocess_runner` discards stdout/stderr and raises `ReleaseError("command failed", EXIT_TRANSPORT)`. | `framenest_release.py:196-203`. | Operator sees "command failed", never the conflict text | Conflict message surfaces | Log the sanitized remote stderr for the db/backup status probes | No |
| D1 | Accepted | `_database_state` swallows the conflict (`except Exception: return "unknown"`). | `KRONIKA_HOST`/`FRAMENEST_HOST` conflict + `framenest-dev status` → **exit 3**, `Database: unknown`, no hint of a conflict. | Degraded, fail-closed | — | See judgement | No |

### Independent vs reused checks

**Independent** (my own constructions, not the repository's helpers): the
settings-source differential (old column rebuilt from the *unmodified*
`pydantic-settings` sources plus `parse_env_vars` — literally the 18c357c path —
versus the current dual-prefix source, over a 16-case process-env matrix and a
15-case environment-file matrix); the `_mutation_header_authorized` differential
against a locally reconstructed pre-C1 gate, exhaustively over old-only values
and 4000 seeded random header maps; the resolver edge-case matrix; the mirror
equivalence matrix executed against both stdlib-only engines loaded from
`deploy/ubuntu/`; the spawned-child-environment capture through the injectable
`spawn_process` hook; and all 13 console-script exit-status observations.

**Reused existing coverage**: the full Python suite, the JavaScript route, and
the retention ledger. I read the five new `test_kronika_*` modules and
`test_kronika_identity_retention.py` in full. Two of my own probe assertions
were initially wrong (not the implementation): my new-spelling matrix rule
omitted the "old absent" case, and I had assumed a whitespace-primary pair
resolves instead of conflicting — both mirrors and the package agree on
conflict, so the probe was corrected, not the code.

## Per-scope-area record

**1. Mutation-authorization boundary — attacked, no bypass found.** Absent
header → 403 (unchanged). Wrong value → 403. Duplicate old spelling, any
combination → bit-for-bit identical to the reconstructed pre-C1 gate
(`test_old_only_requests_are_bit_for_bit_preserved`, >50 combinations).
Both spellings, one wrong → 403. Both correct → authorised. Name case
(`X-Kronika-Request`) → authorised, as HTTP requires and as the old spelling
already behaved. Trailing whitespace in the name (`X-Kronika-Request `) → not
matched, 403. Comma-folded (`1, 0`), `01`, `1 `, ` 1`, `1\x00` → all rejected.
`_single_value` returning `None` for a multi-valued header is *not* reachable —
it returns `values[0]`; the real multi-value weakness is H2, and it is
pre-existing. `_single_value` returning `None` is genuinely indistinguishable
from absent only for an **empty** value list, which `_collect_headers` cannot
produce. **Diff-verified, not comment-verified:** the whole
`18c357c..c02c675` diff of `tailscale_ingress.py` is two hunks — the constants
block and the gate. `_SINGLETON_SECURITY_HEADERS`, `_REMOTE_MARKER_HEADERS`,
`_mutation_origin_allowed`, `self._external_origin` and
`self._companion_extension_origins` are untouched; a scan of every uppercase
module-level container finds `x-kronika-request` only in `MUTATION_HEADERS`. The
new spelling is not reachable around ingress provenance: the gate is evaluated
only after `_has_remote_markers`, `_singleton_conflict`,
`_forwarded_values_valid`, route policy, Tailscale login, and the origin check;
the local channel never consulted the old spelling either. `HEADER_MUTATION` has
no other consumer in the repository — no CORS allow-list, no echo.

**2. Fail-closed resolver.** No conflict path returns a partial result, prefers
a value, or falls through to a default: every `lookup_env` call site either
translates the conflict or is unreachable from a conflict, and I enumerated them
all — `configuration.py:177,214,672`; `development.py:689`;
`catalog_backup_ops.py:270-289`; `catalog_backup_offdevice.py:129`;
`ai/configuration.py:161`; `framenest_release.py:1193-1195`;
`production_ai_deploy.py:161`. Only two direct `FrameNestSettings(...)`
constructions exist outside `configuration.py` (`development.py:470` translated,
`:482` swallowed = D1). `public_published_application.py:85` goes through
`load_settings()`. **No value leak on any channel I could reach:** exception
`str`, `repr`, and `.args`; all 13 console-script outputs; both mirrors'
messages; the audit-event recorder (the gate records no header content — only
`request_id`); the structured-logging path (no `extra=`/`detail=` field carries
a header or env value on the gate or resolver paths); subprocess argv (the only
injected env is `env FRAMENEST_ENV_FILE=<path>`, a path). Case sensitivity:
mixed-case **file** keys still work (measured identical old vs new), mixed-case
**process** keys do not — that asymmetry is F1. Whitespace-only values are
identical pre/post (`' '` is a set value on both sides, and a whitespace pair
with a different value conflicts on both sides) — **no defect**. Import safety:
`identity_env.py` imports only `os`/`typing`, contains no `framenest` import, and
a fresh-interpreter sweep importing each of 9 dependents first-in-order passed.

**3. Stdlib-only mirrors.** Semantically equivalent, verified by executing both
against the same 10-case matrix plus 3 conflict cases: unset, one-set, both-set-equal,
both-empty-means-unset, empty-plus-set (either side), whitespace, lowercase,
mixed case, and conflict. Both raise with a suffix-only message and status 2
(`ReleaseError.exit_status == 2`; `IDENTITY_ENVIRONMENT_CONFLICT_EXIT == 2`).
Only wording differs (leading capital, trailing period). **Concrete drift to
name:** C7 deletes the `FRAMENEST_` fallback from the package resolver. If that
commit touches only `src/framenest/identity_env.py`, `deploy/ubuntu/framenest-release`
and `production_ai_deploy.py` keep accepting `FRAMENEST_NUC_SSH_*` and
`FRAMENEST_PRODUCTION_SSH_TARGET` after the product has stopped accepting that
spelling — an operator-variable surface that silently outlives the server's.
Neither mirror leaks a value where the package would not.

**4. Writer invariance — established by enumerating write sites, not by grep
count.** Every new `COMPATIBLE_*` constant appears only in its own definition and
in an `ACCEPTED_*` membership set or candidate-name list; none appears in a write
position. Write sites verified individually: backup manifest writes
`APPLICATION_NAME = "framenest"`; `catalog_backup_workstation.py:836` writes
`MARKER_NAME`; the sidecar store writes `sidecar_names[0]` (`.framenest.json`);
`framenest_release.py:547-548` writes `.framenest-release-manifest.json` and
`.framenest-release-sha`. `FNCBE01`, `version("framenest")`,
`DEVELOPMENT_DATABASE_DIRECTORY = "framenest-development"` and
`env FRAMENEST_ENV_FILE=` appear on **no** `+`/`-` line of the whole
`18c357c..c02c675` diff. The dead `marker = store / MARKER_NAME` line removed
from `init_workstation_store` was provably unused at 18c357c (the function tests
`MARKER_NAME in children`), so its removal is not a writer change. **Nothing the
installed NUC reads became unreadable:** every `EnvironmentFile=` unit reads
uppercase keys, and my file-path differential shows uppercase, lowercase and
mixed-case file keys all behave as before.

**5. Exit statuses.** Independently verified for ordinary success, ordinary
failure and invalid invocation at 13 entry points. One counter-example found:
F3 (`framenest-ai`, 1 → 2). **Collision judgement (not a rubber stamp):** it
cannot mislead any real caller I could find. `framenest.service` uses
`ExecStartPre=… check-database-ready` with no `SuccessExitStatus`, so systemd
aborts on *any* non-zero and the journal carries the conflict message — the
collision is inert there. No script, unit, JS test or runbook branches on the
value `2`; `framenest_release.py` branches only on its own constants. In 9 of 11
colliding entry points the `error_code` differs from the usage error; in
`framenest-production` both use `FRAMENEST_PRODUCTION_COMMAND_FAILED` and only the
message distinguishes them. F3 adds one more ordinary error class to `framenest-ai`'s
exit 2. **`_database_state` judgement:** acceptable. The consequence is bounded —
`framenest-dev status` prints `Database: unknown` and its ordinary status exit, and
any path that would *act* on the database (`start` → `_migrate_database`) fails
closed with exit 2 and the conflict message. What can still go wrong is
diagnostic: an operator with a conflicting environment sees `unknown` with no
indication of the cause, and `start` reports the generic "Development database
migration failed." The residual risk is confusion, not a security bypass.

**6. Retention ledger.** **No pin is tautological.** Part A pins 89 SHA-256
literals from `ca649f6` and adds two completeness tests that cross-check the
pinned set against the tree — a genuinely independent police. Part B pins an
enumerated 20-path set, not a scalar. Part C pins scalars, so it detects *that*
the total moved but not *which* occurrences moved. On the Orchestrator's premise
about import statements: **partially incorrect.** What actually happened is that
new names were folded into **already-present** `framenest.*` imports
(`covers.py`, `library.py`, `previews.py`, `sidecar.py`, `persistence/cli.py`,
`youtube.py`, `configuration.py`), which is neutral for the counters and would
have happened anyway; where a new module import was unavoidable
(`identity_env` in `catalog_backup_ops.py`, `catalog_backup_offdevice.py`,
`ai/configuration.py`) the counters were re-pinned and each change was reported
with its cause. The pressure is real but low-grade, and it is a *ratchet*, not a
distortion: `ENV_PREFIX_BARE_SPELLING_COUNT` went 2 → 16 purely from C1's own
docstrings, and `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["deploy"]` went 218 → **212**
because composing prefix+suffix removed six literals — a real improvement the
implementing session flagged itself. **C3 will need a full re-pin, not an
incremental one** (every file moves to `kronika.*` and the ledger's own glob
`src/*/…` changes shape). **Would a genuinely missed rename fail at the owning
cut? Not reliably.** A cut that renames some things and re-pins the scalar to
match the partial work passes; the miss survives until a later cut's re-pin
fails to reconcile, i.e. at C7 at the earliest.

**7. Scope compliance and unexamined risk.** The full `18c357c..c02c675` diff
touches only the surfaces the accepted plan's C1 section enumerates. Against
`05_implementation_00.md`: every file outside the explicitly listed set is a
durable-artifact reader the plan names (backup manifest, sidecar format and
filename, workstation/off-device markers), which that prompt explicitly
encompassed; the ledger re-pin is enumerated with causes in `05_report_00.md`.
Against `06_correction_00.md`: no `deploy/**`, `docs/**`, `pyproject.toml`,
`ap.project.conf`, Alembic, `tailscale_ingress.py`, durable reader/writer, or
ledger change in C1b — verified by diff. One in-envelope judgement call for the
Orchestrator: C1b edited `configuration.py` and `identity_env.py`, which its
positive authority framed as "the in-package entry-point modules you enumerate".
**Highest-value missing test:** a *differential parity test* asserting that for
every settings field and a matrix of old-spelling-only inputs (case variants,
empty, whitespace, invalid), `_DualPrefixEnvSettingsSource` produces exactly what
the stock `EnvSettingsSource` + `parse_env_vars` produces. That single test would
have failed on F1 and F2 at the moment they were introduced, and it is the
invariant C1b's "no other exit status changed" claim actually rests on — today
that claim rests on reading, not on a check. Second: F4's spawned-child
environment has no test at all.

## Judgement on the four known-and-accepted items

1. **Retained `env_prefix="FRAMENEST_"`** — I found **no exposure from the
   retained prefix itself**. No bare ambient name is reachable: the prefix is
   applied when building the internal key, and `_identity_suffix` refuses any env
   name outside it. The exposure I found (F1) comes from the *replacement* of
   `env_vars`, not from the prefix. Retaining it is the right call.
2. **`EXIT_IDENTITY_ENVIRONMENT_CONFLICT` consumed once, mirrors keep their own
   constant** — correct and unavoidable for stdlib-only mirrors; the semantics
   are proven equivalent (§3). The one thing missing is a test that pins the
   mirrors to the package, which is cheap and would have caught any future drift.
3. **`_database_state` swallowing a conflict** — acceptable, as judged in §5.
   Residual risk is diagnostic only.
4. **Exit-2 collision** — acceptable, as judged in §5. Inert for systemd, inert
   for every script and unit I could find, distinguishable by error code or
   message in every case except `framenest-production`, where only the message
   separates them. H3 is the real cost: the release engine discards the remote
   text entirely, so an operator sees "command failed" instead of the cause.

## Resolved Execution Issues / Near-Misses

- I invoked `python3` once, as a text editor for my own throwaway probe file under
  `/tmp` (a `str.replace` patch). It produced no evidence about the repository.
  That was still contrary to the letter of "never invoke `python`/`python3` for
  evidence"; I switched to the edit tool immediately and used it thereafter. No
  repository evidence in this report came from that invocation.
- My client restricts external directories to `/tmp/opencode`, narrower than the
  prompt's `/tmp`. I used `/tmp/opencode/ksi07/` as the probe root; it is still
  under `/tmp`, so nothing outside `/tmp` was written.
- Five probe assertions were initially wrong and I initially read them as
  implementation defects. In each case the implementation was right and the probe
  was corrected: the new-header matrix rule, the whitespace-pair conflict
  expectation, a mistyped `X-FRAMEHOST-REQUEST` header name, a non-UUIDv4
  `--media-id`, and a relative-path case that aborts before spawning. Recorded
  because the first two would otherwise have become false findings.
- `ap exec` and the console-script probes necessarily refreshed `__pycache__/*.pyc`
  and `.pytest_cache/` inside the checkout. No tracked file changed;
  `git status --porcelain` is empty.

## Pre-Existing Failure Classification

none — no test failed. The five probe failures listed above were defects in my
throwaway probes under `/tmp`, not repository tests, and are not pre-existing
repository failures.

## Commands used beyond the declared routes

All Python evidence went through `./.ap/ap exec --baseline c02c675… --operation
test` / `test-focus`, plus `./.ap/ap project check` and `./.ap/ap doctor`.
JavaScript used `node --test tests/*.test.js`. Read-only Git: `status`,
`rev-parse`, `log`, `show`, `diff`, `ls-files`, `ls-remote`, `submodule status`.
Library source under `.venv/…/pydantic_settings/` was **read** with the read tool
(never imported by an interpreter I launched). Every console-script invocation
used a synthetic `env -i` environment with `HOME` and `TMPDIR` under
`/tmp/opencode/ksi07` and no inherited identity variable; the before/after file
tree of each run was captured and every conflict run created **no** files
(`new_files=[]`), while the old-only `framenest-db` runs created their SQLite
files under `/tmp/opencode/ksi07/exit/`. `--help` was run on six console scripts
to discover subcommands. Nothing outside `/tmp` was written; nothing in the
repository was modified; no NUC, provider, capture, network or dependency action
occurred.

## Smallest next step

Issue one bounded correction grant for **F1 + F2 + F4 on `c02c675`** — restore
pre-C1 semantics for old-spelling process-environment input (case-insensitive
matching; keep an explicitly empty old-spelling value so invalid input still
fails closed) and normalise the dev launcher's spawned child environment — with
the parity test from §7 as its required regression. F3 and F5 need an
Orchestrator decision (accept and amend the C1b goal; schedule the reader
widening with C5) and should not be bundled into that correction.

Authority expiry: on submission of this report all authority under the prompt
expires. No remediation, push, publication, NUC refresh or later cut is
authorized by it.

Orchestration critique:
MEASURED: the given `KRONIKA_` measurement is stated as "exactly three code
tokens" while a plain grep returns eight; evidence: the three assignments plus
five docstring occurrences, `git diff 18c357c..c02c675 | grep KRONIKA_`;
effect: an auditor must re-derive which occurrences are code; smallest
correction: state "three assignments of the literal `"KRONIKA_"`; five further
occurrences are in docstrings". Separately, the premise that sessions 05/06
"held counters fixed by extending existing import statements" is not what the
diff shows — evidence: the folded imports are counter-neutral and the re-pins
were caused by new module imports plus 14 new bare-prefix docstring occurrences;
effect: it points the audit at a distortion that did not occur; smallest
correction: describe the ledger pressure as a scalar ratchet, not import folding.
LEAD: the dev launcher may have the same unnormalised-injection shape for the
capture or sidecar child processes; cheapest useful check: grep every
`env[` assignment and `env=` subprocess construction in `src/framenest` for a
hand-written identity-prefixed name and compare it with the resolver's view.