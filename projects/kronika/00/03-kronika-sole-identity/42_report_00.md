### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity  
Worker session ordinal: 42  
Worker exchange ordinal: 01  
Task identity: KSI-CORR-C6COMP  
Worker session profile: Bounded Correction Worker  
Persistent role identity: WORKER  
Native planning mode: not-used  
Status: PASS  
Phase-qualified result: not-applicable  
Logical-whole closure: not-closed  
Report justification: new-mutation  

Start commit: `fcde631047650d1ff0a84b84bf185b54d6d11ba5`  
End commit: `e9413dff98605443e7d17557f498c87433c93e92`  
Branch: `main`  
AP pin and submodule HEAD: `73e20ef80b88700d5fcbc397cd8edd4fc425869f`

Delivery: terminal report for the Orchestrator to store as `42_report_00.md`. No report file was written, in accordance with the issued prompt.

**1. Result and scope**

Implemented the three bounded C6 corrections and committed them in exactly one local, non-amended commit:

`e9413dff98605443e7d17557f498c87433c93e92`  
`Fix C6 ingress spelling and environment permission parity`

Changed files:

| File | Purpose |
|---|---|
| [deploy/ubuntu/kronika_release.py](/home/agile/Projects/kronika/deploy/ubuntu/kronika_release.py) | Shared accepted ingress spellings, scheme-preserving replacement, bound environment metadata/content evidence, ownership/mode restoration and installed evidence verification. |
| [tests/contract/test_kronika_identity_migration.py](/home/agile/Projects/kronika/tests/contract/test_kronika_identity_migration.py) | Stateful boundary support, regression matrices, negative cases and five mutation demonstrations. |

The final focused migration module, full Python suite and separate retention module passed. The working tree is clean. Committed source hashes match the tested bytes.

This is an implementation PASS. It is not independent certification, logical-whole closure, publication or live-host acceptance.

NUC contact: none.  
SSH, migration invocation, deployment, provider, browser and capture contact: none.  
Push, branch creation, tag, stash and amend: none.  
Delegation: none.

**2. Reproduced baseline defects and corrected outcomes**

Before production edits, temporary tests reproduced all three defects through the real command builders and synthetic boundary.

| Defect | Baseline observation | Corrected outcome |
|---|---|---|
| D-1 | `unix:<old-socket>` classified as the single former handler, then refused by `replace_tailscale_handler` with `existing ingress handler target is unexpected`, exit 27. | Classification and guard share the same two exact accepted spellings. Both pass the replacement boundary. Foreign targets still fail closed. |
| D-2 | Replacement command always contained `tailscale serve --bg unix+http://<new-socket>`, including when the observed handler used `unix:`. | Replacement preserves the observed scheme: `unix:` remains `unix:`; `unix+http://` remains `unix+http://`. |
| D-3 | Transforming an environment file observed as `root:framenest:640` produced `root:root:600`. No ownership, mode or installed metadata verification command occurred. | Observation binds source metadata and digest. Installation restores the observed owner, group and mode, verifies installed metadata and transformed-content digest, and the existing account/group rename produces final `root:kronika:640`. |

Baseline reproduction and AST inventory: **2 passed, 231 deselected in 0.63s**. Temporary reproduction material was removed before the final commit.

The installed Tailscale rejection and manually completed host state are supplied operational evidence from the authoritative prompt and Meta notes. They were not independently re-observed on the NUC in this cut.

**3. Ingress spelling and refusal matrix**

The shared spelling function returns precisely:

```python
def tailscale_unix_targets(socket_path: str) -> tuple[str, str]:
    """Accepted socket spellings, in matching order for a scheme-preserving edit."""
    return f"unix+http://{socket_path}", f"unix:{socket_path}"
```

It is used by the classifier, replacement guard and verifier.

