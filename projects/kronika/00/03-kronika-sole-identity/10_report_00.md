### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: kronika-sole-identity
Worker session ordinal: 10
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-04 — make the resolver's documented precedence and
 conflict scope match measured behaviour
Status: PASS
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this correction, by design
Start commit: 24bea56daca28603d81cac8d7ed7e3888ba90671
End commit:   02a80485206eeeb33c43393d25514a30d7fe297f
Changed files: 5 — src/framenest/identity_env.py (docstrings only),
  tests/unit/test_identity_env.py, tests/contract/test_kronika_identity_dual_read.py,
  tests/contract/test_kronika_settings_parity.py,
  tests/contract/test_kronika_identity_retention.py (Part C re-pins)
Report justification: new-mutation
```

C1d is complete. The inverted paragraph is rewritten to the measured order, the
per-channel conflict rule is stated where a reader of the resolver will look, both
are pinned by tests shown failing on violation, the parity-matrix value guard is in
place, and **not one line of executable logic changed** — proven mechanically, not
asserted.

## Repository gate (matched as issued, before any edit)

- Branch `feat/kronika-identity-dual-read`, HEAD `24bea56daca28603d81cac8d7ed7e3888ba90671`, subject `fix(identity): restore pre-cut process-environment parity for old spellings`, parent `c02c675…`, lineage `18c357c → 90c93ea → c02c675 → 24bea56`. Tree clean.
- `.ap` gitlink and submodule HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`; `ap doctor` **PASS**, governing variant stable.
- `./.ap/ap project check --baseline 24bea56…` **PASS**.
- `git ls-remote origin refs/heads/main` → `18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`; `refs/heads/feat/kronika-identity-dual-read` absent, so the branch is unpublished as declared. Still unpublished after this commit.

## Measured table (item 2) — every row verified by me

`load_settings(env_file=None)` under `mock.patch.dict(os.environ, …, clear=True)`,
plus `lookup_env` / `lookup_field_value` on the same mapping, plus the file
channel, plus `framenest-db status` under `env -i`.

| Row | Issued table | My measurement | Agrees |
|---|---|---|---|
| A | `KRONIKA_PORT=9998` + `FRAMENEST_PORT=9999` → conflict, exit 2 | `IdentityEnvironmentConfigurationError[exit=2]`, message names only `KRONIKA_PORT`/`FRAMENEST_PORT`, `leaks9998=False leaks9999=False`; CLI `{"error_code":"FRAMENEST_DB_CONFIGURATION_FAILED",…}` **exit 2**, `created=none` | yes |
| B | `kronika_port=9998` + `framenest_port=9999` → `9999`, no conflict | `lookup_env=None`, `lookup_field_value='9999'`, `load_settings` **port=9999**; CLI exit 0 | yes |
| C | `KRONIKA_PORT=9998` + `framenest_port=9999` → `9998`, no conflict | `lookup_env='9998'`, `lookup_field_value='9998'`, **port=9998**; CLI exit 0 | yes |
| D (same name twice, impossible) | n/a | replaced by two case variants of one name — see G/H/I | n/a |
| E | `KRONIKA_PORT=` + `framenest_port=9999` → `9999` | **port=9999** | yes |
| F | `kronika_port=` + `FRAMENEST_PORT=9999` → `9999` | **port=9999** | yes |
| — | `KRONIKA_PORT=9998` + `FRAMENEST_PORT=9998` → accepted | **port=9998** | yes |
| G | two variants of one old name | `FRAMENEST_PORT=9998` + `framenest_port=9999` → `lookup_env='9998'`, `lookup_field_value='9999'`, **port=9999** (later folded entry wins) | — |
| H | case-exact + variant of the identity name | `KRONIKA_PORT=9998` + `kronika_port=9999` → `'9998'` both levels | — |
| I | reversed H | `kronika_port=9998` + `KRONIKA_PORT=9999` → `'9999'` both levels | — |
| K | case-exact identity + empty compatible | `KRONIKA_PORT=9998` + `framenest_port=` → `lookup_env='9998'`, `lookup_field_value='9998'`, **port=9998** | — |
| L | host variant pair | `kronika_host=10.0.0.2` + `framenest_host=127.0.0.1` → `lookup_field_value('HOST')='127.0.0.1'`, **host='127.0.0.1'** (identity case variant silently dropped) | — |
| X1 | cross-channel, identity in process | process `KRONIKA_PORT=9998` + file `FRAMENEST_PORT=9999` → **port=9998**, no conflict | — |
| X2 | cross-channel, compatible in process | process `FRAMENEST_PORT=9999` + file `KRONIKA_PORT=9998` → **port=9999**, no conflict | — |

**No row of the issued table disagreed with the code.** One nuance worth recording:
in the **environment-file** channel the picture differs, because`canonical_identity_environment` upper-cases file keys before the resolver sees
them. Row B written as a *file* becomes `KRONIKA_PORT` + `FRAMENEST_PORT` and
therefore **conflicts**, and rows H/I written as a file collapse to one canonical
name. The issued table's rows are process-channel rows; that is what the docstring
now says ("measured on one mapping").

## Before-and-after: the old docstring was false

Old text: *"the compatible spelling is consulted first, so the identity spelling
cannot be shadowed by a case variant of the compatible one."*

