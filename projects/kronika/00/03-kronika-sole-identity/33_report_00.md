All verification is complete. The terminal report follows.

---

### Report for ORCHESTRATOR_CHAT

| Field | Value |
|---|---|
| Logical whole identity | `kronika-sole-identity` |
| Worker session ordinal | `33` |
| Worker exchange ordinal | `01` |
| Task identity | `KSI-CORR-C6GUARD` |
| Persistent role | `WORKER` |
| Status | **PASS** |
| Report justification | `new-mutation` |
| Phase-qualified result | `not-applicable` |
| Logical-whole closure | `not-closed` |
| NUC contact | `none` |
| Start commit | `b8ec042b5bf1835df77c81341abc75e9cf8ab059` |
| Commit | `cf76f0b3a391663db7f4b0c88b872c08b69ff279` (`fix(deploy): classify preserved foreign paths in unit directives`) |
| Push / publication / deployment | none |
| AP pin | `73e20ef80b88700d5fcbc397cd8edd4fc425869f` (unmoved, not in the diff) |

The unified path-token classification is implemented at all four derived unit-directive guard sites; foreign custom paths carrying the retired spelling are preserved, frozen residues are preserved, near-miss variants of moved roots and under-root leftovers refuse. One local non-amended commit; nothing published; no host contact.

---

## 1. Reproduced baseline failure and post-correction preservation

Synthetic fixture (the live host path is not embedded anywhere; `git grep 'framenest-published'` = absent):

```text
[Service]
ReadWritePaths=/srv/media/framenest-example
```

| Stage | Exact probe output (declared route, same probe file) |
|---|---|
| Baseline, before any edit (`b8ec042` tree) | `C6GUARD-REPRO: {"exit_code": 27, "message": "unit directive ReadWritePaths path is not classifiable", "outcome": "raised"}` |
| Post-correction (`cf76f0b` tree) | `C6GUARD-REPRO: {"outcome": "preserved", "text": "[Service]\nReadWritePaths=/srv/media/framenest-example\n"}` |

The baseline shape is identical to the live preflight refusal: message `unit directive ReadWritePaths path is not classifiable`, exit code `EXIT_MIGRATION` 27, no mutation.

## 2. Derived guard-site set and rule application

Derivation: parsed `_systemd_transform_value` (its sole caller is `transform_unit_dropin_text`), located every site where a token that `transform_path_value` leaves unchanged and that contains the retired spelling could raise, resolved each to its literal text, and verified every `transform_path_value` caller independently. Pre-correction line numbers are from `b8ec042`; post-correction from the commit.

| # | Site (pre → post lines) | Literal pre-correction guard | Classification applied |
|---|---|---|---|
| 1 | `SYSTEMD_PATH_DIRECTIVES` token loop (4309 → 4344) | `transformed == body and "framenest" in body.lower()` | per token after `-` strip: frozen→preserve, foreign→preserve, moved→existing transform (leftover raises), near-miss→refuse |
| 2 | `LoadCredential` path (4251 → 4279) | `transformed == path and "framenest" in path.lower()` | same rule on `path`; identifier handling byte-unchanged |
| 3 | Exec plain token (4287 → 4320) | `transformed == path and "framenest" in command.lower()` | same rule on the executable token only |
| 4 | Exec `{ path=… }` revision (4271 → 4301) | `transformed == original and "framenest" in original.lower()` | same rule on the unescaped path value |

