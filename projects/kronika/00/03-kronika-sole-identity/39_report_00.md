### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity
Worker session ordinal: 39
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit, read-only
Task identity: KSI-AUDIT-C6UNK
status: PARTIAL
Phase-qualified result: not-applicable
Start commit: 980041cf13dd427e77263f573694aed7c1a54018
End commit: 980041cf13dd427e77263f573694aed7c1a54018
Report justification: new-evidence
Logical-whole closure: not-closed
NUC contact: none

The candidate implements the expressly specified literal, case-insensitive policy. All required repository checks pass, all three mutations are detected, and supported-directive behavior is unchanged. The escaped-unknown-value LEAD is substantiated by a synthetic observation probe and installed systemd documentation: absence of the raw spelling does not establish absence of the decoded spelling. That design assumption survives the correction and recheck. No defect affecting the supplied plain `RuntimeDirectoryMode=0700` live setting is demonstrated, but unconditional acceptance needs an explicit residual-risk disposition.

Escalation disposition: NEEDS_ORCHESTRATOR_DECISION

Evidence posture: independent local review of the exact candidate and parent blobs; predecessor reports were treated as claims. No live host or public branch observation. No correction, repository edit, Git write, commit, push, publication, provider call, browser access, or migration invocation occurred. Calls to `read_migration_observation` used the synthetic `ReadOnlyPreflightRunner`; their results are prepared installation text, not real installations.

#### 1. Identity, scope and gate verification

