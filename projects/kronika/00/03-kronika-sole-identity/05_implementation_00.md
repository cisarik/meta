# Authoritative Worker prompt — Worker session 05, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `05`, exchange `01`. Stored under the
Meta filename mapping as `05_implementation_00.md`, with report destination
`05_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C1 — dual-read identity resolver, both mutation header spellings, both durable artifact spellings, old writers unchanged
Reasoning recommendation: High
Recommended context capacity: approximately 250k tokens
```

Rationale for `High`: this cut widens a mutation-authorization boundary by
accepting a second header spelling, and it introduces a fail-closed conflict
path for 639 environment variables across 103 names. Those are named security
and cross-cutting risks that `Medium` should not resolve unaided. This is not
`Extra High`; there is no unresolved cross-cutting contradiction here. If you
judge the named risk removable at `Medium`, say so with the specific evidence
rather than silently downgrading.

This is cut **C1** of the accepted plan `03_report_00.md`. Cut C0 is published on
`main`. No later cut's authority is implied, and this cut does not authorize the
NUC refresh the plan schedules after it — that is a separate grant.

## Accepted plan and authority you implement under

The Orchestrator accepted `03_report_00.md` as decision-complete.
[ADR-0085](docs/adr/0085-kronika-sole-identity.md) is now published authority on
`main` and is the identity authority for this cut. Read both before editing. They
are frozen artifacts; do not edit them.

The single organizing rule of C1: **readers learn the new spelling, writers do
not.** Nothing in this cut may cause a newly written durable artifact, a newly
emitted error code, or a newly sent header to use `KRONIKA_`. The only new
`KRONIKA_` strings this cut may introduce are the resolver's own accepted input
spellings and the second accepted header spelling.

## Verified current state

```text
Repository checkout topology: standalone checkout
Expected branch: main
Expected HEAD: 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672
Expected subject: docs: record the Kronika sole identity in ADR-0085
Remote origin: https://github.com/cisarik/kronika
Public main: 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672
Public refs/heads/docs/adr-0085-kronika-sole-identity: same SHA
Working tree: clean
Containing-repository .ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS, governing variant stable
ap.project.conf projectId: cisarik/kronika, provenanceModule framenest
CPython: 3.13.9   pydantic-settings 2.14.2   Poetry: 2.3.2   Node: v26.8.2
Working directory: /home/agile/Projects/kronika
```

Baseline at this commit, measured by the Orchestrator through the canonical
route: Python `4159 passed, 8 skipped, 3 warnings, 0 failed`; JavaScript
`554 total, 549 passed, 0 failed, 5 skipped`. If your run does not reproduce
this, stop and report.

The retention test `tests/contract/test_kronika_identity_retention.py` is live
and green with 14 tests. It will constrain you: its Part B path-name ledger and
Part C occurrence ledger are pinned at their `18c357c` values and **will fail if
you change a path name or an occurrence count that this cut was not supposed to
change**. If it fails, that is the ledger working, not a broken test. Do not
weaken it. If a legitimate C1 change alters a pinned count, update the pin in
the same commit and state the exact delta and its cause in your report.

Host note: the development host is a CachyOS Linux workstation. The MacBook
paths in older artifacts are historical text. The stale clone at
`/home/agile/Projects/framenest` is not a work source and contains `private/`,
which you must never read.

## Exact mutation surface, verified at the baseline

These were measured by the Orchestrator. Re-verify; do not trust blindly.

