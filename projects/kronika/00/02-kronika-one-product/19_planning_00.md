# Kronika one product — S3 profile-in-use startup failure: bounded recovery planning

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 19
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: KRONIKA-ONE-PRODUCT-S3-PROFILE-IN-USE-RECOVERY-PLAN
Delivery route: manual Cooperator delivery
Reasoning recommendation: Extra High — named risk: the accepted S3 recovery path has reached its single classified host diagnostic and produced a profile-in-use Chromium startup refusal whose lawful correction must be bounded across ProcessSingleton behavior, the unit sandbox, the never-logged-in profile, the profile-ownership rules and the spent launch budget without weakening any accepted boundary; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Planning contract

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: root-cause or bound the classified profile-in-use Chromium startup refusal and design the smallest lawful correction, its causal tests, acceptance/publication route and ordered host sequence
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1

Planning cycle: initial
Prior planning report: 15_report_00.md (accepted S3 recovery plan)
Targeted revision basis: none
Changed decision boundary: the classified profile-in-use launch failure (exit 21, ProcessSingleton wording) replaces the earlier unclassified missing-Chromium boundary
Preserved unaffected decisions: journal recovery via working browser + explicit null-job resume + matching fresh readiness (no journal reset, no SQL surgery, no state recreation); C1 bounded startup diagnostics; C2 fresh-identity activation readiness; activation work/brake/manifest gates; loopback/token/Host-Origin boundaries; sandbox directives; profile-ownership rules; the one-diagnostic-spawn budget already spent; publication and deployment separation
Automatic targeted revisions used: 0
```

Planning authority expires at the terminal planning report. This grant does
not authorize implementation, repository mutation, acceptance, publication,
deployment, host contact or closure.

## Fresh-session opening

This is a genuinely fresh Worker session; inherit no prior authority.
Independently establish the repository evidence named below before reasoning.
Repository reading is read-only. The only write this grant allows is the
terminal report at its exact destination when absent. No subagents.

## Verified starting state (read-only, 2026-09-25)

- FrameNest checkout `/home/agile/Projects/framenest`; branch
  `feat/kronika-one-product`; HEAD
  `e408bb5503f359ec24542304ac1a621c6b9e4ffb` (parent
  `d63d0b725acedf49d1611224c3b5201a90e7ef90`, tree
  `dadc01726a354c319374832bfd385be0bdffb516`); clean; local `main` =
  `origin/main` = public `refs/heads/main` = that commit; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (gitlink and `.ap` HEAD).
- Host state after the D3 cleanup (prior classified evidence; Orchestrator
  cannot reach the host itself): runner `inactive`; Xvfb and bridge `active`;
  web pointer `/opt/framenest/current` = `e408bb5…`; capture pointer
  `/opt/framenest/capture-current` = `94e605c…`; no Chromium process; no
  recovery override present; external brake metadata
  `/var/lib/kronika-capture/profile.capture-launch/` directory present,
  `lock` absent, `last-start.json` valid, remaining interval 0 ms.
- Exactly one C1 startup record from the single diagnostic start (verbatim,
  journal of `kronika-capture-runner.service`):

```text
[headless] capture_startup {"outcome":"failed","code":"E_BROWSER_UNAVAILABLE","stage":"endpoint","reason":"process_exited","spawn_errno":null,"exit_code":21,"signal":null,"endpoint_seen":false,"endpoint_budget_exhausted":false,"stderr_classification":"profile_in_use","cleanup_failed":false}
```

- The start used one temporary `ExecStart` override pinned to the `e408bb5`
  release tree under the real unit account, credentials, display, mount
  restrictions and sandbox. The override has been removed.
- `private/**` is never read. Never print or read the token value. Agents
  must not inspect the browser profile contents or its internal locks.

## What is already established

1. The child Chromium process started (spawn succeeded, no errno) and exited
   with code 21 before any DevTools endpoint appeared.
2. The bounded stderr classifier mapped its failure wording to
   `profile_in_use`. Read `driver.mjs` at this baseline: the class covers two
   distinct wordings — `The profile appears to be in use by another … process`
   and `Failed to create a ProcessSingleton for your profile directory`. The
   single class therefore conflates "another instance holds the profile" with
   "the singleton could not be created at all". Distinguishing them is part of
   this planning question.
3. No Chromium process exists, so the refusal is not observed contention by a
   live capture browser.
4. The profile `/var/lib/kronika-capture/profile` has never been logged in
   (S3 login was never reached); earlier failed runner starts may have left
   process-singleton artifacts in it.
5. The external launch brake is not the cause: the lock was absent and the
   interval expired.
6. The accepted C3 correction (`TMPDIR`) is not selected: its trigger is a
   proven temporary-storage failure, and this classification is not that.
7. The single diagnostic browser spawn allowed by the accepted plan is spent.
8. The unit runs `NoNewPrivileges=true`, `ProtectSystem=strict`,
   `ReadWritePaths=/var/lib/kronika-capture /run/kronika-capture
   /tmp/.X11-unix`; the host has `kernel.apparmor_restrict_unprivileged_userns`
   = 1 with the distro AppArmor userns profile present;
   `/usr/bin/chromium` resolves to Chrome for Testing 154.0.8037.57 under
   `/opt/framenest/tooling/`.

## The planning question

Given the evidence above, produce a decision-complete plan that:

1. **Bounds the cause.** Enumerate the candidate causes (for example: stale
   process-singleton artifacts with a live-PID collision or cross-hostname
   lock; inability to create the singleton socket/symlink under the service
   account, filesystem or sandbox; an invocation/path difference; a Chromium
   behavior specific to this binary/version). For each, state what current
   evidence supports or refutes it and what remains unknown. Do not assert a
   cause the evidence does not establish.
2. **Defines the smallest discriminating evidence.** Specify the exact
   bounded, read-only or synthetic probes that would decide between the live
   candidates, with: exact commands, execution owner (Worker through
   `scripts/operator/network/framenest_nuc_worker_gate.fish` versus a
   Cooperator-executed `# [NUC / bash]` block), allowed targets, expected
   interpretation, fail-closed preconditions, cleanup of any temporary probe
   state, and stop conditions. Respect these hard boundaries: never inspect
   or print browser profile contents; never read, remove or test
   profile-internal locks; never use raw Chromium stderr passthrough; never
   add `--no-sandbox`; never disable AppArmor/user namespaces; never touch
   the token, account, journal or release pointers. This planning grant
   itself authorizes no host contact; probes are proposed, not executed.
3. **Designs the smallest lawful correction per cause class.** For each
   candidate cause that survives, specify: exact files and changes (code,
   unit, documentation), causal tests in the existing suites, why they close
   the evidence gap, the acceptance class (runtime behavior changes are
   full-fresh independent acceptance), the publication route through the
   canonical helper and a separate publication grant, the deployment route
   through `deploy/ubuntu/framenest-release`, the exact ordered host sequence
   with its single corrected browser start if any, rollback, and stop
   conditions. Name what remains Cooperator-owned: profile decisions,
   login/challenges, opaque profile backup/restore, and the view.
4. **Handles the profile-ownership boundary honestly.** If the cause cannot
   be decided without a Cooperator-owned profile operation, state that
   explicitly and present the exact decision options with their consequences,
   including the option of a fresh profile (the current one has never been
   logged in) and the option of a Cooperator-executed opaque profile
   operation with the browser stopped. Do not propose any agent action
   against profile contents or internal locks.
5. **Preserves every accepted boundary.** No journal reset, SQL surgery or
   state-directory recreation; no sandbox weakening; no `--no-sandbox`; no
   stealth; no model/reasoning changes; no automatic restart loop; no
   weakening of loopback/token/Host/Origin checks; no change to C1's bounded
   diagnostics except a strictly bounded, allowlisted refinement if the plan
   proves it necessary; no second browser spawn outside a separately accepted
   correction with its own explicit budget.
6. **Recommends exactly one next bounded grant** for the Orchestrator to
   issue after accepting the plan, in the project's grant shape: identity and
   route, exact baseline and allowlist, positive and negative authority,
   declared route (`./.ap/ap project check` / `./.ap/ap exec`, `node --test`),
   staging and commit rules, stop conditions, report contract, trace and
   delivery record. If the plan concludes that a Cooperator decision must
   come first, say so and make the recommendation the decision request, not a
   mutation grant.
7. **States its own limits.** No claim that synthetic tests establish host
   Chromium startup; no claim of S3 completion; exact unknowns preserved.

## Mandatory reading

- Governing WORKER spine, `RF-19`, and the AP validation and stopping owners.
- `15_report_00.md` (accepted S3 recovery plan; §2 process-singleton context,
  §3 corrections, §5 diagnostic table, §6 host completion, §7 closeout).
- `18_report_00.md` (deploy + D1 classification) and `10_report_05.md`
  (earlier silent startup failure on the same host path).
- `01_plan_sk.md` §4 "Browser a zásah administrátora" and "Prevádzka a
  profil" (one persistent browser, manual restarts, profile ownership).
- `01_report_00.md` §8 S3 and §10 security boundary checklist.
- `AGENTS.md` security boundaries (profile, credentials, loopback, token)
  and the Cursor Worker execution boundary.
- `src/kronika_capture/_assets/extension/src/headless/driver.mjs` (startup
  path, `safeStartupDiagnostic`, `classifyStartupStderr`, `chromiumLaunchArgs`,
  LaunchBrake, spawn/endpoint/cleanup), `runner.mjs` (startup record and
  unavailable loop), `deploy/systemd/kronika-capture-runner.service`,
  `deploy/ubuntu/framenest_release.py` (capture activation), and
  `docs/UBUNTU_NUC_DEPLOYMENT.md`.
- Existing causal tests in `tests/capture_lifecycle.test.js`,
  `tests/contract/test_kronika_capture_services.py`,
  `tests/unit/chatgpt_page/test_capture_journal.py`.

Citation rule: every material claim cites its exact source location at the
baseline; line numbers are locators. Treat all host values above as
Orchestrator-relayed classified evidence, not as your own observation.

## Authority and containment

Positive authority: read-only inspection of the named repository files and
the trace reports; the terminal report write at the exact destination below
when absent; a full readback of the saved report.

Negative authority: no repository mutation (no edit, stage, commit, push); no
test, build, interpreter or package-manager execution; no host, SSH, gate,
service, account, privilege, browser, journal or credential action; no
`private/**`; no profile contents or profile-internal locks; no subagents; no
network use; no second planning cycle. Do not print hostnames, private
network values, tokens or sockets.

## Completion and report contract

Status: `PASS` means the plan is decision-complete for the current evidence;
`PARTIAL` when a material cause or decision remains genuinely open and stated
as such; `BLOCKED` when the planning question cannot be answered inside the
boundaries. Use `Phase-qualified result: not-applicable` and
`Logical-whole closure: not-closed`. `Report justification: new-evidence`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the cause
analysis with evidence; the discriminating probes; the correction options;
the Cooperator-owned decisions; the recommended single next grant; deviations
and missing evidence; authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

The formal report is in English; a short completion notice to the Cooperator
is in Slovak, masculine address. Finalize the report, save it at the exact
destination, read it back in full, verify its first line, coordinates,
content and path, then send the separate short completion notice with status,
path and SHA-256. Terminal report or cancellation expires this authority.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 19_planning_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 19_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