- **Before (measured, code as committed at `24bea56`):** `kronika_port=9998` beside
  `framenest_port=9999` → `lookup_field_value('PORT') == '9999'`. The identity case
  variant **is** shadowed, silently, with no conflict. Same for
  `kronika_host=10.0.0.2` beside `framenest_host=127.0.0.1` → `127.0.0.1`.
  The sentence asserted the exact opposite of the code, and the sentence after it
  asserted the reverse again, so the paragraph was internally incoherent.
- **After:** the docstring states layer 1 short-circuits (immune), layer 2 precedes
  layer 3 (case-variant eviction is real), and both are pinned by tests that fail
  when either half is violated (below).

I did **not** change behaviour to make the old sentence true; the sentence was the
defect, exactly as the re-audit found.

## Exact diff of every path

`git diff 24bea56..HEAD`:

```diff
diff --git a/src/framenest/identity_env.py b/src/framenest/identity_env.py
index 22829f5..797eccf 100644
--- a/src/framenest/identity_env.py
+++ b/src/framenest/identity_env.py
@@ -29,6 +29,21 @@ environment file and existing systemd ``Environment=`` handling keep their
 current meaning. That rule exists for the ``ENV_FILE`` selector, which reads a
 path rather than a field value, and for the direct reader call sites.
 
+The table is a rule about **one mapping**, and the conflict check is
+**per channel**. :func:`lookup_env` is called once per source over that source's
+mapping only: the process environment is one channel and the environment file is
+the other. ``KRONIKA_<SUFFIX>`` in the process environment together with
+``FRAMENEST_<SUFFIX>`` in the environment file therefore raises no conflict, and
+the process-environment source is ordered first, so the process-environment
+value wins; the reverse arrangement resolves the same way.
+
+There is deliberately no cross-channel conflict check. A global rule would fail
+closed on the ordinary case of an environment file that supplies a value and a
+process environment that overrides it, which the installed ``EnvironmentFile=``
+and ``Environment=`` handling treats as normal operation rather than a
+misconfiguration. This is a deliberate silent resolution, not an oversight, and
+it is a divergence from a global conflict rule.
+
 One settings *field* needs a wider rule than a direct reader, and
 :func:`lookup_field_value` states it. A settings field is matched against a
 variable name, not read as a whole setting, so the two behaviours a field must
@@ -133,6 +148,11 @@ def lookup_env(
     the caller's own default. Raises
     :class:`IdentityEnvironmentConflictError` when both spellings are set to
     different values, before either value is returned.
+
+    The check covers exactly the mapping passed in, so it is per channel. A
+    caller that reads two channels calls this once per channel, and two
+    spellings of one suffix split across the two channels never meet in one
+    call. The module docstring states that rule and why it exists.
     """
     env = os.environ if environ is None else environ
     primary = env.get(f"{PRIMARY_ENVIRONMENT_PREFIX}{suffix}")
@@ -190,15 +210,39 @@ def lookup_field_value(
 
     ``case_folded`` is accepted so a caller that resolves many fields folds the
     mapping once. :func:`lookup_env` runs for every field, so the cross-prefix
-    conflict check stays exactly as strict as before and raises before any layer
-    returns.
-
-    When both prefixes are present and differ in case from the canonical
-    spelling, layers 2 and 3 never collide with each other: the compatible
-    spelling is consulted first, so the identity spelling cannot be shadowed by
-    a case variant of the compatible one. The reverse is not true, and is
-    deliberate: a case-exact ``KRONIKA_<SUFFIX>`` outranks a case variant of the
-    compatible spelling rather than being silently ignored by it.
+    conflict check stays exactly as strict as before within that one mapping, and
+    raises before any layer returns.
+
+    What the layer order means, measured on one mapping:
+
+    - A case-exact ``KRONIKA_<SUFFIX>`` carrying a non-empty value is answered
+      by layer 1 and short-circuits, so it is shadowed neither by a case variant
+      of the compatible spelling nor by a case variant of itself.
+    - When both spellings are present only as case variants, layer 2 answers
+      first, so the compatible spelling wins and a case variant of the identity
+      spelling **can** be shadowed by a case variant of the compatible one:
+      ``kronika_port=9998`` beside ``framenest_port=9999`` resolves to ``9999``
+      and raises nothing.
+    - An empty identity spelling counts as unset in layer 1 and in layer 3
+      alike, so ``KRONIKA_PORT=`` beside ``framenest_port=9999`` resolves to
+      ``9999``.
+
+    The compatible layer sits ahead of the identity layer deliberately. Before
+    this resolver existed the compatible prefix was the only prefix the library
+    read, so a case variant of the compatible spelling is what configured a
+    field then; the differential parity matrix in
+    ``tests/contract/test_kronika_settings_parity.py`` measures that reading
+    case by case against the pre-cut source. Keeping layer 2 ahead therefore
+    reproduces the pre-cut result for an input whose identity spelling is a
+    case variant, and changes nothing for an input that carries no identity
+    spelling at all. A case-exact ``KRONIKA_<SUFFIX>`` is the deliberate
+    divergence: layer 1 answers it, where the pre-cut library read the
+    compatible spelling instead.
+
+    The cross-prefix conflict check is unaffected by any of this. It stays
+    case-exact, because it compares the two canonical names only, and it runs
+    unconditionally before any layer decides, because :func:`lookup_env` is
+    called first. It is per mapping like everything else here.
     """
     values = os.environ if environ is None else environ
     folded = folded_identity_environment(values) if case_folded is None else case_folded
diff --git a/tests/contract/test_kronika_identity_dual_read.py b/tests/contract/test_kronika_identity_dual_read.py
index 55f3a8a..f88e84e 100644
--- a/tests/contract/test_kronika_identity_dual_read.py
+++ b/tests/contract/test_kronika_identity_dual_read.py
@@ -183,6 +183,68 @@ def test_environment_file_still_applies_without_a_process_override(
     assert settings.port == 7003
 
 
+@pytest.mark.parametrize(
+    ("process_name", "process_value", "file_line", "expected"),
+    [
+        pytest.param(
+            f"{PRIMARY}PORT",
+            "7006",
+            f"{COMPATIBLE}PORT=7005\n",
+            7006,
+            id="identity-spelling-in-the-process-environment",
+        ),
+        pytest.param(
+            f"{COMPATIBLE}PORT",
+            "7008",
+            f"{PRIMARY}PORT=7007\n",
+            7008,
+            id="compatible-spelling-in-the-process-environment",
+        ),
+    ],
+)
+def test_the_conflict_rule_is_per_channel_and_the_process_environment_wins(
+    process_name: str,
+    process_value: str,
+    file_line: str,
+    expected: int,
+    tmp_path: Path,
+    monkeypatch: pytest.MonkeyPatch,
+) -> None:
+    """A cross-channel pair is not a conflict, in either arrangement.
+
+    The conflict check runs once per source over that source's mapping only, so
+    one spelling in the process environment and the other spelling in the
+    environment file never meet in one call. Reaching this assertion is the
+    evidence that no conflict was raised.
+    """
+    env_file = tmp_path / "framenest.env"
+    env_file.write_text(file_line, encoding="utf-8")
+    monkeypatch.chdir(tmp_path)
+    monkeypatch.setenv(process_name, process_value)
+
+    settings = load_settings(env_file=env_file)
+
+    assert settings.port == expected
+
+
+def test_the_two_spellings_inside_one_channel_still_fail_closed(
+    tmp_path: Path,
+    monkeypatch: pytest.MonkeyPatch,
+) -> None:
+    """The silent cross-channel resolution must not weaken the same-channel rule."""
+    env_file = tmp_path / "framenest.env"
+    env_file.write_text(f"{PRIMARY}PORT=7009\n{COMPATIBLE}PORT=7010\n", encoding="utf-8")
+    monkeypatch.chdir(tmp_path)
+
+    with pytest.raises(FrameNestConfigurationError) as excinfo:
+        load_settings(env_file=env_file)
+
+    assert "PORT" in str(excinfo.value)
+    assert "7009" not in str(excinfo.value)
+    assert "7010" not in str(excinfo.value)
+    assert excinfo.value.exit_status == 2
+
+
 def test_extra_ignore_is_preserved(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
     monkeypatch.chdir(tmp_path)
     env_file = tmp_path / "framenest.env"
diff --git a/tests/contract/test_kronika_identity_retention.py b/tests/contract/test_kronika_identity_retention.py
index 559b93..cf7d011 100644
--- a/tests/contract/test_kronika_identity_retention.py
+++ b/tests/contract/test_kronika_identity_retention.py
@@ -200,17 +200,17 @@ PER_TREE_FRAMENEST_FILE_COUNT = {
 # actually detect a missed content rename. See the `fn-production-env-deploy`
 # case, whose filename is clean while its content names `framenest`.
 PER_TREE_FRAMENEST_OCCURRENCE_COUNT = {
-    "src": 2981,
-    "tests": 4434,
+    "src": 2984,
+    "tests": 4446,
     "deploy": 212,
     "scripts": 104,
     "docs": 1216,
     "extension": 199,
 }
 
-ENV_PREFIX_TOKEN_COUNT = 642
+ENV_PREFIX_TOKEN_COUNT = 643
 ENV_PREFIX_DISTINCT_NAME_COUNT = 101
-ENV_PREFIX_BARE_SPELLING_COUNT = 18
+ENV_PREFIX_BARE_SPELLING_COUNT = 21
@@ -229,7 +229,7 @@ UNIT_ACCOUNT_OCCURRENCE_COUNT = {
     "Group=framenest": 5,
 }
 
-CAPITALIZED_OCCURRENCE_COUNT = 3379
+CAPITALIZED_OCCURRENCE_COUNT = 3381
 CAPITALIZED_FILE_COUNT = 482
diff --git a/tests/contract/test_kronika_settings_parity.py b/tests/contract/test_kronika_settings_parity.py
index 35e74ce..4d7a06 100644
--- a/tests/contract/test_kronika_settings_parity.py
+++ b/tests/contract/test_kronika_settings_parity.py
@@ -192,6 +192,17 @@ def test_environment_file_matches_the_stock_source_for_every_field(tmp_path: Pat
     assert not mismatches, "environment-file parity broken:\n" + "\n".join(mismatches)
 
 
+def test_the_matrix_subject_is_pinned_to_the_compatible_prefix_value() -> None:
+    """The matrix builds its variable names from the constant, so pin its value.
+
+    Without this guard a later cut that changed the constant's *value* would
+    change the subject of every comparison above, and the parity claim would
+    become vacuous with nothing failing.
+    """
+    assert COMPATIBLE_ENVIRONMENT_PREFIX == "FRAMENEST_"
+    assert FrameNestSettings.model_config["env_prefix"] == "FRAMENEST_"
+
+
 def test_the_matrix_reaches_every_field_and_every_value() -> None:
     cases = list(_matrix())
diff --git a/tests/unit/test_identity_env.py b/tests/unit/test_identity_env.py
index effc55c..160a328 100644
--- a/tests/unit/test_identity_env.py
+++ b/tests/unit/test_identity_env.py
@@ -10,6 +10,7 @@ from framenest.identity_env import (
     PRIMARY_ENVIRONMENT_PREFIX,
     IdentityEnvironmentConflictError,
     lookup_env,
+    lookup_field_value,
 )
@@ -132,3 +133,57 @@ def test_accepted_prefixes_are_exactly_the_recorded_identity_pair() -> None:
         "KRONIKA_",
         "FRAMENEST_",
     )
+
+
+# ---------------------------------------------------------------------------
+# The field layer order, in both halves
+# ---------------------------------------------------------------------------
+
+
+def test_a_case_exact_identity_spelling_short_circuits_every_other_layer() -> None:
+    """Layer 1 answers, so no case variant displaces the canonical name."""
+    assert (
+        lookup_field_value("PORT", environ={"KRONIKA_PORT": "9998", "framenest_port": "9999"})
+        == "9998"
+    )
+    assert (
+        lookup_field_value("PORT", environ={"KRONIKA_PORT": "9998", "kronika_port": "9999"})
+        == "9998"
+    )
+
+
+def test_a_case_variant_of_the_identity_spelling_loses_to_the_compatible_layer() -> None:
+    """Layer 2 precedes layer 3, so the case variant of the identity name loses."""
+    assert (
+        lookup_field_value("PORT", environ={"kronika_port": "9998", "framenest_port": "9999"})
+        == "9999"
+    )
+    assert (
+        lookup_field_value(
+            "PORT",
+            environ={"kronika_port": "9998", "Framenest_Port": "9999"},
+        )
+        == "9999"
+    )
+
+
+def test_an_empty_identity_spelling_is_unset_in_both_identity_layers() -> None:
+    """Layers 1 and 3 agree that an empty identity value carries no value."""
+    assert (
+        lookup_field_value("PORT", environ={"KRONIKA_PORT": "", "framenest_port": "9999"})
+        == "9999"
+    )
+    assert (
+        lookup_field_value("PORT", environ={"kronika_port": "", "framenest_port": "9999"})
+        == "9999"
+    )
+    assert lookup_field_value("PORT", environ={"KRONIKA_PORT": ""}) is None
+    assert lookup_field_value("PORT", environ={"kronika_port": ""}) is None
+
+
+def test_the_cross_prefix_conflict_check_precedes_every_field_layer() -> None:
+    """The check runs first, so it also outranks the case-exact short-circuit."""
+    with pytest.raises(IdentityEnvironmentConflictError):
+        lookup_field_value(
+            "PORT", environ={"KRONIKA_PORT": "9998", "FRAMENEST_PORT": "9999"}
+        )
```