| Observed state | Classification/replacement | Verification |
|---|---|---|
| One `unix:<old>` handler | Exactly one `serve --bg unix:<new>` | New `unix:` form accepted; former handler absent. |
| One `unix+http://<old>` handler | Exactly one `serve --bg unix+http://<new>` | New `unix+http://` form accepted; former handler absent. |
| One former handler plus an unrelated handler | Exactly one replacement; unrelated target retained | Correct canonical target accepted. |
| Foreign HTTP target, foreign socket or empty proxy | No former handler; replacement refuses, exit 27 | Refuses without a valid canonical target. |
| Near-miss former or canonical path | Not accepted through prefix matching | Refuses. |
| Unsupported `unix://` spelling | Not classified as accepted | Refuses. |
| Two former handlers, including mixed accepted spellings | Uniqueness refusal, exit 27 | No replacement command. |
| Zero handlers | Exact result `{"replaced": 0, "handler_count": 0}` | Existing health check runs; Serve verification is skipped for a zero-handler plan. |
| Forged classification index pointing to a foreign target | Exact guard refusal retained, exit 27 | No mutation command. |
| Non-default mount, wrong port or empty mount | Existing command-builder refusal, exit 27 | No replacement command. |

Both successful round trips assert the exact generated command, exactly one replacement, preservation of the unrelated target and absence of `reset`.

`cmd_remote_tailscale_replace`, its `:443/` mount guard and `--bg` behavior are unchanged.

The changed host methods are:

```python
def replace_tailscale_handler(self) -> dict[str, object]:
    state = self.record_tailscale_state()
    self._tailscale_state = state
    handler_count = int(state["handler_count"])
    old_handlers = list(state["old_handlers"])
    mounts = list(state["mounts"])
    targets = list(state["targets"])
    if handler_count == 0 and not old_handlers:
        return {"replaced": 0, "handler_count": 0}
    if len(old_handlers) != 1:
        raise ReleaseError(
            "existing ingress handler is not uniquely identifiable",
            EXIT_MIGRATION,
        )
    index = old_handlers[0]
    old_forms = tailscale_unix_targets(self.plan.old_layout.socket_path)
    if targets[index] not in old_forms:
        raise ReleaseError(
            "existing ingress handler target is unexpected", EXIT_MIGRATION
        )
    new_target = tailscale_unix_targets(self.plan.new_layout.socket_path)[
        old_forms.index(targets[index])
    ]
    ssh(
        self.runner,
        **self.transport,
        remote_command=cmd_remote_tailscale_replace(mounts[index], new_target),
    )
    return {"replaced": 1, "handler_count": handler_count}
```

```python
def verify_ingress(self) -> None:
    release_path = self.plan.new_layout.release_dir(self.plan.release_sha)
    ssh(
        self.runner,
        **self.transport,
        remote_command=cmd_remote_check_health(release_path, self.plan.new_layout),
    )
    if self.plan.tailscale_handler_count == 0:
        return
    status = parse_tailscale_serve_status(
        ssh(
            self.runner,
            **self.transport,
            remote_command=cmd_remote_tailscale_serve_status(),
        )
    )
    socket_path = self.plan.new_layout.socket_path
    new_forms = set(tailscale_unix_targets(socket_path))
    if status["old_handlers"] or not (set(status["targets"]) & new_forms):
        raise ReleaseError("ingress replacement did not verify", EXIT_MIGRATION)
```

The classifier now reads:

```python
def parse_tailscale_serve_status(raw: str) -> dict[str, object]:
    """Classify the Serve handler set without exposing host identifiers."""
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ReleaseError("ingress status is unreadable", EXIT_MIGRATION) from exc
    if not isinstance(payload, dict):
        raise ReleaseError("ingress status is unreadable", EXIT_MIGRATION)
    mounts: list[str] = []
    targets: list[str] = []
    old_handlers: list[int] = []
    web = payload.get("Web")
    if isinstance(web, dict):
        for mount, block in web.items():
            handlers = block.get("Handlers") if isinstance(block, dict) else None
            if not isinstance(handlers, dict):
                continue
            for path, handler in handlers.items():
                proxy = handler.get("Proxy") if isinstance(handler, dict) else None
                if not isinstance(proxy, str):
                    continue
                mounts.append(f"{mount}{path}")
                targets.append(proxy)
                if proxy in tailscale_unix_targets(OLD_WEB_LAYOUT.socket_path):
                    old_handlers.append(len(targets) - 1)
    return {
        "handler_count": len(targets),
        "mounts": mounts,
        "targets": targets,
        "old_handlers": old_handlers,
    }
```