New classifier `classify_unit_path_token` (line 4226) order: frozen (`MIGRATION_FROZEN_PATH_PREFIXES`, equal or under) → moved (`MIGRATION_OLD_TO_NEW_ROOTS`, equal or under with separator) → near-miss (starts with a moved root's exact text, neither equal nor under) → foreign. Error codes and messages unchanged; frozen sets, segment renames and all other transformer semantics untouched.

**Guard site the prompt did not name (found by derivation, deliberately unchanged):** `_transform_sudoers_command` (line 4416) carries the same preserved-token shape (`transformed == command and "framenest" in command.lower()` → `sudo rule command path is not classifiable`). It lies outside the unit-directive transformer, the task identity is "in unit directives", and correction point 3 explicitly says not to alter sudo rules; changing it would widen a correction whose re-audit must find the foreign preservation "narrowly scoped". Its existing refusal is exercised by `test_structural_sudoers_transformation_refuses_unknown_forms`. Non-guard `transform_path_value` callers also re-verified: environment values (`transformed_environment_value`), console-script scoping (`migration_required_console_scripts`) and the retained internal under-root leftover refusal (line 2164) — all unchanged.

## 3. Matrix results per site shape

Each row runs against all four shapes (`ReadWritePaths` token list, `LoadCredential`, `ExecStart` plain, `ExecStart={ path=… }`):

| Rule category | Fixture (synthetic) | Result |
|---|---|---|
| frozen preserved | `/opt/framenest/tooling/readwrite` (frozen under a moved root), `/mnt/framenest-catalog-offdevice/bundles` | 8 cases: output byte-equal, classifier `"frozen"` |
| foreign preserved | `/srv/media/framenest-example` | 4 cases: output byte-equal, classifier `"foreign"` |
| near-miss refused | `/opt/framenest-old`, `/run/framenestx`, `/etc/framenest.env` | 12 cases: `EXIT_MIGRATION`, classifier `"near-miss"` |
| under-root leftover refused | `/var/lib/framenest/framenest-staging` | 4 cases: `EXIT_MIGRATION` from the retained leftover check, classifier `"moved"` |
| under-root transform unchanged | `/var/lib/framenest/catalog.sqlite3` → `/var/lib/kronika/catalog.sqlite3` | 4 cases: exact transformed text, classifier `"moved"` |

Plus: one rule-order test over all five roots (`root`, `root/sub/path`, `root-old`, `rootx`), one end-to-end mixed directive (`ReadWritePaths=-/srv/media/framenest-example /var/lib/framenest/catalog-backups` → foreign token preserved beside moved-root token transformed, same directive), and one argument-opacity pin. 35 new tests; nothing existing was weakened or deleted.

## 4. Mutation demonstrations (probe applies exact textual mutations to `classify_unit_path_token` and runs the named repository test against the mutant)

| Mutation | Description | Named test | Observed failure | Directive consequence |
|---|---|---|---|---|
| **FR** | foreign-preserve removed: final `return "foreign"` → `return "near-miss"` | `test_structural_dropin_preserves_foreign_custom_tokens_at_every_guard_site` | `ReleaseError: unit directive ReadWritePaths path is not classifiable` | same refusal returns |
| **NM** | near-miss weakened: `return "near-miss"` → `return "foreign"` | `test_structural_dropin_refuses_near_miss_tokens_at_every_guard_site` | `Failed: DID NOT RAISE ReleaseError` | silently preserves `/opt/framenest-old` |
| **FZ** | frozen check removed: frozen loop deleted | `test_structural_dropin_preserves_frozen_tokens_at_every_guard_site` | `AssertionError: assert 'moved' == 'frozen'` | directive preservation survives via `transform_path_value`'s own frozen branch (disclosed below) |

The probe fails loudly if any mutation does not make its test fail; all three demonstrated it.

## 5. Verification counts and elapsed time

All runs through the declared route with `--baseline b8ec042…`; `ap project check` was PASS before editing.

| Run | Result | Elapsed | Difference from baseline |
|---|---|---|---|
| Focused module `tests/contract/test_kronika_identity_migration.py` | **193 passed** | 0.81s | +35 passed (pre-change measurement of the same module: 158) |
| Full declared Python suite (`--operation test`) | **4863 passed, 8 skipped, 3 warnings, 0 failed** | 691.26s (11:31) | +35 passed; skips and warnings byte-identical (8 env-gated skips, 3 Pydantic warnings) |
| Retention module `tests/contract/test_kronika_identity_retention.py` | **15 passed** | 0.35s | none |

Probes: reproduction 0.04s; mutations 0.33s; retention regeneration 0.19s.

## 6. Commit, diff stat, Part A / Part B / Part C

`git diff --stat` (commit `cf76f0b`, parent `b8ec042`, single non-amended commit on `main`, tree clean):

```text
 deploy/ubuntu/kronika_release.py                  |  64 ++++++--
 tests/contract/test_kronika_identity_migration.py | 192 ++++++++++++++++++++++
 tests/contract/test_kronika_identity_retention.py |  46 +++++-
 3 files changed, 283 insertions(+), 19 deletions(-)
```

- **Part A byte-unmoved:** `git diff b8ec042..HEAD` over every frozen path (ADRs, `docs/FEDORA_SERVICE.md`, `docs/NUC_HOST_BASELINE.md`, Alembic versions directory) is empty; the Part A tests pass. `FROZEN_ALEMBIC_SHA256` computed: **36** keys; frozen documents: 86.
- **Part B still measures 20:** regenerated probe: `basename_count: 20, basename_measured: 20, basename_added: [], basename_missing: []`.
- **Part C movement, measured before re-pinning, cause stated in the file** — every other pin regenerated equal:
  - `PER_TREE_FRAMENEST_OCCURRENCE_COUNT`: `deploy` 250 → **246** (−4: the four guard substring literals removed, none added); `tests` 2251 → **2264** (+13: 9 fixture occurrences, 3 mixed-directive, 1 argument-opacity). `docs`, `extension`, `scripts`, `src` unmoved.
  - `HOST_PATH_OCCURRENCE_COUNT` (all from new synthetic test fixtures; engine adds/removes no host literal): `/opt/framenest` 226 → **228**, `/etc/framenest` 86 → **87**, `/var/lib/framenest` 122 → **125**, mount 25 → **26**; `/var/cache/framenest` unmoved.
  - Unmoved: per-tree file counts (22/88/8/11/186/186), content-path membership, env prefix 699/112/53, capitalized 2773/399, mutation header 73/30, unit accounts 9/9.
  - No pin was tuned toward green: each pin value was written only after a fresh probe measurement, and the final regeneration shows measured == pinned for every scalar.

## 7. Moved or removed sites no test exercises

None. Every moved or removed site is exercised: the four guard sites × five matrix categories (32 parametrized cases), the rule-order derivation, the mixed directive, and the removed whole-command argument scan (pinned by `test_structural_dropin_keeps_exec_argument_text_opaque`). The unchanged sudoers guard's refusal is exercised by the pre-existing unknown-forms test.

## 8. Deviations, risks, missing evidence, smallest next step

- **Deviation (documented):** the Exec plain form's baseline guard scanned the whole command text (`command.lower()`); the unified classification reads the executable token only, so argument text carrying the retired spelling is now opaque. This is required by the specification's "Only near-miss variants of a moved root continue to refuse" and by the required foreign-preservation matrix row, and it is pinned by a new test. Resulting text change stated: `test_structural_dropin_keeps_exec_argument_text_opaque`.
- **Boundary note:** a `LoadCredential` path that is relative or otherwise outside the moved roots and carries the retired spelling is now classified foreign and preserved (previously refused); absoluteness was never validated by this transformer and remains unvalidated.
- **Honest limit on mutation FZ:** for current data the classifier's frozen branch is behaviorally redundant at the sites (frozen tokens are also preserved by `transform_path_value`'s own frozen check); FZ therefore fails on the classification assertion, not the preservation assertion. The branch fixes the documented order (frozen before moved) and guards future frozen prefixes that could collide with a moved root's near-miss text.
- **Unnamed guard found and left unchanged:** `_transform_sudoers_command` (see §2); disposition is scope-based, not a defect claim.
- **Missing evidence:** none material. No host preflight, no rendered acceptance, no provider contact — none was authorized.
- **Smallest next step:** the fresh independent re-audit of this correction stated in the acceptance note; only after its PASS may the C6-H preflight be re-run under its own grant.

