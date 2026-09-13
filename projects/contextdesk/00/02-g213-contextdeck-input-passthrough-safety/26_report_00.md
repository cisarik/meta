### Report for ORCHESTRATOR_CHAT

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 26
Worker exchange ordinal: 01
```

- **status:** **PASS**
- **phase-qualified result:** **implementation-PASS**
- **Report justification:** `new-mutation`
- **Logical-whole closure:** not-closed
- **Start commit:** `ab10491c49d0b6574b6953a02935a4664c39d7c2`
- **End commit:** `ca6052e816d4884ddeac9d7499a42c2aca089e7e`
- **AP pin:** `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`
- **Public META:** `53a0c26e098599932498c017fe4525d92d9ccd61`
- **Handoff:** `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/00_handout_02.md`
- **Finding identity:** `G3-ACL-REPROBE-01`
- **Authority:** expires at this terminal report

This session received the complete Worker prompt as file-based delivery. Worker 25 authority was already expired. No subagents. Speak-to-Cooperator language is Slovak; this report is English. The correction is source/test/docs plus one public product commit. It is non-independent. Host deployment and independent G3 re-audit remain outstanding. This report does not claim the target host is fixed, G3 is accepted, or the finding is verified-closed.

```text
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Security Correction Worker — stabilize G3 ACL revocation
Phase: implementation
Task identity: CONTEXTDESK-G3-ACL-REPROBE-CORRECTION
Delivery: file-based; no Cooperator copy-paste
Evidence tier: E3
Activated stricter profile: INFOSEC.md
Security route: R6 correction followed by a fresh independent re-audit
Acceptance independence: required-separate-fresh-worker
```

## Model / client / reasoning (requested vs observed)

| Fact | Classification |
|------|----------------|
| Requested model | Cooperator choice |
| Observed client/model label | Cursor Grok 4.6 (session communication identity; not independently attested by a provider API dump) |
| Requested reasoning | High |
| Observed reasoning mode | unknown |
| Requested context | approximately 128k tokens |
| Observed context capacity | unknown |
| Delivery | file-based |
| Subagents / Task dispatch | none |

## Finding, threat model, and evidence

Finding ID: G3-ACL-REPROBE-01
Title: session POSIX ACL can remain or return after udev re-probe
Status: corrected (source only; not verified-closed)
Severity: high
Confidence: high for the source weakness; host closure not in scope
Evidence class: reproduced-dynamic (Session 25 on the authorized target host); established-static (this session, rule text)
Security property: confidentiality of G213 input event nodes; session user must not gain raw I/O on `/dev/port` or `/dev/i2c-*`
Asset at risk: G213 input event nodes; `/dev/port`; `/dev/i2c-*`
Trust boundary: distribution OpenRGB udev rules and systemd-logind uaccess processing; ContextDesk udev guard/grant; kernel device-node ACL state after add/change/re-probe
Local-actor assumption: any ordinary process running as the graphical session user
Reachability: packaged OpenRGB lighting rules plus a later udev add/change re-probe; broker not required
Preconditions: ContextDesk tag-guard files present or restored; seat uaccess builtin still able to materialize a session ACL; hidraw lighting ACL intended to remain
Required privileges: ordinary session user after the ACL exists
Observed impact (Session 25, not re-run here): after remove and immediate rollback, documented udev triggers did not stably revoke the session-user ACL; delayed re-probe left session-user ACLs on G213 event nodes, `/dev/port`, and `/dev/i2c-*` while hidraw lighting ACL remained
C/I/A effect: confidentiality of keystrokes and raw I/O/SMBus nodes; integrity/availability of lighting and uinput session access must be preserved
CWE mapping: CWE-732 (MITRE CWE corpus; taxonomy; registry retrieval 2026-07-19)
ASVS mapping: none
Exploitability conclusion: demonstrated on the authorized host in Session 25 (`reproduced-dynamic`); this Worker did not repeat host reproduction
Acceptance-blocking decision: blocking for G3 until a fresh independent re-audit after deployment
Redaction: no host identity, addresses, node numbers, serials, raw ACL dumps, UIDs/GIDs, or private paths

```text
Assets: G213 event-node confidentiality; /dev/port and /dev/i2c-* closed to the session user; hidraw RGB session access retained; /dev/uinput session ACL retained; broker uinput ACL retained
Trust boundaries: OpenRGB udev rules; logind seat uaccess builtin; ContextDesk 61-/62-/99-uinput rules; kernel POSIX ACL on device nodes
Attacker-controlled inputs: none remote; local-actor is the ordinary graphical session user
Security properties: no session ACL on guarded raw input/I/O nodes after add/change; no OWNER/GROUP/MODE rewrite; no hidraw or uinput strip
Abuse cases: session-user keylogging via leftover event-node ACL; raw port/SMBus access via leftover ACL after lighting re-probe
```

This is not a general OpenRGB vulnerability claim. Session 25 was PARTIAL / deployment-PARTIAL: remove and immediate rollback passed; candidate installation was not performed; G3 is not secure; the checkpoint remains; the broker was never started. That report is not G3 closure.

## Repository and AP gate

Canonical product remote `https://github.com/cisarik/contextdesk.git`, branch `main`. Required baseline `ab10491c49d0b6574b6953a02935a4664c39d7c2` matched local `HEAD` and `origin/main` before mutation. Worktree clean. No Git locks or active operations. `.ap` gitlink and checkout `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`. `./.ap/ap doctor`: PASS. Existing three udev files, `tests/unit/test_udev_policy.cpp`, and the G3 documentation sections were read from that baseline.

