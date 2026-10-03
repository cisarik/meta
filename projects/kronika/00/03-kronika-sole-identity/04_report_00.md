### Report for ORCHESTRATOR_CHAT

My client's native planning surface forces a level-1 title above the required header; the standard header is the next line.

Logical whole identity: `kronika-sole-identity`
Worker session ordinal: `04`
Worker exchange ordinal: `01`
Persistent role identity: WORKER
Worker session profile: Fresh Implementation Worker
Task identity: `KSI-IMPL-C0`
Branch: `docs/adr-0085-kronika-sole-identity`
Commit: `18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`
Parent: `ca649f6eb6231591292e174dff994fd0f4448378`
Report justification: `new-mutation`
Phase-qualified result: `not-applicable`
Logical-whole closure: `not-closed`
NUC contact: none in this cut, by design
Published NUC state: unchanged

## Status: PASS

Cut C0 is complete. One commit, exactly seven paths, both suites green, tree clean, not pushed.

## Repository gate (re-verified, and again after the PC suspend)

Branch `main`, HEAD `ca649f6eb6231591292e174dff994fd0f4448378`, clean tree, `origin` `https://github.com/cisarik/kronika`, public `refs/heads/main` equal to that SHA, `.ap` gitlink and submodule HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `ap doctor: PASS` (governing variant `stable`), `ap project check --baseline ca649f6…: PASS`. The `WARN sanitized inherited environment classes` line is the known non-failing environment notice.

After the commit: `./.ap/ap project check --root /home/agile/Projects/kronika --baseline 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672` → **PASS**.

## Full diff of all seven paths

`AGENTS.md`, `SPEC.md`, `DEVELOPMENT.md`, `ROADMAP.md`, `docs/adr/README.md` diffs were shown in full above and are exactly the five enumerated sentence replacements plus the index row and supersession paragraph. `docs/adr/0085-kronika-sole-identity.md` is new (full text below). `tests/contract/test_kronika_identity_retention.py` is new, 434 lines.

The AGENTS.md diff verbatim:

```
-system, family library or Git history. Do not perform a mass branding
-replacement.
+system, family library or Git history. ADR-0085 is the sole-identity authority;
+it is implemented as an ordered sequence of bounded cuts, not as a mass
+branding replacement.
 
-The internal `framenest` package, migration history, compatible HTTP headers
-and deployment identifiers remain. The S4-A through S10 sequence in
+ADR-0085 is the sole-identity authority; the ordered identity cuts implement it.
+The S4-A through S10 sequence in
```

SPEC.md, DEVELOPMENT.md and ROADMAP.md each replace their single enumerated sentence and preserve the neighbouring constraints, including "The existing release helper remains the only deployment system", "Do not port a second manager, account system, family library or Git history", and the ordered-cut-sequence-not-mass-replacement requirement.

## Protected-file confirmation

`git diff --stat HEAD^ HEAD` over ADR-0082, ADR-0083, ADR-0084, `README.md`, `PRODUCT.md`, `SERVER.md`, `SECURITY.md`, `docs/FEDORA_SERVICE.md`, and additionally `src/`, `deploy/`, `scripts/`, `extension/`, `pyproject.toml`, `ap.project.conf` returned **empty output** for every one of them.

The AGENTS.md managed AP integration block is **byte-identical**: extracting lines between the `BEGIN`/`END` markers from `HEAD^` and `HEAD` and diffing yields no difference. Note that the block now begins at line 34 and ends at line 52 rather than 33-51, because the sentence replacement above it added one line. No line inside the block was touched; only its line offset moved.

## ADR-0085

