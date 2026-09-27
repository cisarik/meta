### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 31
Worker exchange ordinal: 01

Status: PARTIAL
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence
Persistent role identity: WORKER
Task identity: KRONIKA-ONE-PRODUCT-S6-EXECUTION-PLAN
Worker session profile: Planner
Phase: planning
Delivery route: manual Cooperator delivery
Planning cycle: initial; no second planning cycle performed
Plan disposition: approval-gated
Implementation in this Worker session: prohibited

## 1. Compact core and disposition

This report provides a concrete schema and service design, a verified inventory of direct audience-seam test fixtures, a candidate file catalogue, an access-inventory design, and the E3/R3 route. It does NOT provide a decision-complete, issuable S6 implementation envelope. Three material mappings remain open in section 9: complete upload/acquisition authorization and its test fallout; approved-projection integration across existing readers and writers; and the live database private-state boundary. The implementation prompt in section 11 is consequently a withheld draft, not authority. Do not issue it by treating these gaps as discretionary implementation work.

Observed repository state at opening and finishing inspection:

```text
Repository: /home/agile/Projects/framenest
Branch: feat/kronika-one-product
Start HEAD: 40e51cb2d061ead96850c9c94aa59de54d5e1310
End HEAD:   40e51cb2d061ead96850c9c94aa59de54d5e1310
Local main:        40e51cb2d061ead96850c9c94aa59de54d5e1310
Local origin/main: 40e51cb2d061ead96850c9c94aa59de54d5e1310
AP gitlink and checkout: 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
Working tree: clean; git status --short --untracked-files=all emitted no entries
Implementation files changed: none
Tests, builds, interpreters and package managers executed: none
Commit, staging, push, remote configuration and network contact: none
Host, browser, provider and credential actions: none
Subagents: none
private/**: not read
Only persisted artifact: this terminal report, outside the project checkout
```

Evidence for these state statements is direct read-only Git command output in this session, not a source-code inference. Equality with the current public remote branch was NOT independently observed: `origin/main` above is a local ref. The issuance claim about public main is not promoted into fresh public evidence. This distinction follows `.ap/AP_WORKER.md:257-260`.

The task attachment, its one-cycle planning contract, and the subsequent instruction to continue are current task authority. The accepted prior report is historical evidence supplied by that authority. The current architecture is ADR-0083; neither roadmap entries nor this report grant execution (`AGENTS.md:12-29`, `AGENTS.md:43-48`). The initial client planning mode was subsequently changed to Default by a developer instruction. Work nevertheless remained planning-only; the change enabled only the already authorized report write, not implementation.

## 2. Citation key, reading and established boundaries

Unless an absolute path is given, every source path below is relative to `/home/agile/Projects/framenest` at baseline `40e51cb2d061ead96850c9c94aa59de54d5e1310`. Line numbers are baseline locators. Proposed files and behavior are explicitly proposals, not claims that code exists.

Citation abbreviations: `domain/`, `application/`, `adapters/` and `infrastructure/` expand under `src/framenest/`; `persistence/` expands under `src/framenest/infrastructure/`. A bare `*_api.py` or `tailscale_ingress.py` expands under `src/framenest/adapters/api/`; a bare `*_repository.py`, `catalog_schema.py`, `engine.py` or `migrations.py` expands under `src/framenest/infrastructure/persistence/`. The bare 0033 migration filename expands under that persistence directory's `alembic_environment/versions/`. Test basenames inherit the exact test path in their table row. These are path abbreviations, not additional sources.

- P5: `/home/agile/meta/projects/kronika/00/02-kronika-one-product/25_report_00.md:356-423`: accepted records, ownership, access, approval and history requirements. In particular, `:371-387` specifies record invariants and private storage; `:391-401` specifies the caller matrix and all-surface coverage; `:405-423` specifies approval and timeline behavior.
- P7: the same trace file `:498-520`: active order and separate S6/S4-B/S7-P boundaries. S6 requires migration, all-route authorization, conflicts, public exclusion and fresh E3/R3 review. S7-P owns common completion, history APIs, media integration and rendering.
- A83: `docs/adr/0083-modular-research-providers-and-administrator-curated-timeline.md:153-209`: immutable completed Q/A, unfinished personal history, deliberate administrator read-all, explicit approval, previous approved projection, internet exclusion, separate working Gallery and approved-only Timeline.
- SQL conventions: `src/framenest/infrastructure/persistence/catalog_schema.py:103-144`, `:1529-1689`, `:2107-2155`; `src/framenest/infrastructure/persistence/alembic_environment/versions/0033_media_analysis_proposals.py:14-84`. These use SQLAlchemy Core, Text identifiers, Integer millisecond timestamps, named checks/FKs/indexes and explicit upgrade/downgrade. The UUID-length database check is not a full UUID validator.
- Transactions: `src/framenest/infrastructure/persistence/engine.py:23-48`, `:127-160`: hidden SQL parameters, FK enforcement, transaction rollback and BEGIN IMMEDIATE support. `src/framenest/infrastructure/persistence/migrations.py:76-109`, `:137` resolves the packaged head; there is no reason to rewrite old migrations to advance it.
- Identity: `src/framenest/domain/identity_access.py:21-45`, `:106-139`, `:178-213`: server-produced IdentityContext, normalized login key and role/capability mapping. A membership or client ownership string is not sufficient authority (A83 `:176-179`).
- Adjacent S4-A conventions: `src/framenest/domain/research.py:14-19`, `:441-522`, `:575-610`, `:683-712`; `src/framenest/application/ports/research.py:1-76`; `src/framenest/infrastructure/ai/configuration.py:28-78`, `:157-211`, `:259-288`; `src/framenest/infrastructure/ai/research_registry.py:1-181`. Keep these accepted pure contracts and schema v3 unchanged. In particular, operation_id is a bounded token, not a UUID (`domain/research.py:590-591`); completion is validated independently of rendering (`:459-491`, `:683-699`).
- AP: `.ap/AP.md:384-537` (RF-19), `:544-606` and `:1005-1117` (planning/authority), `:1467-1492` (E3), `:1794-1832` (Worker), `:2301-2366` (validation), `:2940-2983` (stops); `.ap/AP_WORKER.md:233-280`; `.ap/PROMPT_CONTRACTS.md:14-94`; `.ap/INFOSEC.md:70-110`, `:120-153`, `:362-394`. Implementation evidence is non-independent; authorization acceptance must use a fresh independent session.

The required direct audience-seam test files listed in section 7 were read through, including helpers and downstream assertions. Source searches were also used to discover callers, migration-head assertions and additional route families. Discovery is not represented as full reading or complete mapping of every test in those additional families; the distinction is central to PARTIAL.

## 3. Proposed migration 0034

Revision name: `src/framenest/infrastructure/persistence/alembic_environment/versions/0034_kronika_records.py`; revision `0034`; down_revision `0033`; no branch labels/dependencies. Recheck that 0034 remains free at issuance. Mirror its table definitions in `catalog_schema.py`. Use the existing catalogue, no second database and no provider dependencies (P5 `:360-369`; SQL conventions above).

### 3.1 Proposed `kronika_documents`

This table contains completed immutable Search/Research documents only. It must not become a substitute for pending/failed durable requests in 0035. The following columns are a design proposal grounded in P5 `:371-387`, A83 `:153-163`, and the S4-A bounds in `domain/research.py:14-19`, `:441-522`.