Public META remote `https://github.com/cisarik/meta.git`. `origin/main` = `53a0c26e098599932498c017fe4525d92d9ccd61`, a descendant of `5077bd92c65749a33fd537a14dda8ed777bb46f3`. Public changed paths for that Session 25 commit are the Session 25 pair. Public `origin/main` also contains the Session 24 pair and `00_handout_02.md`. Session 25 report classification used as required: PARTIAL / deployment-PARTIAL. Trace directory and all parents are real directories, not symlinks.

Prompt persistence: destination `26_implementation_00.md` already existed as a regular non-symlink file (18341 bytes, SHA-256 `e2dbf969a702b55b13ae47fdd6eb0c825927ec365bcbbdd4662325fcfeb3aa43`). Exact received bytes were written back and matched on complete readback. `26_report_00.md` was absent before this write.

No host mutation was authorized or performed.

## Design

New late rule `packaging/udev/99-contextdeck-input-acl-guard.rules`:

- filename sorts after `73-seat-late.rules`;
- `ACTION=="add|change"` on all three classes;
- G213 event nodes: USB ancestry `046d:c336` plus `KERNEL=="event*"` and `SUBSYSTEM=="input"`;
- `/dev/port` and `/dev/i2c-*` with the same kernel matchers as the existing tag guard;
- `RUN+="/usr/bin/setfacl -b %N"` only.

`%N` (`$devnode`) is used instead of the prompt's `/dev/%k` example because `%k` on `event*` is the kernel name, which would target a non-event path. `%N` is the device node path for event, port, and i2c nodes. `setfacl -b` removes extended ACL entries and preserves base owner, group, and mode. No `OWNER`, `GROUP`, `MODE`, session username, or UID.

Negative/preservation properties encoded in static tests:

- no hidraw matcher;
- no `/dev/uinput` matcher;
- existing `99-contextdeck-broker-uinput.rules` remains additive `setfacl -m` and is not changed;
- existing `61-` tag guard and `62-` event grant are unchanged.

The two `99-` files do not share matchers, so the ACL strip cannot remove the broker or session ACL on uinput, and cannot remove hidraw lighting ACLs.

## Changed paths

Exactly the allowlist, in commit `ca6052e816d4884ddeac9d7499a42c2aca089e7e`:

- `packaging/udev/99-contextdeck-input-acl-guard.rules` (new)
- `tests/unit/test_udev_policy.cpp`
- `CMakeLists.txt`
- `docs/operations.md`
- `docs/testing-m2.md`
- `docs/architecture.md`

Unchanged: `packaging/udev/61-contextdeck-input-guard.rules`, `packaging/udev/62-contextdeck-broker.rules`, `packaging/udev/99-contextdeck-broker-uinput.rules`. No other product path changed. AP gitlink unchanged.

## Validation

