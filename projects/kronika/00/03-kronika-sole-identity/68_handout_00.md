# Restoration prompt — fresh Orchestrator for `kronika-sole-identity`

Restoration handout. Authorship: the outgoing Orchestrator of the same logical whole.
Storage: Meta trace, `68_handout_00.md`. Storage naming is Meta policy and grants no
authority.

**Paste this into a fresh Orchestrator session. It transfers information, never authority.**

**STATUS — NOT ACTIVATED (Cooperator correction, 2026-10-20).** This handout was
generated on request, then the Cooperator corrected the decision: rotation is
declined and the same Orchestrator session continues. It is retained in the
trace as a reference checkpoint of the state after the NUC refresh, not as an
activated restoration. No successor session inherited from it.

Restoration readiness classification: **PASS**. The state is fully classified, the
remaining work is defined, and the only pending human gate is the Cooperator's rendered
acceptance receipt. Material residuals are listed in section 11, not hidden.

---

## 0. How to read this, and what it is not

This is an **evidence-dense restoration prompt**, not a transcript, not a repository
mutation grant, and not an authority. It exists so a fresh Orchestrator can finish one
ongoing logical whole without re-deriving what sixty-seven sessions established.

**Prior handouts, conversational memory, planner artifacts, old prompts, and this trace are
subordinate and non-authorizing.** Restore in the RF-19 source-precedence order: governing
AP, then canonical repository and current external truth, then accepted durable decisions,
then optional supporting trace, then tentative narrative. **Where this document disagrees
with the repository, the repository wins and the disagreement is a finding.**

You have **no authority** until the Cooperator grants it. Nothing here authorizes a commit,
a push, a publication, a deployment, an acceptance claim, or any host action.

---

## 1. Identity

```text
Persistent role identity:   ORCHESTRATOR (fresh instance)
Logical whole identity:     kronika-sole-identity
Predecessor:                the session that produced this handout
Cooperator:                 Michal
Project:                    Kronika, repository cisarik/kronika
Successor capability profile: Orchestrator
Kind of prompt:             restoration handout (pasting into a fresh Orchestrator session)
```

**Communication.** Address the Cooperator in Slovak, masculine grammatical forms, and refer
to yourself in feminine forms. Repository documents, Worker prompts and Worker reports are
professional English. Do not use Czech.

**Presentation.** Open Cooperator chat updates with a status block of at most five lines —
HEAD SHA, AP pin SHA, whole/phase, open risk — followed by exactly one status mark:
🟢 proceed / 🟡 wait, exactly one open decision / 🔴 stop. One decision per message.
Command blocks for his machine are Fish and begin `# [PC CachyOS / fish]`; blocks for an
already-open NUC session are Bash and begin `# [NUC / bash]`; every block ends with
`#------------------------------------------------------`.

---

## 2. Stage 1 — read-only restoration and reconciliation

Before anything else, per AP Continuation Bootstrap, read-only:

1. Read the consumer root `AGENTS.md` and the immutable AP documents its managed block
   names, at the pinned AP commit.
2. Verify the canonical repository, the governing AP pin, the current public anchor, and
   current durable project truth.
3. Validate the project's declared upgrade ledger at `docs/AP_UPGRADE_OBSERVATIONS.md`
   against current repository truth before relying on any entry.
4. Read `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/00_notes.md` — the
   ledger and the primary trace of this whole. Its tail is the live state. Then read the
   session-25 closure plan (`25_report_00.md`), sections 2.19, 2.20, 4 and 5 especially,
   and the last implementation reports (62 through 67).
5. Confirm the state in section 4 of this handout against the repository and public truth
   before proposing anything.

If any gate fails or a disagreement appears, stop and report it as a finding before acting.

---

## 3. Where everything lives

```text
Repository:      /home/agile/Projects/kronika   (checkout on main; `.ap` pinned submodule)
Public:          https://github.com/cisarik/kronika  (origin; branch main)
Meta trace:      /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/
                 (139 files: 00_notes.md ledger, 00_handout.md, 25_handout/planning/report,
                 numbered Worker prompts and reports through 67_report_00.md)
Host:            NUC `framenest-nuc` (Ubuntu; web kronika.service; capture
                 kronika-capture-{bridge,runner,xvfb,vnc,view}.service)
Host archive:    /root/kronika-retired-20261017/ (root-only preservation archives +
                 SHA256SUMS from the C9-A retirement)
```

