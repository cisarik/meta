# Fresh Orchestrator restoration — opening handout for `kronika-sole-identity`

Artifact relationship: opening restoration handout for a new logical whole.
It transfers information, not authority. Task authority comes only from the
current authoritative Orchestrator routing and the complete Worker prompts
issued from it.

Restoration classification: PASS

```text
Role: ORCHESTRATOR
Orchestrator session target: fresh-agent-orchestrator-session
Capability profile: Orchestrator
Initialization: Capability profile: Orchestrator
Logical whole identity: kronika-sole-identity
Archive sequence: 00
Logical-whole sequence: 03
Trace: /Users/agile/meta/projects/kronika/00/03-kronika-sole-identity/
Live handout: 00_handout.md
Predecessor whole: kronika-one-product
  trace /Users/agile/meta/projects/kronika/00/02-kronika-one-product/
  closed 2026-10-02
Predecessor closure: already emitted. Do not emit it again.
Cooperator: Michal
Delivery route: read-only inventory may proceed. Implementation, Git
  publication, and any NUC mutation require a new bounded grant. This
  handout is not that grant.
Reasoning recommendation: Extra High for the identity-cut Planner.
  An implementation Worker is premature until that plan is accepted.
Development host: MacBook, checkout /Users/agile/Projects/framenest
  branch feat/kronika-one-product
Public repository: https://github.com/cisarik/kronika.git
  main = feat/kronika-one-product =
  0c850996cd2ef17dae4112733fd17fdc732f4699
AP pin, verify, do not upgrade:
  73e20ef80b88700d5fcbc397cd8edd4fc425869f
NUC web release, verified 2026-10-02:
  0c850996cd2ef17dae4112733fd17fdc732f4699
  service active, database revision 0035, backup ready
  capture release unchanged: 94e605c17b881461fad3e22fd8c7fca32cb93976
```

Paste seed for a new Agent chat:

```text
Resume as a fresh Orchestrator for the logical whole kronika-sole-identity.
Read /Users/agile/meta/projects/kronika/00/03-kronika-sole-identity/00_handout.md
completely before any Worker prompt.
Begin read-only. The predecessor kronika-one-product is closed. Do not emit
its closure signal again. Do not mutate, publish, or change the NUC until a
new bounded grant exists.
The objective is one product identity: Kronika. Retire the remaining
framenest package, commands, headers, environment prefix, unit names, and
host paths through a planned cut that keeps the NUC serving.
Communicate with Michal in Slovak. Feminine self-reference. Masculine address.
```

This file opens the whole. It does not authorize implementation. Restoration
grants no repository, implementation, deployment, production, account,
filesystem, external-service, Git, or host mutation authority. The fresh
Orchestrator independently classifies repository and public evidence before
continuing.

## 0. Binding directives

- Speak to Michal in Slovak, masculine address, feminine self-reference.
  Worker prompts, repository artifacts, and reports are professional English.
- Presentation: a status block of at most five lines, exactly one status
  mark, and one decision when a decision is required.
- Python evidence goes through `./.ap/ap project check` and `./.ap/ap exec`
  with an exact `--baseline`. Do not invoke `.venv/bin/python`, `python`,
  `python3`, or `poetry run` for Worker evidence.
- NUC SSH goes through
  `scripts/operator/network/framenest_nuc_worker_gate.fish`. The gate rejects
  shell metacharacters and multiline commands. Do not reconstruct `gpgconf`
  or print agent sockets. The routine release entry point remains
  `deploy/ubuntu/framenest-release` until a later grant replaces it.
  `status` and `check` do not deploy. Deploy never follows from a check.
- Sudo is Cooperator-owned. Workers do not run `sudo -v`. The outgoing
  session released the remote timestamp with `sudo -K` after the 2026-10-02
  deploy. A password prompt is expected lifecycle state, not a broken host.
- Never read `private/**`, browser profiles, cookies, tokens, or credential
  stores. Never print private values, host identifiers, addresses, or secrets.
- The parked capture module stays parked. No browser restart, login, resume,
  activation, job, or ask without a new explicit Cooperator decision.
- `cisarik/cli_chatgpt` stays an active repository. Do not archive it, force
  push, or rewrite history.
- One accountable Worker at a time. Terse confirmation continues the current
  slice. It does not open another whole and it does not authorize a host cut.
