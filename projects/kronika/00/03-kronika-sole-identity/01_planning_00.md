# Authoritative Worker prompt — Worker session 01, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`. It is stored under the Meta filename mapping
`<worker-session>_<phase>_<meta-exchange-index>.md` as
`01_planning_00.md`, with report destination `01_report_00.md` in the same
directory. Storage naming is Meta policy and grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Task identity: KSI-PLAN-01 — plan-only — identity-cut sequence for the sole Kronika product identity
Reasoning recommendation: High
Recommended context capacity: approximately 250k tokens
```

Rationale for the reasoning recommendation: the task crosses a live-service
migration boundary, couples seven independently-renameable identity classes,
and must order cuts so the NUC keeps serving after each published step. That is
named architectural-ambiguity risk, which `High` covers. The opening
restoration handout recommended `Extra High`; I am not escalating to it, because
the one genuine cross-cutting contradiction — ADR-0082 versus the Cooperator's
2026-10-02 statement — is a documentation decision reserved to the Orchestrator
and Cooperator, not something this Planner must reason through. If you judge the
missing evidence to be genuinely unresolvable at `High`, stop and say so with the
exact missing evidence rather than silently producing a weaker plan.

You are the first Planner of a new logical whole. This prompt declares native
planning mode `required`; the delivery session must have its client's actual
native planning mode enabled. If it is not enabled at your client boundary, stop
before any work and report the mismatch.

## Implementation-planning contract

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded technical planning of the retirement of the framenest product identity — reconnaissance, impact mapping, interfaces, the ADR/amendment text needed before implementation, the compatibility windows, the per-cut ordering, rollback, and the exact proposed mutation for each cut
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
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

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

Verified read-only by the Orchestrator on 2026-10-02. Re-verify; do not trust it
blindly.

```text
Repository checkout topology: standalone checkout
Expected branch: main
Expected HEAD: 0c850996cd2ef17dae4112733fd17fdc732f4699
Expected subject: chore: remove the implemented awk observation from the active ledger
Remote origin: https://github.com/cisarik/kronika
Public main: 0c850996cd2ef17dae4112733fd17fdc732f4699 (verified by git ls-remote)
Working tree: clean
Containing-repository .ap gitlink: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
Submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS, governing variant stable
ap project check --baseline 0c850996cd2ef17dae4112733fd17fdc732f4699: PASS
ap.project.conf projectId: cisarik/kronika
CPython: 3.13.9   Poetry: 2.3.2   Node: v26.8.2
Working directory: /home/agile/Projects/kronika
```

Host note. The development host is now a CachyOS Linux workstation, not the
MacBook. The historical MacBook path `/Users/agile/Projects/framenest` appears
in older artifacts as historical text; it is not a path on this host. The
canonical checkout here is `/home/agile/Projects/kronika` on `main`. A stale
second clone exists at `/home/agile/Projects/framenest` on branch
`feat/kronika-one-product` at `38e7beeb3921d7c0fd8e717e480754fbd18130c9` with
remote `cisarik/framenest.git`; it is an ancestor of `main`, it is not the work
source, and it contains a `private/` directory you must never read.

### Re-counted identity inventory

This is a re-count performed at the verified baseline, not the predecessor's
§3 lead. Treat it as a starting measurement and refine it.

| Class | Count at `0c850996` |
|---|---|
| `src/framenest` Python modules | 284 files |
| Files containing `framenest` (case-insensitive) | `src` 254, `tests` 314, `deploy` 19, `scripts` 7, `docs` 87, repository `*.md` 100, `extension` 12 |
| `pyproject.toml` project name | `framenest` |
| `framenest-*` console scripts | 14, plus compatibility alias `framenest-chatgpt-page` → `kronika_capture.cli:main` |
| `provenanceModule` in `ap.project.conf` | `framenest` |
| `FRAMENEST_` settings/error prefix | 639 occurrences, 103 distinct names; leading names `FRAMENEST_DATABASE_PATH` 67, `FRAMENEST_PORT` 51, `FRAMENEST_ENV_FILE` 40, `FRAMENEST_HOST` 30, `FRAMENEST_API_KEY` 19, `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` 18 |
| `X-FrameNest-Request` header | 53 occurrences across 27 files, including `src/framenest/adapters/api/web/app.js`, `extension/background/service_worker.js`, `SECURITY.md`, eight ADRs, and ten `tests/*.test.js` files |
| `/opt/framenest` | 198 |
| `/etc/framenest` | 73 |
| `/var/lib/framenest` | 91 |
| `/var/cache/framenest` | 20 |
| `/mnt/framenest-catalog-offdevice` | 12 |
| `User=framenest` / `Group=framenest` | 5 / 5 |
| `deploy/systemd` sources still `framenest` | `framenest.service`, `framenest-catalog-backup.service`/`.timer`, `framenest-catalog-offdevice.service`/`.timer`, `framenest.env.example`, `framenest-ai-credential-nvidia-nim.conf`, `framenest-ai-credential-opencode-go.conf`, `framenest-ai-credential-vercel-ai-gateway.conf`, `framenest-research-credential.conf` |
| `scripts/operator` scripts | `infosec/framenest_log_triage.sh`, `infosec/framenest_public_surface_check.sh`, `infosec/framenest_socket_permissions_check.sh`, `network/framenest_mullvad_egress.fish`, `network/framenest_mullvad_egress.sh`, `network/framenest_nuc_worker_gate.fish` |
| `deploy/ubuntu` operator entry points | `framenest-release`, `framenest_release.py`, `framenest-catalog-export-v1`, `fn-production-env-deploy`, `production_ai_deploy.py` |
| Repository-root fish launcher | `./framenest`, tracked, invoking `.venv/bin/framenest-*` |
| Alembic migrations | 36 files under `src/framenest/infrastructure/persistence/alembic_environment/versions/`, head `0035_research_requests_and_accounting.py` |
| Capitalized prose `FrameNest` | 3335 occurrences in 478 files; heaviest `src/framenest/domain/x_acquisition.py` 73, `SPEC.md` 57, `src/framenest/domain/youtube_acquisition.py` 55, `src/framenest/domain/uploads.py` 49, `PRODUCT.md` 39 |

Installed NUC state, observed read-only on 2026-10-02 and not re-verified by me:
`framenest.service` enabled; `framenest-catalog-backup.service` and `.timer`
enabled; `kronika-capture-bridge`, `-runner` and `-xvfb` enabled;
`kronika-capture-view` and `-vnc` static; the off-device catalog units were not
in the installed list. Web release verified at
`0c850996cd2ef17dae4112733fd17fdc732f4699`, service active, database revision
`0035`, backup ready. Capture release unchanged at
`94e605c17b881461fad3e22fd8c7fca32cb93976`.

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
   error codes, and what is the removal condition for the fallback?
5. How is `X-FrameNest-Request` retired compatibly, given the Brave companion
   extension sends it and ten `tests/*.test.js` files require it? Name the
   Cooperator-visible step of reloading or updating the extension, and the exact
   server-side acceptance window during which both spellings are honoured.
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

## Authority

```text
Positive authority: read-only inspection inside /home/agile/Projects/kronika,
  including .ap at its pinned commit; read-only public verification of
  https://github.com/cisarik/kronika.git and https://github.com/cisarik/ap.git;
  read-only inspection of /home/agile/Projects/framenest for topology facts
  only, excluding private/; Python and test execution through the canonical
  declared AP route only.

Negative authority: any file edit, create, move, rename or deletion in
  /home/agile/Projects/kronika; any write to /home/agile/meta; any Git write of
  any kind — no add, commit, branch, tag, merge, rebase, stash, checkout,
  switch, reset, clean, submodule update or push; any dependency install,
  update or lockfile change; any NUC contact, including SSH, the NUC worker
  gate, and deploy/ubuntu/framenest-release in every mode; any
  deploy/systemd, package-manager, systemd, AppArmor, UFW, Tailscale, mount or
  storage operation; any provider or capture-browser contact; any reading of
  private/, browser profiles, cookies, tokens, credential stores, .secrets, or
  the NUC's installed environment file or secret values; any creation of the
  plan artifact in the repository or in the trace.

Commands: Python evidence and tests go only through the canonical declared
  route, `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  0c850996cd2ef17dae4112733fd17fdc732f4699 --operation <id> -- <argv>`, with
  operations declared in ap.project.conf, and `./.ap/ap project check --root
  /home/agile/Projects/kronika --baseline
  0c850996cd2ef17dae4112733fd17fdc732f4699`. JavaScript tests use the declared
  `node --test` route. Never invoke `.venv/bin/python`, `python`, `python3` or
  `poetry run` for evidence. Read-only Git inspection is allowed
  (`git status`, `git rev-parse`, `git log`, `git show`, `git ls-files`,
  `git grep`, `git ls-remote`, `git submodule status`); no other Git command.

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
Validation: re-verify the repository gate, HEAD, clean tree, submodule
  equality and `ap project check --baseline` before relying on any measurement;
  re-count the identity classes rather than copying my table; read every file
  the plan depends on rather than inferring it; run the project's declared
  Python test operation and JavaScript test route once to establish the
  green baseline at this commit, and record the exact counts.

Evidence tier: E2. This is cross-cutting, reversible-at-plan-stage work with
  user-visible compatibility and moderate uncertainty. The plan must itself
  identify which future cut will need E3 or E4, because the NUC migration cut
  is a live-service and Unix-account migration with durable state and
  availability consequences.
```

## Finishing

```text
Stopping conditions: stop without improvising if the client has no native
  planning mode enabled; if HEAD, the branch, the remote or the tree does not
  match the verified state; if the submodule is not at the pinned commit; if
  `ap project check --baseline` does not pass; if you would need any mutation
  to answer a question; if you find a genuine cross-cutting contradiction that
  needs a Cooperator or Orchestrator decision rather than a plan; if context
  pressure reaches the point where a bounded rotation is cheaper than a
  degraded plan.

Completion: one terminal report containing the full decision-complete plan, not
  a summary of it.

Required report sections: the standard report core and header; the full cut
  sequence with per-cut proposed mutation, evidence and rollback; the ADR text
  or a complete specification of it; the answer to each of the thirteen
  questions above; your own re-counted identity inventory with the delta against
  mine and the reason for it; the E2 baseline test result with exact counts;
  open questions requiring an Orchestrator or Cooperator decision; risks;
  one smallest next step.

Report destination: the terminal report is delivered to the Orchestrator in
  this session. Do not write it to any file. The Orchestrator stores it as
  `01_report_00.md` in the activated trace directory
  `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/`.

Authority expiry: on submission of the terminal planning report, all planning
  authority expires. Implementation in this session is prohibited. A later
  execution authority event is an explicit ORCHESTRATOR prompt with Native
  planning mode: not-used.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. For a plan-only exchange the expected value is
`new-evidence`.

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
  `env.py`, `script.py.mako` and the applied `versions/` set.
- `deploy/ubuntu/framenest_release.py` and `deploy/ubuntu/framenest-release` in
  full, to establish how the installed environment and unit names are produced.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/00_handout.md`
  and `00_notes.md`.

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