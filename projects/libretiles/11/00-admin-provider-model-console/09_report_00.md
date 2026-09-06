### Report for ORCHESTRATOR_CHAT

Logical whole identity: admin-provider-model-console  
Worker session ordinal: 09, Worker exchange ordinal: 01

**Status: PARTIAL. R-F01 and R-F03 are verified-closed; R-F02 is not accepted.** The same service JWT can rename its account, then create a product game and join human matchmaking.

Security task class: fresh independent re-audit (INFOSEC 4.11)  
Owned/authorized target: Libre Tiles canonical repository, correction commit `f6c9db913450d56ade4399ec5d2e6a3cd807e347`  
Commit under audit: `f6c9db913450d56ade4399ec5d2e6a3cd807e347`  
Scope: three-file correction; original F01/F02/F03 claims; C3–C10 regression spot-check.  
Exclusions: F04 remains dispositioned residual with a slice-5 obligation; F05/F06 remain rejected-false-positive; INFOSEC 4.6 excluded because this correction introduces no provider surface.  
Independence: fresh session; no implementation contribution or correction performed.

**Threat model**

Assets: account identity and passwords, diagnostic integrity, product games, and matchmaking. Trust boundaries: authenticated bearer → account mutation → player participation; reserved username → managed diagnostic identity; migration reversal → user preservation. Attacker-controlled inputs: registration/profile usernames and authenticated game requests. Required properties: no adoption of password-enabled claimants, no ordinary player participation by the service bearer, and no deletion of password-enabled claimants on reversal.

Measured delta: case variants are distinct users under the tested configuration. The managed identity’s username remains writable, and its JWT remains usable after renaming. Ordinary players were not shown able to obtain a service bearer; the demonstrated bypass requires possessing one.

The original session-07 threat-model text was not supplied, so exact textual equivalence cannot be certified.

**Per-finding verdicts**

| Finding | Verdict | Evidence class and pointer |
|---|---|---|
| R-F01 | **verified-closed** for the password-enabled adoption claim | **reproduced-dynamic**, probes P01–P02, P08, P10, P12–P13; [ensure implementation](/home/agile/Projects/libretiles/backend/game/services.py:1150) |
| R-F02 | **not accepted** | **reproduced-dynamic**, P03–P06 and P09; [username-based guard](/home/agile/Projects/libretiles/backend/game/services.py:1082) |
| R-F03 | **verified-closed**, with the stipulated classification-loss residual | **reproduced-dynamic**, P11–P13; **established-static**, [reverse implementation and documentation](/home/agile/Projects/libretiles/backend/game/migrations/0009_diagnostic_session_foundation.py:18) |

Probe identifiers refer to the inline, synthetic audit executions recorded in this exchange; no probe files were created.

**R-F01 evidence and residual**

- A usable-password claimant caused `ImproperlyConfigured`. Its password, staff/superuser/active flags, preference, groups, and permissions remained intact.
- Repeated ensure calls returned the same managed identity with an unusable password and correct flags. Deliberately altered managed flags and permissions were corrected.
- Actual migration execution with a claimant aborted with: “Refusing to adopt or disable the account.” The migration remained unapplied, its schema changes rolled back, and the claimant survived. Forward migration succeeded once the reserved name was free and seeded the correctly configured account.
- `Libretiles-Diagnostic` registered successfully as a distinct user. The inherited normalization is NFKC, preserving case; the username field has ordinary uniqueness, the lookup uses exact equality, and the guard compares strings exactly. Renaming this separate user to the occupied reserved name returned 400. Its product-game creation returned 201, which is ordinary-user behavior, not service-identity adoption.
- The service bearer can still rename the seeded account and free the name. A subsequent ordinary registration claimed that name; the next diagnostic creation then failed loudly without adopting or disabling the claimant.

Thus fail-closed closes silent password-enabled adoption. The remaining namespace disruption is **bearer-reachable**, followed by ordinary registration, with an operator-visible failure. It is not exclusively an operator-originated condition.

**R-F02 participation enumeration**

| Path | Independent result |
|---|---|
| Create / queue, original reserved username | Both 400 with `ok:false`; zero new session rows. |
| Profile rename → create / queue, same service JWT | Rename 200; create 201; queue 200 and matched an ordinary waiting player. |
| Another player’s game: state, move, pass, exchange, give-up, model/prompt changes, websocket ticket | 404 through membership checks. Another player’s queue cancellation also returned 404. |
| Own diagnostic game: give-up | 200; persisted one `give_up` Move, while the diagnostic run remained `queued`. The service bearer does have diagnostic membership. |
| Own diagnostic game: model/prompt changes | Both returned 200; membership does not exclude this diagnostic session. |
| Diagnostic chat / websocket | Ticket request returned 404; chat service rejected the request. |
| Ordinary-user controls | Create 201; queue 200 with a waiting row; existing create/match/reuse/cancel tests passed. |

The diagnostic-control observations are reported under the requested enumeration; they do not independently re-disposition F04.

**Finding record — surviving F02 bypass**