**Resolved Execution Issues / Near-Misses:**

1. My first `edit` call inverted `oldString`/`newString` for the LoadCredential block; the tool rejected it without touching the file, and the corrected call applied the intended change. No residue (`git diff --check` clean).
2. Pin sequencing near-miss: after the first measurement I pinned `tests` at 2263; adding the argument-opacity test afterwards moved the measurement to 2264, which the regenerated probe caught, and I re-pinned only after that fresh measurement. No pin was ever set without a measurement; no suite ever ran green against a guessed value.
3. One stray extra blank line in the inserted test block was removed before the first final run; style only, no test effect.

**Pre-Existing Failure Classification:** none. Baseline full suite 4828 passed / 8 skipped / 3 warnings / 0 failed; my measured full run 4863 / 8 / 3 / 0. The 8 skips are the declared environment-gated real-tools and live-NIM skips, unchanged.

```text
Orchestration critique:
MEASURED: The correction prompt describes every guard as `transformed == token and "framenest" in token`, but the committed baseline's Exec plain guard actually scanned the whole command text (`"framenest" in command.lower()`, `b8ec042:4287`); the prompt therefore did not state the argument-text disposition, and this Worker had to choose it. Evidence: the literal pre-correction line, the required foreign-preservation matrix row, and the new pinning test `test_structural_dropin_keeps_exec_argument_text_opaque`. Effect: argument text carrying the retired spelling no longer refuses, which a re-auditor could read as beyond the named correction unless it is stated as accepted. Smallest correction: a later prompt touching this transformer should state explicitly whether classification covers the executable token only or the whole command.
LEAD: The same-shaped sudoers command guard will still refuse a foreign custom sudo rule path carrying the retired spelling (unverified whether the live host has such a rule; the preflight finding showed only the ReadWritePaths case). Cheapest useful check: in the next authorized preflight window, list effective sudo rule command paths and classify each under the four-way rule before apply, rather than discovering it as a second fail-closed stop.
```

Authority expiry: on submission of this terminal report, all authority under this prompt expires. No further implementation, no second commit, no push, no publication, no host contact, and no later cut is authorized by it.