| Column | SQL type/nullability | Constraint or meaning |
|---|---|---|
| id | Text, PK, NOT NULL | UUID value; named length-36 check; full version/format validation in domain |
| operation_id | Text, NOT NULL, UNIQUE | Original research operation token, length 1..128; do not impose UUID format |
| kind | Text, NOT NULL | CHECK search or research |
| question_text | Text, NOT NULL | Complete original submitted question; nonblank application validation; UTF-8 byte length 1..16384 |
| answer_text | Text, NOT NULL | Complete final answer; nonblank application validation; UTF-8 byte length 1..2097152 |
| citations_json | Text, NOT NULL | Canonical JSON array of normalized citation values; count <=200, URL/title byte bounds 2048/300; structure and safe URL validation in domain/service |
| completion_evidence_json | Text, NOT NULL | Only normalized CompletionEvidence fields needed to revalidate completeness; no raw response, reasoning stream, provider handle or credential |
| created_at_ms | Integer, NOT NULL | Original admission time, >=0 |
| completed_at_ms | Integer, NOT NULL | >= created_at_ms; completion time, not approval time |

Use named `pk_kronika_documents`, `uq_kronika_documents_operation_id`, checks prefixed `ck_kronika_documents_`, and a UNIQUE `(id, operation_id, kind)` parent key for the record/document composite FK. Byte checks use `length(CAST(... AS BLOB))`, not character counts. JSON structure, URL semantics and CompletionEvidence remain application checks; no new SQLite JSON-extension requirement. Invalid persisted documents fail closed and return a sanitized storage-integrity error; never truncate or reinterpret them as valid completion. These choices preserve the distinction between bounded normalized data and raw provider output in P5 `:385-387`, `:443` and `domain/research.py:441-522`.

### 3.2 Proposed `kronika_records`

| Column | SQL type/nullability/default | Constraint or meaning |
|---|---|---|
| id | Text, PK, NOT NULL | UUID; named length-36 check, domain UUID validation |
| kind | Text, NOT NULL | CHECK media/search/research |
| owner_login_key | Text, NOT NULL | Normalized verified server identity; SQL login-key checks following 0033; never client-selected |
| visibility | Text, NOT NULL, server default private | CHECK private/family; no public enum value |
| media_id | Text, NULL, UNIQUE | FK logical_media.id, ON DELETE RESTRICT; length 36 when present |
| document_id | Text, NULL, UNIQUE | Part of FK to completed document; length 36 when present |
| final_operation_id | Text, NULL, UNIQUE | Final operation binding, token length 1..128; part of document composite FK |
| created_at_ms | Integer, NOT NULL | >=0; record origin/admission timestamp |
| completed_at_ms | Integer, NULL | >= created_at_ms when present; NULL is allowed only for unfinished media |
| timeline_entered_at_ms | Integer, NULL | First approval time; >= completed_at_ms when present; retained after withdrawal |
| version | Integer, NOT NULL, server default 1 | >=1, optimistic concurrency token |
| latest_successful_analysis_run_id | Text, NULL | FK media_analysis_runs.id, ON DELETE RESTRICT |
| approved_analysis_run_id | Text, NULL | FK media_analysis_runs.id, ON DELETE RESTRICT; previous success can differ from latest |
| approved_by_login_key | Text, NULL | Same normalized-login checks as owner when present |
| approved_at_ms | Integer, NULL | >= completed_at_ms and >= timeline_entered_at_ms |
| approved_record_version | Integer, NULL | Positive and <= current version; identifies the approved record state |
| approved_projection_json | Text, NULL | Versioned, immutable-at-approval normalized snapshot; retained until explicit reapproval |

Required checks (design under P5 `:371-423`; SQL conventions above):

1. Media has media_id and no document_id/final_operation_id; Search/Research has document_id and final_operation_id and no media_id. Use explicit IS NULL/IS NOT NULL branches so SQL NULL semantics cannot make a malformed row pass.
2. Composite FK `(document_id, final_operation_id, kind)` references `kronika_documents(id, operation_id, kind)` with RESTRICT. This enforces consistent final binding and document kind without referencing nonexistent 0035 tables. 0035 must later bind its durable request to this same operation and record; do not claim 0034 already enforces request existence.
3. Search/Research requires completed_at_ms and forbids both analysis-run references. Media may start incomplete. Completion and document/record timestamp agreement are validated in the transaction as well as local timestamp checks.
4. Approval actor/time/version/projection are all absent or all present. A present approval requires completion and a timeline timestamp; media approval additionally requires an approved run. Family requires that full approved state. Private may retain it after withdrawal. No implicit approval when owner is an administrator.
5. Both analysis IDs have UUID-length checks. FK existence alone does not prove that a run belongs to this media or succeeded: repository approval/completion transactions must query the run, require matching media_id, successful analyzed state and valid stored result. Do not describe this as database-enforced cross-row state validation. Existing successful-run payload checks are at `catalog_schema.py:1642-1669`.
6. Normalize owners using the domain identity function. The SQL lowercase/whitespace checks follow `0033_media_analysis_proposals.py:14-21`; they do not substitute for Unicode casefold/control validation in `domain/identity_access.py:121-139`. No owner FK to a nonexistent local accounts table.
7. Do not provide an update-owner or update-completed-document repository operation. Direct database administration is outside the application access boundary; tests must exercise the repository contract as well as raw SQL constraints.

Indexes: unique media/document/final-operation bindings; `(owner_login_key, created_at_ms DESC, id ASC)` for personal record history; `(created_at_ms DESC, id ASC)` for administrator history; `(visibility, timeline_entered_at_ms DESC, id ASC)` for approved Timeline; indexes on each analysis FK for reference/removal checks. Queries still explicitly order `timeline_entered_at_ms DESC, id ASC`; indexes are not ordering authority. Use stable `ix_kronika_records_*` names following 0033 naming, plus named PK/FK/unique/check constraints. This is the proposed physical realization of P5 `:380-381`, `:423`.

### 3.3 Upgrade, downgrade, data and transaction scope

Upgrade creates the two tables and indexes only. It must not create common records for existing logical_media, assign historical rows to an administrator, or translate legacy publication into family approval. Preserve a populated synthetic 0033 catalogue byte-for-value at the logical row level. Historical backfill is explicitly rejected by P5 `:383` and is not required by the create-only 0033 convention (`0033_media_analysis_proposals.py:25-26`).

Proposed downgrade policy: refuse before DDL if either new table contains rows; otherwise drop record indexes/table before document indexes/table and return to 0033. Test empty downgrade/re-upgrade and populated refusal with unchanged head/tables/data. This is deliberately stricter than the historical 0033 drop-only downgrade (`:74-84`), to avoid silently deleting private history. It is a proposed recovery guard, not a claim that Alembic guarantees whole-DDL rollback on every platform. Deployment and restore over existing host data remain outside S6 (P7 `:518`, `:522`).

Media insertion must eventually bind ownership in the SAME transaction. Existing insertion sites are `media_repository.py:152-161` and `upload_publication_repository.py:552-603`, with the latter committing publication/session state in its immediate transaction (`:657-706`). S6 should supply a transaction-bound infrastructure helper and its synthetic rollback tests; S7-P wires real insertion/completion flows and their verified/configured owner inputs. Calling a second engine-backed record repository after media insertion would not meet P5 `:383`. No real ingestion cutover or ownership backfill is authorized by this plan.

## 4. Domain, policy, service and history design

### 4.1 Placement and caller matrix

Propose pure `domain/records.py` for RecordId, DocumentId, RecordKind, visibility, immutable document and record snapshots, completion/approval values and sanitized errors. Propose pure `domain/record_access.py` for validated caller/access-scope values and decision functions. Place the application port in `application/ports/records.py`, use cases in `application/records.py`, and SQL implementation in `infrastructure/persistence/record_repository.py`. SQL predicate construction belongs in `infrastructure/persistence/record_access.py`, not in domain/application. This follows existing separation between `domain/content_publication.py:1-64`, `application/content_publication.py:38-137`, `application/ports/content_publication_repository.py:118-137` and the existing persistence adapter.