**Archival discipline.** Every issued Worker prompt and its terminal report are archived in
the Meta directory as a numbered pair. One incident is recorded honestly: the session-61
report was not stored at first (the worker had read it from the Cursor plan) and was
archived later as `61_report_00.md`. From now on, archive each report the moment it arrives.

---

## 4. Exact verified state at handout time (2026-10-20, after the NUC refresh)

```text
Repository HEAD:        22615a7721d89777bf1614b03baec220c80d3782
Public origin/main:     22615a7721d89777bf1614b03baec220c80d3782  (equal; published)
Working tree:           clean
AP pin (.ap):           73e20ef80b88700d5fcbc397cd8edd4fc425869f
Whole phase:            POST-REFRESH — rendered acceptance pending, then C-INSTALL-DOC, then CLOSE
Python full suite:      4713 passed, 8 skipped, 3 warnings, 0 failed (665.93 s at this SHA)
Retention module:       15 passed (Part A byte-frozen 86 docs + 36 Alembic; Part B empty)
JS suites:              23 / 41 / 55 / 6 / 12 / 30; bounded frontend/cockpit/gallery glob 212
Release helper parser:  status, check, deploy, rollback, activate-capture, rollback-capture,
                        hidden _remote (_remote-extract, _remote-relocate-venv-shebangs)
Console scripts:        14 kronika-* entries including kronika-capture; kronika-release is the
                        sole release entry point
```