**4. Environment parity, evidence binding and phase ordering**

A material ordering fact governs D-3: `transform-environment` precedes `rename-account`. The canonical group does not yet exist when the environment file is installed.

The implementation therefore applies the observed group by name after the atomic move, verifies that installation, and relies on the existing, unchanged group rename to preserve the group identity under its canonical name. It does not assume the account’s primary GID identifies the file’s named group.

Consequently, the prompt’s literal intermediate demonstration of `chown root:kronika` inside `transform_environment` cannot coexist with the unchanged phase sequence. The implemented and tested sequence is:

`root:framenest:640` → installed and verified `root:framenest:640` → existing group rename → final `root:kronika:640`.

| Former evidence | Installation evidence | Evidence after existing rename |
|---|---|---|
| `root:framenest:640` | `root:framenest:640` | `root:kronika:640` |
| `root:root:640` | `root:root:640` | `root:root:640` |
| `operator:operators:600` | `operator:operators:600` | `operator:operators:600` |
| Former service group GID 1001; account primary GID 2001 | File remains assigned to the observed named group, GID 1001 | Canonical group retains GID 1001; account primary GID remains 2001. |
| Former service-account name as file owner | Refused during plan construction | Owner name cannot be preserved through the account rename. |
| `absent`, `unsafe`, `query-failed` | Distinct failure classifications, exit 27 | No installation. |
| Empty/malformed evidence, invalid octal mode, invalid digest, unresolved owner/group or extra tokens | Refused, exit 27 | No installation. |
| Installed owner, group, mode or digest mismatch | Refused, exit 27 | Transform does not report success. |
| Installed absent/unsafe/query-failed/empty evidence | Refused, exit 27 | Transform does not report success. |

The non-account group cases preserve their original access exactly. The implementation does not add service-group access to a file that lacked it.

The new helpers are:

```python
def parse_environment_file_evidence(evidence: str) -> tuple[str, str, str, str]:
    """Require one regular file's named owner/group, octal mode and SHA-256."""
    evidence = _require_query_result(evidence, "former environment file")
    if evidence in ("absent", "unsafe"):
        raise ReleaseError(f"former environment file is {evidence}", EXIT_MIGRATION)
    match = re.fullmatch(
        r"([A-Za-z_][A-Za-z0-9_.-]*\$?):([A-Za-z_][A-Za-z0-9_.-]*\$?):"
        r"([0-7]{1,4}) ([0-9a-f]{64})",
        evidence,
    )
    if match is None or "UNKNOWN" in match.group(1, 2):
        raise ReleaseError("former environment file evidence is malformed", EXIT_MIGRATION)
    owner, group, mode, digest = match.groups()
    return owner, group, format(int(mode, 8), "o"), digest
```

```python
def environment_file_ownership(
    evidence: str, old_layout: WebLayout
) -> tuple[str, str, str]:
    """Return chown identity, mode and the expected pre-rename stat metadata.

    Environment installation precedes account rename. Apply the observed group
    by name: the later groupmod preserves that group's identity and gives it
    the canonical name. The account's primary GID need not name this group.
    Verify its still-former name at installation.
    Other owners and groups retain their observed names and access exactly.
    """
    owner, group, mode, _digest = parse_environment_file_evidence(evidence)
    if owner == old_layout.user:
        raise ReleaseError("environment file owner cannot be preserved", EXIT_MIGRATION)
    return f"{owner}:{group}", mode, f"{owner}:{group}:{mode}"
```

The complete changed installation method is:

```python
def transform_environment(self) -> dict[str, object]:
    ownership, mode, expected_metadata = environment_file_ownership(
        self.plan.environment_file_evidence,
        self.plan.old_layout,
    )
    destination = self.plan.new_layout.env_file
    ssh(
        self.runner,
        **self.transport,
        remote_command=cmd_remote_make_directory(
            str(Path(destination).parent), "0755"
        ),
    )
    payload = self.plan.environment.text.encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    # Write beside the destination, verify the canonical-only assertion on
    # the staged bytes, then move the file into place atomically.
    pending = f"{destination}.next"
    ssh(
        self.runner,
        **self.transport,
        remote_command=cmd_remote_write_file(pending, digest),
        input_bytes=payload,
    )
    assertion = ssh(
        self.runner,
        **self.transport,
        remote_command=cmd_remote_assert_no_retired_assignments(pending),
    ).strip()
    if assertion != "canonical-only":
        raise ReleaseError(
            "installed environment still carries retired assignments",
            EXIT_MIGRATION,
        )
    ssh(
        self.runner,
        **self.transport,
        remote_command=(
            f"sudo -n mv -T {shlex.quote(pending)} {shlex.quote(destination)}"
        ),
    )
    ssh(
        self.runner,
        **self.transport,
        remote_command=f"sudo -n chown {shlex.quote(ownership)} {shlex.quote(destination)}",
    )
    ssh(
        self.runner,
        **self.transport,
        remote_command=f"sudo -n chmod {mode} {shlex.quote(destination)}",
    )
    metadata, installed_digest = self._root_file_evidence(
        destination, "installed environment file"
    )
    if metadata != expected_metadata or installed_digest != digest:
        raise ReleaseError("installed environment file did not verify", EXIT_MIGRATION)
    return {
        "moved_path_keys": list(self.plan.environment.moved_path_keys),
        "preserved_path_keys": list(self.plan.environment.preserved_path_keys),
    }
```

For the longer observation and plan functions, the following are the exact changed blocks; their surrounding logic remains unchanged.

In [read_migration_observation](/home/agile/Projects/kronika/deploy/ubuntu/kronika_release.py:4798):

```python
environment_file_evidence = ssh(
    runner,
    **transport,
    remote_command=cmd_remote_root_file_evidence(old_layout.env_file),
).strip()
_owner, _group, _mode, source_digest = parse_environment_file_evidence(
    environment_file_evidence
)
environment_source = ssh(
    runner,
    **transport,
    remote_command=cmd_remote_read_optional_file(old_layout.env_file),
)
environment_raw = _require_query_result(environment_source, "former environment file")
if environment_raw == "absent":
    raise ReleaseError("former environment file is absent", EXIT_MIGRATION)
if hashlib.sha256(environment_source.encode("utf-8")).hexdigest() != source_digest:
    raise ReleaseError("former environment file content did not verify", EXIT_MIGRATION)
```

The returned `MigrationObservation` receives:

```python
environment_file_evidence=environment_file_evidence,
```

Both `MigrationObservation` and `MigrationPlan` declare:

```python
environment_file_evidence: str
```

[build_migration_plan](/home/agile/Projects/kronika/deploy/ubuntu/kronika_release.py:2926) validates the evidence before constructing the plan:

```python
environment_file_ownership(
    observation.environment_file_evidence,
    observation.old_layout,
)
```

Its digest input includes:

```python
"environment_file_evidence": observation.environment_file_evidence,
```

Its `MigrationPlan` constructor includes:

```python
environment_file_evidence=observation.environment_file_evidence,
```

`MigrationPlan.payload()` includes:

```python
"environment_file_evidence": self.environment_file_evidence,
```

Evidence binding is precise:

- The plan binds the observed evidence string after outer whitespace stripping: `owner:group:mode <SHA-256>`.
- The source SHA-256 is checked against the **unstripped** UTF-8 source content returned by the existing read command, including its final newline.
- The existing `environment_sha256` plan field binds the transformed UTF-8 payload.
- The unchanged write builder verifies the staged payload digest.
- Canonical-only validation runs against the staged file before `mv -T`.
- Ownership and mode are applied after the move.
- Installed evidence must match both the expected metadata and transformed payload digest.
- Independent changes to owner, group, mode or source digest change the plan digest. Apply rejects observed plan drift before mutation.
- Source disappearance or content changes between evidence collection and content reading fail closed.

Tests preserve the prior destination on staged-write, canonical-assertion and atomic-move failures. The canonical-only refusal message and exit code remain unchanged.

