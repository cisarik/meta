# Authoritative Worker prompt — Worker session 03, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `03`, exchange `01`. Stored under the
Meta filename mapping as `03_planning_00.md`, with report destination
`03_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Task identity: KSI-PLAN-02 — plan-only — decision-complete identity-cut sequence
Reasoning recommendation: High
Recommended context capacity: approximately 250k tokens
```

Rationale for the reasoning recommendation: the task crosses a live-service
migration boundary, couples independently-renameable identity classes that
interact, and must order cuts so the NUC keeps serving after each published
step. That is named architectural-ambiguity risk, which `High` covers. The
opening handout recommended `Extra High`; I am not escalating, because the one
genuine cross-cutting contradiction — ADR-0082 versus the Cooperator's
2026-10-02 statement — is a documentation decision reserved to the Orchestrator
and Cooperator, not something this Planner must reason through. If you judge the
missing evidence to be genuinely unresolvable at `High`, stop and name it.

### Why this is a fresh session and not session 01

Worker session `01` was the initial Planner and returned `BLOCKED` at
`0c850996…` before producing any plan, because a required green baseline did not
exist. That cause is now removed. The whole's one initial plan-only cycle has
therefore not yet yielded a plan, and no automatic targeted revision has been
used. Resumption is routed to a fresh session because the delivery client has
changed across exchanges, so a current-session claim could not be verified at
the client boundary. Session ordinals are contiguous and are never reassigned:
`01` Planner, `02` Bounded Correction Worker, `03` this Planner.

Nothing is lost. Read `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/01_report_00.md`
and treat its findings as Orchestrator-verified input, not as another Worker's
unverified claim: each of its eight material findings and each of its four
inventory corrections was independently reproduced and confirmed by the
Orchestrator before this prompt was issued.

## Implementation-planning contract

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded technical planning of the retirement of the framenest product identity — reconnaissance, impact mapping, interfaces, the ADR or ADR amendment that must precede implementation, compatibility windows and their removal gates, the per-cut ordering, rollback, and the exact proposed mutation for each cut
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
```

## Planning record

```text
Planning cycle: initial
Prior planning report: none — Worker session 01 exchange 01 returned BLOCKED before producing any plan
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: the accepted decisions listed below
Automatic targeted revisions used: 0
```

This remains the whole's initial planning cycle. It does not consume the single
automatic targeted revision, because no plan exists to revise.

## Goal

Produce one decision-complete cut sequence that retires the remaining
`framenest` product identity so that the running product, its commands, its
request header, its settings prefix, its systemd units and its host paths are
Kronika, while the NUC keeps serving after every published step.

The plan's useful outcome is the ordering and the exact proposed mutation per
cut, not a summary of what is named `framenest`.

## Accepted decisions you must treat as fixed

- One product identity: Kronika. On 2026-10-02 the Cooperator stated that the
  `framenest` identity does not remain, and that the product name is Kronika
  including NUC paths and script names.
- That statement supersedes the "kept for now / no mass rename" limit recorded
  in ADR-0082. It does **not** rewrite ADR-0082. ADR-0082's original wording
  stays historical text. This whole records the new decision in its own ADR or
  ADR amendment **before** any implementation, and it must not hide the cut
  inside an unrelated fix.
- One repository, `https://github.com/cisarik/kronika.git`. No second product.
  No Git history rewrite. No force push.
- `https://github.com/cisarik/cli_chatgpt.git` stays active at
  `66c40d43c577276b0ad304a494fbbb1ffb6fc933`. Do not archive it.
- `kronika_capture`, the command `kronika-capture` and the `kronika-capture-*`
  units are already on the Kronika side. Do not rename them again.
- Loopback-first application. Tailscale-only remote ingress. No public
  listener, no router forwarding.
- Owner-private new records; administrator read of product records without
  provider secrets or host administration; household publication only by
  administrator approval. Internet publication stays off.
- Search and Research run through the ADR-0083 / ADR-0084 provider boundary.
  Research stays disabled by default in code. The NUC's saved research settings
  are host state, not a reason to change the default.
- Gallery remains a separate working view. The accepted Gallery and Details
  visual behavior stays frozen unless a concrete defect is identified.