1. Static source/diff review: allowlist exact; no overlap with the uinput rule; no base OWNER/GROUP/MODE assignment; comments distinguish tags from POSIX ACLs; no private host data in the diff.
2. `udevadm verify --resolve-names=never` on all four candidate rule files: Success 4 / Fail 0.
3. Ambient `/usr/bin/cmake --version` classified as poisoned `CMAKE_ROOT`. Documented sanitized `PATH=/usr/bin:/bin:/usr/sbin` configure: `SANITIZED_CMAKE_RC=0`. `cmake --build build`: `BUILD_RC=0` (relinked `test_udev_policy` only).
4. Full CTest once: **15/15 PASS**, `CTEST_RC=0`. Not rerun.
5. Focused `./build/test_udev_policy`: `FOCUSED_POLICY_RC=0`.
6. Shell syntax: no allowlisted script was touched; `sh -n` not applicable.
7. Final product worktree after commit: clean; only the reviewed files are in `ca6052e`.

No live `udevadm trigger`, `udevadm test`, `setfacl` on live devices, sysusers, daemon-reload, broker start/stop, ARM, grab, OpenRGB, or input-remapper change occurred.

## Product Git publication

Exactly one normal commit on `main`, parent = required baseline `ab10491c49d0b6574b6953a02935a4664c39d7c2`. Non-force push to canonical `origin/main`. Public equality: local `HEAD` = `origin/main` = `ls-remote origin refs/heads/main` = `ca6052e816d4884ddeac9d7499a42c2aca089e7e`. Public changed paths match the allowlist. AP pin unchanged.

META was not committed or pushed.

## Host and residual risk

No host file, udev database, identity, or service was mutated. The target host therefore still has the Session 25 G3 hole until a separately authorized deployment and readback. Passing tests do not make the current host secure. Independent deployment and a fresh security re-audit of G3 after deployment are missing evidence. The corrector does not self-certify.

Containment ledger: none (no temporary audit roots; no live-device opens).

```text
Finding ID: G3-ACL-REPROBE-01
Decision: correction-required (source correction published; host residual remains)
Severity: high
Approver: not accepted as residual; re-audit required after deployment
Regression test: tests/unit/test_udev_policy.cpp and test_udev_verify (static scope/order/ACL operation only)
Rationale: source correction is not host evidence
```

## Git actions

Product: fetch for public baseline/equality; add of allowlisted paths only; one commit; one non-force push. No reset/clean/stash/switch/rebase. AP: none. META: prompt identity-verified; this report file prepared; no META add/commit/push.

## Missing evidence

- Host install of `ca6052e` udev files.
- Privileged reload/trigger/readback of G3 ACL state.
- Fresh independent re-audit verdict `verified-closed` or `not accepted`.
- Candidate broker install, live G4, autostart, suspend, and input-remapper coexistence (out of scope).

Logical-whole closure: not-closed

## Smallest next step

Authorize a separate fresh Worker to deploy `ca6052e` udev files on the target host and perform an independent G3 ACL readback/re-audit. Do not start the broker, ARM, or grab under that grant unless a later prompt names it.

## Orchestration critique

```text
Orchestration critique:
MEASURED: source correction published as ca6052e with 15/15 CTest and udev Success 4/Fail 0; host G3 remains open. Evidence: public origin/main equality; Session 25 deployment-PARTIAL still describes the live host. Effect: implementation-PASS, not G3 closure. Smallest correction: do not treat this commit as host recovery.
LEAD: none
```

## Near-miss / pre-existing

```text
Resolved Execution Issues / Near-Misses: (1) ambient CMAKE_ROOT missing; classified, then documented sanitized PATH configure used. (2) prompt example /dev/%k is wrong for event* nodes; %N used and justified; tests forbid /dev/%k. (3) after the required focused binary run, an extra ctest -R test_udev_policy was executed; it also passed; it was not a full-suite rerun to force a result.
Pre-Existing Failure Classification: Session 25 left G3 insecure after remove/rollback; this Worker did not touch the host. Product documentation previously treated tag removal as closing the hole; that claim is updated. Inactive WatchdogUSec vs WatchdogSec and OpenRGB userspace presence remain out of this allowlist.
```

```text
Cooperator delivery / trace destination: configured
Delivery mode: file-based; no Cooperator copy-paste
Downloadable prompt filename: 26_implementation_00.md
Destination path: projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: this WORKER
Report filename: 26_report_00.md
Report persistence owner: this WORKER
Product Git publication owner: this WORKER
META Git publication owner: COOPERATOR
Archival: wait-for-report
```

Logical-whole closure: not-closed

Authority for this Worker expires at this report.