Present at `docs/adr/0085-kronika-sole-identity.md`, status `Accepted`, decision date `2026-10-02`. It records the sole identity (`kronika` package at `src/kronika`, distribution `kronika`, `provenanceModule` `kronika`, `kronika-*` console scripts, `./kronika` launcher), the `KRONIKA_` settings prefix and `X-Kronika-Request: 1` header, the full web host layout, the sole `deploy/ubuntu/kronika-release` entry, the byte-stable Alembic bytes through `0035` with the process-local `sys.modules` alias as the only loader mechanism, the named frozen residues (both tooling paths, `FNCBE01`, `framenest-chatgpt-page`, `/mnt/framenest-catalog-offdevice`, historical ADR bodies, `docs/FEDORA_SERVICE.md`, `docs/NUC_HOST_BASELINE.md`, existing archives and sidecars), the ordered-cuts-not-mass-replacement rule, and an explicit non-grants section. The Supersession section cites exactly the three ADR-0082 passages (lines 87-89, 208-209, and line 196 with its precise non-supersession carve-outs) and never edits that file. The Boundaries section restates the inherited one-repository rule, `cisarik/cli_chatgpt` at `66c40d43…`, the parked capture constraints, frozen Gallery, administrator-curated Timeline, owner-private records with administrator read, household publication by approval only, internet publication off, the ADR-0083/0084 provider boundary with research disabled by default, loopback-first with Tailscale-only ingress, and the single release helper.

## Part B measured path set

Measured 20 paths, matching the Orchestrator's 20 listed paths **exactly**, character for character. The full set is in the report's prompt and is pinned verbatim in the test.

**Discrepancy I did not silently absorb.** The prompt says "The Orchestrator-measured set, 23 paths", then lists 20 and itself says "That is 20. Ten more paths live under `src/framenest/`". I enumerated the full set myself from `git ls-files`:

- The strict measure "tracked path whose basename contains `framenest`, case-insensitively" yields exactly **20**.
- **Zero** files under `src/framenest/` have `framenest` in their own basename. `src/framenest` is one directory that moves as a unit in C3, which the prompt itself acknowledges ("one renamed directory and not a set of individual filenames"). So there is no set of 10 additional individual paths, and there is no set of 3.

The "23" and the "ten more paths" are inconsistent with both the strict definition and the measured tree. The 20 listed paths are complete and correct under the definition the prompt gives, so I pinned 20 and made no silent adjustment. The directory-move itself is covered by Part A's Alembic set-completeness test and by C3's own enumeration.

## Part C measured table and deltas

Every Orchestrator value reproduced exactly at the verified baseline: `FRAMENEST_[A-Z0-9_]+` 637, distinct 102, bare 2, `X-FrameNest-Request` 53/28, `/opt/framenest` 198, `/etc/framenest` 73, `/var/lib/framenest` 91, `/var/cache/framenest` 20, `/mnt/framenest-catalog-offdevice` 12, `User=framenest`/`Group=framenest` 5/5, capitalized `FrameNest` 3335/478, per-tree src/tests/deploy/scripts/docs/extension 254/314/19/7/87/12, `framenest-*` console scripts 14.

Deltas after my edits, all caused by ADR-0085's own cited historical text, all pinned at post-edit values:

| Measure | Baseline | Pinned | Cause |
|---|---:|---:|---|
| `/opt/framenest` | 198 | **200** | ADR-0085 cites the two tooling paths `/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry` and `/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13` |
| `/mnt/framenest-catalog-offdevice` | 12 | **13** | ADR-0085 names it as a frozen residue |
| docs-tree files matching `-i framenest` | 87 | **88** | the new ADR-0085 file |
| all other Part C measures | — | unchanged | ADR-0085 adds no `FRAMENEST_` token, no header, no capitalized `FrameNest`, no console script |

The new ADR contains `framenest` 13 times as cited historical text, exactly as the prompt anticipated.

I also pinned two **new** per-tree occurrence measures that the prompt's table did not contain, because of Orchestrator finding 4: `src` 2975, `tests` 4223, `deploy` 218, `scripts` 104, `docs` 1216, `extension` 199. Their purpose is explained below.

## Test structure, and how each part fails on a deliberate mutation

14 tests, no skip, no xfail, no `pytest.mark`, no disable. File-counting uses `git ls-files` by subprocess, following the existing convention in `tests/contract/test_ap_integration.py`. Binary files are skipped exactly as `git grep -I` does.

