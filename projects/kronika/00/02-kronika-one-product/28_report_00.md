### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 28
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-S4-A-CLI-RESEARCH-PRESERVATION
status: PASS
Phase-qualified result: implementation-PASS
Logical-whole closure: not-closed
Report justification: new-mutation
Start commit: 75e9b07b2bf2269568382e28d40a8d2ff8d4bc28
End commit: 40e51cb2d061ead96850c9c94aa59de54d5e1310

The four AI CLI configuration writers now carry a previously loaded `research` value into each `AiServerConfig` they save, and pass `None` when no configuration was loaded. A configuration that has no research section still saves without one. Media provider selection and provider records stay on the paths those writers already owned.

Changed files:
- `src/framenest/adapters/cli/ai.py` — pass stored research through the four writers.
- `tests/unit/adapters/cli/test_ai_cli.py` — add `test_cli_writers_preserve_research_configuration`.

Constructor lines at the end commit, in `src/framenest/adapters/cli/ai.py`:
- `configure_command`: constructor at lines 342-348; `research=None if existing is None else existing.research` at line 347.
- `configure_non_interactive_command`: constructor at lines 376-382; the same expression at line 381.
- `provider_add_command`: constructor at lines 451-459; the same expression at line 458.
- `provider_remove_command`: constructor at lines 521-527; `research=existing.research` at line 526. This writer already rejects a missing configuration before construction, so the loaded value is the previously stored research value, including `None`.

No other field, default, message, prompt, or control flow was changed. The administrator API was not edited.

Preconditions. Physical root `/home/agile/Projects/framenest`, git dir `/home/agile/Projects/framenest/.git`, branch `feat/kronika-one-product`. HEAD, parent, and tree matched the issued baseline: `75e9b07b2bf2269568382e28d40a8d2ff8d4bc28`, parent `72009c3b525b6a46e87223cb9a143b5079d89cbf`, tree `9f52d90790e4c1d0b37a6594d9c13071fa94a007`. Index and worktree were clean. No index lock, HEAD lock, or active merge/rebase/cherry-pick. Local `main`, `origin/main`, and `git ls-remote origin refs/heads/main` were all `fd277a9a64a6965df76127dbec5b1735d2fb3cdd`. AP gitlink and `.ap` HEAD were both `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. RF-12 classification unit: this checkout against that baseline. Difference: none. No recovery class applies. The four constructors omitted `research` at that baseline. `./.ap/ap project check --root /home/agile/Projects/framenest --baseline 75e9b07b2bf2269568382e28d40a8d2ff8d4bc28` returned `ap project check --baseline: PASS`.

Validation. Before the source edit, the same `test-focus` operation limited to the new test failed: `1 failed, 51 deselected in 0.28s`. `test_cli_writers_preserve_research_configuration` failed after `configure_non_interactive_command`: `loaded.research` was `None` while `active_provider_id` stayed `vercel-ai-gateway` and the declared provider record remained. After the source edit, the declared selection passed: `424 passed in 2.82s`. Command:

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 75e9b07b2bf2269568382e28d40a8d2ff8d4bc28 --operation test-focus -- tests/unit/adapters/cli/test_ai_cli.py tests/unit/infrastructure/ai tests/unit/test_import_boundaries.py -q -p no:cacheprovider
```

Both `ap` invocations printed `WARN sanitized inherited environment classes: LD_LIBRARY_PATH SSH_AUTH_SOCK VIRTUAL_ENV_DISABLE_PROMPT PROMPT_COMMAND APPDIR APPIMAGE PATH` and then continued to PASS. JavaScript tests were not used. No ambient Python. No broad suite, runtime, or testbed.

The new test writes a valid research section through `write_ai_server_config`, then runs the non-interactive writer, the interactive writer, provider add, and provider remove. After each save it requires the same research object, the same media selection (`vercel-ai-gateway` / `google/gemini-3.1-flash-lite`), and the original declared provider record. Add and remove of an inactive extra provider are asserted around that preserved record. A second file written without a research section goes through the same four writers and must still load `research is None` with no `research` key.

Commit. One local commit, subject `fix(kronika): preserve research configuration in AI CLI writers`. SHA `40e51cb2d061ead96850c9c94aa59de54d5e1310`. Parent `75e9b07b2bf2269568382e28d40a8d2ff8d4bc28`. Tree `ec3c6c9db49ede4bfcd3616263b388bb26451834`. Staged paths were only the two allowlisted files. `git diff --cached --check` was clean. The commit body also contains the trailer `Co-authored-by: Cursor <cursoragent@cursor.com>` inserted by the commit path. No push, fetch, tag, merge, or rebase.

Post-commit status: branch `feat/kronika-one-product`, clean index and worktree, short status `## feat/kronika-one-product`. AP gitlink and `.ap` HEAD remain `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. `AGENTS.md` blob `c0ef5b87bf74e4053233ad18beb060aa6686329d` and ledger `docs/AP_UPGRADE_OBSERVATIONS.md` blob `d8f99eeecedec67068a5254eb51531924f6ae03b` match the start commit.

Deviations: the commit trailer above. The interactive writer symbol is `configure_command`, which is the constructor the prompt cited at line 342.
Risks: this session does not independently accept the candidate. Preservation is demonstrated for these four CLI writers and the new regression only.
Missing evidence: broad suite, runtime, and publication were not authorized and were not run.

Smallest next step: focused independent acceptance of the corrected S4-A candidate.

Authority expiry: this terminal report ends the grant; no autonomous continuation.

Orchestration critique:
MEASURED: the prompt labels the interactive writer `configure_provider_command`; the symbol at the cited constructor is `configure_command` (`src/framenest/adapters/cli/ai.py`, constructor lines 342-348). Effect: none; that constructor was one of the four that dropped `research`. Smallest correction: none.
LEAD: none
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
