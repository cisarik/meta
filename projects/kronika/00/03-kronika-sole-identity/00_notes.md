# Era 00 Whole Notes — Kronika sole identity

Classification: private local historical/evidentiary projection for this
logical whole. Orchestrator-owned, append-only during the whole, frozen at
closure. Non-authorizing. Public-safe by default. Michal owns any meta Git
commit.

Working identity:

```text
kronika-sole-identity
```

Trace:

```text
/Users/agile/meta/projects/kronika/00/03-kronika-sole-identity/
```

Opening handout: `00_handout.md`. No Worker has been dispatched. The next
Worker session ordinal is 01. The first exchange, when issued, is stored as
`01_planning_00.md` with report destination `01_report_00.md`.

Predecessor whole: `kronika-one-product`
(`/Users/agile/meta/projects/kronika/00/02-kronika-one-product/`), closed
2026-10-02. Its closure signal was emitted in the Orchestrator chat. Do not
emit it again. A file `05_handout.md` was briefly written inside that closed
trace and removed the same day; it is not a handout of either whole.

## Objective

Retire the remaining `framenest` product identity so the running product,
its commands, headers, units, and host paths are Kronika. Public repository
rename is already done. This whole does not archive `cisarik/cli_chatgpt`,
does not rewrite Git or Alembic history, and does not restart parked capture
as a side effect.

## Session log

- **2026-10-02 — Whole opened.** Michal required the successor handout to be
  `00_handout.md` under `projects/kronika/00/03-…`, not inside the closed
  whole. Archive sequence stays `00`. Logical-whole sequence is `03`.
  Identity `kronika-sole-identity`. Opening handout and these notes written.
  No product mutation, no NUC mutation, no Worker prompt issued.

- **2026-10-02 — Restoration bootstrap; read-only classification complete.**
  Host changed: the development machine is now a CachyOS Linux workstation, not
  the MacBook. Michal will work on the PC until he explicitly announces a switch
  back. The canonical checkout is `/home/agile/Projects/kronika` on `main` at
  `0c850996cd2ef17dae4112733fd17fdc732f4699`, clean, remote
  `https://github.com/cisarik/kronika`, public `main` equality confirmed by
  `git ls-remote`. `.ap` gitlink and the upstream `cisarik/ap` `main` both at
  `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. `ap.project.conf` `projectId` is
  `cisarik/kronika`. Observed but deliberately not used: a stale second clone
  at `/home/agile/Projects/framenest`, branch `feat/kronika-one-product` at
  `38e7beeb3921d7c0fd8e717e480754fbd18130c9`, remote `cisarik/framenest.git`,
  an ancestor of `main`, containing a `private/` directory that was never read.
  Host differences recorded: `.ap/` submodule was uninitialized and no `.venv`
  existed, so no AP evidence route was usable; `poetry 2.3.2`, CPython `3.13.9`,
  Node `v26.8.2` present, against NUC Poetry `2.4.1` and CPython `3.13.14`.

- **2026-10-02 — Bounded Cooperator grant received and discharged.** Michal
  authorized a local workstation bootstrap only: initialize the `.ap` submodule
  at the pinned commit, create the canonical `.venv`, then run
  `./.ap/ap project check`. No product edit, no commit, no push, no NUC contact.
  Executed exactly that. `.ap` checked out at the pin; `poetry install` with
  `POETRY_VIRTUALENVS_IN_PROJECT=true` created `.venv`; `./.ap/ap doctor` PASS
  with governing variant `stable`; `./.ap/ap project check --root
  /home/agile/Projects/kronika --baseline 0c850996…` PASS. `HEAD` unchanged and
  tree still clean; `.venv` is already gitignored. `SSH_AUTH_SOCK`,
  `VIRTUAL_ENV_DISABLE_PROMPT` and `PATH` were reported as sanitized inherited
  environment classes, which is expected ambient-shell state, not a defect.

- **2026-10-02 — Identity inventory re-counted; predecessor §3 materially
  understated.** At `0c850996`: `src/framenest` holds 284 Python modules;
  `pyproject.toml` carries project name `framenest`, 14 `framenest-*` console
  scripts and the `framenest-chatgpt-page` alias; `provenanceModule` is
  `framenest`; `FRAMENEST_` accounts for 639 occurrences across 103 distinct
  names; `X-FrameNest-Request` appears 53 times in 27 files including the Brave
  companion extension and ten `tests/*.test.js` files; host paths
  `/opt/framenest` 198, `/etc/framenest` 73, `/var/lib/framenest` 91,
  `/var/cache/framenest` 20, `/mnt/framenest-catalog-offdevice` 12,
  `User=/Group=framenest` 5 and 5; capitalized prose `FrameNest` 3335
  occurrences in 478 files; 36 Alembic migrations with head `0035`. Two
  couplings the predecessor list did not name and that materially shape the
  cut: the request header is a wire contract shared with the companion
  extension Michal runs in Brave, and `ap.project.conf` is part of the AP
  baseline contract, so changing `provenanceModule` changes the trusted
  baseline. Recorded as Orchestrator classification, not as authorization.

- **2026-10-02 — Planner prompt issued and stored, delivery route open.**
  Worker session `01`, exchange `01`, profile Planner, `fresh-worker-session`,
  `Native planning mode: required`, plan-only, `approval-gated`, one cycle.
  Stored as `01_planning_00.md`; report destination `01_report_00.md`. The
  prompt sets read-only authority only and asks thirteen explicit questions,
  including the ADR that must precede implementation and the exact per-cut
  proposed mutation with rollback. Reasoning recommended at `High`, deliberately
  not escalated to the handout's `Extra High`, because the one genuine
  cross-cutting contradiction — ADR-0082 versus the Cooperator's 2026-10-02
  statement — is an Orchestrator and Cooperator documentation decision, not
  Planner reasoning. Open risk: this Orchestrator client exposes no native
  planning mode, and AP grants no prompt-level read-only substitute for the
  first Planner of a new whole, so the delivery route needs an explicit
  Cooperator decision before dispatch.

- **2026-10-02 — Native planning mode exists on this client; its read-only
  guarantee is not enforced.** `opencode 1.18.34` exposes a built-in `plan`
  primary agent, `opencode debug agent plan` reports the description "Plan mode.
  Disallows all edit tools", with `read` allowed, `question` denied,
  `plan_enter`/`plan_exit` denied, and the native plan write targets
  `~/.local/share/opencode/plans/*` and `.opencode/plans/*.md`. That resolved
  the AP precondition for a first Planner on this host without any protocol
  deviation. However, the same resolved permission list ends with an
  `allow edit *` entry that overrides the earlier `deny edit *`, which comes
  from Michal's global `~/.config/opencode` permissions rather than from this
  project. Recorded as a real finding: on this machine native plan mode does
  not hard-enforce read-only at the client boundary, so the actual guarantee
  rests on the issued prompt's negative authority plus Orchestrator
  re-verification of the tree after the exchange. Tightening that global
  permission is Michal's own configuration decision and is deliberately not
  folded into this whole.

- **2026-10-02 — Delivery route selected: Cooperator manual.** Michal chose
  manual delivery over Orchestrator dispatch. He runs the Planner himself in
  `/home/agile/Projects/kronika` with the `plan` agent and attaches
  `01_planning_00.md`; the terminal report returns to the Orchestrator and is
  stored as `01_report_00.md`. Recorded as a material departure from the Agent
  Orchestrator default dispatch route, with the Cooperator's reason being
  direct visibility and interruption control over the first Planner. No product
  or host mutation occurred while selecting it.

- **2026-10-02 — Worker session 01, exchange 01 returned BLOCKED; routing
  deviation recorded.** The Cooperator delivered the exchange manually but not
  into the client named in the delivery decision: he ran Codex rather than the
  opencode `plan` agent, and selected model "GPT-6 Astra" at Extra High where the
  issued prompt recommended High. AP leaves final reasoning selection with the
  Cooperator, so the escalation itself is lawful; the client substitution is
  recorded as an unverified claim. `Native planning mode: required` was asserted
  active by the Worker and cannot be verified from the Orchestrator side in that
  client. The exact model identity is a Cooperator claim I cannot confirm and do
  not assert. Report stored as `01_report_00.md`.

- **2026-10-02 — Orchestrator verification of the blocker: cause is now MEASURED,
  not a lead.** Independently reproduced through the canonical route:
  `3 failed, 1 passed, 4148 deselected`, same signature `assert 0 == 2` at
  `tests/contract/test_operator_network_scripts.py:870`, with
  `[command]` the only passing case. Cause: `scripts/operator/network/
  framenest_nuc_worker_gate.fish` lines 254-257 seed target, user and identity
  from `$FRAMENEST_NUC_SSH_TARGET`, `$FRAMENEST_NUC_SSH_USER` and
  `$FRAMENEST_NUC_SSH_IDENTITY` before applying CLI flags. This CachyOS host
  carries exactly those three names as **exported fish universal variables** in
  `~/.config/fish/fish_variables`; `FRAMENEST_NUC_SSH_COMMAND` is deliberately
  absent. The harness `_run_fish` strips the four names from the child process
  environment but spawns `/usr/bin/fish` without disabling startup
  configuration, so fish restores the three exported universal variables before
  the gate reads them. Omitting `--command` still fails because nothing supplies
  it, which is precisely why `[command]` passes. Verified without reading or
  printing any personal value: only variable names were extracted, and
  `fish --no-config` was confirmed to suppress all four.

  Orchestrator classification: this is a **host-ambient precondition failure on
  the new development host, not a repository defect and not a predecessor
  regression**. The gate behaves as designed; the harness at
  `tests/contract/test_operator_network_scripts.py:423-444` is not hermetic,
  because it asserts gate behaviour that depends on the developer's personal
  exported universal variables. The MacBook did not carry those variables, which
  is why the suite was green there. Repository state confirmed untouched after
  the exchange: `git status` clean, `HEAD` `0c850996…`, submodule at
  `73e20ef8…`, no stash, reflog showing only the original clone.

- **2026-10-02 — Worker's inventory corrections accepted; my issued table was
  wrong on four counts.** Independently re-measured and confirmed: console script
  entries are **14 total = 13 application commands plus the capture alias**, so my
  table double-counted the alias; `X-FrameNest-Request` occurs 53 times in
  **28** files, not 27; **9** `tests/*.test.js` files, not 10; **5** ADR files,
  not 8. All other classes matched exactly, including 284 Python modules, 639
  `FRAMENEST_` tokens over 103 names, the five host-path counts, and 3335
  capitalized prose occurrences in 478 files. The Orchestrator issued table is
  corrected by the Worker measurement.

- **2026-10-02 — Worker's material findings verified against the baseline.**
  All eight spot-checked and confirmed: **11** applied Alembic revisions import
  `framenest.infrastructure.persistence.sqlite_batch_fk`, so moving the
  environment directory breaks applied history loading unless import support is
  preserved; capture units and the release helper hardcode
  `/opt/framenest/capture-current` and `/opt/framenest/releases` at
  `deploy/ubuntu/framenest_release.py:37,39` and
  `deploy/systemd/kronika-capture-bridge.service:11,14` and
  `kronika-capture-runner.service:11,18`, so the web path migration is coupled to
  capture; backup verification hardcodes `application.name == "framenest"` at
  `src/framenest/infrastructure/persistence/catalog_backup.py:312`; and the ADR
  index ends at `0084`, making `0085` the next free number. Recorded as
  reconnaissance, not as approved design.

- **2026-10-02 — Orchestrator consequence recorded for sequencing.** Because the
  operator-gate contract test is host-sensitive and the identity cut will rename
  `framenest_nuc_worker_gate.fish`, a non-hermetic harness would let the renamed
  gate fail on this PC and on the NUC for an ambient reason and be misread as a
  rename regression. A hermetic harness therefore has sequencing value ahead of
  the unit-and-script rename cut, and must be its own bounded slice rather than
  folded into the rename. No authority is granted by this observation.

- **2026-10-02 — Worker session 02, exchange 01 issued as a bounded correction
  slice.** The Cooperator authorized a separate, minimal grant rather than
  planning against a non-green baseline. Grant `02_correction_00.md` changes
  only `_run_fish` in `tests/contract/test_operator_network_scripts.py` so the
  spawned Fish loads no personal startup configuration, verified mechanism
  `fish --no-config` placed before the script path; one optional focused
  assertion is permitted with justification. It authorizes exactly one local
  branch `fix/operator-gate-test-hermetic` and exactly one local commit, with no
  push and no publication. Reasoning recommended at `Low`: one known function,
  exact verified mechanism, existing failing test, trivial rollback. Evidence tier
  E1. The grant requires reproducing `3 failed, 1 passed` before editing and
  refusing to change a test whose failure could not be reproduced. Worker session
  `01` remains `BLOCKED`; its planning authority expired and planning does not
  resume under this prompt. No roadmap or ADR documentation authority is granted,
  and the slice must not be folded into any rename cut.

- **2026-10-02 — Correction slice executed in the repository; Worker session 02
  report was NOT delivered and the trace file is a duplicate.** The delivered
  `02_report_00.md` is byte-identical to `01_report_00.md`, same MD5
  `91fc0a97f77da736304aa2ce220e64fc`. It declares Worker session ordinal `01`,
  Worker exchange ordinal `01` and task identity `KSI-PLAN-01`, so it is the
  session 01 BLOCKED report duplicated, not a session 02 report. Recorded as a
  trace defect, not reconciled silently: the Meta storage contract requires one
  prompt and one matching report per exchange, and a historical mismatch needs
  explicit prospective reconciliation. The Orchestrator did **not** reconstruct
  a session 02 report. The slice outcome is instead evidenced by repository
  artifacts plus independent Orchestrator verification below.

  Repository state observed read-only: branch `fix/operator-gate-test-hermetic`,
  HEAD `ca649f6eb6231591292e174dff994fd0f4448378`, exactly one commit above
  `0c850996`, clean working tree, submodule at the pin, and the branch absent
  from `origin`, so the no-push boundary held. Diff is one file,
  `tests/contract/test_operator_network_scripts.py`, +22/-1, and is entirely
  inside the granted envelope: `[fish, "--no-config", str(script), *args]` in
  `_run_fish`, plus one new synthetic test
  `test_run_fish_ignores_injected_startup_configuration` that plants a marker
  `config.fish` under a `tmp_path` `XDG_CONFIG_HOME` and asserts the marker never
  appears. That construction is stronger than the optional assertion proposed in
  the grant, because it guards the mechanism on any host rather than only on a
  host that carries exported universal variables. It reads no personal
  configuration.

  Independent Orchestrator verification, canonical route only: affected module
  `62 passed`; full Python suite `4145 passed, 8 skipped, 3 warnings`, exit 0;
  JavaScript `554 tests, 549 passed, 0 failed, 5 skipped`, identical to the
  measured baseline; `ap project check --baseline ca649f6` PASS. The Python delta
  is fully explained: `4141 passed + 3 repaired + 1 new = 4145`, with the same 8
  skips and same 3 warnings, so there is no new skip and no new warning. The
  correction slice is accepted on independent evidence. Routing deviation
  repeats: the exchange was again delivered and run by the Cooperator in Codex,
  not in the client named in the delivery decision.

- **2026-10-02 — Trace defect reconciled; session 02 report accepted.** The
  Cooperator replaced the duplicated `02_report_00.md` with the real Worker
  report, MD5 `883f6975fb8b2480643a3dfeb428c4d6`, coordinates
  `kronika-sole-identity` / session `02` / exchange `01` / `KSI-CORR-01`,
  `status: PASS`, start `0c850996`, end `ca649f6`. It matches the Orchestrator's
  independent verification on every material point. Two evidence-integrity
  observations recorded rather than resolved: the commit message carries an
  environment-added trailer `Co-authored-by: Cursor <cursoragent@cursor.com>`,
  which contradicts the Cooperator's statement that the exchange ran in Codex;
  and the Worker disclosed running one temporary-directory Fish probe outside
  the declared routes, because my grant named routes for Python and JavaScript
  evidence but did not explicitly govern a direct `fish` invocation. Both are
  Orchestrator grant-precision and route-record defects, not boundary
  violations, and the Worker concealed neither.

- **2026-10-02 — New test independently confirmed to have teeth.** Using a
  throwaway `XDG_CONFIG_HOME` under `/tmp/opencode` and no repository mutation:
  without `--no-config` the planted marker reaches stdout, with `--no-config` it
  does not. The committed assertion therefore fails if the isolation is removed,
  on any host, which is exactly the property the MacBook baseline could not
  provide. Session 02 is accepted; the correction slice is complete, in-bounds
  and evidenced.

- **2026-10-02 — Open Orchestrator decision before planning resumes.** The
  correction exists only as an unpublished local branch
  `fix/operator-gate-test-hermetic` at `ca649f6`; `main` and public `main`
  remain `0c850996`. Planning resumption needs an explicit baseline, and
  publication needs its own bounded authority, so the baseline choice is the
  Cooperator's. Recorded as the single open decision; no planning grant is
  issued until it is answered.

- **2026-10-02 — Cooperator authorized publication; correction is on public
  `main`.** Grant executed exactly: verified remote `main` was still
  `0c850996…` and that `ca649f6…` is a descendant, so a fast-forward was safe;
  switched to `main`, `git merge --ff-only fix/operator-gate-test-hermetic`;
  pushed the branch and then `main`. No force, no tag, no merge commit, no
  history rewrite. Public readback: `refs/heads/main` and
  `refs/heads/fix/operator-gate-test-hermetic` both
  `ca649f6eb6231591292e174dff994fd0f4448378`; local `main`, `HEAD` and
  `origin/main` all equal; tree clean; submodule at
  `73e20ef80b88700d5fcbc397cd8edd4fc425869f`; `ap doctor` PASS. The correction
  therefore remains an independently auditable slice that is not folded into
  the rename.

- **2026-10-02 — Planning resumption routing decision recorded.** The initial
  Planner in session `01` returned `BLOCKED` before producing any plan, so the
  whole's one initial plan-only cycle has not yet yielded a plan and no
  automatic targeted revision has been used. Resumption is routed to
  `fresh-worker-session`, session ordinal `03`, exchange `01`, not to
  `current-worker-session`, because the delivery client has changed across
  exchanges and a current-session claim would be unverifiable at the client
  boundary. Nothing is lost by that choice: `01_report_00.md` is a trace-stored
  Orchestrator-verified artifact, and its eight material findings were each
  independently confirmed by the Orchestrator, so they are carried forward as
  verified input rather than as a Worker's retained private context. New
  planning baseline is public `main` at `ca649f6eb6231591292e174dff994fd0f4448378`,
  where the Python suite is `4145 passed, 8 skipped, 3 warnings` and the
  JavaScript route is `549 passed, 0 failed, 5 skipped`.

- **2026-10-02 — Worker session 03 returned a decision-complete plan, `PASS`.**
  Stored as `03_report_00.md`, MD5 `2e45b6d550e10d904c6a314dcd3f71ec`,
  coordinates `kronika-sole-identity` / session `03` / exchange `01` /
  `KSI-PLAN-02`, start and end commit both `ca649f6`, changed files none.
  Repository confirmed untouched afterwards: `main` at `ca649f6`, clean tree,
  submodule at the pin, reflog showing only the Orchestrator's own authorized
  publication steps. The plan is ADR-0085 plus a ten-cut sequence C0 through C9,
  where only C6 changes the web host and only C8 restarts capture. One artifact
  deviation recorded rather than rejected: the client's native planning surface
  forces a YAML frontmatter block and a level-1 title above the standard report
  header, which the Worker disclosed on its first line. AP requires a report to
  begin exactly with the header, so this is a client-imposed deviation, not a
  concealed one.

- **2026-10-02 — Orchestrator verification of the plan's load-bearing technical
  claims.** Confirmed independently, read-only: `FRAMENEST_[A-Z0-9_]+` yields
  exactly `637` tokens over `102` distinct names and there are exactly `2` bare
  `FRAMENEST_` spellings, so the issued `639`/`103` reconciles precisely and the
  Worker's explanation is correct; `relocate_venv_shebangs` does require
  `framenest-db` and `framenest-backup` at
  `deploy/ubuntu/framenest_release.py:924`; routine `deploy` restarts only
  `SERVICE` at line 379 and installs no unit file, renames no account and moves
  no `/opt` tree, so the plan's standing rule is accurate; `PROTOCOL_MAGIC` is
  `b"FNCBE01\0"`; `DEVELOPMENT_DATABASE_DIRECTORY` is `"framenest-development"`;
  the mutation header is consumed in
  `src/framenest/adapters/api/tailscale_ingress.py`; `SIDECAR_FORMAT` is
  `"framenest-media-sidecar"` and `SIDECAR_FILENAME_SUFFIX` is
  `".framenest.json"`; the extension keys `frameNestOrigin`,
  `framenest.companion.v1`, `framenest.youtube.currentClaim.v1` and
  `framenest.catalog.pageSize` all exist; `docs/FEDORA_SERVICE.md` exists; the
  Tailscale Serve handler `/run/framenest/framenest.sock` and
  `tailscale serve status --json` match `docs/UBUNTU_NUC_DEPLOYMENT.md`; and the
  ADR-0082 citations at lines 87-89, 196 and 208-209 are verbatim accurate.

  The single most important claim also verified: **exactly 11** applied revision
  files import `framenest.infrastructure.persistence.sqlite_batch_fk`, and no
  applied revision imports any other `framenest` name, so the plan's in-memory
  `sys.modules` alias is exactly sufficient and not merely plausible. The
  `ap project check --candidate` output is verbatim
  `ap project check --candidate: PASS (non-authorizing)`, as cited. The plan's
  two alias anchors are correct: `load_script_directory` at
  `src/framenest/infrastructure/persistence/migrations.py:116` and
  `alembic_environment/env.py`. The plan implies the former sits in the
  `alembic_environment` directory; it does not. Minor imprecision, no design
  consequence.

- **2026-10-02 — Four substantive review findings against an otherwise
  decision-complete plan.** Recorded as Orchestrator findings that must be
  carried into the later grants, because the plan is frozen as an artifact.

  1. **C7's removal list is incomplete.** Ten tracked paths carrying
     `framenest` in the filename are named by no cut:
     `deploy/systemd/framenest.env.example`, the three
     `deploy/systemd/framenest-ai-credential-*.conf` files,
     `deploy/systemd/framenest-research-credential.conf`,
     `deploy/ubuntu/framenest-catalog-export-v1`,
     `deploy/systemd/framenest-catalog-offdevice.service` and `.timer`, and
     `scripts/operator/infosec/framenest_log_triage.sh`,
     `framenest_public_surface_check.sh`,
     `framenest_socket_permissions_check.sh`, plus
     `scripts/operator/network/framenest_mullvad_egress.fish` and `.sh`.
  2. **The question-12 frozen/living split does not cover the trees where the
     rename is mechanical.** Its living list is thirteen Markdown files; it
     excludes `deploy/`, `scripts/`, `src/`, `tests/` and `extension/`, so a
     path-name miss in exactly those trees cannot be caught by the retention
     test. At least six test modules assert the old script names, unit names or
     host paths, including
     `tests/contract/test_fedora_systemd_service.py` lines 11, 12, 26, 94 and
     157-162, which hardcode `deploy/systemd/framenest.service`,
     `framenest.env.example`, `/opt/framenest/current`,
     `/etc/framenest/framenest.env` and `FRAMENEST_*` values.
  3. **The question-14 Cooperator command block is labelled
     `# [MacBook / fish]`, but the Cooperator is on a CachyOS Linux host with
     fish 4.9.3.** Run as labelled it would set the universal variables on the
     wrong machine and the C7 removal would then be validated against the wrong
     host. The block must be relabelled for the current host before it reaches
     the Cooperator.
  4. **`deploy/ubuntu/fn-production-env-deploy` contains a `framenest`
     reference** despite its name not matching a `framenest` filename search, so
     a filename-driven enumeration alone is not sufficient for that tree.

- **2026-10-02 — Plan accepted; fifth review finding recorded.** The plan is
  accepted as decision-complete, with findings 1 through 4 carried as mandatory
  content of the C0 and C7 grants rather than as plan rewrites, because the plan
  is frozen as an artifact and these are additive clarifications, not
  contradictions.

  Finding 5 concerns scope discipline in C0. The plan's "living-prohibition
  edits" list names seven files, but exactly **five** present-tense sentences in
  **four** files currently forbid the rename, and each was read verbatim:
  `AGENTS.md:21-22` "Do not perform a mass branding replacement.";
  `AGENTS.md:24-25` "The internal `framenest` package, migration history,
  compatible HTTP headers and deployment identifiers remain.";
  `SPEC.md:32-34` the same clause with "MUST remain during this stage";
  `DEVELOPMENT.md:39-40` "The internal `framenest` application, headers and
  migration history remain."; and `ROADMAP.md:78-79` "The existing release helper
  remains the only deployment system; no mass `framenest` rename is part of the
  transition." `README.md`, `PRODUCT.md` and `SERVER.md` contain **no** such
  prohibition; their `framenest` occurrences are descriptive living prose about
  commands, paths and configuration names, or historical narrative, which belong
  to the later cuts under the question-12 denylist. Including those three files
  in C0 would drag later-cut work into the ADR commit and would make C0 neither
  reviewable nor cleanly revertible. C0 is therefore scoped to exactly those five
  sentences in four files. Note also that `AGENTS.md:33-51` is the AP-managed
  integration block and must not be edited by any cut.

- **2026-10-02 — Worker session 04 returned `PASS`; cut C0 executed in-bounds.**
  Stored as `04_report_00.md`, coordinates `kronika-sole-identity` / session `04`
  / exchange `01` / `KSI-IMPL-C0`, branch `docs/adr-0085-kronika-sole-identity`,
  one commit `18c357cf6f8c5ff9cc3b2c28e638510fc73a3672` over parent `ca649f6`,
  not pushed. Orchestrator verification, all read-only: `git diff --stat`
  reports exactly the seven authorized paths and **empty output** for ADR-0082,
  ADR-0083, ADR-0084, `README.md`, `PRODUCT.md`, `SERVER.md`, `SECURITY.md`,
  `docs/FEDORA_SERVICE.md`, `src/`, `deploy/`, `scripts/`, `extension/`,
  `pyproject.toml` and `ap.project.conf`; the AGENTS.md managed AP block is
  byte-identical by SHA-256 of its marker-extracted content, with only its line
  offset moving from 33-51 to 34-52; the new retention test passes `14 passed`
  through the canonical route; the full Python suite is
  `4159 passed, 8 skipped, 3 warnings, 0 failed` against a baseline of `4145`, a
  delta of exactly the 14 new tests; the JavaScript route is unchanged at
  `549 passed, 0 failed, 5 skipped`; `ap project check --baseline 18c357c` PASS.
  The five prohibition sentences were replaced in exactly the four authorized
  files, each neighbouring constraint preserved, and ADR-0085 cites the three
  ADR-0082 passages verbatim at the correct line numbers.

- **2026-10-02 — Orchestrator's own Part B figure was wrong; the Worker found
  it and did not absorb it.** My C0 grant stated "The Orchestrator-measured set,
  23 paths", then enumerated 20, then asserted that ten more lived under
  `src/framenest/`. That prose was internally inconsistent. The Worker measured
  the strict definition from `git ls-files` and found the true set is exactly
  **20**, because **zero** files under `src/framenest/` carry `framenest` in
  their own basename: it is one directory that moves as a unit in C3, not a set
  of filenames. The Orchestrator independently re-measured 20 and accepts the
  correction. Recorded because the cause was Orchestrator drafting, not Worker
  error, and because a Worker following "23" literally would have had to invent
  three paths or stop spuriously.

- **2026-10-02 — Ledger pins independently reproduced; self-exclusion confirmed
  necessary and correctly disclosed.** The retention test excludes itself from
  Part C counting through `_SELF_RELATIVE_PATH`. That exclusion is load-bearing,
  because the ledger file necessarily contains the literals it pins. Verified by
  measuring the committed tree with and without it: raw `git grep` at `18c357c`
  gives `/opt/framenest` 201, `/mnt/framenest-catalog-offdevice` 14 and 647
  `FRAMENEST_` tokens; excluding the ledger file gives exactly the pinned
  **200**, **13**, **637** tokens, **102** distinct and **2** bare. ADR-0085
  itself contributes zero `FRAMENEST_` tokens and 13 lowercase `framenest`
  occurrences as cited historical text, exactly as anticipated. Frozen-blob
  arithmetic verified: 84 ADR bodies `0001`-`0084` plus `docs/FEDORA_SERVICE.md`
  and `docs/NUC_HOST_BASELINE.md` plus 36 Alembic version files equals the 122
  pinned blobs, and the Alembic set is keyed by filename with a globbed versions
  directory so C3 can move the path without breaking the byte pins.

- **2026-10-02 — Orchestrator finding on finding 4's ledger design.** The Worker
  measured that its first Part C implementation, using only per-tree **file**
  counts as my table specified, did **not** detect a content-only change in
  `deploy/ubuntu/fn-production-env-deploy`: that file already contains
  `framenest`, so its file count was already 1 and a content edit was invisible
  to it. It added per-tree **occurrence** counts, which do detect it, and
  re-verified. My table was therefore insufficient for the exact failure mode I
  created finding 4 to catch. The Orchestrator accepts that correction and records
  that the content ledger, not the file ledger, is what carries finding 4.

- **2026-10-02 — C0 published to `main`; repository gate for C1 recorded.**
  Grant executed exactly: verified remote `main` was `ca649f6…` and that
  `18c357c…` is a descendant, `git switch main`, `git merge --ff-only
  docs/adr-0085-kronika-sole-identity`, push branch then push `main`, both
  non-force. Public readback: `refs/heads/main` and
  `refs/heads/docs/adr-0085-kronika-sole-identity` both
  `18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`; local `main`, `HEAD` and
  `origin/main` equal; tree clean. ADR-0085 is therefore public authority and the
  five living-prohibition sentences are corrected in normative text. The NUC was
  **not** refreshed: C0 is behaviour-neutral and the accepted plan marks it
  routine-deployable but not required.

- **2026-10-02 — C1 gate measurements taken before drafting its grant.**
  `src/framenest/configuration.py:26` defines
  `ENV_FILE_ENVIRONMENT_VARIABLE = "FRAMENEST_ENV_FILE"`, consumed at line 544
  inside the settings loader, whose docstring states that process environment
  variables always override environment-file values.
  `FrameNestSettings.model_config` at lines 141-146 is
  `SettingsConfigDict(env_prefix="FRAMENEST_", env_file_encoding="utf-8",
  hide_input_in_errors=True, extra="ignore")` with **no** `env_file` key; the
  env file is passed per construction as `FrameNestSettings(_env_file=...)`.
  `src/framenest/adapters/api/tailscale_ingress.py:80` defines
  `HEADER_MUTATION = b"x-framenest-request"`, consumed only at line 858 via
  `_single_value(...) != EXPECTED_MUTATION_HEADER_VALUE`, answering `403` with
  code `ERROR_MUTATION_HEADER_REQUIRED`. The header gate is therefore a single
  equality comparison against one expected value, and adding a second accepted
  spelling widens a mutation-authorization boundary, which is why the C1 grant
  selects the `High` reasoning profile on a named security risk. Direct
  `FRAMENEST_` readers named by the plan and their current counts:
  `catalog_backup_ops.py` 5, `catalog_backup_offdevice.py` 1,
  `runtime/development.py` 9, `infrastructure/ai/configuration.py` 1,
  `deploy/ubuntu/production_ai_deploy.py` 1, plus
  `deploy/ubuntu/framenest_release.py:48,406,423,433` for `ENV_FILE` and the
  injected `env FRAMENEST_ENV_FILE=`. C1 does **not** change
  `ap.project.conf`, so the AP baseline contract does not drift in this cut and
  the C3 re-gate is not triggered here.

- **2026-10-02 — Worker session 05 returned `PASS`; cut C1 executed in-bounds.**
  Stored as `05_report_00.md`, MD5 `b85baa85a2f18e12192238c68461e823`,
  coordinates `kronika-sole-identity` / session `05` / exchange `01` /
  `KSI-IMPL-C1`, branch `feat/kronika-identity-dual-read`, one commit
  `90c93eac94171182039a76fbb1c956e42b44da2c` over parent `18c357c`, 21 files,
  `+2562 / −78`, not pushed. Orchestrator verification, all read-only: `git diff`
  empty for `ap.project.conf`, `pyproject.toml`, `.gitmodules`, `.gitignore`,
  `deploy/systemd/**`, `src/kronika_capture/**`, the 36 applied Alembic revision
  files, `docs/**` and every root Markdown file; the seven new test files pass
  `129 passed` through the canonical route; full Python suite
  `4274 passed, 8 skipped, 3 warnings, 0 failed` against a baseline of `4159`, a
  delta of exactly the 115 new tests; JavaScript unchanged at
  `549 passed, 0 failed, 5 skipped`; `ap project check --baseline 90c93ea` PASS;
  tree clean.

- **2026-10-02 — The C1 writer-invariance invariant is verified, not asserted.**
  The accepted plan's organising rule for C1 was "readers learn the new spelling,
  writers do not". Orchestrator verification: the complete set of `KRONIKA_`
  occurrences C1 added anywhere outside tests is **three code tokens**, being
  `IDENTITY_ENVIRONMENT_PREFIX = "KRONIKA_"` twice and
  `PRIMARY_ENVIRONMENT_PREFIX = "KRONIKA_"` once, plus five documentation lines.
  All three are read-side prefix constants: one in `src/framenest/identity_env.py`
  and the two stdlib-only deploy-engine mirrors. **No newly written durable
  artifact, error code, or sent header uses a `KRONIKA_` spelling.** Separately
  confirmed that `KRONIKA_RESEARCH_OPENAI_API_KEY` in
  `infrastructure/ai/research_configuration.py` and in
  `deploy/systemd/framenest-research-credential.conf` was already present at
  `18c357c`, so C1 did not introduce it.

  The header gate was read line by line. `_mutation_header_authorized` iterates
  both spellings, returns `False` immediately when any present spelling does not
  equal `EXPECTED_MUTATION_HEADER_VALUE`, and otherwise returns the `present`
  flag, so an absent header still never authorizes and both-present-with-one-wrong
  is rejected. `403` and `ERROR_MUTATION_HEADER_REQUIRED` are unchanged, the
  reworded message adds no header-derived value, and a comment records that the
  second spelling is a mutation gate and not an origin, CORS or companion-origin
  credential.

  The resolver `src/framenest/identity_env.py` implements the required five-row
  table exactly, treats an empty string as unset, raises before returning either
  value, and its exception carries the suffix only. Its message names the two
  variable names and nothing about their values, lengths, hashes or reprs.

- **2026-10-02 — Three Worker deviations accepted with one follow-up recorded.**
  1. **Exit-status uniformity is incomplete.** The accepted plan required exit 2
     for CLIs on a conflict. It is proven for the two deploy engines inside the
     authorized surface: `production_ai_deploy.py` declares its own
     `IDENTITY_ENVIRONMENT_CONFLICT_EXIT = 2` and returns it, because a
     stdlib-only mirror cannot import the constant. For `framenest-db`,
     `framenest-ai`, `framenest-youtube`, `framenest-production` and the server,
     Orchestrator verified that `infrastructure/persistence/cli.py` does not
     import the resolver at all, so a conflict there surfaces through the
     existing `FrameNestConfigurationError` path with that command's existing
     sanitized exit status of 1 or 6. Fail-closed holds: sanitized error, no
     traceback, no value disclosure. The Worker correctly declined to edit five
     modules outside its authorized surface and reported the gap instead. Note
     also that `EXIT_IDENTITY_ENVIRONMENT_CONFLICT` in `identity_env.py` is
     currently **defined but never consumed**, a small dead-constant wart.
     Recorded as a bounded follow-up, not as a blocker.
  2. **Two stdlib-only resolver mirrors.** Real duplication of a fail-closed
     resolver across three copies. Both mirrors are asserted to expose the same
     prefix pair and rule. C7 should delete all three together, as the Worker
     proposed.
  3. **`env_prefix` was retained rather than replaced**, the one structural
     deviation from the Orchestrator's instruction, and it is correct. Setting
     `env_prefix=""` would make the library produce bare field names, so an
     ambient `PORT`, `HOST` or `HOSTNAME` in the process environment would
     silently become application configuration. Retaining `FRAMENEST_` as the
     *internal* key spelling keeps the accepted name set unchanged.
     `test_bare_unprefixed_process_variables_are_not_read` proves no widening.
     This hazard was introduced by the Orchestrator's instruction and was caught
     by the Worker.

  The Worker also measured that composing the prefix from a constant in the two
  deploy engines makes `FRAMENEST_PRODUCTION_SSH_TARGET` no longer greppable
  verbatim anywhere, which is why the ledger's distinct-name count fell 102 to
  101 and the `deploy` occurrence count fell 218 to 212. It proposed restoring
  grep-ability by declaring accepted names as an explicit tuple per engine. That
  is C7 work and is recorded, not actioned.

  The Worker disclosed two self-inflicted contaminated long runs, discarded them
  rather than reporting them as evidence, and reproduced the clean baseline from a
  pristine worktree with the implementation removed. That is the correct response
  to contaminating one's own evidence.

- **2026-10-02 — Worker session 06 returned `PASS`; correction C1b executed
  in-bounds and fixed a real crash path.** Stored as `06_report_00.md`,
  coordinates `kronika-sole-identity` / session `06` / exchange `01` /
  `KSI-CORR-02`, one additional commit `c02c6753694d5d4958045bb79f80b5eb94b9c75c`
  on `feat/kronika-identity-dual-read` over parent `90c93ea`, 19 files,
  `+667 / −48`, no push, no new branch. Orchestrator verification: `git diff`
  empty for `ap.project.conf`, `pyproject.toml`, `deploy/**`,
  `deploy/systemd/**`, `docs/**`, every root Markdown file,
  `src/kronika_capture/**`, the 36 applied Alembic revision files, **and
  `src/framenest/adapters/api/tailscale_ingress.py`**, so the mutation gate was
  not touched. `EXIT_IDENTITY_ENVIRONMENT_CONFLICT` is now consumed at exactly one
  place, `identity_env.py:64`, through the new
  `IdentityEnvironmentConflictFailure.exit_status` mixin, so it is no longer dead
  and no entry point repeats the literal. Retention test passes unchanged.
  Contract tests `89 passed`; full Python suite
  `4314 passed, 8 skipped, 3 warnings, 0 failed` against `4274`, a delta of exactly
  the 40 new tests.

  **The real defect found.** C1 routed `FRAMENEST_AI_CONFIG_PATH` through the
  resolver, but `adapters/cli/ai.py` computed
  `config_path = args.config_path or default_ai_config_path()` **outside** its
  `try` block. A conflicting prefix pair therefore raised
  `IdentityEnvironmentConflictError` with no handler in scope, and
  `framenest-ai` printed an uncaught traceback. C1b moved the two lines inside
  the existing `try` and translated the conflict in `_resolve`. This was a crash
  introduced by C1 and caught only because the entry-point enumeration was
  required rather than assumed. Orchestrator verified the diff directly.

  **Scope was wider than the Orchestrator's own lead.** The prompt listed eleven
  modules; the true reachable set is **thirteen surfaces across twelve
  commands**, because `catalog_backup_ops.load_catalog_backup_ops_config` and
  `catalog_backup_offdevice.parse_configured_destination_id` also reach
  `framenest-backup`, and `default_ai_config_path` ran outside
  `framenest-ai`'s guarded block. `framenest-recovery` and both
  `kronika-capture` scripts were proved inert rather than skipped, the capture
  scripts by static scan only, because executing them would drive a browser. A
  test now fails if any declared console script is unclassified.

  Orchestrator read the clause-placement diffs to confirm the
  no-other-status-changed claim. It holds structurally: in `youtube.py` the new
  clause precedes `except FrameNestConfigurationError`, which is required because
  the new type is a **subclass** of it and Python matches the first clause; in
  `server.py` the existing handler is kept and an `isinstance` test selects the
  status; in `sidecar.py` a bare `except IdentityEnvironmentConfigurationError:
  raise` precedes the blanket `except Exception`, which was previously masking the
  conflict into `_UnavailableError` with exit 1. Each new clause is either
  subclass-ordered or `isinstance`-guarded, so no existing path can be reached
  differently.

- **2026-10-02 — Recorded design consequences that are not C1b defects.**
  1. **Exit 2 does not uniquely mean an identity conflict.** Ten entry points
     already returned 2 for an ordinary usage error before C1b: `db`, `catalog`,
     `library`, `dev`, `ai`, `production`, `backup`, `youtube`, `previews`,
     `covers`. Only `sidecar`, `server` and `recovery` have an unambiguous 2. The
     accepted plan mandated 2, so this was complied with, but any operator
     runbook or C5-C7 automation must discriminate on the message or error code,
     never on the exit status alone.
  2. **`_database_state` in `runtime/development.py` deliberately still swallows a
     conflict** and reports `unknown`, because a status probe must not fail. It
     cannot produce a traceback or a wrong status, and `framenest-dev start` still
     exits 2 through `_migrate_database`. Accepted as a named, reasoned deviation.
  3. **The Orchestrator's retention-ledger design creates a harmful incentive.**
     The Worker reports holding every per-tree *occurrence* counter at its pinned
     value by extending existing import statements instead of adding new ones. A
     word-count counter cannot accommodate an authorized change that adds an
     import line, so it pressures code away from clarity. Cut C3 will move these
     counters massively and legitimately. Orchestrator decision, recorded here so
     it is not left to a Worker: **at C3 the per-tree occurrence counters will be
     explicitly re-pinned as an expected consequence of the package move, and no
     Worker may ever contort a diff to match a counter.** A metric must never
     shape the code. The Worker raised this itself as its `LEAD`.

- **2026-10-02 — C1 + C1b complete; fresh independent audit is the next
  envelope.** `feat/kronika-identity-dual-read` is at
  `c02c6753694d5d4958045bb79f80b5eb94b9c75c`, unpublished, `main` and public
  `main` still `18c357c`, tree clean. The audit must be a genuinely fresh Worker
  session because C1 widened a mutation-authorization boundary and its acceptance
  cannot rest on the session that implemented it. Publication of the branch and
  the routine NUC refresh remain separate bounded grants.

- **2026-10-02 — Worker session 07 returned `PARTIAL` with `new-material-risk`.
  Two confirmed defects, both traced to Orchestrator under-specification.**
  Stored as `07_report_00.md`, coordinates `kronika-sole-identity` / session
  `07` / exchange `01` / `KSI-AUDIT-C1`, start and end commit both `c02c675`,
  changed files none, tree clean before and after. Read-only boundary held.
  Orchestrator verified every given measurement was reproduced, none
  contradicted. The audit's own headline: the mutation-authorization boundary
  and the fail-closed resolver are **sound on every attack it could construct**,
  and the four findings are configuration-trust-boundary defects, not gate
  bypasses.

  **F1, Medium, confirmed by Orchestrator.** Process-environment
  case-insensitive matching is lost. `_DualPrefixEnvSettingsSource._load_env_vars`
  returns only `_resolved_field_values(os.environ)`, **replacing** the mapping the
  library produced, so `parse_env_vars` no longer enumerates and case-folds the
  process environment; the library's `_apply_case_sensitive` at
  `.venv/lib/python3.13/site-packages/pydantic_settings/sources/base.py:359`
  lower-cases, so `framenest_port=9999` used to configure the field and is now
  silently ignored, applying the model default with exit 0. Cause is
  Orchestrator under-specification: the C1 grant required "a settings source that
  calls the resolver for every field" but never required preserving the
  inherited case-insensitive enumeration.

  **F2, Medium, and this one is the Orchestrator's own specification.**
  `lookup_env` coerces an empty string to unset **for every field**, so
  `FRAMENEST_PORT=` no longer raises the `int` coercion `SettingsError` that
  produced `FrameNestConfigurationError` and exit 1; it now silently yields the
  default and exit 0. The C1 grant instructed exactly this: "The resolver must
  treat a variable set to the empty string as unset ... so that the currently
  installed environment file and existing systemd `Environment=` handling do not
  change meaning." That rationale was about the **env-file selector**; the Worker
  implemented it globally, correctly following the instruction as written, and the
  global rule broke a previously rejected configuration. The class docstring's
  claim that `env_ignore_empty` handling is unchanged is also misleading, because
  `env_ignore_empty` is not set in `model_config` and the resolver bypasses it.

  **F2 falsifies C1b's central claim.** C1b asserted "no other exit status
  changed", and the Orchestrator accepted it after reading clause placement. That
  verification was correct about code paths and silent about the input domain: a
  configuration that used to fail now succeeds. The claim was wrong as stated, and
  the Orchestrator's own acceptance reasoning missed that dimension. The audit's
  required regression is a **differential parity test** asserting that for every
  settings field over a matrix of old-spelling-only inputs — case variants,
  empty, whitespace, invalid — the dual-prefix source produces exactly what the
  stock `EnvSettingsSource` plus `parse_env_vars` produces. That single test would
  have failed on F1 and F2 at the moment each was introduced.

  **F3, Low, Orchestrator decision required.** `framenest-ai` moved
  `default_ai_config_path()` and `_CliContext(...)` inside its `try` to fix the C1
  traceback path, which changed a **pre-existing** failure from exit 1 with a
  traceback to exit 2 with a clean message. The audit is right that this is
  another exit-status change C1b's claim did not cover. Orchestrator position:
  accept it, because replacing an uncaught traceback with a sanitized error is a
  strict improvement, and record it as an amendment to the C1b goal rather than a
  defect. It does widen the exit-2 collision on that entry point.

  **F4, Low-Medium, dev-only.** `_spawn_server_process` writes
  `FRAMENEST_HOST` and `FRAMENEST_PORT` into the spawned child environment
  without removing or normalising an inherited `KRONIKA_*` spelling, so it
  **manufactures a conflict** for the server it starts. Captured through the
  injectable `spawn_process` hook with nothing spawned. No NUC exposure, but it
  is a real defect with no test at all.

  **F5, Low, latent.** `cmd_remote_probe_release_markers` accepts both marker
  spellings while `read_current_release` still `cat`s only the `.framenest-*`
  names, so a tree holding only `.kronika-release-sha` probes as present and then
  fails on read. No action now; the audit's instruction is that C5 must land the
  writer switch and this reader widening **in one commit**.

  **H1, Medium, judged inert.** The exit-2 collision is larger than ten entry
  points, eleven. The audit's independent judgement: `framenest.service` uses
  `ExecStartPre=… check-database-ready` with no `SuccessExitStatus`, so systemd
  aborts on any non-zero and the journal carries the conflict message; no script,
  unit, JavaScript test or runbook branches on the value 2. In nine of eleven
  colliding entry points the `error_code` differs from the usage error. Only
  `framenest-production` uses the same code for both, where only the message
  separates them. Accepted.

  **H2, Low, pre-existing.** A duplicate mutation header authorises, because
  `_single_value` returns `values[0]` and the mutation header is not in
  `_SINGLETON_SECURITY_HEADERS`. Same behaviour as pre-C1 for the old spelling.
  The audit notes `_single_value` returning `None` is **not** reachable for a
  multi-valued header, which corrects an Orchestrator hypothesis. Cheap hardening:
  add both spellings to `_SINGLETON_SECURITY_HEADERS`.

  **H3, Low.** The release engine discards remote stdout and stderr, so an
  operator sees "command failed" instead of the conflict text. The audit names
  this as the real cost of the collision.

- **2026-10-02 — Two Orchestrator claims corrected by the audit.**
  1. **The retention ledger is weaker than the Orchestrator believed.** Part C
     pins scalars, so it detects that a total moved but not which occurrences
     moved. A cut that renames some things and re-pins the scalar to match the
     partial work **passes**, so a genuinely missed rename survives until a later
     re-pin fails to reconcile, **C7 at the earliest**. The audit's direct answer:
     a missed rename would **not** reliably fail at the cut that owns it. Part A
     is genuinely independent, pinning 89 SHA-256 literals plus two completeness
     tests; Part B pins an enumerated 20-path set. The weakness is Part C only.
     C3 will additionally need a **full** re-pin, not an incremental one, because
     every file moves to `kronika.*` and the ledger's own `src/*/…` glob changes
     shape. Strengthening Part C before C3 is now required, not optional.
  2. **The Orchestrator's "harmful incentive" claim was overstated.** The audit
     read the diff and found the folded `framenest.*` imports were counter-neutral
     and would have happened anyway; the re-pins were caused by genuinely new
     module imports and by 14 new bare-prefix docstring occurrences. The ledger
     behaves as a low-grade ratchet, not as a distortion. The substance of the
     Orchestrator's recorded decision stands, since C3 still needs a full re-pin,
     but the characterisation was wrong and is corrected here.

- **2026-10-02 — Audit independence recorded as genuine.** The audit states which
  checks were its own constructions rather than reused coverage: the
  settings-source differential against the unmodified stock path, a
  reconstructed pre-C1 gate over more than fifty old-only header combinations plus
  4000 seeded random header maps, the resolver edge-case matrix, the mirror
  equivalence matrix executed against both stdlib-only engines, the spawned-child
  environment capture through an injectable hook, and exit-status observations at
  all thirteen console scripts. Five of its own probe assertions were initially
  wrong and the implementation was right in each case; it corrected the probes and
  recorded that, which prevented two false findings. It also disclosed one
  `python3` invocation used as a text editor on its own throwaway `/tmp` probe,
  contrary to the letter of the no-interpreter rule, and stated that no repository
  evidence came from it.

- **2026-10-02 — Worker session 08 returned `PASS`; correction C1c executed
  in-bounds and restored parity.** Stored as `08_report_00.md`, coordinates
  `kronika-sole-identity` / session `08` / exchange `01` / `KSI-CORR-03`, one
  additional commit `24bea56daca28603d81cac8d7ed7e3888ba90671` on
  `feat/kronika-identity-dual-read` over parent `c02c675`, 6 files,
  `+642 / −20`, no push, no new branch. Orchestrator verification: `poetry.lock`
  and `pyproject.toml` are byte-identical at `18c357c` and at `24bea56`
  (`poetry.lock` SHA-256 `f67d3062…` at both), which is what licenses the oracle;
  `git diff c02c675..24bea56` touches exactly six paths and is **empty** for every
  Out-of-scope path, so F3, F5, H1, H2, H3 and D1 were not touched; the parity,
  retention and launcher modules pass `69 passed`; the full Python suite is
  `4347 passed, 8 skipped, 3 warnings, 0 failed` against `4314`, a delta of exactly
  the 33 new tests; JavaScript unchanged at `549 passed, 0 failed, 5 skipped`;
  `ap project check --baseline 24bea56` PASS; tree clean; branch still unpublished.

  **The oracle is genuinely independent and the Worker proved it.** It takes the
  library's own `BaseSettings.__dict__["settings_customise_sources"]` and patches
  the project class to it, so the library's own `_settings_init_sources` builds the
  stock `EnvSettingsSource` and `DotEnvSettingsSource` from `os.environ` through the
  library's `parse_env_vars`. No project dual-prefix class participates, and
  `test_the_stock_reference_runs_only_library_sources` intercepts the hook and
  asserts the constructed classes are `['InitSettingsSource', 'EnvSettingsSource',
  'DotEnvSettingsSource', 'SecretsSettingsSource']` with no `_DualPrefix*` among
  them. The pre-C1 file had no `settings_customise_sources` override at all, so
  this is literally the pre-cut path. `test_the_settings_library_is_unchanged_since_the_restoration_reference`
  enforces the licence inside the suite, so the oracle cannot silently outlive it.

  **Ordering was respected.** The oracle was built and demonstrated to catch both
  defects at HEAD **before** any code changed: `framenest_port=9999` was silently
  ignored with exit 0 while the oracle honoured 9999, and `FRAMENEST_PORT=` exited 0
  while the oracle raised `ValidationError`. The same probe answered the
  environment-file question in advance: `FRAMENEST_PORT=` in a file already failed
  closed on **both** sides, because `_DualPrefixDotEnvSettingsSource` returns
  `{**file_values, **resolved}` and the raw `""` survives. **The file path never had
  the F2 regression**, so no file-side change was needed.

  **The design preserves the conflict authority.** `lookup_env` is byte-unchanged,
  and `lookup_field_value` calls it **unconditionally** before any layer decides,
  so the cross-prefix conflict check remains the single case-exact authority and
  raises before any value is returned. Orchestrator read this directly. The three
  layers are: the case-exact `KRONIKA_` spelling when non-empty; then the
  case-folded `FRAMENEST_` spelling **raw, including `""`**, which is what the
  library produced before the resolver existed, so an unparseable value still fails
  closed; then the case-folded `KRONIKA_` with empty counting as unset. The
  `ENV_FILE` selector and all six direct reader call sites keep their exact C1
  semantics because they still call `lookup_env` directly.

  **Parity is demonstrated to fail when broken**, which was the point of the
  exercise. Under three in-memory reversions the committed module's own
  `_parity_mismatches` reported **773**, **742** and **773** mismatches with the
  test failing, so F1 and F2 are detected separately and not merely as a union. A
  fourth scratch file disabling only the launcher normalisation raised the expected
  `AssertionError`. The matrix is 39 fields × 10 values × 3 case spellings × 2
  channels, one variable at a time, 2340 comparisons and 4680 constructions.

  **One deliberate divergence, correctly declared.** Case variants of the old
  spelling reach exact parity, including the both-cases-present collision, which
  resolves to the later value exactly as the library's own comprehension did. But
  `KRONIKA_PORT=9998` together with `framenest_port=9999` resolves to 9998 with
  **no conflict raised**, because making the conflict rule case-insensitive is
  forbidden. The Worker declined to claim parity, correctly noted that the input
  contains the new spelling so it is not old-spelling-only, and pinned both halves
  with named tests. Orchestrator accepts this as the correct trade.

  **The launcher's `LEAD` was closed and the count corrected.** The audit's lead
  about capture and sidecar child processes **did not materialise**: no such
  construction exists in this package. `development.py` is the only place in
  `src/framenest` that builds a child environment containing an
  identity-prefixed name, and the launcher injects **three** names, not four;
  `FRAMENEST_DEVELOPMENT_RUNTIME_DIR` and `FRAMENEST_DEVELOPMENT_LOG_DIR` are
  read-only overrides never written into the child. The fix adds
  `drop_identity_environment_spellings` before injection. Verified live: with
  `KRONIKA_HOST=0.0.0.0` and `KRONIKA_PORT=48199` in the parent, the child carries
  one name per suffix and no `KRONIKA_*`.

  **Worker corrections to the Orchestrator, recorded as accepted.**
  1. The issued step-9 check was wrong. `18c357c..HEAD` is **not** empty for
     `deploy/ubuntu/framenest_release.py`, `deploy/ubuntu/production_ai_deploy.py` and
     `src/framenest/adapters/api/tailscale_ingress.py`, because **C1** legitimately
     changed them and they predate this session. The property that matters is
     `c02c675..HEAD` empty for those three, which holds. The Orchestrator's check
     would have made an auditor read a pre-existing C1 change as a scope breach.
  2. The parity matrix sets one variable at a time, so it does not cover
     simultaneous multi-field input. The only combinations that changed behaviour
     are the prefix pairs, which have dedicated tests and an unchanged conflict
     suite.

  Ledger: Part A and Part B untouched; six Part C numbers moved, each with a stated
  arithmetic cause. `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["src"]` fell 2983 to 2981
  because composing the launcher constants replaced three inline literals with
  three references plus one new literal, net −3 +1. `ENV_PREFIX_TOKEN_COUNT` and
  `ENV_PREFIX_DISTINCT_NAME_COUNT` did not move.

- **2026-10-02 — C1, C1b and C1c complete on
  `feat/kronika-identity-dual-read` at `24bea56…`; a fresh independent re-audit is
  the next envelope.** `main` and public `main` remain `18c357c`; the branch is
  unpublished by design. The re-audit must check the oracle licence and the
  both-cases-present divergence first, as the Worker recommended, and should also
  judge whether the Part C scalar weakness needs strengthening before C3, which
  will require a full re-pin because every file moves to `kronika.*`. Publication
  of the branch and the routine NUC refresh remain separate bounded grants.

- **2026-10-02 — Worker session 09 returned `PASS with findings`; C1c accepted,
  three findings recorded, none blocking.** Stored as `09_report_00.md`,
  coordinates `kronika-sole-identity` / session `09` / exchange `01` /
  `KSI-AUDIT-C1c`, start and end commit both `24bea56`, changed files none, tree
  clean before and after every step. Orchestrator verification of the report's
  three checkable claims: the inverted docstring sentence is present verbatim at
  `src/framenest/identity_env.py:196-201` and is **internally incoherent**, since
  the first sentence says the compatible spelling cannot shadow the identity
  spelling because it is consulted first, and the second says the reverse is not
  true; `_ALEMBIC_VERSIONS_GLOB` is `"src/*/infrastructure/persistence/
  alembic_environment/versions"`, confirming the Orchestrator's C1c premise that
  C3 changes the glob was wrong; `FROZEN_ALEMBIC_SHA256` is keyed by **basename**
  and resolved as `versions_directory / name`, confirming it survives the move;
  and `tests/contract/test_kronika_settings_parity.py:83-84` builds its variable
  names from `COMPATIBLE_ENVIRONMENT_PREFIX`, confirming the value coupling.

  **A1, Low-Med, accepted as the material finding.** `lookup_field_value`'s
  docstring states its own precedence **backwards**, and session 08's report
  repeats the inversion. Measured: `kronika_port=9998` plus
  `framenest_port=9999` resolves to **9999**, so a case variant of the compatible
  spelling evicts a case variant of the identity spelling with no conflict. A
  **case-exact** `KRONIKA_<S>` is immune, because layer 1 short-circuits. The
  behaviour is pre-C1-preserving, so this is a false claim rather than a
  regression, but it sits in the docstring of the function that defines the
  resolver's precedence, and C7 deletes the compatible fallback and will read it
  as truth. The audit's judgement that the trade-off is defensible while the
  reasoning offered for it is not, is accepted.

  **A2, Low-Med, Orchestrator decision recorded.** The conflict rule is
  **per-channel**: `lookup_env` runs once per source over that source's mapping
  only, so `KRONIKA_<S>` in the process environment and `FRAMENEST_<S>` in the
  environment file raise nothing and the process environment silently wins; four
  differing cross-channel combinations were measured and all four are silent.
  ADR-0085 states no conflict rule at all. **Orchestrator decision: state the
  per-channel rule, do not add a cross-channel conflict check.** Process-over-
  environment-file precedence is documented and intentional, and making a
  cross-channel pair fail closed would break any deployment where the file
  supplies a default and the process environment overrides it. The rule must be
  documented, not enforced across channels.

  **A3, Low, latent, no action.** The dual-prefix sources drop every `_env_*`
  constructor override, because `settings_customise_sources` rebuilds them with
  only `settings_cls` and `env_file`. The divergence is real
  (`_case_sensitive=True` with `FRAMENEST_PORT=9999` gives 8000 on the stock
  reference and 9999 currently) but the audit verified it is **unreachable today**:
  `git grep` over `src`, `tests` and `deploy` shows no caller passes any `_env_*`
  override. Recorded, not corrected.

  **Non-regression re-established at `24bea56` by the audit.** 361 focused identity
  tests pass; the mutation gate and writer invariance are untouched by the C1c
  diff, with `RESEARCH_CREDENTIAL_IDENTIFIER = "KRONIKA_RESEARCH_OPENAI_API_KEY"`
  confirmed **pre-existing at `18c357c`**; `lookup_env` is instrumented at **76
  calls per settings build, 38 fields × 2 sources**, and precedes every
  value-selection layer; exit 2 with a suffix-only message observed through a real
  console script with neither value present in the string; the installed
  environment-file shape works and only case-exact key styles ever did;
  `hide_input_in_errors`, `extra="ignore"`, `env_file_encoding`, the retained
  `env_prefix` and source order all intact. The audit also established that the
  launcher is **not** an exposure path for the A1 evasion, because
  `drop_identity_environment_spellings` compares case-insensitively and stripped
  all eight spellings of the three suffixes while leaving unrelated names alone.

  **Orchestrator measurements corrected by the audit.** The parity matrix is
  **38** fields, **1140** comparisons per channel, **2280** total, **4560**
  constructions, not the 39 / 1170 / 2340 / 4680 the Orchestrator issued; the
  audit verified two builds per comparison with an instrumented subclass. The
  Orchestrator's stated cause for the `src` occurrence movement, "−3 +1", is also
  wrong in its components; the audit measures `development.py` 35→33 on both the
  lowercase and env-token measures, i.e. **−2 and −2**, with `configuration.py`
  net 0. All six ledger movements were independently recomputed and confirmed
  honest; Part A and Part B did not move.

  **Decisions settled for the next grants.**
  1. **Part C strengthening, before C3's grant is written.** Adopt the audit's
     proposal exactly and nothing more: add
     `EXPECTED_FRAMENEST_CONTENT_PATHS: frozenset[str]`, the pinned set of tracked
     text paths whose decoded content contains `framenest` case-insensitively,
     plus one set-equality test, in the same deliberately-not-recomputed style as
     the existing Part B path ledger. The reason is membership: a count map still
     lets file X fall 12→10 while file Y rises 3→5, whereas a pinned content-path
     set fails both when a file that should have been renamed still carries the
     token and when a file that should not have been renamed no longer does. This
     discharges the ADR-0085 promise at lines 114-115 that a premature or missed
     rename "fails loudly at the cut that owns it rather than at the end".
  2. **Parity-test value guard.** The parity module's `_spelled()` builds variable
     names from `COMPATIBLE_ENVIRONMENT_PREFIX`, so if C3 or C7 changes that
     constant's **value**, the matrix silently changes its subject and the parity
     claim becomes vacuous with no test failing. One-line guard required: assert
     `COMPATIBLE_ENVIRONMENT_PREFIX == "FRAMENEST_"` and
     `FrameNestSettings.model_config["env_prefix"] == "FRAMENEST_"`.
  3. **Redundant work: do not spend a cut on it.** Confirmed performance-only and
     immaterial: one full `load_settings` is 1.68 ms and one extra fold is
     0.0001 ms, about **0.008 %**. The audit also corrected the Orchestrator's and
     session 08's phrasing: `parse_env_vars` runs **once** per build and the
     project's own fold runs twice. Outcome-identical to the stock reference for
     a good, malformed and binary environment file.

  The audit's own `LEAD` is accepted for the C3 grant: add one parity case passing
  `_case_sensitive=True` and one passing a non-default `_env_prefix`, so the A3
  blind spot becomes a recorded decision instead of an omission.

- **2026-10-02 — Worker session 10 returned `PASS`; correction C1d executed with
  no runtime behaviour change, proven mechanically.** Stored as `10_report_00.md`,
  coordinates `kronika-sole-identity` / session `10` / exchange `01` /
  `KSI-CORR-04`, one commit `02a80485206eeeb33c43393d25514a30d7fe297f` on
  `feat/kronika-identity-dual-read` over parent `24bea56`, five files,
  `+186 / −14`, not pushed. Orchestrator verified the central claim **by a
  different method** than the Worker used: after removing every triple-quoted block
  from both revisions of `src/framenest/identity_env.py`, the two are **byte
  identical**, and the `def`/`class`/assignment line count is 23 in both. No
  executable line changed anywhere. Full Python suite
  `4355 passed, 8 skipped, 3 warnings, 0 failed` against `4347`, a delta of exactly
  the eight added tests; the four changed modules pass `87 passed`; `ap project
  check --baseline 02a8048` PASS; tree clean; branch still unpublished.

  **The epistemic discipline held.** Every sentence written or changed is listed in
  a statement-by-statement table with its support and an evidence class: measurement
  taken, line of code read, or authority document. Nothing is in the file without a
  row. The old false sentence pair was **deleted, not hedged**. The Worker also
  **refused to write an operator-facing claim it could not support**, stating that
  no measurement in the repository establishes operator practice, so only the
  library's pre-cut reading is claimed. That is exactly the discipline the A1
  finding required.

  **A negative control was reported rather than hidden.** Removing layer 1 does not
  change the all-case-variant outcome, so
  `test_a_case_variant_of_the_identity_spelling_loses_to_the_compatible_layer` is
  correctly NOT DETECTED under that mutation. The Worker recorded this as a
  **correct negative control** proving the two tests are independent halves rather
  than one test wearing two hats, instead of quietly omitting the row.

  **Two Orchestrator corrections accepted.** 1. My issued item-2 table did not say
  its rows are **process-channel** rows, and in the environment-file channel the
  same inputs behave differently because `canonical_identity_environment`
  upper-cases file keys: `kronika_port=9998` plus `framenest_port=9999` written as
  a file becomes `KRONIKA_PORT` plus `FRAMENEST_PORT` and **does** conflict, while
  `KRONIKA_PORT=9998` plus `kronika_port=9999` as a file collapses to one canonical
  name. The rewritten docstring now says "measured on one mapping". 2. The
  re-audit's claim that the parity matrix would change its subject **silently**
  with no test failing is not what was measured: with the constant temporarily set
  to `"KRONIKA_"` or `"UNRELATED_"`, other tests in the module fail loudly, because
  the case tests hardcode `framenest_port`. The guard's value is that it pins the
  matrix subject **directly and by name** instead of relying on unrelated tests,
  and it survives a future edit that removes them.

  Ledger: five Part C scalars re-pinned, each with a per-file cause; Part A and
  Part B did not move and all 14 retention tests pass.

- **2026-10-02 — Orchestrator `LEAD` for C7 recorded.** `lookup_field_value` can
  return the case-folded compatible value even where `lookup_env` resolved
  something else, so the two functions in the same module can disagree for one
  mapping; measured `FRAMENEST_PORT=9998` with `framenest_port=9999` gives
  `lookup_env` `9998` and `lookup_field_value` `9999`. No field-level consumer can
  currently observe the disagreement, because every consumer passes both arguments
  to the same function. **At C7, when the compatible layer is deleted, this must be
  confirmed rather than assumed**: verify that `lookup_field_value` then equals
  `lookup_env` for every name shape.

- **2026-10-02 — Remaining sequence on this branch, in order.**
  1. Part C strengthening: add `EXPECTED_FRAMENEST_CONTENT_PATHS` and its one
     set-equality test, as the re-audit proposed. Must be settled before C2's
     grant is written, because C3's re-pin depends on it.
  2. Cut C2: send both mutation headers and migrate browser storage on read.
  3. Cut C3: the package, distribution and command rename, which needs the AP
     re-gate, the in-memory Alembic alias, and the full ledger re-pin. A3's
     `_env_*` parity cases and the `lookup_field_value`/`lookup_env` collapse check
     belong in C3's grant.

- **2026-10-02 — Worker session 11 returned `PASS`; ledger cut C1e executed.**
  Stored as `11_report_00.md`, coordinates `kronika-sole-identity` / session `11`
  / exchange `01` / `KSI-IMPL-C1E`, one commit
  `0b7567598b6378da25d46874b7cb3f42fb1733ae` over parent `02a8048`, **exactly one
  file**, `+751 / −1`, the single deletion being one docstring sentence. Not
  pushed. Orchestrator verification: `git diff --stat` confirms one file and one
  deletion; `git grep -I -l -i framenest` excluding the ledger file returns exactly
  **718**, matching the Worker's measurement by an independent route; the set
  contains `deploy/ubuntu/fn-production-env-deploy`, the known clean-name case;
  the retention module passes `15 passed`; `ap project check --baseline 0b75675`
  PASS; tree clean.

  **The compensating-scalar demonstration is the accepted record.** The Worker
  renamed the content of `deploy/ubuntu/fn-production-env-deploy` in memory, then
  did exactly what a cut does: re-pinned only the four scalars the rename moved
  (deploy files 19→18, deploy occurrences 212→211, `FrameNest` 3381→3380,
  `FrameNest` files 482→481). **All 14 pre-existing tests passed**, including both
  Part A hash tests, the Part A completeness tests and the Part B path ledger, while
  the new membership test failed with
  `missing=['deploy/ubuntu/fn-production-env-deploy']`. That is precisely the
  partial-rename failure mode session `09` identified, reproduced. The ADR-0085
  lines 114-115 promise that a missed rename "fails loudly at the cut that owns it"
  now has a mechanical check instead of prose.

  Measured shape: **718** paths; per tree tests 321, src 255, docs 88, deploy 19,
  root-level 16, extension 12, scripts 7; Part B's 20 are a **strict subset**, with
  698 paths beyond Part B. **77 entries can never leave the set**: 75 frozen ADR
  bodies plus `docs/FEDORA_SERVICE.md` and `docs/NUC_HOST_BASELINE.md`, all Part A
  hash-locked. Nine frozen ADRs carry no token today and, being frozen, can never
  join it. The Worker's critique of the Orchestrator's sizing expectation is
  accepted: "substantially larger than 20" understated it by two orders of
  magnitude, and the **16 root-level paths** are themselves a finding, because
  **every tree-scoped measure in Part C is structurally blind to the repository
  root**. Those root files are now covered for the first time.

  Two disclosed deviations, both accepted. 1. The module docstring's Part C
  paragraph gained two sentences describing the new measure; a module whose
  docstring enumerates its own parts must not silently omit one. 2. The
  718-entry literal was spliced in with a shell splice into a `/tmp` file and then
  copied over the single authorized target, rather than 718 edit-tool calls; the
  block content itself came from a probe through the declared route. Only the
  authorized file was written.

  Recorded for C3's grant: the ledger reads the **working tree**, so a cut that
  stages a rename without completing it will fail there. That is intended, but C3
  should run the retention module once mid-flight and confirm the failure message
  names exactly the unrenamed paths, so the check is diagnostically useful at the
  moment it fires.

- **2026-10-02 — MATERIAL: an accepted-plan premise for cut C2 is factually wrong,
  found while preparing C2's grant.** The accepted plan `03_report_00.md` states in
  its C2 section that "The server does not validate those strings; the only server
  contract is the mutation header", and on that basis has C2 switch the companion
  protocol strings inside the extension. Orchestrator verification shows the
  opposite: **the extension validates the server's value.**
  `src/framenest/application/companion_picker.py:30` sets
  `COMPANION_API_VERSION = "framenest-companion.v1"`, which
  `src/framenest/adapters/api/x_companion_api.py:163` emits as
  `companion_api_version` in the response body; and
  `extension/background/service_worker.js:283` compares
  `response.body.companion_api_version !== companion.API_VERSION`, where
  `extension/shared/messages.js:9` defines
  `const API_VERSION = "framenest-companion.v1"`. On mismatch the extension returns
  `{ ok: false, error: "version_skew", disable: true }`, which **disables the
  companion picker**. So `framenest-companion.v1` is a hard, validated,
  cross-boundary contract, and renaming it on the extension side alone would break
  the companion against a not-yet-updated NUC. The plan's premise is wrong, not
  merely imprecise.

  Full identifier inventory measured for C2's grant: four mutation-header send
  sites, `src/framenest/adapters/api/web/app.js:416` and
  `extension/background/service_worker.js:762,804,932`. Storage keys:
  `frameNestOrigin`, `framenest.youtube.currentClaim.v1`,
  `framenest.catalog.pageSize`, `framenest.upload.recovery.v1` in the web shell;
  `framenest.companion.v1`, `framenest.companion.web.v1`,
  `framenest.companion.review.v1`, `framenest.review-inbox` and the
  `framenest-companion.v1` port name in the extension. Extension-internal only:
  `framenest.companion.v1` as `PROTOCOL`, shared across
  `sidebar.js`, `review.js`, `picker.js`, `save.js`, `x_adapter.js`,
  `messages.js` and `service_worker.js`, therefore atomic within one bundle.
  CSS and DOM hooks with no server counterpart: `framenest-composer`,
  `framenest-companion-style`, `framenest-attach*`, `framenest-save-*`,
  `framenest-composer-*`. Host storage keys: `framenest-media-host`,
  `framenest-save-host`, `framenest-companion-save-host`,
  `framenest-companion-popup-host`, `framenest-save-popup`. Mirrored download
  filename: `framenest-media.bin`, which the server sends via
  `Content-Disposition` and the extension merely mirrors as a fallback. User-visible
  prose: manifest name `FrameNest X Companion` at version `0.1.0`, and
  `EXTENSION_CONTEXT_RECOVERY_COPY` "FrameNest was reloaded…". The web shell
  shares **none** of the companion strings, so only the header crosses that
  boundary from the shell side.

  Escalated to the Cooperator as a strategic conflict against an accepted plan
  premise, per the project rule on conflicting sources. No C2 grant is written
  until it is decided.

- **2026-10-02 — Cooperator decided the C2 conflict by dual-accept, matching the
  mutation header. Worker session 12 returned `PASS`; cut C2 executed with one
  further escalation.** Stored as `12_report_00.md`, coordinates
  `kronika-sole-identity` / session `12` / exchange `01` / `KSI-IMPL-C2`, one
  commit `78c841f34b8ef33bb6a27ff2dc9323fd2f6cdfe4` over parent `0b75675`,
  14 files, `+922 / −46`, not pushed. Orchestrator verification: 14 files and no
  path outside the granted set; `extension/manifest.json` `version` is `0.2.0`;
  **no `.css` or `.html` file appears in the diff at all**, so Class 5 is
  byte-identical; `EXPECTED_FRAMENEST_CONTENT_PATHS` untouched, confirmed by the
  diff containing no added line for it; retention module `15 passed`; JavaScript
  `576 tests, 571 passed, 0 failed, 5 skipped`, up from `554/549/0/5`.

  **Order-independence is demonstrated, not asserted.** Two tests model the gate
  from `tailscale_ingress` at both revisions and assert the **actual header object
  the production code produces**: `preC1Gate` compares only its own spelling and
  ignores an unknown header, `c1Gate` accepts either spelling and requires every
  present spelling to be `1`. Both tests assert the produced request is authorised
  under each gate, that a pre-cut single-spelling sender stays authorised under both,
  and that the two gates agree. So the Cooperator may load the extension before or
  after the NUC refresh and mutations keep working either way.

  **The consume-path refinement is accepted and is a real defect in the issued
  rule.** The Worker found that "leave the retired entry in place" is not merely
  undesirable on the three *consume* paths but is a defect: `clearYouTubeClaimRecovery`,
  `clearUploadRecovery` and `clearReviewInboxAlarmAndBadge` exist to mark a record
  consumed, so if a consume removed only the current key the fallback read would
  **resurrect the retired entry**, recovering a consumed YouTube claim forever and
  restoring a dead upload. Consume therefore removes **both** spellings. That is the
  existing feature's semantics applied to both names, and it is the only deletion in
  the cut. The Worker flagged it as the one place it read past the literal wording.

  **Four of the Orchestrator's issued inventory parentheticals were wrong**, and in
  each case the issued classification would have produced a wrong or unsafe edit:
  `framenest-companion.v1` is filed as a port name but is the validated API-version
  contract; `framenest.youtube.currentClaim.v1` is `sessionStorage`, not
  `localStorage`; `framenest.companion.v1` and `framenest.companion.review.v1` are
  message protocol strings, not `chrome.storage` keys; and
  `framenest.review-inbox` is a `chrome.alarms` name, which was missing entirely.
  The Worker also found that the web shell **already** carried a Kronika-branded key
  at baseline, `KRONIKA_ATTEMPT_KEY = "kronika.research.attempt.v1"` in
  `sessionStorage`, and matched that file's existing convention. The Orchestrator's
  prediction that "new `kronika.` strings will move Part C scalars" was wrong in
  mechanism: no Part C scalar counts `kronika`, so every movement came from
  `framenest`/`FrameNest` text the change itself added or removed.

  **MATERIAL, second cross-boundary contract found and escalated.** The Worker found
  that `framenest.companion.web.v1` is **not** an internal protocol string but a
  validated `postMessage` contract across the browser boundary. Orchestrator
  verification: `src/framenest/adapters/api/web/companion_host.js:8` defines
  `PROTOCOL`, **gates** on it at line 75 and emits it at 80, 121 and 135, and that
  file is served by the NUC; `extension/ui/sidebar.js:3` defines its own
  `WEB_PROTOCOL`, **gates** on it at line 28 and emits it at 127, 884, 980 and 994;
  and `tests/companion_web_bridge.test.js:47`,
  `tests/companion_review_extension.test.js:1580` and
  `tests/contract/test_local_web_application.py:267` pin the literal on both sides.
  Because both sides gate on it, a unilateral extension rename would leave the host
  never seeing `host_hello`, `hosted` false, and `attach()` returning
  `{ ok: false, error: "not_hosted" }` — **meme attach to the X composer would break
  silently, with no error the Cooperator would notice**, against any NUC that has
  not been refreshed. This is structurally identical to the API-version case the
  Cooperator already decided. **The Worker changed nothing and escalated it.**
  Orchestrator position: the same dual-accept decision must cover this string, and
  the ordering constraint must be recorded in ADR-0085's frozen-residue list or in
  the removal cut's prompt, because nothing breaks today precisely because neither
  side changed.

  **Residual exposure recorded.** A dual alarm name means the review inbox can be
  fetched twice per minute until the retired alarm is cleared, because both
  `kronika.review-inbox` and the retained `framenest.review-inbox` exist and
  `onAlarm` honours both. The Worker chose this over clearing the retired alarm
  because Class 4 forbids deletion and destructive migration was forbidden; the cost
  is one extra idempotent GET per minute, and **the removal cut should clear the
  retired alarm**. The dual-key and dual-alarm state accumulates in the Cooperator's
  real profile: two extra `chrome.storage` entries and one extra alarm, all inert and
  all removable in the removal cut. The dual-accept on the API version is permanent
  until the removal cut, so shipping the removal cut while an old extension is loaded
  would disable the picker against a new server — the intended fail-closed direction,
  and why the reload confirmation is a removal-cut precondition.

  The Worker also recorded honestly that no browser was opened and no real profile was
  touched, so the Cooperator's actual existing `frameNestOrigin`, in-flight upload
  recovery and alarm state are **not** exercised, only equivalents.

  **Orchestrator `LEAD` accepted for later grants.** The issued inventory's
  parentheticals were unreliable in four places and the file-count framing may hide
  further misclassifications. The C3, C4, C5 and C7 inventories must be **re-derived
  from `git grep`**, not carried forward from the plan.

- **2026-10-02 — Remaining sequence.** Decide `framenest.companion.web.v1` with the
  same dual-accept logic. Then publish the branch, then a separate bounded grant for
  the routine NUC refresh. The NUC refresh must not be presented as making the
  companion reload verifiable; it does not, because both header spellings are accepted
  until the removal cut.

- **2026-10-02 — Worker session 13 returned `PASS`; correction C2a executed
  comment-only on the host side and emit-preserving on the extension side.**
  Stored as `13_report_00.md`, coordinates `kronika-sole-identity` / session `13`
  / exchange `01` / `KSI-CORR-05`, one commit
  `9c71bfb0a06cb30c5d747816e9067f6a25350c58` over parent `78c841f`, five files,
  not pushed. Orchestrator verification, all read-only: `companion_host.js` has
  **0 removed lines and 9 added lines, of which 0 are non-comment** once the diff
  marker is stripped, so it is comment-only and its gate, its emit sites and
  `PINNED_EXTENSION_ORIGIN` are byte-identical; `extension/ui/sidebar.js` has
  **4 emit sites still on `v: WEB_PROTOCOL` and 0 on `v: CURRENT_WEB_PROTOCOL`**;
  `ACCEPTED_WEB_PROTOCOLS` is the frozen pair of both spellings;
  `EXPECTED_FRAMENEST_CONTENT_PATHS` untouched, with 0 diff lines referencing it;
  JavaScript `581 total, 576 passed, 0 failed, 5 skipped`; `git rev-list --count
  18c357c..HEAD` is **7**.

  **Orchestrator verification error, corrected.** My first comment-only check
  returned 9 instead of 0 because I compared the added lines **with the diff's
  leading `+` still attached**, so no line could ever match `^  // `. Re-run with
  the marker stripped the answer is 0. Recorded because a mechanical check that is
  silently wrong is worse than no check, and because this is the third instance of
  one class: an issued inventory label that is unreliable.

  **The emit-spelling guard is the valuable part of this correction.** A single
  well-meaning edit changing one emit site to `v: CURRENT_WEB_PROTOCOL` was
  demonstrated to fail two tests, with the diff naming the exact site, and the
  end-to-end test failed on the emitted payload too. The pins include that
  `kronika.companion.web.v1` occurs exactly **once** in the sidebar source, as the
  constant the receive set reads, and **zero** times in the host source, so the
  current spelling cannot leak into an outbound message unnoticed. The end-to-end
  test drives the sidebar's own registered listener with synthetic in-memory
  messages and shows a `web_ready` in either spelling is answered with the
  **retired** spelling, that `host_ack` posts nothing, and that eight non-spelling
  values are refused with nothing posted at all.

  **Ordering constraint recorded at both sites, ADR untouched.** Each site carries a
  comment stating, once and briefly: a validated cross-boundary contract rather than
  an internal identifier; both sides gate on it, so a one-sided rename breaks meme
  attach silently against an unrefreshed peer; the extension dual-accepts but keeps
  sending the retired spelling; the host keeps emitting it; the rename lands in the
  removal cut on both sides together. No ADR was amended and ADR-0085 is not in the
  diff.

  The Worker declined to reuse the Class 2 acceptance helper, for a correct reason:
  its accept list is the API-version pair, so reusing it would have meant mutating
  the Class 2 acceptance the same prompt forbids. `extension/shared/messages.js` is
  therefore unmodified.

  **Worker `LEAD` accepted for the removal cut.** The static `v: <expr>` multiset
  assertions are deliberately brittle and will fail on any unrelated edit that adds
  or renames an outbound protocol expression. **When the removal cut moves these
  constants on both sides, those multiset assertions must be deleted in the same
  commit rather than re-pinned**, because their purpose expires with the retired
  spelling.

- **2026-10-02 — Branch `feat/kronika-identity-dual-read` is complete and green at
  `9c71bfb`, seven commits above public `main` `18c357c`, unpublished.** Remaining
  sequence: publish the branch, then a separate bounded grant for the routine NUC
  refresh, then a decision on auditing the C2/C2a state before C3. The removal cut
  must carry: both cross-boundary ordering constraints, the retired alarm and key
  cleanup, deletion of the two brittle multiset assertions, A3's `_env_*` parity
  cases, the `lookup_field_value`/`lookup_env` collapse check, and the deferred
  Class 5 identifiers with their paired style edits and rendered acceptance.

- **2026-10-02 — Branch published to `main`.** Grant executed exactly: verified
  remote `main` was `18c357c…` and that `9c71bfb…` is a descendant, `git switch
  main`, `git merge --ff-only feat/kronika-identity-dual-read`, push branch then
  push `main`, both non-force. Public readback: `refs/heads/main` and
  `refs/heads/feat/kronika-identity-dual-read` both
  `9c71bfb0a06cb30c5d747816e9067f6a25350c58`; local `main`, `HEAD` and
  `origin/main` equal; tree clean; submodule at
  `73e20ef80b88700d5fcbc397cd8edd4fc425869f`; `ap doctor` PASS;
  `ap project check --baseline 9c71bfb` PASS. Seven commits are now public: C0's
  ADR-0085 landed earlier as `18c357c`, then `90c93ea` C1, `c02c675` C1b, `24bea56`
  C1c, `02a8048` C1d, `0b75675` C1e, `78c841f` C2, `9c71bfb` C2a. The NUC still
  serves `0c850996cd2ef17dae4112733fd17fdc732f4699` and is therefore **seven commits
  behind and has never run any of C1 through C2a**.

- **2026-10-02 — Facts measured while preparing the NUC refresh.** The release
  engine's available subcommands are `status`, `check`, `deploy`, `rollback`,
  `activate-capture` and `rollback-capture`. There is **no `migrate-identity`**; the
  accepted plan introduces it at C4, so it must not be referenced before that grant.
  The engine contains **seven `sudo -n systemctl` call sites**, so every helper
  invocation requires a valid sudo timestamp. Per the project rule that sudo is
  Cooperator-owned and that a Worker never runs `sudo -v`, the NUC preflight is
  **Orchestrator-led and Cooperator-executed**, not Worker-executed. The gate
  interface is
  `scripts/operator/network/framenest_nuc_worker_gate.fish --probe` and
  `--target <name> --user <user> --identity <file> --command <bounded-command>`, and
  it rejects shell metacharacters and multiline commands, so every observation must
  be a single simple command with no quoting.

- **2026-10-02 — NUC preflight, steps one and two PASS. Capture fingerprint
  recorded before any deployment.** Orchestrator-led and Cooperator-executed, as the
  sudo boundary requires. The NUC worker gate was used only for the agent probe,
  which returned `ssh-agent: ready` and exit 0; the release helper runs **locally**
  and SSHes itself, so no further gate use is needed.

  `framenest-release status`, all seven observations as expected:
  `active_release` and `web_release` `0c850996cd2ef17dae4112733fd17fdc732f4699`,
  `capture_release` `94e605c17b881461fad3e22fd8c7fca32cb93976` unchanged,
  `release_path` `/opt/framenest/releases/0c850996…`, `service_active: active`,
  `database_revision: 0035`, `backup_restore_readiness: ready`.

  `framenest-release check --release 9c71bfb0a06cb30c5d747816e9067f6a25350c58`, all
  fields PASS: `ap_gitlink` `73e20ef80b88700d5fcbc397cd8edd4fc425869f` matching the
  pin, `public_main` equal to the requested SHA, `superproject_sha256`
  `8e507406f7777ba32bc6538c2fc418ff77ade1479b3f59d22a79abadffd23931`,
  `ap_archive_sha256`
  `8676685c6e2e2dfaa06395818cc1845bb2ee021cf10868e7ea4abd4fc69132bf`,
  `current_release` still the old tree, `backup_restore_readiness: ready`.

  **The pre-deployment capture fingerprint, recorded verbatim and to be compared
  after the deploy:**
  ```text
  capture_code_tree: e65422fa576fa5b9947e7408e6980e56707c72c4
  capture_runtime_contract_sha256: 691500d51dc9a2f3966de144c3592b0b984e8b2753cca4d599aee3793ee35e6b
  capture_unit_contract_sha256: 5799ec63d85bf54ee749b56579f3281fb66477f3e8b17f78b62620b18ffe8c40
  capture_bridge_protocol: 1
  ```
  These four values are the only available evidence that a web release refresh left
  capture untouched, a requirement that already holds under ADR-0075 and the
  accepted plan. Any change in any of them after the deploy is a finding, not a
  detail.

  Orchestrator read the engine source before authorising each step. `status` and
  `check` are both declared read-only in their own help text; `_cmd_check` writes
  only into a `tempfile.TemporaryDirectory()` on the local machine and reads the NUC
  without writing. Its source gate requires local `HEAD` equal to the requested SHA,
  a clean superproject **and** a clean `.ap` worktree, and public `main` equal to the
  requested SHA; all four were verified independently before the step was issued. It
  also raises `EXIT_BACKUP_NOT_READY` unless backup readiness is `ready`.

  **Deployment safety analysis recorded before authorising the deploy.** Between
  `0c850996` and `9c71bfb` no cut adds an Alembic migration, so head stays `0035` and
  the routine same-schema path applies rather than the `migration-required`
  continuation. `relocate_venv_shebangs` requires `framenest-db` and
  `framenest-backup`, both still declared in `pyproject.toml` at `9c71bfb`, since C7
  is what removes them. The helper's same-schema check runs `framenest-db status` on
  the **target** tree **before** the symlink switch, so a settings-resolution failure
  aborts while the old release still serves; that check is the real exercise of C1's
  restored parity against the real installed environment file. Ordering is safe in
  both directions: after the deploy the server accepts both header spellings, so a
  not-yet-reloaded extension keeps working, and the server still emits
  `framenest-companion.v1` and still serves the `framenest.companion.web.v1` host,
  both of which the shipped extension accepts.

- **2026-10-02 — Env-file observation, then the routine NUC refresh COMPLETED.**
  Through the gate, counts only, no values read or printed:
  `grep -c FRAMENEST_ /etc/framenest/framenest.env` returned **24**, and
  `grep -c KRONIKA_ /etc/framenest/framenest.env` returned **0**. That closes the last
  open unknown: no key is set under both prefixes, so the fail-closed conflict path
  cannot be exercised by the installed file, and all 24 keys resolve from the
  compatible spelling, which is the case C1 and C1c exist to serve. No further
  empty-value check was needed, because the currently serving `0c850996` already loads
  this file successfully and C1c restored parity, so any value that would fail now
  would already fail today.

  Under the standing routine-refresh authority of ADR-0075 and the runbook, the refresh
  was executed by the Cooperator in his own session, since it restarts a service and
  standing authority is not automatic deployment. Command:
  `./deploy/ubuntu/framenest-release deploy --release 9c71bfb0a06cb30c5d747816e9067f6a25350c58 --yes`.
  No `migration-required` exit; the same-schema path applied as predicted.

  Deploy output, verbatim where it matters:
  ```text
  framenest-release deploy complete: 9c71bfb0a06cb30c5d747816e9067f6a25350c58
  web_release: 9c71bfb0a06cb30c5d747816e9067f6a25350c58
  capture_release: 94e605c17b881461fad3e22fd8c7fca32cb93976
  ```
  **`capture_release` is unchanged at `94e605c1…`.** That is the first of two
  independent pieces of evidence that capture was not touched. The second is the engine
  source, read before the step: `deploy` restarts only `SERVICE` at
  `framenest_release.py:379`, while the capture runner restart lives in
  `activate-capture` at line 562, a different subcommand that was not invoked.

  The NUC web release is now `9c71bfb`, seven commits ahead of where it was, and it has
  for the first time run the dual-read resolver, the exit-2 conflict path, the dual
  header acceptance and the storage-key migration. Post-deploy `status` and a second
  `check` for the capture fingerprint comparison were requested next. The remote sudo
  timestamp is still live and must be released by the Cooperator with a terminal
  `sudo -K` when this sequence ends.

- **2026-10-02 — Post-deploy status HEALTHY. NUC serves C1 and C2 for the first time.**
  ```text
  active_release: 9c71bfb0a06cb30c5d747816e9067f6a25350c58
  web_release:    9c71bfb0a06cb30c5d747816e9067f6a25350c58
  capture_release: 94e605c17b881461fad3e22fd8c7fca32cb93976   (unchanged)
  release_path:   /opt/framenest/releases/9c71bfb0a06cb30c5d747816e9067f6a25350c58
  service_active: active
  database_revision: 0035
  backup_restore_readiness: ready
  ```
  `database_revision` stayed `0035`, confirming the same-schema path never crossed a
  schema boundary. `service_active: active` is the field that would have stopped this
  sequence, and it is healthy. A second `check` was requested to compare the capture
  fingerprint against the pre-deploy record. The remote sudo timestamp remains live and
  is released by the Cooperator with a terminal `sudo -K` at the end of this sequence.

- **2026-10-02 — Worker session 14 returned `PASS`; cut C2b executed, deliberately partial.**
  Stored as `14_report_00.md`, coordinates `kronika-sole-identity` / session `14` /
  exchange `01`, one commit `09e45e54c8444281c147f9ba799e3602bb57d9aa` on `main` over
  parent `9c71bfb`, 16 files, `+149 / −41`, **not pushed; `main` is ahead 1**. This is the
  first cut since C0 authored on `main` directly. Orchestrator verification:
  `extension/manifest.json` `name` is `Kronika X Companion` with `version` still `0.2.0`
  and the manifest `key` byte-stable; `extension/ui/sidebar.html:20` wordmark is `Kronika`;
  exactly two product `.py` files changed and **no `.css` file appears in the diff**; 16
  paths total. JavaScript `582 total, 577 passed, 0 failed, 5 skipped`; Python `4359
  passed, 8 skipped, 3 warnings`; retention `15 passed`.

  **The Worker exceeded the issued grant deliberately and disclosed it.** The
  mandated step-6 enumeration parsed every letter-bearing node on each surface, which
  returned `1` for `index.html`: a fifth prose string at line 470, "FrameNest does not
  expose this application on the public internet", in an already-authorised file of the
  same class. It changed it, on the reasoning that leaving it would ship a served page
  reading Kronika four times and FrameNest once, that over-changing one word is a
  one-line revert while under-changing costs a publication grant and a NUC refresh cycle,
  and that it should be disclosed rather than discovered. Orchestrator accepts.

  **Three Orchestrator enumeration errors corrected by the Worker.** 1. `index.html`
  has **five** user-visible prose strings, not four; the fifth was found only by parsing
  all 1705 text and attribute nodes rather than grepping known literals. 2. My claim that
  "no test pins the `index.html` prose" was **wrong and load-bearing**:
  `tests/contract/test_local_web_application.py:142,966` and
  `tests/integration/test_development_launcher.py:62` assert positively that `
  `"FrameNest"` appears in the served HTML, and those surfaced only as three failures
  in the eleven-minute full suite, because the Worker searched the product side and not test
  assertions over the product. 3. `tests/companion_review_extension.test.js:545,643` also pin
  the manifest action title and the recovery copy. Conversely the Worker **corrected my table
  the other way**: the `framenest-media.bin` literals in `x_companion_extension.test.js` are not
  pins but arbitrary parameters proving the adapter preserves whatever filename it is given,
  proven by tracing the overwrite and left unchanged.

  **The product is now deliberately, visibly partially renamed, and the Orchestrator
  must not present it as complete.** Verified by the Orchestrator: `extension/ui/sidebar.js`
  still carries 16 occurrences including the user-visible "Connect FrameNest", "Disconnect
  FrameNest", "Could not reach FrameNest." and "FrameNest did not load in this panel.";
  `x_adapter.js` 32, `messages.js` 18, `save.html` 2, `save.js` 2, `picker.js` 3,
  `review.js` 2, `picker.html` 1, `service_worker.js` 5. The most visible split is inside a
  single dialog: `sidebar.html:53` now reads "Kronika origin" while
  `sidebar.js:838` directly beneath it still reads "Use the FrameNest HTTPS tailnet origin".
  The files carrying the remaining strings are exactly the files the grant forbade.

  **The retention membership set did its job: it shrank by three.**
  `extension/manifest.json`, `extension/ui/sidebar.html` and
  `src/framenest/adapters/api/web/index.html` left
  `EXPECTED_FRAMENEST_CONTENT_PATHS`, which is the intended behaviour and means a later cut
  that re-adds the brand there fails loudly. Part A and Part B did not move.

  **Sequencing constraint the Orchestrator derived.** The extension is loaded from the
  working tree, not from the NUC. If the Cooperator reloads before C2b is published and
  refreshed, the extension will carry `kronika-media.bin` as its download fallback while the
  still-unrefreshed server sends `framenest-media.bin` in `Content-Disposition`, and the
  normal path takes the server's value. So downloads would keep the old name. The order must be
  publish, refresh, then reload.

  **New finding for the next cut.** `src/framenest/application/media_content.py:88`
  `stem = f"framenest-media-{media_id.to_string()}"` is a distinct literal from
  `framenest-media.bin`, it is arguably **more** visible because it is the fallback stem that
  lands in the Cooperator's Downloads folder when a media file's own name sanitises to empty,
  and it is pinned by `tests/unit/application/test_media_content_application.py:255` and
  `tests/integration/test_local_web_media_playback.py:230`.

- **2026-10-02 — Worker session 15 returned `PASS`; cut C2c executed. The user-visible
  rename in the extension and served shell is now coherent.** Stored as `15_report_00.md`,
  coordinates `kronika-sole-identity` / session `15` / exchange `01`, one commit
  `77bcb81c8a5f84e91ec4b31dd12f8ad2204016a8` on local `main` over parent `09e45e5`,
  16 files, `+315 / −84`, **not pushed; `main` is two commits ahead of public `main`**.
  JavaScript `583 total, 578 passed, 0 failed, 5 skipped`; Python `4359 passed, 8 skipped,
  3 warnings`; retention `15 passed`; `ap project check --baseline 77bcb81` PASS. The Python
  count not moving is itself evidence the cut is a pure display rename.

  **All three exclusion classes verified independently by the Orchestrator, whole-tree:**
  `X-FrameNest-Request` 74 to 74, `FrameNestCompanionWeb` 13 to 13,
  `FrameNestSidebarBridge` 2 to 2, `FrameNestReviewInbox` 4 to 4,
  `canonicalizeFrameNestOrigin` 7 to 7, `acceptFrameNestOrigin` 14 to 14,
  `framenest-attach` 11 to 11, `data-framenest-` 150 to 150,
  `framenest.companion.web.v1` 14 to 14, and `FrameNestSettings` 505 to 505. `manifest.json`
  does not appear in the diff at all, and **no `.css` file appears in the diff at all**.
  The single whole-tree movement, `FrameNestCompanion` 57 to 58, is exactly the `+1` the Worker
  disclosed: a case-sensitivity comment inside its own new guard in a test file. No product
  occurrence of any excluded token moved.

  **The Worker found thirty-three display assertions to repoint against the four the
  Orchestrator listed, and the largest omission is a lesson.**
  `tests/youtube_acquisition_cockpit.test.js:23` pins the **entire 197-character**
  acquisition-confirmation sentence of `app.js:1625` as a module-level constant, so no search for a
  short brand phrase can find it; it would have shipped red at the eleven-minute suite.
  The Worker also found that **two of the four assertions the Orchestrator did list are
  whole-file regexes for a literal that occurs twice in `sidebar.js`**, so reverting either
  occurrence alone leaves them green, verified by single-line revert. It replaced them with
  scoped function extraction.

  **The Orchestrator lesson recorded for every remaining cut:** derive the rename list by
  parsing each artefact, derive the pin list by searching tests both for the retired
  spelling **and** for a distinctive substring of every string being changed, and
  **reject any display pin that is a whole-file regex where the literal occurs more than
  once.** Thirty-one of the thirty-three repoints derive the expected text from the single
  identity rather than spelling it, so a one-sided rename now fails at the pin that owns
  it, and the two Python download-stem pins became structural shape assertions rather than
  literal ones, deliberately not hardcoding the new brand.

  Ledger: `EXPECTED_FRAMENEST_CONTENT_PATHS` shrank by two as `extension/ui/save.html`
  and `extension/ui/picker.html` lost their last occurrence, which is the intended
  behaviour. Part A and Part B did not move.

- **2026-10-02 — MATERIAL for the next cut: `FrameNest Server` is a persisted value, not
  display text.** Orchestrator verification: `SERVER_DEVICE_DISPLAY_NAME = "FrameNest Server"`
  at `src/framenest/application/library_workflow.py:21` is used at line 196 as
  `Device(id=DeviceId.new(), display_name=SERVER_DEVICE_DISPLAY_NAME)`, which is
  **written into the catalog database**. Every device record already created therefore
  stores the old brand in `display_name`, and renaming the constant would only affect
  records created afterwards, leaving the catalog showing a mix of both names. This is the
  first rename in this whole with a durable-data dimension, so it cannot be folded into a
  pure prose cut the way C2b and C2c were. The precedent matters: the predecessor's S9 reset
  emptied the catalog, and the plan records an empty Gallery, so the NUC may hold zero device
  rows, in which case the rename is a no-op in practice. That must be observed, not assumed.

  The remaining CLI and operator prose the Worker identified is safe and process-local:
  `FrameNest is running at …` in `infrastructure/runtime/development.py:296,468`,
  `FrameNest configuration could not be loaded.` in `adapters/cli/ai.py:720`,
  `adapters/cli/youtube.py:187` and `infrastructure/persistence/cli.py:70`, and the
  `FrameNest readiness probe` string in `tests/contract/test_production_ai_deployment.py`.
  Those are printed output, never stored.

- **2026-10-02 — The device-record observation cannot be taken from the Orchestrator
  session.** The sanctioned gate probe returns `ssh-agent: ready` with exit 0, so the agent
  socket is present, but the SSH connection to the NUC times out: this is the untrusted
  Cursor/AppImage ambient environment, which is not on the tailnet. The observation is
  therefore a Cooperator terminal action. The command prepared for him was **verified
  correct against the unit file** rather than assumed: `deploy/systemd/framenest.service`
  declares `User=framenest`, `WorkingDirectory=/opt/framenest/current` and
  `EnvironmentFile=/etc/framenest/framenest.env`, which matches the
  `service_account_prefix` convention in `deploy/ubuntu/framenest_release.py` exactly.
  Its output carries device UUIDs and must never be pasted into a report or this trace.

  **The same probe incidentally proved a C6 scoping fact.** The application units
  (`framenest.service`, `framenest-catalog-backup.service`,
  `framenest-catalog-offdevice.service`) use `User=framenest` with
  `/etc/framenest/framenest.env`, while **all five capture units already use**
  `User=kronika-capture` with `/etc/kronika-capture/capture.env`. The parked capture
  module is therefore already named differently from the application, so C6 is not one
  uniform rename and must treat capture identity as one whole rather than a mixed sweep.

- **2026-10-02 — Orchestrator enumeration error, recorded because it repeats the Worker's
  lesson from the other side.** A whole-tree grep for quoted strings containing
  `FrameNest` returned fifty rows, of which the large majority were **false positives**:
  negative assertions such as `assert ">FrameNest<" not in header_section` and
  `assert.doesNotMatch(adapterSource, /textContent = ["']Save to FrameNest["']/)`, plus
  test module docstrings. Both top candidates were verified by hand and are correct guards
  asserting the old brand is **absent**, and both were already updated by C2b. Had they been
  taken at face value they would have produced a false finding and a pointless cut.
  The derivation discipline is now recorded from both directions: the Worker parses
  artefacts instead of grepping, and the Orchestrator does not treat a grep hit as a
  finding without opening the line and checking whether it is an assertion of presence or
  of absence.

- **2026-10-02 — SECOND durable-data instance, and it is more serious than the device
  name: the development launcher writes a SQLite database to a brand-named default
  path with no fallback read.** In `src/framenest/infrastructure/runtime/development.py`,
  `_database_path` returns macOS `~/Library/Application Support/FrameNest/development/catalog.sqlite3`
  or Linux `$XDG_DATA_HOME/FrameNest/development/catalog.sqlite3`; `_runtime_dir` returns
  the `Application Support`/`XDG_STATE_HOME` equivalent; and `_log_path` returns macOS
  `~/Library/Logs/FrameNest/development/server.log`. Each returns **exactly one** path and
  **never reads the old one**, so renaming does not migrate, it orphans. The concrete cost is
  that an existing development database would be left on disk and a fresh empty one created
  in its place. Each has a `FRAMENEST_`/`KRONIKA_` env override, which is the escape hatch.
  This belongs to C4, which already owns the dev launcher and host paths, and it is the
  concrete reason the next cut must **not** be described as a pure prose cut: the device
  display name and these three default paths are the two places where the brand is
  currently load-bearing for data.

- **2026-10-02 — The domain exception hierarchy is code identity, not prose, and is
  large.** `rg "class FrameNest\\w+" src/framenest/domain` returns a long list of
  `FrameNest*Error` classes across `youtube_acquisition.py`, `x_acquisition.py`,
  `uploads.py`, `upload_publications.py`, `security_audit.py`, `media_user_alias.py`,
  `media_sidecar.py` and more. These are class names rather than user-visible text and
  belong to C3 with the package move, not to a display cut. The user-visible strings
  that genuinely remain in product code are narrow: the `FrameNest is running at …`,
  `FrameNest is stopped.` and `FrameNest startup failed.` runtime messages in
  `development.py`, `Requested category conflicts with the existing FrameNest save.` in
  `application/x_acquisition.py`, `The loopback FrameNest operator API is unavailable.` in
  `adapters/cli/youtube.py`, `FrameNest configuration could not be loaded.` in
  `infrastructure/persistence/cli.py`, and the operator-side
  `FrameNest production AI deployment failed:` in `deploy/ubuntu/production_ai_deploy.py`.

- **2026-10-02 — DEVICE OBSERVATION COMPLETE: exactly one device exists on the NUC, and
  its stored name is operator-typed, not the code default.** The Cooperator ran
  `framenest-catalog device list` and reported **one** row whose `display_name` is
  `"FrameNest NUC"`. **The device UUID he pasted into the session transcript is
  deliberately not recorded in this trace and must not enter any report or commit.**
  The decisive detail is that this value is **not** `SERVER_DEVICE_DISPLAY_NAME`
  (`"FrameNest Server"`). It was supplied by the operator at registration through
  `framenest-catalog device register --display-name`, so `LibraryWorkflow` line 196 was
  never taken on this host. **Consequence: changing the code default would fix zero existing
  rows here.** The earlier framing of a durable-data migration was larger than the facts
  warrant, and the real work is a single stored value, not a data migration.

  **Renaming that value has no product verb, and the schema makes the alternatives worse.**
  `framenest-catalog` exposes only `device register|get|list` with no `rename`, `update` or
  `delete`, and `catalog_schema.py:75` declares
  `ForeignKey("devices.id", ondelete="RESTRICT")` with a unique constraint on
  `(device_id, path_flavor, root_root)`. Therefore delete-and-re-register is blocked by
  `RESTRICT` while any library exists, and would mint a new `device_id` that
  orphan-s any library link. A single-column `UPDATE devices SET display_name` is the
  **only** path that preserves `device_id` and therefore every library foreign key, so it
  is also the least destructive one. This makes the library count immaterial to the
  decision and no further catalog observation is needed.

  **A raw `sqlite3` UPDATE bypasses two application invariants, and the Cooperator
  should decide knowing that.** `engine.py` sets `PRAGMA foreign_keys=ON` and a `busy_timeout`
  on every connect, and then calls `verify_private_catalog(normalized_path)`,
  which re-validates the directory, the database file and the SQLite auxiliary files;
  the standalone `sqlite3` binary defaults `foreign_keys` to **OFF** and runs no such
  verification. For a single display column with no key change the FK exposure is nil, and
  `busy_timeout` means a concurrent write waits rather than fails, but the check is
  genuinely skipped and the operation is operator action on production catalog data, so it
  needs its own bounded grant and a backup first rather than being folded into a prose cut.

- **2026-10-02 — STRATEGIC TENSION raised, not resolved: the Cooperator asked for the word
  `framenest` to appear nowhere at all, and ADR-0085 deliberately forbids that end
  state.** The request was for complete identity, "Kronika NUC" included, with the former
  spelling nowhere. ADR-0085 section "Named frozen residues" lists
  `/opt/framenest/tooling/poetry/...` and `/opt/framenest/tooling/python/...`,
  protocol magic `FNCBE01`, and the capture state directory `framenest-chatgpt-page`, and
  states at line 89: "These keep the former spelling on purpose. **They are not pending
  rename work.**" The retention ledger freezes a further 122 blobs, namely ADR bodies
  0001 through 0084 and 36 applied Alembic revisions. A literal zero-occurrence repository is
  therefore unreachable by design and by decision, and reaching for it would require
  amending ADR-0085 rather than executing it. The charitable and ADR-consistent reading of his
  intent is **zero user-visible and operational occurrences, with the named residues
  kept**, which is what the cut sequence already targets. This must be confirmed with him
  explicitly instead of being silently reinterpreted, because the two readings differ by an ADR
  amendment. No code was changed against either reading.

- **2026-10-02 — Additional unrecorded durable artifact identifier: `framenest_umask`.**
  `engine.py` reads and writes `connection.info["framenest_umask"]` to establish the
  private file mode for newly created catalog files. It is an in-process identifier
  rather than a stored artifact, so it belongs to the C7 code-identity class, but it had not yet
  been inventoried and is now listed so a later cut cannot miss it.

- **2026-10-02 — DECISION CONFIRMED by the Cooperator: the target is zero user-visible and
  operational occurrences of the former spelling, with the ADR-0085 named frozen
  residues deliberately kept.** He was shown that a literal zero-occurrence repository is
  unreachable by design, chose the recommended reading explicitly, and declined the
  alternative that would have required amending ADR-0085. **No ADR amendment is
  pending and none is authorised.** This reading also gives the remaining cuts a crisp, testable
  membership test: user-visible strings, operator-facing process output, and operational
  identifiers are in scope, while source docstrings, test module docstrings, class and
  module names, and the named residues are not. Keeping docstrings out is deliberate, so
  the cut stays narrow and auditable rather than becoming a spelling sweep.

- **2026-10-02 — Next cut scoped as a bounded product-display and operator-prose cut,
  deliberately placed BEFORE C3.** C3 is the highest-risk cut in the programme because it
  re-pins the whole retention ledger, moves the package and distribution, aliases eleven
  Alembic imports and forces an AP `provenanceModule` re-gate with a new baseline.
  Folding display prose into it would make C3 verification ambiguous between two
  unrelated concerns and is hard to reverse, so prose is taken first and C3 is left with
  only its own question. The product-code inventory was verified line by line and is
  narrow: the `FrameNest is …` runtime messages in
  `infrastructure/runtime/development.py` (already running, already stopped, already
  running at, did not become healthy in time, startup failed, not running, stopped, and
  the managed-process health message, plus the concurrent-operation message), the single
  sentence `FrameNest configuration could not be loaded.` which appears in BOTH
  `adapters/cli/ai.py:720` and `infrastructure/persistence/cli.py:70`, `The loopback
  FrameNest operator API is unavailable.` in `adapters/cli/youtube.py`, `FrameNest production
  AI deployment failed:` in `deploy/ubuntu/production_ai_deploy.py`, and
  `SERVER_DEVICE_DISPLAY_NAME` in `application/library_workflow.py:21`.

  **The three-occurrence trap is present in this cut and must be written into the Worker
  prompt.** `application/x_acquisition.py` raises `XAcquisitionCategoryConflictError` with the
  **identical** sentence `Requested category conflicts with the existing FrameNest save.`
  at **lines 369, 373 and 378 of the same method**. A whole-file or whole-function regex
  pin on that sentence would stay green if only one or two of the three occurrences were
  renamed, which is precisely the weak-pin failure the Worker disclosed and corrected in
  C2c. Any pin for it must count or scope all three.

  **Explicitly excluded from this cut and where each item instead belongs:** the three
  development launcher default paths and the macOS `Library/Logs` path are C4;
  `FrameNestSettings`, `FrameNestConfigurationError`, `FrameNestJsonFormatter` and the
  long `FrameNest*Error` domain hierarchy are C3 code identity; `framenest_umask`
  and the env, header, storage and protocol keys are C5 and C7; tooling paths,
  `FNCBE01` and the capture state directory are frozen residues under ADR-0085.

- **2026-10-02 — Sequencing decided: one deploy covers C2b, C2c and the new prose cut, and
  the catalog display-name data operation happens AFTER that deploy against the final
  release.** The stored `devices.display_name` is independent of any code change, since the
  code default was never used on this host, but doing it last means a single deploy and a
  single data operation close the visible identity together, and the data operation is
  then performed against exactly the release that will remain running. One remaining
  catalog question is unanswered and is **not** needed for the code cut but is needed for the
  data operation: whether any `libraries.display_name` also carries the former brand.
  `library list` output contains private media root paths and must never be pasted; only
  the yes-or-no answer on the display name may be reported.

- **2026-10-02 — Orchestrator truncation error, disclosed to the Worker rather than
  quietly corrected.** My first C2d inventory ranked grep output by frequency and
  truncated it with `head -50`. The truncation was silent and hid roughly a dozen real
  sites: every `INVALID_*_MESSAGE` constant in `domain/`, all five argparse `help=`
  strings, `server.py:147`, `configuration.py:461`, `x_request_api.py:185,207` and the
  Alembic `env.py` connection error. The untruncated standalone-word derivation returns
  **96** occurrences in `src/framenest`, of which about a third are docstrings.
  Two lessons now stand together with the C2c lesson: never truncate a derived
  inventory without reporting the truncation, and derive with the brand as a standalone
  word (`(?<![A-Za-z_])FrameNest(?![A-Za-z])`) because a substring search returns class
  names and module paths as noise. The Worker was given the incomplete list **and** told
  explicitly that it is incomplete, so that it re-derives rather than trusting me.

- **2026-10-02 — Cut C2d issued as `16_implementation_00.md`, deliberately before C3.** Scope
  is the eight in-scope item groups: nine `domain/` validation constants, the API error
  payloads, the runtime and CLI output, the argparse help text, the configuration error,
  the Alembic `env.py` connection error, `SERVER_DEVICE_DISPLAY_NAME`, and the external
  AI system prompt. Seven exclusion classes are named precisely, each with its owning
  later cut, so nothing can be lost: the deliberately dual-spelled
  `tailscale_ingress.py:869` message stays until C7; `script.py.mako:19` is named even
  though it is not one of the 36 frozen revisions, because it generates the brand into
  every future migration and belongs to C4; and `development.py` is split so that only its
  messages may change and no path expression may.

  **`movie_identification.py:236` is the one site that leaves the host.** It is the system
  prompt for the movie-identification assistant, `You are FrameNest's movie
  identification assistant.`, sent to an external provider. It is in scope as an
  operational occurrence, it is authorised as a string edit only with an explicit
  prohibition on contacting a provider, and it is required to be reported as its own item
  because it is the only externally visible consequence of this cut.

- **2026-10-02 — C2d test-side cost measured before dispatch, which corrected my own
  risk assessment downward.** I had left "how many tests pin the domain messages" as a
  risk for the Worker to discover. That was a cop-out; it was measurable, so I measured
  it. **Exactly thirteen test literals pin any in-scope string**: `Invalid FrameNest …`
  seven across `test_media.py`, `test_libraries.py`, `test_identities.py` and
  `test_devices.py`; `FrameNest Server` two in `test_library_workflow.py`; `FrameNest
  configuration could not be loaded.` two; `FrameNest startup failed` one; and the
  category-conflict sentence one. **Every other in-scope string is pinned zero times.**
  The `Medium` band is retained rather than lowered, because the reconciliation against
  my deliberately incomplete list, the deliberately dual-spelled message, the externally
  sent prompt and the docstrings boundary are all judgement, but the mechanical size is
  at the low end of the band.

  **Three measured consequences are now written into the prompt as binding
  instructions, each because a naive Worker would get it wrong.** First, **the five argparse
  `help=` strings have zero coverage**: `test_operator_cli_hygiene` asserts only that
  `--help` succeeds from an unrelated cwd and never inspects text, so those renames are
  free but also **cannot be demonstrated failing on revert**, and the Worker is told to say
  so rather than fake a demonstration. Second, and most important, **three of the four
  category-conflict occurrences are entirely unpinned**: the single pin at
  `test_x_request_api.py:282` is a scoped payload comparison covering
  `x_request_api.py:207` only, so `x_acquisition.py:370,374,379` can be missed or
  botched with **no red test anywhere**. This is the weak-pin defect class in its purest
  form, and it is now a measured fact rather than a warning. Third, both `FrameNest
  Server` pins are properly scoped, and `test_library_workflow.py:227` asserts the
  **persisted** row through `devices.list_all()[0].display_name`, which makes it the single
  most valuable assertion in the cut.

- **2026-10-02 — Cooperator granted explicit authority to continue and to deliver
  `16_implementation_00.md`, and confirmed the C2d target as zero user-visible and
  operational occurrences with the ADR-0085 named frozen residues kept.** No P14 model
  rotation and no manual-messenger opt-out has been declared, so the AGENTS.md default
  route applies: direct dispatch of the one complete prompt into one concrete Worker
  session. Prompt is 515 lines and internally consistent, with the baseline SHA in four
  places and the literal count of thirteen stated identically in three.

- **2026-10-02 — C2d ACCEPTED. Commit `d5955d5c0478ef7fa025fa9f8cba26ef56656883`,
  parent `77bcb81`, local `main` three commits ahead of public `main`, not pushed, 33
  files, +116/−67.** Orchestrator verification: residual standalone-brand count in
  `src/framenest` is **47** exactly as reported, and every one is out of scope; the
  seven exclusion classes all show **+0**; no file under `versions/` and no
  `script.py.mako` appears in the diff; **zero** path expressions changed in
  `development.py`; and `tailscale_ingress.py:869` still carries both spellings. Python
  `4359 passed, 8 skipped, 3 warnings` with **+0 tests**, JavaScript
  `583 total, 578 passed, 5 skipped` unchanged. The unchanged Python count is itself
  evidence of a pure string substitution.

  **The two externally sent AI prompts were verified structurally, not just counted:** the
  diff for `infrastructure/ai/prompts.py` and `application/movie_identification.py` is
  **exactly one line each**, brand word only, with every f-string placeholder and
  prompt instruction intact. Both now name Kronika to the provider, and no provider
  was contacted.

  **Orchestrator defects confirmed by independent verification, not conceded on
  report alone.** `youtube.py:187` at `77bcb81` really does carry `"FrameNest
  configuration could not be loaded."` and not the loopback sentence I assigned to it;
  `infrastructure/ai/prompts.py:7` really does hold a second externally sent system prompt,
  `MEDIA_SUGGESTION_PROMPT`, absent from my list; `test_development_launcher.py:51`
  really is `assert "FrameNest is running" in started.stdout`, a genuine presence pin I
  omitted; and `test_x_request_api.py:282` really is the `raise` argument of a local
  `_ConflictService` fake inside a test that asserts only `status_code == 409` and an
  error code, so it is fixture data and not a pin. **The worst defect is my own
  impossible instruction:** I required the Worker to demonstrate that reverting one of
  the four category-conflict occurrences turns a pin red, while all four are
  unpinned. I asserted the existence of a pin I never checked.

- **2026-10-02 — Worker session 16 committed two transcription errors of its own, of the
  same failure mode as mine.** Its byte-identity table reports
  `framenest-companion.web.v1` at 14 occurrences, but that hyphenated token does not
  exist anywhere in the tree, count **0**; the real web protocol string is
  `framenest.companion.web.v1`, measured 14 at base and 14 now. It also reports
  `X-FrameNest-Request` at **71**, where two independent methods both give **74**.
  Neither error changes a delta, so no conclusion in the report is affected, but both
  show the table rows were transcribed rather than re-derived. **Recorded symmetrically:
  the Orchestrator and the Worker each failed C2d by trusting recall over measurement,**
  and the standing rule is that a verification table must be regenerated by the
  reporting party rather than assembled from earlier turns.

- **2026-10-02 — Residual risk accepted and explicitly bounded: nineteen of the forty-
  nine product changes have no behavioural test coverage.** Five argparse
  help/description strings, ten unpinned `development.py` messages and all four
  category-conflict occurrences revert green. The only automated signal for these is
  the retention ledger's whole-tree occurrence **count**, which fires when something moved and
  never on what it moved to, so it cannot distinguish a correct rename from a wrong
  one. The Worker's LEAD is accepted as the mitigation: **before the deploy, read those strings
  by hand from the release**, since they are short and no test reaches them. Also noted:
  `tests/contract/test_development_cli.py:175` holds a stale fake
  `message="FrameNest is running."` that deliberately was left unchanged as fixture data
  and is now unrepresentative, and `infrastructure/ai/configuration.py:173`
  `~/Library/Application Support/FrameNest/ai/config.json` is a C4 default path that no
  exclusion class names and must be added to the written C4 scope.

- **2026-10-02 — Planning prompt issued as `17_planning_00.md`, 661 lines, native
  planning mode, read-only authority, zero Git authority.** Dispatched by the Cooperator to a
  Planning Worker he supplies himself; the Orchestrator used no subagent. Reasoning band
  `High`, the highest issued in this whole, because the deliverable is not a rename but a
  reconciliation of an accepted ten-cut plan against five cuts of evidence.

  **Five corrections to the record are stated as verified, not as suggestions.**
  `Correction 1`: the sequence is **C0 through C9**, and the Orchestrator told the
  Cooperator repeatedly that the whole ends at C7 — `C8` (capture paths with explicit
  restart) and `C9` (delete retired copies, one-way) are not optional tails.
  `Correction 2`: `script.py.mako` belongs to **C3** per the accepted plan, not C4 as the
  Orchestrator stated in the C2d grant and recorded in notes.
  `Correction 3`: `FROZEN_ALEMBIC_SHA256` holds **36 keys**, being revisions `0001`-`0035` plus
  `versions/__init__.py`; session 16 reported 38. `Correction 4`: every NUC state line
  in the accepted plan is stale at `0c850996` against an observed `9c71bfb`. `Correction
  5`: question 14's Fish block is headed `# [MacBook / fish]` and the Cooperator's machine is
  **CachyOS**, so C4 must head it `# [PC CachyOS / fish]`.

  **One suspected plan conflict was investigated and deliberately NOT reported, because it
  does not exist.** The Orchestrator suspected `script.py.mako` might sit inside
  `FROZEN_ALEMBIC_SHA256`, which would have made the C3 instruction to update it
  unsatisfiable. Measured before claiming: the frozen set is 36 keys and does not
  contain `script.py.mako`. Recorded as a worked example of rule 7, since a false alarm
  here would have sent the Planner to re-open a settled question.

  **Eight deficiencies `D-1` through `D-8` are carried by name:** nineteen unverified C2d
  changes with no Python-side agreement guard; the NUC device display name as a data value
  no cut owns, with no product rename verb and `ondelete="RESTRICT"`; the two application
  invariants a raw `sqlite3` write bypasses; the unanswered `libraries.display_name`
  question; two default path components assigned to no cut, including the dev launcher
  macOS and XDG paths and `ai/configuration.py:173`; the stale fixture at
  `test_development_cli.py:175`; the `framenest-chatgpt-page` collision where one token is
  simultaneously a deletable `[project.scripts]` entry and a frozen capture state-directory
  name that a grep sweep cannot distinguish; and the symmetric derivation failures of
  both the Orchestrator and session 16.

  **The earlier "five omitted files" finding is now answered and the answer is machine-**
  **readable.** `EXPECTED_FRAMENEST_BASENAME_PATHS` already enumerates all 20
  brand-named paths by name, including the three credential confs, `framenest.env.example`,
  the off-device units, the catalog export and the five operator scripts. C4 and C7 must
  read them from the ledger rather than reconstruct them from prose, and the prompt
  says so.

- **2026-10-02 — Planning report accepted and archived as `17_report_00.md`, 843 lines.
  Deliverable is a 15-step completion plan: C3-A, C3-B, C4-A, C4-B, C-DATA, C-LOCAL,
  C5, C6, C7-A, C7-B, C8-A, C8-B, C9-A, C9-B, CLOSE. It splits C3, C4, C6, C7, C8
  and C9, adds two work packages no accepted cut owned, and adds a terminal
  read-only CLOSE. Five corrections and eight deficiencies all received decisions.

- **2026-10-02 — The Planner found four errors in MY prompt, all verified by the
  Orchestrator before being accepted.** `73e20ef80b88700d5fc397cd8edd4fc425869f` is **38**
  characters; the real pin is `73e20ef80b88700d5fcbc397cd8edd4fc425869f` at 40.
  The schema uniqueness column is `root_path`, not the `root_root` I wrote.
  The prompt's `FRAMEST_*` typo was caught and named. And I told the Planner that all 47
  residual occurrences lie outside the whole; that is false and the Planner rejected it
  correctly: the seven default path expressions, `script.py.mako` and the live
  mutation-header behaviour all have remaining owners at C4-B, C-LOCAL and C7-A.
  **"Outside C2d" is not "outside this whole",** and the Orchestrator conflated the two.

  **Independently verified against the repository:** exactly **11** revisions import
  `sqlite_batch_fk`, each once — `0016, 0017, 0018, 0023, 0024, 0025, 0026, 0027, 0028,
  0030, 0031` — matching the Planner exactly, so ADR-0085's singular "one applied
  revision" is stale explanatory text. `FrameNestSettings` splits **500 in
  src+tests and 5 in frozen ADRs**, so C3 must not mechanically rename all 505.
  The header count resolves too: the ledger records **73** excluding itself and **74**
  including it, so session 16's 71 was wrong and my 74 was the whole-tree figure.

- **2026-10-02 — MATERIAL: my capture fingerprint verification was measuring the wrong
  thing, and the Planner is right.** `capture_runtime_identity()` at
  `deploy/ubuntu/framenest_release.py:866` computes
  `code_tree = git rev-parse {release_sha}:src/kronika_capture` — the capture subtree
  **of the release under consideration**, not of the installed capture runtime. The value I
  carried and compared across every refresh, `e65422fa…`, is the capture tree of the web
  release `9c71bfb`, compared against itself, so it was **tautological**. The installed
  capture release is `94e605c`, whose capture subtree is `977465503254fe6cdf31673b7e107b9e0487ffe2`
  — a different value, which the Planner derived and the Orchestrator confirmed against
  the repository. The substantive conclusion still holds, because no capture command was
  ever run and the capture release SHA stayed `94e605c` throughout, but the evidence
  was wrong. The helper does have a genuine live probe,
  `cmd_remote_capture_identity()` at line 756, which reads the service payload's `runner_id`
  and `browser_session`; **that has never been recorded in this whole.** Future receipts
  must label target-source identity and installed runtime identity separately, and the next
  NUC window should capture the live pair.

- **2026-10-02 — C3-A implementation prompt issued as `18_implementation_00.md`,
  implementing section 1.3 of the accepted completion plan. E2, one commit, no product file in
  the diff, no publication, no NUC contact.** Before writing it the Orchestrator
  re-measured every input rather than reusing an earlier turn, because three of the last
  three prompts carried an error.

  **Re-derived for this prompt and confirmed:** the AP pin at exactly **40** characters;
  all **19** target sites with their exact current text; the duplicate literal counts,
  `"Kronika is stopped."` **three** times in `development.py` and the category-conflict
  sentence **three** times in `x_acquisition.py` and **once** in `x_request_api.py`; the
  stale fixture `message="FrameNest is running."` at `test_development_cli.py:175`; and
  both negative assertions that must survive, `test_development_launcher.py:64` and
  `test_local_web_application.py:1228`.

  **Resolved the identity-source question by measurement rather than assumption.** The browser
  precedent is `x_companion_extension.test.js:25`, `manifest.name.split(/\\s+/)[0]`, with the
  full display name independently pinned at line 2637. The Orchestrator checked
  whether a Python equivalent already existed and established that **it does not**: every
  Python reference to `manifest.json` is to the release marker
  `.framenest-release-manifest.json`, and the only other two mentions of the extension
  manifest are provenance comments in the ledger. So the Python derivation is genuinely
  new, `tests/conftest.py` exists as the natural helper home, and the prompt requires the
  full-name pin to be a **separate** assertion, since a derived-only guard would still
  pass if the manifest and the product were renamed together.

  **Three properties are required of the guard, because aggregate failure is the defect
  this cut closes:** per-occurrence failure demonstrated for all nineteen without
  substituting a retention-counter failure; an occurrence-level structural check so a
  deleted duplicate cannot make coverage look complete; and behavioural exercise of
  parser output, the individual runtime branches and all four category-conflict paths,
  with any site that genuinely cannot be reached behaviourally declared rather than
  silently downgraded to a textual check.

  **A near-miss recorded honestly.** An Orchestrator probe printed an empty result and
  the label "(prazdne = nie)" suggested no Python test read `manifest.json`. The list was
  in fact non-empty, so the label was misleading and the reading was wrong. Re-running
  without the misleading label is what revealed the references were to the release
  marker. This is rule 9 in a new form: **a probe's own label is not its result**, and it is
  now covered by the requirement to report counting scope.

- **2026-10-02 — Sequence after C3-A, recorded so it is not improvised later:** C3-A,
  then a bounded publication of `09e45e5`, `77bcb81`, `d5955d5` and the C3-A commit, then
  the routine NUC refresh, then **reading the previously unguarded strings by hand from
  the release** as the accepted mitigation for the fact that guarding is not observing, then
  the Cooperator's extension reload and his confirmation of the canonical companion name. Only
  then does C3-B begin. The hand-read is deliberately placed after the refresh so the
  strings are read as the Cooperator actually receives them.

- **2026-10-02 — C3-A ACCEPTED. Commit `e1d5ee510b4a1532606dba7d2a098aed71c16225`,
  parent `d5955d5`, local `main` four commits ahead of public `main`, not pushed. 16 files,
  +1207/−13, and Orchestrator verification confirms **zero non-`tests/` paths in the diff**.
  Python `4359` to `4399 passed` (+40, +0 failures), JavaScript `583/578/5` identical,
  retention `15`, Part A and Part B unmoved.** Both negative assertions at
  `test_development_launcher.py` and `test_local_web_application.py` verified
  byte-unchanged at **0 diff lines**, and the stale `RuntimeStatus` fake is repaired.

  **My issued list of nineteen was short by fifteen, for the fourth time in this
  whole.** The Worker's AST parse resolves **50** brand-bearing runtime literals in
  `src/framenest`: 13 already pinned, 1 the deliberately dual-spelled header, 2
  externally sent prompt bodies, and **34 carrying no assertion anywhere in `tests/`** —
  my nineteen plus both alias API payloads, both loopback refusals, the launcher-error and
  log-unavailable operator strings, five domain validation constants, the health-check
  failure, the server configuration error, the storage-overlap refusal and the Alembic
  connection error. The cause is now understood and recorded: **each previous cut
  demonstrated red-on-revert only for the categories it was pointed at**, so unpinned
  sites outside the pointer were never exercised. All 34 are now guarded, each
  demonstrated red on its own independent mutation, twice, in both directions of wrong
  replacement.

- **2026-10-02 — THE MOST IMPORTANT FINDING OF THIS CUT, confirmed independently by
  construction: the retention ledger is silent, not merely ambiguous, under a
  wrong-brand rename.** Session 16 established that the whole-tree counter cannot say
  *which* occurrence moved. Session 18 established the stronger fact: mutating
  `Kronika` to `Zoneta` at any of the 34 sites left the ledger **green in all 34
  cases**, while every site's own behavioural guard failed. Orchestrator verification of the
  mechanism: `CAPITALIZED_OCCURRENCE_COUNT` and the per-tree counters are keyed to the
  **retired** spelling `FrameNest`, so removing a *current* brand token moves none of
  them. **The ledger detects reintroduction of `framenest`; it cannot detect that the
  replacement is wrong.** For the most likely class of real mistake in this whole, the
  aggregate signal contributes nothing.

- **2026-10-02 — `development.py:273` is unreachable dead text, and that reduces the real
  observation surface by one.** Orchestrator read `development.py:270-290`: the `raise
  DevelopmentRuntimeError("Kronika did not become healthy in time.")` sits inside the `try`
  whose own `except Exception:` catches it, performs cleanup, and returns
  `RuntimeResult(False, status, status.message)` carrying the **`:286`** string
  `"Kronika startup failed. Check logs for details."` instead. The `:273` literal
  can never reach a caller. The Worker marked it structural-only and said so rather than
  faking a behavioural demonstration, which was the correct call. **Consequence: of the
  nineteen, eighteen are genuinely observable product strings and one is internal dead
  text**, so the hand-read mitigation covers eighteen.

  Worker session 18 repeated session 16's error of reporting `FROZEN_ALEMBIC_SHA256` as
  **38** keys. Measured definitively, untruncated: **36** keys, being revisions
  `0001`-`0035` plus `__init__.py`, matching the 36 files in `versions/`. The two
  Implementation Workers independently produced 38 while the Planner and the
  Orchestrator produced 36, which is the signature of a remembered figure rather than a
  measured one — rule 8 failing in the identical place twice.

- **2026-10-02 — PUBLISHED. `git push origin main` fast-forward `9c71bfb..e1d5ee5`, no force,**
  remote confirmed as `https://github.com/cisarik/kronika`. After the push `origin/main`
  equals local HEAD `e1d5ee510b4a1532606dba7d2a098aed71c16225` with divergence `0 0`.
  The four published commits are `09e45e5` C2b, `77bcb81` C2c, `d5955d5` C2d, `e1d5ee5`
  C3-A. 68 files, +1774/-192 in total.

  **Pre-publication checks, all measured before the push rather than assumed.** The
  merge-base equalled `origin/main` exactly, so the push was a strict fast-forward with
  no divergence. **Zero paths matching `kronika_capture` or `capture` appear in the
  diff**, so capture continuity holds by construction rather than by fingerprint. **Zero
  paths matching the Alembic `versions/` directory, `pyproject.toml`, `ap.project.conf`
  or the `.ap` gitlink** appear either, so no migration is added, head stays `0035`, the
  same-schema rule holds and no AP re-gate is required. C3-B owns all of those.

- **2026-10-02 — Capture continuity cannot be verified the way session 17 recommended, and
  the reason is structural.** `_snapshot_capture_identity()` at
  `deploy/ubuntu/framenest_release.py:1726` and the readiness gate at 1744 are called
  **only from `_cmd_capture_transition` at 1770**, the `activate-capture` and
  `rollback-capture` path. **A web deploy therefore never reads capture identity at
  all.** Obtaining the live `runner_id` and `browser_session` pair would require a
  capture transition, which is forbidden without its own grant and which would itself
  restart capture. The `capture_code_tree` that `status` prints is computed from
  `git rev-parse {release_sha}:src/kronika_capture` and is therefore target-source
  identity, not runtime identity.

  **Consequence for this refresh, stated honestly rather than overclaimed:** capture
  continuity rests on three structural facts - zero capture paths in the diff, no capture
  command run, and the capture release SHA still `94e605c` - and **not** on any runtime
  identity measurement. **New finding for C4-A: the release helper should print the live
  `runner_id` and `browser_session` pair in `status`, labelled separately from
  `capture_code_tree`,** so future receipts can carry runtime evidence without a capture
  transition. This is the concrete action item arising from the C2d verification defect.

- **2026-10-02 — PRE-DEPLOY CHECK PASSED, and it surfaced a pre-existing capture
  divergence that must never be described as continuity.** Cooperator-run
  `framenest-release status` reported active and web release `9c71bfb`, capture release
  `94e605c`, service active, database `0035`, backup readiness ready.
  `check --release e1d5ee5` reported `release`, `public_main` and the intended SHA all
  equal, `ap_gitlink` matching the 40-character pin, backup readiness ready, and capture
  bridge protocol 1.

  **The capture divergence, measured.** `git rev-parse 94e605c:src/kronika_capture` is
  `977465503254fe6cdf31673b7e107b9e0487ffe2`, while
  `git rev-parse e1d5ee5:src/kronika_capture` is
  `e65422fa576fa5b9947e7408e6980e56707c72c4`, and `94e605c` **is an ancestor** of
  `9c71bfb`. Capture files therefore changed between the installed capture release and the
  current web release. The delta is **three files, +157/-28, across two commits**:
  the bundled headless `driver.mjs`, the bundled headless `runner.mjs`, and
  `src/kronika_capture/cli.py`.

  **What this does and does not mean.** It does **not** mean the four published commits
  touched capture: they did not, and the capture subtree hash was already `e65422fa` at
  `9c71bfb`, so this web deploy's capture continuity argument stands on that fact plus the
  structural proof that web deploy never reads capture. It **does** mean **the NUC runs
  capture code two commits and 157 lines behind the repository**, including browser-driver
  changes, entirely independent of this logical whole. This independently confirms session
  17's C8-B warning that the retained release and current source already differ in three
  capture files beyond branding. **Any future `activate-capture` would deploy real
  behavioural change and must never be approved as a path-only or identity-only move.**

- **2026-10-02 — WEB DEPLOY COMPLETE AND VERIFIED. The NUC now serves
  `e1d5ee510b4a1532606dba7d2a098aed71c16225`.** Cooperator-run evidence: deploy reported
  `web_release e1d5ee5`; subsequent `status` reported `active_release e1d5ee5`,
  `web_release e1d5ee5`, `release_path /opt/framenest/releases/e1d5ee5...`,
  `service_active active`, `database_revision 0035`, `backup_restore_readiness ready`.

  **The one gate that mattered most passed: `capture_release` is still
  `94e605c17b881461fad3e22fd8c7fca32cb93976`, unchanged across the deploy.** That is the
  first runtime-level confirmation of the structural argument, and it confirms that a web
  deploy does not touch capture. `database_revision` stayed `0035`, so the same-schema
  rule held and no upgrade ran.

  Note what this deployment did **not** prove, so it is not recorded as proved: capture
  **runtime** identity was not measured, because `_snapshot_capture_identity` is reachable
  only from `_cmd_capture_transition` and a web deploy never calls it. Capture continuity
  here is evidenced by an unchanged capture release pointer plus zero capture paths in the
  published diff, not by a live `runner_id`/`browser_session` comparison. The gap stays
  open as a C4-A action item.

- **2026-10-02 — Remaining Cooperator-facing step after this refresh: hand-read the
  operator-visible strings from the deployed release.** This is the mitigation Worker
  session 16 identified and the Orchestrator accepted for the nineteen C2d sites that no
  test could reach; session 18 subsequently guarded thirty-four sites, of which
  `development.py:273` was shown to be unreachable dead text because its `raise` is
  swallowed by an enclosing `except Exception` that substitutes the `:286` message. So
  eighteen strings are genuinely observable. Scope of the hand-read is deliberately
  limited to **operator terminal output**, which is what a person can actually see; the
  API 422 payloads and domain validation constants are exercised behaviourally by the new
  guards and are not hand-readable. Only `--help` renderings and the health probe are in
  scope. **`framenest-dev start` must not be run**, since it would start a second server
  and rewrite launcher state.

- **2026-10-02 — HAND-READ PASS 1: eight of eighteen operator strings verified from the
  deployed release, all correct.** The Cooperator ran `framenest-db --help`,
  `framenest-production --help` and `framenest-dev --help` through the sanctioned gate
  against `/opt/framenest/current/.venv/bin`. Every brand-bearing operator string
  rendered as **Kronika**, and **zero occurrences of the retired spelling appeared in any
  of the three outputs**: `Upgrade the Kronika database to head.`, `Inspect the Kronika
  database revision.`, `Verify the Kronika listener answers a local /health request.`,
  `Run the production Kronika server in the foreground.`, and the `framenest-dev`
  description `Control the local Kronika browser-development server.`

  **The `usage:` lines still read `framenest-db`, `framenest-production` and
  `framenest-dev`, and that is correct at this point, not a defect.** Those are command
  names. C3-B installs the thirteen canonical `kronika-*` commands but deliberately keeps
  thirteen `framenest-*` aliases, and C7-B is the cut that removes them. `check-database-ready`
  carries no brand and was correctly out of scope; its two-line wrapping is the argparse
  wrapping the C3-A Worker described, not a formatting defect.

  **Read-only safety verified before recommending the second pass.** `framenest-dev
  status` reaches `runtime.status()` at `development.py:348`, which calls
  `_status_with_state()` using only `_read_state()`, `_database_state()` and
  `log_path.exists()`. `_database_state()` at line 496 calls
  `inspect_database_migration_status`, **status and not upgrade**, against the
  **development** database path rather than the production catalog, and is wrapped in a
  bare `except` returning `unknown`. `framenest-dev logs` reaches `_print_logs`, which at
  `adapters/cli/development.py:115` prints the log-unavailable message and otherwise only
  reads. Both are therefore safe. **`start`, `stop`, `restart` and `open` remain excluded**:
  the first three mutate launcher state and the fourth opens a browser, which browser
  authority forbids.

- **2026-10-02 — HAND-READ PASS 2 complete, and the Orchestrator corrected its own
  miscount immediately.** `framenest-dev status` returned `Status: stopped`,
  `Database: uninitialized`, `Log: not yet available` and the runtime message
  `Kronika is stopped.` `framenest-dev logs` returned
  `Kronika development log is not yet available.` **Zero occurrences of the retired
  spelling in either output.**

  **Correction of an Orchestrator arithmetic error, recorded rather than quietly fixed.**
  The Orchestrator told the Cooperator this would bring the hand-read to "ten of
  eighteen". It is **six of eighteen**. The five argparse strings are all confirmed, but
  `status` and `logs` together rendered only **one** of the ten `development.py` runtime
  messages, and the log-unavailable string belongs to `adapters/cli/development.py:115`,
  which is one of session 18's fifteen extras rather than one of the original nineteen.
  Accurate position: of the eighteen observable strings, **six are hand-verified and
  twelve remain unobserved** — eight runtime messages reachable only through `start`,
  `stop`, `restart` or `open`, which must not be run, and the four category-conflict
  paths, which need a real API request. This is the second Orchestrator arithmetic or
  scope slip in this logical whole after the truncated inventory, and it is recorded for
  the same reason: the number was stated before it was recounted.

  **Material incidental finding for C-LOCAL.** `Database: uninitialized` shows the NUC
  has **no development catalog** for the service account. Note precisely what this does
  and does not establish: it describes the NUC under the `framenest` account, because
  these commands ran through the gate on the NUC. It says nothing about the Cooperator's
  own machine, which is a separate filesystem context and where any real legacy
  development state would live. C-LOCAL therefore still requires the Cooperator to
  identify his own existing local installations, but the NUC side of that cut is empty.

- **2026-10-02 — COMPANION TRANSITION RECEIPT RECORDED. This is the first rendered
  acceptance in this logical whole.** After the refresh to `e1d5ee5`, the Cooperator
  reloaded the Brave companion and confirmed three results:

  ```text
  1  extension identity   "Kronika X Companion", version 0.2.0    PASS
  2  X attach flow        works end to end                       PASS
  3  retired spelling     not observed anywhere in the panel     none seen
  ```

  This satisfies the acceptance receipt the completion plan requires for the companion
  transition in section 1.12, and it identifies both revisions involved: extension
  `0.2.0` carrying the `Kronika X Companion` manifest, and server `e1d5ee5`.

  **Stated precisely so it is not overclaimed later.** This proves the companion loads,
  presents the canonical name, and can still attach media with both mutation headers
  being sent. It does **not** prove that the retired header spelling has stopped, because
  the extension deliberately still sends both spellings and will until C7-A. The receipt
  is evidence about naming and behaviour, not about header removal, and C7-B's
  precondition on the companion transition remains unsatisfied until C7-A actually runs.

- **2026-10-02 — Nothing is outstanding on the Cooperator side at this point.** The
  question-14 Fish universals were deliberately **not** requested yet: the current gate
  does not read `KRONIKA_NUC_SSH_*` names, because that arrives with C4-A, and the
  completion plan requires those universals to be exported with guarded `set -Ux`
  semantics rather than blind copying. Asking now would produce variables nothing reads.

  **Position in the sequence.** Complete: C0, C1, C1b, C1c, C1d, C1e, C2, C2a, C2b, C2c,
  C2d, C3-A. Repository and NUC agree at `e1d5ee5`. The next cut is **C3-B**, the atomic
  package, distribution and executable identity move, which is the highest-risk cut so
  far: it moves `src/framenest` to `src/kronika`, renames `FrameNestSettings` and its
  500 in-source references, requires the in-memory Alembic alias for the eleven revisions
  that import `framenest.infrastructure.persistence.sqlite_batch_fk`, and forces an AP
  re-gate because `ap.project.conf` changes, which invalidates the current baseline for
  the remainder of that worktree.

- **2026-10-02 — C3-B implementation prompt issued as `19_implementation_00.md`,
  highest-risk cut so far, `High` reasoning band and approximately 500k context.** Every
  input was measured before writing rather than carried forward, because the last three
  prompts each carried an error.

  **Verified mutation targets recorded with their exact current values:** `pyproject.toml`
  name and `packages` entry; **five explicit `src/framenest` include paths**;
  `ap.project.conf` `provenanceModule` and the `runtime-info` argv that imports
  `framenest` and prints `framenest.__file__`; `catalog_backup.py:263` `version("framenest")`;
  `migrations.py:24` `DEFAULT_MIGRATION_PACKAGE`; `migrations.py:121` the single
  `ScriptDirectory.from_config` call site; eight `framenest*` logging identifiers in
  `structured_logging.py`; the three `framenest_umask` occurrences at `engine.py:72,73,76`;
  the `script.py.mako` downgrade message; and `kronika_capture/config.py` lines 7 and 8.
  Console-entry arithmetic measured from the file: fifteen entries today, **twenty-eight**
  after the cut, with `framenest-*` names staying **fourteen** so
  `CONSOLE_SCRIPT_ENTRY_COUNT` must not move.

  **Eight named traps, T1 through T8, each a specific failure mode.** T1:
  `test_chatgpt_page_packaging.py:99` asserts `not any(name.startswith(("kronika/",
  "vendor/")))` and therefore **must be inverted**, not deleted. T2: the five include
  paths, where missing one ships a wheel with no web shell and a **green suite would not
  reveal it**. T3: `docs/adr/0004, 0008, 0009, 0011, 0084` are frozen and reference
  `src/framenest`, so a repository-wide replace breaks Part A. T4: `config.py` lines 7 and
  8 hold the **identical literal with opposite destinations**, so a token-scoped
  substitution gets it exactly backwards. T5: the eleven revisions importing
  `sqlite_batch_fk`. T6: `framenest_umask`. T7: the AP baseline invalidation that forces
  the ordered re-gate. T8: `tests/admin_batch_actions_frontend.test.js` references
  `src/framenest` as a path, so this cut may legitimately touch JavaScript.

  **The Worker is authorised for exactly one commit and must stop there.** Re-gate step 4,
  the root installation refresh inside the canonical `.venv`, is a **Cooperator maintenance
  action** and is explicitly forbidden to the Worker, because step 5 cannot run until the
  environment holds the renamed distribution. The prompt requires the Worker to report the
  exact commands instead of improvising a workaround.

  **Measured correction to the completion plan's own figures:** `FrameNestSettings` now
  occurs **504** times in `src` and `tests`, not the 500 recorded at `d5955d5`, because the
  C3-A agreement guards deliberately reference the retired class name as an inventory
  entry. The five occurrences in `docs/adr` remain frozen and must not be renamed. The
  prompt states this and also restates rule 3, so those references are repointed as part
  of this cut rather than "fixed" as if they were display prose.

- **2026-10-02 — C3-B COMMITTED BUT NOT VERIFIED. Commit
  `76416ce08aefb3c8892fc50f52378459f56e8614`, parent `e1d5ee5`, one commit, not pushed,
  tree clean, 604 files, +4562/-4534.** The cut is **incomplete by construction** and the
  Worker said so rather than substituting weaker evidence.

  **Why no Python ran: trap T7 materialised exactly as predicted.** The AP execution
  envelope validates `provenanceModule` against `sourceRoot` on **every** `ap exec`, and
  `ap exec` requires a `--baseline` whose `ap.project.conf` matches the worktree. The
  instant `src/framenest` ceased to exist, no baseline was valid, so the route closed and
  the AP envelope itself instructed `STOP and report the mismatch; do not repair the
  environment`. Verification items 4, 5, 6, 7, 8, 9 and 12 are therefore **unproduced**:
  no wheel listing, no import-level proof, no fresh-database migration, no unchanged
  `alembic_version` row, no synthetic shim alarm, no entry-point callable identity, no
  `kronika_capture` import proof and no executed retention module.

  **Orchestrator verification, independent of the Worker.** `src/` contains only
  `kronika` and `kronika_capture`; `src/framenest` is absent. Trap T4 resolved correctly:
  `config.py:7` is `APP_NAME = "kronika-capture"` and `config.py:8` is still
  `STATE_DIR_NAME = "framenest-chatgpt-page"`. `KronikaSettings` totals 504.
  `CONSOLE_SCRIPT_ENTRY_COUNT` remains **14**. No ADR appears in the commit.
  **All 36 frozen Alembic revisions verified by SHA-256 against the ledger's own pins:
  36 match, 0 mismatches**, so Part A is intact. **The JavaScript suite was executed by the
  Orchestrator independently of `ap exec`: 583 tests, 578 passed, 0 failed, 5 skipped**,
  confirming the Worker's claim on the one route that never closed.

  **The three surviving `FrameNestSettings` are correct.** All three are provenance
  comments in the ledger at lines 1046, 1057 and 1066, and each narrates that the
  `FrameNestSettings` to `KronikaSettings` rename happened. A comment describing a rename
  must name the old spelling or it becomes factually wrong. The ledger excludes itself
  from every count, so this affects no measurement.

- **2026-10-02 — TWO PROMPT ERRORS CONFIRMED, both against the Orchestrator.** **T8
  undercounted JavaScript by 28 files.** The prompt said "One JavaScript test references
  the old path" and named `admin_batch_actions_frontend.test.js`. Measured: **29**
  JavaScript test files carry `src/framenest` asset paths, 84 changed lines, every one of
  them a pure repath. Executing T8 literally would have left 28 suites reading a path that
  no longer exists. **The `structured_logging.py` line list was also incomplete** - eight
  lines were issued where roughly eighteen coupled occurrences exist across five distinct
  identifier names, including the root-logger key, the `f"framenest.{component}"` logger
  name and the `cls.__name__`/`cls.__module__` literals that make settings redaction work.
  Renaming only the issued lines would have produced a `kronika`-named namespace that no
  longer matched its own handlers.

  **Standing correction adopted: the Orchestrator must stop issuing per-file targets for a
  whole class of change, and must issue the derivation rule instead.** Both failures were
  the same shape as the session 14, 15 and 16 findings - a hand-built list where a
  derivation was required. The C3-B prompt also repeated Correction 5's environment-label
  rule nowhere, and the Worker consequently emitted both Cooperator blocks headed
  `# [MacBook / fish]` for a CachyOS machine. **Every future prompt that emits a
  Cooperator command block must restate the label requirement explicitly.**

- **2026-10-02 — DECISION TAKEN on the unrenamed class hierarchy.** The Worker renamed
  only `FrameNestSettings` and left the `FrameNest*Error` domain hierarchy,
  `FrameNestConfigurationError`, `FrameNestJsonFormatter`, `FrameNestRedactionFilter` and
  `FrameNestLogger` untouched, measuring the residue as roughly **1,423 occurrences across
  about 95 classes**, and flagged the decision explicitly for Orchestrator review. **The
  Orchestrator accepts the narrow scope and defers the hierarchy to a dedicated cut after
  C4-A.** Reasoning: the Cooperator-confirmed membership test places **Python class and
  module names out of scope**, so their retention does not violate the goal; renaming 95
  classes immediately after the highest-risk cut adds risk for no goal compliance; and
  C7 already owns removing old entry points. **The resulting inconsistency is real and is
  recorded rather than glossed** - a module under `src/kronika/` whose domain exceptions
  are `FrameNest*Error` while their user-visible messages already say `Invalid Kronika …`.
  This is named follow-up work, not an oversight.

- **2026-10-02 — C3-B STEP 4 SUCCEEDED; THE AP CONTRACT IS COHERENT. The route reopened
  and the Orchestrator proved it with the cheapest possible command.** The Cooperator ran
  the maintenance block. The `AP route re-opened` and
  `ap exec --baseline 76416ce --operation runtime-info` printed
  **`/home/agile/Projects/kronika/src/kronika/__init__.py`**, proving the renamed
  `provenanceModule` resolves to the moved package. `ap project check --baseline` PASS.
  Both launchers print `Kronika local development launcher`, and both
  `.venv/bin/kronika-db --help` and `.venv/bin/framenest-db --help` exit 0, which is the
  decisive compatibility fact: **the retained alias still resolves after the move**, so
  `relocate_venv_shebangs` and the installed `framenest.service` keep working.

  **Two Orchestrator defects in this exchange, both recorded.** First, the Orchestrator's
  step-0 flag probe was written for bash, not fish: after a line continuation, `and echo`
  was absorbed by `grep` as file operands, so the `--only-root` verdict never printed.
  The Orchestrator stated the flag status as unknown rather than assuming it, and the
  install proved correct regardless, since `poetry.lock` was unchanged and an install from
  an unchanged lock verifies rather than re-resolves. Second, the `ls` verification lines
  produced no output and both `grep -c` lines returned `0` even though the scripts
  demonstrably exist. **The Orchestrator did not guess at that inconsistency** and
  resolved the question by the runtime probe instead, which was unambiguous.

- **2026-10-02 — DEFECT FOUND IN C3-B: the retention re-pin produced invalid Python, and
  it is the only one.** Executing the ledger module fails at collection:

  ```text
  tests/contract/test_kronika_identity_retention.py:444
  EXPECTED_FRAMENEST_CONTENT_PATHS: frozenset[str] = frozenset(
  E   TypeError: frozenset expected at most 1 argument, got 507
  ```

  **Cause, located exactly.** At line 444 the call is followed immediately by 507
  comma-separated string literals and then a bare `)` at line 952. **The enclosing set
  braces are gone**, so the call receives 507 positional arguments instead of one
  iterable. Part B at line 166 retains its braces and is structurally correct, so the
  defect is isolated to this single set. It is a **syntax-level** failure, not a wrong
  value, which means the Worker's shell-measurement values remain unverified rather than
  known-bad.

  **Scope is one error in the entire suite.** `pytest --collect-only` across everything
  reports **exactly one** collection error, this one, with every other module collecting
  cleanly. A 604-file refactor therefore produced a single syntactic defect, and it is the
  two missing braces the Orchestrator identified by reading lines 440-448 and 950-953.

  **Consequence: C3-B needs one correction commit, not a re-do.** The commit itself is
  sound; the ledger file is not. The Worker predicted this exact outcome: *"If
  `test_kronika_identity_retention.py` is the only red, the re-pin method is wrong and
  nothing else needs redoing."* What the correction must also establish is whether the
  **507 re-pinned values** are correct, which cannot be known until the file parses.

- **2026-10-02 — Correction prompt issued as `20_correction_00.md`, bounded to one commit.**
  The defect is a two-line insertion, located exactly by the Orchestrator: `    {` after
  line 444 and `    }` before line 952 of
  `tests/contract/test_kronika_identity_retention.py`, matching the four-space brace and
  eight-space element indentation already used by the correct Part B set at line 166. The
  Worker must re-derive the 507 element count before editing and stop if it differs.

  **The real risk is stated as the primary task, not the syntax.** The braces are the
  visible defect; whether the **507 re-pinned values** are correct cannot be known until
  the file parses, because session 19 measured them by shell and never executed the
  module. The prompt carries every expected value, requires the Worker to re-pin only
  from its own measurement, and explicitly forbids tuning a pin until the suite is green.
  **If a value cannot be reproduced, it must stop and report rather than adjust.**

  **Seven C3-B verification items are owed and are now assigned**, since the route is
  open: wheel or sdist listing with all five re-pathed resources present and `framenest/`
  absent; import-level proof that ordinary `import framenest` fails while the shim
  resolves `sqlite_batch_fk`; fresh migration to `0035` plus a populated fixture with an
  unchanged `alembic_version` row; the synthetic-alarm demonstration without committing
  the synthetic revision; entry-point identity across thirteen canonical and thirteen
  alias names with `framenest-*` still 14; `kronika_capture` importability with
  `STATE_DIR_NAME` preserved; and the retention module itself.

  **Opportunistic fixing is forbidden by name.** A full-suite run will very likely
  surface failures not caused by this cut; the prompt requires each to be reported and
  classified, and permits a fix only for a defect demonstrated to be caused by C3-B. The
  two failures session 19 predicted for the un-step-4 window are called out as ones that
  **should now pass**, so if they still fail that is a real defect.

  **The unrenamed `FrameNest*Error` hierarchy is named in the prompt as out of scope**,
  with its measured residue and its deliberate deferral after C4-A, so the Worker does
  not "helpfully" rename 95 classes inside a correction grant.

  Publication and the routine NUC refresh remain separate grants. The NUC still serves
  `e1d5ee5`, which will be two commits behind local `main` once this correction lands.

- **2026-10-02 — C3-B CORRECTION ACCEPTED, and the reopened route exposed 37 failures that
  C3-B never saw. All 37 classified by the Orchestrator; 36 are test-side, 1 is not.**
  Commit `0eb6e8e562e6c22c3de4038105b84689e9b1c76b`, parent `76416ce`, and its diff is
  **exactly 2 insertions in 1 file** - the two missing set braces - so **no ledger value
  needed re-pinning and Worker session 19's 507 measured values were correct all along**.

  Orchestrator independent verification: the retention module now **executes and passes,
  15 passed**; `runtime-info` resolves `/home/agile/Projects/kronika/src/kronika/__init__.py`;
  and the packaging, import-boundary and reader group passes **76 tests**.

  **One Orchestrator error in this exchange:** the first `ap exec` calls were made with the
  abbreviated SHA `0eb6e8e` and failed with `--baseline must be a full lowercase commit
  object ID`. The Orchestrator had used full SHAs in every earlier command and briefly
  regressed to the short form. Re-run with `git rev-parse HEAD`.

  **The 37 failures, complete and classified:**

  ```text
  23  tests/unit/test_structured_logging.py       getLogger("framenest") returns a
                                                   logger with no handlers: IndexError
   5  tests/contract/test_kronika_product_string_agreement.py
                                                   inventories product strings by
                                                   src/framenest paths; all 50 are now
                                                   "missing" at src/kronika; also looks
                                                   for the frozen revisions under the
                                                   old path
   3  tests/contract/test_uvicorn_logging.py      KeyError 'framenest_json' and
                                                   'framenest_stderr'; production now
                                                   emits kronika_json/kronika_stderr
   2  tests/contract/test_public_published_uds.py  assert 0 == 1 over a moved path
   1  tests/unit/test_configuration.py            getLogger("framenest"), same cause
   1  tests/unit/test_server_runtime.py            same logging-namespace cause
   1  tests/contract/test_workspace_media.py       hardcoded
                                                   src/framenest/.../media_attribution_repository.py
                                                   -> FileNotFoundError
   1  tests/contract/test_kronika_settings_parity.py   SEE BELOW, NOT A RENAME DEFECT
  ```

  **The finding that matters: production code is sound.** Every one of the 36 mechanical
  failures is a test-side reference that C3-B failed to repoint - the same failure mode as
  the 29 JavaScript files in session 19, now on the Python test side. No product defect was
  found. The full suite is `37 failed, 4362 passed, 8 skipped, 2 warnings`.

- **2026-10-02 — ONE FAILURE IS NOT OURS TO FIX AND IS ESCALATED TO THE COOPERATOR.**
  `tests/contract/test_kronika_settings_parity.py:253`, inside
  `test_the_settings_library_is_unchanged_since_the_restoration_reference`, asserts that
  `pyproject.toml` at HEAD is **byte-identical** to
  `RESTORATION_REFERENCE = 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`, which is the **C0
  commit, the first commit of this logical whole**. The test's own docstring reads: *"The
  oracle is licensed only while the library matches the older commit."* `poetry.lock` still
  matches; `pyproject.toml` no longer does, because **C3-B legitimately changed the
  distribution name, the package declaration and the script table.**

  **This is a licensing condition, not a code defect.** Repointing or deleting that
  assertion could circumvent the terms under which `pydantic_settings` is used, and it is
  therefore **outside any Worker's authority and outside the Orchestrator's to decide
  alone.** It is escalated to the Cooperator with the exact reference commit named.

- **2026-10-02 — THE LICENSING ESCALATION WAS A FALSE ALARM, and the Orchestrator
  withdraws it. The failure is an over-broad assertion, not a licence condition.**
  Evidence, all measured before any conclusion:

  ```text
  pyproject.toml:253 context   the constant's own comment reads
    "#: Published `main` at the moment the restoration was scoped; the behaviour the
        dual-prefix cut must not change for old-spelling-only input."
    -> it is a behavioural baseline for the dual-prefix cut, not a licence oracle

  test docstring              "The oracle is licensed only while the library matches
                                the older commit."
    -> "oracle" is used in the testing sense, a reference implementation used as a
       measuring standard, and "licensed" in the sense of permitted, not licensed under
       a licence. The Orchestrator misread both senses and raised a false alarm.

  poetry.lock in C3-B diff    0 files. The lock is byte-identical.
  pydantic-settings version   still 2.14.2 in poetry.lock, and pydantic_settings.VERSION
                               equals it, so the test's first library assertion passes.
  C3-B pyproject.toml diff    distribution name and script entry points only. No library
                               version, no dependency specifier, no source of any kind.
  ```

  **Therefore the test's own stated purpose is still satisfied**: the settings library has
  not changed since the restoration reference. What fails is its **third** assertion, that
  the whole of `pyproject.toml` is byte-identical to the reference commit. **That
  assertion is strictly broader than the test's name and docstring**, which claim only
  that the *library* is unchanged. C3-B changed the manifest's identity, not its
  libraries, so it invalidated a stronger claim than the test was making.

  **The correct fix is to narrow the assertion, not to move the reference commit and not
  to delete it.** Moving `RESTORATION_REFERENCE` forward would silently discard the very
  baseline the dual-prefix parity evidence rests on. The Orchestrator's escalation is
  withdrawn, the failure returns to the ordinary defect class, and **no Worker or Cooperator
  licence question exists here.**

  **Recorded as a process lesson, because it is the second time this Orchestrator raised
  an alarm that measurement dissolved.** In both cases the answer came from reading the
  artefact's own stated intent before acting on a keyword. The corrective is now standing
  practice: **when a keyword suggests a legal, security or irreversible condition, read
  the artefact's own definition of that keyword before escalating it.**

- **2026-10-02 — Correction prompt issued as `21_correction_00.md`, bounded to one commit.**
  It closes all 37 C3-B test-side failures and **applies the Orchestrator's own standing
  lesson by issuing a derivation rule rather than a site list**, because sessions 14, 15,
  16 and 19 each found omissions of exactly that shape. The confirmed inventory is
  supplied explicitly as a **sample to reconcile against**, and the prompt requires the
  Worker to report every moved-name site that **no failing test exercises**, since a site
  in a skipped test or an untaken branch is precisely how this defect class survives.

  **The verified production names are given as the substitution authority**, so the
  Worker never guesses: root logger `kronika` at `structured_logging.py:138`, component
  logger `f"kronika.{component}"` at line 152, handler `kronika_stderr`, formatter
  `kronika_json`, package directory `src/kronika`. The **frozen class-name residue is
  listed explicitly as names that must NOT be touched** - `FrameNestLogger`,
  `FrameNestJsonFormatter`, `FrameNestRedactionFilter`, `FrameNestConfigurationError` and
  the `FrameNest*Error` hierarchy - so the Worker does not "helpfully" rename them inside a
  correction grant.

  **Rule 3 has a named live application**, because two kinds of hit in this area look like
  moved-name sites and are not: the negative assertions that the retired spelling is
  absent, and the **provenance comments in the ledger** at lines 378, 1046, 1057 and 1066
  which narrate what earlier cuts did and must keep the historical spelling of
  `FrameNestSettings` and `logging.getLogger("framenest")`.

  **The settings-parity instruction is precise about both prohibited moves**: do not
  advance `RESTORATION_REFERENCE`, which would discard the baseline the dual-prefix parity
  evidence rests on, and do not delete or skip the assertion, which would leave the
  library pin unproven. The Worker is told to narrow it to what the test's own name claims
  and to stop and report rather than choose if that cannot be done without weakening the
  library pin.

  **Orchestrator grouping error caught before the prompt was written.** An initial
  attribution placed `test_server_runtime.py` with the `getLogger` cause and
  `test_public_published_uds.py` among the hardcoded-path sites. Both were wrong: the
  former fails on `KeyError: 'framenest_json'` at line 185 and carries its own
  `SOURCE_ROOT = Path("src/framenest")` at line 25, and the latter contains **zero**
  occurrences of `src/framenest` and fails because it compares `record.name` against
  `framenest.public_published_api` and `framenest.public_published_application` while
  production now emits `kronika.<component>`. The corrected grouping is what the prompt
  carries. This is the third time in this whole a hand-built attribution was wrong and
  direct measurement corrected it.

- **2026-10-02 — C3-B FULLY VERIFIED AND ACCEPTED. Commit
  `6e89328640fe5477e08f17f4c31c9fc4bf261238`, parent `0eb6e8e`, 9 files, +88/-24, and
  **zero `src/` paths in the diff.** Independent Orchestrator verification:

  ```text
  Full declared Python suite   4399 passed, 8 skipped, 3 warnings, 0 failed
  JavaScript suite             583 total, 578 passed, 0 failed, 5 skipped
  Retention + settings parity  38 passed
  moved-name sites             16 -> 0
  frozen-name sites            75 -> 75, untouched
  ```

  **The Python count is the meaningful number.** It is **exactly 4399, the pre-move
  baseline at `e1d5ee5`**, with no tests added and none lost. That proves the C3-A
  agreement guards followed the package rename automatically, because the brand they
  assert is derived from the extension manifest rather than spelled. The C3-A design
  decision - derive the identity, never hardcode it - is what made a 604-file rename
  verifiable without rewriting a single guard.

  `RESTORATION_REFERENCE`, the `poetry.lock` byte-identity assertion and the first two
  assertions of the settings-parity test are all untouched, confirmed by the commit diff.
  The narrowed assertion now parses both manifests, extracts the single declared
  `pydantic-settings` requirement from each, and compares those exactly, which is the
  constraint that decides which version the lockfile may resolve to. That preserves the
  library pin while allowing an identity cut to rename the distribution.

- **2026-10-02 — THE STRONGEST FINDING OF THIS CUT: four import-boundary guards were
  passing VACUOUSLY, and only the derivation rule found it.** Every one of the 37
  failures was attributed by Worker session 21 with **no unexplained remainder**, and the
  derivation found **four sites that fail nothing at all**: two `SOURCE_ROOT =
  Path("src/framenest")` constants, one `["framenest_redaction"]` key masked by an
  earlier `KeyError`, and one module docstring. The two `SOURCE_ROOT` constants feed four
  whole-tree guards:

  ```text
  test_structured_logging.py:419  test_no_third_party_structured_logging_module_imported
  test_structured_logging.py:436  test_production_logging_imports_confined_to_...
  test_server_runtime.py:295      test_production_uvicorn_imports_are_confined_to_...
  test_server_runtime.py:367      test_fastapi_imports_remain_confined_to_adapters_api
  ```

  Each iterated a directory that no longer existed, so each passed while checking
  nothing. **A fix-the-failings approach would have left all four vacuous**, and they
  would have silently permitted a third-party logging import, an out-of-module uvicorn
  import or a misplaced FastAPI import for the rest of the programme. **This is the
  concrete payoff of the Orchestrator issuing a derivation rule instead of a site list**,
  and it retroactively justifies that decision four prompts after two of its own
  hand-built lists were found incomplete.

- **2026-10-02 — PUBLISHED. `git push origin main` fast-forward `e1d5ee5..6e89328`, no
  force, divergence `0 0`.** Public `main` is now
  `6e89328640fe5477e08f17f4c31c9fc4bf261238`, equal to local `HEAD`. The three published
  commits are `76416ce` C3-B, `0eb6e8e` the brace correction and `6e89328` the test-side
  repoint.

  **Two pre-publication surprises were investigated rather than assumed away, and both
  turned out correct.** The occurrence count of paths matching `capture` was **1**, not 0
  as in the previous publication, and the count matching `alembic_environment/versions`
  was **36**, not 0.

  The 36 are the moved revision files, and their bytes are unchanged: the Orchestrator had
  already verified all 36 SHA-256 pins individually at `0eb6e8e`, and the earlier
  grep matched both the old and the new directory path.

  The one capture path is `src/kronika_capture/config.py`, changed by exactly **one line
  added and one removed**, which is the authorised `APP_NAME` change required by the
  accepted plan: *"Make CLI parser program names canonical, including capture's
  `APP_NAME = "kronika-capture"`. Leave capture's `STATE_DIR_NAME` untouched."*

  **Trap T4 is now definitively resolved, and the independence is structural, not
  incidental.** `APP_NAME` is referenced only at `cli.py:67` as `prog=APP_NAME` and at
  `cli.py:72` in the `--version` string. `STATE_DIR_NAME` is referenced only at
  `paths.py:40` as `base / STATE_DIR_NAME`. **The two constants share a value but no
  code path**, so renaming `APP_NAME` cannot move the capture state directory.

  **Deployment consequence, recorded so it is not re-derived later.** The capture running
  on the NUC is release `94e605c`, whose `APP_NAME` is still the former value, and a web
  deploy does not touch capture. So the running capture's program name and `--version`
  output are unchanged by this publication; the canonical `kronika-capture` identity only
  appears when C8-B activates a new capture release, which is exactly what C8-B exists to
  do and to do as a separately reviewed delta.

- **2026-10-02 — PRE-DEPLOY CHECK PASSED for `6e89328`, and the capture fingerprint moved
  for a legitimate single-line reason that was verified rather than explained away.**
  Cooperator evidence: `release`, `public_main` and the intended SHA all equal;
  `ap_gitlink` matches the 40-character pin; `ap_archive_sha256` byte-identical to the
  previous check, confirming the AP submodule is untouched; `backup_restore_readiness
  ready`; `current_release` still `e1d5ee5`, correctly, because no deploy has run;
  `capture_release` still `94e605c`; `database_revision 0035`.

  **`capture_code_tree` changed from `e65422fa…` to `cb61ef7d…`, and the Orchestrator
  verified the exact cause.** `capture_code_tree` is
  `git rev-parse {release_sha}:src/kronika_capture`, so it tracks the **target source** of
  the release being considered. The Orchestrator measured both ends:

  ```text
  e1d5ee5:src/kronika_capture   e65422fa576fa5b9947e7408e6980e56707c72c4
  6e89328:src/kronika_capture   cb61ef7df481b823647f8c3687b01fc06fe18e0c   matches check
  delta between them            exactly 1 file, +1/-1
  -APP_NAME = "framenest-chatgpt-page"
  +APP_NAME = "kronika-capture"
  ```

  **Three distinct capture values must now be labelled separately in every future receipt,
  and conflating them is the exact defect this whole already made once:**

  ```text
  target-source capture subtree at e1d5ee5   e65422fa…   superseded
  target-source capture subtree at 6e89328   cb61ef7d…   what check reports
  installed capture release                   94e605c     what is actually running
  installed capture subtree at 94e605c        9774655…    what is actually executing
  ```

  The fingerprint moved because the **repository** changed by one authorised line. The
  **running** capture is untouched and will remain so, because a web deploy does not read
  capture identity at all.

- **2026-10-02 — WEB DEPLOY COMPLETE AND VERIFIED at
  `6e89328640fe5477e08f17f4c31c9fc4bf261238`.** Cooperator evidence: `active_release`,
  `web_release` and `release_path` all at the intended SHA; `service_active active`;
  `database_revision 0035`, so the same-schema rule held and no upgrade ran;
  `backup_restore_readiness ready`; **`capture_release` still
  `94e605c17b881461fad3e22fd8c7fca32cb93976`, unchanged**. This is the second consecutive
  runtime confirmation that a web deploy does not touch capture.

  **One line in the output was investigated rather than glossed over:**
  `framenest-release: existing remote lock or recovery state`. The Orchestrator traced it
  to `framenest_release.py:1345-1350`, where the deploy gate is

  ```python
  try:
      ssh(runner, **transport, remote_command=cmd_remote_mkdir_deploy_dir())
  except ReleaseError as exc:
      raise ReleaseError("existing remote lock or recovery state", EXIT_EXISTS) from exc
  ```

  and `cmd_remote_mkdir_deploy_dir()` at line 363 is
  `sudo -n mkdir -m 0700 {REMOTE_DEPLOY_DIR}` — **`mkdir` without `-p`**, so it fails when
  the directory already exists. The exact sequence of invocations was **not** determinable
  from the output, and the Orchestrator deliberately did not invent one.

  **The final state is independently confirmed correct by the `status` block**, so no
  outcome is in doubt. What the investigation established is a **real operational hazard,
  recorded for C4-A**: the deploy directory is removed in an `except` branch at lines
  1526-1531 and in a **`finally`** at lines 1683-1685, so it is cleaned on both success and
  failure — **but the gate is at line 1346 and the `finally` is at line 1683**. A deploy
  interrupted between the two therefore leaves the directory behind, and **every later
  deploy then fails at `EXIT_EXISTS` with no self-healing path**, because the abort happens
  before the cleanup handler is ever established. There is no stale-state inspection and
  no recovery command for it. C4-A already owns adding explicit migration locking, a phase
  journal and exact-object recovery, and **this is the concrete first requirement to hand
  it**: the deploy gate must distinguish an interrupted run from a concurrent one, and must
  be able to reclaim its own prior lock safely.

  No extension reload is required after this deploy. The companion has not changed since
  `e1d5ee5`, and the receipt for `Kronika X Companion` version `0.2.0` with a working X
  attach stands unchanged.

- **2026-10-02 — C4-A implementation prompt issued as `22_implementation_00.md`,
  `High` band and approximately 450k context, bounded to one commit, zero NUC
  authority.** Every input was measured before writing, and two of the measurements
  corrected the accepted plan.

  **Correction 1 — the installed-unit guard does not exist.** The accepted plan says C4
  would *add* the guard to the paths that switch the web pointer. Measured:
  `rg 'ExecStartPre|ExecStart' deploy/ubuntu/framenest_release.py` returns **nothing**. No
  such guard exists anywhere. This matters more than a wording correction, because C7
  deletes the `framenest-*` entry points while the host still runs `framenest.service`
  whose `ExecStart` names `framenest-production`; **without this guard that deploy would
  switch the pointer and restart onto a release whose executable is absent.** C4-A
  therefore creates the mechanism that makes C7 safe to deploy, and the prompt states
  that dependency explicitly.

  **Correction 2 — C1's marker compatibility is half-delivered, now located precisely.**
  The constants at `framenest_release.py:43-49` know both spellings, but call sites at
  **lines 547, 548, 1665 and 1783 hardcode the former spelling as a literal** rather than
  using the constants, and `read_optional_release_sha` is called at **1249, 1535 and
  1687**. So probing recognises both names while later readers open only the old
  filename. C5's precondition of complete installed readers is therefore not met today.

  **Correction 3 — the analysis filter hides data, and there are TWO constants, not one.**
  `_successful_generic_predicates()` at
  `src/kronika/infrastructure/persistence/companion_review_repository.py:789-793` ends
  with `media_analysis_runs.c.result_schema_version == RESULT_SCHEMA_VERSION`. The
  constants are `RESULT_SCHEMA_VERSION` at `domain/media_analysis_runs.py:21` and
  `MOVIE_IDENTIFICATION_RESULT_SCHEMA_VERSION` at `domain/media_classification.py:114`.
  Both are written into the database, so C5's writer change would make this filter match
  only new rows and **hide every historical successful analysis from the companion
  inbox**. The prompt requires derivation of the full comparison set rather than a fix at
  that one line.

  **The deploy-lock hazard is written in as its own in-scope item** with the measured
  mechanism: `mkdir` without `-p` at line 363, the gate at 1346, cleanup in `except` at
  1526 and `finally` at 1683, so an interrupted run wedges every later deploy at
  `EXIT_EXISTS` with no self-heal. The requirement is ownership plus liveness, never a
  blanket delete, and **refusing is an acceptable outcome while silently deleting a live
  lock is not** - that is stated as an explicit stopping condition.

  **Derivation discipline carried forward.** The prompt issues the derivation rule and
  marks the site list a sample, and records that rule 8's corrected value is 36 frozen
  keys. It also records that sessions 14, 15, 16, 19 and 21 each found omissions when
  the Orchestrator issued a hand-built list, and that one of those left **four
  import-boundary guards passing vacuously**.

  **The deferred `FrameNest*Error` residue is excluded by name and count** so the Worker
  does not rename roughly 1,423 occurrences across about 95 classes inside a release cut,
  and `RESTORATION_REFERENCE` and `poetry.lock` are protected explicitly. The prompt's
  acceptance note also flags that the canonical gate name lands while the Cooperator's
  `KRONIKA_NUC_SSH_*` universals are unset, and that **nothing breaks on publication
  day** because the old path and old variable names keep working until C7-B.

- **2026-10-02 — C4-A ACCEPTED. Commit
  `b16ea2c719f46e167c579c34ddd87a915b70cb00`, parent `6e89328`, one commit, not pushed,
  23 files, +4856/-2448.** Orchestrator independent verification: `EXIT_MARKER_CONFLICT =
  24` and `EXIT_UNIT_EXEC_GUARD = 25` exist; **all 36 Alembic revisions match their SHA-256
  pins; host constants are unchanged** (`SERVICE = "framenest.service"`,
  `SERVICE_USER = "framenest"`, `/opt/framenest/releases`, `/opt/framenest/current`,
  `/opt/framenest/capture-current`, `/etc/framenest/framenest.env`); both entry points and
  both gate paths exist; and `deploy/ubuntu/framenest_release.py` still exists as the
  retained alias.

  **One number is taken on report and not verified: the Python count of 4493 passed.**
  The Cooperator aborted the twelve-minute suite run, and the Orchestrator did not re-run
  it. Everything else in this acceptance is independently measured. The JavaScript
  count, 583/578/0/5, was verified by the Orchestrator at the previous commit and this cut
  touches no JavaScript.

- **2026-10-02 — THE ORCHESTRATOR'S PROMPT CONTAINED A DIRECT CONTRADICTION, and the Worker
  caught it.** The prompt required both "Part A and Part B must not move" and "move the
  engine to `deploy/ubuntu/kronika_release.py`". **Those cannot both hold**, because
  `deploy/ubuntu/framenest_release.py` **is a Part B path** - confirmed by the Orchestrator:
  it appears twice in `EXPECTED_FRAMENEST_BASENAME_PATHS`, and deleting it would remove a
  Part B entry. The Worker resolved it the conservative way, by keeping a 49-line retained
  alias that `os.execv`s the canonical engine, which satisfies Part B and follows the
  pattern the same prompt mandates for the other two renames. **The Orchestrator accepts
  that resolution and records the prompt error as its own.** The alias costs one dead file
  and carries its own namespace copy, so `monkeypatch.setattr` on the retained name
  silently does nothing; the Worker repointed the source-contract test to the canonical
  module and documented the semantics.

- **2026-10-02 — A SECOND WORKER-FOUND ERROR IN THE SAME PROMPT: the affected reader set
  was misdescribed.** The prompt said the schema equality filter hides rows "from the
  companion inbox". Measured: that predicate gates `_load_history_page` and
  `_require_eligible_run`, so the affected surface is **run eligibility and opening, not
  inbox listing**, and the repository's own test asserts a `not-v1` row *is* in the inbox
  list. The defect and the fix are unchanged, but **an acceptance check written against
  the inbox would have passed both before and after the fix and proved nothing.** This is
  the third consecutive cut in which the Orchestrator's own description of a defect was
  partly wrong and only measurement caught it.

  **A third prompt defect, disclosed by the Worker as a negative-authority breach:** the
  Orchestrator wrote that the worker gate is forbidden "in any mode". The Worker ran
  `--probe` and `--help` outside the harness and disclosed it. **The wording was
  over-broad and the Orchestrator owns it:** `--probe` attaches a local agent and prints
  one line, opens no SSH session, contacts nothing and mutates nothing, so it is not NUC
  contact. The intent was "no NUC contact", and that intent was never violated. **No
  adverse consequence, and the run is what exposed the hermeticity defect below.**

- **2026-10-02 — THE STRONGEST FINDING OF THIS CUT: three gate tests were green for the
  wrong reason, because the Cooperator's personal Fish configuration supplied the
  variables.** The retained gate wrapper re-execs its target through the target's shebang,
  which starts a new `fish` that does **not** inherit `--no-config`. So during tests, the
  Cooperator's own `~/.config/fish/config.fish` supplied `FRAMENEST_NUC_SSH_*`, and **the
  gate silently passed with exit 0 where the contract requires exit 2 for a missing
  target.** Three baseline tests were therefore vacuous. The Worker fixed the harness by
  pointing `HOME`, `XDG_CONFIG_HOME` and `XDG_DATA_HOME` at a synthetic per-test root, and
  **deliberately did not force `--no-config` inside the wrapper**, because that would
  change production behaviour for an operator whose variables legitimately come from
  `config.fish` - a change he was not authorised to make and could not verify.

  **This is a second instance of the same class as the four vacuous import-boundary guards
  found in session 21: a test that passes while checking nothing.** It also means the
  Orchestrator's own earlier gate invocations in this whole were working with values
  supplied by the Cooperator's personal configuration rather than by a declared mechanism,
  which is worth remembering when the question-14 universal migration is planned.

- **2026-10-02 — ACTION REQUIRED BY THE COOPERATOR BEFORE THE NEXT DEPLOY, and it is a
  hard blocker.** The deploy lock is now reclaimable, but **only when the lock carries an
  ownership record naming this workstation, older than the 60-second bound, with a dead
  pid.** The lock the Orchestrator observed earlier **predates that mechanism and has no
  owner record**, so the new code will **refuse** it rather than reclaim it - which is the
  correct safe outcome, and it means **the next routine deploy will still stop at
  `EXIT_EXISTS`** until an operator removes `/run/framenest-release-deploy` under its own
  bounded authority. The Worker named this as his smallest next step, alongside one
  read-only `systemctl show --property=ExecStart --property=ExecStartPre framenest.service`
  so that the new guard's systemd parse sees real host output before the cut is installed.
  **Both actions close real risks and neither is authorised yet.**

- **2026-10-02 — NEW WORK ITEM REQUESTED BY THE COOPERATOR: clean-install documentation
  for a fresh Ubuntu NUC.** He intends to reinstall the NUC from scratch so that the host
  identity is fully Kronika - the SSH target becomes `kronika-nuc` rather than its current
  former-spelling name, and Tailscale is renamed completely - and he wants **documentation,
  not scripts**, because he will perform the Ubuntu installation himself. He explicitly
  deferred it: first finish removing the retired identity from the repository. **Captured
  here so it is not lost.** Two related host-side residues were disclosed by him and are
  **not recorded with their values**: his operator SSH identity file name still carries the
  former spelling, and his canonical transport variables currently arrive through shell
  exports in a user dotfile rather than through the universal-variable mechanism the plan's
  question 14 assumed. Both belong in the clean-install document and in the C7-B window
  respectively.

- **2026-10-02 — C4-B implementation prompt issued as `23_implementation_00.md`, `High`
  band, approximately 500k context, one commit, zero host authority.** Every input was
  measured before writing, and the measurements produced three things the accepted plan
  and the Orchestrator's own earlier notes got wrong or understated.

  **`migrate-identity` does not exist.** The plan allocated it to "C4", and the C4-A
  prompt assumed it would be added there. Measured: no `migrate-identity` reference exists
  anywhere. **C4-B creates it**, which makes this cut the point at which C6 becomes
  executable at all.

  **The environment transformation is the item most likely to be done wrongly, and the
  evidence is concrete.** `deploy/systemd/framenest.env.example` carries the former
  spelling in its **values**, not only in its key prefixes: the database path, the gallery
  preview cache, the cover storage root, the cover thumbnail cache, the AI config path,
  four catalog backup roots, the YouTube acquisition root and the UDS path all name
  `/var/lib/framenest`, `/var/cache/framenest` or `/run/framenest` directly. **Changing
  prefixes alone leaves every one of them on the former paths.** The prompt requires a
  typed transformation that classifies each key as path-bearing or opaque, with the
  measured key list quoted, and names `/mnt/framenest-catalog-offdevice` as a frozen
  residue that must never be renamed.

  **The Part B contradiction is resolved by an explicit rule rather than left to
  judgement.** Cut C4-A's prompt demanded both "Part B must not move" and a rename of a
  Part B path, and the Worker correctly refused to satisfy both. The rule is now stated
  precisely: **adding** a canonical artifact whose basename carries no retired spelling
  does not move Part B, while **removing or renaming** an existing Part B path does.
  C4-B therefore creates counterparts and retains every existing artifact, and the
  acceptance check is that **Part B still measures exactly 20**.

  **Two host facts were verified and are quoted so the canonical units are written
  against reality.** The installed web unit names a console script inside `.venv/bin`
  directly in both `ExecStartPre` and `ExecStart`, with `check-database-ready` and
  `serve` as **arguments**, so C4-A's guard resolves it cleanly to
  `framenest-production` with no interpreter-wrapper form to misparse. And capture units
  are **already `kronika-capture-*`**, so capture identity is asymmetric with web identity
  today and already correct; the prompt forbids "uniformising" it.

  **The prompt carries the derivation discipline and the corrected counts**, records that
  five sessions found omissions from hand-built lists, requires failure injection after
  every phase with explicit assertions for preserved UID/GID, no second service account
  and no capture restart, and requires the pre-write versus post-write recovery
  distinction to be shown on both branches. The outstanding C4-A host items - the stale
  owner-less deploy lock and the unverified `systemctl show` parse - are named as
  preconditions for the C6 window, **not** for this cut. The Cooperator's clean-install
  documentation request is named at the end as explicitly **not** part of this cut.

- **2026-10-02 — C4-B ACCEPTED. Commit
  `ed5bcb481749f5a732170fd967efc5a2f940cae2`, parent `b16ea2c`, one commit, not pushed,
  16 files, +4478/-187.** Orchestrator independent verification: all 36 Alembic revisions
  match their SHA-256 pins; **`git diff --diff-filter=D` is empty, so nothing was removed
  and Part B could not have moved**; Part B extracts to exactly **20**; `migrate-identity`
  exists with `_cmd_migrate_identity`; the canonical units are fully canonical
  (`User=kronika`, `Group=kronika`, `/opt/kronika/current`,
  `EnvironmentFile=/etc/kronika/kronika.env`, `kronika-production serve`,
  `StateDirectory=kronika`); `kronika.env.example` carries **canonical values**
  (`KRONIKA_DATABASE_PATH=/var/lib/kronika/catalog.sqlite3`,
  `KRONIKA_COVER_STORAGE_ROOT=/var/lib/kronika/covers`); and the **single** surviving
  former-spelling occurrence in that template is the **frozen off-device mount comment**,
  which is exactly where it belongs. **Zero product capture files changed**; the one
  `kronika_capture` path in the diff is a test file. `STATE_DIR_NAME` is unchanged and
  `APP_NAME` remains `kronika-capture`.

  **Taken on report, not verified: the Python count of 4587 passed.** The Orchestrator did
  not run the twelve-minute suite. JavaScript `583/578/0/5` was verified at the
  predecessor and this cut touches no JavaScript.

- **2026-10-02 — A THIRD PROMPT SCOPE ERROR, and the Worker caught it himself.** The
  accepted plan's section 1.6 says C4-B prepares *"web, backup and optional off-device
  units; environment template; credential drop-ins; export script; **and affected operator
  scripts**."* The Orchestrator's prompt section 3 listed **only the eleven `deploy/`
  artifacts** and omitted the operator scripts. The live Part B set contains **five**
  `scripts/operator/` paths whose canonical counterparts were therefore not created:

  ```text
  scripts/operator/infosec/framenest_log_triage.sh
  scripts/operator/infosec/framenest_public_surface_check.sh
  scripts/operator/infosec/framenest_socket_permissions_check.sh
  scripts/operator/network/framenest_mullvad_egress.fish
  scripts/operator/network/framenest_mullvad_egress.sh
  ```

  **The Worker reconciled against the Orchestrator's sample, found zero differences, and
  then separately flagged that the sample itself disagreed with the plan.** That is the
  correct behaviour and it exposes a meta-lesson now recorded: **reconciling against the
  Orchestrator's sample is only as good as the sample**, so a derivation must be
  reconciled against the plan as well as against the issued list.

  **Decision: the five operator-script counterparts are assigned to a dedicated bounded
  cut that must complete before C7-B.** They are workstation operator diagnostics rather
  than NUC web layout artifacts, so they do not gate C6, and creating them by mechanical
  copy inside C4-B would have been provisioning-by-copy as the Worker argued. But C7-B
  removes old entry points, so the canonical counterparts **must exist before C7-B**, and
  this is now a named obligation rather than a lost finding.

- **2026-10-02 — The Worker added three dead builders and reported them rather than hiding
  them:** `cmd_remote_switch_layout_release`, `cmd_remote_unit_enabled_state` and
  `migration_unit_required`, each with no caller and no test. **Recorded as a real, minor
  defect to be removed in the next cut that touches `kronika_release.py`.** The Worker's
  stated reason - that removal was impossible inside one non-amended commit - is not
  strictly true, since removal could have preceded the commit, but the disclosure is
  honest and the residue is harmless.

  **Two other deviations are accepted as sound.** The `apply` confirmation is
  `--yes` **plus** a required `--preflight-digest` binding apply to the exact validated
  plan, which is stronger than the plan required. And the narrow sudo rule is copied from
  the installed instance and validated with `visudo -cf` rather than authored, because its
  content is not in the repository - correct, since authoring it would be provisioning
  authority the cut does not have.

  **A genuine C6 blocker was found and fixed during derivation rather than after
  deployment.** The transferred `_remote` extract and relocate helpers validated every
  path against the single former release root, so after C6 they would have **refused the
  canonical `/opt/kronika/releases/<sha>` path on the host with no layout to select
  from**. Fixed with `accepted_release_roots()`, read at call time so C6's constant change
  needs no second edit. This is the second consecutive cut whose derivation prevented a
  host-side failure.

  **The outstanding C4-A read-only probe is now more important, and its scope has grown.**
  The layout selector consumes `systemctl show` properties (`LoadState`, `ActiveState`,
  `UnitFileState`, `User`, `Group`, `WorkingDirectory`, `ExecStart`) that have never been
  observed on the NUC, and both the C4-A guard and the layout selector parse them.
  **One read-only Cooperator command can now close both risks at once**, which the
  Orchestrator will consolidate into a single bounded probe before C5 or C6.

- **2026-10-02 — DECISION CONFIRMED by the Cooperator: the five operator-script canonical
  counterparts get their own bounded cut before C7-B.** He chose the dedicated cut over
  folding them into the C6 window and over leaving them as permanent residues. Recorded
  as a **named obligation**, not a note: the counterparts must exist **before C7-B removes
  the old entry points**, and they are **not** a C6 precondition because they are
  workstation operator diagnostics rather than NUC web layout artifacts.

- **2026-10-02 — THE STALE LOCK IS NOW AN IMMEDIATE BLOCKER, NOT A FUTURE RISK, and the
  sequence must change because of it.** Cut C4-A added the reclaimable deploy lock. The
  helper the Cooperator runs is the **checkout's**, so the next deploy already executes the
  new lock logic. That logic requires an ownership record naming this workstation, older
  than the 60-second bound, with a dead pid. **The lock currently present on the NUC
  predates the mechanism and carries no owner record, so the new code will REFUSE it with
  `existing remote lock without readable ownership` and exit `EXIT_EXISTS`.** The next
  deploy therefore cannot succeed until that directory is removed under its own bounded
  authority. This is the safe behaviour working as designed, and it is now the first item
  in the sequence.

  **The outstanding C4-A read-only probe has also grown in scope and now closes two risks
  at once.** Cut C4-A's installed-unit guard parses the `path=` field of effective
  `ExecStart` and `ExecStartPre`. Cut C4-B's layout selector additionally parses
  `LoadState`, `ActiveState`, `UnitFileState`, `User`, `Group` and `WorkingDirectory`.
  **Neither parse has ever seen live systemd output from this host.** One read-only
  `systemctl show` invocation covering all of those properties closes both, and it must run
  before anything depends on either parse. The Worker's LEAD named a value such as
  `enabled-runtime` or an unfamiliar output dialect as the plausible failure, whose effect
  would be a **refused routine operation rather than a wrong tree**, because both parses
  fail closed.

  **Sequencing now: read-only probe, then stale-lock removal, then publication of C4-A and
  C4-B, then `check` and `deploy`.** C5 must not begin until the complete C4 reader release
  is installed, which is the plan's own deployment gate.

- **2026-10-02 — PROBE RESULT: BOTH NEW PARSES ARE CONFIRMED AGAINST LIVE SYSTEMD
  OUTPUT.** The read-only `systemctl show` returned exactly the documented shape:

  ```text
  ExecStartPre={ path=/opt/framenest/current/.venv/bin/framenest-production ;
                 argv[]=/opt/framenest/current/.venv/bin/framenest-production
                        check-database-ready ; ignore_errors=no ; ... }
  ExecStart={ path=/opt/framenest/current/.venv/bin/framenest-production ;
              argv[]=/opt/framenest/current/.venv/bin/framenest-production serve ; ... }
  LoadState=loaded  ActiveState=active  UnitFileState=enabled
  User=framenest    Group=framenest     WorkingDirectory=/opt/framenest/current
  ```

  **C4-A's guard is safe on this host**: `path=` is present in the expected form, is a
  `.venv/bin` console script, and `argv[]` carries `check-database-ready` and `serve` as
  **arguments** exactly as predicted. **C4-B's layout selector is safe on this host**:
  `loaded`, `active` and `enabled` are the ordinary values, with no `enabled-runtime` and
  no unfamiliar dialect. The two outstanding parse risks from C4-A and C4-B are closed by
  observation rather than by argument.

  **The failure mode that remains is only the safe one:** a future systemd change that
  produced an unrecognised value would cause a **refused routine operation**, never a
  wrong tree, because both parses fail closed.

- **2026-10-02 — THE STALE LOCK IS NOT EMPTY, and the Orchestrator refused to invent an
  explanation for its persistence.** `ls -la /run/framenest-release-deploy` shows four
  root-owned staging files from an interrupted run: `ap.tar` 880640 bytes,
  `framenest_release.py` 70943 bytes, `previous-release` 64 bytes and `superproject.tar`
  11714560 bytes, with mtimes **Oct 5 21:02-21:03**. Because the directory is **not
  empty**, the helper's own cleanup command `sudo -n rmdir` cannot remove it.

  The Orchestrator verified from the code that `previous-release` inside the deploy
  directory is **transient within a single run** - written at line 4144, read only by that
  same run's rollback at 4329, and removed on success at 4340 - so a stale copy is inert
  and nothing alive reads it. `acquire_deploy_lock` at 2287 reads a **sibling** ownership
  record at `/run/framenest-release-deploy.owner` (line 101), and refuses with
  `existing remote lock without readable ownership` when that record is absent, which
  C4-A's own report confirmed.

  **What the Orchestrator could not establish, and deliberately did not guess:** why the
  directory survived the deploys of `e1d5ee5` and `6e89328`. A simple model predicts it
  could not, so the model is incomplete. **The forward path was chosen so that the
  uncertainty does not need resolving in advance:** both possible outcomes of the next
  deploy are safe, since a reclaim quarantines and proceeds while a refusal mutates
  nothing, and the refusal names its exact reason.

- **2026-10-02 — PUBLISHED. `git push origin main` fast-forward `6e89328..ed5bcb4`, no
  force, divergence `0 0`.** Public `main` is now
  `ed5bcb481749f5a732170fd967efc5a2f940cae2`. Pre-publication checks: strict fast-forward,
  **zero capture product files**, **zero Alembic revision content change**
  (`numstat` empty), and **zero `pyproject.toml` or `ap.project.conf` changes**, so no AP
  re-gate is required.

  **The next deploy is the first live exercise of three mechanisms at once:** the
  reclaimable deploy lock, the installed-unit executable guard, and the layout selector.
  The probe above de-risked the guard and the selector. The lock is the one that may
  refuse, and its refusal is the designed safe outcome.

- **2026-10-02 — `status` and `check` both PASS, and the layout selector is confirmed live.**
  Cooperator output:

  ```text
  kronika-release status
  layout: old
  active_release: 6e89328640fe5477e08f17f4c31c9fc4bf261238
  web_release: 6e89328640fe5477e08f17f4c31c9fc4bf261238
  capture_release: 94e605c17b881461fad3e22fd8c7fca32cb93976
  release_path: /opt/framenest/releases/6e89328640fe5477e08f17f4c31c9fc4bf261238
  service_active: active
  database_revision: 0035
  backup_restore_readiness: ready

  kronika-release check
  release: ed5bcb481749f5a732170fd967efc5a2f940cae2
  layout: old
  ap_gitlink: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
  public_main: ed5bcb481749f5a732170fd967efc5a2f940cae2
  current_release: /opt/framenest/releases/6e89328640fe5477e08f17f4c31c9fc4bf261238
  backup_restore_readiness: ready
  capture_code_tree: cb61ef7df481b823647f8c3687b01fc06fe18e0c
  capture_bridge_protocol: 1
  ```

  **Three things are confirmed by this output.** First, the new `layout: old` field appears
  in both commands, so **C4-B's layout selector executed against live systemd and resolved
  correctly**; it did not fail closed because there was nothing ambiguous to fail on.
  This is the third new mechanism exercised on the host. Second, `capture_release` is
  still `94e605c` and `capture_code_tree` is still `cb61ef7d`, unchanged from the
  `6e89328` check, which is consistent because neither C4-A nor C4-B touched capture
  product code - the Orchestrator verified zero capture product files in both diffs.
  Third, `ap_archive_sha256` is unchanged, confirming the AP submodule is untouched.

  **Neither `status` nor `check` touched the deploy lock**, which is correct: both are
  read-only, so the lock question remains open until `deploy` runs.

  **Position:** `current_release` is still `6e89328`, so the deploy has not yet run. The
  guard and the lock are the two mechanisms still to be exercised live, and `deploy` is
  the command that does both.

- **2026-10-02 — THE STALE LOCK IS FULLY EXPLAINED, and the explanation resolves the
  Orchestrator's earlier confusion about a message and a success appearing together.**
  `previous-release` contains
  `/opt/framenest/releases/e1d5ee510b4a1532606dba7d2a098aed71c16225`, which is `e1d5ee5`.

  **Reconstruction, consistent with every piece of evidence:** the deploy that took the
  host from `e1d5ee5` to `6e89328` succeeded and was run with the **pre-C4-A helper**,
  whose deploy path had **no directory cleanup on success** - exactly the finding C4-A's
  Worker reported. That run therefore left `/run/framenest-release-deploy` and the
  `previous-release` marker it had written at line 4290 behind. **Then the Cooperator ran
  the deploy a second time in that same session**, which is why the log he pasted shows
  both output and status; that second attempt hit the `mkdir` gate and emitted
  `existing remote lock or recovery state`. **The message and the success came from two
  different invocations**, which is why they appeared contradictory in one transcript.

  **This also means the failure can no longer recur**: C4-A added the deploy path's
  cleanup, so a successful deploy now removes its own directory. The stale state is a
  one-time residue of the old behaviour, not an ongoing hazard.

- **2026-10-02 — THE DOCUMENTED RECOVERY DOES NOT COVER THIS STATE, and the Orchestrator
  stopped rather than improvising.** `docs/UBUNTU_NUC_DEPLOYMENT.md` lines 913-945
  documents the recovery: list the directory, remove exactly `ap.tar`,
  `framenest_release.py` and `superproject.tar`, then `rmdir` the empty directory. **Its
  own precondition is explicit: "Unexpected names, extra files, or a missing expected file
  stop the run."** Measured: the directory holds **four** files, being those three plus
  `previous-release`, which the runbook does not list. **The documented precondition
  therefore fails on the real host state, and the runbook's own instruction is to stop.**
  The Orchestrator stopped and reported rather than silently extending the procedure.

  **Two further findings about that runbook section.** It describes interruption **before
  the schema gate**, which is why its artifact list has no `previous-release`: that marker
  is written at line 4290, after the gate. **Our interruption was at a later phase**, so
  the documented recovery covers a different failure point than the one that actually
  occurred. And the same section requires the target tree to report
  `current_revision=0032` and `head_revision=0033`, **which is two schema generations
  stale** - the host is at `0035`. That section needs a follow-up documentation cut, and it
  is recorded as a real gap rather than a curiosity.

  **The fourth file is inert and safe to remove**, verified from the code: `previous-release`
  is written at 4144/4290, read only by that same run's rollback at 4329, and removed on
  success at 4340. Nothing outside its own run consults it, and its recorded value
  `e1d5ee5` is two releases behind the current target, so it cannot mislead any future
  operation even if it survived.

- **2026-10-02 — DEPLOY REFUSED SAFELY, and the reclaimable lock is confirmed live.**
  `kronika-release deploy --release ed5bcb4 --yes` returned
  `kronika-release: existing remote lock without readable ownership`, and the following
  `status` showed `active_release 6e89328`, `capture_release 94e605c`, service active,
  database `0035`, backup ready. **Nothing was mutated and the host is exactly as it was.**
  This is the designed safe outcome and it confirms two things at once: the new lock
  **refuses rather than deleting** when ownership cannot be established, and the absence of
  an ownership record is now established by observation rather than inference.

- **2026-10-02 — STALE LOCK REMOVED under bounded Cooperator authority.** The four staging
  files and the directory were removed by explicit name, without recursion and without a
  wildcard, and the verification listing returned
  `ls: cannot access '/run/framenest-release-deploy': No such file or directory`.
  **The `mkdir` gate can now succeed and the deploy path can proceed to the guard**, which
  is the one mechanism among the three that has still never run live.

- **2026-10-02 — DEPLOY COMPLETE. ALL THREE NEW MECHANISMS CONFIRMED LIVE. The NUC now
  serves `ed5bcb481749f5a732170fd967efc5a2f940cae2`.** Cooperator output:

  ```text
  kronika-release deploy complete: ed5bcb481749f5a732170fd967efc5a2f940cae2
  web_release: ed5bcb481749f5a732170fd967efc5a2f940cae2
  capture_release: 94e605c17b881461fad3e22fd8c7fca32cb93976
  remote_lock: acquired (none)
  unit_executables: .venv/bin/framenest-production

  kronika-release status
  layout: old
  active_release: ed5bcb481749f5a732170fd967efc5a2f940cae2
  web_release: ed5bcb481749f5a732170fd967efc5a2f940cae2
  capture_release: 94e605c17b881461fad3e22fd8c7fca32cb93976
  release_path: /opt/framenest/releases/ed5bcb481749f5a732170fd967efc5a2f940cae2
  service_active: active
  database_revision: 0035
  backup_restore_readiness: ready
  ```

  **`remote_lock: acquired (none)` proves the reclaimable lock acquired cleanly with no
  pre-existing state**, on the first deploy after the stale directory was removed.

  **`unit_executables: .venv/bin/framenest-production` is the decisive line.** It is the
  installed-unit guard reporting the executable it located and validated in the target
  release's `.venv/bin`, which means **the guard that C4-A created from nothing ran
  against live systemd output, resolved the `path=` field correctly, found the retained
  alias, and permitted the switch.** That was the last mechanism in this whole with no
  live confirmation, and it is now confirmed. The guard's fail-closed behaviour on a
  missing executable remains proven only by simulation, but its happy path is now observed
  on the real host.

  **`layout: old` remains correct and unchanged**, because C6 has not run. It will become
  `new` only after the host migration, so its persistence is evidence the selector is
  reading the installed state rather than a constant.

  **`capture_release` is still `94e605c` for the third consecutive deploy**, `service_active
  active`, `database_revision 0035` with no upgrade, and `backup_restore_readiness ready`.

  **This satisfies the completion plan's deployment gate for C5:** *"publish and install
  the complete C4 reader release separately before C5. C1 ancestry alone is insufficient."*
  The complete readers are now installed, and **`ed5bcb4` is the named rollback floor** for
  the C5 writer change. **C5 is unblocked.**

- **2026-10-02 — CLEANUP CONFIRMED.** `ls -la /run/framenest-release-deploy` returned
  `No such file or directory` after the deploy, so **the deploy path now removes its own
  directory on success** - the behaviour C4-A added and the exact defect that created the
  stale lock in the first place. The residue cannot recur.

  **Milestone: C4-A and C4-B are published and installed, all three new mechanisms are
  confirmed live, and the completion plan's C5 deployment gate is satisfied.** The named
  rollback floor for the C5 writer change is `ed5bcb4`.

- **2026-10-02 — C5 implementation prompt issued as `24_implementation_00.md`, `High` band,
  approximately 450k context, one commit, zero host authority, evidence tier E3.**
  Measurement before writing produced two traps that the accepted plan describes only in
  general terms.

  **Trap 1, the loud one.** Four durable identities exist as pairs, each built through
  `accepted_durable_identity(current, canonical)` in
  `src/kronika/domain/analysis_identities.py`, and that helper **raises
  `ValueError` when the two spellings are equal**. Its purpose is exactly to stop a writer
  switch that forgets to restructure the pair. So changing `RESULT_SCHEMA_VERSION` to the
  canonical string without restructuring makes the module raise **at import time** and the
  application cannot start. The locations are `media_analysis_runs.py:21`,
  `media_classification.py:116,117`, and - the one a domain-only derivation would miss -
  **`application/media_suggestion.py:36`**, because `PROMPT_VERSION` lives in the
  application layer.

  **Trap 2, the quiet one, and it is worse.** `src/kronika/domain/media_sidecar.py:38`
  builds its acceptance set as a literal `frozenset({SIDECAR_FORMAT,
  COMPATIBLE_SIDECAR_FORMAT})`. **Changing `SIDECAR_FORMAT` to the canonical string
  collapses that set to one element silently** - no exception, no alarm, and every
  historical sidecar written under the former spelling becomes unreadable. The prompt
  requires the derivation to sort every acceptance set into **raises-on-collapse versus
  collapses-silently**, and requires the silent category to be **demonstrated** so the
  defect class is visible rather than described.

  **Other writer groups measured and carried:** the backup `APPLICATION_NAME` and its
  coupled temporary prefix plus the incomplete-artifact recognizer that must keep
  recognising the former prefix; the off-device and workstation marker names and purposes,
  where **the marker purpose switches but `/mnt/framenest-catalog-offdevice` must not**; the
  release marker constants and manifest identity key, whose accepted tables must still
  carry the former spelling because historical release trees are read during rollback; the
  vision-probe identity, which is **never persisted** and therefore has **no historical
  reader obligation**, a distinction the prompt requires to be stated rather than copied;
  and `SHARED_USER_AGENT = "framenest/0.1"` at `infrastructure/ai/constants.py:13`.

  **The precondition and the boundary are stated as the cut's central fact.** The installed
  rollback floor is `ed5bcb4` - the complete C4 reader release - and the plan's own gate
  required C4 to be installed separately before C5 precisely so that a checkpoint written
  with the new spelling remains readable. **Nothing earlier is a valid floor for C5
  artifacts**, and the Orchestrator must stop describing every C1 descendant as safe. After
  acceptance and the refresh that follows it, `ed5bcb4` **ceases** to be the floor and the
  C5 release becomes it.

  **One Orchestrator typo was caught and corrected before issue:** the report-section list
  named `Pre-Flux Failure Classification` where the standing template requires
  `Pre-Existing Failure Classification`.

- **2026-10-02 — C5 ACCEPTED. Commit
  `3194f48f6b343a460ed5988d92999f91ef999a79`, parent `ed5bcb4`, one commit, not pushed,
  35 files, +1031/-206.** Orchestrator independent verification: **Part A 36/36
  byte-unchanged**, **Part B exactly 20**, **`git diff --diff-filter=D` empty** so nothing
  was removed, `PROTOCOL_MAGIC = b"FNCBE01\0"` intact, and the frozen
  `/mnt/framenest-catalog-offdevice` literal absent from the diff entirely.

  **Both traps closed, verified by reading the result rather than trusting the report.**
  `RESULT_SCHEMA_VERSION = "kronika-media-suggestion-result-v1"` with
  `COMPATIBLE_RESULT_SCHEMA_VERSION = "framenest-media-suggestion-result-v1"` feeding
  `accepted_durable_identity(...)`, so the pair is distinct and the alarm still fires.
  `ACCEPTED_SIDECAR_FORMATS = frozenset({SIDECAR_FORMAT, COMPATIBLE_SIDECAR_FORMAT})` with
  two distinct elements, so the silent collapse did not happen, and the code now carries a
  comment naming that hazard. The same writer/compatible/accepted shape repeats across
  backup, the sidecar suffix, the off-device and workstation markers and the release
  markers, and the application-layer `PROMPT_VERSION` was found and switched.

  **The `accepted_durable_identity` helper was generalised rather than bypassed:** it now
  takes a current spelling plus **one or more** historical spellings and raises on any
  empty or duplicate, so the alarm survives the writer switch in a stronger form than
  before. That is the right way to preserve an invariant across a change that would
  otherwise dissolve it.

- **2026-10-02 — TWO MORE PROMPT ERRORS, both found by the Worker and both confirmed.**
  **First, the prompt mislocated the sidecar suffix.** Group 2 placed it in
  `domain/media_sidecar.py`; measured, the suffix constant is
  `application/ports/media_sidecar_store.py:12-19`, while `domain/media_sidecar.py` carries
  the sidecar **format** and the filesystem module carries the temporary prefix. **A Worker
  following the location literally would have missed the suffix writer entirely.** The
  format/accepted pair and the suffix/accepted pair are now confirmed correct at their real
  locations.

  **Second, and more serious, the prompt named one coupled recognizer where the tree has
  three.** Derivation found a hardcoded former literal at
  **`catalog_backup_ops.py:1548` in `_bundle_looks_complete`**, which is the **retention
  classification** path. **Without that fix, a former-spelling incomplete backup bundle
  would have been classified as COMPLETE**, and retention could then have discarded or
  kept the wrong artefacts. It now uses `ACCEPTED_TEMP_PREFIXES`. This is the substantive
  cost of issuing a named recognizer count instead of a derived recognizer set, and the
  Worker's own recommendation is recorded: **keep requiring derivation rather than a named
  count.**

- **2026-10-02 — The Worker disclosed two writer-output byte fixtures were re-pinned.**
  `MINIMAL_CANONICAL_BYTES` and `UNICODE_MOVIE_BYTES` in `test_media_sidecar.py` were
  re-pinned because the sidecar **writer** changed their bytes by definition, which is this
  cut's purpose. The former-format **decode** fixture in the same file is byte-untouched,
  and explicit former-format round-trip coverage was added. **Disclosed rather than
  slipped through**, and correctly distinguished from rewriting a historical artifact,
  which the prompt forbade. Also noted: `VISION_PROBE_PROMPT_VERSION` has **zero production
  references** - it is declared only - so switching it changes no runtime behaviour.

  Python `4625 passed` against a reproduced `4587` baseline, so **+38**, all in one new
  file. JavaScript unchanged at `583/578/0/5`. Retention `15 passed`. The rollback-floor
  proof uses the floor's **Git bytes** rather than a live process, and the Worker says so
  plainly.

- **2026-10-02 — C5 PUBLISHED. `git push origin main` fast-forward `ed5bcb4..3194f48`, no
  force, divergence `0 0`.** Public `main` is now
  `3194f48f6b343a460ed5988d92999f91ef999a79`. Pre-publication checks: strict fast-forward,
  **zero capture product files**, **zero schema or packaging changes**, and **zero
  deletions**, so no existing artifact fixture was removed.

  **What makes this deploy different from every earlier one, recorded so it is not treated
  as routine.** The routine deploy writes a checkpoint backup using the **target tree's
  code**, so this deploy's checkpoint is the **first artifact ever written with the
  canonical spelling**. The plan's C5 precondition is that such a checkpoint must still
  verify on the rollback release, which is the C4 reader release `ed5bcb4`; the Worker
  proved that from the floor's Git bytes, and **this deploy is where it becomes a live
  observation.**

  **After this refresh `ed5bcb4` ceases to be the artifact floor.** Every later grant must
  name the C5 release explicitly instead, and must not refer to the C4 readers as the
  floor.

- **2026-10-02 — C5 DEPLOYED AND VERIFIED. The NUC now serves
  `3194f48f6b343a460ed5988d92999f91ef999a79`.** Cooperator evidence:

  ```text
  kronika-release deploy complete: 3194f48f6b343a460ed5988d92999f91ef999a79
  web_release: 3194f48f6b343a460ed5988d92999f91ef999a79
  capture_release: 94e605c17b881461fad3e22fd8c7fca32cb93976
  remote_lock: acquired (none)
  unit_executables: .venv/bin/framenest-production

  kronika-release status
  layout: old
  active_release: 3194f48f6b343a460ed5988d92999f91ef999a79
  web_release: 3194f48f6b343a460ed5988d92999f91ef999a79
  capture_release: 94e605c17b881461fad3e22fd8c7fca32cb93976
  release_path: /opt/framenest/releases/3194f48f6b343a460ed5988d92999f91ef999a79
  service_active: active
  database_revision: 0035
  backup_restore_readiness: ready
  ```

  **`backup_restore_readiness: ready` is the C5 live confirmation.** The routine deploy
  writes a checkpoint using the target tree's code, so that checkpoint is **the first
  artifact ever written with the canonical spelling**, and it verifies. The plan's C5 proof
  requirement is met: a canonical-spelled checkpoint was produced and read back. `service_active`
  active, `database_revision 0035` with no upgrade, `capture_release` unchanged for the
  **fourth consecutive deploy**, `layout: old` still correct because C6 has not run, and
  both new deploy mechanisms reported normally.

  **`ed5bcb4` CEASES to be the artifact floor as of this refresh.** The floor is now
  `3194f48f6b343a460ed5988d92999f91ef999a79`, and every later grant must name it explicitly
  rather than referring to the C4 readers.

- **2026-10-02 — ORCHESTRATOR DEVIATION FROM THE ACCEPTED SEQUENCE, recorded rather than
  quietly reordered.** The accepted completion plan orders the cuts
  `C4-B (4) -> C-DATA (5) -> C-LOCAL (6) -> C5 (7)`. **The Orchestrator ran C5 at position
  five and skipped C-DATA and C-LOCAL entirely.** Measured against the plan file rather than
  recalled: the ordering table lists C-DATA and C-LOCAL before C5.

  **Assessment: not harmful, but a real deviation that must be stated.** Neither skipped cut
  is a precondition of C5. C-DATA changes a **data value** (`devices.display_name`) through
  the application engine, and C5 changes **writer identities**; they touch different
  surfaces and neither reads the other's state. C-LOCAL concerns local development and AI
  paths and the plan requires it only *before C7-B*. So C5 was safe to run, and its
  checkpoint - the first canonical artifact - is unaffected by either.

  **What is now constrained:** the plan's C6 preconditions include **"C-DATA complete"**, so
  C-DATA must still precede C6, and C-LOCAL must still precede C7-B. **The next cuts are
  therefore C-DATA and C-LOCAL, and C6 remains blocked on C-DATA** exactly as the plan
  requires. The Orchestrator will not treat the reordering as licence to skip them.

  **One more Orchestrator error in this step, recorded because it is the class the
  Orchestrator keeps holding Workers to:** the Cooperator command block named
  `./kronika-release`, which does not exist. **The release helper is
  `deploy/ubuntu/kronika-release`; `./kronika` at the repository root is the local
  development launcher and something entirely different.** Issued blocks must always carry
  the full path, and the two must never be conflated again.

- **2026-10-02 — RESTORATION HANDOUT WRITTEN, and the outgoing Orchestrator rotates.**
  Stored as `25_restoration_00.md` in the Meta trace. It follows the AP Continuation
  Bootstrap: **Stage 1 is read-only restoration and reconciliation** in the RF-19
  source-precedence order, and **Stage 2 selects exactly one bounded logical whole**. It is
  an **evidence-dense information transfer and grants no authority**, which is what
  `AP.md:2669` and `AP_ORCHESTRATOR.md:516` require - *"Rotation transfers information, never
  authority."* The Cooperator asked for this rotation specifically to stop the recurring
  Orchestrator errors, so the handout carries that record as its most valuable content
  rather than as an appendix.

  **The handout contains, in order:** the instruction to restore read-only and verify every
  figure rather than transcribe it; exact verified refs including the AP pin, HEAD, public
  anchor and suite baselines; the live NUC state and the two host facts that are easy to get
  wrong; what the whole is and the Cooperator-confirmed goal with its in-scope and
  out-of-scope boundary; the named frozen residues; the deliberately accepted
  `FrameNest*Error` inconsistency; the complete list of nineteen completed commits with
  their subjects; the remaining sequence with its load-bearing ordering constraints; the
  three named obligations that are not yet cuts; the ten discipline rules plus the three
  recurring patterns to hunt; and the full Orchestrator error record.

  **Verification performed on the handout itself, applying rule 8 to the Orchestrator:** the
  nineteen-commit table was **regenerated from `git log` rather than transcribed**, and all
  nineteen SHAs match exactly. The AP pin, HEAD, public anchor and the trace file listing
  were each re-measured. **One inaccuracy was found and corrected before rotation:** the
  handout listed the trace as `01_*` through `24_*` and omitted `00_handout.md` and
  `00_notes.md`, and it now names `00_notes.md` explicitly as the highest-value file,
  because it is the only place where every decision, defect and Orchestrator error appears
  together in order.

  **The handout's error record is the reason this rotation exists, and it names the
  recurring classes rather than individual slips:** six incomplete inventories caused by
  issuing hand-built site lists where a derivation was required; two lines attributed to the
  wrong string or the wrong file; one prompt containing two requirements that cannot both
  hold; one false legal alarm raised from a keyword and withdrawn after reading the
  artefact's own definition; one verification that measured the target source and reported
  it as the installed runtime; one deviation from the plan's stated ordering; and one
  Cooperator command block naming a path that does not exist. It also records the corrective
  that actually worked - **derivation rule plus a sample to reconcile against, with a
  required report of every site no test exercises** - which found four latent sites and two
  vacuous guards that no list would have found.

  **The handout's first-act instruction to the fresh Orchestrator is the Cooperator's
  stated shape:** emit exactly one complete copyable **Planner prompt with native planning
  mode**, re-deriving state from the repository, planning the whole remaining sequence
  **through CLOSE** rather than the next cut, stating clause-by-clause what closure means,
  and stating explicitly that **a zero-result text search is not the closure test** and that
  named residues survive closure deliberately.

  **Orchestrator rotation is now the Cooperator's to perform. The outgoing
  Orchestrator has no further authority and will not issue another cut.**

- **2026-10-07 — Fresh Orchestrator restoration completed read-only; every figure
  re-derived, not transcribed.** HEAD, branch, public `main` and the AP pin verified
  at `3194f48f6b343a460ed5988d92999f91ef999a79` /
  `73e20ef80b88700d5fcbc397cd8edd4fc425869f`; `ap doctor` PASS, variant stable;
  Node `v26.8.2`; the three suite baselines reproduced through the declared routes
  (Python `4625 passed, 8 skipped, 3 warnings, 0 failed` in 670 s; JavaScript
  `583 total, 578 passed, 0 failed, 5 skipped`; retention `15 passed`); the frozen
  ledgers measured at **86** document and **36** Alembic keys; the nineteen C0–C5
  commits regenerated from `git log` and matched exactly. The declared upgrade
  ledger validated unchanged and consistent. NUC state classified **carried** —
  this session cannot reach the host. Two handout inaccuracies recorded: the
  class-name residue figures ("roughly 1,423 occurrences across about 95 classes")
  are stale against the measured **61** `class FrameNest*` definitions and
  **1,483** tokens under `src/kronika` (**1,954** Python tokens across
  `src`+`tests`); and the stored handout file is `25_handout_00.md` while its body
  self-names `25_restoration_00.md`.

- **2026-10-07 — `25_planning_00.md` issued (session 25, exchange 01, Planner,
  native planning mode); `25_report_00.md` returned PASS and the closure plan is
  accepted.** Independent source verification of its load-bearing C6 findings:
  `MIGRATION_DIRECTORY` at `kronika_release.py:251` is
  `/var/lib/kronika/identity-migration`, inside the state-copy source tree, while
  `copy_state` requires every destination absent at 2977; `run_migration_apply`
  writes the recovery manifest and journal (3596–3597) before `acquire_lock`
  (3598); `verify_local_readiness:3354` and `cmd_remote_switch_layout_release:2533`
  have no caller; `resume_writers:3439` force-enables every installed timer; the
  capture delta from installed `94e605c` is exactly four files, +158/−29. The
  regenerated inventory table was spot-checked against the ledger (content set
  **507**; env tokens **655/103/29**; header **73/30**; capitalized **2748/394**;
  console entries **14**). The plan formally excludes the Python class/module-name
  residue for the life of the repository under the Cooperator-confirmed membership
  test, and records the Cooperator's in-session selection of the
  `kronika-catalog identity-labels` maintenance CLI for C-DATA.

- **2026-10-07 — Orchestrator prompt defect recorded (own).** The session 25 grant
  omitted the structural `Planning layer` / `Plan disposition` /
  `Implementation in same Worker session` / `Maximum plan-only cycles` record that
  PROMPT_CONTRACTS requires of a plan-only prompt. The exchange still produced a
  plan and no implementation (negative authority held), but the omission is a
  defect and every later planning grant must carry the record.

- **2026-10-07 — Sequence re-baselined by the accepted plan; next cut is C6-P1.**
  Recommended order: `C6-P1 → C6-P2 → C6-V → C-RUNBOOK → C-DATA-P → C-DATA-H →
  C-LOCAL-P → C-LOCAL-H → C-OPS → C6-H → C7-A/S → C7-A/C → C7-B → C8-A/P →
  C8-A/H → C8-B/P → C8-B/H → C9-A → C9-B → C-INSTALL-DOC → CLOSE`. Mandatory gates
  preserved: `C-DATA-H` before `C6-H`; `C-LOCAL-H` and `C-OPS` before `C7-B`;
  canonical emissions before reader removal. **C6 must not run against the current
  adapter.** `26_implementation_00.md` (session 26, exchange 01) is the C6-P1
  repository-only repair grant: one exclusion mechanism, journal/recovery control
  state outside every copy destination, durable intent and writes-possible
  boundary, pre/post-write recovery, copy verification, the three dead builders,
  and failure classification. One local commit, no host authority, no push.

- **2026-10-08 — C6-P1 accepted after independent verification; next cut is
  C6-P2.** `26_report_00.md` (session 26, exchange 01, PASS, `new-mutation`)
  reported commit `8a5861c792122468468b3bc20934a26cb5eb1c93` over `3194f48`,
  three authorized files, +1353/−161. Orchestrator verification: the diff
  contains exactly the three authorized paths; the three dead builders and the
  old migration lock constants are absent; `MIGRATION_DIRECTORY` is now
  `/var/lib/kronika-identity-migration` with `_assert_control_location` deriving
  containment from `plan.copy_moves`; `RemoteMigrationHost.acquire_lock` calls
  `acquire_deploy_lock`; `writes_possible` is durable. Independently re-run at
  the commit through the declared route: focused migration module **117 passed**,
  retention **15 passed**, full declared Python suite **4648 passed, 8 skipped,
  3 warnings, 0 failed** (687 s), exactly the reported +23 with no deletions;
  Part A and Part B unmoved. Public `main` remains `3194f48` — the commit is
  local and unpublished. The report's honest untested-site list and its P2
  deferrals are accepted; no correction was needed. `27_implementation_00.md`
  (session 27, exchange 01) is the C6-P2 repository-only grant for the pointer
  switch and release preparation, unit/ingress/workstation integration and
  readiness/capture-identity verification; one local commit, no host authority.

- **2026-10-08 — C6-P2 accepted after independent verification; C6-V is next.**
  `27_report_00.md` (session 27, exchange 01, PASS, `new-mutation`) reported
  commit `24d2b7d718eb303c79197f6e2f41c81ad479a79a` over `8a5861c`, six authorized
  files, +2511/−185. Orchestrator verification: diff scope exact;
  `MIGRATION_SCRATCH_DIRECTORY` (0700) owns the remote helper and `release_lock`
  removes exactly it and the now-empty directory; the new `switch-current` phase
  runs `verify_unit_executables`, then `cmd_remote_atomic_switch`, then a link
  readback, all before `start-service`; `start_service` now calls
  `verify_local_readiness`; `verify_capture_untouched` compares fresh identity
  snapshots; `resume_writers` restores only observed scheduling; the workstation
  selection is two fixed tuples with default `old` and rejects arbitrary input.
  Independently re-run at the commit through the declared route: focused migration
  **155 passed**, recovery CLI **10 passed**, retention **15 passed**, full
  declared Python suite **4689 passed, 8 skipped, 3 warnings, 0 failed** (690 s)
  — exactly the reported +41 with no deletions. Public `main` remains `3194f48`;
  C6-P1 and C6-P2 are local and unpublished by design. `28_audit_00.md` (session
  28, exchange 01) is the C6-V fresh independent read-only readiness review of the
  exact local candidate before any host window.

- **2026-10-08 — C6-V independent audit PASS accepted; C6 host window unblocked to
  scheduling; C-RUNBOOK next.** `28_report_00.md` (session 28, exchange 01, Fresh
  Independent Audit, read-only, PASS, `new-evidence`, candidate `24d2b7d`)
  reconciled 22 required C6 capabilities against production implementations and
  non-vacuous tests, detected all 16 independent in-memory mutation probes,
  independently re-ran the focused modules (155/10/15) and the full suite
  (4689/8/3/0), and verified Part A (86/36), Part B (20), committed-lock
  byte-identity and routine/capture isolation. **No blocking finding and no
  production-sequence defect.** Non-blocking findings recorded: **F1** three
  uncovered production composites (`create_checkpoint`, `verify_effective_units`,
  production `quiesce`); **F2** further untested branches (eleven named); **F3**
  pre-write recovery leaves copied canonical state, installed units and
  ancillaries in place (to be documented in C-RUNBOOK); **F4** startup readiness
  is `check-database-ready` only with full health at ingress verification; **F5**
  write-only `MIGRATION_JOURNAL_VERSION`. The audit's probe leftovers remain under
  `/tmp/opencode/ksi28/` (non-secret, outside project state); no repository
  mutation. `29_correction_00.md` (session 29, exchange 01) is the C-RUNBOOK
  docs-and-contract-test grant, with the F1 production-adapter coverage as its
  bounded Part B; publication of `8a5861c` + `24d2b7d` + C-RUNBOOK remains a
  separate later grant before any host task relies on it.

- **2026-10-08 — C-RUNBOOK accepted; no stale schema or lock pin survives;
  publication batched after C-DATA-P.** `29_report_00.md` (session 29, PASS,
  `new-mutation`) reported commit `335e91d199e99e28f2585c1b25531f29bb54270c` over
  `24d2b7d`, five authorized files, +432/−27. Orchestrator verification: the
  runbook and both contract suites no longer pin `0032`/`0033` (only legitimate
  ADR links remain) and now carry `<C>`/`<H>` generic pins plus negative stale
  literals; the three-file and four-file lock residues are engine-driven tests;
  the owner-record lifecycle and the C6-V F3 residue are documented; Part B adds
  `create_checkpoint`, `verify_effective_units` and production `quiesce` coverage
  with mutation probes. Independently re-run at the commit: the four focused
  modules **218 passed** (docs 28, operator runbook 17, migration 158, retention
  15) and the full declared Python suite **4696 passed, 8 skipped, 3 warnings,
  0 failed** (684 s). The report's MEASURED critique exposed a pre-existing
  vacuous fake in `tests/contract/test_nuc_release_remote_contract.py` (its
  `rmdir` fake succeeds on a populated directory) and an inaccurate
  `remote_deploy_lock` docstring claim; recorded as **F6**, non-blocking
  test-fidelity residue for a later coverage cut — the engine behavior itself is
  correct and now strictly tested. Publication of `8a5861c` + `24d2b7d` +
  `335e91d` is batched after C-DATA-P, before C-DATA-H. `30_implementation_00.md`
  (session 30, exchange 01) is the C-DATA-P repository-only grant for the bounded
  `kronika-catalog identity-labels` maintenance interface.

- **2026-10-08 — Trace defect: the stored `30_report_00.md` is not the session-30
  outcome.** It is byte-identical to `29_report_00.md` (MD5
  `1d8f094539fe09f74768af14d202c81e`) and declares session `29` / exchange `01` /
  `KSI-IMPL-CRUNBOOK`. No session-30 commit exists: `HEAD` is still `335e91d`, the
  reflog shows only the four accepted commits, and there is no stash or extra
  branch. There is therefore no terminal outcome for `KSI-IMPL-CDATAP` to
  reconcile. Per the Companion Integrity Invariant the companion is rejected; no
  report was reconstructed, no file was overwritten, and the repository was not
  touched. Pending Cooperator decision: provide the real session-30 terminal
  report (and confirm whether the Worker committed — an expected HEAD above
  `335e91d`), or confirm the exchange did not run so the C-DATA-P grant is
  re-issued for the next session ordinal.

- **2026-10-08 — C-DATA-P returned PARTIAL at the authority boundary; one
  bounded correction issued (session 30, exchange 02).** The corrected
  `30_report_00.md` (PARTIAL, `new-mutation`) reported the candidate complete but
  staged uncommitted: the full suite shows exactly three failures in
  `tests/contract/test_kronika_product_string_agreement.py`, because the two new
  canonical runtime literals (`Kronika NUC`, `Kronika`) are brand-bearing and the
  agreement inventory was not in the grant's allowlist. Orchestrator
  verification: the staged set is exactly the seven authorized paths (`engine.py`
  untouched, and `create_sqlite_readonly_engine` already existed there at line
  88), and the focused agreement module fails exactly the three reported tests
  with `KeyError` on the unmapped `identity_labels.py` constants. This is an
  **Orchestrator allowlist defect**, not a Worker defect; the Worker's stop was
  correct and no commit was created. `30_correction_01.md`
  (`current-worker-session`, correction, one commit) authorizes the pin file's
  two rows and the `53→55` / `51→53` counts, plus the two named LEAD completions
  (one library-only apply/rollback test; one runbook owner sentence), and
  finalization of the candidate as one local commit. Publication remains batched
  afterwards.

- **2026-10-08 — C-DATA-P accepted via the bounded correction; full suite green;
  publication next.** `30_report_01.md` (session 30, exchange 02, Bounded
  Correction Worker, PASS, `new-mutation`) reported commit
  `a37be37dd538afa626dbea94b074b676d0b8301c` over `335e91d`, eight files,
  +2751/−14, one non-amended local commit, no push. Orchestrator verification:
  the agreement guard's three failures are resolved by re-derived pins
  (`OCCURRENCE_COUNT` 55, `IN_SCOPE` 53, two rows; duplicates unchanged); the
  library-only apply/rollback test and the runbook owner sentence are in; the
  previously staged candidate is preserved exactly. Focused modules re-run:
  agreement 19, identity-labels 39, retention 15 (**73 passed**); full declared
  Python suite **4737 passed, 8 skipped, 3 warnings, 0 failed** (721 s); Part A
  (86/36) and Part B (20) unmoved; index empty and tree clean. Local `main` is
  four commits ahead of public `origin/main`: `8a5861c`, `24d2b7d`, `335e91d`,
  `a37be37`. Next: publication fast-forward, then the routine NUC refresh
  installing `kronika-catalog identity-labels`, then the C-DATA-H maintenance
  window.

- **2026-10-08 — PUBLICATION PASS: public main is `a37be37`.** The Cooperator
  executed the fail-closed fast-forward block. REMOTE BEFORE `3194f48…`; LOCAL
  AHEAD exactly `8a5861c`, `24d2b7d`, `335e91d`, `a37be37`; `git push origin
  main` reported `3194f48..a37be37  main -> main` with `PUSH_EXIT=0`; REMOTE
  AFTER `a37be37dd538afa626dbea94b074b676d0b8301c`. Orchestrator direct readback
  after the push: `git ls-remote origin refs/heads/main` = `a37be37…`, local
  `main...origin/main` in sync. The C6-P1, C6-P2, C-RUNBOOK and C-DATA-P commits
  are now public. Next: routine NUC refresh (status and `check --release a37be37…`
  under a live remote sudo timestamp, then the deploy under the routine-refresh
  procedure) to install `kronika-catalog identity-labels` before the C-DATA-H
  window.

- **2026-10-10 — PRE-DEPLOY `status` and `check --release a37be37…` PASS; deploy
  next.** Cooperator output: `status` shows layout `old`, active/web release
  `3194f48…`, capture release `94e605c…` unchanged, service `active`, database
  revision `0035`, backup readiness `ready`, `STATUS_EXIT=0`. `check` shows
  `public_main` and `release` both `a37be37…`, `ap_gitlink` the pin,
  `ap_archive_sha256` unchanged, `current_release` still `3194f48…` (correct —
  no deploy has run), backup readiness `ready`, `capture_code_tree` `cb61ef7d…`,
  bridge protocol 1, `CHECK_EXIT=0`. The same-schema path applies (database
  `0035` equals packaged head `0035`). The remote sudo timestamp is live (both
  layout probes succeeded). Deploy grant issued: `deploy/ubuntu/kronika-release
  deploy --release a37be37… --yes` plus an immediate `status`; the timestamp is
  retained through the immediately following C-DATA-H window and released at its
  end.

- **2026-10-10 — DEPLOYMENT PASS: the NUC now serves `a37be37`.** Deploy output:
  `deploy complete: a37be37…`, `web_release: a37be37…`, `capture_release:
  94e605c…` unchanged, `remote_lock: acquired (none)`, `unit_executables:
  .venv/bin/framenest-production`, `DEPLOY_EXIT=0`. Post-deploy `status`:
  active/web release `a37be37…`, capture `94e605c…`, release path
  `/opt/framenest/releases/a37be37…`, service `active`, database revision `0035`,
  backup readiness `ready`, `STATUS2_EXIT=0`. The same-schema path held; no
  capture restart; the installed-release guard passed against the retained
  `framenest-production` alias. The C-DATA-H maintenance window is unblocked:
  fresh preflight, stopped writers, verified checkpoint, then the bounded label
  correction (device `FrameNest NUC` → `Kronika NUC`; libraries only if the
  preflight is positive and the scope is explicitly included). The remote sudo
  timestamp stays live until the window's post-state evidence is captured.

- **2026-10-10 — C-DATA-H W1 complete: writers stopped; two host findings.**
  Prior state recorded: `framenest.service` enabled+active;
  `framenest-catalog-backup.timer` enabled+active; the **off-device units do not
  exist on this host** (`not-found`) — the optional integration was never
  installed and stays absent; `framenest-catalog-backup.service`
  disabled/inactive. `/etc/framenest/framenest.env` is `0640 root:framenest`
  (readable by the service account); the catalog is `0600 framenest` at
  `/var/lib/framenest/catalog.sqlite3`. The combined stop returned `STOP_EXIT=5`
  solely because `framenest-catalog-offdevice.timer` is not loaded; the existing
  units stopped (`framenest.service` inactive, backup timer inactive) and
  `pgrep -u framenest` shows no remaining processes, so the catalog is
  quiescent. Restoration contract: start exactly `framenest.service` and
  `framenest-catalog-backup.timer`; leave the absent off-device integration
  absent. Next: W2 `identity-labels check` (creates the private receipt) and W3
  verified checkpoint through the installed backup implementation.

- **2026-10-10 — C-DATA-H W2/W3 complete: preflight positive for one device and
  one library; checkpoint verified.** `check` as the owner reported
  `device_candidate_count: 1`, `device_candidate_present: true`,
  `library_candidate_count: 1`, `library_brand_present: true`, receipt digest
  `dc28c4f06ee3f78a18a45244da9cc68a94a1e4e271bc0c0fab1dc1ec5658a650`; the private
  receipt is `0600 framenest`, 369 bytes, at
  `/var/lib/framenest/catalog.sqlite3.identity-labels-receipt.json`. The
  checkpoint `run-scheduled` succeeded: bundle `auto-20261010T070301Z-0a7b6ac3`,
  catalog SHA-256 `284b5f4c4c9770a6d083336a07186d9b0c0574e900a6179135f448789de2d148`,
  size 798720, revision `0035`, retention applied, `state: succeeded`. Both exits
  0. Awaiting the Cooperator's explicit library-scope decision before `apply`;
  the Orchestrator recommends including libraries because the confirmed goal is
  zero user-visible occurrences and the command replaces only the brand
  substring while preserving every other character.

- **2026-10-10 — C-DATA-H W4 APPLY PASS: the live catalog labels are corrected.**
  Sanitized output: `device_updated: true`, `libraries_updated: 1`,
  `device_transition_verified: true`, `libraries_transition_verified: true`,
  `foreign_keys_valid: true`, `schema_revision_at_head: true`,
  `selected_retired_labels_remaining: 0`, receipt digest matching `dc28c4f0…`,
  `APPLY_EXIT=0`. One device label (`FrameNest NUC` → `Kronika NUC`) and one
  library display name (brand substring only) were corrected inside one
  immediate transaction with compare-and-set; the private receipt is retained
  for receipt-bound rollback. The plan's additional invariants (unchanged IDs,
  relationships and non-label columns) are structurally guaranteed by the
  single-column CAS update and covered by the suite's fixture matrix; the live
  output covers transition, foreign keys, revision and zero selected residue.
  Next: W5 restore the exact prior writers (`framenest.service`,
  `framenest-catalog-backup.timer`), then W6 post-state `status`.

- **2026-10-10 — C-DATA-H W5/W6 PASS: writers restored exactly and the NUC is
  healthy; window closing.** `START_EXIT=0`; `framenest.service` and
  `framenest-catalog-backup.timer` both `enabled=enabled active=active`; the web
  socket `/run/framenest/framenest.sock` is listening. Post-state `status`:
  `service_active: active`, `web_release: a37be37…`, `capture_release: 94e605c…`
  unchanged, `database_revision: 0035`, `backup_restore_readiness: ready`,
  `STATUS_EXIT=0`. The absent off-device integration stayed absent. **C-DATA is
  complete on the host**: one device label and one library display name
  corrected by the bounded command, one immediate transaction, receipt retained
  for receipt-bound rollback, no schema or relationship change. Remaining in the
  window: the observed `sudo -K` privilege release, then closure. Next repository
  cut after closure: `C-LOCAL-P`.

- **2026-10-10 — C-DATA-H window CLOSED. Privilege release observed; C-DATA
  complete.** The Cooperator ran `sudo -K`; the post-release check
  `sudo -n true` failed with `sudo: a password is required` and
  `SUDO_AFTER_K_EXIT=1`, which is the observed release evidence (no fabricated
  `sudo -k` claim). The window's complete evidence: writers stopped and catalog
  quiescent; sanitized preflight (one device, one library); verified checkpoint
  `auto-20261010T070301Z-0a7b6ac3` at `0035`; apply with
  `device_updated: true`, `libraries_updated: 1`, transitions verified, foreign
  keys valid, `selected_retired_labels_remaining: 0`; writers restored exactly
  (`framenest.service` and `framenest-catalog-backup.timer` enabled+active,
  socket listening); post-state `status` healthy at `a37be37` with capture
  `94e605c` unchanged and backup `ready`. The private receipt remains at
  `/var/lib/framenest/catalog.sqlite3.identity-labels-receipt.json` for
  receipt-bound rollback. Next: `C-LOCAL-P` repository grant (session 31,
  exchange 01).

- **2026-10-10 — `31_implementation_00.md` issued (session 31, exchange 01):
  C-LOCAL-P.** Repository-only grant for `kronika-dev migrate-identity-paths
  check|apply`: canonical mapping (`FrameNest`→`Kronika`, `framenest`→`kronika`,
  `framenest-development`→`kronika-development`) across the owned macOS
  Application Support/Logs, Linux/XDG data/state/log, temporary development root
  (database, runtime settings, gallery previews, covers, thumbnails) and AI
  configuration/test-state/status paths; copies only to absent destinations with
  WAL-safe database verification; private receipts and idempotent re-apply; the
  legacy-state empty-replacement safeguard; **no default changes** (that is
  C7-B); synthetic fixtures only; one local commit.

- **2026-10-10 — C-LOCAL-P accepted; full suite green; C-LOCAL-H next.**
  `31_report_00.md` (session 31, exchange 01, PASS, `new-mutation`) reported
  commit `a3977755b6d20a369f1a5c75e39bbcacd88de5c6` over `a37be37`, seven files,
  +2893/−9, one local commit, no push. Orchestrator verification: diff scope
  exact; `DEVELOPMENT_DATABASE_DIRECTORY` is still `"framenest-development"`
  (defaults unmoved) and the `migrate-identity-paths` dispatch is present;
  focused modules re-run **103 passed**; full declared Python suite **4773
  passed, 8 skipped, 3 warnings, 0 failed** (688 s); Part A unchanged and Part B
  still 20; tree clean; public `main` remains `a37be37`. The report's disclosed
  deviations are accepted (root `DEVELOPMENT.md` is the actual documentation
  surface; the product-agreement inventory was extended by disclosure; the
  persistence-boundary failure was a candidate defect fixed by routing through
  the engine boundary, not by editing the boundary test). Recorded Orchestrator
  lesson from its critique: anchor maps for in-package modules must include the
  package boundary/agreement modules. Next: `C-LOCAL-H` Orchestrator-led
  Cooperator window — identify existing local state with the read-only `check`,
  then apply per identified installation; all receipts must exist before C7-B.

- **2026-10-10 — C-LOCAL-H discovery: 4 owned sources present, all destinations
  absent, no overrides.** The Cooperator ran the read-only
  `kronika-dev migrate-identity-paths check` from the checkout
  (`env PYTHONPATH=/home/agile/Projects/kronika/src .venv/bin/python -m
  kronika.adapters.cli.development`): `Classes: 12 total, 0 explicit overrides`,
  `Sources: present 4, absent 8`, `Destinations: absent 4, occupied 0`,
  `CHECK_EXIT=0`; the detailed source/destination mapping was recorded in the
  private receipt. No managed development server is running (the check would
  have refused otherwise). Next: `apply` for the four present sources —
  originals preserved, absent-only destinations, WAL-safe database
  verification, private apply receipt.

- **2026-10-10 — C-LOCAL-H apply: 2 copied verified, 1 refused
  (`xdg_development_database`), 8 sources absent, 1 no-durable-content;
  `APPLY_EXIT=5`.** The refused class is the XDG development catalog; the tool's
  refusal is fail-closed and distinguishes source-symlink, destination-occupied
  and copy-refused, while the database copy path opens the source through the
  application engine's private-catalog boundary (directory `0700`, file `0600`,
  same owner, regular file, `nlink == 1`). The CLI's apply summary does not print
  the `no_durable_content` bucket, so its printed buckets sum to 11 of 12; the
  private apply receipt holds the exact per-class outcomes. Originals are
  preserved; the two copied items and the apply receipt were written privately.
  Next: sanitized diagnosis only — the refusal status kind from the private
  receipt and the file/directory modes of the refused source, without printing
  any path — before any remediation or re-apply.

- **2026-10-10 — C-LOCAL-H refusal diagnosed: `copy-refused` because the legacy
  XDG development catalog is not private.** Receipt status counts:
  `2 copied-verified`, `1 copy-refused`, `1 no-durable-content`,
  `8 source-absent`. The refused source: development directory mode `755`,
  catalog regular file mode `644`, 573440 bytes, `links=1`, and no WAL/SHM/
  journal siblings. The application's private-catalog contract requires exactly
  `0700`/`0600` with the same owner, so the engine boundary refused to open the
  source — fail-closed, nothing copied, nothing lost. **Authorized remediation:**
  make exactly those two owned objects more restrictive (`chmod 700` the
  development directory, `chmod 600` the catalog), then re-run `apply`
  (idempotent; the two existing destinations become `already-verified` and the
  catalog copies with WAL-safe verification). The CLI's unprinted
  `no-durable-content` bucket remains a minor reporting observation for a later
  touch of the module.

- **2026-10-10 — C-LOCAL-H complete: all four present sources migrated or
  explained; originals preserved; `APPLY_EXIT=0`.** After the bounded
  remediation (development directory `700`, catalog `600`), the re-apply
  reported `Copied verified: 1`, `Already verified: 2`, `Sources absent: 8`,
  `Refused: 0`, `APPLY_EXIT=0` — the refused XDG development catalog copied with
  WAL-safe verification, the two earlier copies re-verified as
  `already-verified`, one class has no durable content (unprinted bucket; the
  receipt holds it) and eight classes have no state. Receipts: one check plus
  one apply in the private per-user directory; the source originals remain in
  place. The fail-closed privacy refusal and its bounded resolution are recorded
  as executed evidence for `C7-B`'s default switch, which must retain the
  legacy-state safeguard. Next: `C-OPS` (five canonical operator-script
  counterparts), then publication of `a397775` + `C-OPS`, then the `C6-H`
  window.

- **2026-10-10 — `32_implementation_00.md` issued (session 32, exchange 01):
  C-OPS.** Repository-only grant for the five canonical operator-script
  counterparts (`kronika_log_triage.sh`, `kronika_public_surface_check.sh`,
  `kronika_socket_permissions_check.sh`, `kronika_mullvad_egress.sh`,
  `kronika_mullvad_egress.fish`): dual-prefix `KRONIKA_*`/`FRAMENEST_*`
  contract following the NUC gate (conflict exits 2 naming only the variable
  names), canonical operational defaults, unchanged checks/refusals/exit codes,
  the canonical Fish wrapper targeting the canonical Bash implementation, the
  old five scripts frozen and Part B still 20, hermetic fake-tool tests with
  `fish --no-config`, and operator-instruction updates; one local commit.

- **2026-10-10 — C-OPS accepted; full suite green; publication next, then
  C6-H.** `32_report_00.md` (session 32, exchange 01, PASS, `new-mutation`)
  reported commit `b8ec042b5bf1835df77c81341abc75e9cf8ab059` over `a397775`,
  eleven files, +2561/−64, one local commit, no push. Orchestrator verification:
  the diff contains the five canonical scripts, the two test modules, the three
  operator docs and the retention ledger, and **no old `framenest_*` operator
  script**; all five old-script SHA-256 values match the report byte-for-byte;
  the five canonical scripts are mode `755`; focused modules re-run **149
  passed**; full declared Python suite **4828 passed, 8 skipped, 3 warnings,
  0 failed** (692 s); Part A unchanged and Part B still 20; tree clean; public
  `main` remains `a37be37`. The report's dual-prefix semantics (conflict exits 2
  naming only variable names; eager resolution before any logic) and its
  mutation demonstrations are accepted. Its open items are recorded: the
  canonical Mullvad branch matrix is proven by classified equivalence rather
  than re-execution (candidate for one bounded independent-acceptance harness
  run), and `scripts/operator/network/README.md` still names the retained
  scripts (a C7-B documentation candidate). Next: publication of `a397775` +
  `b8ec042`, then the `C6-H` preflight.

- **2026-10-10 — PUBLICATION PASS: public main is `b8ec042`.** The fail-closed
  block reported REMOTE BEFORE `a37be37`; LOCAL AHEAD exactly `a397775`,
  `b8ec042`; `git push origin main` reported `a37be37..b8ec042  main -> main`
  with `PUSH_EXIT=0`; REMOTE AFTER `b8ec042b5bf1835df77c81341abc75e9cf8ab059`.
  Orchestrator direct readback confirms `b8ec042…` and local `main` in sync. All
  accepted repository work through C-OPS is now public. Next: C6-H preflight —
  re-establish the remote sudo timestamp, then `status`, `check --release
  b8ec042…`, and `migrate-identity preflight --release a37be37…` (the installed
  release) as the read-only plan for the host window.

- **2026-10-10 — C6-H preflight STOPPED fail-closed: an effective unit drop-in
  carries an unclassifiable `ReadWritePaths` path.** `status` and `check
  --release b8ec042…` both passed (`STATUS_EXIT=0`, `CHECK_EXIT=0`): layout
  `old`, served release `a37be37…`, capture `94e605c…`, service `active`,
  database `0035`, backup `ready`, `public_main` and `release` both `b8ec042…`.
  `migrate-identity preflight --release a37be37…` then stopped with
  `kronika-release: unit directive ReadWritePaths path is not classifiable`,
  `MIGRATE_PREFLIGHT_EXIT=27` — no mutation, the designed fail-closed refusal.
  The transformer knows `ReadWritePaths` as a path-list directive, but for each
  token it raises when the token contains the retired spelling and
  `transform_path_value` leaves it unchanged; frozen prefixes and foreign/custom
  paths are deliberately preserved, so a frozen or custom token inside an
  installed drop-in trips that guard. This is exactly the class of live-host
  form the preflight exists to catch; the remote sudo timestamp is live.
  Next: a bounded read-only host probe to identify the effective drop-in(s) and
  the exact directive line before deciding the smallest correction.

- **2026-10-10 — C6-H preflight finding identified: an operator drop-in
  preserves a custom media path; the directive guard is over-broad.** The probe
  found the failing directive in
  `/etc/systemd/system/framenest.service.d/30-publication-write-path.conf`
  line 2: `ReadWritePaths=/srv/media/framenest-published`; the installed backup
  service and timer carry no drop-ins. The path is host-side and appears nowhere
  in the repository; it is a custom media/publication path containing the
  retired spelling. `transform_path_value` deliberately preserves foreign/custom
  paths, but the directive-level guard (`unchanged + contains framenest →
  raise`) cannot distinguish a deliberate custom path from an incomplete rename,
  so the preflight refused fail-closed. The accepted plan says "preserve custom
  media roots" and forbids altering library roots or original media, so C6
  preserves this path; a rename would be its own bounded media-path migration
  and is recorded as a **deferred host-residue candidate** for the closure
  reconciliation. `33_correction_00.md` (session 33, exchange 01) is the bounded
  correction: one unified path-token classifier across the path-list, exec and
  LoadCredential guards (frozen → preserve; foreign/custom → preserve; near-miss
  variants of a moved root → refuse; under a moved root with leftover spelling →
  refuse), with tests and mutation demonstrations; a fresh independent re-audit
  follows before the preflight re-run.

- **2026-10-10 — C6-P2 guard correction accepted at implementation level; fresh
  re-audit next.** `33_report_00.md` (session 33, exchange 01, PASS,
  `new-mutation`) reported commit
  `cf76f0b3a391663db7f4b0c88b872c08b69ff279` over `b8ec042`, three files,
  +283/−19. Orchestrator verification: diff scope exact;
  `classify_unit_path_token` present with the frozen → moved → near-miss →
  foreign order; focused modules re-run **208 passed** (migration 193 + retention
  15); full declared Python suite **4863 passed, 8 skipped, 3 warnings, 0 failed**
  (680 s); Part A unchanged and Part B still 20; tree clean; public `main`
  remains `b8ec042`. Accepted deviations to judge in the re-audit: the Exec plain
  guard now classifies the executable token only (argument text opaque, pinned by
  a new test) and a foreign `LoadCredential` path is now preserved; the untouched
  sudoers-command guard remains strict, so a foreign sudo rule path carrying the
  retired spelling would still stop the preflight fail-closed (to check in the
  next host window). `34_audit_00.md` (session 34, exchange 01) is the fresh
  independent re-audit of this correction; only after its PASS may the C6-H
  preflight be re-run.

- **2026-10-10 — C6-V2 re-audit returned BLOCKED on a new finding (B1); bounded
  repair authorized at the escalation decision.** `34_report_00.md` (session 34,
  Fresh Independent Audit, read-only) verified identity/scope, re-derived all
  five guard sites, independently ran a 160-case matrix and three mutation
  probes, reconstructed the baseline refusal from the parent blob (`git show`),
  and confirmed the full suite (4863/8/3/0) and Part A/B. It found **B1: the
  revision-form `Exec*={ path=… }` transformer decodes the captured executable
  and, for frozen/foreign classification, re-inserts the decoded text, losing
  systemd escaping.** Demonstrated with `path=/srv/audit34/framenest\x20assets`:
  the output `.../framenest assets` reparses to a different executable
  (`/srv/audit34/framenest` plus argument `assets`); the parent refused those
  inputs, so the correction exposed a preservation regression for newly accepted
  forms. The audit judged both accepted deviations (Exec argument opacity;
  foreign/relative `LoadCredential` preservation) acceptable and narrow, and left
  the sudoers command guard's strictness as a residual host-preflight risk. The
  C6 host window is blocked by B1. Orchestrator decision (as escalation
  disposition owner; new material evidence, not the same assumption): authorize
  one bounded B1 repair with a fresh independent re-audit after it. The
  confirmatory code path is `kronika_release.py:4288-4309` (decode → classify →
  reinsert without re-encoding), while the plain-exec, path-list and
  `LoadCredential` branches already operate on raw text.
  `35_correction_00.md` (session 35, exchange 01) is the repair grant.

- **2026-10-10 — B1 repair accepted at implementation level; trace filename
  mismatch recorded; fresh re-audit next.** The repair report (content
  coordinates session `35` / exchange `01`, task `KSI-CORR-C6ENC`, PASS,
  `new-mutation`) is stored as `36_report_00.md`; the file must be renamed to
  `35_report_00.md` to keep the Meta session-ordinal grammar and to clear
  `36_report_00.md` for the session-36 re-audit. Orchestrator verification:
  commit `78cba281960e2f17137647bcc90aab83847a1c0c` over `cf76f0b`, three files,
  +227/−9; `_render_moved_revision_token` present; focused modules **218 passed**
  (migration 203 + retention 15); full declared Python suite **4873 passed, 8
  skipped, 3 warnings, 0 failed** (696 s); Part A unchanged and Part B still 20;
  tree clean; public `main` remains `b8ec042`. The repair: frozen/foreign
  revision tokens return byte-identically; moved tokens are rewritten from raw
  text with a reparse guard; unprovable raw forms fail closed with `revision
  path is not provably transformable` (exit 27). Disclosed deviation: one
  ambient `python3` counter use, not test evidence — recorded as a route
  deviation and accepted with disclosure. `36_audit_00.md` (session 36, exchange
  01) is the fresh independent re-audit of the repair, including the report's
  LEAD (escaped-slash plain/path-list/LoadCredential probes).

- **2026-10-10 — Session 36 re-audit BLOCKED on an Orchestrator prompt defect
  (stale repair-report path); corrected audit re-issued as session 37.** The
  Cooperator renamed the repair report to `35_report_00.md` as instructed, but
  the session-36 prompt still named `36_report_00.md` in its candidate identity
  and mandatory reading, so the auditor followed the prompt literally, found the
  path absent, and stopped BLOCKED with
  `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` (G1: missing mandatory
  repair report), performing no review work and mutating nothing. The candidate
  is not implicated: `78cba28` remains accepted at implementation level (focused
  218, full suite 4873/8/3/0, Part A/B unmoved). The corrected audit is re-issued
  as session 37, exchange 01 (`37_audit_00.md`) with the repair-report path
  corrected to `35_report_00.md`; it keeps the Fresh Independent Audit profile
  and read-only authority. Recorded as the second Orchestrator prompt-path defect
  in this whole (after session 25's missing Plan-to-Execution record).

- **2026-10-11 — C6-V2 re-audit (session 37) returned PASS; the C6 adapter is
  accepted and the host preflight is unblocked.** `37_report_00.md` (session 37,
  exchange 01, Fresh Independent Audit, read-only, PASS, `new-evidence`)
  independently re-derived identity and scope, the B1 evidence (byte-identity,
  reparse, idempotence, parent comparison), the full regression matrix across the
  four site shapes plus refusals, the LEAD escaped-form probes, and three
  in-memory mutations (all detected); it reproduced the declared checks exactly
  (focused 203, retention 15, full suite 4873/8/3/0) and confirmed Part A (86/36)
  and Part B (20) unchanged. **No blocking finding.** Residuals recorded: **R1**
  pre-existing sibling-site gap — an escaped root character or escaped renamed
  segment at the plain-`Exec*`, path-list and `LoadCredential` sites is preserved
  or partially rewritten without refusal (parent-identical; a live unit carrying
  such a spelling would pass preflight while naming the retired layout at
  runtime); **R2** new intended fail-closed behavior for unprovable revision raw
  forms; **R3** sudoers-command guard residual; **R4** malformed-hex `ValueError`
  boundary; **R5** the accepted deviations remain. Next: publish `78cba28`, then
  the preflight window with the LEAD backslash probe (list effective unit
  directive tokens containing a backslash and classify their decoded forms
  before apply).

- **2026-10-11 — PUBLICATION PASS: public main is `78cba28` (two commits).** The
  fail-closed block reported REMOTE BEFORE `b8ec042`; LOCAL AHEAD was **two**
  commits — `cf76f0b` (guard correction) and `78cba28` (B1 repair) — not the one
  I stated in the message; the guard correction had never been published
  separately, and both are accepted work, so the push `b8ec042..78cba28` with
  `PUSH_EXIT=0` was correct. REMOTE AFTER
  `78cba281960e2f17137647bcc90aab83847a1c0c`; Orchestrator direct readback
  confirms `78cba28…` and local `main`/`origin/main` in sync. Recorded as an
  Orchestrator expectation misstatement (local-ahead count), not a publication
  error. Next: C6-H preflight window — remote sudo timestamp, `status`, `check
  --release 78cba28…`, `migrate-identity preflight --release a37be37…`, and the
  LEAD backslash probe over effective unit/drop-in lines.

- **2026-10-11 — Preflight window attempt #1 aborted by a NUC session anomaly;
  no mutation, retry minimal.** The Cooperator ran the NUC block; the paste
  preserves the backup unit fragment/drop-in listing
  (`framenest-catalog-backup.service` and `.timer`, both without drop-ins), but
  the first unit's listing, the timestamp result and the backslash probe output
  are missing. At the probe the terminal shows a mangled `^[[H` fragment, two
  interrupts, `free(): double free detected in tcache 2`, and then
  `Connection to 100.102.127.11 closed` — the SSH session died with an
  unknown-cause heap error in some process. Every command in the block was
  read-only; no migration, product or repository action is implicated, and the
  timestamp step is unverified. The PC preflight block was not run. Next:
  reconnect and run a minimal health/timestamp check first; if the anomaly
  recurs, treat it as a bounded host finding rather than retrying blindly.

- **2026-10-11 — Minimal retry clean: `framenest-nuc`, `up 1 day, 2:47`,
  `systemctl is-system-running: running`, `SUDO_READY=0`.** The double-free
  anomaly did not recur and the host shows no reboot; the remote sudo timestamp
  is live. Proceeding with the simplified backslash probe and the PC preflight
  block (`status`, `check --release 78cba28…`, `migrate-identity preflight
  --release a37be37…`).

- **2026-10-11 — Preflight stopped fail-closed again on an unsupported host
  directive (`RuntimeDirectoryMode`); complete directive-key derivation requested
  before the next correction.** `migrate-identity preflight` passed the
  foreign-path case but stopped with `kronika-release: unit directive
  RuntimeDirectoryMode is not supported`, `MIGRATE_PREFLIGHT_EXIT=27` — no
  mutation. The web drop-in directory contains `20-ai-credential.conf` (82 B),
  `30-publication-write-path.conf` (56 B), `40-runtime-directory-mode.conf`
  (36 B, the failing `RuntimeDirectoryMode`) and `framenest-research-credential.conf`
  (526 B). The backslash probe found no escaped lines (`GREP_STATUS=1`), so R1
  does not manifest in this host's drop-ins. Fragment texts are not transformed
  (the single `transform_unit_dropin_text` call site is the drop-in loop), so the
  drop-ins are the complete surface. Instead of discovering remaining
  unsupported directives one preflight at a time, a directive-keys-only probe
  will derive the complete set for one coherent correction. `status` and `check
  --release 78cba28…` both passed (layout `old`; `a37be37`; capture `94e605c`;
  database `0035`; backup `ready`; `public_main` `78cba28`).

- **2026-10-11 — Directive-key derivation complete: the host's four web drop-ins
  contain only `LoadCredential`, `ReadWritePaths` and `RuntimeDirectoryMode`.**
  Exactly one key is outside the transformer's supported set — the benign,
  brand-free `RuntimeDirectoryMode`. `38_correction_00.md` (session 38, exchange
  01) is the bounded correction that replaces the blanket unknown-directive
  refusal with a principled policy: known directives keep their structural
  handling; an unknown directive is preserved when neither its key nor its value
  carries the retired spelling, and refused (same message and exit 27) when
  either does. The two existing tests that asserted refusal for brand-free
  unknown forms are updated to the new contract; brand-bearing refusal tests
  remain. One commit; a fresh independent re-audit follows; then the preflight.
  Budget note: this is a distinct new live finding (not the same assumption), and
  the complete key derivation plus the general policy means no further
  unknown-directive surprise is expected.

- **2026-10-11 — Unknown-directive policy correction accepted at implementation
  level; fresh re-audit next.** `38_report_00.md` (session 38, exchange 01, PASS,
  `new-mutation`) reported commit
  `980041cf13dd427e77263f573694aed7c1a54018` over `78cba28`, three files,
  +121/−14. Orchestrator verification: the terminal branch refuses only when the
  key or value carries the retired spelling and preserves brand-free unknown
  directives; focused modules **222 passed** (migration 207 + retention 15);
  full declared Python suite **4877 passed, 8 skipped, 3 warnings, 0 failed**
  (721 s); Part A unchanged and Part B still 20; tree clean; the two adjusted
  tests keep genuine refusal assertions with brand-bearing fixtures and the new
  preservation tests pin the policy; public `main` remains `78cba28`.
  `39_audit_00.md` (session 39, exchange 01) is the fresh independent re-audit;
  after its PASS: publish `980041c`, re-run the preflight, then the E4 apply
  decision.

- **2026-10-11 — Session-39 re-audit returned PARTIAL on one design residual
  (R1); Orchestrator disposition: accepted for the C6 window, with live exclusion
  evidence.** The audit verified identity/scope, the policy matrix, adjusted-test
  genuineness, full regression (all parent-identical), three mutations, checks
  exactly `4877/8/3/0` and Part A/B — and raised **R1**: the policy tests raw
  text, while systemd decodes C-style escapes in `Environment`-style values (per
  installed systemd 261.3 manuals), so an encoded spelling in an unknown
  directive value would be preserved rather than refused; it also notes the live
  inventory completeness was not observable under its no-host grant.
  **Disposition (Orchestrator, RF-08 escalation owner): accept R1 as a documented
  policy-level limitation and proceed**, because the transformed surface for this
  window is fully and directly enumerated: the complete drop-in key set is
  `LoadCredential` / `ReadWritePaths` / `RuntimeDirectoryMode`; the only unknown
  directive is `RuntimeDirectoryMode=0700`, whose file is exactly 36 bytes
  (`[Service]\nRuntimeDirectoryMode=0700\n`), a plain numeric value with no
  escape or specifier; and the Cooperator's backslash probe over every effective
  unit/drop-in file returned no matches (`GREP_STATUS=1`), which directly excludes
  any `\xXX`-encoded spelling from the entire transformed surface. The residual
  does not affect the supplied live set and is recorded as a **deferred
  hardening** (refuse an unknown value containing a backslash or specifier, or
  add systemd-style decoding, in a later bounded cut — not required for C6).
  Other audit notes: R3 the renderer normalizes CRLF to LF (byte preservation
  limited to LF forms); R4 a retention-comment prose defect (three-plus-five
  split misstated as two-plus-six; counts correct); the audit's report write was
  explicitly instructed by the Cooperator after the prompt's no-file clause.
  Next: publish `980041c`, restore the timestamp, third `migrate-identity
  preflight`, then the E4 apply decision.

- **2026-10-11 — PUBLICATION PASS: public main is `980041c`.** Fail-closed block:
  REMOTE BEFORE `78cba28`; one local commit (`980041c`); `git push origin main`
  reported `78cba28..980041c  main -> main` with `PUSH_EXIT=0`; REMOTE AFTER
  `980041cf13dd427e77263f573694aed7c1a54018`. Orchestrator direct readback
  confirms `980041c…` and local `main` in sync. Next: third C6 preflight —
  re-establish the timestamp, then `status`, `check --release 980041c…` and
  `migrate-identity preflight --release a37be37…`; the complete drop-in key set
  and the clean backslash probe mean no further unsupported-form surprise is
  expected.

- **2026-10-11 — Third preflight PASS (exit 0): the migration plan is prepared.**
  `status` and `check --release 980041c…` passed; `migrate-identity preflight
  --release a37be37…` printed `old_layout: old`, `new_layout: new`,
  `plan_digest: 2c287485206bfdaf54883012ac9fc88e9e75b8cfcd5a295b272ebf46f0e1aa40`,
  `copy_moves: 3`, `installed_units: framenest.service,framenest-catalog-backup.service,framenest-catalog-backup.timer`,
  `observed_units: 9`, `installed_dropins: 4`, `credential_sources: 3`,
  `export_installed: /usr/local/libexec/framenest-catalog-export-v1`,
  **`sudo_rule_installed: absent`** (the sudoers residual R3 is moot on this
  host), `capture_pointer: old`, `tailscale_handlers: 1`,
  `tailscale_old_handlers: 1`, `required_scripts: .venv/bin/kronika-backup,.venv/bin/kronika-production`,
  all twelve environment path keys move and `preserved_path_keys` is empty. The
  timestamp is live (`SUDO_READY=0`). E4 apply decision presented to the
  Cooperator with the exact command binding the digest, the internal phase
  sequence, recovery branches and stop rules.

- **2026-10-11 — C6 apply stopped fail-closed at its first gate: the
  no-legacy-writers query misreads procps's empty-selection exit.**
  `migrate-identity apply` reported `former web account process state is
  unverifiable`, `MIGRATE_APPLY_EXIT=27`. `quiesce` had already stopped the web
  service and backup timers (writers stop first), then
  `assert_no_legacy_writers` ran `ps -u framenest -o pid= >/dev/null 2>&1`; with
  every framenest writer stopped the selection is empty, and procps-ng returns
  exit 1 for an empty selection — demonstrated locally (`ps from procps-ng
  4.0.7`: `ps -u nobody -o pid=` → exit 1 with empty output, `ps -u root` → 0) —
  which the guard maps to `query-failed` and refuses. `run_migration_apply` then
  wrote outcome `failed`, ran the automatic pre-write recovery
  (`recover_pre_write` restores the observed units and scheduling), and
  re-raised; no copy, rename, unit install or pointer switch ran. The failed
  journal remains, so a fresh apply refuses ("an incomplete migration journal
  exists; recovery is required first") and the parser has no explicit recovery
  subcommand — the journal must be archived (`mv` to a timestamped name, not
  deleted) under its own bounded authority after the host state is verified.
  Next: host-state checks, then a bounded correction of the process query with a
  fresh independent re-audit, then the journal archive, fresh preflight and
  retry.

- **2026-10-11 — Apply failure root cause and host state confirmed; ps-check
  correction issued.** NUC evidence: procps-ng 4.0.4; `ps -u nobody -o pid=`
  → exit 1 (empty selection), `ps -u framenest` → exit 0; the control directory
  holds `journal.json` (814 B) and `recovery-manifest.json` (1017 B), root-only
  `0600`; `framenest.service` and `framenest-catalog-backup.timer` are **active**
  — the automatic pre-write recovery restored the old layout and no destructive
  step ran. The defect is `cmd_remote_account_processes_absent`'s success
  criterion: procps-ng exit 1 for a valid user with zero processes is the normal
  post-quiesce state, not a query failure. `40_correction_00.md` (session 40,
  exchange 01) is the bounded correction: resolve the UID, verify the
  system-wide ps query itself, and count by UID so a valid user with zero
  processes returns `0` while a broken query or unknown user still returns
  `query-failed`; tests for the full matrix and mutation demonstrations. A fresh
  independent re-audit follows, then the failed journal is archived under
  bounded authority (`mv` to a timestamped name, not deleted), a fresh preflight
  is run, and the apply is retried with the new digest.

- **2026-10-11 — Process-query correction accepted at implementation level;
  fresh re-audit next.** `40_report_00.md` (session 40, exchange 01, PASS,
  `new-mutation`) reported commit
  `fcde631047650d1ff0a84b84bf185b54d6d11ba5` over `980041c`, two files,
  +224/−13. Orchestrator verification: the builder now resolves and validates
  the UID, takes one checked system-wide `ps -e -o uid=` snapshot, counts exact
  numeric UID matches with malformed-line detection, and returns `query-failed`
  for every genuine failure; focused modules **246 passed** (migration 231 +
  retention 15); full declared Python suite **4901 passed, 8 skipped,
  3 warnings, 0 failed** (676 s); Part A unchanged, Part B still 20 and Part C
  unmoved; tree clean; public `main` remains `980041c`. `41_audit_00.md`
  (session 41, exchange 01) is the fresh independent re-audit; after its PASS:
  publish `fcde631`, archive the failed journal under bounded authority, fresh
  preflight, apply retry.

- **2026-10-11 — Process-query re-audit (session 41) PASS; the C6 adapter is
  fully accepted.** `41_report_00.md` (session 41, exchange 01, Fresh Independent
  Audit, read-only, PASS, `new-evidence`) independently reproduced the
  three-outcome matrix (`0`/`1`/`N`/`query-failed`, decoys, quoting, malformed
  inputs) through both the repository boundary and an independent `/bin/sh`
  probe, verified the caller contract, quiesce order and pre-write recovery,
  detected all three mutations (`old-selection-guard`, `unchecked-ps`,
  `unguarded-uid`), and reproduced the checks exactly (migration 231, retention
  15, full suite 4901/8/3/0, 695 s). Non-blocking notes: a zero-padded UID field
  counts as a match and refuses the migration (safe); failure-expected cases
  could pass for the wrong reason only if the synthetic functions were omitted,
  which the success cases exclude. No blocking finding. Next: publish `fcde631`,
  archive the failed journal on the NUC (`mv` to a timestamped name), fresh
  preflight (the digest changes because the engine changed), then the apply
  retry under the same E4 window approval.

- **2026-10-11 — Publication PASS (`fcde631`), failed journal archived, fresh
  preflight PASS with a new digest.** Push `980041c..fcde631` with
  `PUSH_EXIT=0`; direct readback confirms `fcde631…` and local `main` in sync.
  The failed journal was archived as `journal.failed-20261011T145124Z.json`
  (814 B, preserved; `journal.json` gone) and `recovery-manifest.json` remains;
  `SUDO_READY=0`. Fresh `status`/`check` passed (layout `old`, `a37be37`,
  capture `94e605c`, service `active`, database `0035`, backup `ready`;
  `public_main` `fcde631`). Fresh `migrate-identity preflight` returned exit 0
  with the **new** `plan_digest:
  eef5b8f3793ebf3b63d2d0874d4df08622fbac2d7fd3b660700b95cfdaf7090e` (the engine
  changed), and the plan shape is unchanged: `copy_moves: 3`, `installed_dropins:
  4`, export installed at the old path, `sudo_rule_installed: absent`,
  `capture_pointer: old`, `tailscale_handlers: 1`, all twelve path keys move.
  Apply retry issued with the new digest under the same approved E4 window.

- **2026-10-11 — Apply retry stopped at phase 12 (`replace-ingress`), post-write;
  guard/classifier mismatch, host partially migrated with the new service
  running.** Output: `kronika-release: existing ingress handler target is
  unexpected`, `MIGRATE_APPLY_EXIT=27`. Cause, from the code: the observation's
  `parse_tailscale_serve_status` classifies a handler as the old web handler when
  its Proxy is either `unix+http://<old_socket>` **or** `unix:<old_socket>`, but
  `replace_tailscale_handler` then requires exact equality with
  `tailscale_unix_target(old_socket)` (`unix+http://…`). The live host's single
  handler is the `unix:` form, so the preflight passed and the apply refused.
  Failure position: `replace-ingress` (12 of 15), i.e. **after** `start-service`
  and `writes_possible`; `recover_post_write` touches nothing, so the host is
  left in the new layout: `kronika.service` active on `/run/kronika/kronika.sock`,
  account and state migrated, capture untouched, the Tailscale handler still
  pointing at the old socket (tailnet web unreachable), installed timers not
  resumed, and a failed post-write journal. Next: read-only state confirmation,
  then a bounded forward completion (surgical handler replacement with the
  helper's own command form plus exact scheduling resume), then a repository
  correction of the guard with a fresh re-audit.

- **2026-10-11 — Post-write state confirmed read-only.** Journal: all twelve
  phases through `start-service` completed; `current_phase:
  replace-tailscale-handler`; `outcome: failed`; `writes_possible: true`.
  `kronika.service` enabled+active; `framenest.service` disabled+inactive; both
  backup timers disabled+inactive. `/opt/kronika/current` →
  `/opt/kronika/releases/a37be37…`; `/opt/framenest/current` still points at the
  old tree. Tailscale Serve: one root handler at `:443` with `Proxy:
  unix:/run/framenest/framenest.sock` (the `unix:` form). Only
  `/run/kronika/kronika.sock` is listening. Forward completion: replace the
  handler with the helper's exact command form (`tailscale serve --bg
  unix+http:///run/kronika/kronika.sock`), resume
  `kronika-catalog-backup.timer` (observed enabled+active), then verify locally,
  through the tailnet, and archive the failed journal.

- **2026-10-11 — Forward completion, step 1: scheduling resumed; the ingress
  retry needs the host-accepted `unix:` scheme.** `kronika-catalog-backup.timer`
  is enabled+active (`ENABLE_EXIT=0`). The first handler replacement attempt used
  the engine's generated target `unix+http:///run/kronika/kronika.sock` and was
  **rejected by the installed Tailscale**: "must be a URL starting with one of
  the supported schemes: [http https https+insecure unix]" (`SERVE_EXIT=1`,
  handler unchanged). The correct form on this host is `unix:<path>` — the form
  the existing handler uses and the engine's verifier already accepts. This is a
  **second defect** in the C6 `replace_tailscale_handler` path (the guard's
  accepted-forms equality and the generated target scheme), for the pending
  guard correction. The PC `status` block was pasted into the NUC bash session
  by mistake (`cd` failed, `or` was not found, nothing ran); it must run in the
  Cooperator's fish terminal.

- **2026-10-11 — Ingress handler replaced with the host-accepted `unix:` form;
  helper `status` now fails with transport exit 20 and needs diagnosis.**
  `sudo -n tailscale serve --bg unix:/run/kronika/kronika.sock` returned
  `SERVE_EXIT=0`; Tailscale reports `proxy unix:/run/kronika/kronika.sock` and
  the Serve JSON root handler now points at the new socket. `kronika.service`
  remains active and `kronika-catalog-backup.timer` enabled+active. A later
  helper `status` run returned `kronika-release: command failed` with
  `STATUS_EXIT=20` (transport), i.e. some remote query in the status path exits
  non-zero on the new layout. Candidates: the service-account access
  (`sudo -n -u kronika`) after the account rename, the db/backup status commands
  with the new env file, the new-tree release markers, or the capture-pointer
  read. A targeted read-only probe replicates each command exactly before any
  conclusion. UI/tailnet confirmation of the restored web path is pending.

- **2026-10-11 — Status failure identified: the installed canonical env file is
  not readable by the service account.** `readlink` and `is-active` pass; the
  new tree carries `.kronika-release-sha` and `.kronika-release-manifest.json`;
  `sudo -n -u kronika true` works; the layout reads pass. The db-status route
  fails because `/etc/kronika/kronika.env` is `0600 root:root`, while the helper
  runs the CLI as `kronika` with `FRAMENEST_ENV_FILE=/etc/kronika/kronika.env`;
  the old file was `0640 root:framenest`. `framenest-backup status` still
  returns full JSON (`restore_readiness: ready`; the migration's checkpoint
  `auto-20261011T150355Z` is the latest successful scheduled backup at `0035`).
  The migration's install path therefore loses the observed env-file
  mode/ownership — **defect #3** for the C6 completion correction set (with the
  guard accepted-forms equality and the `unix:` target scheme). Immediate bounded
  remediation: `chown root:kronika` and `chmod 0640` on the env file, then
  `kronika-release status` and the UI check. The web path itself is already
  restored (handler → new socket; service active).

- **2026-10-11 — C6 host cutover functionally complete: `kronika-release status`
  passes on the new layout.** After the bounded env-file remediation
  (`root:kronika`, `0640`), `status` reports `layout: new`,
  `active_release`/`web_release` `a37be37…`, `release_path
  /opt/kronika/releases/a37be37…`, capture `94e605c…` unchanged,
  `service_active: active`, `database_revision: 0035`,
  `backup_restore_readiness: ready`, exit 0. The web path was restored by the
  manual `unix:` handler replacement; scheduling is resumed
  (`kronika-catalog-backup.timer` enabled+active); the migration's checkpoint
  (`auto-20261011T150355Z`, revision `0035`) is the latest successful scheduled
  backup. Remaining: archive the failed retry journal, then one bounded
  C6-completion correction (guard accepted forms, the `unix:` target scheme, and
  the env-file mode/ownership installation) with tests and a fresh re-audit;
  Cooperator UI/tailnet rendered confirmation still pending.

- **2026-10-11 — Cooperator confirmed the tailnet URL loads: C6 rendered path
  accepted.** His usual tailnet address loads — server `a37be37` on the new
  layout, ingress via `unix:/run/kronika/kronika.sock`. The C6 host cutover is
  complete end-to-end (functionally and rendered). `42_correction_00.md`
  (session 42, exchange 01) is the single bounded C6-completion correction for
  the three live defects: the `replace_tailscale_handler` accepted-forms guard
  (`unix:` vs `unix+http://`), the generated replacement-target scheme (the
  installed Tailscale rejects `unix+http://`), and the env-file mode/ownership
  installation (`0600 root:root` instead of the account-readable
  `0640 root:<account>`). A fresh independent re-audit follows; the failed retry
  journal is archived under bounded authority.

- **2026-10-11 — `42_correction_00.md` issued (session 42, exchange 01, task
  `KSI-CORR-C6COMP`): the single bounded C6-completion correction.** Required
  outcomes: (D-1) one shared accepted-spelling source of truth so the
  `replace_tailscale_handler` guard, `parse_tailscale_serve_status` and
  `verify_ingress` accept exactly the classified former/new spellings and the
  guard refuses everything else; (D-2) the replacement target mirrors the
  observed former handler's scheme (`unix:<old>` → `unix:<new>`,
  `unix+http://<old>` → `unix+http://<new>`); (D-3) environment-file parity —
  observe the former file's owner/group/mode evidence, carry it as a bound plan
  fact, apply the mapped ownership (former-account group mapped through the
  identity transition; live `root:framenest:0640` → `root:kronika:0640`) after
  the atomic move, and verify installed evidence with fail-closed
  absent/unsafe/query-failed handling. Baseline `fcde631`, measured focused
  migration module `231 passed`, retention `15 passed`, full suite `4901/8/3/0`.
  Repository-only, no host contact; one local commit; mutations plus
  focused/full/retention runs required. A fresh independent re-audit (session
  43) must PASS before the failed journal is archived and C6 is closed; the
  journal stays in place until then.

- **2026-10-12 — `42_report_00.md` accepted after independent Orchestrator
  verification.** Worker session 42 delivered commit
  `e9413dff98605443e7d17557f498c87433c93e92` (parent `fcde631…`, exactly two
  files, +551/−24, one commit, no push; `origin/main` still `fcde631`; tree
  clean). Verified independently: committed file SHA-256s match the report's
  tested bytes (`kronika_release.py` `1708ebf3…`,
  `test_kronika_identity_migration.py` `9180f511…`); the engine diff matches the
  three declared corrections (shared `tailscale_unix_targets` across
  classifier/guard/verifier, scheme-mirroring replacement, plan-bound
  environment-file evidence with post-move ownership/mode application and
  installed-evidence verification plus raw-source-digest check); focused
  migration module `285 passed`; retention module `15 passed` with the ledger
  unmodified (⇒ Part A 86/36, Part B 20 and all Part C pins green); full
  declared suite `4955 passed, 8 skipped, 3 warnings, 0 failed` in 677.27s.
  Material qualification (Worker MEASURED critique): the prompt's literal D-3
  intermediate (`chown root:kronika` inside `transform-environment`) cannot
  coexist with the unchanged phase order — installation precedes
  `rename-account`, so the observed group name is applied and verified
  pre-rename, and the existing group rename canonicalizes it
  (`root:framenest:640` installed → `root:kronika:640` final). The engine also
  refuses a former-account-owned former file (documented, fail-closed). Both
  choices go to the fresh audit for an explicit verdict.
  `43_audit_00.md` (session 43, exchange 01, `KSI-AUDIT-C6COMP`) is issued as
  the fresh independent re-audit, explicitly covering the D-3 phase-order
  interpretation, all three matrices and an independent full-suite run; the
  failed C6 journal stays in place until its PASS.

- **2026-10-12 — `43_report_00.md` PASS accepted: the C6 completion correction
  is independently certified and C6 close is authorized.** The fresh audit
  re-verified identity/scope (candidate `e9413df…`, exactly two paths, phase
  order / method map / journal / recovery unchanged), the full ingress
  spelling/refusal matrix, the environment parity and evidence-binding matrix,
  and the five mutation demonstrations (in-memory only, all detected). D-3
  verdicts: phase-order interpretation confirmed (`transform-environment`
  precedes `rename-account`; `chown root:kronika` at install time cannot
  succeed on a host that passed preflight; observed-group-name application plus
  the existing GID-preserving rename yields `root:kronika:640`); non-account
  groups preserved without widening; the former-account-owner refusal is
  fail-closed-correct, not a supported shape. Checks at the candidate: focused
  `285`, retention `15`, full suite `4955 passed, 8 skipped, 3 warnings, 0
  failed` (689.12s), Part A 86/36, Part B 20, Part C no movement. No blocking
  finding. Non-blocking residuals (recorded, not reopened): verifier accepts
  either new spelling (specified); plan-count-zero skips ingress readback under
  a concurrent handler change (LEAD; command failure still aborts);
  out-of-range forged index raises `IndexError` outside `ReleaseError`;
  unsearchable-parent evidence reads as absent (fail-closed); a post-move
  `chown`/`chmod` failure leaves the new path without pre-write deletion while
  the former file is untouched; ACLs/xattrs are not copied. The failed C6
  journal archive is the closing action, granted with the C7-A/S handoff.

- **2026-10-12 — C7-A/S grant issued: `44_implementation_00.md` (session 44,
  exchange 01, `KSI-IMPL-C7AS`).** Scope: canonical server companion web
  emissions — `companion_host.js` emits `kronika.companion.web.v1` at every
  outbound site and accepts both spellings; the two source-regex multiset
  assertions in `tests/companion_web_bridge.test.js` are deleted, not re-pinned,
  and replaced with behavioral emission/acceptance proofs; the served-asset
  contract test asserts the canonical emission plus the retained retired
  reader; Part C re-pin only if measured. Baseline `e9413df`; measured
  baselines: JS `14/40/213`, Python `4955/8/3/0`, retention `15`.
  Repository-only, one local commit, no push; publication and the exact-main
  NUC refresh are arranged separately after acceptance and must precede
  C7-A/C.

- **2026-10-12 — C6 closed on the host: the failed retry journal is archived.**
  The archive block ran under bounded authority: `journal.json` (1323 bytes,
  the ingress-refusal retry) → `journal.failed-20261011T230854Z.json`. The
  earlier `journal.failed-20261011T145124Z.json` and the
  `recovery-manifest.json` from the first attempt's automatic pre-write
  recovery stay in place; nothing was deleted. C6 is closed: the new layout is
  served and rendered, `kronika-release status` is green on the new layout,
  the backup timer is resumed, capture is untouched, and the correction set is
  implemented, deployed to the live host manually, and independently audited
  (session 43 PASS).

- **2026-10-12 — `44_report_00.md` accepted after independent Orchestrator
  verification (C7-A/S).** Commit `7c1cee299e14dbccaca10fe0ce749b4dc7553420`
  (parent `e9413df…`, exactly four files, +235/−73, one commit, no push;
  `origin/main` still `fcde631`). Verified: the served host asset emits
  `kronika.companion.web.v1` at every outbound site and accepts both spellings
  (`ACCEPTED_WEB_PROTOCOLS`, guarded `.includes(data.v)`); the contract comment
  is truthful; exports extended. Both source-regex multiset assertions and the
  `countOccurrences` helper are deleted, not re-pinned, and replaced with
  behavioral proofs: host sends captured through `postMessage` (WEB_READY,
  HOST_ACK, ATTACH_REQUEST all canonical, pinned origin), both inbound
  spellings exercised across HOST_HELLO/ATTACH_RESULT/OPEN_DETAILS with the
  23-value refusal matrix and positive controls, extension unchanged (emits
  retired, accepts both). The served-asset contract asserts the canonical
  emitter and the retained retired reader. Part C re-pinned `src` 1706→1705
  and `tests` 2283→2282 with the running-cause ledger entry; Part A 86/36 and
  Part B 20 unmoved; membership 516. Independent runs at the candidate: bridge
  JS `27 passed`, extension+UI JS `82 passed`, bounded non-browser glob `213
  passed`, focused Python `225 passed` (43.6s), retention `15 passed`, full
  suite `4955 passed, 8 skipped, 3 warnings, 0 failed` (675.54s). Publication
  and the exact-main NUC refresh are the next step; the Cooperator's rendered
  acceptance against the served canonical server with the current extension
  build precedes C7-A/C.

- **2026-10-12 — C7-A/S served: NUC refreshed to `7c1cee2`.** `git push
  origin main` published `fcde631..7c1cee2`; `status` + `check --release
  7c1cee2…` passed (layout new, backup ready, `CHECK_EXIT=0`); `kronika-release
  deploy --release 7c1cee299e14dbccaca10fe0ce749b4dc7553420 --yes` completed
  (`DEPLOY_EXIT=0`). Status now: new layout, active/web release `7c1cee2…`,
  capture `94e605c…` unchanged, DB `0035`, backup ready. The plan's
  precondition for the companion transition — the canonical server published
  and served — is met. Rendered spot-checks pending: the served
  `/assets/companion_host.js` spelling and a UI load check.

- **2026-10-12 — Save retry succeeded; automatic AI analysis fails — under
  diagnosis (possibly unrelated to C6).** The retry after the deploy cataloged
  the item successfully, but the automatic post-catalog AI analysis failed; the
  earlier pre-deploy attempt had shown "Save to Kronika failed". The analysis
  failure is persisted by the lifecycle with a classified error
  (`PROVIDER_NOT_CONFIGURED`/`PROVIDER_AUTH`/`PROVIDER_RATE_LIMITED`/
  `PREPARATION_FAILED`/…). Candidate causes: provider credential or config
  after the C6 transform, provider availability, or local preparation.
  Read-only diagnostics requested: env AI keys, the runtime-settings overlay,
  the AI config, credential drop-ins with `LoadCredential`, the state dirs and
  the service journal, plus the UI error detail. Not yet classified as a C6
  side effect; no host mutation authorized.

- **2026-10-12 — Save and AI analysis verified working; earlier failures
  classified as transient.** The credential diagnostics confirmed
  `LoadCredential=NVIDIA_API_KEY:/etc/kronika/credentials/NVIDIA_API_KEY`,
  both mounted credentials present under `/run/credentials/kronika.service/`
  (`NVIDIA_API_KEY`, `KRONIKA_RESEARCH_OPENAI_API_KEY`), the AI config
  selecting `nvidia-nim` with its model, and
  `AUTOMATIC_MEDIA_ANALYSIS_ENABLED=true`. The analysis retry succeeded
  ("AI funguje") and the save had already been confirmed cataloged. The single
  failed analysis and the earlier failed save attempt are classified as
  transient/environmental — auth, model and configuration are proven healthy by
  the successful retries; the exact transient code was not captured. Not a
  C6-window defect on current evidence. The served canonical web asset was
  verified from the tailnet (`const PROTOCOL = "kronika.companion.web.v1"` plus
  the dual accepted set).

- **2026-10-12 — C7-A/S scoping miss found; completion correction issued:
  `45_correction_00.md` (session 45, `KSI-CORR-C7AS-API`).** The plan's §2.11
  names two server emissions: the web-host emission (done and served in
  `7c1cee2`) and the server companion API version. The latter is still the
  retired spelling: `companion_picker.py` declares
  `COMPANION_API_VERSION = "framenest-companion.v1"`, emitted as
  `companion_api_version` by `x_companion_api.py` and pinned by two contract
  tests; the extension already dual-accepts (`ACCEPTED_API_VERSIONS`), and its
  comment names this switch as C7-A/S's. The correction flips the constant to
  `kronika-companion.v1`, flips exactly the emitted-literal pins, keeps every
  reader unchanged, and re-pins only measured Part C movement (expected
  `src` −1, `tests` −2; verify by measurement). After acceptance: publish and
  exact-main refresh so the served server carries both canonical emissions,
  then the companion cut (`C7-A/C`).

- **2026-10-12 — `45_report_00.md` accepted after independent Orchestrator
  verification (C7-A/S completed).** Commit
  `c152a178dcfbbe6e8f04f98d1b9f3f8cb7aea209` (parent `7c1cee2…`, exactly four
  files, +22/−5, one commit, no push). Verified: `COMPANION_API_VERSION` is now
  `kronika-companion.v1` and both emitted-literal pins assert the canonical
  spelling; the 92-hit inventory classified every occurrence (extension reader
  and its acceptance lines kept; DOM attributes and env-key spellings reported
  for later cuts); the mutation demonstration flipped the constant back and
  both pins failed as intended. Independent runs: focused companion modules
  `97 passed`, JS extension suite `40 passed`, retention `15 passed`, full
  suite `4955 passed, 8 skipped, 3 warnings, 0 failed` (670.89s); Part C
  re-pinned `src` 1705→1704 and `tests` 2282→2280 with the recorded cause,
  Part A 86/36 and Part B 20 unmoved. C7-A/S is now complete in the repository:
  both server emissions (web-host protocol and companion API version) are
  canonical with compatible readers retained. Recorded residual: the extension
  comment `messages.js:9–11` ("the server keeps emitting the retired spelling
  until a later cut moves COMPANION_API_VERSION") is now stale by design and is
  updated in the companion cut, which owns `extension/**`. Next: publish and
  routine exact-main refresh, then `C7-A/C`.

- **2026-10-12 — C7-A/S completion published; deploy granted and C7-A/C
  issued.** `git push origin main` published `7c1cee2..c152a17`;
  `status` (pre-deploy `7c1cee2` active, backup ready) and
  `check --release c152a17…` passed (`public_main: c152a17…`,
  `superproject_sha256: 2fb008c9…`, `CHECK_EXIT=0`). The deploy block follows;
  in parallel the C7-A/C implementation grant `46_implementation_00.md`
  (session 46, exchange 01, `KSI-IMPL-C7AC`) is issued: canonical companion
  emissions (extension web protocol; mutation header canonical-only), internal
  ports/messages, JavaScript globals moved together — the extension's six
  globals and origin helpers plus the served companion web host global
  `FrameNestCompanionWeb` — the `data-framenest-*` DOM family with style
  agreement, stored-state completion (write-verify-remove; retired duplicate
  alarm cleared) and the corrected stale API-version comment, with every
  retired reader retained until C7-B. Measured baselines: JS
  `27/40/53/6/12/30/213`, focused Python `225`, retention `15`, full suite
  `4955/8/3/0`. Rendered acceptance (extension reload against the refreshed
  exact-main server) follows the post-46 publication and refresh.

- **2026-10-12 — `46_report_00.md` accepted after independent Orchestrator
  verification (C7-A/C).** Commit
  `aee0a60a04b78685608ec5a65ec5780c7d9884e7` (parent `c152a17…`, exactly 20
  files, +681/−355, one commit, no push). Verified: the extension emits the
  canonical web protocol and only `X-Kronika-Request`; the internal tokens
  (`kronika-attach`, `kronika-save-popup`/`-host`), the six extension globals
  and origin helpers (`canonicalizeKronikaOrigin`/`acceptKronikaOrigin`), and
  the served companion web-host global (`KronikaCompanionWeb` in
  `companion_host.js`/`app.js`) moved with every reference; the
  `data-framenest-*` family is fully `data-kronika-*` with the agreement proof
  (`data-framenest-` 140→1, the negative assertion; `data-kronika-` 38→187);
  stored-state completion writes, verifies, then removes (operation order
  `get,get,set,get,remove`), canonical wins on conflict, a failed readback does
  not remove, reset does not resurrect, and the retired alarm
  `framenest.review-inbox` is cleared once when the companion is configured
  while the listener still serves it; every retired reader is retained for
  C7-B. Independent runs: JS `27/42/54/6/12/30` plus the bounded glob `213`,
  focused Python `225`, retention `15` (Part C: `src` 1704→1695, `tests`
  2280→2190, `extension` 145→4; file counts `tests` 186→185, `extension` 8→2;
  mutation-header counts 73/30→69/29), full suite `4955 passed, 8 skipped, 3
  warnings, 0 failed` (671.58s); Part A 86/36 and Part B 20 unmoved.
  Classifications recorded: the served shell's dual mutation-header emission
  (`app.js framenestMutationHeaders`) is a deliberate retained compatibility
  emission (survives rollback and cached shells; C7-B removes readers only);
  the remaining `FrameNestCompanion*` hits are the excluded Python class-name
  residue; `framenest-media.bin` in tests is a synthetic fixture. Residual
  LEAD (non-blocking): the sidebar/picker storage migration runs outside the
  worker's serialized origin queue, so a reset interleaving could be
  overwritten; the cheapest check is one synthetic interleaving of
  `completeStoredEntryMigration` with `resetState`. Next: publish `aee0a60`,
  exact-main refresh, extension reload and the Cooperator's rendered
  acceptance against the actual server/extension pair; C7-B follows that
  acceptance.

- **2026-10-12 — `aee0a60` published and refreshed to the NUC; rendered
  acceptance pending.** `git push origin main` published `c152a17..aee0a60`;
  the pre-deploy status showed the intermediate `c152a17` refresh had landed;
  `check --release aee0a60…` passed (`public_main: aee0a60…`,
  `superproject_sha256: 5158cc19…`, backup ready, `CHECK_EXIT=0`) and
  `deploy --release aee0a60… --yes` completed (`DEPLOY_EXIT=0`). Post-deploy
  status: new layout, active/web release `aee0a60…`, capture `94e605c…` and
  DB `0035` unchanged, service active, backup ready. The served server now
  carries both canonical server emissions (web protocol and companion API
  version); the extension revision `aee0a60` is what the Cooperator reloads
  for the rendered acceptance against the actual pair. Acceptance checklist
  awaiting results: extension reload, stale panels closed and pages refreshed,
  hosted shell load, history/inbox, attach, save (canonical header only),
  hosted details.

- **2026-10-13 — C7-A closed: the Cooperator's rendered acceptance passed
  ("Všetko ok").** Against the actual served pair (server `aee0a60`, extension
  revision `aee0a60` after reload, stale panels closed and pages refreshed):
  the hosted shell loads, history/inbox loads, attach works, a save works with
  the canonical header only, and hosted Details open. C7-A as a whole
  (C7-A/S + C7-A/C) is accepted; the whole moves to C7-B.

- **2026-10-13 — C7-B grant issued: `47_implementation_00.md` (session 47,
  exchange 01, `KSI-IMPL-C7B`).** The removal cut: the fourteen retired
  console aliases leave `pyproject.toml`; the twenty Part B paths are deleted
  (ten systemd artifacts, three Ubuntu wrappers, the root `framenest` launcher,
  three infosec and three network scripts) with every consumer reconciled
  first; old environment/SSH fallbacks and their shell mirrors are removed
  only after new `_env_*` parity coverage characterizes canonical behavior;
  the retired protocol/header/browser-key readers are removed (server escaped
  header acceptance, host retired web protocol, extension retired
  protocol/API version/browser keys/alarm) while the served shell's dual
  mutation-header emission stays as rollback safety; emitted command error
  codes become `KRONIKA_*` with numeric statuses preserved; local defaults and
  workstation recovery become canonical-only with the legacy-state safeguard
  retained; finishing items cover production credential tooling, backup/export
  defaults, temporary operational names,
  `scripts/operator/network/README.md` and the AGENTS.md transitional
  sentences; and the ledger moves Part B to the empty set with measured Part C
  re-pins and Part A unmoved. Repository-only: the `.venv` environment refresh,
  the wheel/console evidence, publication and the exact-main refresh remain
  separate Cooperator steps. Measured baselines: full suite `4955/8/3/0`, JS
  `27/42/54/6/12/30/213`, focused Python `225`, retention `15`.

- **2026-10-14 — Session 47 stopped cleanly (BLOCKED): acceptance-criterion
  conflict in the C7-B grant; no mutation.** The Worker correctly refused to
  start: verification item 3 demanded no remaining reference to a deleted path
  while the grant also required frozen Part A documents to stay byte-unmoved,
  and frozen entries carry historical references. The Orchestrator's full
  sweep found **29 frozen entries** carrying deletion-target references — the
  ADRs 0012, 0015, 0016, 0020, 0025, 0026, 0031, 0032, 0033, 0036, 0047,
  0048, 0050, 0052, 0056, 0057, 0058, 0059, 0060, 0061, 0063, 0064, 0069,
  0074, 0075, 0076 and 0082, plus `docs/FEDORA_SERVICE.md` and
  `docs/NUC_HOST_BASELINE.md`. No deletion target is itself a frozen entry.
  `48_implementation_00.md` (session 48, exchange 01, corrected `KSI-IMPL-C7B`
  re-issue) fixes the criterion: frozen references are history and exempt, only
  **active** consumers must be reconciled before a deletion, the complete
  frozen sweep is verification step one, and a stop is reserved for a deletion
  target being frozen or an edit being required to a frozen document.

- **2026-10-14 — Session 48 returned PARTIAL: C7-B does not fit one session;
  split into three bounded grants.** It completed only the parity-first
  checkpoint — 14 parametrized settings-parity cases added to
  `tests/contract/test_kronika_settings_parity.py` (+80 lines, module 37
  passed, green) — with no removals, no staging and no commit; the sole change
  remains unstaged (sha256 `ce54c7e6…`) and is adopted as the foundation of
  C7-B/1. It re-confirmed the frozen inventories (86/36), the twenty targets
  and the absence of any frozen overlap, and produced a partial consumer
  inventory (known sites: `deploy/ubuntu/production_ai_deploy.py`,
  `catalog_backup_workstation.py`, CLI parser names, migration guidance,
  deployment artifact tests, release-contract tests, active root
  documentation). Its MEASURED critique — the 29-entry frozen list matches a
  broad token search rather than exact deletion-path references — is recorded;
  the later grants state the matcher scopes separately. Split: **C7-B/1**
  settings/defaults/codes (session 49); **C7-B/2** physical removals
  (consoles, twenty paths, operator-script mirrors) and the retired readers;
  **C7-B/3** finishing tooling and active instructions. One commit and one
  measured ledger movement per grant.

- **2026-10-14 — C7-B/1 grant issued: `49_implementation_00.md` (session 49,
  exchange 01, `KSI-IMPL-C7B1`).** Scope: settings sources canonical-only
  (remove the `FRAMENEST_` fallbacks in `identity_env.py`/`configuration.py`;
  preserve the characterized case/empty/precedence behavior; keep
  `lookup_field_value` and `lookup_env` distinct); the release engine's
  `FRAMENEST_ENV_FILE` → `KRONIKA_ENV_FILE`; the 42 emitted `FRAMENEST_*` code
  values → `KRONIKA_*` with numeric statuses preserved; canonical development
  defaults with the legacy-state refusal demonstrated; canonical-only
  workstation recovery (`--remote-layout` removal); Part C re-pins with
  causes; Part B stays 20 in this grant. The unstaged parity file is adopted
  continuation with its hash pinned in the prompt.

- **2026-10-14 — Session 49 BLOCKED (clean): C7-B/1 candidate preserved
  uncommitted; one authority gap.** It implemented the full B/1 surface — 50
  files (+764/−938): 12 production paths
  (`kronika_release.py`, `cli/backup.py`, `cli/catalog.py`, `cli/recovery.py`,
  `configuration.py`, `identity_env.py`, `ai/configuration.py`,
  `catalog_backup_workstation.py`, `persistence/cli.py`,
  `runtime/development.py`, `local_state_migration.py`,
  `runtime/production.py`) and 38 tests/support — with settings canonical-only
  and the 14 adopted parity cases unchanged (55 passed with resolver units),
  the engine `KRONIKA_ENV_FILE` switch, 37 emitted code values renamed
  (42 literals = 37 codes + 5 development variables), canonical development
  defaults with the demonstrated legacy-state refusal, recovery
  canonical-only, and focused modules 368 passed. It stopped before staging
  because the authorized edits removed the last retired-name occurrence from
  exactly four files (`test_library_cli.py`, `test_operator_cli_hygiene.py`,
  `test_ai_configuration_storage.py`, `test_catalog_backup_ops.py`) whose
  `EXPECTED_FRAMENEST_CONTENT_PATHS` entries my scalar-only authority did not
  permit removing. Two stale assertions remain
  (`test_release_helper_still_injects_the_old_env_file_name`,
  `test_development_database_directory_is_unchanged`), the cleanup review is
  incomplete (obsolete conflict helpers), the four mutation demos and the full
  suites were not run, and no commit exists. Part A verified byte-unmoved,
  Part B still 20; no active document names an emitted code — the sole
  document reference is the frozen ADR-0047. `50_implementation_00.md`
  (session 50, exchange 01,
  `KSI-IMPL-C7B1` continuation) adopts the candidate (state and parity hash
  pinned) and authorizes exactly the four departures, the stale assertions,
  the cleanup review, the demos, the suites and the commit.

- **2026-10-14 — Session 50 BLOCKED (clean): C7-B/1 candidate complete; one
  pattern class remains.** It applied the four content-path departures,
  renamed and corrected both stale assertions
  (`test_release_helper_injects_the_canonical_env_file_name`,
  `test_development_database_directory_is_canonical`), completed the cleanup
  review (caller-free helpers removed; referenced conflict types retained;
  `lookup_env`/`lookup_field_value` still distinct), performed all four
  mutation demonstrations (each detected), updated the retention module (now
  the 51st modified path; **51 files, +815/−977**), and ran focused modules
  `439 passed` plus retention `15` and all JS suites (`27/42/54/6/12/30` +
  glob `213`). The full suite exposed three failures in
  `tests/contract/test_catalog_backup_timer.py`, whose `_ops_env` fixture still
  supplies five retired environment names plus a retired keep-auto name;
  canonical-only resolution ignores them, so the commands fail — a
  fixture-input repair outside its authority. No commit. Part A byte-unmoved
  (86/36), Part B still 20; final Part C candidate: `src` 1695→1630, `tests`
  2190→1891 (four content-path departures), `deploy` 248→246, env tokens
  702→381, distinct 114→74, bare 53→44, capitalized 2681→2663, host paths
  −2/−2/−1. LEAD: the retired-fixture pattern may exist in further modules.
  `51_implementation_00.md` (session 51, final C7-B/1 continuation) adopts the
  candidate, closes the fixture-input class across every test module
  (behavioral assertions preserved, inputs canonicalized), completes the
  obsolete two-prefix premise test, requires a completed green full suite,
  final ledger measurements and the single commit.

- **2026-10-14 — Session 51 BLOCKED (clean): the fixture class is closed; a
  product-string pin family remains.** It canonicalized the timer fixture
  inputs (five retired names plus the keep-auto name and two API-key pops
  across `test_catalog_backup_timer.py` and `test_catalog_offdevice_timer.py`)
  with every behavioral assertion preserved and the three known timer failures
  gone; retired the vacuous two-prefix premise test with cause (canonical
  success still covered by the ordinary-status test); completed the retired
  input-consumer inventory (ignore-proofs and still-accepting consumers left
  unchanged with causes); and ran the completed full suite:
  `4 failed, 4967 passed, 8 skipped, 3 warnings` (695.46s). All four failures
  are in `tests/contract/test_kronika_product_string_agreement.py` — measured
  inventory length 63 against the pin 57, `"Kronika"` duplicate multiplicity 8
  against 2, the six unexpected nodes being the candidate's canonical
  development path constants — outside the closed pattern classes, so it
  stopped. Focused `95 passed`; retention `15`; JS `27/42/54/6/12/30` + `213`
  green. Candidate now **53 files, +838/−1005**; ledger updated (`tests`
  1891→1883, environment tokens 381→373, nothing else moved).
  `52_implementation_00.md` (session 52, exchange 01, closing continuation)
  adopts the candidate, authorizes the product-string inventory completion to
  the measured truth (never weakening into a prefix or subset check), grants
  broad test-side completion authority for any further measured mismatch
  (production sources frozen), and requires the green full suite and the
  single commit.

- **2026-10-14 — `52_report_00.md` accepted after independent Orchestrator
  verification: C7-B/1 committed.** Commit
  `6531965e5406805a17dc9a68e26d03d9e78e8260` (parent `aee0a60…`, exactly 54
  files, +859/−1008, one commit, no push; `origin/main` still `aee0a60`).
  Verified: the resolver is canonical-only (`identity_environment_names`
  removed, `canonical_identity_environment` keeps canonical keys only, the
  settings sources renamed `_Canonical*` with `env_prefix="KRONIKA_"`,
  `lookup_env` and `lookup_field_value` still distinct); the release engine
  injects `KRONIKA_ENV_FILE`; recovery codes are canonical and
  `--remote-layout` is gone; the development defaults are canonical with the
  legacy-state refusal wired into `DevelopmentRuntime.start()`; the timer
  fixtures are canonical inputs with every assertion intact; the product-string
  inventory pins are completed (`OCCURRENCE_COUNT` 57→63, `"Kronika"`
  duplicates 2→8, six new path-component nodes); the ledger records the
  combined movement (`src` 1695→1630, `tests` 2190→1883, `deploy` 248→246,
  environment tokens 702→373, the four content-path departures; Part A 86/36
  and Part B 20 unmoved). Independent runs: focused `78 passed`, JS
  `27/42/54/6/12/30` plus the bounded glob `213`, full suite `4971 passed, 8
  skipped, 3 warnings, 0 failed` (673.94s). C7-B/1 accepted.
  `53_implementation_00.md` (session 53, `KSI-IMPL-C7B2A`) opens C7-B/2a: the
  retired reader removals (server mutation header, host web protocol,
  extension protocol/API version/browser keys/alarm) with their tests, the
  ledger movement and one commit; the physical removals (consoles, twenty
  paths, operator scripts) follow as C7-B/2b and the finishing documents as
  C7-B/3.

- **2026-10-15 — `53_report_00.md` accepted after independent Orchestrator
  verification: C7-B/2a committed.** Commit
  `6dd72f65976412bf92d672f9349bbd74752b0f39` (parent `6531965…`, exactly 26
  files, +311/−495, one commit, no push). Verified: the server accepts only
  `X-Kronika-Request: 1` (the retired constant and dual authorization are
  removed; the message names the canonical header; every rejection code and
  numeric status is unchanged); the host accepts only the canonical web
  protocol; the extension loses the retired protocol, API version, browser-key
  fallbacks and the retired alarm name, with the completed migration helpers
  removed and every unrelated stored key unchanged; the picker's startup
  migration call is gone. Refusal matrices and three mutation demonstrations
  recorded. Independent runs: JS `23/41/55/6/12/30` plus the bounded glob
  `212`, focused Python `342 passed`, full suite `4971 passed, 8 skipped, 3
  warnings, 0 failed` (684.22s). Ledger: `src` 1630→1627, `tests` 1883→1810,
  `extension` 4→0 occurrences and 2→0 files, content paths 505→502, retired
  mutation-header occurrences 69→43 across 29→19 files; Part A 86/36 and
  Part B 20 unmoved. Active-document findings carried to C7-B/3:
  `SECURITY.md`, `docs/UBUNTU_NUC_DEPLOYMENT.md`,
  `docs/ACCEPTANCE_DUAL_AUDIENCE.md`, `ROADMAP.md`, `docs/X_COMPANION.md`,
  `scripts/operator/network/README.md`, `AGENTS.md`.
  `54_implementation_00.md` (session 54, exchange 01, `KSI-IMPL-C7B2B`) opens
  C7-B/2b: the fourteen console aliases out of `pyproject.toml`, the twenty
  Part B paths deleted with every active consumer reconciled before deletion,
  the retained operator scripts' retired fallback mirrors removed, the empty
  Part B ledger set and the measured Part C re-pins. The Cooperator `.venv`
  refresh follows the commit; C7-B/3 and the final publication/refresh/rendered
  acceptance close the cut.

- **2026-10-15 — Session 54 (C7-B/2b) returned PARTIAL: stopped before
  mutation on context pressure; no changes, no commit.** It verified the
  gates, the 86/36 frozen sets and the empty target/frozen intersection, and
  produced a partial consumer inventory whose key findings are now carried
  forward: the capture packaging contract requires `framenest-chatgpt-page` in
  the wheel; the migration contract derives tests from a nonempty Part B and
  needs non-vacuous coverage for the empty-set transition;
  `production_ai_deploy.py` reads the three retired credential templates with
  coupled destinations; the release and worker-execution contracts require the
  retained wrappers, and `test_worker_execution_contract.py` asserts the
  `AGENTS.md` and `docs/WORKER_EXECUTION_CONTRACT.md` sentences that name
  them. Matcher scopes measured separately: exact deletion paths plus
  `./framenest` → 11 frozen docs; exact fourteen console names → 18; broader
  `framenest[-_.]` → 29; case-insensitive → 77. Its report file had been
  stored as `55_report_00.md` while its session ordinal is 54; the Meta file
  was renamed to `54_report_00.md` to keep the numbering mapping exact.
  `55_implementation_00.md` (session 55, exchange 01, `KSI-IMPL-C7B2B`
  re-issue) carries the session-54 inventory into the grant, broadens the
  reconciliation authority to every actively-consuming path (engines and
  their contract tests, packaging, migration, worker-execution and release
  contracts, `production_ai_deploy.py` and `fn-production-env-deploy`, the
  engine's temporary `REMOTE_DEPLOY_DIR`, backup/export defaults), requires
  the coupled minimal edits in `AGENTS.md` and
  `docs/WORKER_EXECUTION_CONTRACT.md` exactly where the worker-execution test
  checks them, the empty Part B set with non-vacuous coverage, and the single
  local commit.

- **2026-10-15 — `55_report_00.md` accepted with a recorded incident: C7-B/2b
  committed.** Commit `551dd397b3cd5c9c4f5e3b1eec1cd01ea8ba0d4f` (parent
  `6dd72f6…`, exactly 72 files, +751/−2669, one commit, no push; twenty
  deleted paths confirmed path-by-path). The fourteen retired console aliases
  are gone (exactly fourteen canonical remain); the operator scripts' retired
  fallback mirrors are removed with their canonical variables retained; the
  engine's `REMOTE_DEPLOY_DIR` is `/run/kronika-release-deploy`;
  `production_ai_deploy.py` and `fn-production-env-deploy` are canonicalized;
  the coupled sentences in `AGENTS.md` and
  `docs/WORKER_EXECUTION_CONTRACT.md` are updated; the runbook carries
  eighteen coupled substitutions; the ledger's Part B set is `frozenset()`
  with a non-vacuous `CANONICAL_REPLACEMENT_PATHS` (twenty pinned canonical
  counterparts); the whole-tree sweep scopes stay separated (11/18/29/77).
  Independent runs: JS `23/41/55/6/12/30` plus the bounded glob `212`,
  focused `505 passed`, full suite `4968 passed, 8 skipped, 3 warnings, 0
  failed` (674.05s; the −3 net from the gate-helper/mirror-test
  reparametrizations is explained in the report). **Incident disposition:**
  during an early harness edit a collapsed Fish escape (`$$primary_name` →
  `$primary_name`) let two gate tests reach the real `ssh` binary and local
  agent discovery against the synthetic host `nuc-magicdns-name` under a
  hermetic `HOME`; the attempts failed at name resolution (status 255), no
  NUC connection succeeded, and no socket or credential value was printed.
  The harness was corrected and a containment precheck added (the resolver is
  exercised in isolation and asserted to return the synthetic `1` before the
  gate executes); the Orchestrator verified the precheck at
  `tests/contract/test_operator_network_scripts.py` lines 503–514 and re-ran
  the suites with the corrected harness. Classification: boundary deviation,
  contained, no host contact, no disclosure; accepted with the incident
  recorded and the forward rule that any operator-script harness edit must
  preserve the isolation precheck.

- **2026-10-15 — C7-B/3 grant issued: `56_implementation_00.md` (session 56,
  exchange 01, `KSI-IMPL-C7B3`).** Scope: sweep every active (non-frozen)
  document to the canonical truth (the carried findings list includes
  `SECURITY.md`, `docs/ACCEPTANCE_DUAL_AUDIENCE.md`, `ROADMAP.md`,
  `docs/X_COMPANION.md`, `scripts/operator/network/README.md`, `README.md`,
  `DEVELOPMENT.md`, `AI_WORKSPACE.md`, `COVER_PIPELINE.md`, `DESKTOP.md`,
  `SERVER.md`, `SPEC.md`, `deploy/ubuntu/README.md`,
  `docs/BACKUP_AND_RECOVERY.md`, `docs/WORKER_EXECUTION_CONTRACT.md`,
  `AGENTS.md`, `docs/UBUNTU_NUC_DEPLOYMENT.md`); rename the live opt-in
  evidence gates (`FRAMENEST_RUN_BROWSER_EVIDENCE`,
  `FRAMENEST_RUN_REAL_MEDIA_TOOLS`, `FRAMENEST_RUN_NVIDIA_NIM_SMOKE`,
  `FRAMENEST_CHROME_BIN`) to `KRONIKA_*` with the frozen ADR-0015 mention kept
  as history; update the doc-content tests; produce the whole-tree C7-B
  closing classification with its residual list for CLOSE; re-pin the Part C
  `docs` and other movement with content-path departures; all suites; one
  commit. The Cooperator environment refresh (`poetry install`, stale
  `framenest-*` script removal, fourteen canonical consoles plus zero retired
  as evidence) runs alongside.

- **2026-10-15 — Cooperator environment refresh completed and verified: the
  installed environment is canonical-only.** `poetry install` (Poetry 2.3.2,
  in-project `.venv`, `virtualenvs.in-project = true`) reinstalled the root
  package with `INSTALL_EXIT=0`; poetry pruned the retired entry-point scripts
  and wrote the canonical ones. The Cooperator's displayed counts read zero
  because his interactive `ls` alias produces non-one-per-line output that
  defeats `grep -c '^…'`; the Orchestrator verified directly: `.venv/bin`
  carries **zero `framenest-*`** and **fourteen `kronika-*`** scripts, their
  shebangs resolve to `.venv/bin/python`, and `.ap exec` runtime-info is green
  (CPython 3.13.9, repository provenance). The plan's "installed wheel
  exposes exactly fourteen canonical consoles; old aliases are absent,
  including stale environment scripts" evidence holds.

- **2026-10-15 — `56_report_00.md` accepted after independent Orchestrator
  verification: C7-B/3 committed; C7-B complete in the repository.** Commit
  `7ebf4955e78731170477280c3b7f9f0cdd726e5a` (parent `551dd39…`, exactly 36
  files, +906/−883, one commit, no push). Verified: every active document is
  canonical (AGENTS.md, the runbook, README/PRODUCT/SERVER, DEVELOPMENT, the
  worker contract, SECURITY, ACCEPTANCE_DUAL_AUDIENCE, X_COMPANION, ROADMAP,
  BACKUP_AND_RECOVERY, OPERATOR_NETWORK, network/README, INFOSEC, SPEC,
  COVER_PIPELINE, AI_WORKSPACE, DESKTOP, GALLERY, the architecture evidence,
  the ADR index, `.gitignore`) with frozen Part A byte-unmoved; the five live
  evidence gates are `KRONIKA_*` with the frozen ADR-0015 mention kept as
  history; the whole-tree classification carries its residual list for CLOSE —
  frozen history, historical artifacts (markers, the dated release path,
  tooling and capture pointers), negative assertions, parked capture internals
  (C8 owns `/opt/framenest/capture-current`), the served shell's deliberate
  dual mutation-header emission, and no action-required finding. Independent
  runs: focused `68 passed`, JS `23/41/55/6/12/30` plus the bounded glob
  `212`, full suite `4968 passed, 8 skipped, 3 warnings, 0 failed` (680.21s;
  the skip reason now names the canonical gate). Ledger: `docs` 1184→749,
  `tests` 1445→1382, `scripts` 9→0, `deploy` 95→78, `src` unchanged, sixteen
  content-path departures. C7-B as a whole (B/1 + B/2a + B/2b + B/3) is
  complete in the repository. Residuals recorded for C9: the `framenest-nuc`
  tailnet node label (a live host name; Cooperator confirmation pending), the
  release engine's former-layout module constants, and the parked capture
  pointer. Next: push, check, deploy `7ebf495`, extension reload and the
  rendered regression acceptance that closes C7-B.

- **2026-10-16 — C7-B final deploy refused fail-closed at the backup gate
  (`CHECK_EXIT=11`); the push had already published.** `git push origin main`
  reported "Everything up-to-date" with `HEAD = origin/main = 7ebf495…` — the
  four C7-B commits are public. The NUC still runs `aee0a60`;
  `kronika-release check` returned `backup_restore_readiness: stale` and the
  deploy refused (`DEPLOY_EXIT=11`, "catalog backup is not restore-ready") —
  the engine's designed fail-closed gate. `stale` means the last
  `last_successful_scheduled_backup_and_restore` is older than 48 hours
  (`STALE_AFTER = timedelta(hours=48)` in `derive_restore_readiness`) while
  the latest attempt is not `failed`; the daily timer fires at 03:17 UTC
  (Persistent), so either the timer has not fired, the service failed before
  the operation recorded an attempt, or recent runs have not produced a fresh
  backup-and-restore success. Diagnostics requested on the NUC (timer and
  service state, journal since Oct 12, selected backup-status fields); the
  remedy is a successful `kronika-backup run-scheduled` (or the identified
  cause's fix), after which check and deploy resume. The extension reload and
  rendered acceptance remain pending the deploy.

- **2026-10-16 — Backup-gate diagnosis, decisive anomaly found.** The timer is
  enabled and active (next fire 2026-10-17 03:29 UTC); the service runs
  `kronika-backup run-scheduled` daily and **every observed run since Oct 12
  reports `succeeded`** (bundles `auto-20261012T032106Z` through
  `auto-20261016T032040Z`, retention pruning working, exit 0). Yet the
  operator status (read through the same
  `KRONIKA_ENV_FILE=/etc/kronika/kronika.env` service-account form) shows
  `last_scheduled_attempt` = `attempt_seq 124`, `completed_at_utc`
  `2026-10-12T18:56:25Z`, `state succeeded`, and `restore_readiness: stale` —
  i.e. the runs since the Oct 13 reboot appear to write their attempt records
  somewhere other than the ops root the status reads (or the service's
  effective environment diverges from the env file's canonical roots). The
  next probe reads the backup service's effective unit fragments/drop-ins and
  effective environment, the env file's backup keys, and the new versus old
  ops/backup roots with mtimes and recent entries.

- **2026-10-16 — Backup-gate root cause confirmed; bounded correction issued:
  `57_correction_00.md` (session 57, `KSI-CORR-C7BREAD`).** The host's
  canonical ops root is fresh — `status.json` written today 03:20:41 UTC by
  the daily service run, events tail `attempt_seq:130`,
  `scheduled_backup_and_restore_succeeded`, the canonical backups root holding
  `auto-20261016T032040Z…`; the release check instead read the **former** root
  `/var/lib/framenest/catalog-backup-ops/status.json` (attempt 124,
  `2026-10-12T18:56:25Z`). Mechanism: the engine's `cmd_remote_backup_status`
  and `cmd_remote_run_scheduled_backup` invoke `kronika-backup` through
  `service_account_prefix` with only `env KRONIKA_ENV_FILE=…`, and the backup
  console resolves its roots from the process environment only (no
  environment-file support, unlike `kronika-db`), so it fell back to its code
  defaults — the former `/var/lib/framenest/…` roots on the deployed `aee0a60`
  release. The pre-cutover checkpoint routes wrote the former root for the
  same reason (the former root's bundles at 2026-10-12 09:07, 17:50 and 18:56
  are those checkpoints). The readiness gate has therefore read the former
  root since the routine engine existed and only now — as it aged past the
  48-hour window — produced the fail-closed refusal. The correction binds both
  backup routes to the unit environment via the established oneshot
  `systemd-run --property=EnvironmentFile=` pattern (as
  `cmd_remote_production_cli` already does), leaves the database and
  production route contracts byte-identical, and adds the pins, the mutation
  demonstration and the residual finding (backup console versus database
  console configuration resolution). After acceptance: re-run check + deploy
  with the corrected engine (the deploy's own pre-cutover checkpoint then
  writes the canonical root), then the extension reload and the rendered
  acceptance.

- **2026-10-16 — `57_report_00.md` accepted after independent Orchestrator
  verification: the backup-environment correction is committed.** Commit
  `c0f456656c9930810e11d13e1d4684efdb3ee4ff` (parent `7ebf495…`, exactly
  three files, +73/−7, one commit, no push). Verified: the new
  `cmd_remote_backup_cli` runs the release's backup console through the
  established oneshot `systemd-run --quiet --pipe --wait --collect --uid=…
  --gid=… --working-directory=… --property=EnvironmentFile=…` binding for
  exactly `status` and `run-scheduled` (any other operation refuses with the
  usage exit); both routes are rewired; the database and production routes
  are byte-identical; three existing pins were tightened and thirteen cases
  added; the mutation demonstrations failed as designed when either route
  was reverted. Independent runs: focused `420 passed`, full suite `4981
  passed, 8 skipped, 3 warnings, 0 failed` (678.27s), JS sanity `119 passed`,
  Part A 86/36 and Part B empty with no Part C movement. Residual finding
  recorded for disposition: the backup console resolves its configuration
  from the process environment only while the database console honors
  `KRONIKA_ENV_FILE`; no console was changed. Next: the corrected C7-B final
  sequence — push `c0f4566`, status, check, deploy; the readiness read now
  binds the unit environment (canonical ops root, attempt 130 today) and the
  deploy's own pre-cutover checkpoint writes the canonical root; then the
  extension reload and the rendered regression acceptance.

- **2026-10-16 — C7-B final refresh complete: the NUC serves `c0f4566`.** The
  corrected engine's read showed `backup_restore_readiness: ready` — the
  unit-environment binding works against the fresh canonical ops root — and
  `check --release c0f4566…` passed (`public_main` matched,
  `superproject_sha256 9da42774…`, `CHECK_EXIT=0`). `deploy --release
  c0f4566… --yes` completed (`DEPLOY_EXIT=0`, remote lock acquired,
  `unit_executables: .venv/bin/kronika-production`); the final status reports
  active/web release `c0f4566…`, capture `94e605c…` unchanged, DB `0035`,
  service active, backup ready. The full C7-B state (canonical-only settings,
  consoles, scripts, readers and documents) is now served. Remaining for
  C7-B closure: the Cooperator's extension reload and rendered regression
  acceptance against the actual server/extension pair.

- **2026-10-16 — C7-B CLOSED: the Cooperator's rendered acceptance passed.**
  Against the actual pair (server `c0f4566`, the extension reloaded from the
  same checkout, stale panels closed and pages refreshed): the hosted shell
  loads, history/inbox loads, attach works, save works, hosted details open.
  With the publication, the served refresh, the ledger's empty Part B and the
  whole-tree classification, C7-B as a cut is complete and accepted — the last
  temporary compatibility layer of the identity transition is gone from the
  repository and from the running system. The whole proceeds to C8.

- **2026-10-16 — C8-A/P grant issued: `58_implementation_00.md` (session 58,
  exchange 01, `KSI-IMPL-C8AP`).** Scope: the explicit `migrate-capture-paths`
  command (read-only `preflight` with a plan digest; `apply` refusing without
  digest/`--yes`; structurally unreachable from routine web
  deploy/rollback/check/status), which prepares the freshly observed installed
  capture release under `/opt/kronika/releases` (same source identity and
  markers; virtual environment rebuilt from the release's committed lock with
  the frozen tooling), stages/switches the canonical pointer
  `/opt/kronika/capture-current`, installs the canonicalized capture units
  (only the two `/opt/framenest/capture-current` path lines become
  `/opt/kronika/capture-current`; unit names, account, state directory, token,
  profile, journal, ports and bridge protocol byte-unchanged), enforces the
  existing drain/work gate, brake gate and identity/readiness gates, and
  performs exactly one bounded bridge/runner stop-start cycle with Xvfb,
  view, VNC and the web service untouched. The six repo capture artifacts get
  the pointer path lines (the `capture_unit_contract_sha256` recomputes); the
  deployment runbook gains the bounded procedure and its restoration path;
  tests cover preservation, gates, bounded actions and the routine-path
  separation. Focused baseline `429 passed`; full `4981/8/3/0`; repository
  only, one commit, no push. C8-A/H (the Cooperator host execution) follows
  acceptance.

- **2026-10-16 — `58_report_00.md` accepted after independent Orchestrator
  verification: C8-A/P committed.** Commit
  `90766ca04358af876a7fb154c44fb005612d34ad` (parent `c0f4566…`, exactly
  seven files, +1406/−17, one commit, no push; the first report delivery was
  a byte-identical copy of the prompt and was set aside as
  `58_report_00.md.MISPLACED-PROMPT-COPY`, then replaced by the true terminal
  report). Verified: `migrate-capture-paths` is a separate two-phase command
  (`preflight` read-only with a plan digest; `apply` refusing without
  digest/`--yes`); routine `status`/`check`/`deploy`/`rollback` cannot reach
  it (stub test and transcript assertions); the apply copies the installed
  tree (`cp -a`, markers untouched), rebuilds the venv from its own lock
  through the frozen Poetry/CPython (no `uv`), enforces the work and brake
  gates twice, switches the pointer (staged `.next` + `mv -T`, former symlink
  removed, former tree kept), installs the five units with only the
  `WorkingDirectory=`/`ExecStart=` path lines changed, performs exactly one
  bridge/runner stop/start cycle with one `daemon-reload`, and keeps Xvfb,
  view, VNC and the web service untouched; three mutation demonstrations
  recorded; the five-line artifact diff is exact and
  `capture_unit_contract_sha256` recomputes to `11a1f07cc1d36294da481fcc2c64e13e44277449290db216c2c5b6cc86c3d902`.
  Independent runs: focused `462` (six-module set) and the report's
  nine-module `609`, full suite `4999 passed, 8 skipped, 3 warnings, 0
  failed` (682.72s), JS sanity `161`; Part C re-pins recorded (deploy files
  7→4, docs 749→751, tests 1382→1386, content paths −3, `/opt/framenest`
  152→146). Carried findings: `deploy/ubuntu/README.md`'s pointer-switch
  sentence is now incomplete (fix in C8-B/P); several success-path calls lack
  failing assertions (the poetry.toml/lock probes, `chown -R root`,
  `chmod -R a-w`, the shebang relocation upload, the post-install
  `WorkingDirectory` read-back). The commit stays local — the host execution
  runs from the PC checkout and needs no publication.

- **2026-10-16 — C8-A/H started: preflight issued.** The host execution of
  the prepared operation runs from the PC checkout at `90766ca` against the
  NUC: step 1 is the read-only `kronika-release migrate-capture-paths
  preflight`; the Orchestrator reviews the printed plan (former pointer
  alone, `release_sha 94e605c…`, marker spellings, `capture_code_tree`,
  bridge protocol `1`, installed versus canonical unit hashes,
  `plan_digest`), then the apply runs with the digest and `--yes`; evidence
  after: unchanged capture identity, canonical pointer and effective unit
  paths, frozen state/token/profile, one bridge/runner cycle, Xvfb/view/VNC
  and the web service untouched, readiness green, no second browser start on
  failure. The runbook section is the procedure; `deploy/ubuntu/README.md`
  is not.

- **2026-10-16 — C8-A/H preflight refused fail-closed: installed capture
  units drifted beyond the pointer path lines (`EXIT_SOURCE_GATE 3`,
  `kronika-capture-xvfb.service`).** The refusal is the designed gate: the
  installed host units predate the repository fixes `d63d0b7` (2026-09-25:
  Xvfb runs without `-nolock` and `/tmp` is added to `ReadWritePaths`) and
  `5260e2d` (2026-10-01: the `Documentation=` URL rename), so their exact
  text differs from the repository unit contract. Expected drift to confirm
  from the host: all five units carry the former `Documentation` URL; the
  xvfb unit additionally carries `-nolock` and the old `ReadWritePaths`; the
  runner unit may predate `fd277a9` (the TMPDIR/ExecStartPre fix). No
  mutation happened — the preflight is read-only. Next: dump the five
  installed units and any drop-ins, compile the exact diff, then reconcile
  the unit files to the repository text (pointer lines preserved at the
  current former pointer; one `daemon-reload`; no service restarts) as the
  bounded pre-step of the C8-A/H grant, re-run the preflight and proceed to
  apply.

- **2026-10-16 — Unit drift diagnosed exactly: one `Documentation=` line per
  unit.** The host dump shows the five installed capture units are otherwise
  identical to the repository units — the xvfb lock fix (`d63d0b7`) and the
  runner TMPDIR fix (`fd277a9`) are already present on the host, there are no
  unit drop-ins, and the pointer is the single former symlink to
  `/opt/framenest/releases/94e605c17b881461fad3e22fd8c7fca32cb93976`. The
  only difference in all five is the former URL
  `https://github.com/cisarik/framenest` versus the canonical
  `https://github.com/cisarik/kronika`. The bounded reconciliation (the
  C8-A/H pre-step, now authorized): one exact `sed` replacement per unit plus
  one `daemon-reload`, no service restarts; then the preflight re-runs and,
  on PASS, the apply follows with its digest.

- **2026-10-16 — Unit reconciliation applied; re-preflight PASS; apply
  authorized.** The five `sed` replacements succeeded (`exit=0` each), the
  grep shows the canonical `Documentation=` URL in all five units, the files
  are `-rw-r--r-- root root`, and `daemon-reload` returned 0 (no service
  restarts). The re-preflight passed with the plan:
  `source_pointer /opt/framenest/capture-current` alone; `release_sha
  94e605c17b881461fad3e22fd8c7fca32cb93976` (equal to the served
  `capture_release` identity); `marker_spellings
  .framenest-release-manifest.json,.framenest-release-sha` (historical,
  preserved); `capture_code_tree 977465503254fe6cdf31673b7e107b9e0487ffe2`
  (the capture tree's manifest value — a different scope from the web tree's
  `capture_runtime_identity` value `cb61ef7d…`, both correct);
  `capture_bridge_protocol 1`; `target_pointer
  /opt/kronika/capture-current`; `target_release
  /opt/kronika/releases/94e605c…`; the canonical executable path; the five
  unit names; `plan_digest
  b8c68cb5ce246e7b4a792f9ea31e98b0a7e73fe269b87a2cdaca04fffa2d61ad`.
  The Orchestrator reviewed and authorized the `apply` with that digest
  (`--yes`): drain/brake gates twice, release copy, pointer switch, five unit
  installs with only the pointer lines, one bridge/runner stop/start cycle,
  one readiness read; Xvfb, view, VNC and the web service untouched. The
  verification block after the apply covers the pointer states, effective
  unit paths, service states, Xvfb uptime, the copied tree's markers and the
  unchanged web service.

- **2026-10-16 — C8-A/H apply failed in the publish phase (transport EXIT 20);
  the engine cleaned up and left the live capture untouched.** Output:
  `capture-path migration left the installed pointer unchanged` plus
  `command failed`, `APPLY_EXIT=20`. Because `switched` is set only after a
  successful pointer switch, the failure happened at or before
  `_switch_canonical_capture_pointer` — i.e., in the publish sequence (copy,
  tree-manifest equality, the `poetry.toml`/`poetry.lock` existence probes,
  `.venv` removal, `poetry check --lock`/`env use`/`install`, shebang
  relocation, chown, writable-bit removal, staging rename), the second gates,
  the identity snapshot, or the stop step — and the cleanup removed the
  created trees. Host evidence: `/opt/kronika/releases/` holds no `94e605c…`
  (neither target nor `.staging`), the capture services are all active, the
  Xvfb `ActiveEnterTimestamp` is unchanged (2026-10-15 06:31:47), the pointer
  is still the former one, and the web status is unchanged (`capture_release
  94e605c…`, active `c0f4566`). The engine deliberately swallows remote
  stderr ("command failed"), so the diagnosis proceeds by exact host probes
  (source-tree `poetry.toml`/`poetry.lock` presence, leftovers, space) and a
  faithful `/tmp` reproduction of the publish commands with the frozen
  tooling.

- **2026-10-16 — Apply failure narrowed: the stop/switch never ran; the
  publish path is reproduction-proven green.** Host state: `/opt/kronika/`
  contains only the web `current` pointer (no `capture-current`, no `.next`),
  the former capture pointer is intact, and the bridge/runner
  `ActiveEnterTimestamp`s are 2026-10-14 19:33:24 and 2026-10-15 06:31:47
  with `NRestarts=0` — the services were never stopped, so the failure
  happened in the publish tail, the gates or the snapshot. The faithful
  `/tmp` reproduction of copy → `.venv` removal → `poetry check --lock` →
  `env use` → `install --only main` → executable presence passed every step
  (`CHECK/ENVUSE/INSTALL/EXEC=0`; the venv builds as `framenest` in-project
  and carries `kronika-capture`), and the source tree has `poetry.toml`
  (`in-project = true`) and `poetry.lock`, so the venv-rebuild hypothesis is
  disproven. Remaining unknowns: the scratch write, the shebang relocation,
  the executable probes, chown/chmod, the staging rename, the gates and the
  identity snapshot — or a transient transport failure. Next: rerun the
  apply with a logging `ssh` shim on the PC PATH (argv and stderr of any
  failing remote command captured to `/tmp/sshlog/ssh.log`), same preflight
  digest `b8c68cb5ce246e7b4a792f9ea31e98b0a7e73fe269b87a2cdaca04fffa2d61ad`.

- **2026-10-16 — Apply failure root-caused exactly: web-only required
  console scripts in the shared relocation helper.** The logging `ssh` shim
  caught the failing call: `_remote-relocate-venv-shebangs` on the rebuilt
  capture venv exits 14 with `required console script is missing`, because
  `relocate_venv_shebangs` hardcodes the web pair `("kronika-db",
  "kronika-backup")` while the capture venv carries the capture script
  (`kronika-capture`). Everything before that step succeeded on the host
  (copy, marker checks, `poetry check --lock`, `env use`,
  `install --only main`, lock-hash stability, scratch write) and the failed
  run cleaned up completely; the live capture was never touched (bridge and
  runner `NRestarts=0`, former pointer intact). The same log confirmed the
  C7 corrections live: the post-failure `status` read went through the
  `systemd-run --property=EnvironmentFile` database and backup routes. The
  failure is deterministic — a scoping-class defect of the session-58 code
  (a shared helper reused for a different release kind without
  parameterizing its web requirement), not a transient.
  `59_correction_00.md` (session 59, exchange 01, `KSI-CORR-C8RELOC`)
  parameterizes the required scripts with the web default preserved
  byte-identical, adds the repeatable remote flag, derives the capture
  caller's script from the plan executable, audits sibling helpers for the
  same class, and requires the three named mutation demonstrations. After
  acceptance: rerun the apply with the same digest, then the host
  verification block closes C8-A/H.

- **2026-10-17 — `59_report_00.md` accepted after independent Orchestrator
  verification: the relocation correction is committed.** Commit
  `7c1ea48be1176cd454f0ce6a97dc09d32d543838` (parent `90766ca…`, exactly five
  files, +323/−10, one commit, no push). Verified: the required-script set is
  an explicit validated input (`relocate_venv_shebangs` defaults to the web
  pair and an explicit sequence replaces it; unsafe names, empty sequences
  and a string passed as a sequence are refused; the validation runs before
  any rewrite); the remote builder emits the baseline command
  byte-identically when the sequence is omitted and appends one validated
  flag per requested name otherwise; both web callers — the
  identity-migration preparer and `_cmd_deploy` — stay flag-free; the capture
  publish passes exactly one script derived from
  `PurePosixPath(plan.executable).name`; the same-class audit found no further
  web-only requirement on the capture path. Independent runs: focused
  `473 passed` (five modules; the report's nine-module run was `623`), full
  suite `5013 passed, 8 skipped, 3 warnings, 0 failed` (685.31s), JS sanity
  `161`; Part A 86/36 and Part B empty with no Part C movement. Next: rerun
  the capture-path apply with the unchanged digest `b8c68cb5…` (the host
  state is untouched) and the host verification block; the logging `ssh`
  shim stays available for the trace.

- **2026-10-17 — C8-A/H executed successfully: the capture release moved to
  the canonical pointer without a software change.** The corrected apply
  (`7c1ea48`) ran against the unchanged digest
  `b8c68cb5ce246e7b4a792f9ea31e98b0a7e73fe269b87a2cdaca04fffa2d61ad`. Host
  evidence: the bridge and runner unit-effective texts name
  `/opt/kronika/capture-current/.venv/bin/kronika-capture` and
  `/opt/kronika/capture-current` while keeping the same unit names, account,
  state directory, token, profile, journal, ports and bridge protocol; all
  four services (bridge, runner, Xvfb, web) are active; the bridge/runner
  `ActiveEnterTimestamp`s are 2026-10-17 07:28:18 and 07:28:19 (exactly one
  bounded cycle) while Xvfb keeps 2026-10-15 06:31:47 (never restarted); the
  copied tree `/opt/kronika/releases/94e605c…` exists as the canonical
  release with the preserved historical `.framenest-release-sha` marker =
  `94e605c…` (same source identity); the failed-run scratch is removed.
  Remaining formality for the trace: the PC `status` and the pointer
  readlink outputs; then C8-A/H closes and C8-B/P opens.

- **2026-10-17 — C8-A/H CLOSED: the capture release runs from the canonical
  pointer with identical software.** Final confirmation: `readlink
  /opt/kronika/capture-current` → `/opt/kronika/releases/94e605c…`; the
  former pointer is removed (`readlink` prints nothing); `ls -la /opt/kronika`
  shows `capture-current -> …/94e605c…`; the PC `status` reports
  `capture_release 94e605c…` **unchanged**, web `c0f4566`, service active,
  DB `0035`, backup ready. With the earlier host evidence (canonical unit
  paths, the single bridge/runner cycle at 07:28:18/19, Xvfb untouched since
  2026-10-15 06:31:47, the copied tree with the preserved historical marker)
  the cut satisfies the plan's proof list: identical capture source identity,
  valid release markers, canonical effective paths, frozen state name,
  unchanged protocol, one expected browser transition, unchanged web
  release/health. The former release tree remains for C9.
  `60_implementation_00.md` (session 60, exchange 01, `KSI-IMPL-C8BP`) opens
  C8-B/P: the remaining HTTP `Server` and health `api` labels to the
  canonical capture identity (the frozen state token preserved only at the
  state-directory sites), the explicit capture transition extended to restart
  the bridge as well as the runner (safe order, existing gates, no second
  launch), the stale `deploy/ubuntu/README.md` pointer sentence, the
  complete-delta review of the installed 94e605c software against the target
  (the four known files — `driver.mjs` +124, `runner.mjs` +41, `cli.py` +20,
  `config.py` 2 — behavior changes beyond branding), and the named C8-A/P
  test-quality additions. After acceptance: publication of the exact target,
  then C8-B/H.

- **2026-10-17 — C8-B/P ACCEPTED independently; the C8-B/H grant is issued.**
  Commit `5b86d896b3ea03f89fef2c90f7af2c121d0ef915` verified by the
  Orchestrator: `src/kronika_capture` tree `1b193a8b…` =
  `5b86d89:src/kronika_capture`; the installed-to-target delta is exactly five
  files (`driver.mjs`, `runner.mjs`, `bridge/server.py`, `cli.py`,
  `config.py`, `+160/−31`, `git diff --name-status 94e605c 5b86d89`); the HTTP
  `Server` label and health `api` label are canonical via `config.APP_NAME`
  (`kronika-capture/0.1.0`; health `{"ok": true, "api": "kronika-capture",
  "api_version": 1}`); `STATE_DIR_NAME` and the protocol constants unchanged;
  `activate-capture`/`rollback-capture` restart the bridge and then the runner
  with wrapped readiness-class failures and one readiness check; the README
  pointer sentence is canonical; retention moves only Part C (src 183 files /
  1604 occurrences, deploy 3 / 72, `/opt/framenest` 145, content paths −2) with
  cause. Independent runs: full Python `5016 passed, 8 skipped, 3 warnings, 0
  failed` in 686.39 s; JS exactly `23/41/55/12/30/6` plus bounded glob `212`.
  The gate pre-check for C8-B/H is resolved: the deployed `94e605c` release was
  built by the 2026-09-25 engine, which already emitted
  `capture_bridge_protocol: "1"` in its manifest, equal to the target constant,
  so the activation's protocol gate passes; the target release must pre-exist,
  so the grant publishes `5b86d89`, runs the routine deploy (which prepares the
  shared release tree, web moves to 5b86d89 and `capture_release` must stay
  `94e605c`), then runs `activate-capture --release 5b86d89… --yes`, then
  collects NUC evidence (token-exempt `/v1/health` curl, pointer readlink,
  marker cat, bridge/runner/xvfb unit timestamps) and releases the sudo
  timestamp with `sudo -K`. Same-schema only (DB `0035` = packaged head);
  brake satisfied since the 07:28 cycle; rollback remains the explicit
  compatible capture rollback under a fresh grant and brake; a rollback
  restoring retired operational branding leaves the whole open (plan §2.17).
  After C8-B/H closes: C9-A (which additionally needs the scheduled-backup
  receipt, fresh exact manifests and no unresolved recovery state), C9-B,
  C-INSTALL-DOC, CLOSE.

- **2026-10-17 — C8-B/H executed: the canonical capture software is live from
  the published target; final `status` read pending.**
  Orchestrator-verified locally: `origin/main` = `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`
  (the three local commits `90766ca`, `7c1ea48`, `5b86d89` are public).
  NUC evidence: `curl -sS -D - http://127.0.0.1:8765/v1/health` returned
  `Server: kronika-capture/0.1.0` and `{"ok": true, "api": "kronika-capture",
  "api_version": 1}` (canonical bridge headers and health identity, protocol
  values unchanged); `readlink /opt/kronika/capture-current` →
  `/opt/kronika/releases/5b86d896b3ea03f89fef2c90f7af2c121d0ef915`;
  `ActiveEnterTimestamp` bridge `2026-10-17 09:47:07 UTC`, runner
  `2026-10-17 09:47:08 UTC` (one bounded cycle, bridge before runner — the new
  restart extension executing live), Xvfb unchanged `2026-10-15 06:31:47 UTC`.
  The shared release tree necessarily pre-existed (the activation's
  `cmd_remote_test_exists` + marker gates passed), so the routine deploy of
  `5b86d89` ran and prepared it. `cat
  /opt/kronika/capture-current/.kronika-release-sha` as the admin user is
  `Permission denied` — expected: release trees are service-owned and the
  engine reads markers through `sudo -n` readers; `readlink` plus `status` are
  the accepted provenance reads. The migrate `preflight`/`apply` EXIT 20
  section that appeared in the pasted scrollback is the recorded 2026-10-16
  failed attempt (publish-phase failure in the web-only
  `relocate_venv_shebangs` required-script pair; the engine cleaned up and left
  the former pointer and services untouched), fixed by `7c1ea48` before the
  successful 2026-10-17 07:28 apply — history, not a new event. Pending: one
  final `status` (expected `capture_release` = `web_release` = `5b86d89`,
  active, DB `0035`, backup ready), then C8-B/H closes and C9-A opens.

- **2026-10-17 — C8-B/H CLOSED: the reviewed capture software is active and
  the capture transition is complete.** Final `status`: `active_release` =
  `web_release` = `capture_release` =
  `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`, `release_path`
  `/opt/kronika/releases/5b86d896…`, `service_active: active`, DB `0035`,
  `backup_restore_readiness: ready`. With the prior evidence (publish =
  `origin/main`; canonical `Server`/health labels live; pointer readlink; one
  bridge→runner cycle at 09:47:07/08 UTC; Xvfb untouched) every §2.17 proof
  item is satisfied: installed release/source provenance, canonical bridge
  headers and health identity, unchanged protocol/state, bounded browser
  transition, no automatic resend, and a web release the capture activation
  left at the deploy's target. The C9-A precondition set now needs only the
  scheduled-backup receipt and fresh exact manifests (C8-A/B accepted; no
  unresolved recovery state). Next: read-only C9-A reconnaissance — canonical
  kronika-catalog timers with `kronika-backup status`, then the former-layout
  inventory (`/opt/framenest`, `/etc`, systemd units/drop-ins, state/cache
  roots, `/usr/local/bin`) to build the exact candidate list and the private
  preservation manifest for individual approval.

- **2026-10-17 — C9-A reconnaissance, first set: the scheduled-backup receipt
  exists and the candidate inventory is captured.**
  Receipt: `kronika-catalog-backup.timer` last fired Sat `2026-10-17
  03:25:40 UTC` (next `2026-10-18 03:22:16 UTC`), `ExecMainStatus=0`, exit
  `03:25:41`; `kronika-backup status` reports `last_scheduled_attempt`
  `attempt_seq 133` `run-scheduled` succeeded `2026-10-17T09:46:18Z` — the
  routine deploy's "Fresh verified checkpoint before cutover" runs exactly
  this operation on the target (engine line 6343) — with
  `last_successful_scheduled_backup`, `..._and_restore` and
  `..._restore_verification` all at seq 133, `alembic_revision 0035`,
  `catalog_sha256 09664c…`, `restore_readiness: ready`, `recent_failure:
  null`, retention `30/30` automatic with `28` pinned, `planned_expire 0`.
  The off-device timer is absent/unconfigured (`configured: false`, service
  never ran) — separate ADR-0056 capability, untouched by this whole.
  Inventory: `/opt/framenest` = former `current → releases/a37be37…` (still
  present), `releases/` with ~88 historical trees (Jul 11 – Oct 10),
  `tooling/` (frozen). `/opt/kronika` = `current` and `capture-current` both
  → `releases/5b86d896…`; canonical `releases/` holds 7 trees (`a37be37`,
  `c152a17`, `aee0a60`, `7c1cee29`, `c0f4566`, `94e605c`, `5b86d896`).
  `/etc/framenest` = `credentials/` (root 0700) + `framenest.env` + four
  timestamped backups; `/etc/kronika` = `credentials/` + `kronika.env`.
  Former units all present as files but disabled and unlinked:
  `framenest.service`, `framenest.service.d/framenest-research-credential.conf`,
  `framenest-catalog-backup.service`, `framenest-catalog-backup.timer`; the
  live `kronika.service.d/` carries only the misnamed
  `framenest-research-credential.conf` drop-in. `/usr/local/bin`: `node` →
  frozen tooling (correct), **`yt-dlp` → `/opt/framenest/current/.venv/bin/yt-dlp`
  — a live-used former-path pointer** (the X downloader runs a `yt-dlp`
  subprocess resolved from PATH; the Python `yt_dlp` package is imported from
  the running canonical venv). `/var/lib`: `framenest/` (two orphaned
  `*.tmp` preflight SQLite copies from 2026-07-22 plus
  `chatgpt-page/{chromium-profile, chromium-profile-flagged-20260923}` —
  operator-sensitive profile copies), `kronika/` (canonical data),
  `kronika-capture/` (live capture home, mtime today), `kronika-identity-migration/`
  (root 0700). `/var/cache`: `framenest/` and `kronika/` (both Aug 2). Next:
  second read-only probe set (drop-in content, credentials reconciliation,
  former-path counts in the live env, `grep -rl framenest /etc`,
  `systemctl cat` of the three services, cache roots, identity-migration
  store, `/usr/local/bin` symlinks, off-device mount state, `du` sizes),
  then the exact C9-A proposal with the private preservation manifest.

- **2026-10-17 — C9-A reconnaissance, second set: classification and new
  live-object findings.** `/etc/framenest/credentials` versus
  `/etc/kronika/credentials`: the recursive diff prints nothing — identical
  content, so the former is a redundant copy. The host drop-in
  `/etc/systemd/system/kronika.service.d/framenest-research-credential.conf`
  carries the canonical LoadCredential path
  (`KRONIKA_RESEARCH_OPENAI_API_KEY:/etc/kronika/credentials/research-openai`)
  and differs from `deploy/systemd/kronika-research-credential.conf` only in
  one comment spelling (`FRAMENEST_AI_CONFIG_PATH` vs
  `KRONIKA_AI_CONFIG_PATH`) — a rename/replace candidate. The `/etc` content
  sweep found further live objects with retired spellings:
  `/etc/sudoers.d/framenest-catalog-export`,
  `/etc/ssh/sshd_config.d/00-framenest-hardening.conf`,
  `/etc/apparmor.d/framenest-chrome`, and
  `/etc/systemd/system/kronika.service.d/30-publication-write-path.conf`
  (host-only; no repository counterpart), plus OS-history files
  (`/etc/passwd-`, `/etc/group-`, `/etc/shadow-`, `/etc/hostname`,
  `/etc/hosts`, SSH host-key comments). `/etc/fstab` carries the frozen
  `/mnt/framenest-catalog-offdevice` line while the mount itself is absent —
  consistent with `off_device configured: false`. `/var/cache/framenest` and
  `/var/cache/kronika` hold the same `cover-thumbnails/` and
  `gallery-previews/` entry sets (diff pending). `/var/lib/kronika` holds the
  live catalog, the backup roots, `covers/` (protected accepted covers),
  `deployment-evidence/` (root-only), a root-only one-time backup directory,
  feature staging dirs, nine obsolete July scratch `*.tmp` SQLite copies, and
  `chatgpt-page/` (an old chromium profile copy);
  `/var/lib/framenest/chatgpt-page/` holds two more old profile copies; both
  are operator-sensitive. `/var/lib/kronika-identity-migration/` holds the
  closed migration's journals and `recovery-manifest.json`. `/usr/local/bin`
  has exactly two symlinks: `node` → frozen tooling (kept) and `yt-dlp` →
  `/opt/framenest/current/.venv/bin/yt-dlp` (repoint to
  `/opt/kronika/current/.venv/bin/yt-dlp` before retirement). Sizes: former
  releases 6.5G, frozen tooling 969M, canonical releases 563M, former state
  113M. `systemctl cat` needs sudo (the unit file is not world-readable).
  Third probe set gathers the live-object contents (sudoers, sshd, AppArmor,
  publication-write-path, `systemctl cat`, masked env lines, fstab line,
  cache diff, `libexec` listing, clean release lists, profile sizes).

- **2026-10-17 — C9-A reconnaissance, third set: live objects classified; the
  host-name residue is resolved as retained.** Key findings: the three
  `site-sudoers` files are `framenest-catalog-export` (92 B, rule
  `michal ALL=(framenest) NOPASSWD:NOSETENV:
  /usr/local/libexec/framenest-catalog-export-v1 ""` — run-as user no longer
  exists and the canonical launcher `/usr/local/libexec/kronika-catalog-export-v1`
  is already installed, so the old rule and launcher are a latent broken
  pair), `framenest-worker-chdir` (25 B) and `framenest-worker-timestamp`
  (61 B) — both unreferenced by any repository script; the live
  `kronika.service` drop-ins are `20-ai-credential.conf` (canonical
  credential path), `30-publication-write-path.conf`
  (`ReadWritePaths=/srv/media/framenest-published` — the C6-deferred custom
  publication path, preserved deliberately then and reconciled here),
  `40-runtime-directory-mode.conf` and the misnamed research drop-in. The
  sshd drop-in contains only hardening directives plus one comment spelling;
  the AppArmor profile `framenest-chrome` is `flags=(unconfined)` for
  `/opt/framenest/tooling/chrome-for-testing/**/chrome` and is loaded. The
  live env's five former tokens are two header comments, two commented-out
  legacy keys and `KRONIKA_EXTERNAL_ORIGIN=https://framenest-nuc.tail247768.ts.net`
  (the retained live host name, not a rename target). `capture.env` carries
  one former token pending a masked line check. `/var/cache/framenest` is
  recursive-identical to `/var/cache/kronika` (diff silent) and the canonical
  venv already carries `yt-dlp`. The former release root lists 89 trees;
  canonical 7. `/var/lib/framenest` turns out to be a complete former state
  root (catalog copy, backup roots, covers, deployment-evidence, profiles,
  staging, plus hidden scratch files; the earlier `find | head -60` had
  truncated it) — the pre-migration original kept since the C4/C7 state move;
  bind-mount status and inode separation are checked before any retirement.
  `/var/lib/kronika/chatgpt-page` is 74M, `/var/kronika/catalog-backups` 33M,
  `/var/cache/framenest` 244K. The host-name residue is resolved from the
  Cooperator's own 2026-10-02 request: the live `framenest-nuc` host and
  tailnet names stay, and the from-scratch reinstall with canonical naming is
  documented by C-INSTALL-DOC; no rename happens in C9-A.

- **2026-10-17 — C9-A reconnaissance, fourth set: the last facts are in, the
  proposal is ready.** `capture.env` line 22 is a commented
  `# KRONIKA_CAPTURE_RELEASE=/opt/framenest/capture-current` (the canonical
  repository template already carries the `/opt/kronika/capture-current`
  form). The two worker sudoers files are **live sudo policy**, not orphans:
  `framenest-worker-chdir` is `Defaults:michal runcwd=*` and
  `framenest-worker-timestamp` is
  `Defaults:michal timestamp_type=global,timestamp_timeout=1440` — the global
  timestamp is the mechanism that lets the Cooperator's `sudo -v` cover the
  helper's later SSH `sudo -n` calls, so the content is retained and only the
  file names are canonicalized. `/var/lib/framenest` is a complete former
  state root (catalog copy, all backup roots, covers, deployment-evidence,
  profiles, staging, `chatgpt-page`, plus the same nine hidden July scratch
  files seen in the live root); `findmnt` shows both roots on the root
  filesystem with no bind mounts, and `stat` shows distinct directory inodes
  (`2066:9702528` vs `2066:9830441`) — even a hardlinked file would keep its
  live link when the copy's link is removed, so retirement is safe.
  `/srv/media/framenest-published` **exists** (kronika-owned, Oct 13); the
  earlier `test -d` "absent" was an EACCES artifact because `/srv/media` is
  `root:kronika 2750` and the operator user cannot traverse it. The other
  `/srv/media` entries are canonical (`memes`, `movies`, `youtube`).
  `/etc/fstab` carries only the cosmetic comment `# FrameNest media SSD` and
  no former path. Repository checks: no `worker-chdir`/`worker-timestamp`
  reference anywhere; no AppArmor source in the repository; no
  `framenest-published` literal in the repository; the worker gate script
  reads no sudoers names. The full C9-A proposal is issued with the
  preservation step (root-only archives into
  `/root/kronika-retired-20261017/`), Part A live-object canonicalization
  (yt-dlp repoint, export chain fix with the canonical sudoers rule, worker
  sudoers renames, research drop-in replacement, publication-path rename,
  sshd drop-in rename, AppArmor profile rename, env comment canonicalization),
  Part B retirements (dead units/drop-in directory, former pointer, 88 former
  release trees, five unreferenced canonical releases with `5b86d896` and
  `c0f4566` retained, `/etc/framenest`, `/var/cache/framenest`, the nine live
  scratch files, the `/var/lib/framenest` state copy, and — on the
  Cooperator's choice — the old profile copies and the closed migration
  store), and post-checks; no service is restarted, and the fstab comment plus
  the OS-history files are retained and documented. Pending the Cooperator's
  single approval, then stage 0+A execution, then stage B.

- **2026-10-17 — C9-A APPROVED ("schválené"), V1a/V2a selected; stage 0+A
  issued.** The Cooperator approved the full proposal with the recommended
  choices: the old profile copies and the closed migration store are
  archive-then-delete. Stage 0 creates the root-only preservation archives in
  `/root/kronika-retired-20261017/` (0700): `/etc/framenest`,
  `kronika-identity-migration`, the retired config files, the pre-edit env
  snapshots, pointer/listing records, and `SHA256SUMS`. Stage A canonicalizes
  the live objects: `yt-dlp` repoint, export chain replacement (canonical
  sudoers rule with run-as `kronika`, old launcher and rule removed, worker
  sudoers renamed with unchanged content, `visudo -c` both times), research
  drop-in replacement plus publication path rename (`/srv/media/kronika-published`)
  and `daemon-reload`, sshd drop-in rename with `sshd -t` (no reload), AppArmor
  profile rename (`unconfined`, unload/edit/rename/load), and comment-only env
  canonicalization. No service is restarted. Stage B follows after the stage
  A outputs are verified.

- **2026-10-17 — C9-A stage 0+A executed green; stage B issued.** Preservation
  archives live under `/root/kronika-retired-20261017/` (0700) with
  `SHA256SUMS` (`capture-env 2e961a60…`, `etc-framenest e4bd947a…`,
  `identity-migration fd62cf1e…`, `kronika-env d9ebd386…`, `retired-config
  32b46812…`) plus pointer/listing records and the 88-tree list (3608 B).
  Stage A verified: `yt-dlp` → `/opt/kronika/current/.venv/bin/yt-dlp`
  (version `2026.07.04`, the pinned version); canonical export rule installed
  (88 B, run-as `kronika`, `visudo -c` parsed OK both times) with the old
  rule and old launcher removed; worker sudoers renamed with unchanged bytes
  (25/61 B); research drop-in replaced by the canonical fragment;
  publication path renamed to `/srv/media/kronika-published` with the drop-in
  line updated; sshd drop-in renamed (`sshd -t` OK, no reload); AppArmor
  profile renamed to `kronika-chrome` (unload/edit/rename/load, only the new
  name listed); env comments canonical — `kronika.env` keeps only the
  retained `KRONIKA_EXTERNAL_ORIGIN` line 26 and `capture.env` is clean.
  Post-checks: three services active, `systemctl --failed` empty, bridge
  health `Server: kronika-capture/0.1.0`, and the `/etc` sweep leaves only
  planned stage-B targets plus the retained baseline (fstab comment,
  hostname/hosts, `passwd-`/`group-`/`gshadow-`/`shadow-`, SSH host-key
  comments, the origin line). Two expected artifacts: `head` without sudo is
  denied (0640 root:kronika; re-checked with sudo in stage B) and
  `kronika-chrome` matches the sweep only through the frozen
  `/opt/framenest/tooling` path inside the profile. Stage B: two large
  archives (state copy, old profiles) with a disk check, then the enumerated
  retirements — dead units and drop-in directory, former pointer, the 88
  trees deleted from the recorded list with 40-hex, existence and exact-count
  gates, five unreferenced canonical releases with `5b86d896` and `c0f4566`
  retained, `/etc/framenest`, `/var/cache/framenest`, the nine scratch files,
  `/var/lib/framenest`, the closed migration store and the old profiles —
  then the fresh `run-scheduled` receipt and the final status.

- **2026-10-17 — C9-A stage B executed; two bounded corrections issued.**
  All retirements executed green: dead units gone (`no-framenest-units`),
  former pointer removed (`/opt/framenest` = tooling only), the 88 trees
  deleted with `checked 88 trees, ok=1 … remaining: 0`, five canonical
  releases removed with `5b86d896` and `c0f4566` retained and both pointers
  unchanged, `/etc/framenest` and `/var/cache/framenest` gone, the
  `/var/lib/framenest` state copy, the closed migration store and the old
  profile roots removed, the fresh backup receipt succeeded (`attempt_seq
  134`, bundle `auto-20261017T104725Z-9e58119a`, `ExecMainStatus=0`,
  `recent_failure: null`), services active and the `/etc` content sweep is
  the retained baseline only. TWO CORRECTIONS: (1) B7's nine scratch files
  survived because the `[ -f ]` guard ran unprivileged inside the 0700 root
  and reported MISSING for every file; re-run under `sudo bash -c`.
  (2) `/srv/media/framenest-published` is a live **upload-publication
  destination library**: ~45 UUID media files (1.8 GB, written up to
  2026-10-13), resolved by the app from the catalog's library record
  (`upload_publication_library_id` → `FilesystemPublishedMediaStorage(root=destination.root.path)`),
  so the A5 rename broke the destination contract; A5 is reverted (directory
  and drop-in line restored; the running unit's mount-namespace bind and the
  app's resolved path string both converge on the restored name, so no
  restart is needed) and the canonicalization stays a documented deferred
  media-path migration (the C6 disposition — it needs the app/database side,
  not a filesystem rename). A name-based sweep (`find -iname`) surfaced
  `/etc/fstab.before-framenest-media.20260708-135419` (a pre-media-change
  fstab backup; name match only): archived into the retired directory and
  removed. Lesson recorded: content greps miss name matches; the closure
  sweep must be name-based. C9-A closes after the corrections verify.

- **2026-10-17 — C9-A corrections verified; the name sweep exposed the last
  residues.** F-1: `/srv/media/framenest-published` restored and the drop-in
  line back; the catalog carries the destination path twice (the library root
  and a second copy) and the env sets `KRONIKA_UPLOAD_QUARANTINE_ROOT` +
  `KRONIKA_UPLOAD_PUBLICATION_LIBRARY_ID` + `KRONIKA_YOUTUBE_ACQUISITION_ROOT`;
  `runtime-settings.json` is absent. F-2: all nine scratch files removed
  (`no-scratch-left`). F-3: the fstab backup archived (`7ebe10ec…`) and
  removed; `restore_readiness: ready`; the retired directory is 91M. Name
  sweep verdict — retain and document:
  `/srv/media/framenest-published` (deferred media-path migration),
  `/var/lib/tailscale/certs/framenest-nuc.tail247768.ts.net.{crt,key}` (live
  TLS material for the retained tailnet name; secrets; untouched),
  `/var/lib/kronika/deployment-evidence/deploy-20260724T142300Z-c76599aa/framenest-previews-help.txt`
  (historical evidence snapshot; untouched), `/opt/framenest` and
  `/opt/framenest/tooling` (frozen). Clean up now:
  `/var/backups/framenest` (2026-08-01 env backup; archive then remove),
  `/var/cache/apparmor/2693c843.0/framenest-chrome` (stale compiled profile
  cache), `/var/lib/systemd/timers/stamp-framenest-catalog-backup.timer`
  (orphan timer stamp). Inspect before deciding: `/var/tmp/framenest-mibench`.
  The PC `status` output was missing from the paste and is re-requested.

- **2026-10-17 — C9-A R2: the last cleanups executed; mibench is operator
  material.** `/var/backups/framenest` archived (`eac52fce…`) and removed; the
  stale AppArmor cache entry and the orphan timer stamp removed; the final
  `find -iname '*framenest*'` sweeps for `/etc` and `/var/lib/kronika`
  return empty. `/var/tmp/framenest-mibench` (owner `michal`, 2026-08-03) is
  the Cooperator's own movie-ID quality benchmark material (`reps/` reports,
  `tools/movie_id_quality_benchmark`, `work/snapshot_partial.json`) — an
  unexpected operator-owned object under the preservation clause: retained in
  place and documented, never deleted by this cut; `/var/tmp` ages it out
  through systemd-tmpfiles. Final verification block issued: web
  `check-health`, the definitive name sweeps (expected retained set:
  `framenest-published`, the deployment-evidence help file, the two tailscale
  cert files, `/opt/framenest`, `/opt/framenest/tooling`), service states,
  then the PC status and the timestamp release. C9-A closes on that output.

- **2026-10-17 — C9-A R3: the health alarm was the orchestrator's command
  error; a real `sed -i` mode regression is fixed.** `check-health` failed
  only because the direct invocation bypassed the systemd contract:
  `kronika-production` ignores `KRONIKA_ENV_FILE` and reads process
  environment only, so the check ran with default loopback TCP settings
  instead of the live tailscale UDS and got connection refused. The deploy's
  own verification at 09:46 used the correct `systemd-run
  --property=EnvironmentFile` wrapper and passed; the application `/health`
  endpoint returns `{"status":"ok"}` unconditionally, so no application fault
  exists. The real finding: `sed -i` rewrites files with default ownership and
  mode, so `/etc/kronika/kronika.env` (secrets) and the sshd drop-in likely
  lost their `0640 root:kronika` / `0600` modes (and the publication drop-in
  and AppArmor profile may have lost theirs). R4 restores the exact modes
  (evidenced against the pre-edit archives), re-runs `check-health` through
  the correct `systemd-run` wrapper, and the final sweeps confirmed the
  retained name set (`framenest-published`, the deployment-evidence help
  file, the two tailscale cert files, `/opt/framenest`, plus the
  operator-owned `/var/tmp/framenest-mibench`) with `/etc` and
  `/var/lib/kronika` name-clean.

- **2026-10-17 — C9-A CLOSED; the Cooperator chose host-identity option A;
  C9-B planning opened.** Final micro-step issued: the research drop-in
  returns to its original `0600` (all other modes already verified against the
  pre-edit archives). Decision A recorded: the live `framenest-nuc` hostname,
  tailnet name, Serve targets, certs, `KRONIKA_EXTERNAL_ORIGIN` and the
  operator's SSH identity filename are **retained and documented** — no live
  rename and no reinstall dependency; `C-INSTALL-DOC` is reframed as a
  clean-install / recovery runbook for a fresh or replacement host (still
  documenting the canonical host/tailnet naming). With that, C9-A is fully
  closed: every plan §2.18 proof item is evidenced, the retained set is
  explicit, and the host-state record lives in this ledger and in
  `/root/kronika-retired-20261017/`. C9-B opens with a fresh Planning Worker
  session (61, `KSI-PLAN-C9B`): derive the exact removal inventory
  (former-layout web support, temporary migration/recovery implementations,
  transitional client options) against the durable-reader, Alembic-shim and
  local-state-safeguard keeps; the stale-claim inventory across the living
  documents; the semantic-classification method for remaining operational
  hits; the proof design (both suites, wheel/resource checks, frozen hashes,
  canonical executable set, public-main equality, no routine deployment route
  able to select deleted layouts); and the sub-grant split with the
  publish/refresh/rendered-acceptance boundary.

- **2026-10-17 — C9-B planning report accepted after an independent
  Orchestrator spot-check; C9-B/1 issued.** The report (session 61,
  `KSI-PLAN-C9B`, PASS, `new-evidence`) was verified at the definitions:
  `OLD_WEB_LAYOUT` 210 / `NEW_WEB_LAYOUT` 226 / `WEB_LAYOUTS` 240,
  `accepted_release_roots` 1354, `parse_web_layout_probe` 1937,
  `select_web_layout` 2003, `resolve_capture_pointer` 2046,
  `resolve_host_layout` 2077; `MIGRATION_PHASES` 301,
  `COMPATIBLE_ENVIRONMENT_PREFIX` 44, `run_migration_apply` 4740,
  `observe_capture_path_plan` 5401, the migrate CLI at 5866/5889/5971/5973;
  `alembic_compat` `ALIASED_NAMES` 47 with exactly eleven frozen revisions
  importing the aliased helper; `refuse_silent_legacy_state_replacement`
  1365 with `development.py` calls at 221/225; the stale sentences in
  README 89–91, ROADMAP 79–80, DEVELOPMENT 156–161, `deploy/ubuntu/README.md`
  56–60 and the runbook sections at 273 and 1137. The report's LEAD is
  answered by C9-A evidence: `/var/lib/framenest` no longer exists on the host
  and the final name sweeps show no reference to it, so the parked
  `DEPLOYMENT_STATE_DIR` stays classified and untouched. Plan accepted as
  written: B/1 removes the one-time migration commands, B/2 retools the
  former-layout selection to canonical-only, B/3 finalizes living truth, then
  publication, refresh and rendered acceptance. Session-62 prompt
  `62_implementation_00.md` (`KSI-IMPL-C9B1`) issued.

- **2026-10-17/18 — C9-B/1 ACCEPTED independently; C9-B/2 issued.** Commit
  `f2c4624ded775e3446bfafef4a5a413253a03136` ("Remove the finished one-time
  identity and capture-path migration commands", 8 files, +167/−9543):
  verified by the Orchestrator — every deleted symbol absent from the engine
  (`migrate-identity`, `migrate-capture-paths`, `MIGRATION_PHASES`,
  `observe_capture_path_plan`, `run_migration_apply`), keeps present
  (`ACCEPTED_RELEASE_SHA_MARKERS`, `CAPTURE_BRIDGE_UNIT`,
  `EXIT_MIGRATION_REQUIRED` 13, `OLD_WEB_LAYOUT`/`WEB_LAYOUTS` for B/2,
  `read_release_markers`), focused five-module run `162 passed`, independent
  full suite `4714 passed, 8 skipped, 3 warnings, 0 failed` in 679.15 s (the
  −302 from the 5016 baseline = the deleted migration module and the 15
  removed capture-path tests). The report's measured retention re-pin:
  deploy occurrences 72→25, tests 1386→1101, docs 751→748, `/opt/framenest`
  145→122, content path −1. The `EXIT_MIGRATION` prefix near-miss (which also
  removed `EXIT_MIGRATION_REQUIRED` = 13) was caught by the first focused run
  and restored before any green suite. The session-61 report was archived to
  `61_report_00.md` (it had not been stored in the Meta directory; the worker
  had read it from the Cursor plan). Session-63 prompt
  `63_implementation_00.md` (`KSI-IMPL-C9B2`, canonical layout only) issued
  against `f2c4624`.

- **2026-10-18 — C9-B/2 ACCEPTED independently; C9-B/3 issued.** Commit
  `9b291e936e93026ebe540b4a23a11b89721747a8` ("Retool the release engine so
  routine commands use only the canonical layout", 7 files, +419/−263):
  verified — every removed selector absent (`OLD_WEB_LAYOUT`, `WEB_LAYOUTS`,
  `OLD_CAPTURE_CURRENT`, `CAPTURE_POINTERS`, `SERVICE`, `SERVICE_USER`,
  `SERVICE_GROUP`, `RELEASE_ROOT`, `CURRENT`, `CAPTURE_CURRENT`, `ENV_FILE`),
  `CANONICAL_WEB_LAYOUT` 183 with `WEB_LAYOUT_CANDIDATES` 198 = one member,
  `CANONICAL_CAPTURE_CURRENT` 201, no function default naming a former path,
  keeps present (marker tables 52/62, `POETRY_BIN` 76, `CPYTHON_BIN` 77);
  independent full suite `4713 passed, 8 skipped, 3 warnings, 0 failed` in
  687.42 s (the −1 = −4 backup-cli parametrize cases +3 new proofs). Retention
  re-pin measured: deploy occurrences 25→9 (engine 22→6 = the two marker
  names, the historical manifest key, the two tooling paths, the sanitizer
  needle), tests 1101→999, `/opt/framenest` 122→64, `User=framenest` 2→0,
  `Group=framenest` 3→1. Both mutations observed (second candidate → the
  single-layout test fails; absent branch → the capture-pointer test fails).
  Disclosed near-miss: a `python3 -c 'print("skip")'` was invoked while
  collecting git evidence (not product evidence, not a mutation; the contract
  route carried all product evidence) — a disclosed minor, no product effect.
  The session's LEAD: `cmd_remote_service_fragment_path` has no caller — note
  for a later cut. Session-64 prompt `64_implementation_00.md`
  (`KSI-IMPL-C9B3`, living truth) issued.

- **2026-10-18 — C9-B/3 report came back BLOCKED; the fail-closed gate worked
  and exposed both a taxonomy gap and a real defect.** The three sentence
  edits and the measured `capitalized FrameNest` re-pin (2327→2328) sit
  verified in the worktree but uncommitted: the classification gate found
  **808 of 3375** case-insensitive hits with no owning category, and the
  worker stopped instead of inventing one (disclosed; correct). Orchestrator
  review against the session-25 plan sections 4–6 defines the missing owners:
  source comments and docstrings are outside the identity goal (plan §4);
  existing historical backup/sidecar/snapshot and stored-analysis identities
  are retained with canonical writers (plan §5); historical ADR bodies and
  citations, historical artifacts and their narrowly retained readers are
  retained (plan §5); negative test assertions and retained-spelling
  fixtures are retained (plan §5, §6 rule 3); accepted Python class/module
  names stay; the retired-prefix strip, sanitizer needle, parked budget path,
  `.gitignore` guard and provenance record are owned as before. Two clusters
  need strict per-hit verification: code-local non-operational identifiers
  (logger/coordinator/JS variable names) and stored keys (the web shell keeps
  `framenest.youtube.currentClaim.v1`, `framenest.catalog.pageSize`,
  `framenest.upload.recovery.v1` as historical read/migration keys beside the
  canonical ones — retained per plan §5). **The gate also exposed a real
  defect: `src/kronika/adapters/api/web/app.js` emits
  `X-FrameNest-Request` on unsafe methods while the tailscale ingress gate
  accepts only `x-kronika-request`** (plan §4: request protocols are not
  excluded); its frontend tests pin the former emission. Scheduled as a
  bounded correction (session 66) which will align the emitter, move its test
  mirrors, re-pin the measured retention and verify the emitter inventory
  against the server's expected header. Session-65 prompt
  `65_implementation_00.md` (`KSI-IMPL-C9B3R`) issued: validate and keep the
  four-path worktree edits, re-run the classification under the amended
  taxonomy with the defect in its own scheduled-correction category, run the
  full proof, and commit exactly those four paths.

- **2026-10-18 — C9-B/3 ACCEPTED independently; the category-16 correction
  split into two grants.** Commit `ca280c45755e28b6363690c50d7cdaa42187de96`
  ("Finalize living truth and classify the remaining retired spellings", four
  paths, +14/−8): the three corrected sentences and the
  `CAPITALIZED_OCCURRENCE_COUNT = 2328` pin validated byte-for-byte against
  the session-64 report; my focused run `83 passed` (retention, docs contract,
  both schema-head tests, the sidecar reader, the capture state-name module)
  and an independent `FrameNest` count of `2328`; the report's full suite
  `4713 passed, 8 skipped, 3 warnings, 0 failed` in 719.56 s. The classification
  is complete under the amended taxonomy: 3375 of 3375 hits owned
  (cat 1: 673, cat 2: 20, cat 3: 18, cat 4: 11, cat 5: 12, cat 6: 12, cat 7:
  4, cat 8: 12, cat 9: 1848, cat 10: 569, cat 11: 56, cat 12: 72, cat 13: 2,
  cat 14: 1, cat 15: 8, cat 16: 42, cat 17: 1, cat 18: 2, cat 19: 12), zero
  outside; strict proofs recorded for categories 11 and 15. **Correction
  nuance:** `app.js` sends *both* spellings deliberately (the in-code comment:
  keeps working against a server that predates the dual-read cut; the
  canonical gate value is applied after the merge), so the web shell's
  mutations are not broken — the retired header is a superseded compatibility
  mirror that the closure retires per the C7 direction ("removes environment
  compatibility mirrors") and plan §4 (request protocols are not excluded).
  The category-16 set is larger than the one known header: 24 header mirrors
  in seven test files, 13 thread-name/prefix strings, one `mkdtemp` prefix,
  `DEFAULT_PUBLIC_PUBLISHED_UDS_PATH`, and `default_ai_config_path`'s legacy
  fallbacks (the workspace socket constant stays: the frozen ADR-0048/0074
  bodies cite it). Split: session 66 = the protocol/string hygiene (header,
  thread names, temporary prefix, public socket default); session 67 = the
  AI-config default switch with the migration-coherence proof. Session-66
  prompt `66_implementation_00.md` (`KSI-CORR-C9B16A`) issued.

- **2026-10-19 — C9-B/16A correction ACCEPTED independently; part B issued.**
  Commit `063b045c0e431760cfc48996bec1160c4d4b7e0b` ("Retire the active
  mutation-header mirror, runtime names, and public socket default", 22 files,
  +113/−64): verified — `app.js` canonical-only (`Object.assign({}, headers)`
  plus the post-merge `X-Kronika-Request`, zero retired literals in the file),
  `DEFAULT_PUBLIC_PUBLISHED_UDS_PATH = /run/kronika/kronika-public.sock` with
  `WORKSPACE_UDS_PATH` untouched, the fourteen producer strings canonical
  (`kronika-*`), my focused run `346 passed` (retention, mutation-header,
  ingress, upload-validation, process, local web application) and the seven
  JS suites exactly `23/41/55/12/30/6` plus bounded glob `212`; the report's
  full suite `4713 passed, 8 skipped, 3 warnings, 0 failed` in 720.39 s. The
  measured retention re-pin: `src` 1604→1587, `tests` 999→987, mutation-header
  37→31 and files 16→14, capitalized 2328→2321 and files 343→341; both
  mutations observed (the restored header fails the frontend mirror; the
  restored thread prefix fails the upload-validation pin). Disclosed near-miss
  (second occurrence of the pattern): an accidental `/usr/bin python3 -c`
  printed `skip`, not used as evidence; the contract route carried the
  product evidence — recorded for the closing critique. Part B = the last
  category-16 correction: `default_ai_config_path`'s fallback literals switch
  to canonical while the migration module's legacy constants and its legacy
  AI source move stay untouched, with the migration-coherence proof explicit.
  Session-67 prompt `67_implementation_00.md` (`KSI-CORR-C9B16B`) issued.

- **2026-10-20 — C9-B/16B ACCEPTED independently; category 16 closed; the
  final candidate is verified and the publication/refresh/acceptance
  sequence is issued.** Commit `22615a7721d89777bf1614b03baec220c80d3782`
  ("Point the unset AI config default at the canonical migration
  destination", 4 files, +105/−23): verified — the darwin and XDG fallbacks
  are `Kronika`/`kronika`, the migration module is absent from the diff, the
  coherence test binds the new default to the migration's canonical AI
  destination and the previous default to its legacy source, my focused run
  `119 passed` (local-state migration, AI config storage, direct reader
  routing, product-string agreement, retention), and my independent full
  suite `4713 passed, 8 skipped, 3 warnings, 0 failed` in 665.93 s. Retention
  re-pin measured: `src` files 183→182 (`infrastructure/ai/configuration.py`
  leaves the content set), `src` occurrences 1587→1585, `tests` 987→986,
  capitalized 2321→2320 / 341→340; the product-string inventory was missed by
  the path-literal parse, caught by the first full suite, measured, pinned
  (occurrences 63→64, in-scope 61→62, duplicate literal 8→9) and the suite
  re-ran green. The mutation was observed (restored darwin literal → the
  coherence test fails). With this, **category 16 is closed** and the
  repository candidate for publication is `22615a77`; local `main` is five
  commits ahead of public `5b86d896` (`f2c4624`, `9b291e9`, `ca280c4`,
  `063b045`, `22615a77`). The final Cooperator grant is issued: publish, the
  routine NUC refresh through `deploy/ubuntu/kronika-release` to the exact
  SHA (capture stays on `5b86d896`; no capture code changed), and the
  rendered acceptance against the refreshed tailnet UI including the
  companion review flows. Residual notes for CLOSE: the migration module's
  opening sentence about the current defaults is slightly stale (module
  untouched by design; the coherence test is the live binding), and the
  `python3 -c` near-miss pattern occurred a third time (always disclosed, never
  used as evidence). After the acceptance receipt: C-INSTALL-DOC, then CLOSE.

- **2026-10-20 — Publication PASS; the first NUC refresh attempt failed and was
  localized to the staging-leftover gate; round-2 diagnosis issued.** Push
  `5b86d89..22615a7 main -> main`; `origin/main` = `22615a7721…`. The routine
  deploy's own `check` passed (`layout: canonical`, `public_main` = the
  target, capture identity values), then the deploy failed with the raw
  `command failed` and `DEPLOY_EXIT=20`, host unchanged and healthy (web and
  capture on `5b86d896`, health `ready`, capture `Server:
  kronika-capture/0.1.0`, backup `ExecMainStatus=0`, name sweeps = the
  retained set). The logging-ssh-shim run localized the second attempt to
  `sudo -n test ! -e /opt/kronika/releases/22615a7721….staging` (rc=1): the
  **first** attempt failed somewhere inside the staging build and left the
  `.staging` tree; the engine correctly refused to proceed, self-healed its
  stale deploy scratch (`mkdir` conflict → quarantine as
  `reclaimed-abandoned-owner` → fresh dir), and released the lock and owner
  record. Because the `.staging` path still exists, the first failure was
  before `cmd_remote_rename_staging` (the build window: extract/AP/poetry
  lock+install/relocate/chown/chmod/markers), and its stderr was swallowed.
  Round 2: inspect the leftover tree's phase state, move it aside (exact
  path, evidence preserved), and re-run the deploy with the shim still on
  `PATH` to capture the failing remote command. The NUC timestamp needed
  re-authentication in the evidence block (unexpected, noted; each block
  re-establishes it).

- **2026-10-20 — Refresh round 2 localized the root cause: `poetry install`
  fails with rc=1 (empty shim stderr; the engine discards stdout on failure);
  round 3 reproduces it visibly.** The round-2 shim log shows the full
  successful prefix — check gates, lock, transfers, extract, AP, poetry.toml,
  lock hash, `poetry check --lock`, `poetry env use` ("Creating virtualenv
  kronika") — and then `poetry install --only main --no-interaction --no-ansi
  --directory <staging>` failing with rc=1 and no captured stderr; the
  engine's failure cleanup then `rmdir`s the deploy dir (not empty → the
  tarballs remain as evidence) and leaves the staging tree in place. The
  packaging inputs are identical to the successful 2026-10-17 build
  (`git diff 5b86d89..22615a77 -- pyproject.toml poetry.lock poetry.toml` is
  empty; the repository has no `poetry.toml`; the engine writes the 32-byte
  in-project venv config), so the cause is runtime/environmental, not a
  content regression. Round 3: reproduce the exact command in the newly left
  staging tree with full stdout/stderr, probe memory, disk, PyPI reachability
  and kernel OOM lines, then move that tree aside; if the reproduction exits
  0, immediately retry the deploy with the shim still active, otherwise stop
  with the visible failure.

- **2026-10-20 — Refresh root cause: the NUC's Mullvad exit-node egress is not
  carrying general internet; PyPI times out.** Round-3 probes: RAM 14 GiB
  (9.8 GiB free), disk 192 G free, no kernel OOM lines; `pypi.org` resolves
  (IPv6 answers) but `curl https://pypi.org/simple/` times out
  (`pypi_http=000`). The reproduction could not run because the engine had
  already quarantined its own failed staging as `…staging.failed2-20261020`
  (self-healing again). `docs/OPERATOR_NETWORK.md` + ADR-0058 define the
  durable contract: the NUC selects an explicit Mullvad exit node and all
  general egress goes through it; tailnet traffic (SSH, coordination) works,
  which matches a broken exit-node path rather than no network. The documented
  route is `scripts/operator/network/kronika_mullvad_egress.sh`
  (`status`/`verify` read-only; `recover` clears only the selected exit node,
  the sanctioned fallback to direct egress). The Cooperator flow is issued:
  status + verify through the SSH pipe, and if the Mullvad egress is
  unusable, `recover` + a PyPI probe + the deploy retry with the shim, then
  the cleanup of the two quarantined staging trees (exact paths) and the
  standard evidence. The Mullvad exit node can be re-enabled after the
  refresh via the same contract.

- **2026-10-20 — The egress contract reports `exit-node: none`; the failure is
  NUC-specific direct egress, so the diagnosis moves to the WAN/routing
  layer.** Canonical `status`: backend Running, `client-get` supported,
  `exit-node: none`, LAN access false, Mullvad nodes available, no
  self-advertisement, no standalone tunnel; `verify`: diagnostic transport
  failed, egress unknown. So no Mullvad node was selected for the failed
  builds — general egress was already direct — while the PC on the same LAN
  pushed to GitHub successfully today and the tailnet path works. The
  suspicion is a NUC-specific WAN defect (a lingering `tailscale0` default
  route from the cleared exit node, lost address/lease, or host firewall).
  Round 4: a read-only network matrix that emits device names, address
  counts, route-device names, ping exit codes, split IPv4/IPv6 PyPI probes,
  a GitHub probe and the UFW policy head — no raw private addresses.

- **2026-10-20 — Network matrix: the NUC is on Wi-Fi with LAN-only reach; the
  wired `eno1` is DOWN, so the deploy's package download has no WAN path.**
  `lo` unknown, `eno1 DOWN`, `wlp1s0 UP`, `tailscale0` unknown; two global
  IPv4 addresses, one IPv6; one default route via `wlp1s0`; **both** pings
  fail; `pypi.org` resolves A records and every HTTPS probe times out
  (`pypi_v4`, `pypi_v6`, `github_v4` all 000); UFW is active with only the
  wired-trusted-LAN SSH rule. So the tailnet works because it is LAN-direct,
  while general internet egress is absent — a physical/link-layer change
  (cable/port or the Wi-Fi uplink), not something the repository cuts touched.
  The docs' SSH boundary (wired trusted LAN) confirms the wired path is the
  intended one. The Cooperator flow: identify the network manager and link
  state, plug/connect the wired interface (bounded), verify the default route
  and PyPI reachability, prefer the wired path if the Wi-Fi route still wins,
  then retry the deploy and collect the evidence.

- **2026-10-20 — Cooperator direction change: Kronika now runs over Wi-Fi; the
  cable is out of scope.** The wired path is not pursued. Diagnosis continues
  on the Wi-Fi stack: gateway reachability, whether the Wi-Fi subnet differs
  from the documented wired trusted LAN, an HTTPS probe, a plain-HTTP probe
  (captive-portal detection) and the UFW verbose default policy, plus a
  human-side check whether other devices on the same Wi-Fi have internet. If
  the Wi-Fi network has WAN, the hunt stays host-side; if it has none, the fix
  is router-side (operator domain). The deploy remains blocked either way:
  `poetry install` needs the package index.

- **2026-10-20 — Wi-Fi diagnosis: the network has WAN (other devices work) and
  the block is NUC-specific; the gateway does not answer and the Wi-Fi subnet
  differs from the wired trusted LAN.** `gateway_ping=1`; both HTTPS and
  plain-HTTP time out (`pypi_https=000`, `debian_http=000`); DNS resolves;
  UFW default is `deny (incoming), allow (outgoing)` so the host firewall is
  not the cause; the Cooperator confirms internet works on other devices on
  the same Wi-Fi. Most likely a stale lease/route after the Wi-Fi network
  change. Bounded attempt: read the NM profile method lines (no profile
  names), reconnect `wlp1s0` for a fresh DHCP lease, then re-check the default
  route, gateway, ping and PyPI. If the reconnect does not fix it, inspect
  the profile's IPv4 method/addresses privately and align them.

- **2026-10-20 — The Wi-Fi reconnect lost the lease: NetworkManager is
  inactive; recovery moves to the actual manager on the NUC console.** The
  branch fell back to `ip link set wlp1s0 down/up`, after which the default
  route disappeared (no `dev` line; `gateway_ping=2` with an empty gateway;
  no PyPI). The NUC may momentarily be off the tailnet, so the next step is
  NUC-console only: detect `systemd-networkd`/netplan, re-run the interface
  configuration for a fresh DHCP lease, verify address count, default route,
  gateway, ping and PyPI, and only then resume the PC-side deploy retry.
  NetworkManager is not the manager and `nmcli` is not the tool here.

- **2026-10-20 — networkd reconfigure restored the lease and default route, but
  the gateway still does not answer and egress fails; the host configuration
  is sane, so the remaining evidence decides host-side vs network-side.**
  Before and after: one IPv4 address on `wlp1s0` and one default route via it;
  `gateway_ping=1`, `ping4=1`, `pypi=000`. Round 6 gathers neighbor-state
  counts, radio signal/frequency/bitrate, `wpa_supplicant` state (no SSID/
  BSSID), a masked `systemd-networkd` journal tail, and an ARP-level gateway
  probe when `arping` exists. A FAILED/INCOMPLETE gateway neighbor or a weak
  distant association points to the AP association path (router-side, operator
  domain); a REACHABLE gateway with no WAN points to router filtering.

- **2026-10-20 — L2/L3 to the AP is healthy; the last two candidates are the
  Tailscale policy table and the router's own WAN/client rules.** Neighbor
  entries are REACHABLE; the association is a healthy 5 GHz WPA2 link to the
  Archer AP (-70 dBm, 195–260 Mbit/s); DHCP and the default route are correct
  before and after the reconfigure, so the silent gateway is not itself proof
  of a broken path. Round 7: `ip rule`/`ip route show table 52` (Tailscale
  exit-node policy table) and `ip route get` for an IPv4 and IPv6 destination
  (device only), plus an HTTP probe of the gateway's own interface. A
  `tailscale0` device in the `get` result or a table-52 default route is the
  blackhole; restarting `tailscaled` (bounded, capture services untouched) is
  then the correction. Otherwise the cause is the Archer's WAN/client policy
  and the fix is router-side. A `tailscale0` device in the `get` result or a
  table-52 default route is the blackhole; restarting `tailscaled` (bounded,
  capture services untouched) is then the correction.

- **2026-10-20 — Confirmé: the Tailscale exit-node policy table blackholes all
  general egress.** `ip rule` line 5270 sends every non-marked packet to table
  52, and table 52 contains `default dev tailscale0` while the prefs say
  `exit-node: none` — an inconsistent daemon state left after the exit node
  was cleared. Both `ip route get` probes resolve to `tailscale0`, and the
  gateway's own HTTP probe never leaves (`gw_http=000`), which is why every
  external probe timed out while the LAN, ARP, DHCP and the Wi-Fi association
  stayed healthy. Fix: restart `tailscaled` so the route tables resync from
  the empty prefs (general traffic returns to the `wlp1s0` default; the
  tailnet re-establishes with persisted state; capture services untouched),
  then re-probe PyPI, retry the deploy and collect the evidence. Re-enabling
  a Mullvad exit node afterwards stays an operator choice through the
  contract script.

- **2026-10-20 — The tailscaled restart did not clear the table-52 default; the
  next step is the prefs read, a forced canonical empty set, and (if needed)
  exact reversible route surgery.** After the restart, table 52 still holds
  `default dev tailscale0` plus the tailnet peer routes, `ip route get
  1.1.1.1` still resolves to `tailscale0` while the main default correctly
  uses `wlp1s0`, and egress remains dead. Round 8: read the daemon's exit-node
  prefs, run `tailscale set --exit-node=` (the documented empty set, forcing
  a route resync), and verify; if the default persists, delete exactly that
  one route from table 52 (reversible: re-add with the same command), which
  lets the policy rule fall through to the main table. Then re-probe PyPI and
  resume the deploy retry. The anomaly — policy table default surviving both
  a cleared pref and a daemon restart — is recorded as an operator finding for
  the closing report; ADR-0058's scripts should eventually harden `recover`
  against it.

- **2026-10-20 — Evidence block confirms the old release still serves and a
  stale staging from an earlier attempt remains; network-fix outputs were not
  captured.** `check-health` ready, both pointers on `5b86d896`, the two
  quarantined trees removed, and a plain `…22615a77….staging` from 15:32
  still present — the deploy never ran again after it. Round 9: re-read the
  table-52/route/pypi state, delete the anomalous route if it survived, remove
  the stale staging so the pre-existence gate is free, then retry the deploy
  with the shim and collect the evidence. The route deletion is stable while
  tailscaled keeps running (it re-syncs only on netmap or prefs changes).

- **2026-10-20 — NUC REFRESH COMPLETE: the routine deploy of `22615a77`
  succeeded after the network fix.** `kronika-release deploy` →
  `deploy complete: 22615a7721…`, `web_release: 22615a7721…`,
  `capture_release: 5b86d896…` (capture-neutral), `DEPLOY_EXIT=0`,
  `remote_lock: acquired (none)`, `unit_executables:
  .venv/bin/kronika-production`; the shim log shows every phase rc=0 through
  the cleanup; `status`: layout canonical, active/web `22615a77`, capture
  `5b86d896`, service active, DB `0035`, backup ready; NUC evidence:
  `check-health` ready, `current` → `releases/22615a77…`,
  `capture-current` → `releases/5b86d896…`, `/run/kronika-release-deploy*`
  absent. Public-main equality is proven by the deploy's own check on top of
  the push. The blocking cause was the Tailscale policy-table blackhole
  (table 52 `default dev tailscale0` with no exit node), cleared by the exact
  route deletion; the fix held through the build. Remaining sequence: the
  Cooperator's rendered acceptance, then C-INSTALL-DOC and CLOSE. Operator
  findings for the closing report: ADR-0058's `recover` did not clear the
  policy-table default; the Mullvad exit node is currently none (operator's
  choice to re-enable); the NUC now runs over Wi-Fi per the Cooperator's
  decision — `eno1` stays down and the UFW wired-SSH rule is now descriptive
  history (the tailnet path serves SSH), which the clean-install runbook
  should reflect.

- **2026-10-20 — Orchestrator rotation handout generated (`68_handout_00.md`),
  restoration readiness PASS.** The outgoing Orchestrator produced a
  contract-shaped Fresh Orchestrator Restoration prompt (phase Restoration,
  synthesis only, no authority) per `.ap/PROMPT_CONTRACTS.md`: identity and
  communication rules; Stage 1 read-only restoration; the file map (repository,
  public, Meta trace, host, archive); the exact verified state (HEAD = public =
  `22615a77`, clean tree, AP pin `73e20ef8…`, full suite `4713/8/3/0`, host
  web/capture releases, pointers, DB `0035`, backup ready, the retained former
  set, the network incident and its exact fix, the operational notes for host
  work); what the whole is and the frozen boundaries; the completed cuts with
  their commits; the remaining sequence (A rendered acceptance — pending, the
  only human gate; B C-INSTALL-DOC reframed as clean-install/recovery; C CLOSE
  per the section-5 closure table); the retained Cooperator decisions (host
  identity, Wi-Fi, no reinstall, parked items); the non-negotiable discipline
  (twelve rules, including the classification taxonomy, measured re-pins,
  exact-object host work, deploy forensics, the systemd-run health wrapper and
  the Tailscale table-52 rule); an honest error record of this era's
  Orchestrator mistakes; the successor's first act (verify, then request the
  rendered receipt); open risk; and the no-mutation-authority statement. The
  outgoing session remains the reference until the fresh Orchestrator confirms
  restoration.

- **2026-10-20 — CORRECTION: the Cooperator declined the rotation; this
  Orchestrator session continues as before.** The handout
  `68_handout_00.md` is marked NOT ACTIVATED in place and retained as a
  reference checkpoint of the post-refresh state; no successor inherited from
  it. The remaining sequence is unchanged and continues here: the Cooperator's
  rendered acceptance receipt (the only pending human gate), then
  C-INSTALL-DOC, then CLOSE.

- **2026-10-29 — Rendered acceptance surfaced a defect: "Save to Kronika
  failed" when saving an X meme through the extension.** Repository check:
  the extension sends the canonical `X-Kronika-Request: 1` header
  (`extension/background/service_worker.js`), and its failure mapping reserves
  the specific texts for the category errors and for ambiguous network states;
  the plain message means the request result carried an error or the claim
  reached state `failed` — an app-side acquisition/submission failure or a
  network failure, not a header mismatch. Diagnosis opened: the app journal
  around the attempt (`journalctl -u kronika.service` filtered for
  x/requests, mutation, yt-dlp, publish, quarantine), the companion-origins
  environment key presence, and the current network state — after ten days a
  reboot can have reintroduced the Tailscale table-52 blackhole
  (`default dev tailscale0`), which would break the yt-dlp download path.
  Two Cooperator datapoints requested: the last time an X save worked, and
  whether the NUC rebooted since the 2026-10-20 fix.

- **2026-10-29 — Cooperator datapoint: X saves were not tested for a long
  time; the defect may predate this whole.** So it must be classified, not
  assumed to be a refresh regression. The app-runtime changes of this era
  (web-shell header, thread names, AI default, public socket default) do not
  touch the extension-server X flow; the last change that did is the C7-era
  canonical request-protocol cut — if the Brave extension installed there is
  an older build still sending the former mutation header, its saves would
  fail with 403 since then, and the extension maps that to the plain "Save to
  Kronika failed". The decisive datapoints: the installed extension revision
  versus `extension/manifest.json`, the app journal around the attempt, and
  the current network/blackhole state. Classification candidates:
  (a) pre-existing old-extension protocol mismatch (operator-side reload or
  rebuild, not a repository change); (b) network/blackhole or X-login failure
  in the yt-dlp path; (c) an app-side regression (bounded correction). The
  rest of the rendered acceptance (Gallery, Details, companion review flows)
  is still owed for the receipt.

- **2026-10-29 — Extension and network are exonerated; live reproduction is the
  next evidence.** Installed extension = `Kronika X Companion` 0.2.0 (the
  canonical-header build); tree 52 has no `default` line, `ip route get
  1.1.1.1` resolves to `wlp1s0`, `pypi_v4=200`; the companion-origins key is
  present; the app journal had no matching line in three hours. The remaining
  candidate class is the X acquisition itself: the claim ends `failed` after
  the download attempt, which the extension maps to the plain message. The
  next step is a live reproduction — retry the save, then read the unfiltered
  journal window and the staging count — to capture the app-side error for the
  claim.

- **2026-10-29 — The save now passes; the AI content analysis fails and becomes
  the acceptance focus.** The earlier save failure is recorded as transient
  (extension 0.2.0, canonical header, clean network). The analysis failure is
  the key function finding. First classification question: whether the
  session-67 AI-config default change (fallback `Kronika`/`kronika`) matters
  on the NUC — only if `/etc/kronika/kronika.env` lacks
  `KRONIKA_AI_CONFIG_PATH` would the app now resolve the XDG fallback
  (`/var/lib/kronika/.config/kronika/ai/config.json`) instead of the
  historical `.config/framenest/...` path, making a previously working
  selection invisible. Evidence round: the AI-related env keys (masked), the
  `ai/` directory and both `.config` AI paths, `runtime-settings.json`, the
  credential drop-ins, and the journal around the failed analysis. The
  Cooperator also plans the model-administration and new-model-on-existing-
  records flows; those include real provider calls and remain his explicit
  authority.

- **2026-10-29 — The session-67 AI-path change is exonerated: the live env sets
  `KRONIKA_AI_CONFIG_PATH` explicitly.** `/var/lib/kronika/ai/config.json`
  exists (1049 B, 2026-10-16) and holds the provider/model selection (no
  `runtime-settings.json` overlay); the `.config` AI fallbacks are absent;
  `KRONIKA_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` and `..._MAX_ATTEMPTS` are set;
  the NVIDIA credential drop-in and the research drop-in are installed. The
  failed analysis therefore points at the provider call or the analysis
  pipeline, not at configuration resolution. Next: show the non-secret config
  (masked for any key-like field), retrigger the analysis on the saved record,
  and capture the unfiltered journal window plus the earlier save/analysis
  window to obtain the app-side error.

- **2026-10-29 — The AI analysis failure is a host provisioning gap, not a code
  regression: the active provider is `vercel-ai-gateway` but only the NVIDIA
  credential drop-in is installed.** The live config selects
  `vercel-ai-gateway` / `google/gemini-3.1-flash-lite` (updated 2026-10-16)
  with `nvidia-nim` as the alternative; the repository contract requires
  `AI_GATEWAY_API_KEY` via `kronika-ai-credential-vercel-ai-gateway.conf`,
  while the installed drop-in is `20-ai-credential.conf` = NVIDIA_API_KEY
  only. The journal carries no analysis entries (the app does not journal
  them), so the decisive evidence is the `media_analysis_runs` row
  (`state`, `error_code`, `error_message`) plus the credential-directory
  names. The Cooperator's planned model-administration test — switching the
  active provider/model to a provisioned one (nvidia-nim) — is the natural
  acceptance path; provisioning the vercel credential is separate secret
  authority and an optional follow-up.

- **2026-10-29 — Confirmed in the database: since the 2026-10-16 selection of
  `vercel-ai-gateway`, every analysis run is `failed` / `PROVIDER_UNAVAILABLE`
  with an empty provider id (never submitted), while the successful runs of
  2026-10-12/13 used `nvidia-nim`.** The `AI_GATEWAY_API_KEY` credential file
  exists (`/etc/kronika/credentials/`, 60 B, preserved from 2026-07-21) but
  the canonical vercel credential drop-in was never installed, so the service
  never receives it. This is a pre-existing host provisioning gap created by
  the model-admin selection, not a regression of this whole. The acceptance
  path: the Cooperator's planned switch of the active provider/model to
  `nvidia-nim` (`nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`, provisioned)
  and re-analysis of the new and existing records. Optional bounded follow-up
  (separate authority, after acceptance): install
  `deploy/systemd/kronika-ai-credential-vercel-ai-gateway.conf` into
  `kronika.service.d/`, daemon-reload and restart the service — with the caveat
  that the 2026-07-21 key's validity is unknown.

- **2026-10-29 — The batch analysis refusal is by design; re-analysis of existing
  records is not a shipped UI surface in this product version.** The admin
  "Analyze selected" batch is first-analysis-only (the UI text and the
  confirmation say so; ineligible items are skipped). The server's
  `RequestManualMediaAnalysis` would create a superseding pending run when the
  latest matching run is terminal, but the UI deliberately does not expose a
  re-analysis action (no record-detail analyze button; the batch eligibility
  blocks requested/finished states). This matches the accepted scope and is
  not a regression. The acceptance path for the AI area is therefore:
  switch the active provider/model in the AI admin to the provisioned
  `nvidia-nim` / `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` (the model
  proved vision-capable in the 2026-10-12/13 runs), use the AI admin ping
  test (a real provider call under his authority), then save a fresh X meme —
  a new record with no run — and run the batch analysis end to end. The
  previously failed record stays terminal under the shipped UI (first-analysis
  rule); it is a documented product-surface note, not acceptance debt.

- **2026-10-29 — A retest failed again on a specific X post
  (`.../the_cia_hacker/status/2115577977228374351`); the save flow is
  post-dependent.** The first save succeeded, this one fails, so the earlier
  transient conclusion is revised: the evidence is the `x_post_claims` row
  (`state`, `failure_stage`, `failure_code`, success/failure counts), the app
  journal around the attempt (the unit does log to journald), and an x.com
  reachability probe. Candidate classes: a post-level external condition
  (login/age gate, protected media), the pinned X extractor drifting from the
  live site (pre-existing external compatibility debt — the downloader is
  pinned to `yt-dlp==2026.7.4` and a `TwitterIE._extract_status` signature),
  or an app-side failure. The classification decides whether this is the
  whole's debt (bounded correction) or pre-existing external compatibility
  (recorded, separate task).

- **2026-10-29 — The recurring save failure is `acquisition` / `X_STAGING_FAILED`:
  the downloader's "X produced no artifact" path (yt-dlp exits 0, prints the
  matching id, yet `artifact.bin` absent), or the photo bridge's invalid
  staging path.** The claim ledger: the 10:45 save completed (1 asset) while
  the 11:26 retest failed with 0/1; earlier failures were extractor drifts
  (Oct 20/25) and a no-supported-media post. The photo path uses the custom
  pbs bridge, the video path the pinned yt-dlp subprocess (fixed output name
  `artifact.bin`, cwd = the claim staging). Next evidence: the per-asset rows
  (`media_type`, `stage_key`, state, failure fields) and the recent staging
  leftovers, which show whether a photo or a video asset failed and what file
  the tool actually left. That distinguishes the photo bridge (`X_STAGING_FAILED`
  path-invalid), a yt-dlp output/naming or merge issue (bounded correction if
  app-side), and the external extractor class.

- **2026-10-29 — Root pattern confirmed: every failed asset is `video`
  (`X_STAGING_FAILED`), every success is `image` (`cataloged`), since at least
  2026-10-13.** The photo bridge path always works; the yt-dlp video path never
  produced an artifact. The downloader runs yt-dlp with a fixed
  `--output artifact.bin`, cwd = the claim staging directory, a minimal
  environment (PATH/LANG/LC_ALL/PYTHONNOUSERSITE/NO_COLOR) and
  `--print after_move:%(id)s`; the failure path is reached only when yt-dlp
  exits 0 and the artifact is absent, so the tool reports success while writing
  nothing to the staged directory. Next: a bounded manual reproduction of the
  exact argv/env in a writable temp directory, capturing yt-dlp stderr, the
  exit code, the printed id and the produced filenames — plus the recent
  staging leftovers — to distinguish an output/naming or cwd issue (bounded
  correction) from an external X/format condition (pre-existing known issue).
  The reproduction is the Cooperator's action on a public post he already
  tried to save.

- **2026-10-29 — ROOT CAUSE FOUND (app-side, pre-existing): merged X video
  downloads append the extension to the fixed staging name.** The manual
  reproduction of the exact subprocess printed the media id, exited 0 and left
  `artifact.bin.mp4` — not `artifact.bin` — because yt-dlp post-processes the
  merged video+audio stream. The downloader's artifact resolution checks only
  the exact fixed name, so every video acquisition ends in
  `X_STAGING_FAILED` ("X produced no artifact") while every photo (the bridge
  writes the exact name) succeeds — exactly the observed ledger pattern since
  2026-10-13. Not a refresh regression and not an external X condition. A
  bounded correction grant is issued (session 69, `KSI-CORR-XVIDEO`): resolve
  the artifact strictly but merge-aware (the exact fixed name, or exactly one
  regular file = the fixed name plus one appended extension segment; no
  symlinks, no temp/partial files, multiple candidates fail closed), the
  consumers use the resolved path, new tests (merged-video success, empty
  artifact unchanged, two-candidate fail-closed, photo path unchanged), the
  measured retention re-pin if any, the mutation proof and one commit. After
  publication and a routine refresh, the Cooperator retests the failed claim
  through the extension's retry path; then the AI acceptance continues on
  nvidia-nim, C-INSTALL-DOC follows and CLOSE reconciles everything.

- **2026-10-29 — X-video correction ACCEPTED independently; publish + refresh +
  video retest issued.** Commit `7d6463f54d0552eb54e0d6fe39d49171c8ce31e0`
  ("Fix X merged video artifact resolution", 5 files, +322/−20): verified —
  `staging.find_artifact` prefers the exact fixed name (non-symlink regular
  file) and otherwise accepts exactly one merged candidate matching
  `artifact.bin.<1–10 alphanumeric>` with temporary suffixes excluded, failing
  closed with `X_STAGING_AMBIGUOUS` on multiple candidates; the downloader and
  the staging reader consume the resolved artifact; my focused run
  `113 passed` (downloader, staging, X lifecycle, retention); my independent
  full suite `4759 passed, 8 skipped, 3 warnings, 0 failed` in 679.00 s (the
  report's +46 over the 4713 baseline = the new and parametrized tests);
  retention Part A/B/C unmoved. Report critique recorded: my prompt's test
  locator `tests/unit/infrastructure/x/` was wrong — the owning modules live
  directly under `tests/unit/infrastructure/`; the worker derived correctly.
  Next, one Cooperator flow: publish the commit, run `status`/`check`, the
  routine deploy of `7d6463f` (capture-neutral), collect the NUC evidence, and
  retest the failed X video claim through the extension; then the AI
  acceptance on `nvidia-nim` and the closing rows C-INSTALL-DOC and CLOSE.

- **2026-10-29 — PUBLISH + REFRESH of the X-video correction DONE.**
  `22615a7..7d6463f main -> main`; `check` verified public main, AP pin,
  superproject and capture identity; `deploy complete: 7d6463f…`,
  `web_release: 7d6463f…`, `capture_release: 5b86d896…` (capture-neutral),
  `remote_lock: acquired (none)`, `unit_executables:
  .venv/bin/kronika-production`; status active/DB `0035`/backup ready;
  NUC evidence: `check-health` ready, `current` → `releases/7d6463f…`,
  `capture-current` → `releases/5b86d896…`, releases = {22615a77, 5b86d896,
  7d6463f, c0f4566}. The Cooperator's video retest is the next step, then the
  AI acceptance on `nvidia-nim`.

- **2026-10-29 — The Cooperator hit `AI_PROVIDER_UNAVAILABLE` in an AI flow; the
  active selection is still `vercel-ai-gateway` and the switch is a pure config
  write.** The UI text maps the code from the AI-admin and media-suggestion
  endpoints; the X save path has no provider dependency (the image saves
  succeeded while the provider was down). `PUT /api/admin/ai/active-selection`
  validates provider/model against the config and writes it without any
  provider connectivity call, so the switch to the provisioned `nvidia-nim`
  works despite the unavailable provider. The acceptance steps: switch the
  active selection, run the admin Ping (the real provider test), then analyze a
  fresh record; separately confirm the video retest outcome.

- **2026-10-29 — AI admin is green after the switch (nvidia-nim, credential
  present, connection test success) yet an unavailable-provider message
  persists somewhere.** The wiring explains the split: the media-suggestion
  and lifecycle APIs read the provider lazily through
  `ai_provider_resolver.resolve` (fresh config read), while a startup-resolved
  provider and a `LazyResolvedAiProvider` also exist; the admin ping uses the
  same resolver and succeeds. The persisted message is therefore either the
  display of a pre-switch failed run (vercel era) or a different surface. The
  decisive evidence: the latest `media_analysis_runs` rows (timestamps,
  provider ids after the switch), the latest x claims/assets (the video retest
  outcome), and the exact UI surface where the message appears.

- **2026-10-29 — ACCEPTANCE AREAS LIVE-PROVEN: video fix, gif save and
  nvidia-nim analyses all succeed.** X claims: the retried video
  `2115577977228374351` completed at 12:39 and the new gif
  `2115700394634682600` at 12:53; assets `video` and `animated_gif`, both
  `cataloged` (the video's 2,301,563 bytes match the reproduction). Analysis
  runs at 12:39:34, 12:42:02 and 12:53:44 are `analyzed` with
  `nvidia-nim`/`nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`; one transient
  `PROVIDER_UNAVAILABLE` run at 12:42:03 (empty provider id, between
  successes — the switch transition) is recorded and does not leave any
  substantive media unanalyzed. The AI admin switch, credential presence and
  connection test are green. The Cooperator's explicit rendered receipt is
  requested for the closure record; then C-INSTALL-DOC and CLOSE remain.

- **2026-10-29 — Cooperator change request: the admin batch must allow
  re-analysis.** He wants "Analyze selected" in Manage media publication to
  enqueue analyses for already-analyzed or failed records (the new-model-on-
  existing-records flow). The server already supports it: the durable-analysis
  endpoint's `RequestManualMediaAnalysis` creates a superseding pending run
  when the latest matching run is terminal and stays idempotent while one is
  active. Only the UI eligibility blocks it: `adminAnalysisEligibility`
  currently accepts `analysis_state === "not_requested"` alone. ADR-0049's
  frozen "Deferred Work" list (multi-select, bulk first analysis, batch
  progress) is historical — those surfaces shipped later — so no ADR edit is
  needed. A bounded UI correction grant is issued (session 70,
  `KSI-CORR-REANALYZE`): eligibility becomes terminal-state-based
  (`not_requested`, `analyzed`, `failed`; ineligible only for active runs),
  all first-analysis-only texts and the confirmation copy move with it, the
  frontend tests are updated and extended, the declared JS glob count moves by
  exactly the added cases, Python stays `4759/8/3/0`, retention unmoved, one
  commit. After publication and refresh the Cooperator retests the bulk
  re-analysis, finishes the receipt, then C-INSTALL-DOC and CLOSE.

- **2026-10-29 — Re-analysis correction ACCEPTED independently; publish +
  refresh + retest issued.** Commit
  `f6859362f64cf4b5d5ec7529785d53e1ad483969` ("Allow administrator batches to
  re-analyze terminal media", 2 files, +85/−20): verified — eligibility now
  uses `AUTOMATIC_ANALYSIS_TERMINAL_STATES` (not_requested/analyzed/failed
  eligible; `pending`/`analyzing` ineligible with the new active-analysis
  reason; unknown fail-closed), the enqueue stays the per-item
  durable-analysis POST (server supersession verified read-only), and every
  first-analysis-only string moved to the re-analysis truth. My independent
  runs: admin batch `54 passed` (+4), the six named suites unchanged
  (23/41/55/12/30/6), bounded glob `216` (212+4), full Python
  `4759/8/3/0` in 679.48 s, retention 15. Report critique recorded: my prompt
  named six unchanged-suite counts without their filenames — resolved by
  repository inspection. Next, one Cooperator flow: publish `f685936`, the
  routine deploy (capture-neutral), NUC evidence, then the bulk re-analysis
  retest on existing records with `nvidia-nim`, after which the rendered
  receipt completes and C-INSTALL-DOC and CLOSE follow.

- **2026-10-29 — PUBLISH + REFRESH of the re-analysis correction DONE.**
  Push `7d6463f..f685936`; `check` verified public main, AP pin and capture
  identity; `deploy complete: f685936…`, web/active `f685936…`, capture
  `5b86d896…` (capture-neutral), `remote_lock: acquired (none)`,
  `unit_executables: .venv/bin/kronika-production`; status active/DB `0035`/
  backup ready. The NUC evidence block raced the deploy and captured a
  mid-flight snapshot (`current` still `7d6463f`, the staging directory still
  present); the helper's own post-deploy status is authoritative. A quick
  re-read of the pointers/releases/health confirms the final state, then the
  Cooperator's bulk re-analysis retest closes the rendered receipt.

- **2026-10-29 — Bulk re-analysis retest: 2 analyzed, 2 failed with provider
  5xx-class unavailability.** The flow itself works: the batch accepted the
  terminal-state items, queued them sequentially and two analyses completed
  with `nvidia-nim`. The two failures show "AI provider is temporarily
  unavailable", which the provider mapping reserves for HTTP 5xx and transport
  unavailability — not 429 (rate limit has its own message), not auth, not
  model-404 — so the failures are external NVIDIA endpoint transients,
  fail-closed and retryable. The analysis retry policy (attempts within the
  configured maximum) and the new terminal eligibility make a retry the
  natural confirmation. DB check and a retry of the two failed records are
  the next step; on success the rendered receipt completes with the provider
  transients documented.

- **2026-10-29 — Retest detail correction: the two failed runs carry an EMPTY
  provider id (pre-submission), so the 5xx reading is not yet proven.** The
  run order matches the batch (GIF analyzed, matrix failed, geometric failed,
  Bad ass analyzed) and the analyzed runs record `nvidia-nim`; the failed ones
  recorded no provider, which points at the provider resolution/construction
  failing before submission (or the run recording the id only on submission).
  The corrected query includes `provider_submission_occurred` (and the proper
  `unixepoch` modifier — the earlier `'utc'` was my query's bug, not the
  data). The pending retry of the two failed records decides: success =
  transient resolution/provider hiccup, retryable; the same failure again =
  content- or resolution-specific and needs a bounded investigation.

- **2026-10-29 — Corrected reading: the failed runs DID submit (submission
  flag 1); the empty provider id is the failure-path recording policy.** The
  corrected query shows `provider_submission_occurred = 1` on the failed runs
  as well, so the provider was constructed and called and the failure is the
  API response class (5xx/transport → UNAVAILABLE). Successes interleave with
  the failures across 15:52, 17:04 and 17:31:03/16 versus 17:31:11/14 — the
  NVIDIA endpoint is intermittently returning unavailability. The failure is
  external, fail-closed and retryable; the pending retry of the two failed
  records is the final receipt evidence.

- **2026-10-29 — RENDERED ACCEPTANCE COMPLETE; C-INSTALL-DOC issued.** The
  retry of the two provider-failed records passed ("Preslo to") and the
  Cooperator directed the whole to closure. Receipt record: the NUC serves
  `f685936`; the web shell and companion flows work over the tailnet with the
  canonical mutation header; X image, video and animated-gif saves complete
  and catalog; the AI admin switch to `nvidia-nim` with credential and
  connection test succeeds; analyses and the bulk re-analysis complete with
  `nvidia-nim` (superseding runs, terminal eligibility) and the two provider
  5xx failures retried successfully — provider transients are external,
  fail-closed and retryable. Pre-existing gaps documented and out of scope:
  the vercel credential drop-in (optional) and ADR-0058's `recover` hardening.
  The last repository row, C-INSTALL-DOC, is issued as session 71
  (`KSI-IMPL-CINSTALL`): the clean-install/recovery runbook per plan §2.20,
  reframed by decision A, plus this era's findings — docs-only, one commit.
  Then the final publication, the routine refresh to the resulting SHA and
  the read-only CLOSE reconciliation per plan §2.21 and the section-5 table.

- **2026-10-29 — C-INSTALL-DOC ACCEPTED independently; the final publication,
  refresh and CLOSE evidence are issued.** Commit
  `8c58a81234a97fdf5af9d724a3b526f19745d32a` ("docs: add Ubuntu NUC
  clean-install and recovery runbook", 5 files, +579/−4): the new
  `docs/UBUNTU_NUC_CLEAN_INSTALL.md` reviewed — ten required areas, the exact
  ADR-0085 exceptions only (the four frozen spellings), no values, addresses,
  identities, scripts or provider activation, the helper documented as the
  sole routine route with the manual empty-host bootstrap and the exit-13
  continuation, the sudo lifecycle, the operator notes without values, and
  the historical ADR-0058 caution; links from the deployment runbook and the
  README map; six new documentation-contract tests; measured retention re-pin
  (docs files 84→85, docs occurrences 748→752, content paths 448→449,
  `/opt/framenest` 64→66, mount 13→14). My independent runs: focused
  `81 passed`, bounded JS glob `216`, full Python `4765/8/3/0` in 678.61 s.
  The final Cooperator sequence is issued: publish `8c58a81`, the last
  authorized routine refresh to it, and the CLOSE evidence set (web health and
  served marker, pointers, capture health, services, backup timer and last
  run, release inventory). After that evidence the Orchestrator writes the
  read-only CLOSE reconciliation against the section-5 table, distinguishing
  freshly observed identities from carried receipts and naming the two
  Cooperator-requested acceptance corrections (the X-video fix and the
  re-analysis eligibility extension) in the scope audit.

- **2026-10-29 — Refresh final state confirmed.** `current` →
  `/opt/kronika/releases/f685936…`, `capture-current` →
  `releases/5b86d896…`, releases = {22615a77, 5b86d896, 7d6463f, c0f4566,
  f685936} with no staging remnant, `check-health` ready. The only remaining
  acceptance item is the Cooperator's bulk re-analysis retest; then the
  rendered receipt completes and C-INSTALL-DOC and CLOSE follow. Note for
  CLOSE: the canonical release set now holds five trees (the C9-A retained
  pair plus the three refresh targets); pruning older ones is optional and
  outside this whole.

- **2026-10-29 — LOGICAL WHOLE CLOSED (`kronika-sole-identity`).** Final
  publication `f685936..8c58a81 main -> main`; the last authorized routine
  refresh deployed `8c58a81234a97fdf5af9d724a3b526f19745d32a` (web/active),
  capture unchanged at `5b86d896…`, `check-health` ready, DB `0035`, backup
  ready; fresh CLOSE evidence: `current` → `releases/8c58a81…`, marker
  `.kronika-release-sha` = `8c58a81…`, `capture-current` →
  `releases/5b86d896…`, capture `Server: kronika-capture/0.1.0`, three
  services active, `kronika-catalog-backup.timer` last fired
  `Thu 2026-10-29 03:27:34 UTC` with `ExecMainStatus=0` (timer-triggered,
  16 h before the check) and restore readiness ready; releases =
  {22615a77, 5b86d896, 7d6463f, 8c58a81, c0f4566, f685936}. §5 table all
  clauses evidenced — one canonical package/wheel (fresh packaging tests);
  the fourteen canonical executables; frozen hashes 86+36 (fresh); canonical
  visible/operator output (parsed assertions plus the rendered receipt);
  canonical environment/request protocols; catalog relationships (carried
  C-DATA receipt, live DB `0035`, backup semantics); development and AI
  state; durable compatibility (Part B empty, readers green); canonical NUC
  web layout with the exact served SHA; canonical capture operational
  identity; retired objects (C9-A manifests and the root-only archive);
  timer-triggered backup success; rendered behavior accepted; no scope
  expansion — the audit names the two Cooperator-requested acceptance
  corrections (`7d6463f` X-video artifact resolution and `f685936`
  administrator re-analysis eligibility); and the independent final
  reconciliation with separated identities: repository `8c58a81…` (clean,
  AP pin `73e20ef8…`), public `8c58a81…`, served web `8c58a81…`, companion
  `Kronika X Companion 0.2.0`, capture `5b86d896…`. Retained operator
  findings: the vercel credential drop-in (optional provisioning), the
  ADR-0058 `recover` hardening (documented in the new runbook), the Wi-Fi
  topology decision, the retained live host identity, the deferred
  media-path migration of `/srv/media/framenest-published` with its catalog
  library root, and the optional release-tree pruning. The whole is CLOSED;
  every remaining item is documented and outside its authority.

- **2026-10-29 — Development-continuation handout generated
  (`72_handout_00.md`), restoration readiness PASS.** After the closure the
  Cooperator asked for the best possible prompt for a fresh Orchestrator
  continuing development. The handout is contract-shaped per
  `.ap/PROMPT_CONTRACTS.md` (Fresh Orchestrator Restoration, synthesis only,
  no authority) and carries: the identity and communication rules; Stage 1
  restoration; the file map; the exact final state (repository = public =
  served web `8c58a81`, AP pin, baselines `4765/8/3/0` + JS `23/41/55/6/12/30`
  + glob `216`, host releases/pointers/markers/timers/network, the retained
  former set, the frozen boundaries, the host operational notes); what Kronika
  is now (the shipped surface and the parked rows); the closed whole's
  narrative and its two acceptance corrections; **the forward horizon** (no
  active whole; `NUC Security Hardening` expected before any VPS; the frozen
  wholes; the priority ordering; the declared pattern for scoping the next
  whole); the eleven-rule method this whole paid for; an honest error record;
  open risks; and the no-mutation-authority statement. It supersedes the 68
  handout's purpose (that one targeted finishing the closed whole and remains
  marked NOT ACTIVATED). The outgoing orchestration trace ends here; the fresh
  Orchestrator continues from 72.