- Meta layout is
  `projects/<project>/<archive-sequence>/<logical-whole-sequence>-<identity>/`.
  This whole is archive `00`, sequence `03`. Do not store its handouts inside
  `00/02-kronika-one-product/`.

## 1. What the predecessor finished

`kronika-one-product` accepted one Kronika in the existing repository. Its
active sequence S4-D, S4-A, S6, S4-B, S7-P, S8, S9, S9-R, and S10 is complete
on public `main` and on the NUC web release named above.

S10 renamed the public repositories only:

- `cisarik/framenest` is now `cisarik/kronika`. The old URL redirects to the
  same refs.
- The former capture repository is `cisarik/cli_chatgpt` at
  `66c40d43c577276b0ad304a494fbbb1ffb6fc933`. Michal kept that name and kept
  the repository active.
- Live `Documentation=` URLs in `deploy/systemd/*` point at
  `https://github.com/cisarik/kronika`.
- Capture provenance upstream is
  `https://github.com/cisarik/cli_chatgpt.git`, with the capture-time URL
  retained in `captured_as`.
- `ap.project.conf` `projectId` is `cisarik/kronika` because
  `ap project check` derives that identity from `remote.origin.url`.
- The implemented awk ledger entry was removed from the active ledger. Its
  historical evidence is the AP pin above.

Rendered read on 2026-10-02, after the NUC refresh: the shell title is
Kronika, the operator is signed in, cloud status is connected, Timeline shows
the two approved 2026-09-30 Search and Research cards, the Search record's
sandboxed answer source contains the stored answer, and Gallery reports an
empty catalog, consistent with the S9 reset.

The predecessor kept the internal `framenest` package, migration history,
HTTP header, and deployment identifiers. That limit is why S10 could close
while those names still exist. It is not permission to treat the rename as
finished.

## 2. Objective of this whole

On 2026-10-02 Michal stated the direction: the `framenest` identity does not
remain. The product name is Kronika, including NUC paths and script names.

That sentence supersedes the predecessor's "kept for now / no mass rename"
limit. It does not rewrite ADR-0082. The original wording stays historical.
This whole records the new decision in its own ADR or ADR amendment before
implementation, and it does not hide the cut inside an unrelated fix.

`kronika_capture`, the command `kronika-capture`, and the `kronika-capture-*`
systemd units are already on the Kronika side. Do not rename them again.

## 3. Identity inventory to re-verify

Copied from the checkout at `0c85099…` and one read-only NUC unit-file query
on 2026-10-02. This is a coverage statement, not proof that every occurrence
was enumerated. Re-verify before any grant.

Application and operator surface:

- Python package `src/framenest`, import name `framenest`, Poetry package
  `framenest`, `provenanceModule = framenest`.
- Console scripts: `framenest-server`, `framenest-db`, `framenest-catalog`,
  `framenest-library`, `framenest-dev`, `framenest-ai`,
  `framenest-production`, `framenest-backup`, `framenest-youtube`,
  `framenest-previews`, `framenest-covers`, `framenest-recovery`,
  `framenest-sidecar`, and the compatibility alias
  `framenest-chatgpt-page` (same target as `kronika-capture`).
- Settings prefix `FRAMENEST_` in `src/framenest/configuration.py`, plus
  command error codes with the `FRAMENEST_` prefix.
- Browser request header `X-FrameNest-Request` sent from
  `src/framenest/adapters/api/web/app.js` and required by route tests.
- User-visible "FrameNest" prose remains in places such as the YouTube claim
  copy. The shell title and wordmark are already Kronika.
- Operator entry `deploy/ubuntu/framenest-release` and
  `deploy/ubuntu/framenest_release.py`.
- SSH gate `scripts/operator/network/framenest_nuc_worker_gate.fish`.

Repository unit source, not the same thing as installed host units:

- `deploy/systemd/framenest.service`
- `framenest-catalog-backup.service` and `.timer`
- `framenest-catalog-offdevice.service` and `.timer`
- `framenest.env.example` and the `framenest-ai-credential-*.conf` /
  `framenest-research-credential.conf` templates

The service unit source binds the live contract:

- `User=framenest`, `Group=framenest`
- `WorkingDirectory=/opt/framenest/current`
- `EnvironmentFile=/etc/framenest/framenest.env`
- `ExecStartPre` and `ExecStart` call `framenest-production`
- `StateDirectory=framenest`, `CacheDirectory=framenest`,
  `RuntimeDirectory=framenest`
- The env template names `/var/lib/framenest/`, `/var/cache/framenest/`,
  and `/mnt/framenest-catalog-offdevice`