```text
src/framenest/configuration.py:26   ENV_FILE_ENVIRONMENT_VARIABLE = "FRAMENEST_ENV_FILE"
src/framenest/configuration.py:141  SettingsConfigDict(env_prefix="FRAMENEST_",
                                        env_file_encoding="utf-8",
                                        hide_input_in_errors=True, extra="ignore")
                                    no env_file key; the file is passed per
                                    construction as FrameNestSettings(_env_file=...)
src/framenest/configuration.py:544  the loader reads ENV_FILE_ENVIRONMENT_VARIABLE
src/framenest/adapters/api/tailscale_ingress.py:80
                                    HEADER_MUTATION = b"x-framenest-request"
src/framenest/adapters/api/tailscale_ingress.py:858
                                    _single_value(header_map, HEADER_MUTATION)
                                      != EXPECTED_MUTATION_HEADER_VALUE
                                    -> 403, ERROR_MUTATION_HEADER_REQUIRED
src/framenest/infrastructure/persistence/catalog_backup.py:312
                                    application.name must equal "framenest"
src/framenest/application/ports/media_sidecar_store.py:12
                                    SIDECAR_FILENAME_SUFFIX = ".framenest.json"
src/framenest/domain/media_sidecar.py:34
                                    SIDECAR_FORMAT = "framenest-media-sidecar"
src/framenest/infrastructure/persistence/catalog_backup_transfer.py:33
                                    PROTOCOL_MAGIC = b"FNCBE01\0"   (unchanged in C1)
deploy/ubuntu/framenest_release.py:48,406,423,433
                                    ENV_FILE = "/etc/framenest/framenest.env" and
                                    injected `env FRAMENEST_ENV_FILE=`
```

Direct `FRAMENEST_` readers named by the plan, with current occurrence counts:
`src/framenest/infrastructure/persistence/catalog_backup_ops.py` 5,
`src/framenest/infrastructure/persistence/catalog_backup_offdevice.py` 1,
`src/framenest/infrastructure/runtime/development.py` 9,
`src/framenest/infrastructure/ai/configuration.py` 1,
`deploy/ubuntu/production_ai_deploy.py` 1.

There are 639 `FRAMENEST_` occurrences over 103 distinct names in total, and you
are routing a subset of them through one resolver. Enumerate the rest yourself
and report any reader you find that the plan and this list both missed.

## Required mutation

### 1. One resolver

Add one module, `src/framenest/identity_env.py`, exposing `lookup_env(suffix)`,
where `suffix` is the part after the prefix, for example `DATABASE_PATH`.

Precedence and conflict semantics, exactly:

| `KRONIKA_<SUFFIX>` | `FRAMENEST_<SUFFIX>` | Result |
|---|---|---|
| set | unset | the `KRONIKA_` value |
| unset | set | the `FRAMENEST_` value |
| unset | unset | the caller's default |
| set | set, identical | that value |
| set | set, different | **fail closed** |

Fail-closed means: a dedicated error type carrying the two **suffixes only**,
never a value, and no partial read. For CLI entry points the process exits with
status 2 and a message naming the suffixes only. No value, no length, no hash and
no repr of either value may appear in the message, the exception, the log, or a
test snapshot.

The resolver must treat a variable set to the empty string as **unset**, matching
the current behaviour of an unset prefixed variable, so that the currently
installed environment file and existing systemd `Environment=` handling do not
change meaning.

### 2. Route the settings model through the resolver

In `configuration.py`:

- `ENV_FILE_ENVIRONMENT_VARIABLE` bootstrap must resolve through the resolver, so
  both `KRONIKA_ENV_FILE` and `FRAMENEST_ENV_FILE` select the env file, and a
  conflict between them fails closed before the file is opened.
- Replace `env_prefix="FRAMENEST_"` with a settings source that consults the
  resolver for every field. Preserve exactly: the env-file source, the
  precedence that **process environment overrides environment-file values**,
  `extra="ignore"`, `env_file_encoding="utf-8"`, and
  `hide_input_in_errors=True`.

`hide_input_in_errors=True` is a secret-containment control, not a style
preference. A `KRONIKA_` prefix must not make a value leak into a validation
error where the `FRAMENEST_` prefix did not. Add a test that proves this for at
least one `SecretStr` field.

Verify the installed `pydantic-settings` `2.14.2` custom-source API by reading
it in the canonical `.venv` rather than assuming a signature. If the pinned API
cannot express a dual-prefix field source without weakening any preserved
behaviour above, **stop and report** with the exact API limitation. Do not
degrade `extra`, `hide_input_in_errors`, or the env-file precedence to make it
fit.

### 3. Route every direct reader through the same function

`catalog_backup_ops.py`, `catalog_backup_offdevice.py`,
`infrastructure/ai/configuration.py`, `infrastructure/runtime/development.py`,
`deploy/ubuntu/production_ai_deploy.py`, and the release helper's injected
env-file name. The release helper keeps injecting `FRAMENEST_ENV_FILE` in this
cut; that is correct and required, because the installed unit still uses the old
name until C6.