- Standalone checkout `/home/agile/Projects/kronika`, branch `main`, initially and finally clean.
- Candidate `980041cf13dd427e77263f573694aed7c1a54018`; parent `78cba281960e2f17137647bcc90aab83847a1c0c`.
- Containing gitlink and submodule HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`; submodule clean.
- `ap doctor`: PASS, strict pin, governing variant `stable`. Baseline-bound `ap project check`: PASS.
- `runtime-info`: CPython 3.13.9; interpreter invoked through the declared `.venv`; `kronika` imported from `/home/agile/Projects/kronika/src/kronika/__init__.py`. No ambient Python invocation or environment reconstruction.
- Local `refs/remotes/origin/main` equals the parent. Public branch state not directly observed; network access was not authorized.
- Exactly three modified paths, no addition, deletion, rename, or mode change:

| Candidate path | Additions / deletions |
|---|---:|
| `deploy/ubuntu/kronika_release.py` | 20 / 7 |
| `tests/contract/test_kronika_identity_migration.py` | 71 / 3 |
| `tests/contract/test_kronika_identity_retention.py` | 30 / 4 |

The engine changes two docstrings and the terminal unknown-directive branch at lines 4425–4432. Exact source-segment comparison establishes that all supported branches are byte-identical to the parent; the executable body of `transform_unit_dropin_text` is also byte-identical. Every other top-level function/class source segment, including the classifier, revision renderer, path transformer, observation reader, and sudoers guards, is unchanged. Supported sets, root mappings, frozen prefixes, segment renames, and exit code 27 are unchanged. Diff inspection shows no other engine edits.

The terminal condition checks both `key.lower()` and `value.lower()`. Its retained refusal has exactly `unit directive <key> is not supported` and exit 27. The current prompt explicitly replaces the older blanket-unknown-refusal policy in report 25 section 2.2; that older wording was not used to reject the authorized new policy.

#### 2. Policy matrix results

| Synthetic input | Candidate result |
|---|---|
| `RuntimeDirectoryMode=0700` | Preserved byte-for-byte |
| `Environment=FOO=bar` | Preserved byte-for-byte |
| `UnknownDirective=value` | Preserved byte-for-byte |
| `UnknownDirective=framenest-x` | Refused, exit 27, exact unsupported-directive message |
| `Environment=FRAMENEST_X=1` | Refused, exit 27, exact message |
| `UnknownDirective=fraMeNest-x` | Refused, exit 27, exact message |
| `FramenestMarker=value` | Refused, exit 27, exact message |
| Uppercase and alternating-case brand-bearing keys | Refused, exit 27, exact message |
| Both key and value brand-bearing | Refused, exit 27, exact message |

Preservation was independently checked with LF endings, indentation, surrounding value whitespace, no final newline, and idempotence. All three brand-free forms also passed the synthetic observation path. The RuntimeDirectoryMode installation text was exactly `[Service]\nRuntimeDirectoryMode=0700`; the observation reader's existing stripping removes the trailing newline. All three forms refused at the parent, as expected from its old policy.

Supported identity, path, executable, credential, mixed-directive, and refusal cases remained correct. Blank lines and semicolon comments were independently exercised. `user=kronika` is treated as an unknown brand-free key and preserved, as the specified policy implies.

#### 3. Adjusted-test verdicts for every adjusted existing line

All three fixture edits retain genuine refusal assertions. Their assertion ASTs are identical to the parent. The four other entries of the existing refusal loop are unchanged.

| Candidate line in migration tests | Adjustment | Verdict |
|---|---|---|
| 2974 | `Environment=FOO=bar` → `Environment=FRAMENEST_FOO=bar` | Genuine observation-level refusal; same raises/exit/message assertions. Brand-free Environment is separately pinned for preservation. |
| 3141 | Same replacement in the refusal loop | Genuine transformer refusal; assertion unchanged. |
| 3144 | `UnknownDirective=value` → `UnknownDirective=framenest-x` | Genuine transformer refusal; original brand-free shape separately pinned for preservation. |

The remaining changed existing executable test lines are the four retention pins:

| Candidate retention line | Parent → candidate | Independent verdict |
|---|---|---|
| 723 | tests occurrences 2275 → 2283 | Correct: +8 in the migration test file |
| 736 | deploy occurrences 246 → 248 | Correct: two new literal checks |
| 1492 | environment-prefix tokens 699 → 702 | Correct: `FRAMENEST_FOO` twice, `FRAMENEST_X` once |
| 1493 | distinct prefix names 112 → 114 | Correct: those two new names |

No assertion was removed or weakened. Exactly four test functions were added. The retention module independently measures the current tracked tree and passes all its assertions.

Non-blocking prose discrepancy: retention lines 716–718 describe “two adjusted” plus “six remaining” occurrences. The actual split is three adjusted fixture occurrences plus five new matrix occurrences. The total eight and the executable pin are correct. Report 38's “no brand-bearing unknown passes” claim also needs the qualification “literal raw spelling”; section 5 demonstrates why.

#### 4. Regression results

An independent parent/candidate matrix exercised all four sites: path list, LoadCredential, plain ExecStart, and revision-form ExecStart.

| Category | Cases | Result |
|---|---:|---|
| Frozen, including escaped forms | 20 | Byte-identical preservation |
| Foreign, including escaped forms | 20 | Byte-identical preservation |
| Moved roots and renamed segments | 28 | Exact rewrite and idempotence |
| Near-miss roots | 16 | Same exit 27 and messages |
| Under-root leftovers | 16 | Same exit 27 and leftover message |

Additional passing comparisons covered:

- All six Exec directive names with frozen, foreign, and moved escaped revision tokens; raw capture preservation, reparse, and argument-text preservation.
- Four unprovable forms across all six Exec names: escaped root, escaped remainder slash, escaped root-boundary slash, and escaped renamed segment. All retain the exact revision-path refusal and exit 27.
- Twelve remainder forms, including escaped space, dot, semicolon, brace, tab, backslash, newline and carriage return, exact root, trailing slash and double slash; exact rendered capture and decoded reparse remained correct.
- All five path-directive names, both identity-directive names, and eleven other malformed/unclassifiable cases.
- Direct defensive renderer refusals for absent root pair and segment mismatch.
- The sudoers foreign-command guard: `sudo rule command path is not classifiable`, exit 27, unchanged.

No behavior difference from the parent was found in these supported-directive regressions. Existing residuals were reproduced unchanged: raw classification at the three non-revision sibling sites can preserve an escaped old root or partly rewrite an escaped renamed segment; malformed hexadecimal revision escapes raise `ValueError`; executable arguments remain opaque; relative foreign credential paths remain preserved.

#### 5. Escaped unknown-value LEAD and disposition

Synthetic input:

```text
[Service]
Environment=FOO=fra\x6denest
```

Candidate: preserved byte-for-byte by the transformer and carried through the synthetic observation into prepared installation text. Parent: refused with `unit directive Environment is not supported`, exit 27. This is a newly admitted unknown-directive form, not a parent-identical residual at that site.

Read-only local interpretation evidence:

- Installed binary reports systemd `261 (261.3-1-arch)`.
- `/usr/share/man/man5/systemd.exec.5.gz`, Environment section, specifies unquoting by the systemd.syntax quoting rules.
- `/usr/share/man/man7/systemd.syntax.7.gz`, version 261.3, Quoting section and escape table, specify C-style escapes and hexadecimal `\xXX` decoding.

Those primary installed manuals establish that this Environment assignment decodes to `FOO=framenest`. Transformer/observation behavior is reproduced dynamically; systemd interpretation is established from local documentation, not from starting a service. No claim is made about the NUC's installed systemd version or actual runtime.

**R1 — unresolved design residual:** a raw textual absence check does not establish absence of a decoded retired spelling. The implementation matches the expressly granted textual policy, but the broader assumption that every such unknown value is benign does not hold generally. The supplied live unknown setting is plain `RuntimeDirectoryMode=0700`, so this specific residual does not affect that supplied setting. Its live inventory completeness was not independently observed under this no-host grant.

Disposition: an Orchestrator decision is required for unconditional acceptance. This is not evidence that the reported live setting fails, and it is not authority to widen the correction.

#### 6. Independent mutation probes

Each mutation replaced exactly one asserted-unique source anchor in an in-memory engine module. Repository source was never edited. Each named committed test first passed against the unmutated candidate.

| Mutation | Committed tests exercised | Observed outcome |
|---|---|---|
| Remove brand check (`if False`) | `test_preflight_refuses_an_unknown_dropin_directive`; `test_structural_dropin_transformation_refuses_unknown_forms`; `test_structural_dropin_refuses_brand_bearing_unknown_directives` | All three failed: `DID NOT RAISE ReleaseError` |
| Force refusal (`if True`) | `test_structural_dropin_preserves_brand_free_unknown_directives`; `test_preflight_installs_a_brand_free_runtime_directory_mode_dropin`; `test_structural_dropin_transforms_a_mixed_unknown_and_supported_dropin` | All three failed with unsupported RuntimeDirectoryMode, exit 27 |
| Make value check case-sensitive | The same three refusal tests named in the first row | All three failed: `DID NOT RAISE ReleaseError` |

The case-sensitive mutation was additionally tested separately with uppercase `FRAMENEST_X=1` and mixed-case `fraMeNest-x` values. Both refusal expectations failed on the mutant and passed on the candidate. All three mutations were detected; no mutated code persisted.

#### 7. Checks and retention evidence

All Python evidence used the declared AP route and exact candidate baseline.

| Check | Result |
|---|---|
| Focused migration plus retention execution | 222 passed in 1.18 s |
| Independent collection count | 207 migration, 15 retention |
| Full Python suite | 4877 passed, 8 skipped, 3 warnings, 0 failed; 687.79 s |
| Independent audit probes | 193 passed in 1.52 s |
| Additional residual and pin probes | 17 passed in 1.20 s |
| Candidate diff whitespace check | PASS |

Difference from declared `4877/8/3/0`: none. The eight skips are five real-tool cover cases, two real-tool media-analysis cases, and one live NVIDIA NIM case. The three warnings are Pydantic non-serializable-default warnings at the two health/OpenAPI tests and the configuration representation test.

Full-suite invocation used `--operation test-focus -- -p no:cacheprovider --basetemp=/tmp/ksi39-audit.NKhy7M/full-tmp`, with no test selector. This ran the complete configured `tests` suite while avoiding repository cache writes; no tests were filtered out. The full suite ran once.

Part A declarations are byte-identical to the parent: 86 document keys and 36 Alembic keys, independently counted. Their hash and set-completeness tests passed. Part B's declaration is byte-identical, contains 20 paths, and its measured membership test passed. No frozen file or Part B path is in the candidate diff.

#### 8. Findings, blocking disposition and untested sites

- **R1, acceptance decision outstanding:** escaped unknown Environment values can carry the retired spelling after systemd decoding. The raw policy is correctly implemented; broader completeness acceptance is unresolved. This prevents an unconditional audit PASS until disposition, not a finding of failure in the supplied plain live setting.
- **R2, non-blocking retained limitations:** sibling-site escape gaps, malformed-hex `ValueError`, opaque Exec arguments, relative foreign LoadCredential preservation, and the sudoers foreign-command refusal are parent-identical and reproduced.
- **R3, non-blocking wording limit:** the existing renderer normalizes CRLF to LF. Whole-document “byte-for-byte” preservation is therefore limited to the tested LF forms; value/indentation preservation and the unchanged renderer were verified. The observation reader also strips outer whitespace as before.
- **R4, non-blocking prose defect:** the retention comment's three-plus-five split is misstated as two-plus-six; executable counts remain correct.

No new terminal-policy branch is untested: preservation, key-triggered refusal, and value-triggered refusal were exercised. The broader unsupported-key space is intentionally not semantically validated by this transformer.

Not exercised in this audit: live systemd parsing/execution, NUC inventory and deployment, public branch equality, arbitrary systemd directive/specifier semantics, malformed multi-`path=` revision forms, and the revision reparse guard's three rejecting subconditions by fresh fault injection. Successful reparsing, unprovable rendering refusals, and the unchanged guard source were verified; predecessor mutation results are not claimed as freshly executed evidence. The eight environment-gated full-suite cases remained skipped. No browser, provider, or private-data evidence was obtained or required.

#### 9. Deviations, containment, missing evidence and next step

The original prompt prohibited report persistence. Before terminal submission, the Cooperator explicitly instructed continuation and writing `39_report_00.md`. That later instruction authorizes this one report at the already named Meta destination. The destination was absent, its physical parent resolved to the expected directory, and no ancestor AGENTS.md was found on that destination path. No Meta Git operation is authorized or performed.

Containment: `/tmp/ksi39-audit.NKhy7M` was created as an owned private temporary directory. It contained only synthetic probe source, pytest temporary fixtures, and the full-suite log. Parent/mutant engine modules existed in memory. The exact audit directory was removed and its absence verified. The initial focused run used pytest's default temporary area, whose current pointer resolves to `/tmp/pytest-of-agile/pytest-8`; that pytest-managed area is retained and reported rather than deleting shared temporary state whose ownership was not recorded before that initial run. No project artifact was written by these probes, and pytest caching was disabled.

Command accounting: read-only Git inspection (`status`, `branch --show-current`, `rev-parse`, `ls-tree`, `show`, `diff`, `ls-files`); AP doctor/check/runtime/test operations; file inspection with `cat`, `sed`, `rg`, `nl`, `tail`, `awk`, `stat`, `readlink`, `realpath`, and shell file predicates; local manual decompression with `gzip -cd`; and `systemd-analyze --version`. These inspection commands mutated nothing. `mktemp`, shell heredocs/redirection, pytest fixture creation, and cleanup affected only the reported temporary state; the separately authorized final heredoc creates this report. No dependency or system configuration was changed.

Final project state: unchanged HEAD and parent, clean project and AP worktrees, unchanged AP pin, clean candidate diff check. Source/probe work is complete. The missing evidence and residual acceptance are explicitly bounded above.

Smallest next step: the Orchestrator records an explicit disposition of R1 for the reported plain live directive set before treating this re-audit as permission to proceed to a separately authorized publication/preflight window.

#### Resolved Execution Issues / Near-Misses

- The full suite continued during the Cooperator's interruption. On resumption, its original process returned exit 0 and the complete terminal summary was read; it was not restarted or double-counted.
- Automatic command review rejected the first temporary cleanup command because it used `rm -rf`; none of that compound command executed. The safer exact-path `rm -r -- /tmp/ksi39-audit.NKhy7M` succeeded. Directory absence and final Git gates were then independently verified. No cleanup residual remains in that owned audit directory.
- The first broad combined documentation read was output-truncated. The relevant mandatory protocol, execution, source, and report sections were subsequently read in bounded selections; truncated output was not treated as complete evidence.

#### Pre-Existing Failure Classification

none. No repository test failed. Deliberate in-memory mutation failures were expected audit evidence. Parent-identical behavior limitations are listed as residual observations, not used to dismiss a failing gate.

Persistence: this report is saved at `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/39_report_00.md` under the Cooperator's later explicit instruction. Complete readback and delivery verification precede the terminal completion notice. No report commit or push.

Authority expiry: submission of this terminal report ends this grant. No autonomous correction, publication, host action, or later cut is authorized.

Orchestration critique:
MEASURED: The unknown-directive policy tests raw text, while the locally documented Environment parser decodes C-style escapes. A synthetic `Environment=FOO=fra\x6denest` is preserved through candidate observation but refused by the parent; installed systemd 261.3 manuals establish decoding to the retired spelling. Effect: general decoded-spelling completeness cannot be inferred from the passing literal-policy tests. Smallest correction to orchestration: explicitly accept or reject this residual for the supplied plain live set; do not silently turn a literal-policy PASS into broader semantic acceptance.
LEAD: Whether the effective NUC inventory includes any encoded or specifier-derived unknown value beyond the supplied plain RuntimeDirectoryMode setting remains unverified here. Cheapest useful check, only if the Orchestrator lacks complete prior inventory evidence: inspect and classify those effective values during the next separately authorized read-only host preflight.