| Context | Own private/incomplete | Other owner's private/incomplete | Approved family | Approve/withdraw |
|---|---|---|---|---|
| Verified ordinary member | allow | deny | allow approved projection | deny |
| Verified application administrator | allow | allow | allow; Timeline still approved-only | allow explicit service action |
| Missing/malformed/unmapped identity | deny | deny | deny | deny |
| Public reader composition | deny | deny | deny | deny |

This is the accepted matrix, not a new privilege decision (P5 `:391-401`; A83 `:165-201`). Administration is explicit server-derived role/capability authority; ownership alone never grants approval. An admin read scope must not turn the shared Timeline into an all-record inventory. Personal history uses own owner key even for an administrator; an explicitly separate admin inventory uses read-all.

For bound media, the common-record decision has precedence over old publication and upload/YouTube/X contribution claims. A denied bound record never falls back to a legacy grant. For unbound legacy media only, preserve verified legacy requester/admin/publication behavior as compatibility until the separately authorized empty-catalog transition. Anonymous access to new records is never a compatibility exception. `ContentAudiencePolicy` currently grants admin existence, then legacy publication, then requester access (`application/content_publication.py:47-73`); this order must be replaced for bound records.

### 4.2 Fail-closed seam and SQL filtering

`content_audience_allows` must return false when policy or valid identity is absent before invoking any permissive test double. Existing callers then retain their sanitized not-found response. Preserve sanitized unavailable/error mapping for repository failure; do not turn infrastructure failure into allow. The baseline permissive branch is exactly `adapters/api/content_audience_api.py:19-33`. Keep optional dependency fields as representable misconfiguration so negative tests can prove denial; do not silently fill explicitly supplied incomplete dependency objects with a permissive policy in create_app (`adapters/api/application.py:426-485`, `:548-572`).

Production composition injects one real record-aware policy backed by the same catalogue engine. Tests of downstream formatting/playback may inject an explicit bounded policy permitting only their known media IDs plus an explicit synthetic IdentityContext. Security evidence uses real policy and real disposable SQLite rows. A global autouse administrator, always-allow default, None fallback, or monkeypatch bypass is not a permitted fixture migration. Full direct-seam inventory is in section 7.

Direct object checks are insufficient for list confidentiality. Carry a typed server-derived access scope into `ListMediaCatalog` and `MediaCatalogQuery`; default missing scope denies, while public composition explicitly selects legacy-public scope. SQL must restrict membership before count, search, pagination, tag facets and result loading. Current list execution passes published_only=True without an identity (`application/media_catalog.py:47-82`); the API list route lacks a direct audience check (`adapters/api/media_catalog_api.py:115-178`); SQL membership comes from publication/companion conditions (`persistence/media_catalog_repository.py:254-407`). These are separate integration points, not automatically repaired by changing the helper.

The same central SQL semantics must override contribution-based workspace/companion paths. Workspace currently unions upload/YouTube/X contribution IDs (`media_attribution_repository.py:279-312`) and counts selected rows (`:79-135`). Companion owns separate history predicates and unopened counts (`companion_review_repository.py:143-183`, `:646-722`). Bound-record ownership is authoritative; an old cross-owner contribution claim must neither grant history access nor inflate counts. Admin inventory remains read-all under its verified admin capability. Explicit query parity tests must compare domain decisions with SQL-selected IDs.

### 4.3 Approval, withdrawal and concurrency

Proposed service operations: authorized detail/history/timeline/admin-inventory reads; prepare approval candidate; approve candidate; withdraw approval. Keep HTTP record/history/render APIs out of S6. Proposed port operations accept a validated caller and exact expected version/candidate, not caller-supplied owner/approver fields. All decisions and writes occur inside one immediate transaction using the existing `engine.py:143-160` boundary. These choices implement P5 `:405-423`.

Approval sequence:

1. Verify application administrator before loading content; fetch record and check expected version. Missing/unauthorized object reads share sanitized not-found behavior; an authenticated ordinary caller cannot approve even its own record.
2. Revalidate complete immutable document or successful media run for the same media. Media also requires persisted nonblank title/description and >=1 canonical tag, reusing `derive_content_publication_readiness` (`domain/content_publication.py:43-64`). Successful analysis never silently applies suggestions.
3. For media, prepare/read a candidate containing record version, latest successful run ID and a deterministic digest of the exact persisted approval metadata/projection. Recheck that digest inside approval's write transaction. Record version alone cannot detect unrelated legacy metadata writes unless every such writer increments it; the unresolved integration is called out in G2 below.
4. Save the normalized approved projection and selected analysis ID; set visibility family; set approval actor/time and approved version; increment record version exactly once; set timeline_entered_at_ms only if NULL. Own-admin records follow the same action. Persist no raw provider payload or hidden reasoning.
5. On exact already-approved candidate replay with the SAME current version and same projection/run, return an explicit no-change result. Otherwise stale expected version is a conflict, including a retry carrying the old pre-commit token. No silent last-writer-wins approval.

Withdrawal requires administrator and current version; changes family to private, increments once, and retains the completed document, approved projection/provenance and first-entry time. An already-private current-version request is a no-change result; a stale token remains conflict. The service returns the current token to authorized callers without leaking record existence to denied callers. No new approval HTTP response contract is shipped in S6.

A new successful analysis can advance latest_successful_analysis_run_id and record version, while approved_analysis_run_id/projection/time remain unchanged. A failed rerun changes neither previous success nor approved projection. Reapproval replaces the approved snapshot on the same record/card without changing timeline order. Older run rows referenced by either pointer cannot be deleted accidentally because FKs restrict deletion. The remaining integration of these updates with actual analysis/metadata readers and writers is G2; storing two pointers alone is not sufficient to claim the behavior (P5 `:417`; A83 `:187-190`).

Legacy `PUT /api/admin/media/{media_id}/content-publication` must reject both publish and unpublish for a bound record with a typed conflict before any mutation. Choose rejection in S6, rather than silently adapting an old body that lacks the exact common-record version. The repository must check binding within the same write transaction, not only in the adapter. Existing publish/unpublish transactions are at `persistence/content_publication_repository.py:229-305`. Companion metadata apply must not substitute for approval; its current result derives legacy publication status without automatically publishing (`companion_review_repository.py:545-600`). Bound-record responses must not advertise a stray legacy row as household approval (P5 `:421`).

### 4.4 History and deferred work

S6 supplies private common-record history queries, explicit admin inventory and approved-only timeline query foundations. Order personal/admin history by creation time DESC then id ASC; Timeline by first-entry time DESC then id ASC; default 24/max100. Queries filter before totals and paging. A completed save is private and adds no shared card. A withdrawn record remains in personal/admin history (P5 `:405-423`; A83 `:198-209`).

Pending/failed Search/Research entries cannot be fabricated as completed records. Original question and truthful lifecycle live in 0035 requests, then S7-P combines them with completed records without duplicate entries. S6 reserves the final operation binding; it does not implement S4-B request persistence, provider runtime, budgets or credentials. S7-P implements the atomic request/document/record/final-binding completion, real media ownership/success integration, record/history APIs and safe rendering. S8 implements Timeline/History/forms/review UI. Capture, S3 remainder, S5 and S7-C remain parked (P7 `:503-520`; `AGENTS.md:18-29`).

## 5. Candidate file catalogue and explicit exclusions

This is an EXACT-PATH candidate catalogue, not a claim of a complete implementation allowlist. Sets N, P, T and H below are established proposals. Set G in section 9 is unresolved and therefore NOT implicitly authorized. An issuable next grant must replace this partial catalogue with a closed complete list; the implementer may not interpret it as permission to edit surrounding directories.

### N: proposed new files

