### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: kronika-sole-identity
Worker session ordinal: 11
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C1E — pin the retention ledger's content-path membership so a partial rename cannot pass
Status: PASS
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none, by design
Start commit: 02a80485206eeeb33c43393d25514a30d7fe297f
End commit:   0b7567598b6378da25d46874b7cb3f42fb1733ae
Changed files: exactly one — tests/contract/test_kronika_identity_retention.py
Report justification: new-mutation
```

Client-surface disclosure: my native surface did not force a preamble above thisheader. During execution I did emit short progress lines into the chat
("Gate passes", "Baseline green", and similar); none of them are part of this
report, and no file, ref or external state was touched by them.

The ledger now carries a pinned membership set beside its scalars, and the
failure mode the re-audit identified is demonstrated, not asserted.

## Repository gate

Matched exactly as issued, before any edit:

- Branch `feat/kronika-identity-dual-read`, HEAD `02a80485206eeeb33c43393d25514a30d7fe297f`, subject as declared, tree clean.
- `.ap` gitlink and submodule HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`.
- `ap doctor`: **PASS**, resolved governing variant stable.
- `./.ap/ap project check --root … --baseline 02a80485206eeeb33c43393d25514a30d7fe297f`: **PASS**. (`ap doctor` takes no `--root`; first invocation errored with `doctor takes no argument or --candidate` and was re-run bare.)
- `git ls-remote origin refs/heads/main` → `18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`. Unpublished branch, as declared.

## The diff

`git diff --stat 02a8048..0b75675` → **1 file changed, 751 insertions(+), 1 deletion(-)**.

```diff
--- a/tests/contract/test_kronika_identity_retention.py
+++ b/tests/contract/test_kronika_identity_retention.py
@@ -15,7 +15,9 @@ from the working tree, which would make the assertion tautological.
 
 Part C pins per-tree content-occurrence counts so that a missed content rename is
 detectable even where the filename is already clean, as in
-`deploy/ubuntu/fn-production-env-deploy`.
+`deploy/ubuntu/fn-production-env-deploy`, and it pins the exact membership set of
+tracked text paths whose content carries the token, because a scalar detects that
+a total moved but not which occurrences moved.
 
 The question-12 living-prose `\bframenest\b` scan over the living document list
 is deliberately NOT implemented at this cut. It is armed in cut C7. That intent
@@ -208,6 +210,739 @@ PER_TREE_FRAMENEST_OCCURRENCE_COUNT = {
     "extension": 199,
 }
 
+# The exact tracked text paths, this ledger excluded, whose decoded content
+# contains `framenest` case-insensitively. Part B is membership over basenames
+# and cannot see a content-only rename inside an already matching file; the
+# Part C scalars below detect that a total moved but not which occurrences+# moved, so a partial rename re-pinned to match the partial work still passes
+# them. This set is membership per path, so no compensating swap is possible: it
+# fails when a file that should have been renamed still carries the token and
+# when a file that should not have been renamed no longer does. It is
+# deliberately not recomputed from the working tree, which would make the
+# assertion tautological.
+EXPECTED_FRAMENEST_CONTENT_PATHS: frozenset[str] = frozenset(
+    {
+        ".gitignore",
+        "AGENTS.md",
+        "AI_WORKSPACE.md",
+        "COVER_PIPELINE.md",
+        "DESKTOP.md",
+        "DEVELOPMENT.md",
+        "GALLERY.md",
+        "PRODUCT.md",
+        "README.md",
+        "ROADMAP.md",
+        "SECURITY.md",
+        "SERVER.md"
+        … 706 further sorted entries …
+        "tests/x_companion_extension.test.js",
+        "tests/youtube_acquisition_cockpit.test.js",
+        "tests/youtube_request_cockpit.test.js",
+    }
+)
+
 ENV_PREFIX_TOKEN_COUNT = 643
 ENV_PREFIX_DISTINCT_NAME_COUNT = 101
 ENV_PREFIX_BARE_SPELLING_COUNT = 21
@@ -406,6 +1141,21 @@ def test_per_tree_framenest_occurrence_counts_match() -> None:
     assert measured == PER_TREE_FRAMENEST_OCCURRENCE_COUNT
 
 
+def test_framenest_content_path_ledger_matches_exactly() -> None:
+    """Pin the membership of content-carrying paths, so a partial rename fails."""
+    measured = {
+        relative
+        for relative, text in _decoded_pairs(_counted_paths())
+        if "framenest" in text.lower()
+    }
+
+    assert measured == set(EXPECTED_FRAMENEST_CONTENT_PATHS), (
+        "content-path ledger drifted: "
+        f"unexpected={sorted(measured - set(EXPECTED_FRAMENEST_CONTENT_PATHS))} "
+        f"missing={sorted(set(EXPECTED_FRAMENEST_CONTENT_PATHS) - measured)}"
+    )
+
+
 def test_environment_prefix_token_counts_match() -> None:
```