`git diff --stat 24bea56..HEAD`: `identity_env.py | 62 ++--`, `dual_read | 62 ++`,
`retention | 10 +-`, `parity | 11 ++`, `unit identity_env | 55 ++` → 186 insertions,
14 deletions, five files, no executable line.

**Test modules used, reported explicitly** (the prompt asked for this):
- `tests/unit/test_identity_env.py` — the resolver's own unit module; the four
  layer-order and conflict-precedence tests live here.
- `tests/contract/test_kronika_identity_dual_read.py` — the contract module for the
  dual-prefix read boundary; it already owns both channel tests and the conflict
  test, so the per-channel rule and its same-channel contrast live here.
- `tests/contract/test_kronika_settings_parity.py` — the value guard, in the module
  whose `_spelled()` builds names from the constant.

I did not put the new tests in the parity matrix itself: the matrix is a*differential against the pre-cut source* and the cross-channel rule is
new-behaviour territory the oracle deliberately does not cover.

## Statement-by-statement evidence table

Every sentence I wrote or changed, with its support and evidence class
(M = measurement I took, C = line of code I read, A = authority document).
No sentence is in the file without a row here.

### Module docstring, new paragraphs

| # | Statement | Evidence | Class |
|---|---|---|---|
| M1 | "The table is a rule about **one mapping**, and the conflict check is **per channel**." | `lookup_env` reads only `env = os.environ if environ is None else environ` (`identity_env.py:137-139`); the two call sites pass one mapping each — `os.environ` (`configuration.py:207`) and `canonical_identity_environment(file_values)` (`configuration.py:221`) | C |
| M2 | "``lookup_env`` is called once per source over that source's mapping only." | `identity_env.py:249` inside `lookup_field_value`, reached once per field per source; `configuration.py:170-187` loops fields per source | C |
| M3 | "``KRONIKA_<SUFFIX>`` in the process environment together with ``FRAMENEST_<SUFFIX>`` in the environment file therefore raises no conflict" | measured X1: process `KRONIKA_PORT=9998` + file `FRAMENEST_PORT=9999` → `port=9998`, no exception | M |
| M4 | "the process-environment source is ordered first, so the process-environment value wins" | measured X1 (`9998` = process value) and X2 (process `FRAMENEST_PORT=9999` + file `KRONIKA_PORT=9998` → `9999`); `settings_customise_sources` docstring `configuration.py:244-249`; `load_settings` docstring `configuration.py:668-669` "Process environment variables always override environment-file values" | M + C |
| M5 | "the reverse arrangement resolves the same way" | measured X2 | M |
| M6 | "There is deliberately no cross-channel conflict check." | M1/M2 by construction; and counterfactually demonstrated — installing a global rule makes the new per-channel test fail with `IdentityEnvironmentConfigurationError` in both arrangements | C + M |
| M7 | "A global rule would fail closed on the ordinary case of an environment file that supplies a value and a process environment that overrides it" | measured: the global-rule mutation raises exactly on the pairs the real code accepts silently (X1/X2 arrangement) | M |
| M8 | "which the installed ``EnvironmentFile=`` and ``Environment=`` handling treats as normal operation rather than a misconfiguration" | `deploy/systemd/framenest.service:12-13` combines `Environment=` with `EnvironmentFile=`; `deploy/systemd/framenest.env.example` supplies values; `configuration.py:668-669` states the override is the intended ordering; existing module text already relies on "existing systemd ``Environment=`` handling" | A + C |
| M9 | "This is a deliberate silent resolution, not an oversight, and it is a divergence from a global conflict rule." | the divergence is measured (X1/X2 accept what a global rule rejects); "deliberate" is the recorded Orchestrator decision A2 in this task | M + A |