```text
src/framenest/domain/records.py
src/framenest/domain/record_access.py
src/framenest/application/ports/records.py
src/framenest/application/records.py
src/framenest/infrastructure/persistence/record_repository.py
src/framenest/infrastructure/persistence/record_access.py
src/framenest/infrastructure/persistence/alembic_environment/versions/0034_kronika_records.py
tests/support/record_access.py
tests/unit/domain/test_records.py
tests/unit/domain/test_record_access.py
tests/unit/application/test_records.py
tests/integration/persistence/test_kronika_records_migration.py
tests/integration/persistence/test_kronika_record_repository.py
tests/contract/test_kronika_record_authorization.py
tests/contract/test_kronika_access_inventory.py
docs/KRONIKA_ACCESS_INVENTORY.md
```

These are proposed placements, based on the existing domain/application/port/adapter separation cited in section 4.1 and the accepted S6 row, not assertions that these files exist. The support module provides opt-in synthetic identities and scoped test policies, never production bypasses. The two contract files separate executable authorization attempts from route/inventory completeness; neither substitutes for the independent audit.

### P: established existing production/documentation integration paths

| Exact path | Proposed change and baseline evidence |
|---|---|
| src/framenest/infrastructure/persistence/catalog_schema.py | Mirror 0034 tables/checks/indexes; existing logical media/run/proposal conventions at :103, :1529, :2107 |
| src/framenest/application/content_publication.py | Record-first ContentAudiencePolicy and typed bound-publication refusal; :38-137 |
| src/framenest/application/ports/content_publication_repository.py | Typed bound-record conflict/result contract for legacy publication; :99-137 |
| src/framenest/infrastructure/persistence/content_publication_repository.py | Bound-record exclusion from legacy is_published and atomic publish/unpublish refusal; :61-95, :229-305 |
| src/framenest/adapters/api/content_audience_api.py | Missing policy/identity deny; :19-33 |
| src/framenest/adapters/api/application.py | Inject shared real record-aware policy and query scope dependencies; :426-485, :548-572, :612-673, :772, :839 |
| src/framenest/adapters/api/content_publication_api.py | Sanitized bound-publication conflict; route :205-206 |
| src/framenest/application/media_catalog.py | Explicit access-scope input; :47-82 |
| src/framenest/application/ports/media_catalog_repository.py | Typed query scope, no permissive missing scope; :16-35 |
| src/framenest/infrastructure/persistence/media_catalog_repository.py | Shared access predicate before count/search/paging, explicit legacy-public exclusion; :43-170, :254-407 |
| src/framenest/adapters/api/media_catalog_api.py | Verified list scope and approved projection selection requirement; :115-178, :189-220 |
| src/framenest/application/companion_picker.py | Pass verified scope rather than treating requester login alone as general record authority; :78-105 |
| src/framenest/infrastructure/persistence/media_attribution_repository.py | Common owner precedence in workspace list before counts; :79-135, :279-312 |
| src/framenest/infrastructure/persistence/companion_review_repository.py | Owner precedence in own history/open state; bound publication-status semantics; :143-183, :341, :545-600, :646-722 |
| src/framenest/infrastructure/persistence/analysis_proposal_repository.py | Transactional bound-record authorization before proposal insertion; currently existence-only :48-61 |
| src/framenest/application/analysis_proposal.py | Pass server-derived authorization context for proposal; :50-76 |
| src/framenest/application/ports/analysis_proposal.py | Carry the matching proposal authorization contract; :57-69 |
| src/framenest/adapters/api/analysis_proposal_api.py | Supply verified scope, preserve rate/audit/capability behavior; identity gate :119, admin gate :178 |
| src/framenest/infrastructure/persistence/media_metadata_repository.py | Public tag query excludes every bound media record, even with legacy publication row; :124-145 |
| src/framenest/adapters/api/public_published_application.py | Exact reader schema pin 0034 and explicit legacy-public query scope; :59, :107-152 |
| src/framenest/adapters/api/public_published_api.py | Pass explicit public scope on list; direct public guards remain record-excluding; :217-275, :279-349 |
| README.md | Current implemented schema sentence only, plus bounded S6 status; :79 |
| PRODUCT.md | Current implementation summary only; :98 |
| SPEC.md | Current head/status and precise S6-vs-future boundary; :7, :24; preserve historical 0033 description :1196 |
| ROADMAP.md | Current head summary and truthful S6 implementation-evidence state; :178; do not claim accepted/deployed |
| docs/INFOSEC.md | Update current reader-pin checklist/rule :127, :228; preserve historical audit/finding evidence at :46, :56 |

Projection edits to existing adapter families are not silently covered by P; their missing end-to-end mapping is G2. Similarly, permission/storage edits are not inferred from the ability to add tables.

Explicit exclusions:

- `.ap/`, `ap.project.conf`, dependency manifests/lockfiles and environment tooling: no protocol/toolchain/dependency change; declared route is already defined (`AGENTS.md:47-58`, `ap.project.conf:1-32`).
- Old migration files, including 0033: immutable history; only current-head tests change. No 0035 file in S6 (P5 `:364-369`).
- `domain/research.py`, `application/ports/research.py`, `infrastructure/ai/configuration.py`, `infrastructure/ai/research_registry.py`: accepted S4-A contracts/configuration remain unchanged; no runtime or credentials.
- Real insertion/analysis cutover in `media_repository.py`, `upload_publication_repository.py`, acquisition services and analysis workers: S7-P integration boundary. Their S6 authorization implications are not thereby waived; G1/G2 must be resolved separately before issuance (P7 `:518-520`).
- `src/framenest/adapters/web/` and frontend resources: no S8 UI; no product rename, capture package or second account system (`AGENTS.md:18-29`, A83 `:198-204`).
- Deployment/operator scripts, host baseline documents and live database paths: no host or reset/deployment authority. Historical 0032-to-0033 runbook examples are not a mandate to deploy 0034.
- `docs/ACCEPTANCE_DUAL_AUDIENCE.md` is not blanket-authorized for rewriting historical acceptance as S6 acceptance; any needed current-contract change must be explicitly mapped first.
- Private trace paths and transcript archives never enter the public tree. Only the proposed repository access inventory is public documentation, without Meta paths.

## 6. Access inventory artifact design

Create `docs/KRONIKA_ACCESS_INVENTORY.md` and `tests/contract/test_kronika_access_inventory.py` together. Each route-method key must list composition, resource identifier, verified identity source, capability gate, object/SQL predicate source, projection selected, mutation transaction check, file-open position, positive/negative test IDs and explicit exclusion/deferred reason. Record list counts/search/facets and indirect linked IDs as surfaces, not just path parameters. This implements P5 `:401` and `.ap/INFOSEC.md:145-153`.

The test must enumerate actual route methods from both app compositions and compare them to an explicit inventory; compare workspace route classification with `tailscale_ingress.ROUTE_POLICIES`. Fail on an unclassified route, missing method, stale entry or content-bearing route with no behavioral case. Do not equate a capability label with object authorization. Health/static/configuration-only entries require a reason but need not pretend to be record readers. Existing route policy declaration and fail-closed fallback are at `adapters/api/tailscale_ingress.py:187-678`.

Minimum record-related inventory seeds (each shorthand set must expand to separate method/path entries in the artifact):