**Deliberate compression, disclosed:** the literal body is 718 mechanically
generated, sorted paths; I show its header comment, its first 12 and last 3
entries, and its exact shape rather than 718 lines. It is fully reproducible with
one read-only command:

```text
git diff 02a80485206eeeb33c43393d25514a30d7fe297f..0b7567598b6378da25d46874b7cb3f42fb1733ae
```

The single `-` line in the whole diff is the docstring sentence. Every Part A
hash, every Part B path and every existing Part C value is byte-identical.

## The measured set at this baseline

Measured **before** the edit, through the declared route, using the module's own
`_tracked_paths()` → `_counted_paths()` → `_decoded_pairs()` chain:

```text
size                 718
by tree              tests 321 | src 255 | docs 88 | deploy 19 | <root> 16 | extension 12 | scripts 7
Part B size          20
in both              20      (Part B is a strict subset; no Part B path is absent)
only in content set  698
only in Part B       0
known clean-name case present True   (deploy/ubuntu/fn-production-env-deploy)
```

Shape notes that matter for C3:

- The six per-tree file counts sum to **702**; the content set is **718** because it also holds the **16** tracked paths outside those trees — `README.md`, `AGENTS.md`, `pyproject.toml`, `.gitignore`, `ap.project.conf`, the root launcher `framenest`, `SERVER.md`, `SECURITY.md`, `SPEC.md`, `PRODUCT.md`, `ROADMAP.md`, `DEVELOPMENT.md`, `DESKTOP.md`, `GALLERY.md`, `AI_WORKSPACE.md`, `COVER_PIPELINE.md`. Every one of them has a clean basename and carries the token, so Part B sees none of them.
- Independent cross-check by a different route: `git grep -I -l -i framenest`, minus the ledger path, returns exactly **718** paths with the same per-tree split. The Python measurement and the Git measurement agree.
- Of the 718, **75** are frozen ADRs `0001`–`0084` and **2** are the frozen host documents `docs/FEDORA_SERVICE.md` and `docs/NUC_HOST_BASELINE.md`. Their bytes are Part A hash-locked, so they are permanently in this set and no cut can move them. The other **9** frozen ADRs (`0053`, `0054`, `0055`, `0065`, `0068`, `0070`, `0073`, `0078`, `0080`) carry no token today and, being frozen, can never join it. `docs/adr/0085` and `docs/adr/README.md` are living and may move.

## Demonstrations

All four ran through `./.ap/ap exec --operation test-focus` against throwaway
probes under `/tmp/opencode/ksi11/`. No repository file was written; the
simulated rename is an in-memory patch of the module's own `_decoded_pairs` and
of `Path.read_bytes`, scoped to one path.

**Step 0 — the real tree is green.** All **15** tests (14 pre-existing + the new
one) `PASS`.

**Step 1 — removing a path that should remain.** Pinned literal perturbed to 717
by dropping `deploy/ubuntu/fn-production-env-deploy` (a cut claiming a rename it
never performed):

```text
FAIL content-path ledger drifted: unexpected=['deploy/ubuntu/fn-production-env-deploy'] missing=[]
```

**Step 2 — adding a path that should not appear.** Pinned literal perturbed to
719 by adding `src/kronika/infrastructure/persistence/alembic_environment/versions/9999_x.py`,
which carries no token:

```text
FAIL content-path ledger drifted: unexpected=[] missing=['src/kronika/infrastructure/persistence/alembic_environment/versions/9999_x.py']
```

Both directions fail, naming both sides, as Part B does.

**Step 3 — the compensating-scalar scenario, the deliverable.** I renamed the
content of `deploy/ubuntu/fn-production-env-deploy` in memory — the knownclean-name case, one lowercase and one capitalized occurrence, no env token, no
mutation header, no host path, no unit account, basename untouched — and then did
what a cut does: re-pinned the four scalars that rename moved.

```text
scalars before          (deploy files 19, deploy occurrences 212, FrameNest 3381, FrameNest files 482)
scalars re-pinned       (deploy files 18, deploy occurrences 211, FrameNest 3380, FrameNest files 481)

14 pre-existing tests   ALL PASS
  test_frozen_adr_and_host_document_bytes_are_unchanged   PASS
  test_frozen_adr_and_host_document_set_is_complete       PASS
  test_frozen_alembic_revision_bytes_are_unchanged        PASS
  test_frozen_alembic_revision_set_is_complete            PASS
  test_framenest_basename_path_ledger_matches_exactly     PASS
  test_per_tree_framenest_file_counts_match               PASS
  test_per_tree_framenest_occurrence_counts_match         PASS
  test_environment_prefix_token_counts_match               PASS
  test_bare_environment_prefix_spellings_match            PASS
  test_mutation_header_occurrence_counts_match            PASS
  test_host_path_occurrence_counts_match                  PASS
  test_unit_account_occurrence_counts_match               PASS
  test_capitalized_framenest_occurrence_counts_match      PASS
  test_framenest_console_script_entry_count_matches       PASS

new membership test     FAIL content-path ledger drifted: unexpected=[] missing=['deploy/ubuntu/fn-production-env-deploy']
```