The root-file evidence command was also exercised through `/bin/sh` against synthetic temporary files, directories and symlinks, using a shell-local `sudo` substitute. No real sudo or remote access occurred.

**5. Mutation demonstrations**

The committed mutation tests parse the production class with `ast`, modify one method in memory, compile it, and use `monkeypatch` for restoration. They do not write mutated production files.

Each demonstration first exercises the unmutated behavior and asserts the expected number of AST edits.

| Mutation | Observed regression |
|---|---|
| `old-only-guard` | The `unix:` round trip raises `existing ingress handler target is unexpected`, `EXIT_MIGRATION` (27). |
| `fixed-replacement` | The assertion requiring the exact mirrored `unix:` target fails. |
| `no-ownership` | Installed metadata verification raises `installed environment file did not verify`, exit 27. |
| `no-mode` | Installed metadata verification raises the same mismatch refusal, exit 27. |
| `no-verification` | Unsafe installed evidence is accepted; the rejection assertion fails with `DID NOT RAISE`. |

All five mutations were detected. They are retained in [test_c6_completion_mutation_demonstrations](/home/agile/Projects/kronika/tests/contract/test_kronika_identity_migration.py:4841).

**6. Validation results and provenance**

Python evidence used only the authorized AP route with the exact baseline:

`fcde631047650d1ff0a84b84bf185b54d6d11ba5`

Initial repository gates matched the prompt: standalone checkout, clean `main`, expected HEAD, correct public repository, matching public `main`, unchanged AP gitlink/submodule HEAD, AP doctor PASS and baseline project check PASS.

The AP runtime check established CPython 3.13 and repository-local package provenance. No direct Python, `.venv/bin/python` or `poetry run` invocation was used.

Final acceptance runs:

| Check | Result | Pytest elapsed | Difference from supplied baseline |
|---|---:|---:|---|
| Focused migration module | **285 passed** | **1.22s** | +54 passed versus 231 |
| Full declared Python suite | **4,955 passed, 8 skipped, 3 warnings, 0 failed** | **661.87s** | +54 passed; skips, warnings and failures unchanged versus 4901/8/3/0 |
| Separate retention module, after full suite | **15 passed** | **0.37s** | No change versus 15 |

All three final runs exited 0.

The final full suite collected 4,963 tests. Its three warnings remained the `PydanticJsonSchemaWarning` concerning the non-JSON-serializable `OMITTED` default, reported by two health-contract tests and one configuration test. The eight skips were the gated real-tools/live integration cases. No live provider test was activated.

The baseline aggregate counts are the Orchestrator’s supplied baseline evidence; this Worker did not repeat the entire baseline suite.

Supplementary execution results, including superseded development runs:

| Check | Result | Elapsed |
|---|---|---:|
| Baseline reproduction plus AST inventory | 2 passed, 231 deselected | 0.63s |
| Initial new-case selection | 52 passed, 232 deselected | 0.62s |
| Intermediate focused module, including temporary material | 284 passed | 1.81s |
| Expanded selection plus temporary inventory | 58 passed, 231 deselected | 1.03s |
| Initial statement-trace probe | 289 passed, 1 teardown error | 3.78s |
| Corrected intermediate trace selection | 57 passed, 232 deselected | 0.99s |
| Superseded focused implementation | 288 passed | 1.22s |
| Intentionally interrupted preliminary full suite | 1,224 passed, 2 warnings; `KeyboardInterrupt`, exit 2 | 203.07s |
| Final changed-statement trace selection | 54 passed, 231 deselected | 0.97s |

The interrupted full suite and faulty temporary trace probe are not acceptance evidence. Their causes and resolutions are recorded below.

The final trace probe was removed before the full acceptance run. After committing, SHA-256 checks confirmed unchanged tested bytes:

```text
deploy/ubuntu/kronika_release.py
1708ebf365abd6749cf0bcf20cd738a83dcd3e04a146613d7b3c273f301da882

tests/contract/test_kronika_identity_migration.py
9180f511717b1fe367ad8bd236e62b1fdcdb81805c7340dd0a4a7faecd91fdd4
```