### 4. Accept both mutation header spellings

In `tailscale_ingress.py`, accept the mutation when `x-kronika-request` is `1` or
`x-framenest-request` is `1`, preserving today's exact value expectation
`EXPECTED_MUTATION_HEADER_VALUE`. Required edge behaviour:

- A header present with any value other than `1` is rejected, exactly as today.
- If both spellings are present, **both must be `1`**; otherwise rejected.
- The `403`, the error code `ERROR_MUTATION_HEADER_REQUIRED`, and the existing
  sanitized message shape are unchanged. You may reword the human message to name
  both spellings; you may not change the code, the status, or add any
  header-derived value to the response.
- Senders in this cut still send only `X-FrameNest-Request`. That is the browser
  work of C2 and is out of scope here.
- Do not add the new spelling to any CORS, allow-origin, or companion-origin
  list. This is a mutation gate, not an origin gate.

### 5. Readers accept both spellings for durable artifacts

No writer changes. Readers gain a second accepted spelling:

- backup verification accepts `application.name` equal to `framenest` **or**
  `kronika`;
- sidecar readers accept format `framenest-media-sidecar` **and**
  `kronika-media-sidecar`, and filename suffix `.framenest.json` **and**
  `.kronika.json`;
- off-device and workstation marker purposes and marker filenames accept both
  spellings;
- release-manifest readers accept key `framenest_release_sha` **and**
  `kronika_release_sha`;
- release-marker filename readers accept `.framenest-release-sha` and
  `.framenest-release-manifest.json` **and** the `.kronika-*` pair.

`PROTOCOL_MAGIC` `FNCBE01` is unchanged. `importlib.metadata.version("framenest")`
is unchanged until C3. Emitted CLI error-code strings stay `FRAMENEST_*` in this
cut. `DEVELOPMENT_DATABASE_DIRECTORY` stays `framenest-development`.

The NUC environment file at `/etc/framenest/framenest.env` must keep working
unchanged, because the new code still reads `FRAMENEST_`. That is the whole point
of this cut and needs a test that proves it.

## Authority

```text
Positive authority: create exactly src/framenest/identity_env.py; edit exactly
  src/framenest/configuration.py,
  src/framenest/adapters/api/tailscale_ingress.py,
  src/framenest/infrastructure/persistence/catalog_backup_ops.py,
  src/framenest/infrastructure/persistence/catalog_backup_offdevice.py,
  src/framenest/infrastructure/ai/configuration.py,
  src/framenest/infrastructure/runtime/development.py,
  deploy/ubuntu/production_ai_deploy.py,
  deploy/ubuntu/framenest_release.py,
  and the minimal set of reader files that the durable-artifact and release-marker
  reads above actually require, which you must enumerate and report explicitly
  before relying on them;
  create tests for every behaviour listed under Required mutation;
  update the pinned values in
  tests/contract/test_kronika_identity_retention.py only where this cut
  legitimately changes a pinned count or path, and report each change;
  create one local branch named feat/kronika-identity-dual-read from main;
  stage and commit only the paths you reported; run the declared AP test
  operations and the declared JavaScript test route; run read-only Git inspection.

Negative authority: any change to ap.project.conf, pyproject.toml, .gitmodules,
  .gitignore or any packaging or console-script entry; any package move or
  directory rename; any import of the form `from kronika...`; any change to
  docs/adr/*, AGENTS.md, README.md, PRODUCT.md, SPEC.md, SECURITY.md, SERVER.md,
  DEVELOPMENT.md, ROADMAP.md or the ADENTS/ADR managed blocks; any change to the
  36 applied Alembic revision files or to any file in src/framenest/infrastructure/
  persistence/alembic_environment/versions/; any change to PROTOCOL_MAGIC; any
  change to a systemd unit source, to deploy/systemd/**, or to an installed host
  path string; any writer switching to a KRONIKA_ spelling, including backup
  manifests, sidecars, markers, error codes and sent headers; any removal of a
  FRAMENEST_ reading path; any dependency install, update or lockfile change; any
  Git push, tag, merge, rebase, remote branch creation or history rewrite; any
  NUC contact, including SSH, the NUC worker gate, and
  deploy/ubuntu/framenest-release in every mode; any provider or capture-browser
  contact; any reading of private/, personal Fish configuration, browser
  profiles, cookies, tokens, credential stores, .secrets or ~/.config/opencode;
  any write to /home/agile/meta.

Commands: Python evidence and tests go only through the canonical declared
  route, `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  18c357cf6f8c5ff9cc3b2c28e638510fc73a3672 --operation <id> -- <argv>`, with
  operations declared in ap.project.conf, plus `./.ap/ap project check --root
  /home/agile/Projects/kronika --baseline
  18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`. JavaScript tests use the declared
  `node --test` route. Never invoke `.venv/bin/python`, `python`, `python3` or
  `poetry run` for evidence. To read the installed `pydantic-settings` API, use
  the declared `runtime-info` operation or add a focused test that imports it;
  do not shell out to an interpreter. Read-only Git inspection is allowed (`git
  status`, `git rev-parse`, `git log`, `git show`, `git ls-files`, `git grep`,
  `git ls-remote`, `git submodule status`, `git merge-base`); no other Git
  command. Any other command you need must be stated in the report with its
  purpose and a confirmation that it mutated nothing.

Dependency authority: none. The canonical `.venv` is correct. Do not reinstall,
  update or relock anything. If you conclude a new dependency is required, stop
  and report instead.

Git authority: create the named local branch, stage only the reported paths, make
  exactly one local commit. No push, no publication, no tag, no merge.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none. Never print, quote or summarize secret values, host
  identifiers, addresses, disk serials, UUIDs or SSH fingerprints. This applies
  with extra force to the fail-closed conflict path, which must reveal suffixes
  only.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope; the
  accepted plan `03_report_00.md` and this prompt are task context, not higher
  authority. On conflict between retained context and current repository evidence,
  stop.

Side-effect authority: reversible local repository mutation only. No destructive
  mutation, no remote effect, no deployment, no credential effect, no billing
  effect.

Browser authority: none.
```