**Part A, 4 tests.** Pins 122 frozen blobs: 84 ADR bodies `0001`–`0084`, `docs/FEDORA_SERVICE.md`, `docs/NUC_HOST_BASELINE.md`, and all 36 Alembic version files. Two tests verify the pinned hashes; two verify the pin *set* is still complete, so adding an unpinned ADR `0086` or a new migration fails too. Alembic entries are keyed by **filename only** and the versions directory is resolved by glob `src/*/infrastructure/persistence/alembic_environment/versions`, so C3 can move the directory path without breaking the byte pins — which is precisely the "a path move is allowed to change a path, never these bytes" requirement.

- Mutation A1, appended one comment line to `docs/adr/0001-supported-python-version.md`: `test_frozen_adr_and_host_document_bytes_are_unchanged` failed, 1 failed / 12 passed.
- Mutation A2, appended one line to `versions/0035_research_requests_and_accounting.py`: `test_frozen_alembic_revision_bytes_are_unchanged` failed, 1 failed / 13 passed.

**Part B, 1 test.** Compares the measured tracked-basename set against the pinned literal `frozenset`. The expected set is a literal in the test file; it is never recomputed from the tree.

- Mutation B, perturbed one pinned entry: `test_framenest_basename_path_ledger_matches_exactly` failed and named both sides: `unexpected=['deploy/systemd/framenest.env.example'] missing=['deploy/systemd/DELIBERATE-MUTATION-probe.conf']`.

**Part C, 9 tests.** Env-prefix token/distinct/bare counts, mutation-header occurrences and files, five host paths, `User=`/`Group=`, capitalized occurrences and files, per-tree file counts, per-tree occurrence counts, console-script entries.

- Mutation C1, appended `# framenest deliberate probe` to `deploy/ubuntu/fn-production-env-deploy`, the finding-4 file whose **filename is clean**: `test_per_tree_framenest_occurrence_counts_match` failed with `{'deploy': 219} != {'deploy': 218}`.
- Mutation C2, appended a line with `FRAMENEST_PROBE_KEY=1`, `/opt/framenest/probe` and `X-FrameNest-Request: 1` to `deploy/systemd/framenest.env.example`: 5 tests failed independently — per-tree occurrences, env-prefix tokens, mutation header, host paths, capitalized occurrences.

Every deliberate mutation was reverted with `git show HEAD:<path>` and each affected path confirmed `CLEAN` by `git diff --quiet` before the final run.

**Why the extra occurrence ledger exists.** My first Part C implementation used only per-tree *file* counts, matching the Orchestrator's table literally. Mutation C1 then **did not fail**: `fn-production-env-deploy` already contains `framenest`, so its file count was already 1 and a content-only change was invisible. This is precisely the finding-4 failure mode, and the Orchestrator's table alone does not detect it. I added per-tree **occurrence** counts, which do detect it, and re-verified. This is a measured finding, not an assumption.

One design point worth flagging: the ledger file necessarily contains the tokens it pins, so it excludes itself from all Part C counting via `_SELF_RELATIVE_PATH`. Without that, its own literals would inflate every count and later cuts could not compute an honest delta. This is documented in the module docstring and in the helper.

The question-12 living-prose `\bframenest\b` scan is **not** implemented, per instruction. The intent to arm it at C7 is recorded in the module docstring only; there is no disabled or skipped placeholder test.

## Test counts

| Route | Baseline | Final | Delta |
|---|---|---|---|
| Python `--operation test` | 4145 passed, 8 skipped, 3 warnings, 0 failed (658.13s) | **4159 passed, 8 skipped, 3 warnings, 0 failed** (658.41s) | **+14 passed**, skips unchanged at 8 |
| JavaScript `node --test tests/*.test.js` | 554 total, 549 passed, 0 failed, 5 skipped | 554 total, 549 passed, 0 failed, 5 skipped | none |

The delta is exactly my 14 new tests and nothing else. The new file also passes against the new commit baseline `18c357c…`: 14 passed, 0.27s.

## Git

