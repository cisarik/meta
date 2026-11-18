### Report for ORCHESTRATOR_CHAT

Logical whole identity: nuc-security-hardening  
Worker session ordinal: 03  
Worker exchange ordinal: 01  
Task identity: NSH-REVIEW-05  
Status: PARTIAL  
Phase-qualified result: not-applicable  
Logical-whole closure: not-closed  
Report justification: new-evidence

Independence declaration: I did not participate in this implementation, have no session 02 context, and am a fresh independent Worker session.

Start and end commit: `8cbbcad947964d711ebc2001e1c80976c4f82e24`. I made no source changes, Git writes, publication, deployment, or host contact.

**Verdict**

Acceptance is incomplete. The focused suite passed, but the required local `systemd-analyze verify` returned exit code 1. Following the prompt’s environment stopping condition, I stopped substantive review. This establishes an evidence limitation, not a candidate security defect.

**Candidate identity and boundaries**

Observed:

- Clean `main`, one commit ahead of `origin/main`.
- Candidate `8cbbcad…`, immediately following `8c58a81…` in Git history.
- Exactly the prescribed 18 changed paths: 1089 insertions, 7 deletions.
- AP gitlink and checkout both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`.
- Direct read-only public-ref verification returned:

```text
8c58a81234a97fdf5af9d724a3b526f19745d32a	refs/heads/main
```

**Fixed claims**

| Claim | Result | Evidence and limits |
|---|---|---|
| C1 | Verified for observed state | Candidate, clean branch, one-commit history, exact allowlist/stat, AP pin and public ref matched. Historical absence of any earlier push is not independently provable from these observations. |
| C2 | Partially verified | Read the complete candidate web unit; all 12 selected additions are present, with no excluded directive or publication write path. Exact preservation of every parent line was not completed before stopping. |
| C3 | Partially verified | Read the complete backup unit; selected common directives, `AF_UNIX`, `IPAddressDeny=any`, and `InaccessiblePaths=/srv/media` are present. Exact parent-line preservation remains unfinished. |
| C4 | Verified at committed-path level | The exact changed-path inventory excludes capture/off-device units, release helpers, credential templates, dependencies, AP, ADRs, migrations and frozen documents. |
| C5 | Partially verified | Read all 253 helper lines and its behavioral tests. Static review supports fixed surfaces, private state, validation, locking and staged restoration. Full acceptance was interrupted. |
| C6 | Verified within focused execution | All six focused modules passed. Helper parameterization accounts for 54 cases. Foreign-owner metadata and copy failures are explicitly labelled synthetic fixtures. |
| C7 | Partially verified | Retention diff changes only the stated Part C pins; retention tests passed. Independent arithmetic/count regeneration was not performed. |
| C8 | Partially verified | Reviewed changed documentation and the complete new hardening contract. They distinguish source evidence from host acceptance and retain deferred risks. Mandatory contextual reading remained incomplete. |
| C9 | Partially verified | Reproduced focused **151 passed**. This includes helper 54 and retention 15 cases. Full Python **4822/8/3/0** was not reproduced. No JavaScript path changed. |
| C10 | Partially verified | Committed effects stay within the allowlist. This review performed no NUC contact or host mutation. Prior implementer host activity was not independently inspected. |

**Validation evidence**

| Check | Result |
|---|---|
| Baseline-bound `ap project check` | PASS |
| Baseline-bound `runtime-info` | PASS; CPython 3.13.9, import from candidate checkout’s `src/kronika` |
| Six focused modules, `-q -p no:cacheprovider` | **151 passed in 5.84s** |
| `bash -n` helper | PASS |
| Local systemd version | **262.1-1-arch**, distinct from target Ubuntu systemd 255 |
| Local `systemd-analyze verify` | **Exit 1**, diagnostics below |
| Full Python suite | Not run after stopping condition |
| Independent retention counts | Not run after stopping condition |

The unrestricted local parser check reported exactly:

```text
kronika.service: Command /opt/kronika/current/.venv/bin/kronika-production is not executable: No such file or directory
kronika.service: Command /opt/kronika/current/.venv/bin/kronika-production is not executable: No such file or directory
kronika-catalog-backup.service: Command /opt/kronika/current/.venv/bin/kronika-backup is not executable: No such file or directory
```

No unknown-directive diagnostic appeared. This is limited local parser evidence; it is neither a zero-exit verification nor effective Ubuntu-host sandbox evidence.

**Helper security review**

Threat model:

- Assets: UFW/SSH configuration integrity and private recovery bytes.
- Trust boundaries: operator arguments/environment, live configuration paths, saved manifests and restore destinations.
- Attacker-controlled inputs: malformed state, unsafe filesystem objects, metadata and test-root values.
- Security properties: fixed paths, refusal before unsafe restoration, exact bytes/metadata, serialized operations and bounded errors.
- Abuse cases: path substitution, symlink/hardlink use, snapshot corruption, conflicting staging/state and concurrent operations.

Static observations:

- Arguments select only two operations dimensions and four literal surface paths.
- Manifest parsing uses no `source` or `eval`; canonical-byte and checksum checks precede restoration.
- All destinations are preflighted before staging; replacement is atomic per present file.
- No wildcard deletion, recursive permission change, service action or network operation appears.
- The test override prefixes all state/surfaces beneath a validated private root. Installed rollback requires a clean root environment without that override.
- No blocking helper defect was established before stopping.

Residual classification, without granting acceptance:

| Residual | Classification |
|---|---|
| Privileged pathname races | Acceptable residual for the stated trusted-root, serialized-writer model; hostile-root resistance is unproven. |
| Partial multi-file restoration | Acceptable residual with explicit nontransactional recovery handling. |
| Transient timer loss on reboot | Acceptable residual only with the documented prohibition on reboot during a dependent cut. |
| Publication write exception | Acceptable deferred residual for this bounded source slice; effective host acceptance remains separate. |

These classifications do not constitute risk-owner sign-off.

**Retention arithmetic**

The candidate proposes:

| Measurement | Parent pin | Candidate pin |
|---|---:|---:|
| Docs content files | 85 | 86 |
| Docs occurrences | 752 | 753 |
| Capitalized occurrences | 2320 | 2321 |
| Capitalized files | 340 | 341 |

The sole added content-path member is `docs/NUC_SECURITY_HARDENING.md`, containing the historical “FrameNest host baseline” link label. Part A and Part B are unchanged in the inspected diff; retention tests passed. The table above records inspected pins, **not independently regenerated counts**.

**Finding**

Finding ID: NSH-REVIEW-05-F01  
Severity: blocking  
Claim or surface: Required local unit-verification evidence.  
Evidence: `systemd-analyze verify` returned exit 1 because both NUC executable paths are absent locally; local systemd is 262, not target 255.  
Effect: The required control did not pass. The prompt’s environment stopping condition prevented completing the full suite, independent retention measurements and remaining review. No candidate vulnerability is demonstrated.  
Smallest correction: The Orchestrator should explicitly resolve how the documented missing-executable diagnostics satisfy—or fail—the local parser gate, then authorize completion of the outstanding checks. No candidate correction was applied.

**Execution issues and limitations**

Resolved Execution Issues / Near-Misses: Sandbox DNS initially blocked `git ls-remote`; an approved network-enabled invocation succeeded. Sandbox socket restrictions initially blocked systemd analysis; an approved unrestricted invocation exposed the missing-executable diagnostics above.

Pre-Existing Failure Classification: No Python failure observed. The systemd result is an environment limitation, not an established candidate regression.

Some combined reading output was truncated. Complete helper, new hardening document and helper tests were subsequently obtained separately; I do not claim complete mandatory reading or complete audit coverage.

Containment: Behavioral tests used pytest-owned synthetic `tmp_path` fixtures. Cleanup/retention belongs to pytest; exact temporary paths and cleanup outcomes were not independently recorded. No separate audit fixtures were created manually.

**Smallest next step**

Reconcile the local systemd gate’s expected outcome, then issue bounded authority to finish the uncompleted acceptance controls. Publication, deployment and logical-whole closure remain outside this review.

Orchestration critique:  
MEASURED: The prompt anticipates absent-NUC-executable parser diagnostics but also requires stopping when a required local check cannot be supported. The observed exit 1 makes that acceptance disposition ambiguous; state its exact expected treatment.  
LEAD: None.

This terminal report expires my current Worker authority.