## Verification

Before editing confirm branch `main`, HEAD `18c357c…`, clean tree, public `main`
equal, submodule at the pin, `ap doctor` PASS, `ap project check --baseline` PASS.
Stop without editing if any fails. Re-enumerate the mutation surface above and
report any reader the plan and this prompt both missed.

Then:

1. Reproduce the baseline once with the declared `test` operation and
   `node --test tests/*.test.js`. Expect `4159 passed, 8 skipped, 3 warnings` and
   `549 passed, 0 failed, 5 skipped`. The suite takes about eleven minutes; let
   it finish once.
2. Implement every mutation above.
3. Run the retention test. If a pinned value moved, justify it; never weaken the
   test to make it pass.
4. Run the full declared `test` operation once. Report exact counts. Skips must
   remain 8 and warnings 3; any other movement needs explanation.
5. Run `node --test tests/*.test.js`. Only the mutation header expectations can
   legitimately change; report the exact delta.
6. Prove each of these positively and negatively, and report each as a named
   test: `KRONIKA_` alone works for a settings field; `FRAMENEST_` alone still
   works for the same field, including the shape of the installed
   `/etc/framenest/framenest.env`; identical values in both prefixes are
   accepted; conflicting values fail closed with exit 2 for a CLI path and no
   value in any message or log; an empty-string variable behaves as unset; an
   unknown extra `KRONIKA_` variable does not raise; a `SecretStr` field does not
   leak its value in a validation error under either prefix; both header
   spellings authorize; `x-kronika-request` with a wrong value is rejected;
   `x-framenest-request` with a wrong value is still rejected; both present with
   one wrong value is rejected; an old-name backup manifest still verifies; a
   new-name manifest also verifies; sidecar, off-device marker, workstation
   marker, release-manifest key and release-marker filename readers accept both
   spellings; and no writer emits a `KRONIKA_` spelling.
7. Confirm `git diff` is empty for `ap.project.conf`, `pyproject.toml`,
   `ap.project.conf`, `deploy/systemd/**`, `src/kronika_capture/**`, and the 36
   applied Alembic revision files.
8. After the commit run `./.ap/ap project check --root /home/agile/Projects/kronika
   --baseline <new commit SHA>` and confirm PASS. `ap.project.conf` is unchanged
   in this cut, so the C3 re-gate is **not** triggered here; the pre-commit
   baseline stays valid.