| Surface | Required policy source/evidence |
|---|---|
| GET /api/media | typed verified scope + SQL predicate before total/search/page; media_catalog_api.py:115, media_catalog_repository.py:254 |
| GET /api/media/{media_id} | common-record decision and permitted projection; media_catalog_api.py:189-220 |
| GET /api/workspace/media | own-history SQL, common owner before contribution fallback; workspace_media_api.py:107-120; media_attribution_repository.py:79-135 |
| GET /api/admin/media | verified admin inventory; content_publication_api.py:152-153; tailscale_ingress.py:235 |
| PUT /api/admin/media/{media_id}/content-publication | admin capability/audit plus transactional bound-record refusal; content_publication_api.py:205-206; content_publication_repository.py:229-305 |
| GET/PUT /api/media/{media_id}/metadata | common read decision; canonical write capability remains separate; media_metadata_api.py:316-365 |
| GET/PUT /api/media/{media_id}/alias | common read decision plus caller-private overlay/capability; media_alias_api.py:104-153 |
| GET /api/admin/media/{media_id}/aliases | explicit administrator/team-alias capability, never ordinary history; tailscale_ingress.py:249 |
| GET /api/media/{media_id}/ai-suggestions | approved-only versus owner/admin current projection must be explicit; media_analysis_lifecycle_api.py:210-261 |
| GET /api/media/{media_id}/automatic-analysis | policy before current/approved run selection; media_analysis_lifecycle_api.py:299-314 |
| GET /api/media/{media_id}/movie-identification | same record/read policy and projection distinction; media_analysis_lifecycle_api.py:420-435 |
| POST /api/media/{media_id}/locations/{location_id}/durable-analysis | admin action + object/location binding; media_analysis_lifecycle_api.py:350-373; tailscale_ingress.py:465 |
| POST /api/media/{media_id}/locations/{location_id}/movie-identification | admin action + record/location binding before provider side effects; media_analysis_lifecycle_api.py:458-513 |
| POST /api/media/{media_id}/locations/{location_id}/ai-suggestion-preview | admin/confirmation + record gate before preparer/provider; media_suggestion_api.py:317-341 |
| POST /api/workspace/media/{media_id}/analysis-proposals | verified proposal capability plus bound object authorization inside insert transaction; analysis_proposal_repository.py:48-61; tailscale_ingress.py:221 |
| GET /api/admin/analysis-proposals | verified administrator; tailscale_ingress.py:241; analysis_proposal_api.py:178 |
| GET /api/x/companion/media | verified member plus SQL record precedence before picker count/page; companion_picker.py:78-105; media_catalog_repository.py:357-407 |
| GET /api/companion/review-inbox and GET /api/companion/review-inbox/{media_id} | verified admin; companion_review_api.py:139-166, :232-265, :409-415 |
| GET /api/companion/own-history | verified member; own bound records before count/keyset; companion_review_api.py:185-216; companion_review_repository.py:143-183 |
| POST /api/companion/review-inbox/{media_id}/opened | own/admin authorization, no cross-owner ID confirmation; companion_review_api.py:285-319 |
| POST /api/companion/review-inbox/{media_id}/apply | admin publish+canonical capabilities, audit, metadata review only; companion_review_api.py:344-399, :431-445 |
| GET /api/media/{media_id}/locations/{location_id}/content and /download | deny before resolution/open/stream; Range and conditional requests included; media_content_api.py:70-151 |
| GET /api/media/{media_id}/locations/{location_id}/gallery-preview | deny before cache/read/generation and ETag handling; gallery_preview_api.py:64-90 |
| GET /api/media/{media_id}/cover-thumbnail | same decision before thumbnail access; cover_api.py:364-384 |
| GET /api/media/{media_id}/locations/{location_id}/cover-timeline and /cover-frame; PUT .../cover; GET /api/admin/media/{media_id}/cover | preserve admin canonical capability and object/location binding; cover_api.py:119-242, :318-319; tailscale_ingress.py:332-372 |
| POST /api/uploads; GET /api/uploads/capability; GET/PATCH/DELETE /api/uploads/{upload_id}; POST .../complete and .../duplicate-resolution | Enumerate actual methods only; there is no GET collection route. Session identity, duplicate and linked-media mapping remains G1; upload_api.py:139-357, :401-440, :661-704 |
| GET/POST /api/youtube/requests; GET /api/youtube/requests/{request_id}; POST .../retry | requester/admin scope plus no forbidden bound media pointer leakage; youtube_request_api.py:118-249; deeper mapping G1 |
| GET/POST /api/x/requests; GET /api/x/requests/{claim_id}; POST .../retry | requester/admin scope and linked-record precedence; x_request_api.py:149-275; deeper mapping G1 |
| /api/admin/youtube/acquisitions and /api/admin/x/acquisitions; local operator YouTube paths | each actual method classified separately; admin/local transport is not a general common-record identity bypass; tailscale_ingress.py:485-563; G1 |
| Admin media removal/receipt/cleanup routes | explicit admin + referenced-record lifecycle; RESTRICT must not become partial destructive work; tailscale_ingress.py:265-299; deletion semantics require G2 mapping |
| GET /api/canonical-tags | distinguish global vocabulary from content-derived facets; public tags must exclude bound records even with stray legacy publication; media_metadata_repository.py:124-145 |
| Public composition /api/media, details, metadata, tags, content, preview and cover routes | explicit legacy-only predicate plus NOT EXISTS bound common record before any output/open; public_published_api.py:217-349; public_published_application.py:118-152 |
| Future record, question-history, Timeline approval and render APIs | not installed in S6; absence is checked, S7-P inventory extension required, P7 :520 |

The upload row intentionally records the collection-method discovery trap rather than manufacturing a GET route. The final artifact must contain only exact actual method/path keys; this planning table is a seed, not already-completed all-route evidence. Full actual coverage remains a blocker because G1/G2 are open.

## 7. Verified direct-seam affected-test inventory

The following files were read in full where the seam appears. This is the verified direct-helper ripple, not a claim that it covers all consequences of new SQL scopes, upload decisions or projection integration. Existing behavior tests must remain meaningful; identity/policy setup changes should not replace Range, ETag, error, provider-call-count or metadata assertions.