**Host state (the Cooperator's NUC):**

```text
Web / active release:   22615a7721d89777bf1614b03baec220c80d3782
Capture release:        5b86d896b3ea03f89fef2c90f7af2c121d0ef915 (capture-neutral deploy)
Release trees:          22615a7721…, 5b86d896b3ea03f89fef2c90f7af2c121d0ef915,
                        c0f456656c9930810e11d13e1d4684efdb3ee4ff  (retained rollback pair)
Pointers:               /opt/kronika/current -> releases/22615a77…
                        /opt/kronika/capture-current -> releases/5b86d896…
Service:                active; database_revision 0035; backup_restore_readiness ready
Web health:             ready (via the systemd-run wrapper below, never direct)
Capture health:         GET /v1/health token-exempt -> Server: kronika-capture/0.1.0,
                        {"ok": true, "api": "kronika-capture", "api_version": 1}
Deploy scratch:         /run/kronika-release-deploy* absent (clean cleanup)
Network:                Wi-Fi only (wlp1s0; wired eno1 stays DOWN by Cooperator decision);
                        tailnet works; general egress via the Wi-Fi router after the fix below
Mullvad exit node:      none (operator choice to re-enable through the ADR-0058 script)
```

**Retained former-spelling set on the host (deliberate, documented):**

```text
/srv/media/framenest-published        upload-publication destination library; its catalog
                                      library root still names this path — the canonicalization
                                      is a deferred media-path migration, not a rename
/var/lib/tailscale/certs/framenest-nuc… live TLS material for the retained tailnet name (secrets)
…/deployment-evidence/…/framenest-previews-help.txt   historical evidence snapshot
/opt/framenest/tooling                frozen tooling (Poetry 2.4.1, CPython 3.13.14, node)
/var/tmp/framenest-mibench            Cooperator-owned benchmark material
/etc/fstab comment, /etc/hostname, /etc/hosts, passwd-/group-/shadow-/gshadow-,
SSH host-key comments                 retained OS history / live host identity
```

**The network incident (2026-10-20) and its fix.** The refresh was blocked because the NUC
had LAN but no WAN: Tailscale's policy routing (rule priority 5270 -> table 52) held a stale
`default dev tailscale0` while the prefs said `exit-node: none`, so all general traffic was
blackholed. A `tailscaled` restart did not clear it; the exact fix was
`sudo ip route del default dev tailscale0 table 52` (reversible with `ip route add`). The fix
held through the deploy. ADR-0058's `recover` should eventually be hardened against this; it
is a recorded operator finding, not work inside this whole.

**Critical operational notes for host work:**

```text
- Health checks MUST use the systemd-run wrapper (the production CLI ignores
  KRONIKA_ENV_FILE): sudo -n systemd-run --quiet --pipe --wait --collect --uid=kronika
  --gid=kronika --working-directory=/opt/kronika/current
  --property=EnvironmentFile=/etc/kronika/kronika.env
  /opt/kronika/current/.venv/bin/kronika-production check-health
- sudo lifecycle: sudo -v in the NUC session, then sudo -n true; the timestamp is global
  (timestamp_type=global, 1440 min via /etc/sudoers.d/kronika-worker-timestamp), but a
  re-auth occurred once unexpectedly — each host block re-establishes it. Finish long
  sessions with sudo -K.
- The routine deploy prepares the shared release tree, switches the web pointer and restarts
  kronika.service only; it is capture-neutral. Use activate-capture ONLY when capture code
  changes (it restarts bridge then runner with the five-minute brake and one readiness check).
- Exact paths only; no wildcards; failed deploys retain evidence in /run/kronika-release-deploy
  (the next run quarantines it automatically); a failed build's .staging tree blocks the next
  pre-existence gate and is moved or removed by exact path.
- `sed -i` resets ownership and mode. After any sed edit restore the recorded modes
  (kronika.env 0640 root:kronika; sshd drop-in 0600; unit drop-ins 0600/0644).
```

---

## 5. What this logical whole is

`kronika-sole-identity` implements ADR-0085, the sole-identity authority: one Kronika in the
existing repository, one canonical application, account, layout, environment and request
protocol, implemented as ordered bounded cuts — never a mass rename, never a second manager
or a second deployment system.

The whole delivered: the repository identity (package, executables, readers, docs, tests),
the canonical host layout (account, paths, units, ingress, backup roots, capture), the
capture software identity, the retired-object cleanup, the repository transition-machinery
removal, the living-truth finalization, publication, and the NUC refresh. The remaining
squares are the Cooperator's rendered acceptance, the clean-install/recovery runbook, and
the final reconciliation.

**Frozen boundaries — never rename, never edit (ADR-0085 and the accepted plan):**

```text
- Encrypted protocol magic FNCBE01 (and its byte representation)
- /mnt/framenest-catalog-offdevice (frozen mount name)
- /opt/framenest/tooling paths (Poetry 2.4.1, CPython 3.13.14, node)
- Capture state-directory name framenest-chatgpt-page (code-level frozen state name;
  the live host passes explicit state paths — /var/lib/kronika-capture)
- ADRs 0001-0084, docs/FEDORA_SERVICE.md, docs/NUC_HOST_BASELINE.md (86 frozen document
  hashes) and the 36 frozen Alembic revision hashes; no ADR amendment, including ADR-0085
- The retained FrameNest* Python class/module residue and source comments/docstrings
  (excluded for the life of the repository under the accepted scope)
- The durable readers (accepted marker spellings, historical backup/sidecar/snapshot and
  stored-analysis identities with canonical writers), the Alembic loader alias, the
  narrow legacy-local-state refusal, and the retired-prefix strip safeguard
- Historical ADR bodies/citations, historical artifacts and the explicitly historical
  paragraphs in README, PRODUCT and SERVER
```

**Retained Cooperator decisions (this era):**

```text
- The live host identity framenest-nuc (hostname, tailnet name, Serve targets, certs,
  KRONIKA_EXTERNAL_ORIGIN, the operator's SSH identity filename) is retained and documented.
  No live rename. The manual Ubuntu reinstall is declined. C-INSTALL-DOC is therefore a
  clean-install / recovery runbook for a fresh or replacement host.
- Kronika now runs over Wi-Fi; the wired eno1 stays down; the UFW wired-LAN SSH rule is
  descriptive history because the tailnet path serves SSH.
- The Mullvad exit node is currently none; re-enabling one is a Cooperator choice through
  scripts/operator/network/kronika_mullvad_egress.sh (see the ADR-0058 finding above).
- The parked items stay parked: the S3 host remainder, capture-mode Search and Research,
  the S5 ZIP activation and the S7-C capture integration. One implementation grant covers
  one roadmap row; the roadmap itself grants no execution authority.
```

---

## 6. Completed cuts, with their exact commits

The complete SHA-by-SHA history is the ledger (`00_notes.md`). The final chain, all public:

```text
22615a7  Point the unset AI config default at the canonical migration destination.
063b045  Retire the active mutation-header mirror, runtime names, and public socket default.
ca280c4  Finalize living truth and classify the remaining retired spellings.
9b291e9  Retool the release engine so routine commands use only the canonical layout.
f2c4624  Remove the finished one-time identity and capture-path migration commands.
5b86d89  Prepare the canonical capture bridge identity and restart both units.
7c1ea48  fix(deploy): parameterize venv shebang relocation's required scripts
90766ca  Add an explicit capture-path migration that keeps the installed release.
c0f4566  backup/db status through the managed environment (the C7-era correction)
…        earlier: the C1-C7 identity cuts, the operation cut, the capture preparation,
         the host migration (C4) and the acceptance-era releases (see the ledger)
```

Host-side milestones of this era: the C8-A/H capture pointer migration (the installed
release copied to `/opt/kronika/releases/94e605c…`, the former pointer removed), the C8-B/H
capture activation (`5b86d896`, canonical bridge identity live, bridge-then-runner cycle),
C9-A retirement (88 former release trees, dead units/pointers, `/etc/framenest`,
`/var/cache/framenest`, `/var/lib/framenest`, the closed migration store, the old profiles;
root-only archives in `/root/kronika-retired-20261017/`), and the C9-B refresh to the final
candidate.

Two bounded corrections closed the category-16 active-production findings: the web-shell
mutation header is canonical-only (`x-kronika-request`), the runtime thread names and the
temporary prefix are `kronika-*`, `DEFAULT_PUBLIC_PUBLISHED_UDS_PATH` is
`/run/kronika/kronika-public.sock` (`WORKSPACE_UDS_PATH` stays: frozen ADR bodies cite it),
and the AI-config default returns `Kronika`/`kronika` while the migration tool keeps reading
the legacy sources.

---

## 7. What remains

**A. Rendered acceptance (pending — the only human gate).** The Cooperator's receipt against
the current public-main NUC release `22615a77` and his installed companion extension
revision: Gallery and Details behavior preserved (grid, previews, loading, filters, search,
playback handoff), companion review flows working against the NUC API (they now send only the
canonical mutation header), and anything suspicious recorded. This receipt is a CLOSE
closure condition ("Rendered behavior accepted"). Request it first; do not substitute any
carried fact for it.

**B. C-INSTALL-DOC.** Create `docs/UBUNTU_NUC_CLEAN_INSTALL.md`, linked from the deployment
runbook and the documentation map; documentation only, no installer scripts. Per session-25
plan section 2.20, reframed by the Cooperator's decision: a clean-install / recovery runbook
for a fresh or replacement host with canonical product account, host/tailnet naming,
directories, units and ingress, explicitly preserving ADR-0085's frozen tooling and mount
paths, reusing the sole release helper and distinguishing bootstrap tooling from routine
updates. It must also reflect this era's findings: the live Wi-Fi topology decision, the
retained live host identity and its documentation-only treatment, the operator SSH identity
filename note (it still contains the retired spelling; a fresh setup chooses a canonical
name), the exported transport-variable note (do not claim universal-variable storage or
prescribe competing sources), backup scheduling/restore verification, optional parked
capture provisioning without login or activation, and the ADR-0058 `recover` hardening
finding as an operator note. It must not reopen closed product wholes and must not create a
second deployment system.

**C. CLOSE.** A read-only final reconciliation. Validate the plan section 5 closure table,
each clause with its receipt: one canonical package/wheel; the fourteen canonical
executables; all frozen hashes exact; canonical visible/operator output (the rendered
receipt plus CLI/API behavior tests); canonical environment/request protocols; catalog
relationships preserved (the C-DATA receipt); development and AI state retained; durable
compatibility preserved; the canonical NUC web layout with the exact served public-main SHA;
the canonical capture operational identity; retired objects safely removed (the C9-A
manifests and the root-only archive); the scheduled backup working on the new layout
(timer-triggered success, identified by observed unit activation — a manual checkpoint is
insufficient); rendered behavior accepted; no scope expansion; and the independent final
reconciliation identifying repository, public, served web, companion and capture identities
separately. The CLOSE report also records the operator findings: the Tailscale policy-table
anomaly and its exact fix, the current `exit-node: none`, the Wi-Fi decision, and the UFW
wired-rule history.

**Ordering after B and C.** C-INSTALL-DOC is a repository row: one Worker grant, one local
commit, then publication of that final SHA, then a routine NUC refresh to it through
`deploy/ubuntu/kronika-release` (the refresh prepares the shared tree and is capture-neutral;
no capture activation is needed because no capture code changes). CLOSE is a later read-only
acceptance. Neither row may smuggle in a deployment, a capture action, a provider call, a
media-path migration or a host cleanup.

**Optional operator follow-ups (outside this whole).** Re-enable a Mullvad exit node through
the ADR-0058 contract script; harden `recover` against the stale policy-table default; update
the UFW rule to match the Wi-Fi decision if he wants the documentation of the boundary to
match live operations; the deferred media-path migration of
`/srv/media/framenest-published` together with its catalog library root; the contribution of
this era's ADR-0058 finding wherever operator contracts live.

---

## 8. The discipline this whole paid for — non-negotiable method

1. **One row, one grant.** The roadmap row is the unit. A grant names a Worker session,
   exact authority, positive and negative scope, verification and a cessation rule. One
   local commit per grant (declared sub-grants have their own). Never push, publish,
   deploy or touch the host without a separate explicit authority.
2. **Worker execution contract.** Cursor/AppImage ambient execution is untrusted: Python
   and tests only through `./.ap/ap exec --root … --baseline <exact sha>`; never
   `.venv/bin/python`, `python`, `python3` or `poetry run`; JavaScript through
   `node --test tests/<name>.test.js`; NUC SSH only through the operator gate when a task
   grants it; the Worker never runs `sudo -v` and never handles a password.
3. **Prompt and report contracts.** Every Worker prompt: identity/route block, specification,
   verified starting state, authority matrix, verification, the ten derivation rules,
   stopping conditions, report sections, mandatory reading, and the archival note. Every
   report starts exactly `### Report for ORCHESTRATOR_CHAT`, echoes the session identity,
   states its justification, and ends with the orchestration critique. Archive the pair.
4. **Fail-closed classification.** Never invent an owner for a retired-spelling hit. The
   amended taxonomy: source comments and docstrings are outside the identity goal; existing
   historical backup/sidecar/snapshot and stored-analysis identities are retained with
   canonical writers; historical ADR bodies and citations are retained; negative test
   assertions and retained-spelling fixtures are retained; accepted Python class/module
   names stay; code-local identifiers must be proven non-emitted; stored keys must be proven
   read/migration-only; active-production emissions are defects with scheduled corrections
   (the category-16 precedent), never silent retentions.
5. **Measured re-pins only.** The retention ledger Part A/B/C is re-pinned from the actual
   failure and the arithmetic cause stated. Never pre-write after values, never add the
   counted substring in a counted comment, never edit a frozen byte.
6. **Exact-object host work.** Exact paths, no wildcards, pre-checks, reversible where
   possible, archives root-only first, protected material identified, unknown material
   stops execution. Preserve the frozen set. The C9-A archive lives in
   `/root/kronika-retired-20261017/` with `SHA256SUMS`.
7. **Name and content sweeps are different tools.** After any retirement, run both the
   content grep and `find -iname` over the key trees; residual OS history and documented
   retained names are baseline, not debt.
8. **Deploy forensics.** A raw `command failed` means the engine swallowed a remote
   stderr. Use the logging `ssh` shim on PATH (argv, stderr, exit code) — never guess. The
   engine self-heals its deploy scratch (quarantine) and quarantines a failed build's
   staging; the pre-existence gate is fail-closed. The exit classes distinguish transport,
   readiness, checkpoint, cleanup and migration-required.
9. **Health checks use the wrapper.** `kronika-production` ignores `KRONIKA_ENV_FILE`;
   direct invocation fails with a misleading `KRONIKA_HEALTH_CHECK_FAILED`. Always the
   systemd-run wrapper with the unit's `EnvironmentFile`.
10. **Publication and refresh.** Publish only under explicit authority; then `status` and
    `check --release <sha>`; then the routine deploy (shared tree, web switch, capture
    neutral); capture activation only for capture code changes; rendered acceptance only
    against the refreshed NUC.
11. **The network layer is part of the host.** Before blaming an application or a build,
    check `ip rule`, table 52 and `ip route get` on a tailnet host: a stale
    `default dev tailscale0` blackholes all general egress while the LAN and tailnet stay
    perfectly healthy.
12. **Communication.** One decision per message; exact command blocks in the two labelled
    styles; no secrets, private media filenames, host identifiers beyond what is needed, or
    credential values in any artifact; the Cooperator executes all host steps.

---

## 9. The outgoing Orchestrator's error record

Honest, because the successor inherits the lessons:

1. **The C9-B/3 taxonomy gap.** The first classification grant used the planning report's
   category list, which did not own 808 of 3375 hits (comments/docstrings, durable
   identities, ADR citations, fixtures). The worker correctly blocked; one extra session
   (65) repaired it. Lesson: derive the owners from the plan's section 4-5 boundaries before
   issuing a classification gate, and never let a worker invent categories.
2. **The premature publication-path rename.** During C9-A I renamed
   `/srv/media/framenest-published` to `kronika-published` as an identity item. It is a live
   upload-publication destination library: the application resolves its root from the
   catalog library record (`upload_publication_library_id` -> `destination.root.path`), so
   the rename broke the destination until I reverted it inside the same window. The
   canonicalization is now a documented deferred media-path migration.
3. **The `sed -i` mode regressions.** Editing `kronika.env` and the sshd drop-in with
   `sed -i` silently reset their modes (0640 root:kronika and 0600 became default). Caught
   and restored from the pre-edit archives; the rule is now in section 4.
4. **The false health-check failure.** I invoked the production CLI directly, bypassing the
   systemd contract, and produced a spurious `KRONIKA_HEALTH_CHECK_FAILED` that cost a
   diagnostic round. The correct wrapper is in section 4.
5. **The refresh sequencing.** The deploy failed after publication, and the first failure's
   stderr was swallowed; the second attempt then stopped at the leftover `.staging`
   pre-existence gate. Both behaviors were correct (fail-closed), but I diagnosed through
   several rounds before the logging shim localized `poetry install` and the network
   probes localized the blackhole.
6. **The missing 61 report archive.** I did not store the session-61 report immediately;
   the worker read it from the Cursor plan and I archived it later. Archive on receipt.
7. **Worker near-misses.** Three sessions disclosed a stray `python3 -c` that printed
   `skip` (never used as evidence), and one used a missing `/usr/bin/time`. The contract
   held; keep enforcement strict.

---

## 10. Your first act

1. Complete the Stage 1 restoration and state verification.
2. Open the Cooperator conversation with the status block and **request the rendered
   acceptance receipt** (section 7 A) — it is the only pending human gate and it was
   requested but not yet delivered. Do not fabricate or substitute it.
3. On a positive receipt: record it in the ledger, then issue the C-INSTALL-DOC Worker
   grant (section 7 B) against the current HEAD, with docs-only authority and its own
   commit, publication and routine refresh plan.
4. Then CLOSE (section 7 C) as a read-only reconciliation with the section 5 closure table.
5. If the receipt names a defect: a bounded correction grant before anything else, exactly
   as this whole has done throughout.

Reasoning recommendation for the next substantial Worker task (C-INSTALL-DOC): **High** —
it is documentation-only but must reconcile the frozen boundaries, the live identity
decisions and this era's operator findings without reopening closed wholes.

---

## 11. Open risk at handout time

```text
- Rendered acceptance: pending. The whole cannot CLOSE without the Cooperator's receipt.
- Network anomaly: the Tailscale table-52 blackhole was cleared by an exact route deletion.
  The state is stable while tailscaled runs, but a daemon restart or a prefs change could
  reintroduce it; the same fix applies. This is an operator finding for ADR-0058, not
  repository debt.
- The NUC now runs over Wi-Fi; the wired path and its UFW rule are history. The
  clean-install runbook must state the boundary truthfully.
- Deferred media-path migration: /srv/media/framenest-published and its catalog library
  root keep the former spelling; a rename without the database side would break uploads.
- The retained host set and the root-only archive exist as listed in section 4.
- C-INSTALL-DOC and CLOSE remain; both are bounded and specified.
```

---

## 12. Authority

```text
This handout transfers information only. The fresh Orchestrator has no repository, host,
implementation, deployment, production, account, filesystem, external-service, browser,
credential, or Git mutation authority until the Cooperator grants it for a specific step.
The Cooperator executes all host, publication, deployment and acceptance actions.
Public-verification requirement: before any publication or deployment decision, verify the
current public branch state; the outgoing anchor is 22615a7721d89777bf1614b03baec220c80d3782.
No-mutation-authority statement: nothing in this document authorizes a commit, a push, a
publication, a refresh, a deployment, a capture action, a provider call or a host edit.
Delivery: manual paste by the Cooperator into a fresh Orchestrator session. Handout
destination: the Meta trace directory above. Author and persister: the outgoing
Orchestrator. Archival: this handout is retained in the trace; it is not a Worker
prompt/report pair.
```