```text
Evidence tier: E2. Cross-cutting, multiple layers, user-visible compatibility,
  and a widened mutation-authorization boundary. This is local development-surface
  mutation with no remote effect, so it is not E3. Because the mutation gate is a
  trust boundary, a fresh independent audit is recommended after this cut and
  before C2. The NUC refresh the plan schedules after C1 is a separate E2 deploy
  grant, and the E3 read-only status observation after it is separate again.
```

## Git

One local commit on `feat/kronika-identity-dual-read`, parent
`18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`. Suggested subject:

```text
feat(identity): read both KRONIKA_ and FRAMENEST_ spellings, write only the old
```

Do not push.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the baseline does not reproduce; if the pinned pydantic-settings API
  cannot express the dual-prefix source without weakening a preserved
  behaviour; if a required change would need a new dependency; if any step would
  need a path outside the reported mutation surface; if you find a `FRAMENEST_`
  reader the plan and this prompt both missed and cannot route it through the
  resolver; if any writer would have to change; if the full suite shows a
  failure you cannot attribute and cannot explain with evidence; if context
  pressure reaches the point where a bounded rotation is cheaper than a degraded
  commit.

Completion: exactly one commit on the named branch, both prefixes reading, all
  writers unchanged on the old spelling, the installed env file shape proven to
  keep working, both header spellings proven with negative cases, the retention
  test green or its pin updated with a justified delta, both routes green, and
  the tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `05_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this
  prompt expires. No further implementation, no push, no publication, no NUC
  refresh and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
Published NUC state: unchanged; the NUC still serves release
  0c850996cd2ef17dae4112733fd17fdc732f4699
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `05` and exchange `01` unchanged. Then:
the exact diff of every path; the complete list of reader files you touched and
the `FRAMENEST_` occurrences you routed through the resolver in each; every
`FRAMENEST_` reader you found that the plan and this prompt both missed; the
mechanism you used for the dual-prefix settings source and how you verified it
against the installed `pydantic-settings` version; how you preserved
`hide_input_in_errors`, `extra="ignore"`, `env_file_encoding` and
process-over-env-file precedence; the named test for each item in Verification
step 6; proof that no writer emits a `KRONIKA_` spelling; the installed env file
compatibility test; baseline and final exact counts for both routes; each
retention-test pin change with its cause; the branch name and commit SHA;
deviations, risks and missing evidence; and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification.

Finish every terminal report with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

If your client's native surface forces any preamble above the report header,
disclose it on the first line of the report body, as sessions 03 and 04 did.

## Mandatory reading

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/03_report_00.md`,
  the accepted plan. C1 is its second cut; read C1 and its C5 and C6
  preconditions, because C5 and C6 depend on this cut being installed first.
- `docs/adr/0085-kronika-sole-identity.md` in full.
- `src/framenest/configuration.py` in full, especially lines 26, 138-146 and
  536-560.
- `src/framenest/adapters/api/tailscale_ingress.py` around lines 60-95 and
  840-880.
- `src/framenest/infrastructure/persistence/catalog_backup.py` around line 312,
  `src/framenest/infrastructure/persistence/catalog_backup_transfer.py` around
  line 33, `src/framenest/domain/media_sidecar.py` around line 34,
  `src/framenest/application/ports/media_sidecar_store.py` around line 12.
- `deploy/ubuntu/framenest_release.py` around lines 37-50, 400-440 and 880-960.
- `tests/contract/test_kronika_identity_retention.py` in full, so you know
  exactly what it pins.
- Existing tests covering settings, the mutation header, backup verification,
  sidecars and the release remote contract, so you extend the established
  conventions instead of inventing new ones.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md` Worker Execution section,
  `.ap/AP_WORKER.md`, and `.ap/AP.md` §5, §9, §10 and §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, or
any credential store.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak in repository or report artifacts.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the diff, the writer-invariance claim and
the counts. Because this cut widens a mutation-authorization boundary, a fresh
independent audit is the expected next envelope before C2. Publication of this
branch and the routine NUC refresh are each separate bounded grants; neither
follows from acceptance.