### `lookup_env` docstring, new paragraph

| # | Statement | Evidence | Class |
|---|---|---|---|
| L1 | "The check covers exactly the mapping passed in, so it is per channel." | `identity_env.py:137-139` | C |
| L2 | "A caller that reads two channels calls this once per channel, and two spellings of one suffix split across the two channels never meet in one call." | two call sites, one mapping each (`configuration.py:207`, `configuration.py:221`); measured X1/X2 | C + M |
| L3 | "The module docstring states that rule and why it exists." | this file, lines 32-45 | C |

### `lookup_field_value` docstring, rewritten closing| # | Statement | Evidence | Class |
|---|---|---|---|
| F0 | "the cross-prefix conflict check stays exactly as strict as before **within that one mapping**" | `lookup_env` call unchanged at `identity_env.py:249`; measured rows A/B/C/J show the check is still case-exact on the two canonical names | C + M |
| F1 | "A case-exact ``KRONIKA_<SUFFIX>`` carrying a non-empty value is answered by layer 1 and short-circuits" | `identity_env.py:250-251` returns before layers 2-3; measured C → `9998` and K → `9998` | C + M |
| F2 | "so it is shadowed neither by a case variant of the compatible spelling" | measured C: `KRONIKA_PORT=9998` + `framenest_port=9999` → `9998` | M |
| F3 | "nor by a case variant of itself" | measured H: `KRONIKA_PORT=9998` + `kronika_port=9999` → `9998` (and I, reversed, → `9999`, i.e. the case-exact name's own value is what answers) | M |
| F4 | "When both spellings are present only as case variants, layer 2 answers first, so the compatible spelling wins" | `identity_env.py:252-254` precedes `255-257`; measured B → `9999` and J (`Framenest_Port`) → `9999`; measured L host → `127.0.0.1` | C + M |
| F5 | "a case variant of the identity spelling **can** be shadowed by a case variant of the compatible one: ``kronika_port=9998`` beside ``framenest_port=9999`` resolves to ``9999`` and raises nothing" | measured B at resolver, `load_settings` and CLI level; `lookup_env` returns `None` so no conflict is even possible | M |
| F6 | "An empty identity spelling counts as unset in layer 1 and in layer 3 alike" | layer 1 is `if values.get(...)` (truthiness, `identity_env.py:250`), layer 3 is `if primary:` (`identity_env.py:256`) — both reject `""`; pinned by `test_an_empty_identity_spelling_is_unset_in_both_identity_layers`, which fails if layer 3 is changed to `is not None` | C + M |
| F7 | "so ``KRONIKA_PORT=`` beside ``framenest_port=9999`` resolves to ``9999``" | measured E | M |
| F8 | "Before this resolver existed the compatible prefix was the only prefix the library read, so a case variant of the compatible spelling is what configured a field then" | stock reference (the library's own `settings_customise_sources` hook, the same construction the parity module uses) on `{"kronika_port":"9998","framenest_port":"9999"}` → `port=9999`; and `{"kronika_host":"10.0.0.2","framenest_host":"127.0.0.1"}` → stock accepts the compatible value | M |
| F9 | "the differential parity matrix … measures that reading case by case against the pre-cut source" | `tests/contract/test_kronika_settings_parity.py:1-24` module docstring plus `test_process_environment_matches_the_stock_source_for_every_field` / `…environment_file…`, both green in the final run | A + M |
| F10 | "Keeping layer 2 ahead therefore reproduces the pre-cut result for an input whose identity spelling is a case variant" | stock `9999` == current `9999` for `{"kronika_port":"9998","framenest_port":"9999"}` | M |
| F11 | "and changes nothing for an input that carries no identity spelling at all" | `identity_env.py:255-257`: with no identity name present, `primary` is `None` and layer 3 cannot answer, so the relative order of layers 2 and 3 is unreachable | C |
| F12 | "A case-exact ``KRONIKA_<SUFFIX>`` is the deliberate divergence: layer 1 answers it, where the pre-cut library read the compatible spelling instead." | stock `9999` vs current `9998` on `{"KRONIKA_PORT":"9998","framenest_port":"9999"}`; existing `test_the_case_exact_identity_spelling_outranks_a_case_variant_of_the_old_spelling` already names it "A deliberate divergence" | M + A |
| F13 | "It stays case-exact, because it compares the two canonical names only" | `identity_env.py:138-139` builds exactly `KRONIKA_<S>` and `FRAMENEST_<S>`; measured A (conflict) vs B/C/J (no conflict) | C + M |
| F14 | "it runs unconditionally before any layer decides, because :func:`lookup_env` is called first" | `identity_env.py:249` precedes `250-258`; measured A raises although layer 1 would have returned `9998`; pinned by `test_the_cross_prefix_conflict_check_precedes_every_field_layer` | C + M |
| F15 | "It is per mapping like everything else here." | M1/M2 | C |

**Deleted, not hedged.** The old sentence pair "layers 2 and 3 never collide with
each other" and "The reverse is not true" is gone entirely; nothing in its place
claims immunity for a case-variant identity spelling. I found no sentence I had
to delete for lack of evidence — but I did refuse to write the operator-facing
version of F8 ("what an operator had working"), because no measurement in this
repository establishes operator practice; only the library's pre-cut reading is
measured, and only that is claimed.

## Tests shown failing when their property is violated

Every mutation below is an **in-memory rebind** (`mock.patch.object`) of the
resolver function the test module imported. No repository file was written for any
of them. "DETECTED" means the committed test raised.

| Committed test | Mutation violating its named property | Result |
|---|---|---|
| `test_a_case_exact_identity_spelling_short_circuits_every_other_layer` | layer 1 removed | **DETECTED** (`AssertionError`) |
| same | layers 2/3 inverted | **DETECTED** (`AssertionError`) |
| `test_a_case_variant_of_the_identity_spelling_loses_to_the_compatible_layer` | layers 2/3 inverted | **DETECTED** (`AssertionError`) |
| same | layer 1 removed | NOT DETECTED — **correct negative control**: removing layer 1 cannot change the all-case-variant outcome, which proves the two tests are independent halves rather than one test wearing two hats |
| `test_an_empty_identity_spelling_is_unset_in_both_identity_layers` | layer 3 changed to `if primary is not None` | **DETECTED** (`AssertionError`) — after I added two assertions; the first draft of this test was **not** detected, see near-misses |
| `test_the_cross_prefix_conflict_check_precedes_every_field_layer` | `lookup_env` call removed from the field path | **DETECTED** (`DID NOT RAISE IdentityEnvironmentConflictError`) |
| `test_the_conflict_rule_is_per_channel_and_the_process_environment_wins[identity-spelling-in-the-process-environment]` | a **global** cross-channel rule installed on the file source (its resolver mapping merged with `os.environ`) | **DETECTED** (`IdentityEnvironmentConfigurationError: Conflicting environment variables KRONIKA_PORT and FRAMENEST_PORT…`) |
| `…[compatible-spelling-in-the-process-environment]` | same global rule | **DETECTED** (same conflict) |
| `test_the_two_spellings_inside_one_channel_still_fail_closed` | `lookup_env` replaced by a lenient version that never raises | **DETECTED** (`DID NOT RAISE FrameNestConfigurationError`) |

## Value guard shown failing

Temporary local edit of `src/framenest/identity_env.py:67`, then restoredimmediately and verified by `grep` plus `git diff`:

| Constant value | Guard | Other tests in the parity module |
|---|---|---|
| `"KRONIKA_"` | **FAILS**: `assert 'KRONIKA_' == 'FRAMENEST_'` | both parity tests also failed |
| `"UNRELATED_"` | **FAILS**: same assertion | 7 tests failed, including `test_an_old_spelling_name_in_any_case_configures_the_field[framenest_port]` |
| restored `"FRAMENEST_"` | passes | module green (23 tests) |

**Correction to the re-audit's phrasing, measured.** Report 09 said the matrix
"silently changes its subject and the parity claim becomes vacuous with no test
failing". The guard is real and necessary, but the *silent* part is not what I
measured: with **either** changed value, other tests in that module fail loudly,
because `test_an_old_spelling_name_in_any_case_configures_the_field` and
`test_both_cases_of_one_old_name_resolve_to_the_later_value` hardcode
`framenest_port`. The guard's value is that it pins the matrix subject *directly
and by name*, instead of relying on unrelated tests to notice, and it survives a
future edit that removes or renames those case tests. No contradiction of the
Orchestrator's decision, and the guard is in place as instructed.

## Part C movements, each with its exact cause

Re-pinned **only** what my change genuinely moved. Part A and Part B did not move
(all 14 retention tests green after the re-pin).

| Pin | Was | Now | Δ | Exact cause |
|---|---|---|---|---|
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["src"]` | 2981 | **2984** | +3 | `identity_env.py` lower-case `framenest` 6→9: one in the module paragraph ("environment file"), two in the `lookup_field_value` paragraph ("compatible spelling"). Verified per file. |
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["tests"]` | 4434 | **4446** | +12 | `tests/unit/test_identity_env.py` 2→8 (+6: docstring "resolver" paragraph, "identity name", "identity value", "canonical name", plus two `framenest_port`/`FRAMENEST_PORT` literals); `test_kronika_identity_dual_read.py` 38→41 (+3); `test_kronika_settings_parity.py` 27→30 (+3). |
| `ENV_PREFIX_TOKEN_COUNT` | 642 | **643** | +1 | one new token `FRAMENEST_PORT` in the new resolver unit test; `ENV_PREFIX_DISTINCT_NAME_COUNT` stays **101** because that name already exists globally (`development.py:47`) — verified by the passing distinct assertion. |
| `ENV_PREFIX_BARE_SPELLING_COUNT` | 18 | **21** | +3 | `identity_env.py` 4→5 (one `` ``FRAMENEST_<SUFFIX>`` `` in the new module paragraph); `test_kronika_settings_parity.py` 0→2 (the two `"FRAMENEST_"` literals in the guard). |
| `CAPITALIZED_OCCURRENCE_COUNT` | 3379 | **3381** | +2 | `test_kronika_identity_dual_read.py` 13→14 (`FrameNestConfigurationError`), `test_kronika_settings_parity.py` 13→14 (`FrameNestSettings`). |

Not moved, and why: `PER_TREE_FRAMENEST_FILE_COUNT` (no path added or removed),
`CAPITALIZED_FILE_COUNT` 482 (no new file carries `FrameNest`),
`ENV_PREFIX_DISTINCT_NAME_COUNT` 101, mutation-header / host-path / unit-account /
console-script pins (no such token added), Part A hashes and the Part B path set.
The ledger file excludes itself from counting, so editing it moved nothing.

## Proof that no executable logic changed

Not an assertion — a machine check. A throwaway probe parsed both
`git show 24bea56:src/framenest/identity_env.py` and the working-tree file, removed
**every** docstring from both abstract syntax trees, re-unparsed and compared the
normalised dumps:

```text
CODE_EQUAL_AFTER_DOCSTRING_STRIP: True
```

Combined with the other two required checks:

```text
git diff --stat c02c675..HEAD -- src/framenest/adapters/api/tailscale_ingress.py   → empty
git diff --stat 24bea56..HEAD  → 5 files, 186 insertions(+), 14 deletions(-)
```

The14 deletions are all inside docstrings (8 in `lookup_field_value`'s paragraphplus the 6 re-pinned scalar lines in the ledger). `pyproject.toml`, `poetry.lock`,
`deploy/**`, `docs/**`, `AGENTS.md`, `src/kronika_capture/**`, the 36 Alembic
revisions and `.ap` were not touched.

## Baseline and final exact counts

| Route | Before (`24bea56`) | After (`02a8048`) |
|---|---|---|
| `./.ap/ap exec --operation test` | `4347 passed, 8 skipped, 3 warnings` in 689.76 s | **`4355 passed, 8 skipped, 3 warnings` in 690.13 s, 0 failed** |
| `node --test tests/*.test.js` | `554 total, 549 passed, 0 failed, 5 skipped` | **`554 total, 549 passed, 0 failed, 5 skipped`** (Node v26.8.2) |
| retention module | 14 passed | 14 passed |
| `./.ap/ap project check --baseline <new>` | — | **PASS** (`02a80485206eeeb33c43393d25514a30d7fe297f`) |

`+8` is exactly the eight tests I added (4 resolver + 2 parametrized per-channel +
1 same-channel + 1 value guard). Skips remain 8, warnings remain 3, same eight
named skips. The baseline run was taken **before** any edit and nothing was edited
while it ran.

## Branch and commits

Branch `feat/kronika-identity-dual-read`, one new local commit, parent `24bea56…`,
not pushed:

```text
02a80485206eeeb33c43393d25514a30d7fe297f  docs(identity): state the resolver's measured precedence and per-channel conflict rule
24bea56daca28603d81cac8d7ed7e3888ba90671  fix(identity): restore pre-cut process-environment parity for old spellings
c02c6753694d5d4958045bb79f80b5eb94b9c75c  fix(identity): exit 2 on an identity-environment conflict at every entry point
90c93eac94171182039a76fbb1c956e42b44da2c  feat(identity): read both KRONIKA_ and FRAMENEST_ spellings, write only the old
18c357cf6f8c5ff9cc3b2c28e638510fc73a3672  docs: record the Kronika sole identity in ADR-0085   (published main, base)
```

Working tree clean after the commit. `.ap` still at `73e20ef…`; public `main` still
`18c357c…`; no remote branch created.

## Deviations, risks, missing evidence

1. **No lint or typecheck run.** `ap.project.conf` declares only `runtime-info`,
   `test` and `test-focus`; there is no declared lint operation, and invoking a
   linter would have meant a command outside the canonical route. Mitigation:
   read-only check that no line I added exceeds 100 characters (only the
   pre-existing SHA-256 literals in the ledger exceed it). No repository linter is
   configured in `pyproject.toml` anyway.
2. **Scope precision in the new module paragraph.** "Per channel" is stated for the
   conflict check. I did not generalise it into a claim about *field value*
   precedence across channels; the cross-channel outcome for a field is decided by
   the library's source ordering, which is cited rather than re-derived.
3. **ADR-0085 untouched.** Verified `grep -niE 'conflict|fail.closed|case'` over
   `docs/adr/0085-kronika-sole-identity.md` → no match. It states no conflict rule,
   so nothing I documented contradicts it and no amendment is needed.
4. **Out of scope, untouched, as instructed:** A3 (the dropped `_env_*` overrides),
   the Part C strengthening (`EXPECTED_FRAMENEST_CONTENT_PATHS`), the redundant
   double fold, F3/F5/H1/H2/H3/D1.
5. **Residual risk, unchanged by me:** a case-variant identity spelling can still be
   silently displaced by a case variant of the compatible spelling in one mapping.
   That is now *documented and test-pinned* rather than fixed, and fixing it would
   require a runtime change, which this correction forbids. C7, which deletes the
   compatible fallback, is where the exposure disappears.
6. **`KRONIKA_HOST` + `framenest_host` is an extra measured case not in the issued
   table** (row L). Included because it shows the same eviction on a security-relevant
   field, and I mention it only as evidence.

## Resolved Execution Issues / Near-Misses

- My first mutation-proof run reported **`empty-identity-is-a-value→empty-test: NOT
  DETECTED`**. The cause was mine: with `framenest_port=9999` present, layer 2 answers
  before layer 3 is ever reached, so the test could not discriminate layer 3's
  empty-means-unset rule. I strengthened the test with two assertions that isolate
  layer 3 (`{"KRONIKA_PORT": ""}` and `{"kronika_port": ""}` → `None`) and re-ran the
  mutation, which is then DETECTED. A test that had shipped in the first form would
  have been decoration. Residual risk: none.
- My first per-channel mutation reported `AttributeError: 'function' object has no
  attribute '__wrapped__'` — a defect in my throwaway probe, which I read as a
  "detection" until I inspected the verdict text. Fixed by calling the parametrized
  function directly; the corrected run shows the real
  `IdentityEnvironmentConfigurationError`.
- I drafted the short-circuit test with a third assertion
  (`{KRONIKA_PORT: 9998, FRAMENEST_PORT: 9999} == "9998") or True`, written before I
  checked that the pair raises. Removed before any run; the conflict case is covered
  by its own test.
- My first `git commit` heredoc attempt and one `ap project check --baseline
  02a8048` (abbreviated SHA) were rejected by their own guards — `--baseline must  be a full lowercase commit object ID`. Re-run with the full SHA: PASS. No state
  changed in either case.
- `rm -rf` on a scratch directory was blocked by the client's deny rule before it
  ran. I used fresh unique `/tmp` subdirectories instead of deleting anything.

## Pre-Existing Failure Classification

none — no repository test failed at any point in this session. The only failures I
observed were (a) the retention module's four Part C assertions *before* the
re-pin, which is the ledger working as designed, and (b) the parity module's
seven failures during the deliberate temporary constant change, both of which I
caused and both of which I reversed. All six probe modules passed; the full suite
is `4355 passed, 8 skipped, 3 warnings, 0 failed`; the JavaScript route is
`549 passed, 0 failed, 5 skipped`.

## Commands beyond the declared routes

Python evidence only through
`./.ap/ap exec --root /home/agile/Projects/kronika --baseline 24bea56… --operation
test` and `--operation test-focus`, plus `./.ap/ap project check` and
`./.ap/ap doctor`. JavaScript: `node --test tests/*.test.js` and `node --version`.
Console-script exit-status probes: `env -i` with `HOME`/`TMPDIR` under
`/tmp/opencode/ksi10/exitA` and a synthetic `FRAMENEST_DATABASE_PATH` under the same
directory, four runs, each verified `created=none` by a before/after listing of that
directory. Read-only Git only: `status`, `rev-parse`, `log`, `show`, `diff`,
`ls-files`, `ls-remote`, `submodule status`, `merge-base`; Git writes limited to
`git add` of five named paths and one `git commit`. Throwaway probe modules and
scratch files exist only under `/tmp/opencode/ksi10/`. One temporary edit of
`src/framenest/identity_env.py:67` was made and reverted inside this session for
the guard demonstration; the file was verified back at `"FRAMENEST_"` before the
commit, and the committed AST proof is against the post-restore content. Nothing
outside `/tmp` was written; no NUC, provider, capture, dependency, credential or
network action occurred.

## Smallest next step

Issue the Part C strengthening as the single bounded grant the re-audit proposed —
add `EXPECTED_FRAMENEST_CONTENT_PATHS` plus its one set-equality test — so C3's
re-pin has a settled ledger to write against; do not start C2's grant before it, and
keep A3, the double fold and F3/F5/H1–H3/D1 out of that grant.

```text
Authority expiry: on submission of this terminal report all authority under this
prompt expires. No further implementation, no push, no publication, no NUC contact,
no ADR-0085 amendment and no later cut is authorized by it.

Orchestration critique:
MEASURED: the issued item-2 table is correct in all six of its rows, but it does not
say that its rows are process-channel rows, and in the environment-file channel the
same inputs behave differently because canonical_identity_environment upper-cases
file keys: "kronika_port=9998" plus "framenest_port=9999" written as an environment
file becomes KRONIKA_PORT plus FRAMENEST_PORT and raisesIdentityEnvironmentConflictError, while "KRONIKA_PORT=9998" plus "kronika_port=9999"
written as a file collapses to one canonical name and resolves to the later entry.
Evidence: the same inputs measured through _DualPrefixDotEnvSettingsSource with an
explicit _env_file; effect: a future reader who treats the table as channel-neutral
will state a rule that is false for one of the two channels the resolver actually
serves; smallest correction: state the scope in the table itself, as the rewritten
docstring now does with "measured on one mapping". Separately, the re-audit's
"silently changes its subject … with no test failing" is not what I measured: with
COMPATIBLE_ENVIRONMENT_PREFIX temporarily set to "KRONIKA_" or to "UNRELATED_", the
new guard fails and so do2 or 7 other tests in that module, because
test_an_old_spelling_name_in_any_case_configures_the_field hardcodes framenest_port;
effect: an Orchestrator may believe the parity module currently has no protection at
all against a constant change and over-weight the guard; smallest correction: record
that the guard pins the subject directly and by name rather than being the sole
defence.
LEAD: lookup_field_value can return the case-folded compatible value even when
lookup_env resolved something else, so the two functions in the same module can
disagree for one mapping (measured: FRAMENEST_PORT=9998 with framenest_port=9999
gives lookup_env "9998" and lookup_field_value "9999"); I did not establish whether
any field-level consumer can observe that disagreement, because every field consumer
passes both arguments to the same function; cheapest useful check: at C7, when the
compatible layer is deleted, confirm that lookup_field_value then equals lookup_env
for every name shape rather than assuming the two collapse.
```