Branch `docs/adr-0085-kronika-sole-identity`, one commit `18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`, subject `docs: record the Kronika sole identity in ADR-0085`, parent `ca649f6eb6231591292e174dff994fd0f4448378`. `git status --porcelain` listed exactly the seven paths before staging and is empty after. `git ls-remote origin refs/heads/docs/adr-0085-kronika-sole-identity` returns nothing: **not pushed**. No tag, merge, rebase, or history rewrite.

## Commands outside the declared routes

Two, both read-only, both mutating nothing, both disclosed here as required:

- `sha256sum <122 frozen paths>` to compute the Part A pin values. Purpose: compute SHA-256 for files that have no existing pinned hash.
- `git show HEAD:<path>` to restore four files after the deliberate mutation tests. Read-only Git inspection, explicitly allowed.

No Python was invoked outside `./.ap/ap exec`. No `git mv`, `rm`, `checkout --`, or any other mutating Git command was used; the forbidden-command policy also blocked my first attempt to rename a file for mutation B, so I verified Part B by perturbing the pinned literal instead, which tests the same assertion.

## Deviations, risks, missing evidence

- The Part B "23 paths" / "ten more paths" prose does not match the tree. Reported above, not absorbed. The pinned set of 20 is correct under the prompt's own definition and matches its 20 listed paths exactly.
- Part C required two measures the prompt's table did not contain: per-tree occurrence counts (to close finding 4), and the post-edit deltas for ADR-0085's own text. Both stated above.
- The managed AP block's line range moved from 33-51 to 34-52. Content byte-identical; verified by marker extraction and diff.
- Not verified, by design and out of authority: that ADR-0085's normative content matches the Cooperator's intent beyond the accepted plan; any NUC-side consequence; any later cut's delta arithmetic.
- The C0 branch is unpublished. C1 needs its own grant.

## Resolved Execution Issues / Near-Misses

1. `git ls-files` reports the `.ap` submodule as a directory path, which made seven Part C tests die with `IsADirectoryError`. Fixed by filtering `_tracked_paths` to regular files, which also matches `git grep`'s non-descent into submodules.
2. `_decoded_texts` skips binaries, so it cannot be zipped 1:1 against the path list; `ValueError: zip() argument 2 is shorter than argument 1`. Fixed by introducing `_decoded_pairs` returning `(path, text)` tuples.
3. ADR-0085 was untracked when Part C first ran, so `git ls-files` could not see its delta and the counts came out at baseline values. Resolved by staging the new files, which is within Git authority; the pins are post-edit values.
4. `EXPECTED_FRAMENEST_BASENAME_PATHS` was lost during shell assembly of the test file because an intermediate fragment was a stub I later overwrote. Caught by a grep assertion before the first run, then inserted with the edit tool.
5. The first Part C design did not detect the finding-4 case. Measured, fixed, re-verified. This is the substantive one.

## Pre-Existing Failure Classification

none. The 8 Python skips (7 real-media-tool, 1 live NVIDIA) and 5 JavaScript skips (gated browser-evidence suites) are identical before and after this cut and are pre-existing environment gates, not failures.

## Smallest next step

Orchestrator verifies this diff, the 122 hashes and the Part B/C pins, then issues the C1 grant for the dual-read `lookup_env` resolver. Do not publish or proceed to C1 on this report alone.

Orchestration critique:
MEASURED: the Orchestrator's Part B table is internally inconsistent — it states "23 paths", lists 20, and asserts "ten more paths live under `src/framenest/`", but zero files there have `framenest` in their basename; evidence: `git ls-files 'src/framenest/**'` filtered on basename returns 0 rows, and the strict basename measure returns exactly the 20 listed paths; effect: a Worker following the "23" figure literally would have to invent 3 paths or stop spuriously, and the path-name ledger's whole purpose is to be unambiguous; smallest correction: restate Part B as the 20 enumerated paths and state that the `src/framenest` → `src/kronika` directory move is governed by C3's own enumeration, since it is one directory rename and not a set of filenames.
LEAD: none.