**7. Git result and retention measurements**

Exactly one `git add` named the two authorized paths. Exactly one local commit followed. Its parent is the required baseline.

Actual commit diff:

```text
 deploy/ubuntu/kronika_release.py                  | 106 ++++-
 tests/contract/test_kronika_identity_migration.py | 469 +++++++++++++++++++++-
 2 files changed, 551 insertions(+), 24 deletions(-)
```

Per-file additions/deletions:

```text
87   19  deploy/ubuntu/kronika_release.py
464   5  tests/contract/test_kronika_identity_migration.py
```

`git diff --check` and staged-diff checks passed. Post-commit status is clean. Local `main` is one commit ahead of `origin/main`; no push occurred. Public `main` was rechecked before commit and still pointed to the baseline.

No documentation, dependency, lockfile, configuration, Alembic revision, retention ledger or AP file changed.

Retention values were independently regenerated at report time from tracked files and checked against the retained assertions and baseline.

Part A:

- **86 frozen document hashes:** all match.
- **36 frozen Alembic revision keys:** computed, all hashes match.
- Retention module: byte-identical to baseline.
- Frozen bytes: unmoved.

Part B:

- **20** tracked paths with the retired basename token.
- Exact membership remains unchanged; retention assertions pass.

Part C:

| Tree | Files containing retired token | Case-insensitive occurrences | Baseline delta |
|---|---:|---:|---:|
| `src` | 186 | 1,706 | 0 |
| `tests` | 186 | 2,283 | 0 |
| `deploy` | 22 | 248 | 0 |
| `scripts` | 11 | 98 | 0 |
| `docs` | 88 | 1,206 | 0 |
| `extension` | 8 | 145 | 0 |

| Additional measurement | Final value | Baseline delta |
|---|---:|---:|
| Content-path membership | 516 files | 0 |
| Environment prefix tokens | 702 | 0 |
| Distinct environment names | 114 | 0 |
| Bare environment prefix spellings | 53 | 0 |
| Mutation-header occurrences / files | 73 / 30 | 0 |
| Capitalized occurrences / files | 2,773 / 399 | 0 |
| Console-script entries | 14 | 0 |
| `User=framenest` / `Group=framenest` | 9 / 9 | 0 |

| Host-path token | Occurrences | Baseline delta |
|---|---:|---:|
| `/opt/framenest` | 231 | 0 |
| `/etc/framenest` | 88 | 0 |
| `/var/lib/framenest` | 128 | 0 |
| `/var/cache/framenest` | 31 | 0 |
| `/mnt/framenest-catalog-offdevice` | 26 | 0 |

No Part C scalar moved, so no re-pin was necessary or performed. New tests derive former names from existing layout constants. The touched engine retains 85 retired-token occurrences; the migration test retains 295.

The independent measurement excluded the retention ledger from its own content counts and skipped binary files, matching ledger semantics. Its known-impossible sentinel control measured zero.

**8. Derived callers, boundary branches and unexercised sites**

The affected inventory was derived by parsing the engine and tests. Locator matches were not treated as a caller inventory. Assertion context was inspected before classifying literals as pins.

Additional relationships and branches identified beyond the prompt’s direct list:

| Site or relationship | Finding and treatment |
|---|---|
| `_cmd_migrate_preflight` and `_cmd_migrate_apply` | Both obtain observations and build plans. Evidence changes affect digest comparison; drift refusal is exercised before mutation. |
| `run_migration_apply` and `_MIGRATION_PHASE_METHODS` | Production methods are invoked through phase dispatch. The phase order and mapping remain unchanged. |
| `record_tailscale_state` | Supplies parsed status to replacement; round-trip tests exercise it before and after mutation. |
| Environment installation versus account rename | Installation precedes rename. Tests cover installation metadata and final renamed-group metadata. |
| Named service group versus primary GID | They need not coincide. A dedicated test uses GIDs 1001 and 2001 to prevent an accidental substitution. |
| Source evidence versus later content read | Source content can change or disappear between reads. Digest drift, absent and query-failed cases are exercised. |
| Zero-handler verification | Health still runs while the Serve query is omitted for a zero-handler plan. |
| Default Serve mount | Root path on port 443 remains enforced; three invalid mount cases are exercised. |
| Shared `cmd_remote_write_file` | Also serves release preparation, unit/drop-in installation and routine deployment uploads. The builder is unchanged; staged digest behavior remains covered. |
| Shared `_root_file_evidence` | Existing ancillary installation/validation callers remain unchanged; environment installation adds another caller. |
| `service_account_prefix` | Database status, backup status and scheduled-backup routes explain why environment readability is functional. These commands were not changed. |
| Other `MigrationPlan` references | The local-state migration module’s similarly named class is a separate implementation, not a caller of this release-engine plan. |