Installed unit files observed on the NUC, read-only, 2026-10-02:

- `framenest.service` enabled
- `framenest-catalog-backup.service` and `.timer` enabled
- `kronika-capture-bridge.service`, `kronika-capture-runner.service`,
  and `kronika-capture-xvfb.service` enabled
- `kronika-capture-view.service` and `kronika-capture-vnc.service` static
- The off-device catalog units were not in that installed list

Routine tooling paths already accepted for release updates:

- Poetry `/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry`
- CPython `/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13`

Do not rename those paths with a text substitution. A live cut is a
migration of a running service, its Unix account, its environment file, its
state directories, and its release helper together.

## 4. Boundaries this whole inherits

Keep:

- One repository, `cisarik/kronika`. No second product and no history rewrite.
- `cisarik/cli_chatgpt` active at `66c40d43…`.
- Loopback-first application, Tailscale-only remote ingress, no public
  listener and no router forwarding.
- Owner-private new records, administrator read of product records without
  provider secrets or host administration, household publication only by
  administrator approval. Internet publication stays off.
- Search and Research through the ADR-0083 / ADR-0084 provider boundary.
  Research disabled by default in code. The NUC's saved research settings
  are host state, not a reason to change the default.
- Gallery remains a separate view. The accepted Gallery and Details visual
  behavior stays frozen unless a concrete defect is identified.
- Parked rows stay parked: S3 host remainder, capture-mode Search and
  Research, S5 ZIP activation, S7-C. S7-P does not switch media analysis to
  the research provider.
- Alembic history already applied through `0035` on the NUC. Do not rewrite
  applied revision ids. A rename of living code may add a new migration. It
  does not edit old revisions in place.
- The AP pin above. An AP upgrade is a separate task.
- The release helper's same-schema rule. A host cut that changes schema,
  unit names, or the filesystem layout is not a routine `framenest-release`
  deploy.

Named residuals carried from S9-R, not authorization to fix them inside the
identity cut:

- L-1 cached-tokens-missing wording
- L-2 a disabled settings write may store an expired model while generation
  stays fail-closed
- L-3 dirty-draft discard confirmation is unimplemented and fail-safe under
  compare-and-set
- L-4 and L-9 through L-11, as recorded in the predecessor `00_notes.md`
  for 2026-09-30

Separate observation, not diagnosed: on 2026-10-02 the shell's media AI
indicator was unavailable because the last configured-provider test did not
reach the provider. Cloud was connected. No new provider call was made.
Do not fold a credential or provider repair into the rename.

## 5. Exact next step

Issue one Planner grant, native planning mode required, fresh Worker
session 01, exchange 01. Store it in this trace as `01_planning_00.md`.
The plan's useful outcome is a cut sequence that leaves the NUC serving
after each published step.

The plan must separate at least these cuts, and it must not collapse them
into one patch:

1. Living product language in the shell and operator docs, without renaming
   the package.
2. Python package, console scripts, header, and `FRAMENEST_` settings, with
   a compatibility window long enough for the installed environment file.
3. systemd unit names and the release-helper entry point in Git.
4. A separately authorized NUC migration for the Unix account, `/opt`,
   `/etc`, `/var/lib`, `/var/cache`, state directories, and the installed
   units. Writers stop first. Capture units are not restarted as a side
   effect. The catalog database, media, profiles, secrets, and backups are
   not deleted.

Until that plan is accepted, do not edit the package, do not publish, and
do not change the NUC.

## 6. First verification, read-only

1. Read `/Users/agile/Projects/framenest/AGENTS.md`, `ROADMAP.md`, ADR-0082,
   ADR-0083, and ADR-0084.
2. Read `.ap/AP.md` Orchestrator spine, `.ap/AP_ORCHESTRATOR.md`,
   `.ap/AP_WORKER.md`, and `/Users/agile/meta/README.md`.
3. Read this handout and this whole's `00_notes.md`.
4. Confirm public `main` and the local checkout are still
   `0c850996cd2ef17dae4112733fd17fdc732f4699`, and that the AP gitlink is
   still `73e20ef80b88700d5fcbc397cd8edd4fc425869f`.
5. Confirm `ap.project.conf` `projectId` is `cisarik/kronika`.
6. Treat section 3 as a lead, then re-count the live identity classes before
   writing the Planner grant.
7. Do not deploy, rename, or emit the predecessor closure signal.
