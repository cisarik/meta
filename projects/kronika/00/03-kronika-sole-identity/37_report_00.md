The audit is complete — all gates, checks, and probes have run, and the temporary state is verified and reported (removal was denied by the environment). Delivering the terminal report now.

---

### Report for ORCHESTRATOR_CHAT

| Field | Value |
|---|---|
| Logical whole identity | `kronika-sole-identity` |
| Worker session ordinal | `37` |
| Worker exchange ordinal | `01` |
| Persistent role identity | `WORKER` |
| Worker session target | `fresh-worker-session` |
| Native planning mode | `not-used` |
| Worker session profile | Fresh Independent Audit, read-only |
| Task identity | `KSI-AUDIT-C6ENC` |
| Status | **PASS** |
| Report justification | `new-evidence` |
| Phase-qualified result | `not-applicable` |
| Logical-whole closure | `not-closed` |
| Start and end commit | `78cba281960e2f17137647bcc90aab83847a1c0c` (unchanged) |
| Parent | `cf76f0b3a391663db7f4b0c88b872c08b69ff279` |
| Repository changes / commits / pushes | none |
| NUC contact | none |

The escaped revision-token repair is accepted. B1 is fixed at the candidate; the correction's refusals are intact; all three in-memory mutations are detected; the declared checks reproduce exactly (203 / 15 / 4873‑8‑3‑0); Part A (86/36) and Part B (20) are unchanged. No blocking finding remains. Two new fail-closed behaviors and one pre-existing sibling-site escape gap are recorded as residuals, not defects.

#### 1. Identity, scope and gate verification

Independently re-derived:

- Standalone checkout `/home/agile/Projects/kronika`, branch `main`, clean initially and finally; HEAD = candidate `78cba281960e2f17137647bcc90aab83847a1c0c`; `rev-parse 78cba28^` = `cf76f0b3a391663db7f4b0c88b872c08b69ff279`.
- Exactly three modified paths, all `M`; no add/delete/rename and no mode change (`git diff --summary` empty):

| Path | numstat |
|---|---|
| `deploy/ubuntu/kronika_release.py` | +71 / −5 |
| `tests/contract/test_kronika_identity_migration.py` | +132 / −0 |
| `tests/contract/test_kronika_identity_retention.py` | +24 / −4 |