- Parked rows stay parked: S3 host remainder, capture-mode Search and Research,
  S5 ZIP activation, S7-C. S7-P does not switch media analysis to the research
  provider.
- Alembic history applied through `0035` on the NUC is immutable. Do not rewrite
  applied revision ids and do not edit old revisions in place. A rename of
  living code may add a new migration.
- The AP pin `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. An AP upgrade is a
  separate task and is out of scope.
- The release helper's same-schema rule stands. A host cut that changes schema,
  unit names, or the filesystem layout is **not** a routine
  `deploy/ubuntu/framenest-release` deploy.
- The following named residuals from the predecessor audit are carried and are
  **not** authorization to fix them inside the identity cut: L-1 cached-tokens
  missing wording; L-2 a disabled settings write may store an expired model
  while generation stays fail-closed; L-3 dirty-draft discard confirmation is
  unimplemented and fail-safe under compare-and-set; L-4 and L-9 through L-11.
- Separate undiagnosed observation: on 2026-10-02 the shell's media AI
  indicator was unavailable because the last configured-provider test did not
  reach the provider. Cloud was connected. Do not fold a credential or provider
  repair into the rename.

## Verified current state

Verified read-only by the Orchestrator at the new baseline. Re-verify; do not
trust it blindly.

```text
Repository checkout topology: standalone checkout
Expected branch: main
Expected HEAD: ca649f6eb6231591292e174dff994fd0f4448378
Expected subject: fix(test): isolate the operator gate Fish tests from personal configuration
Remote origin: https://github.com/cisarik/kronika
Public main: ca649f6eb6231591292e174dff994fd0f4448378 (verified by git ls-remote)
Public refs: refs/heads/fix/operator-gate-test-hermetic also ca649f6eb6231591292e174dff994fd0f4448378
Working tree: clean
Containing-repository .ap gitlink: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
Submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS, governing variant stable
ap.project.conf projectId: cisarik/kronika
CPython: 3.13.9   Poetry: 2.3.2   Node: v26.8.2   fish: 4.9.3
Working directory: /home/agile/Projects/kronika
```

Baseline test result at this commit, measured by the Orchestrator through the
canonical route:

```text
Python declared test operation: 4145 passed, 8 skipped, 3 warnings, 0 failed
JavaScript node --test tests/*.test.js: 554 total, 549 passed, 0 failed, 5 skipped
```

A green baseline now exists. If your own run does not reproduce it, stop and
report rather than planning on a different state.

Host note. The development host is a CachyOS Linux workstation, not the
MacBook. The historical MacBook path `/Users/agile/Projects/framenest` in older
artifacts is historical text, not a path on this host. The canonical checkout is
`/home/agile/Projects/kronika` on `main`. A stale second clone exists at
`/home/agile/Projects/framenest` on branch `feat/kronika-one-product` at
`38e7beeb3921d7c0fd8e717e480754fbd18130c9` with remote `cisarik/framenest.git`;
it is an ancestor of `main`, it is not the work source, and it contains a
`private/` directory you must never read.

### Identity inventory, corrected

Counts were taken at `0c850996…`, which differs from this baseline only by one
test file that contains no `framenest` identity. Re-verify rather than copy.
Corrections to the first issued table are marked; they are the Orchestrator's
error, not a discovery.

| Class | Count |
|---|---:|
| `src/framenest` Python modules | 284 files |
| Files containing case-insensitive `framenest`: src / tests / deploy / scripts / docs / extension | 254 / 314 / 19 / 7 / 87 / 12 |
| Matching tracked Markdown files, including nested | 100 |
| Distribution name in `pyproject.toml` / AP `provenanceModule` | `framenest` / `framenest` |
| `framenest-*` console script entries | **14 total = 13 application commands plus the `framenest-chatgpt-page` alias**. *Corrected: the first table double-counted the alias.* |
| `FRAMENEST_` prefix | 639 occurrences, 103 distinct names; leading `FRAMENEST_DATABASE_PATH` 67, `FRAMENEST_PORT` 51, `FRAMENEST_ENV_FILE` 40, `FRAMENEST_HOST` 30, `FRAMENEST_API_KEY` 19, `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` 18 |
| `X-FrameNest-Request` | 53 occurrences in **28** files. *Corrected: 28, not 27.* In `tests/*.test.js`: **9**. *Corrected: 9, not 10.* In `docs/adr/*`: **5**. *Corrected: 5, not 8.* |
| `/opt/framenest` / `/etc/framenest` | 198 / 73 |
| `/var/lib/framenest` / `/var/cache/framenest` | 91 / 20 |
| `/mnt/framenest-catalog-offdevice` | 12 |
| `User=framenest` / `Group=framenest` | 5 / 5 |
| `deploy/systemd` sources still `framenest` | `framenest.service`; `framenest-catalog-backup.service`/`.timer`; `framenest-catalog-offdevice.service`/`.timer`; `framenest.env.example`; `framenest-ai-credential-nvidia-nim.conf`; `framenest-ai-credential-opencode-go.conf`; `framenest-ai-credential-vercel-ai-gateway.conf`; `framenest-research-credential.conf` |
| `scripts/operator` scripts | `infosec/framenest_log_triage.sh`; `infosec/framenest_public_surface_check.sh`; `infosec/framenest_socket_permissions_check.sh`; `network/framenest_mullvad_egress.fish`; `network/framenest_mullvad_egress.sh`; `network/framenest_nuc_worker_gate.fish` |
| `deploy/ubuntu` operator entry points | `framenest-release`; `framenest_release.py`; `framenest-catalog-export-v1`; `fn-production-env-deploy`; `production_ai_deploy.py` |
| Repository-root fish launcher | `./framenest`, tracked, invoking `.venv/bin/framenest-*` |
| Alembic migrations | 36 files under `src/framenest/infrastructure/persistence/alembic_environment/versions/`, head `0035_research_requests_and_accounting.py` |
| Capitalized prose `FrameNest` | 3335 occurrences in 478 files |

### Verified material findings carried forward

Each of these was independently confirmed by the Orchestrator. Treat them as
established; your job is to design around them, not to re-litigate them.

1. **Applied migration history imports the package name.** 11 applied revision
   files import `framenest.infrastructure.persistence.sqlite_batch_fk`. Moving
   the Alembic directory and changing `DEFAULT_MIGRATION_PACKAGE` alone breaks
   loading that history. The design must preserve applied bytes and cover both a
   fresh database and loading the existing `0035` database.
2. **Capture and web share the old `/opt` hierarchy.** `RELEASE_ROOT =
   "/opt/framenest/releases"` and `CAPTURE_CURRENT = "/opt/framenest/capture-current"`
   at `deploy/ubuntu/framenest_release.py:37,39`, and the capture bridge and
   runner units use `/opt/framenest/capture-current` at
   `deploy/systemd/kronika-capture-bridge.service:11,14` and
   `kronika-capture-runner.service:11,18`. A web path migration needs explicit
   capture-path continuity, and the existing `activate-capture` operation
   restarts the runner, so it cannot serve as an incidental rename step.
3. **Settings consumers extend beyond `FrameNestSettings`.** AI configuration,
   backup operations, off-device configuration, the development launcher,
   deployment helpers and operator scripts read `FRAMENEST_` names separately.
   Prefix compatibility confined to `configuration.py` would be incomplete.
4. **The header is only one companion compatibility boundary.** The repository
   also contains branded companion protocol identifiers, message sources,
   connection names, globals and browser recovery or storage keys. Their
   transition must preserve the installed extension and open browser contexts
   until the Cooperator-visible update step.
5. **Backup and recovery identifiers are durable contracts.** Backup
   verification currently requires `application.name == "framenest"` at
   `src/framenest/infrastructure/persistence/catalog_backup.py:312`. Sidecars,
   workstation stores, off-device markers and snapshot metadata also carry
   branded identifiers. New writers cannot change these before the corresponding
   readers and rollback path understand them, and existing archives must remain
   unchanged.
6. **AP contract migration needs an explicit trust handoff.** The pinned AP
   executable rejects `ap exec` when the working `ap.project.conf` differs from
   the authorized baseline. `--candidate` provides readiness evidence only; it
   cannot authorize execution against a newly renamed provenance module.
7. **Release preparation already creates a release-local environment.** The
   helper installs through pinned Poetry into staging and relocates staging paths
   in scripts and installation metadata. Its relocation checks currently require
   `framenest-db` and `framenest-backup`, and its operational commands require
   the old production executable. Those checks must change together with
   packaging and installed-unit compatibility.
8. **Historical and living documents are mixed.** The ADR index ends at `0084`,
   so `0085` is the next available number at this baseline. Several living
   documents contain dated historical paragraphs, while documents such as the
   Fedora service guide explicitly retain historical evidence. A blanket
   filename or text replacement is insufficient.

The NUC migration remains the highest-risk prospective cut: account identity,
absolute interpreter paths, release environments, credential source paths,
service units, persistent state, socket ingress and rollback are coupled.
Repository inspection cannot prove the installed host's current readiness.

Installed NUC state, observed read-only on 2026-10-02 and not re-verified by
the Orchestrator: `framenest.service` enabled; `framenest-catalog-backup.service`
and `.timer` enabled; `kronika-capture-bridge`, `-runner` and `-xvfb` enabled;
`kronika-capture-view` and `-vnc` static; the off-device catalog units were not
in the installed list. Web release at `0c850996cd2ef17dae4112733fd17fdc732f4699`,
service active, database revision `0035`, backup ready. Capture release
unchanged at `94e605c17b881461fad3e22fd8c7fca32cb93976`.

Accepted NUC tooling paths that must **not** be renamed by text substitution:
Poetry `/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry` and CPython
`/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13`.
A live cut is a migration of a running service, its Unix account, its
environment file, its state directories and its release helper together.

## Questions the plan must answer

1. What exact ADR or ADR amendment text records the new identity decision before
   any code changes, what is its number, and what exactly does it supersede in
   ADR-0082 without rewriting ADR-0082?
2. What is the exact cut sequence, and what is the published state of the NUC
   after each cut? The bar is: still serving, no manual rescue.
3. Per cut, the exact proposed mutation: paths, symbols, signatures, packaging
   metadata, test changes, documentation changes, and the evidence that closes
   that cut.
4. How is the `FRAMENEST_` prefix retired with a compatibility window long
   enough for the installed `/etc/framenest/framenest.env`, including command
   error codes, and what is the exact removal condition for the fallback?
5. How is `X-FrameNest-Request` retired compatibly, given the Brave companion
   extension sends it? Name the Cooperator-visible step of reloading or updating
   the extension, and the exact server-side acceptance window during which both
   spellings are honoured.
6. How are the systemd units renamed in Git while the installed units keep
   working, and how is `deploy/ubuntu/framenest-release` replaced without
   creating a second deployment system or a period with no entry point?
7. What is the separately authorized NUC migration sequence for the Unix
   account, `/opt`, `/etc`, `/var/lib`, `/var/cache`, the systemd
   `StateDirectory`/`CacheDirectory`/`RuntimeDirectory`, and the installed
   units? Writers stop first. Capture units are not restarted as a side effect.
   The catalog database, media, profiles, secrets and backups are not deleted.
8. What is the rollback for each cut, and which cuts are one-way?
9. Does the Alembic environment directory move with the package? If so, what is
   the exact safe mechanism that adds a migration without editing applied
   revisions, and what proves the NUC's `0035` database is unharmed?
10. `pyproject.toml` project name and `provenanceModule` both participate in
    identity. `ap.project.conf` is part of the AP baseline contract, so
    changing `provenanceModule` changes the trusted baseline. What is the exact
    ordering and the exact re-gate, and what is the correct
    `--baseline`/`--candidate` handling for that step?
11. How is the distribution rename handled in the installed release virtual
    environment, so that `ExecStart` resolves a `kronika-production` binary and
    the old `framenest-production` name does not survive as a stale alias?
12. Which occurrences are historical text that must stay, and which are living
    prose that must go? Give an explicit rule and its verifiable test, not a
    list of judgement calls. Historical ADRs, applied Alembic revisions and
    accepted-history documents stay.
13. What is the total effort and risk ordering across cuts, and which cut is the
    one most likely to leave the NUC not serving?

Additionally, answer this one, which the previous attempt could not reach:

14. `scripts/operator/network/framenest_nuc_worker_gate.fish` is renamed by this
    work, and the Cooperator operates that gate from his own shell on this host
    with `FRAMENEST_NUC_SSH_TARGET`, `FRAMENEST_NUC_SSH_USER` and
    `FRAMENEST_NUC_SSH_IDENTITY` present as exported Fish universal variables.
    What is the exact compatibility window and the exact Cooperator-visible step
    that retires those ambient names without breaking his operator workflow, and
    how is it verified without reading his personal configuration?

## Authority

```text
Positive authority: read-only inspection inside /home/agile/Projects/kronika,
  including .ap at its pinned commit; read-only public verification of
  https://github.com/cisarik/kronika.git and https://github.com/cisarik/ap.git;
  read-only inspection of /home/agile/Projects/framenest for topology facts
  only, excluding private/; Python and test execution through the canonical
  declared AP route only; execution of read-only commands outside that route
  only when a specific planned verification step requires it, disclosed in the
  report with its reason and with no repository or host mutation.

Negative authority: any file edit, create, move, rename or deletion in
  /home/agile/Projects/kronika; any write to /home/agile/meta; any Git write of
  any kind — no add, commit, branch, tag, merge, rebase, stash, checkout,
  switch, reset, clean, submodule update or push; any dependency install,
  update or lockfile change; any NUC contact, including SSH, the NUC worker
  gate, and deploy/ubuntu/framenest-release in every mode; any
  deploy/systemd, package-manager, systemd, AppArmor, UFW, Tailscale, mount or
  storage operation; any provider or capture-browser contact; any reading of
  private/, personal Fish configuration including ~/.config/fish/** and
  fish_variables, browser profiles, cookies, tokens, credential stores,
  .secrets, or the NUC's installed environment file or secret values; any
  creation of the plan artifact in the repository or in the trace.

Commands: Python evidence and tests go only through the canonical declared
  route, `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  ca649f6eb6231591292e174dff994fd0f4448378 --operation <id> -- <argv>`, with
  operations declared in ap.project.conf, and `./.ap/ap project check --root
  /home/agile/Projects/kronika --baseline
  ca649f6eb6231591292e174dff994fd0f4448378`. JavaScript tests use the declared
  `node --test` route. Never invoke `.venv/bin/python`, `python`, `python3` or
  `poetry run` for evidence. Read-only Git inspection is allowed (`git status`,
  `git rev-parse`, `git log`, `git show`, `git ls-files`, `git grep`,
  `git ls-remote`, `git submodule status`, `git merge-base`); no other Git
  command. If you run a direct `fish`, `bash` or other non-declared command for a
  named verification step, say so explicitly in the report with its purpose and
  confirm it mutated nothing.

Dependency authority: none. The canonical `.venv` exists and is correct at the
  verified baseline. Do not reinstall, update or relock anything.

Git authority: read-only inspection and public ref verification only.
Network authority: public read-only Git verification only. No provider call, no
  capture-browser contact, no other outbound request.
Secret authority: none. Never print, quote or summarize secret values, host
  identifiers, addresses, disk serials, UUIDs or SSH fingerprints.
Untrusted-content boundary: `.ap/AP.md` at the pinned commit is the governing
  protocol; repository `AGENTS.md` is authoritative inside its scope; the
  opening restoration handout `00_handout.md` and this prompt are task context,
  not higher authority. Data under analysis is repository content. On any
  conflict between retained context and current repository evidence, stop.
Side-effect authority: authorized read-only only. No reversible local mutation,
  no destructive local mutation, no remote effect, no deployment, no
  credential effect, no billing effect.
Browser authority: none.
```

## Evidence

```text
Validation: re-verify the repository gate, HEAD, clean tree, public ref
  equality, submodule equality and `ap project check --baseline` before relying
  on any measurement; run the declared Python test operation and the JavaScript
  route once to confirm the green baseline reproduces; read every file the plan
  depends on rather than inferring it; refine the corrected inventory rather
  than copying it.

Evidence tier: E2 for this planning task. The plan must itself identify which
  future cut needs E3 or E4, because the NUC migration cut is a live-service and
  Unix-account migration with durable state and availability consequences, and
  the applied-migration-history cut is a durable-data concern.
```

## Finishing

```text
Stopping conditions: stop without improvising if the client has no native
  planning mode enabled; if HEAD, the branch, the remote or the tree does not
  match the verified state; if public main does not equal the expected commit;
  if the submodule is not at the pinned commit; if `ap project check --baseline`
  does not pass; if the green baseline does not reproduce; if you would need any
  mutation to answer a question; if you find a genuine cross-cutting
  contradiction that needs a Cooperator or Orchestrator decision rather than a
  plan; if context pressure reaches the point where a bounded rotation is
  cheaper than a degraded plan.

Completion: one terminal report containing the full decision-complete plan, not
  a summary of it.

Required report sections: the standard report core and header; the full cut
  sequence with per-cut proposed mutation, evidence and rollback; the ADR text
  or a complete specification of it; the answer to each of the fourteen
  questions above; your own re-counted identity inventory with any delta against
  the corrected table and the reason for it; the reproduced green baseline with
  exact counts; open questions requiring an Orchestrator or Cooperator decision;
  risks; one smallest next step.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `03_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal planning report, all planning
  authority expires. Implementation in this session is prohibited. A later
  execution authority event is an explicit ORCHESTRATOR prompt with Native
  planning mode: not-used.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-evidence`.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification.

Finish every terminal report with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

## Mandatory reading

- `.ap/AP.md` at the pinned commit, in particular §1 Distribution Model, §3
  Instances/Sessions/Worker Session Profiles, §5 Task Authority, §6 Adaptive
  Orchestration Lifecycle, §13 Artifact Lifecycle, §19 Anti-Patterns, and the
  Plan-to-Execution Gate.
- `.ap/AP_WORKER.md` in full.
- `AGENTS.md` at the repository root, including its managed AP integration
  block and its Worker Execution section.
- `docs/WORKER_EXECUTION_CONTRACT.md`.
- `docs/adr/0082-kronika-one-product-and-private-records.md`,
  `docs/adr/0083-modular-research-providers-and-administrator-curated-timeline.md`,
  `docs/adr/0084-administrator-managed-research-settings-and-versioned-pricing.md`,
  and `docs/adr/README.md`.
- `ROADMAP.md`, `PRODUCT.md`, `SPEC.md`, `SECURITY.md`, `SERVER.md`,
  `README.md`, `DEVELOPMENT.md` — for living prose that must change, and for
  accepted limits that must not.
- `pyproject.toml`, `ap.project.conf`, `.gitmodules`, `.gitignore`.
- `deploy/systemd/*`, `deploy/ubuntu/*`, `scripts/operator/**`.
- `src/framenest/configuration.py` in full, and every place that constructs or
  consumes a `FRAMENEST_` name.
- `src/framenest/adapters/api/web/app.js` header construction, the route layer
  that requires it, and `extension/background/service_worker.js`.
- `src/framenest/infrastructure/persistence/alembic_environment/` including
  `env.py`, `script.py.mako` and the applied `versions/` set, and the 11 applied
  revisions that import `sqlite_batch_fk`.
- `src/framenest/infrastructure/persistence/catalog_backup.py` around line 312,
  and every backup, sidecar, off-device marker and snapshot writer and reader.
- `deploy/ubuntu/framenest_release.py` and `deploy/ubuntu/framenest-release` in
  full, to establish how the installed environment and unit names are produced.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/00_handout.md`,
  `00_notes.md`, `01_report_00.md` and `02_report_00.md`.

Predecessor residuals are recorded in
`/home/agile/meta/projects/kronika/00/02-kronika-one-product/00_notes.md`.
Read only the residual disposition region; do not read that whole's private
material and do not treat it as authority.

## Communication

Worker prompts, the report and any plan artifact text are professional English.
Do not use Czech or Slovak in repository or report artifacts.

## Orchestrator acceptance note

This plan is `approval-gated`. On acceptance, the Orchestrator will issue one
separate bounded implementation grant per cut, in the order the plan proves
safe. No cut, and especially not the NUC migration cut, inherits authority from
plan acceptance.