Every moved or removed production site lacking test exercise: **none identified**.

A temporary AST-aware statement trace measured **31 changed executable statements** in the final implementation. Its unexercised set was empty. Dataclass declarations and docstrings were excluded from executable-statement counting; constructor, payload and digest tests cover the new bound field.

This is evidence for the changed executable sites, not a claim of complete branch coverage for the whole release engine.

**9. Resolved Execution Issues / Near-Misses**

1. **Output truncation during broad reading.** Some broad combined reads and supplemental ledger listings exceeded tool output limits. They were not used as complete inventory evidence. Required material was recovered through bounded reads, and final measurements were regenerated with compact output. The parsed affected-site inventory was complete.

2. **Temporary trace probe counted docstrings.** The first probe treated three docstrings as executable statements and produced one teardown error despite 289 passing tests. The probe was corrected to exclude docstrings. The final probe found all 31 changed executable statements exercised. Temporary probe code was removed.

3. **Primary-GID assumption rejected during review.** An intermediate ownership approach depended on the account’s primary GID identifying the observed service group. Review established that this need not hold. The preliminary full suite was intentionally interrupted after 1,224 passing tests, the implementation was corrected to apply the observed group by name, and a dedicated divergent-GID test was added. The final focused, full and retention runs all passed.

No unresolved execution issue remains within this bounded task.

**10. Pre-Existing Failure Classification**

None asserted as an unresolved pre-existing test failure.

The three baseline behavioral defects were reproduced before correction and are addressed by this commit. The temporary probe error was Worker-created instrumentation failure. The interrupted suite was a deliberate stop for correction. Neither is classified as a repository failure.

The final suite has zero failed tests. Its warnings and skips match the supplied baseline counts.

**11. Deviations, risks, missing evidence and next step**

The material implementation qualification is the D-3 phase ordering described above: installation verifies the former group name, and the unchanged group rename establishes the canonical name later. A direct canonical-group `chown` during installation would require changing the sequence or assuming an account/group state the existing observation rejects.

The apply sequence, phase names, journal and receipt shapes, recovery semantics and unrelated command builders remain unchanged. The plan gains the explicitly requested evidence field and corresponding digest binding.

No repository document requiring correction was identified for these behaviors. The deployment guide’s `unix:` Serve form is consistent with the corrected replacement path.

Live execution evidence for the corrected engine is intentionally absent. The NUC was already completed manually, and this task prohibited host contact and migration invocation. Synthetic command-boundary tests establish the repository behavior; they do not claim a new live migration.

**Smallest next step:** perform the required fresh independent re-audit of commit `e9413dff98605443e7d17557f498c87433c93e92`, explicitly checking the D-3 phase-order interpretation and all three regression matrices. Archival of the failed C6 journal remains contingent on that re-audit’s PASS and separate authority.

Authority expiry: submission of this terminal report ends this grant. No further implementation, second commit, push, publication, host contact or later cut is authorized.

Orchestration critique:  
MEASURED: The prompt’s literal D-3 intermediate expectation names the canonical group during a phase that precedes account/group rename. Repository phase order and the boundary tests establish that the group does not yet exist. Applying the observed group, verifying installation and retaining the existing rename produces the required final parity without sequence changes. The smallest correction is to distinguish installation-time metadata from final post-rename metadata in future verification instructions.  
LEAD: none