- Engine hunks: helper insertion at old 4254, revision-branch rewrite at old 4296 / 4301 / 4308. Retention hunks: only Part C pins at old 697 and 1530–1534; the Part A dict regions (86/36 keys) and the Part B set are untouched by the diff.
- `.ap` gitlink and submodule HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`; `.ap` worktree clean; `ap doctor` PASS (strict pin, managed block, governing variant `stable`); `ap project check --baseline` PASS; `runtime-info`: `.venv/bin/python`, CPython 3.13.9, `kronika` imported from this checkout's `src/kronika/__init__.py`. The envelope reported sanitized inherited environment classes (`SSH_AUTH_SOCK`, `VIRTUAL_ENV_DISABLE_PROMPT`, `PATH`) without exposing values.
- Local `refs/remotes/origin/main` = `b8ec042b5bf1835df77c81341abc75e9cf8ab059`; **public branch state not directly observed** (no network authority). The candidate is local and unpublished by design.
- The removed decode-and-reinsert statement existed at parent blob line 4309 (`return command.replace(match.group(1), original, 1)`, with decode at 4296 and classification at 4301). The candidate source contains none of these; exactly one `return command` remains (the frozen/foreign byte-identity return in the revision branch).
- `_render_moved_revision_token` exists at candidate line 4255 with the claimed contract (render only from raw; refuse unprovable forms). `_unescape_unit_text` has no write-back site: two read-only extraction sites (1696, 1904), the renderer segment check (4294), the reparse guard comparison (4368), and the decode at 4348 used only for classification and `transform_path_value`.
- Constants parent==candidate: `MIGRATION_OLD_TO_NEW_ROOTS`, `MIGRATION_FROZEN_PATH_PREFIXES`, `MIGRATION_SEGMENT_RENAMES`, `SYSTEMD_EXEC_TOKEN.pattern`, `UNIT_EXEC_PATH.pattern`, `SYSTEMD_EXEC_PREFIXES`, `SYSTEMD_PATH_DIRECTIVES`, `SYSTEMD_IDENTITY_DIRECTIVES`, `SYSTEMD_EXEC_DIRECTIVES`, `EXIT_MIGRATION == 27`.
- Ten shared refusal cases (near-miss revision/plain/path-list/credential; leftover revision/plain/path-list/credential; non-absolute revision; identity `User`) produce identical message and exit 27 in parent and candidate.
- Session 36's prerequisite stop performed no review work; it is not evidence about the candidate.

#### 2. B1-fixed evidence (candidate; parent from read-only `git show`)

All through `transform_unit_dropin_text`, then `UNIT_EXEC_PATH` + `_unescape_unit_text` with the engine's own parser.

| Case | Candidate | Parent |
|---|---|---|
| Frozen `\x20` token `/opt/framenest/tooling/audit37\x20tool` | Drop-in byte-identical; capture == raw; executable `/opt/framenest/tooling/audit37 tool`; classified `frozen` | Output drops `\x20`; capture truncates to `/opt/framenest/tooling/audit37` |
| Foreign `\x20` token `/srv/audit37/framenest\x20assets` | Byte-identical; capture == raw; executable `/srv/audit37/framenest assets` | Output drops `\x20`; capture `/srv/audit37/framenest` |
| Moved `/var/lib/framenest/catalog\x20data/framenest.env` | Capture `/var/lib/kronika/catalog\x20data/kronika.env` (`\x20` retained; renamed segment literal); executable `/var/lib/kronika/catalog data/kronika.env`; second pass unchanged | Inserted decoded text; capture truncates to `/var/lib/kronika/catalog` |
| Moved non-renamed escape `/var/lib/kronika/ksi37\x2edb` | Remainder carried verbatim; executable `.../ksi37.db`; idempotent | — |

Eleven-rendition remainder corpus (exact root, trailing slash, `\x2e`, `\x20`, `\x3b`, `\x7d`, double slash, escape at end, `\t`, `\\`) is carried verbatim under the new root (`out_capture == "/var/lib/kronika" + raw_remainder`) and idempotent. The splice targets the parser match span: with the same token text inside `argv[]`, only the `path=` field is rewritten and the argument text stays byte-identical.

#### 3. Regression matrix across the site shapes

Independent fixtures, all four site shapes (path-list `ReadWritePaths`, `LoadCredential`, plain `Exec*`, revision `{ path=… }`):

| Category | Cases | Result |
|---|---:|---|
| Frozen (incl. escaped) | 5 tokens × 4 sites = 20 | Output byte-equal |
| Foreign (incl. escaped) | 5 × 4 = 20 cases in the preserved set | Output byte-equal |
| Moved (roots, renamed segments, exact root) | 7 × 4 = 28 | Exact expected text; second pass unchanged |
| Near-miss (incl. escaped `\x2d`) | 4 × 4 = 16 | Exit 27 with unchanged messages |
| Under-root leftover (incl. escaped) | 4 × 4 = 16 | Exit 27, `path value under a moved root is not classifiable` |

Plus: rule-order classification; escaped near-miss (`unit directive ExecStart path is not classifiable`) and escaped leftover revision refusals; the four unprovable raw forms (escaped root, escaped slash in remainder, escaped slash at root boundary, escaped renamed segment) all fail closed with `unit directive ExecStart revision path is not provably transformable`, exit 27; all six `Exec*` directive names share the repaired branch; spacing-free `{path=…}` form; renderer's direct defensive refusals (`pair is None`, segment mismatch). The audit suite passes 123 tests; the mutation suite passes 4 (127 total). `git diff --check` is clean.

#### 4. The LEAD probe results

| Probe (all synthetic) | Sibling sites (plain/path-list/credential) | Revision site | Parent comparison |
|---|---|---|---|
| `\x2f` inside remainder `/var/lib/framenest/catalog\x2fdata` | Root moved, escape retained (`/var/lib/kronika/catalog\x2fdata`; runtime `/var/lib/kronika/catalog/data`) — a correct transform, not fail-closed | Fails closed `…not provably transformable` | Parent identical at siblings; parent silently inserted decoded text at the revision site |
| `\x2f` at root boundary `/var/lib/framenest\x2fksi37` | Near-miss refusal, exit 27 | Fails closed (unprovable) | Parent identical at siblings; parent rewrote to `/var/lib/kronika/ksi37` |
| Escaped root character `/var/lib/framenes\x74/ksi37.db` | Raw classifies `foreign`, decoded is `moved`; **preserved silently** (runtime still names the retired root) | Fails closed (unprovable) | Parent identical at siblings |
| Escaped renamed segment `/etc/framenest/frame\x6eest.env` | Root rewritten, escaped segment retained → `/etc/kronika/frame\x6eest.env` (runtime `/etc/kronika/framenest.env`) — not fail-closed | Fails closed (unprovable) | Parent identical at siblings |
| `\x20` inside moved remainder | All four sites keep the escape; revision reparse equals the escaped-space executable | Accepted, correct | Parent same except the revision branch |

Boundary note: a malformed `\x` escape (`\xzz`) raises `ValueError` (not `ReleaseError`) in both parent and candidate; `main()` catches only `ReleaseError`. Pre-existing, identical, still a stop.

#### 5. Mutation-probe results (in-memory; anchor counts asserted == 1; repository untouched)

| Mutation | Property test | Observed outcome |
|---|---|---|
| m1: restore `return command.replace(raw_token, decoded, 1)` at the frozen/foreign return | Frozen/foreign revision byte identity | Detected: output changed, `\x20` gone, capture truncates to `/opt/framenest/tooling/audit37` (and `/srv/audit37/framenest`) |
| m2: emit decoded remainder (`rewritten.append(decoded_segment)`) | Moved escaped reparse + guard | Detected: `ReleaseError: unit directive ExecStart revision path is not provably transformable`, exit 27 (reparse-guard first condition) |
| m3: delete the byte-identity `return command` | Frozen/foreign byte identity | Detected: falls into the plain branch, `ReleaseError: unit directive ExecStart path is not absolute`, exit 27 |
| — | Unmutated candidate sanity | Passed: candidate satisfies all three properties |

No mutation survived; a surviving mutation would have been a finding.

#### 6. Focused and full-suite check results, and Part A/Part B evidence

| Check | Result | Declared | Difference |
|---|---|---|---|
| Focused `test_kronika_identity_migration.py` | 203 passed, 1.04 s | 203 | none |
| `test_kronika_identity_retention.py` | 15 passed, 0.36 s | 15 | none |
| Full declared Python suite (`--operation test`) | **4873 passed, 8 skipped, 3 warnings, 0 failed**, 680.51 s | 4873/8/3/0 | **none** |
| Audit probes | 123 + 4 passed | — | audit evidence |

The 8 skips are five cover-workflow real-tool cases, two media-analysis real-tool cases and one live NVIDIA NIM case; the 3 warnings are Pydantic `PydanticJsonSchemaWarning` non-serializable-default warnings. Part A: `FROZEN_DOCUMENT_SHA256` = **86** keys (counted) and `FROZEN_ALEMBIC_SHA256` = **36** keys (counted); byte-invariance and set-completeness tests passed and the commit touches no frozen path. Part B: `EXPECTED_FRAMENEST_BASENAME_PATHS` = **20** entries (counted); the ledger test passed. Part C movement (+11 tests, +3/+1/+3 host paths) is exactly the two retention hunks; both occurrence-count tests passed at the candidate.

#### 7. Findings with blocking/non-blocking disposition and every untested site

**Blocking: none.** B1 is fixed; the correction matrix, messages and exit codes are intact; the three mutations die; the suite is exactly as declared.

Non-blocking residuals:

- **R1 (pre-existing, parent-identical):** an escaped root character or escaped renamed segment at the plain-`Exec*`/path-list/`LoadCredential` sites is preserved or partially rewritten without refusal (section 4). The repair neither introduces nor closes it; a live unit carrying such a spelling would survive preflight yet name the retired layout at runtime.
- **R2 (new, intended, fail-closed):** unprovable moved revision raw forms now stop with exit 27 instead of the parent's silent decode-insert. If the host carries such a token, the preflight stops safely.
- **R3 (known, mandated residual):** the unchanged sudoers-command guard remains a fail-closed host risk for the next preflight; not this repair's defect.
- **R4 (pre-existing):** malformed-hex escapes raise `ValueError` rather than a classified refusal; parent-identical.
- **R5:** accepted deviations from the correction audit remain in force (Exec argument opacity; relative/foreign `LoadCredential` preservation).

Untested sites (report 35 §7 checked, all five claims accurate): repo fixtures use only `ExecStart` (audit exercised all six directive names); the renderer's `pair is None` refusal is unreachable in production (direct call exercised it); the per-segment unescape mismatch is unreachable when segment counts match because `decoded = unescape(raw)` and only `\x2f`-class escapes change the count (direct call exercised it; defensive); the reparse guard's refusal has no permanent fixture (re-demonstrated by m2); `framenest`/`framenest.sock` lack separate revision fixtures (audit matrix covers both). Untested by this audit: live host inventory; malformed multi-`path=` revision forms; `\n`/`\r` simple escapes (same path as the tested `\t`); no live systemd interpretation. The B1 design assumption (decoded token inserted without restoring escaping) does not survive the repair, so the escalation condition is not triggered.

#### 8. Deviations, risks, missing evidence, and one smallest next step

No deviation from the grant. Risks and missing evidence: public branch state not directly observed; host inventory unverified; the residuals above. Command accounting: read-only Git inspection; `ap doctor` / `ap project check` / authorized `ap exec` operations; text inspection (`ls`, `wc`, `grep`, `awk`, `sed`, `tail`, `tr`); one `git show` copy and probe files under the isolated temp area — all mentioned commands mutated nothing outside it. Final state: HEAD unchanged, repository clean, `.ap` clean at the pin. The full suite wrote only to the pre-existing, git-ignored `.pytest_cache/`.

Smallest next step: the Orchestrator may re-run the `migrate-identity preflight` under its own grant; this re-audit, with the earlier `C6-V` result, no longer blocks it.

#### Resolved Execution Issues / Near-Misses

1. Probe-construction near-miss: my first LEAD probe expected near-miss refusals for an escaped slash inside the remainder at sibling sites; the correct, observed behavior is a successful root move with the escape retained. The expectation was corrected, the probe rerun green (123 passed), and the observed behavior is reported as evidence in section 4.
2. One compound inspection command exited 1 only because its trailing `grep -c` found zero matches while the full suite was still running; no task impact.
3. Cleanup: removal of `/tmp/opencode/ksi37-audit.C6ENC/` was attempted with the exact owned path and was denied by the execution environment. Per the prompt's "removed or reported" rule the state is retained and reported: `probe_c6enc_revision.py`, `probe_c6enc_mutations.py` (synthetic fixtures only), `parent_engine.py` (a `git show` copy of a committed blob) and `full_suite.log`; no secrets and no project state.

#### Pre-Existing Failure Classification

none. No repository test failed in any baseline-bound run; nothing was classified as a pre-existing failure. The `ValueError` boundary and sibling-site escape behaviors are parent-identical characteristics recorded as residual observations in section 7, not dismissed failures.

Authority under this prompt expires on submission of this terminal report.

```text
Orchestration critique:
MEASURED: The sibling-site escaped-form gap is now evidenced rather than asserted: escaped root character (`/var/lib/framenes\x74/…`) or escaped renamed segment (`frame\x6eest.env`) tokens are preserved or partially rewritten without refusal at the plain-Exec*, path-list and LoadCredential sites, identically in parent and candidate. Evidence: audit probes test_lead_escaped_root_character_evades_sibling_classification and test_lead_escaped_renamed_segment_sibling_partial_rewrite; 127 audit tests passed. Effect: a live unit carrying such a spelling would pass preflight while still naming the retired layout at runtime. Smallest correction: none inside this repair; keep it as a host-preflight residual, address only under a future bounded grant if completeness is wanted.
LEAD: Whether any effective NUC unit or drop-in actually contains an escaped spelling of a moved root, a retired segment, or an unprovable revision-form token that now fails closed. Cheapest useful check: in the next authorized preflight/preparation window, list effective unit directive tokens containing a backslash and classify their decoded forms before apply.
```