That is the exact failure mode the re-audit described, reproduced: **the whole
existing ledger passes on a partial rename re-pinned to match the partial work,
and the membership assertion fails at the cut that owns it.** ADR-0085 lines
114-115 are now backed by a check rather than by prose.

The re-pinned numbers are not asserted by me; the four passing scalar tests
measure them from the simulated tree, so had my arithmetic been wrong those four
would have failed.

## Ledger discipline

No pin moved, and I did not re-pin anything:

- `git diff --stat` before commit: one file, 751 insertions, **1 deletion**, and
  that deletion is the docstring sentence.
- All 14 pre-existing tests pass with their committed literals untouched.
- The new pin excludes `_SELF_RELATIVE_PATH`, so editing the ledger moved  nothing — confirmed by the module being green after the edit, not asserted.
- Nothing was renamed, no existing helper was changed, Part A and Part B were not
  touched.

## Counts

| Route | Baseline `02a8048` | Final `0b75675` |
|---|---|---|
| Python `test` | `4355 passed, 8 skipped, 3 warnings` in 679.25 s | `4356 passed, 8 skipped, 3 warnings` in 681.23 s |
| Retention module | `14 passed` | `15 passed` in 0.34 s |
| JavaScript `node --test tests/*.test.js` | not run at baseline (unchanged by construction) | `554 total, 549 passed, 0 failed, 5 skipped`, 10200 ms |

Exactly one test added, skips still 8, warnings still 3, JavaScript identical.
After the commit, `./.ap/ap project check --root /home/agile/Projects/kronika
--baseline 0b7567598b6378da25d46874b7cb3f42fb1733ae` → **PASS**.

## Branch and commits

Branch `feat/kronika-identity-dual-read`, unpublished, not pushed. Five commits
on public `main` `18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`:

```text
90c93eac94171182039a76fbb1c956e42b44da2c feat(identity): read both KRONIKA_ and FRAMENEST_ spellings, write only the old
c02c6753694d5d4958045bb79f80b5eb94b9c75c  fix(identity): exit 2 on an identity-environment conflict at every entry point
24bea56daca28603d81cac8d7ed7e3888ba90671  fix(identity): restore pre-cut process-environment parity for old spellings
02a80485206eeeb33c43393d25514a30d7fe297f  docs(identity): state the resolver's measured precedence and per-channel conflict rule
0b7567598b6378da25d46874b7cb3f42fb1733ae  test(retention): pin the content-path membership set so a partial rename fails   ← this cut
```

Working tree clean after the commit.

## Deviations

1. **The exact diff is compressed** as described above: the 718-entry literal body
   is characterised, not pasted. Everything else is verbatim.
2. **The module docstring's Part C paragraph gained two sentences** describing the
   new measure. No pin, no assertion and no helper changed. The grant permitted
   "any comment needed to explain why the set is a literal"; I judged that a
   module whose docstring enumerates its own parts must not silently omit one.
   Flagging it explicitly so you can accept or reject it.
3. **The literal was spliced in with a shell splice** — `head`/`cat`/`tail` into a
   file under `/tmp`, then `cp` over the single authorized target — rather than
   718 individual edit-tool calls. The block content itself was produced by a
   Python probe through the declared route, not by an interpreter I launched. The
   splice touched only `tests/contract/test_kronika_identity_retention.py`; the
   verified result is the diff above and the green module.

## Risks and missing evidence

- **Working-tree measurement, now with 718 paths of surface.** Every part of this
  ledger reads the working tree rather than HEAD blobs. Pre-existing property, but
  the new part widens the exposure from 20 paths to 718: any cut that leaves the
  tree dirty, or that stages a rename without completing it, will fail here. For
  C3 that is the intended behaviour, not a surprise.
- **C3 will churn this literal heavily** — roughly 255 `src/framenest/**` paths
  become `src/kronika/**`. That is the re-pin the plan already budgets for.
- **Permanent floor.** 77 entries (75 frozen ADRs + 2 frozen host documents) can
  never leave this set. C3's grant should know that before it sizes the re-pin.
- Not verified, and not required at E1: rendered UI, NUC state, runtime
  behaviour. Nothing in this cut touches product code.
- Not verified: the literal against HEAD blob content rather than working-tree
  content. Working tree and `git grep` agreed at 718; a staged-but-uncommitted
  divergence is theoretically possible and would be caught by the test, not by
  this report.