- Finding ID: APMC-S4-IA-F02
- Title: Service bearer escapes player-participation guard through profile rename
- Status: confirmed
- Severity: medium
- Confidence: high
- Evidence class: reproduced-dynamic
- Affected commit: `f6c9db913450d56ade4399ec5d2e6a3cd807e347`
- Affected component and exact location: [guard](/home/agile/Projects/libretiles/backend/game/services.py:1082), [writable username](/home/agile/Projects/libretiles/backend/accounts/serializers.py:40), [profile PATCH](/home/agile/Projects/libretiles/backend/accounts/views.py:37).
- Security property: diagnostic service bearers cannot participate as ordinary players.
- Asset at risk: identity separation, product sessions, matchmaking.
- Trust boundary: mutable profile attribute controls service-identity authorization.
- Attacker-controlled input or local actor: profile `username`, followed by create/queue requests.
- Reachability: authenticated HTTP endpoints using the same signed JWT throughout.
- Preconditions: possession of a valid service bearer; available replacement username.
- Required privileges: ordinary user — authenticated service-account bearer, without staff/superuser privileges.
- Observed or potential impact: product-game creation and human-match participation by the original managed account.
- C/I/A effect: demonstrated integrity boundary failure; namespace disruption can additionally interrupt diagnostic creation. No confidentiality compromise demonstrated.
- CWE mapping: none assigned.
- ASVS mapping: none assigned.
- Source-standard references: none; repository and installed dependency evidence only.
- Dynamic reproduction evidence: P03 established rejection before rename; P09 reproduced rename 200 → create 201 → matchmaking 200 with the same JWT.
- Static evidence: the guard reads the current username by user ID; profile serialization permits changing that username.
- Synthetic containment: process-local in-memory database and synthetic JWTs; destroyed on process exit.
- False-positive analysis: the successful requests used the original managed account and unchanged bearer, not the separately registered case-variant user.
- Exploitability conclusion: demonstrated.
- Smallest safe correction direction: make participation restrictions survive profile renaming, or prevent the managed identity’s rename under an explicit correction grant.
- Regression-test requirement: authenticate with a service JWT, attempt profile rename, then prove that the same identity cannot create or join product games.
- Residual risk: previously issued service bearers and diagnostic membership need explicit consideration.
- Acceptance-blocking decision: blocking; accepted F02 remains reachable.
- Redaction requirements: never publish real bearers, signing keys, or credential-file contents.

No separate new finding ID was introduced; this is independently reproduced continuation of F02.

**R-F03 evidence**

Historical migration models lacked `has_usable_password`. Their reverse handler preserved the claimant’s identity and password and deleted the unusable managed account. Installed Django’s `has_usable_password()` directly returns `is_password_usable(self.password)`; dynamic comparisons agreed.

The reverse docstring explicitly documents classification loss on rollback. Its following “re-forward as their stored value” sentence must not be treated as a guarantee that a dropped classification survives rollback.

**Regression and validation evidence**

- C3: reproduced 404s in both directions between ordinary players’ product games and the diagnostic identity.
- C6: diagnostic abort persisted zero Moves.
- C8: Git tree comparison established that **all 350 other tracked entries are byte-identical**. Only the declared three files changed. The prompt did not name its four invariant files; the broader comparison covers every unchanged tracked file.
- C10: `create_diagnostic_game`, including `parameters_json`, is structurally unchanged. Inspection found no new secret materialization in the correction diff.
- Other service functions are structurally unchanged; changes are confined to the new guard, create, queue join, and ensure. Existing diagnostic tests cover additional acting-seat and isolation behavior.

Gate summaries, verbatim:

```text
All checks passed!
Success: no issues found in 89 source files
23 passed in 8.31s
4 passed in 1.83s
```

Pytest used plain `-m pytest`, without a second `-q`. Bytecode and tool-cache writes were disabled. No frontend build ran.

**Containment ledger**

Filesystem temporary roots: none used. Process-local SQLite databases, synthetic accounts, groups, permissions, games, and JWTs were owned by this audit; filesystem permission mode: not applicable. Cleanup: transaction rollback/process exit. Independent probes blocked socket connections and used an in-memory channel layer. Credential-file loading was disabled. No network, provider call, development-database write, or credential-file read occurred.

**Limitations and residual-risk summary**

Dynamic evidence uses SQLite and in-process HTTP clients; production PostgreSQL collation and deployment behavior were not exercised. Session-07’s complete report and exact C8 file list were unavailable. No live provider evidence was required.

The fail-closed exception is a sound substitute **for preventing password-enabled claimant adoption**. It is insufficient as a substitute for stable identity enforcement across authorization boundaries: the participation guard still relies on the writable attribute.

**Compact closeout**

- Phase-qualified result: `not-applicable`.
- Start/end commit: both `f6c9db913450d56ade4399ec5d2e6a3cd807e347`.
- Repository gate: expected AP pin verified; porcelain empty at start and end.
- Changed files: none.
- Commit/push result: not-applicable.
- Deviations, risks, missing evidence: as stated above; no correction performed.
- Smallest next step: ORCHESTRATOR issues a bounded correction for the surviving F02 rename bypass.
- Report justification: `new-evidence`.
- Authority expiry: this Worker’s task authority expires upon this report. Slice-4 acceptance remains the ORCHESTRATOR’s decision.

Resolved Execution Issues / Near-Misses: two migration-harness errors—an assumed table name and use of the current-model deletion collector against rolled-back schema—were resolved within synthetic memory fixtures. Final migration probes passed.

Pre-Existing Failure Classification: surviving F02 security failure; no test-suite or backend-gate failures.

Orchestration critique: **MEASURED:** narrowing corrected silent adoption but left a demonstrated authorization bypass through mutable identity. **LEAD:** the next correction should preserve the restriction across identity changes and test the complete JWT/profile/game sequence.

Enumeration widened: only the explicitly requested bearer-path checks; diagnostic membership disproved the prompt’s “none owned” assumption.