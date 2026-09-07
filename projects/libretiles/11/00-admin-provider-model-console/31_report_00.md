### Report for ORCHESTRATOR_CHAT

Logical whole identity: admin-provider-model-console  
Worker session ordinal: 31  
Worker exchange ordinal: 01

**Status: PARTIAL**  
**Phase-qualified result: not-applicable**

The audit identified an activation overwrite mechanism that can defeat the catalog safety invariants, an unchecked token flag binding, and an informational HTTP-status mismatch. All required verification commands passed. Provider calls remained **ZERO**.

**Core report**

1. Coordinates: recorded above; task `APMC-S8-AUDIT`, fresh independent audit, evidence tier E2.
2. Status: `PARTIAL`; C1–C3 are not accepted as written.
3. Phase-qualified result: `not-applicable`. Logical-whole closure: `not-closed`.
4. Start and end commit: `8853a29eb5e9f937b3db49236cac6ad876db6469`. Both AP pins matched `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; branch remained `main...origin/main`, with empty porcelain status.
5. Changed files: none. No implementation or corrections.
6. Verification: required backend tests **21 passed**; required frontend tests **26 passed**; Ruff, mypy (**99 source files**), typecheck, and lint passed. Independent checks are detailed below.
7. Commit/push: neither authorized nor performed.
8. Deviations/limitations: cache suppression and temporary cache paths preserved audit containment. One initial harness run stopped because its synthetic client lacked a CSRF cookie; the corrected fixture ran successfully. Concurrent PostgreSQL requests and live provider behavior were not exercised.
9. Smallest next step: Orchestrator review of F03 for a bounded correction grant and fresh independent re-audit.
10. Report justification: `new-evidence`.
11. Authority expiry: this report ends the Worker’s authority; no corrections will follow.

Context pressure: moderate; sufficient context remained to complete the bounded audit.

**Security audit scope**

Security task class: focused defensive audit — authN/Z, CSRF, template safety, and provider probe boundary.

Owned/authorized target: Libre Tiles canonical repository at the exact candidate commit, under the supplied read-only audit grant.

Scope: the 24-path diff from `4c524ec3020bbd2f27f2ce32ac160d2c40469c0e`, plus adjacent catalog selection, ordinary admin saves, and installed Django enforcement code.

Exclusions: production infrastructure, genuine provider calls, unrelated gameplay, and corrections; outside this grant.

Source records: candidate Git/source evidence, the pinned AP protocol, installed Django **5.2.17**, and Node **v26.4.0**, inspected on **2026-09-07**. No external security standard was invoked; CWE/ASVS mappings are omitted.

**Threat model**

| Field | Audit model |
|---|---|
| Assets | Catalog activation/order, selectable AI service, review integrity, probe history, credentials, admin sessions |
| Trust boundaries | Browser→admin; review→apply; concurrent database writers; Django→Node; stored strings→HTML |
| Attacker-controlled inputs | POST fields, review tokens, request timing, stored model/probe strings |
| Security properties | Staff/model authorization, CSRF, signed context binding, atomic invariants, immutable history, escaping, isolated probes |
| Abuse cases | Unauthorized mutation, stale confirmation, activation overwrite, forged history, stored XSS, unintended provider execution |
| Attacker profile | Anonymous/non-staff users; restricted staff; authorized catalog editor attempting guard bypass |
| Attack surface | Review/apply/probe endpoints, ordinary AIModel change form, history administration, worker stdin/environment |
| Threat condition | Missing permissions, changed review context, or overlapping catalog writes |
| Technical mechanism | Forged requests, stale signed state, stale ORM saves, unsafe rendering, excessive environment forwarding |
| Blast radius | Global catalog availability/order and administrative observations; potential credential exposure |
| Verification strategy | Required tests, independent synthetic HTTP requests, controlled interleaving, rollback snapshots, source inspection, isolated Node execution |
| Residual risk | Findings below; actual PostgreSQL concurrency and live-provider execution remain untested |

**Claim verdicts**

| Claim | Verdict | Evidence |
|---|---|---|
| C1 | **not accepted** | Authorization and CSRF held. Non-staff requests with valid CSRF returned **302**, not the claimed 403. F01. |
| C2 | **not accepted** | Tampering, expiry, cross-user submission, and replay were refused; accompanying editable fields were ignored. Changing the signed flag state did **not** invalidate the token. F02. |
| C3 | **not accepted** | Apply-path locking and rollback work, but an ordinary admin save can overwrite a valid reviewed activation swap with stale values. F03. |
| C4 | **verified-closed** | Read-only administration, newest-100 retention, atomic insert/prune, and simulated/live labeling verified. |
| C5 | **verified-closed** | Added templates use escaping; hostile strings escaped on controls, change form, changelist, and history. No `safe`, `mark_safe`, or disabled autoescaping found in the audited surfaces. |
| C6 | **verified-closed** | Fake execution avoided subprocess/runtime creation; exact live gate, environment whitelist, and timeout layers verified. Direct Node negative checks produced no provider calls. |
| C7 | **verified-closed** | Seed/sync preserve existing activation/order and use the shared transaction lock before advancing revision. Preservation tests passed; concurrency support is established-static. |
| C8 | **verified-closed** | No diagnostic FK or mutation path found. Worker rejected diagnostic ID, URL, and credential-name fields. Fake execution did not materialize provider credentials. |

Independent HTTP checks, with valid CSRF:

| Actor | Review | Apply with invalid token | Fake probe |
|---|---:|---:|---:|
| Anonymous | 302 | 302 | 302 |
| Non-staff with model permissions | 302 | 302 | 302 |
| View-only staff | 403 | 403 | 403 |
| Change-only staff | 200 | 409 | 403 |
| Probe-only staff | 403 | 403 | 403 |
| Change + probe staff | 200 | 409 | 302 |

Authorized GET requests returned **405** on all three action endpoints; missing-CSRF POSTs returned **403**. History add/change/delete POSTs returned **403 even for a superuser**. An injected pruning failure rolled back both the new observation and admission timestamp.

**Finding F01 — informational claim mismatch**

Relevant source: [admin endpoint wrapping](/home/agile/Projects/libretiles/backend/catalog/admin.py:82).

```text
Finding ID: APMC-S8-AUDIT-F01
Title: Non-staff refusal redirects instead of returning 403
Status: confirmed
Severity: info
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 8853a29eb5e9f937b3db49236cac6ad876db6469
Affected component and exact location: backend/catalog/admin.py:82; installed Django admin/sites.py:233
Security property: Accurate refusal contract; authorization itself held
Asset at risk: Acceptance evidence accuracy
Trust boundary: Non-staff browser to privileged admin endpoints
Attacker-controlled input or local actor: Valid-CSRF action POST
Reachability: All three action endpoints
Preconditions: Authenticated non-staff account
Required privileges: ordinary user
Observed or potential impact: Login redirect (302), not the specified 403; no privileged action executed
C/I/A effect: None demonstrated
CWE mapping: none
ASVS mapping: none
Source-standard references: none
Dynamic reproduction evidence: Synthetic non-staff account with change/probe permissions received [302,302,302]
Static evidence: Django admin_view redirects when is_active/is_staff permission fails
Synthetic containment: In-memory SQLite and synthetic accounts; Worker-owned; discarded at process exit
False-positive analysis: This is a contract discrepancy, not an authorization bypass
Exploitability conclusion: not applicable
Smallest safe correction direction: Reconcile C1 with intended Django refusal semantics
Regression-test requirement: Pin non-staff outcomes with valid CSRF on each endpoint
Residual risk: None identified from the redirect behavior
Acceptance-blocking decision: Non-blocking security discrepancy; C1 cannot pass literally
Redaction requirements: Do not retain real sessions, cookies, or account details
```

**Finding F02 — signed flag state is not enforced**

Relevant source: [token creation](/home/agile/Projects/libretiles/backend/catalog/admin_controls.py:182), [token application](/home/agile/Projects/libretiles/backend/catalog/admin_controls.py:222).

```text
Finding ID: APMC-S8-AUDIT-F02
Title: Review token survives a dynamic-catalog flag change
Status: confirmed
Severity: low
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 8853a29eb5e9f937b3db49236cac6ad876db6469
Affected component and exact location: backend/catalog/admin_controls.py:189,222,245
Security property: Confirmation bound to the reviewed configuration
Asset at risk: Operator review integrity and catalog ordering
Trust boundary: Previously reviewed configuration to current apply context
Attacker-controlled input or local actor: Previously issued valid review token
Reachability: POST /admin/catalog/aimodel/controls/apply/
Preconditions: Same actor, unchanged catalog revision/fingerprint, unexpired token, flag changes
Required privileges: admin
Observed or potential impact: Changes apply under a different flag state without renewed review
C/I/A effect: Review-context integrity affected; no bricking demonstrated through this gap
CWE mapping: none
ASVS mapping: none
Source-standard references: none
Dynamic reproduction evidence: Both false→true and true→false returned HTTP 302 and persisted sort_order=321
Static evidence: dynamic_enabled is signed but never compared during token application
Synthetic containment: In-memory SQLite, synthetic signing key/accounts; discarded at process exit
False-positive analysis: Both flag previews and invariant checks limit impact, but do not enforce the claimed binding
Exploitability conclusion: demonstrated
Smallest safe correction direction: Reject apply when current flag state differs from the signed value
Regression-test requirement: Both flag transitions must return 409 with unchanged database snapshots
Residual risk: Review snapshot consistency and other writers still require consideration
Acceptance-blocking decision: Blocking C2 as written
Redaction requirements: Do not expose real signing keys, cookies, or review tokens
```

**Finding F03 — ordinary saves can undo a safe activation swap**

Relevant source: [AIModelAdmin.save_model](/home/agile/Projects/libretiles/backend/catalog/admin.py:123), [reviewed transaction](/home/agile/Projects/libretiles/backend/catalog/admin_controls.py:265).

```text
Finding ID: APMC-S8-AUDIT-F03
Title: Ordinary admin save can restore stale activation outside catalog coordination
Status: confirmed
Severity: medium
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 8853a29eb5e9f937b3db49236cac6ad876db6469
Affected component and exact location: backend/catalog/admin.py:133-142
Security property: Reviewed activation authority and nonempty/tools catalog invariants
Asset at risk: Global selectable AI catalog and operator decisions
Trust boundary: Ordinary descriptive edit to guarded activation state
Attacker-controlled input or local actor: Authorized ordinary change-form POST and timing
Reachability: POST /admin/catalog/aimodel/<id>/change/ → AIModelAdmin.save_model
Preconditions: Save reads stale activation before another transaction completes a reviewed swap; relevant production configuration is PostgreSQL READ COMMITTED
Required privileges: admin
Observed or potential impact: Stale full-row save can undo activation, leaving zero selectable models and zero active tools models
C/I/A effect: Catalog integrity and AI availability; no confidentiality effect demonstrated
CWE mapping: none
ASVS mapping: none
Source-standard references: none
Dynamic reproduction evidence: Controlled interleaving in the actual change-form POST returned HTTP 302 and produced selectable_count=0, active_tools_count=0
Static evidence: save_model reads without the catalog lock, copies protected values, then calls Django's unrestricted obj.save(); it performs no invariant validation or revision advance
Synthetic containment: In-memory SQLite with synthetic accounts/models; interleaving injected at the existing manager.get read; discarded at exit
False-positive analysis: SQLite concurrent transactions may refuse this schedule. The controlled interleaving proves the overwrite mechanism, not simultaneous PostgreSQL execution. Django's installed PostgreSQL backend defaults to READ COMMITTED
Exploitability conclusion: probable
Smallest safe correction direction: Prevent ordinary saves from writing protected catalog fields and coordinate any required protected writes with the shared lock
Regression-test requirement: Overlap a descriptive save with a reviewed last-model replacement using separate PostgreSQL connections; both outcomes must preserve activation/order and catalog invariants
Residual risk: Other writers and lock-order consistency require focused re-audit
Acceptance-blocking decision: Blocking C3; the accepted safety invariant can be defeated outside the apply transaction
Redaction requirements: Use only synthetic accounts/data; exclude production credentials and connection details
```

The reproduced schedule was: **A inactive / B active → ordinary save reads A → reviewed swap activates A and deactivates B → ordinary save restores A’s stale inactive value**. The swap itself passed validation.

**Containment and residual risk**

| Temporary root / identity | Owner | Mode | Contents | Cleanup owner | Cleanup outcome |
|---|---|---|---|---|---|
| `/tmp/apmc-s8-audit-31-01` | Worker 31 | `0700` | Test/cache artifacts only | Worker 31 | Removed and absence verified |
| Independent audit Python processes | Worker 31 | Memory-only | Synthetic SQLite database, accounts, signing key, hostile strings | Worker 31 | Discarded at exit |
| Direct Node probe processes | Worker 31 | Empty/restricted environment | Synthetic protocol input; fake or live-disabled execution | Worker 31 | Processes exited; no retained artifacts |

No network targets were contacted by the independent probes. Required provider tests used mocks/fakes. No real credentials were printed or forwarded to the directly executed Node workers.

F03 remains the material acceptance risk; its PostgreSQL concurrency behavior needs verification during correction/re-audit. F02 remains an unmet binding requirement. F01 requires claim reconciliation only. No residual risk is accepted by this Worker.

The repository remains unchanged and clean. **Audit authority has expired.**