| Exact test path and baseline locator | Required update |
|---|---|
| tests/contract/test_content_audience_policy.py:28-95, :97-249 | Ordinary fixture currently lacks identity; inject a synthetic ordinary identity for legitimate legacy reads. Add None-policy, None-identity, malformed identity, real owner/Bob/admin, bound-record precedence and stray-publication cases. Preserve private==unknown direct response checks. Service query assertion must include scope. |
| tests/unit/application/test_content_audience_requester_private.py:18-87 | Fake publication/requester repositories must include an explicit empty record lookup for unbound legacy cases. Test bound-record result takes precedence and denial never falls back. None identity must deny even published legacy content through this workspace policy. |
| tests/contract/test_x_route_policy.py:199-215 | Its two direct ContentAudiencePolicy constructions need the explicit record lookup. Preserve verified X requester behavior and capability policies; add denied bound owner mismatch. |
| tests/contract/test_gallery_preview_api.py:46-100 | Helper currently injects no policy/identity. Add fixture-scoped allow decision and verified identity for successful cache/ETag/error tests; add missing-policy/identity negatives that assert preview service untouched. |
| tests/contract/test_media_content_api.py:59-295 | Same explicit helper setup for known media IDs; preserve download, partial Range, invalid Range, stream-close and sanitized resolver failures. Denial must precede resolver/file calls, including conditional and Range requests. |
| tests/contract/test_media_alias_api.py:77-163 | Identity injection already exists; add scoped policy to dependencies. Keep caller overlay and client-owner-field rejection. Existing missing-object test is not proof of policy denial; add real denial case. |
| tests/contract/test_media_ai_suggestions_api.py:95-185 | Explicit scoped policy for identity-bearing positive/error paths. Retain no-identity 401 and capability tests; new household-approved projection behavior belongs to G2/new security tests, not an always-allow fixture. |
| tests/contract/test_media_catalog_api.py:130-160, :217, :277, :300-382 | Fake list execute signature/query assertions gain scope. Direct detail helper gains scoped policy. Replace anonymous canonical-data success in overlay test with denied/no-data result; keep Alice/Bob caller-private overlays. Repository helper query at :277 must use explicit admin test scope. |
| tests/contract/test_media_metadata_api.py:153-191, :212-413 | Add explicit identity and policy for metadata GET/PUT fixture; preserve field/tag/clear/immutability/error assertions. Vocabulary-only tag tests do not gain blanket record authorization from this helper. |
| tests/contract/test_cover_api.py:133-184, :337-389 | Replace implicit None permission for positive thumbnail cases with scoped explicit policy and identity; preserve false-policy denial, admin capability and audit cases. The constant boolean stub must not stand in for real-policy authorization evidence. |
| tests/contract/test_media_analysis_lifecycle_api.py:38-69, :256-278, :332-354, :446-471, :565-588 | All five app constructions inject lifecycle dependencies without policy; supply scoped policy plus synthetic identity at each. Keep status, manual/rerun, unavailable-provider and zero-side-effect assertions. Do not turn provider capability checks into live calls. |
| tests/contract/test_media_suggestion_api.py:229-277, :294, :502-714 | Shared helper gains identity/policy for imported-media preview requests. Library preview/capability cases are not record-seam bypasses and remain separate. Retain confirmation, error, provider/preparer-call and no-partial-result assertions through end of file. |
| tests/contract/test_companion_review_api.py:101-120, :1030-1186 | Normal helper already exercises verified synthetic ingress and real composition; keep it. The injected imported-preview dependencies at :1092-1098 specifically need a real policy backed by the fixture engine. Keep join/inbox/history and provider-call counts. Legacy review/publication cases remain unbound fixtures; add bound cases separately. |
| tests/integration/test_local_web_media_suggestion_review.py:121-192, :204-292 | Library-preview-only first test is not affected by the helper. Imported-media test needs verified synthetic admin and real record-aware policy with the injected suggestion dependency. Preserve the actual repository/review path. |
| tests/integration/test_local_web_media_playback.py:77, :152, :195, :228 | Four app clients presently rely on identity-free published playback. Inject verified synthetic member for content calls using the real policy. Preserve streaming/playback behavior; do not restore anonymous workspace access. |
| tests/unit/application/test_media_catalog.py:40-71, :74-140 | Add explicit scope at helper call and expected MediaCatalogQuery. Validation tests stay focused; add missing scope denial without repository call. Import-boundary assertion remains. |
| tests/contract/test_media_catalog_repository.py:140-153, :222-228, :273-282 | Explicit admin scope for unfiltered repository tests, verified caller scope for companion query-plan test. Retain SQL count-before-page, literal wildcard search, tag AND and tie-breaker tests; add SQL/domain parity in new record repository tests. |
| tests/contract/test_analysis_proposal.py:64-115, :118-172, :179-248, :378-447, :485-499 | Read in full as a newly identified object-authorization path. Fixtures labelled Alice/Bob currently have no ownership binding; Bob can propose MEDIA_A in the rate-isolation test. Bind positive examples explicitly. Rate-isolation must use separately owned/authorized targets and keep its rate purpose; add cross-owner denied/unknown-equivalence and zero-insert tests. Update injected rate-limited dependencies with verified scope, preserving audit/rate/provider-free assertions. |

These exact paths form candidate set T and are the only existing behavior-test modifications established by the full direct-seam reading in this report. Additional affected tests in G1/G2 are NOT asserted to be fully read or exhaustively mapped.

Other app constructions are not automatically broken merely because they call create_app: real composition injects the policy when the engine is composed (`application.py:444-485`). Conversely, tests using real composition but no identity can break even without an explicit dependency object, as playback above demonstrates. Therefore searching only for `audience_policy=` would be an incomplete inventory.

No production missing-policy/identity bypass is a permitted seam. The only permitted isolation is an explicitly injected, fixture-scoped policy with synthetic identity; missing-context tests deliberately omit it and expect denial. Public composition is a separate explicit legacy-public query mode, never a None-workspace fallback.

## 8. Migration-head test and documentation ripple

Set H consists of the following exact paths. The listed assertions were located/read as current-head expectations; this is a mechanical migration-head update, not permission to rewrite historical migration targets or unrelated tests. Keep explicit 0032->0033 historical tests and their expected 0033 results unchanged. `migrations.py:137` discovers head, so advancing the new resource changes these expectations.

| Exact test path | Baseline current-head locators to update to 0034 |
|---|---|
| tests/integration/test_persistence_migrations.py | :59, :76-77, :95, :108; file read in full |
| tests/integration/test_process_sigterm_lifecycle.py | :249 |
| tests/integration/persistence/test_content_publication_migration.py | :234 |
| tests/integration/persistence/test_media_user_alias_overlay_migration.py | :65 |
| tests/integration/persistence/test_populated_0015_upgrade_to_0017.py | :220 |
| tests/integration/persistence/test_device_registry_migration.py | :18 CURRENT_HEAD only; preserve EXPECTED_HEAD 0002 |
| tests/integration/persistence/test_upload_session_migration.py | :17, :1526 |
| tests/integration/persistence/test_media_catalog_migration.py | :17 |
| tests/integration/persistence/test_x_requester_acquisition_migration.py | :94 |
| tests/integration/persistence/test_companion_review_migration.py | :121-130 current-head test name/assertion only |
| tests/integration/persistence/test_analysis_proposal_migration.py | :96-105 current-head test only; explicit 0033 tests :108-216 retained; file read in full |
| tests/integration/persistence/test_x_requested_category_migration.py | :142 |
| tests/integration/persistence/test_media_cover_migration.py | :306 |
| tests/integration/persistence/test_upload_publication_migration.py | :241 |
| tests/integration/persistence/test_library_registry_migration.py | :18 |
| tests/integration/persistence/test_media_metadata_migration.py | :16 |
| tests/unit/infrastructure/backup/test_catalog_backup.py | :41, :57, :331, :425, :430, :536 |
| tests/unit/infrastructure/runtime/test_production_runtime.py | :261; inspect the independent canned response at :57 before deciding whether it represents head or arbitrary ready revision |
| tests/contract/test_persistence_cli.py | :123, :143-144 |
| tests/contract/test_team_alias_api.py | :429-440 schema-head sentences/test name, coordinated with P documentation |
| tests/contract/test_adr_0073.py | :94-99 current-head sentences/test name |

Do not bulk-replace `0033`. Examples deliberately retained include the historical migration filename in `tests/contract/test_analysis_proposal.py:325`, explicit migration-to-0033 and downgrade tests in `test_analysis_proposal_migration.py:108-216`, and the self-contained read-only URI fixture in `tests/unit/infrastructure/persistence/test_engine_readonly_uri.py:21,49`. ADR numbers and synthetic content IDs are not schema-head assertions. Current reader pin updates must preserve the historical audit evidence distinction described for `docs/INFOSEC.md` in P.

## 9. Material open mappings and why status is PARTIAL

### G1. Upload/acquisition authorization and complete indirect test fallout

Verified gap: the existing upload API permits missing identity in both `may_access_upload_session` and enforcement, and creates ownerless explicit-mode sessions (`src/framenest/adapters/api/upload_api.py:408-440`). Its cataloged response obtains a media pointer separately (`:661-704`). Thus the central media helper does not cover the entire accepted upload/acquisition boundary. Ordinary duplicate mode currently uses SILENT_KEEP_SEPARATE (`:414-416`), but that alone is not proof that all IDs/status/detail/retry paths obey common-record ownership.

The final implementation mapping must specify exactly where to close identity-free access, how explicitly configured operator ownership is represented without inventing an admin identity, and how linked media/duplicate results are filtered without corrupting ingestion/recovery. It must then read and enumerate affected fixtures, including the local upload cockpit and requester-private details. This report does not assert that work is complete.

Exact discovered paths requiring that mapping, not added authorization:

```text
src/framenest/adapters/api/upload_api.py
src/framenest/adapters/api/youtube_request_api.py
src/framenest/adapters/api/x_request_api.py
src/framenest/application/youtube_acquisition.py
src/framenest/application/x_acquisition.py
src/framenest/application/upload_catalog.py
src/framenest/infrastructure/persistence/upload_publication_repository.py
tests/contract/test_upload_api.py
tests/contract/test_ordinary_upload_ownership_boundary.py
tests/contract/test_youtube_request_api.py
tests/contract/test_requester_private_youtube_details.py
tests/contract/test_x_request_api.py
tests/integration/test_local_web_upload_cockpit.py
tests/integration/test_atomic_upload_publication.py
```

This is a minimum discovered set, not a claim that no other caller/test changes. A grant that says only "fix the central seam and update failing tests" would leave the authority boundary undefined. Resolution evidence is a closed method/service/repository/test mapping with all indirect app fixtures read, and exact identity/duplicate semantics, before issuance.

### G2. Approved projection across live readers/writers and removal

Verified gap: several readers expose current metadata or analysis after only a boolean audience gate; `media_analysis_lifecycle_api.py:227-261` calls the suggestion service after the check. Companion apply edits live metadata (`companion_review_repository.py:482-519`); the catalog queries live metadata (`media_catalog_repository.py:254-355`). Two run pointers in a new table do not by themselves preserve an older approved projection. Existing publication and contribution queries also need bound-record precedence, as mapped above.

The design decision is to serve the approved snapshot to a non-owner household member, while owner/admin working views may see current state. However, the exact adapter/service serialization and mutation-version mapping for every existing path has not been completed here. The following exact existing modules are implicated but are NOT an approved blanket allowlist:

```text
src/framenest/adapters/api/media_metadata_api.py
src/framenest/adapters/api/media_analysis_lifecycle_api.py
src/framenest/adapters/api/media_alias_api.py
src/framenest/adapters/api/cover_api.py
src/framenest/adapters/api/media_content_api.py
src/framenest/adapters/api/gallery_preview_api.py
src/framenest/adapters/api/media_suggestion_api.py
src/framenest/infrastructure/persistence/media_metadata_repository.py
src/framenest/infrastructure/persistence/companion_review_repository.py
```

Resolution must fix snapshot field/schema selection, approved-vs-current filtering before search/facets, candidate digest/version invalidation across metadata edits, analysis-success updates and safe referenced-media removal behavior. It must enumerate the additional tests, including real public composition, workspace/companion and requester readers. `tests/contract/test_public_published_uds.py`, `tests/contract/test_workspace_media.py`, and `tests/unit/test_companion_picker.py` were discovered; they are not falsely labelled fully mapped in this report. The direct-seam fixture table is complete for its stated seam search, not for G2.

Do not resolve this by denying all family reads indefinitely, exposing the latest private rerun, copying legacy publication state into family, moving all authorization to S7-P, or declaring a documentation inventory to be all-route evidence. Those would change accepted P5/A83 behavior.

### G3. Private live database/WAL/SHM boundary

P5 `:387` requires private state (0700/0600). The inspected engine configures FK/timeout and SQL log redaction (`engine.py:23-48`); the migration entry point creates parent directories without an explicit mode (`migrations.py:76-94`). Backup helpers do contain private directory/file handling (`catalog_backup.py:430-467`). These observations do NOT prove that the whole application's live state is insecure, nor that backup permissions establish live DB/WAL/SHM permissions.

The missing evidence is an exact normal database-creation/open/WAL lifecycle and configuration path mapping, including existing directory handling and platform policy, with corresponding synthetic tests. No scan of private live state is required or permitted. The candidate allowlist deliberately does not authorize speculative chmod changes to engine.py, migrations.py or arbitrary parent directories. An issuable S6 grant must either cite the existing enforced live-state boundary and its tests or add exact code/test paths and safe behavior to enforce it. No real prompts or answers may be used to test this.

These three gaps are material because S6's accepted gate is all-route authorization plus durable private records, not only schema compilation (P7 `:518`). No second planning cycle is self-authorized. The Orchestrator must resolve the omissions prospectively and accept a closed mapping before issuing the one fresh implementation grant.

## 10. Proposed E3/R3 tests and acceptance route

All items below are future evidence, not executed results. Use synthetic owners Alice/Bob/admin, synthetic content and disposable databases under a test-owned temporary root. No real provider, browser, host, external URL fetch, credentials or existing catalog. Record temporary paths, modes, ownership and cleanup in the implementation/audit containment ledger (`.ap/INFOSEC.md:145-153`, `:283-330`).

| Evidence group | Required positive/negative/rollback cases |
|---|---|
| Migration | Empty head upgrade; populated synthetic 0033 preserves old rows and creates zero common records; correct FKs/default/checks/indexes; duplicate media/document/operation rejected; wrong kind/reference shape rejected; owner/timestamp/version checks; foreign_key_check; empty downgrade/re-upgrade; populated downgrade refuses without changes |
| Domain and completion | UUID vs operation-token distinction; exact S4-A byte/citation bounds; full answer retained; refusal/incomplete/no-search evidence cannot become completed document; invalid persisted normalized JSON fails closed; no raw provider payload storage |
| Transactions | Synthetic document+record rollback on injected failure; duplicate final operation conflicts/idempotent return without second record; media insertion+owner binding rollback through shared connection helper; no partial approval/withdrawal on conflict or storage exception |
| Access matrix | Owner incomplete/private, Bob private denial, admin read-all, member approved-family read, anonymous/unmapped/public denial; client owner/approver overrides rejected; actual server role/capability source exercised |
| Lists and indirect exposure | Forbidden IDs/titles/counts/search hits/facets/cursors/duplicate identities absent; authorization precedes total/limit; common ownership wins over conflicting legacy contribution/publication; SQL predicate agrees with pure domain matrix |
| Direct content | All route/method entries; identical denied/unknown responses where applicable; no downstream resolver/provider/open on deny; original/Range/download/ETag/preview/cover paths included; supplied location must belong to authorized media |
| Approval | Only admin; own-admin also explicit; completed/validated Q/A; analyzed matching media + persisted readiness; exact version/digest conflict; racing approve/withdraw yields one winner; no silent metadata apply; first timeline time once; withdrawal preserves history; repeat behavior as section 4.3 |
| Reanalysis | New pending/failed/successful run does not replace old approved family projection until explicit reapproval; owner/admin current view distinct; reapproval changes same card without moving timestamp; no private new terms leaking through search/tags |
| Public exclusion | Seed bound private AND bound family records with erroneous legacy publication rows; no list totals/tags/details/bytes in real public composition, direct repository public queries or direct URL reads; preserve only authorized legacy fixture behavior; public mode stays disabled by configuration |
| State privacy | Synthetic new/existing safe and unsafe roots; DB/WAL/SHM modes and cleanup; no content in errors/logs/audit; backup/restore contains records and preserves private-state constraints; final exact scope pending G3 |
| Regression | Direct-seam files in T, head files H, existing Gallery/player and metadata/companion behavior; full suite only through declared route after focused checks, with purpose of discovering identity-free app fixtures and schema-head ripple |