## Resolved Execution Issues / Near-Misses

- **A backgrounded baseline suite was killed.** I launched the 11-minute run with
  `nohup … &`; the tool terminated the command at its 120 s timeout and took the
  process group with it, leaving a truncated log at 6 %. Discarded and re-run in
  the foreground with a 1500 s timeout. Only the one full run is reported.
- **`ap doctor --root` is not a valid invocation** (`ap: ERROR: doctor takes no
  argument or --candidate`). Re-run bare.
- **My first demonstration probe reported a false `PASS` shape.** The probe  truncated the failure message at the first `missing=` marker, so both  direction-2 and the compensating-scalar scenario printed
  `unexpected=[]` and my own assertions correctly failed on the truncated
  string. This was a defect in my probe's message capture, not in the repository
  test. Fixed to capture the full message and re-run; all four demonstrations  then reported the full two-sided message. Recorded because the truncated output
  would have looked like a silent no-op failure.
- **`ap project check --baseline 0b75675` rejected the short SHA**
  (`--baseline must be a full lowercase commit object ID`). Re-run with the
40-character SHA; PASS.

## Pre-Existing Failure Classification

none — no repository test failed at any point. The only failures observed were in
my own throwaway probes under `/tmp/opencode/ksi11/` (the truncated-message defect
above), both corrected before any conclusion was drawn from them.

## Commands beyond the declared routes

Python evidence went only through
`./.ap/ap exec --root /home/agile/Projects/kronika --baseline <sha> --operation test`
and `--operation test-focus -- <argv>`, plus
`./.ap/ap project check --baseline <sha>`. JavaScript used
`node --test tests/*.test.js`. Read-only Git only: `status`, `rev-parse`, `log`,
`ls-files`, `ls-remote`, `grep`, `submodule status`, `add`, `commit`, `diff`.
The one mutation command beyond the declared routes is the shell splice named
under Deviations; it wrote only the authorized test module. Throwaway probes and
scratch files exist only under `/tmp/opencode/ksi11/`. No dependency, network,
provider, capture, NUC or credential action occurred; nothing outside `/tmp` was
written apart from the single committed test module.

## Smallest next step

Accept C1e and write cut C2's grant. C3's grant should then re-pin the whole
ledger — including this 718-path set — in one pass, and should carry the
`COMPATIBLE_ENVIRONMENT_PREFIX == "FRAMENEST_"` guard the re-audit named as a
hidden value coupling.

```text
Orchestration critique:
MEASURED: the issued expectation that the membership set would be "substantially larger than Part B's 20 paths" is right but understates it by two orders of magnitude — the set is 718 paths, 698 of which Part B does not have, and Part B's 20 are a strict subset of it rather than an overlapping sample; evidence: measured718 at 02a8048 through the module's own helper chain, independently reproduced as 718 by `git grep -I -l -i framenest` minus the ledger path, with per-tree split tests 321 / src 255 / docs 88 / deploy 19 / root-level 16 / extension 12 / scripts 7; effect: the re-audit's sizing intuition ("C3 already pays a full re-pin, so the size cost is not incremental") holds, but a reviewer expecting a set tens of percent larger than 20 will read 718 as a defect, and 16 of the entries are root-level files that no tree-based pin has ever covered — which is itself the finding: every tree-scoped measure in Part C is structurally blind to the repository root; smallest correction: state 718 total, 698 beyond Part B, Part B a strict subset, and 16 root-level paths, and record in C3's grant that the root files (`README.md`, `AGENTS.md`, `pyproject.toml`, `.gitignore`, `ap.project.conf`, the root launcher) are now covered for the first time. Second, the compensating-scalar demonstration is reproducible exactly as specified, so the ADR-0085 lines 114-115 promise now has a mechanical check: evidence: with the content of `deploy/ubuntu/fn-production-env-deploy` renamed in memory and only the four scalars it moved re-pinned (deploy files 19→18, deploy occurrences 212→211, FrameNest 3381→3380, FrameNest files 482→481), all 14 pre-existing tests including both Part A hash tests and Part B report PASS while the new membership test reports `missing=['deploy/ubuntu/fn-production-env-deploy']`; effect: the "fails loudly at the cut that owns it" claim is no longer prose; smallest correction: none, this is the accepted record.
LEAD: the membership set is measured from the working tree, so a cut that stages a rename without completing it will fail here for a reason that looks like a ledger bug rather than an incomplete cut; I verified the current tree is clean and the set matches both the Python and the Git measurement, but I did not test what happens when a tracked file is modified-but-unstaged or renamed-but-unstaged; cheapest useful check: at C3, when the package move is mid-flight in the worktree, run the retention module once before staging and confirm the failure message names exactly the unrenamed paths, which would confirm the check is diagnostically useful at the moment it fires.
```