Proposed execution route, only for a later explicit implementation grant, from the repository root:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310 --operation test-focus -- tests/unit/domain/test_records.py tests/unit/domain/test_record_access.py tests/unit/application/test_records.py tests/integration/persistence/test_kronika_records_migration.py tests/integration/persistence/test_kronika_record_repository.py tests/contract/test_kronika_record_authorization.py tests/contract/test_kronika_access_inventory.py -q -p no:cacheprovider
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310 --operation test-focus -- tests/unit tests/contract tests/integration -q -p no:cacheprovider
```

The full Python suite is proposed once because the named risk is every identity-free app construction plus packaged migration-head ripple. The final grant must first close G1-G3 and explicitly include its required focused tests. Do not run the above commands during planning. Do not replace AP with ambient python/pytest/Poetry or repair the environment if preflight fails (`AGENTS.md:51-58`, `ap.project.conf:1-32`, `.ap/AP_WORKER.md:233-249`). A failure is classified and reproduced narrowly before any justified broad rerun. There is no test result in this report.

After a locally committed candidate and complete inventory/transaction receipts, the Orchestrator issues a SEPARATE fresh independent E3/R3 authorization review against the exact candidate SHA. The reviewer must not inherit implementation reasoning as independent evidence and must not implement fixes. Review actual direct APIs, horizontal/vertical access, identity forgery, admin actions, CSRF/audit boundaries, all inventory rows, SQL/list leaks, approved projection, public exclusion and migration/recovery. Synthetic probes only. Corrections require a separate correction task and fresh independent re-audit; no self-certification (`.ap/AP.md:1472-1492`, `.ap/INFOSEC.md:83,95`, `:145-153`, `:369-377`). No acceptance, publication, deployment, live provider use or logical-whole closure follows automatically.

## 11. Exactly one recommended next implementation grant: withheld draft

Recommendation: one fresh S6 implementation grant, after the Orchestrator closes G1-G3 and accepts the plan. No alternative grant or same-session implementation is recommended. The following is the project grant shape with concrete baseline, scope and stop semantics. It is NOT READY FOR ISSUANCE because its exact complete allowlist and indirect-test matrix are missing. Do not deliver it to an implementer as executable authority and do not replace the missing mappings with a wildcard.

| Field | Proposed value |
|---|---|
| Role / logical whole | WORKER / kronika-one-product |
| Session / exchange | Next genuinely fresh session, proposed 32 / 01 if still unallocated at issuance |
| Session target/profile | fresh-worker-session / Fresh Implementation Worker |
| Native planning mode | not-used |
| Phase/task | implementation / KRONIKA-ONE-PRODUCT-S6-IMPLEMENTATION |
| Delivery | manual Cooperator delivery |
| Independence | no; implementation evidence explicitly non-independent |
| Baseline/branch | exact 40e51cb2d061ead96850c9c94aa59de54d5e1310; feat/kronika-one-product; clean; local refs and .ap pin reverified without network |
| AP pin | 7478ddb07d2c3911f79e1aa1441f0115a31c45d8, read-only |
| Outcome | Migration 0034, common records, complete-document storage foundations, centralized fail-closed record access, admin approval/withdrawal/history foundations, executable all-route inventory; all gates in section 10 |
| Allowlist | Exact sets N + P + T + H, with conflicts/deduplication resolved, AND an exact prospectively approved G1-G3 completion. This unresolved field prevents issuance; no open-ended editing is authorized by this draft. |
| Positive authority | On issuance only: edit allowlisted files, use synthetic disposable fixtures, AP preflight/tests, inspect diff/status, explicitly stage exact accepted files and create one local commit |
| Negative authority | No real data or live DB migration; no private/**; no host/network/provider/browser/credentials; no AP/dependency/toolchain changes; no S4-B/S7-P/S8/capture implementation; no push/merge/branch publication/deployment/acceptance/closure; no subagents |
| Declared route | Exact AP commands in section 10 plus the final closed focused-test list; no ambient execution or environment repair |
| Staging/commit | After required checks pass and diff matches closed allowlist, stage paths explicitly, inspect cached diff/check/stat, then one local commit with subject `feat(kronika): add private records and administrator approval`; no git add -A, force actions or remote writes |
| Stops | Baseline/pin/branch/dirty-state drift, 0034 collision, unresolved G mapping, out-of-list required edit, permission/route failure, failing unexplained gate, private data/network/host requirement, unverifiable identity/projection/transaction invariant; report exact evidence, do not broaden scope |
| Report result | PASS only for the complete bounded implemented/tested candidate, Phase-qualified result Implementation PASS; otherwise truthful PARTIAL/BLOCKED as applicable; Logical-whole closure not-closed; Report justification new-evidence |
| Report core | Exact start/end SHA, changed paths, commands and exit statuses, focused/full results, inventory cases/exclusions, transaction/recovery receipts, containment ledger, residual risks, commit/no-push evidence, next independent audit, mandatory critique and authority-expiry fields |
| Trace | Same private historical-evidence-only project directory; proposed prompt `32_implementation_00.md`, report `32_report_00.md`, only if that session slot is confirmed unused at issuance |
| Persistence/archival | Orchestrator persists prompt; assigned Worker persists absent report at exact issued destination, reads back fully and returns SHA-256; Cooperator owns archival/Git publication |
| Expiry | Terminal implementation report or cancellation; no implicit continuation or acceptance authority |

This draft deliberately preserves the need for an explicit authoritative ORCHESTRATOR prompt with Native planning mode not-used. Approval of a plan is not itself that execution prompt (`.ap/AP.md:544-606`; current task planning contract). The next action is Orchestrator disposition of the named omissions, not implementing the mapped subset and calling S6 complete.

## 12. Deviations, missing evidence and authority expiry

No implementation, test execution, acceptance, publication or host action occurred. No code-existence claim is made for any proposed file. The code checkout stayed clean and at the starting SHA. The terminal report is the only authorized write.

Material shortfall: the requested complete all-route allowlist and affected-test inventory were not fully established. Section 7 is a verified direct-seam inventory; it is not relabelled as the complete S6 inventory. Sections 9 and 11 prevent accidental issuance on partial evidence. Existing historical plan decisions, S4-A contracts/v3 and parked work are preserved.

Several broad read outputs were truncated; relied-on narrow passages and the direct-seam files were read in smaller ranges. Some guessed path reads failed before discovery of actual paths. These were read-only execution issues; no tests, package operations or environment repairs followed. The initial shell cwd was the predecessor project; authoritative inspection and all implementation planning were redirected to the named FrameNest checkout. No authority from the predecessor project was used to authorize this task.

The report destination's parent chain was checked with namei and contained directories, not symlinks. The destination was absent before exclusive creation. The file is created with private mode under umask 077. Final full readback, first-line/coordinate checks, path/mode check and SHA-256 are performed before the separate Slovak terminal notice. The digest is reported outside this file to avoid a self-referential hash.

Orchestration critique:
MEASURED: S6's central-seam description understates distinct integration sites if used as the execution allowlist: media list SQL uses publication/companion conditions (media_catalog_repository.py:254-407), proposals currently check existence only (analysis_proposal_repository.py:48-61), and upload identity absence permits access (upload_api.py:408-440). Effect: a helper-only patch cannot establish accepted all-route authorization. Smallest correction: close G1-G3 and issue one exact bounded S6 grant with the method/service/repository/test mapping; retain fresh E3/R3 acceptance.
LEAD: The full indirect app-fixture ripple and approved-projection serialization/version coupling may require additional paths beyond N/P/T/H. Cheapest useful check: finish the specific G1/G2 caller-and-test reading and record exact decisions before issuance; then use the declared focused/full tests under implementation authority. No new vulnerability severity or live exposure is claimed from static planning evidence alone.
Resolved Execution Issues / Near-Misses: Initial repository-location mismatch corrected before target planning; failed guessed read paths and truncated outputs narrowed where relied upon; client mode transition did not expand task scope; no forbidden execution or repository mutation used as a workaround.
Pre-existing Failure Classification: none observed by execution because tests were prohibited. Existing permissive seams are verified baseline behavior and S6 integration findings, not invented test failures or independently certified security findings. Private live-state enforcement remains unproven, not declared broken.

Planning authority expires on submission of this terminal report and completion notice. No second planning cycle, implementation, acceptance, publication or closure authority is retained. Trace remains private historical evidence; its persistence grants no execution authority.
