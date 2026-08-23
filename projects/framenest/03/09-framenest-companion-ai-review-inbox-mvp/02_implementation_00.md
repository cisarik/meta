# Authoritative Prompt for Fresh Worker 02

## FrameNest Companion AI Review Inbox — ADRs, five-tag prompt, admin X enqueue

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 01 completed repository-grounded implementation planning. That planning
authority is expired. On 2026-08-23 the COOPERATOR accepted the frozen
architecture in `01_report_00.md` (Slovak “Schvaľujem”), including G2, S1,
badge-without-notifications, administrator-only X automatic analysis, generic
five-tag cap, movie exclusion from the companion, tag **replace** (not union),
and `alarms` in a **later** slice. The ORCHESTRATOR binding reconciliations in
Section 8 of this prompt outrank the Planner where they conflict.

Your task is **slice W02 only**: accept the six successor ADRs, bump the
generic suggestion contract to v4 with at most five tags, and refactor X
automatic-analysis policy so an administrator-owned X catalog event may enqueue
generic analysis when the server flag is on. Do not enter Native Plan Mode. Do
not produce another architecture plan. Do not implement inbox routes, Alembic
0031, review overlay, badge, alarms, G2 apply, or NUC.

Validate, create at most two coherent local commits, write the exact terminal
report, and stop.

If Native Plan Mode is on, stop `BLOCKED`. Do not use Max. Extra High is
requested; if the client does not expose a measurable Extra High SKU, continue
only while Plan Mode stays off and Max is unused, and record that in the
handshake.

```text
Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-companion-ai-review-inbox-mvp
Prior logical whole identities:
  framenest-x-meme-browser-companion-mvp
  framenest-x-companion-save-alias-mvp
  framenest-x-companion-save-category-mvp
  framenest-x-save-overlay-edit-subset-mvp
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: FN-COMPANION-AI-REVIEW-INBOX-IMPL-02
Task type: bounded implementation candidate
Native planning mode: not-used
Reasoning recommendation: extra-high
Evidence posture: non-independent
Independence required: no
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
Prior planning report: Worker 01 / exchange 01 architecture accepted by Cooperator 2026-08-23; planning authority expired
Continuity anchor: none — do not resume the Planner session
Internal delegation posture: not-used
Accountable Worker: one WORKER
Material phase gate: yes
Changed material axis: mutation-authority-or-side-effect-class
Routing reopened for: mutation-authority-or-side-effect-class
Unchanged axes reopened: none
Ordinary-only trigger: no
Automatic model selection: off
Enhanced/maximum mode: not requested
```

```text
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: c581c0e6fa57391c1da40dd45e4bd224955a7f7d
Changed-path allowlist: Section 11
Implementation boundaries: Sections 8, 9, 10, 12, and 14
Independence required: no
```

```text
Evidence tier: E3
Evidence tier basis: whole introduces later migration, companion mutations, canonical apply, and G2; this Worker lands only ADRs plus policy/prompt/enqueue. Do not self-certify the whole.
Authorized implementation stages: causal slices 1–3 in Section 10
Combined implementation envelope: allowed for those three slices only
Implementation stage gates: Section 10; a failed gate stops the sequence
Independent acceptance: not-required (this session). INFOSEC R3 is a later grant after W06.
Rollback or recovery checkpoint: local Git commits on feat/x-meme-browser-companion; no push; no NUC
Activated stricter profile: INFOSEC.md R1 inline only
Terminal implementation report point: after slices 1–3 are committed and validated, before inbox/0031/overlay/acceptance/publication/NUC
```

Reasoning recommendation: Extra High. The candidate changes automatic-analysis
authorization, the live NIM prompt/validator, and six accepted ADRs. Do not
silently downgrade. Do not use Max.

```text
COOPERATOR: Michal
ORCHESTRATOR: ORCHESTRATOR_CHAT
WORKER: this fresh implementation session
```

Internal delegation, sub-agents, parallel Workers, Explore tasks, and hidden
secondary workstreams are not authorized.

Repository documentation, code comments, test names, commit subjects, and the
terminal Worker report must use professional English. Czech is forbidden.
The terminal report must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Do not expose private chain-of-thought. Report decisions, evidence, commands,
results, resolved issues, and residual risks concisely.

Implementation PASS is not acceptance, publication, deployment, production
acceptance, or ORCHESTRATOR closure. This slice does not close the logical
whole.

Protocol-variant selection:

```text
Canonical repository identity: https://github.com/cisarik/ap.git
Immutable version identity: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Declared variant: stable
Governing variants in effect: one
Declaration location: project governing rules
Rules from non-governing variants: none
Migration required: no
```

---

## 1. External trace and Meta write boundary

```text
External trace disposition: configured
Trace discovery: cisarik/meta repository path projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp
Trace project key: framenest
Trace logical-whole projection identity: 03/09-framenest-companion-ai-review-inbox-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR after the outcome exists
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_implementation_00.md
Destination path: projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/02_implementation_00.md
Archival: wait-for-report
```

You may **read** the accepted plan (historical evidence, subordinate to this
prompt):

```text
/home/agile/meta/projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/00_handout.md
/home/agile/meta/projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/01_planning_00.md
/home/agile/meta/projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/01_report_00.md
```

Frozen hashes at issuance (re-check; stop `BLOCKED` if either drifted):

```text
01_planning_00.md SHA-256 675d31b71df7eadbd47ffcec36a86a68d54d3fb59ecb9122a9be37df4a33f320
01_report_00.md   SHA-256 51e124c02009a6822ebb36afc8893187074c680cd139462d79e72cb61bab75ce
```

You may **write** only this exact report file:

```text
/home/agile/meta/projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/02_report_00.md
```

You may not alter any other Meta path, stage Meta, commit Meta, or push Meta.
Do not execute parent-whole, `03/07`, or `03/08` prompts. Do not create
`00_handout.md`. If the Worker environment cannot safely write the report file,
return the complete report in chat so the ORCHESTRATOR can save it verbatim.
Do not invent another filename.

---

## 2. Communication and human-governance routing

```text
Operator presentation: not used inside this Worker prompt
Orchestrator: ORCHESTRATOR_CHAT
Worker prompt language: professional English
Worker report language: professional English
Direct-user Slovak presentation: Orchestrator-owned; do not emit the Cooperator capsule
Report header: ### Report for ORCHESTRATOR_CHAT
Cooperator visibility: implementation grant already issued; deterministic steps inside this envelope need no micro-approval
Human decision points remaining outside this grant: inbox/0031/overlay (W03–W06), living docs (W07), independent R3, NUC flag/origins/0030/0031/x_acquisition_root, live NIM, Brave Reload
Deterministic steps inside bounded authority: slices 1–3, tests, local commits
Brainstorming classification: not authority
Internal delegation posture: not-used
```

---

## 3. Capability handshake

This is a fresh session. Perform a compact capability handshake before
mutation. Report each material value as `requested`, `directly observed`,
`inferred`, or `unknown/not observably exposed`.

Record at least:

- product/client and requested versus observed model;
- requested Extra High versus observed state; Max not requested;
- Native planning mode requested `not-used` versus observed state;
- filesystem containment and writable scope;
- network and tools required by this prompt;
- source inspection/editing, tests, local commit, and public-ref `ls-remote`;
- that push, NUC, sudo, provider, signed-in browser, AP mutation, and
  independent acceptance remain unauthorized even if technically possible.

Do not probe credentials, print `SSH_AUTH_SOCK`, reconstruct `gpgconf`, or
treat capability as authority. If Native Plan Mode is on, stop `BLOCKED`. Do
not silently continue as Medium.

```text
Repeated-gate or reasoning-loop stop: configured
Broad gate: once per materially changed candidate
Narrow before re-broad: required
Unchanged hypothesis, candidate, and failing gate: not-progress
Escalate only on: named missing evidence the higher profile must solve
Cost cannot falsify evidence: yes
```

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: owners in Section 13
Affected tests: Section 13
New causal regression: Section 9 invariants
Broad or full suite: not-used in this Worker (later after W03/W04 schema/mutation)
Runtime or testbed: not-used
Independent acceptance: not-required
```

Browser, provider, owner-command, authenticated-readback, publication,
deployment, and production-acceptance annexes are **not activated**.

---

## 4. Repository gate and exact baseline

Canonical checkout (do not invent another worktree):

```text
Expected canonical root: /home/agile/Projects/framenest
Repository checkout topology: standalone checkout
Working-copy topology: canonical checkout
Topology rationale: unpublished feature branch; public main lacks this whole
Applicable branch: feat/x-meme-browser-companion
Expected HEAD: c581c0e6fa57391c1da40dd45e4bd224955a7f7d
Expected parent: af348847608fbb1e546d6db5e116e7ee81bacd9e
Expected tree: 823c5650ac3db39a00b197fc2110c850b2bc0d35
Expected subject: fix: submit X save on host Enter without title autofocus
Working tree: expected clean
Upstream: none configured (expected)
Schema head: Alembic 0030 (do not add 0031 in this Worker)
```

Canonical AP pin (read-only; do not mutate):

```text
Submodule path: .ap
Repository: https://github.com/cisarik/ap.git
Expected gitlink and checkout: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Detached submodule checkout: acceptable
```

Issuance-time public refs verified by the ORCHESTRATOR without `git fetch`:

```text
cisarik/framenest refs/heads/main
045f33b44897a6f3949cc515792336396f1d33a1

cisarik/ap refs/heads/main
9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

Before mutation, re-verify both refs through credential-free Git transport:

```text
git ls-remote https://github.com/cisarik/framenest.git refs/heads/main
git ls-remote https://github.com/cisarik/ap.git refs/heads/main
```

Do not `git fetch`. Do not use GitHub webpages as current-ref evidence.

Public `main` is **behind** this feature branch. That is expected. Do not
fast-forward local `main`. If public `main` advanced past `045f33b`, inspect
intervening commits read-only and stop `BLOCKED` only when they materially
conflict with this whole. If local HEAD is not `c581c0e`, stop `BLOCKED`
unless the only difference is this Worker’s own later commits from this
session.

Preserve unrelated dirty state. Do not stash, reset, or clean. Stop if
unexplained FrameNest remainder overlaps this allowlist.

Canonical Python evidence route only:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline c581c0e6fa57391c1da40dd45e4bd224955a7f7d
./.ap/ap exec --root /home/agile/Projects/framenest --baseline <EXACT SHA OF THE CANDIDATE UNDER TEST> --operation test-focus -- <tests> -q -p no:cacheprovider
```

After the first commit, `--baseline` is that commit’s SHA, not a stale
issuance SHA used as if it were HEAD while HEAD has moved. Do not invoke
`.venv/bin/python`, `python`, `python3`, or `poetry run` for project evidence.

The NUC gate `scripts/operator/network/framenest_nuc_worker_gate.fish` is named
only to close route resolution. It is **not activated**.

Spot-check before mutation (do not “fix” these here):

- `automatic_analysis_allowed_for_upload` in `x_acquisition.py` returns
  `repository.find_asset_by_upload_id(upload_id) is None`.
- YouTube helper of the same name still fail-closes linked YouTube uploads.
- `_combined_analysis_allowed` in `application.py` calls the X helper first,
  then the YouTube helper.
- `identity_mapping` is built **after** catalog-coordinator wiring today
  (around the Tailscale middleware block). This Worker must move mapping
  construction **before** that wiring, as the accepted plan requires.
- `PROMPT_VERSION == "framenest-media-suggestion-v3"`;
  `TAG_MAX_COUNT = 12`; prompt text still says “Return 4 to 10”.
- `companion_mutation` remains only the two X POSTs. Do not add review routes.
- Ingest Save overlay remains Title → Tags → Description → Save; no radios;
  host Enter submits. Do not edit `save.*` or `x_adapter.js`.
- Movie identification prompt version remains
  `framenest-movie-identification-prompt-v2` with its own `MAX_TAG_COUNT = 12`.

---

## 5. Required reading

- `AGENTS.md`
- `.ap/AP.md`, `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md`
- `.ap/INFOSEC.md` §3–§5 (R1 inline; do not execute R3)
- `docs/WORKER_EXECUTION_CONTRACT.md`
- `docs/adr/0016-provider-neutral-media-suggestions-and-nvidia-nim-prototype.md` (read-only)
- `docs/adr/0020-on-demand-ai-suggestion-review.md` (read-only)
- `docs/adr/0044-durable-automatic-post-catalog-analysis.md` (read-only; do not edit)
- `docs/adr/0045-content-classification-and-movie-identification.md` (read-only)
- `docs/adr/0049-durable-content-publication-boundary.md` (read-only)
- `docs/adr/0061-x-meme-browser-companion.md` (read-only; do not edit)
- `docs/adr/0063-companion-side-panel-web-host.md` (read-only)
- `docs/adr/0065-x-save-edit-subset-and-acquisition-time-canonical-metadata-seed.md` (read-only)
- `src/framenest/application/x_acquisition.py`
- `src/framenest/application/youtube_acquisition.py` (read-only except you must
  not change its fail-closed helper)
- `src/framenest/adapters/api/application.py` (`_combined_analysis_allowed`,
  catalog coordinator, identity mapping)
- `src/framenest/domain/identity_access.py` (`ROLE_ADMIN`,
  `IdentityMappingEntry`, `build_identity_mapping`, `normalize_login`)
- `src/framenest/application/ports/x_acquisition.py`
  (`find_post_by_upload_id`, `created_by_login_key`)
- `src/framenest/application/media_suggestion.py`
- `src/framenest/infrastructure/ai/prompts.py`
- `src/framenest/infrastructure/ai/nvidia_nim.py`
- `src/framenest/application/media_analysis_lifecycle.py` (`enabled` scheduler)
- `src/framenest/application/upload_catalog_coordinator.py`
  (`analysis_allowed_for_upload`)
- `src/framenest/adapters/api/web/app.js` (fallback `prompt_version` string)
- Accepted plan `01_report_00.md` Sections 7, 9, 12, 14–17 (architecture;
  this prompt wins on W02 scope)

---

## 6. Goal

One coherent W02 candidate:

1. Six **Accepted** successor ADRs (0066–0071) plus README index rows, without
   editing prior ADR bodies.
2. Generic media suggestion `PROMPT_VERSION = "framenest-media-suggestion-v4"`,
   `TAG_MIN_COUNT = 1`, `TAG_MAX_COUNT = 5`, and prompt text that demands at
   most five **most significant** tags for a GIF, image, or video.
3. X automatic analysis allowed **only** when the linked claim’s
   `created_by_login_key` currently maps to `ROLE_ADMIN`. Flag default remains
   false. YouTube remains fail-closed. Ordinary/null/unmapped X remains
   denied. No companion UI. No 0031. No new HTTP routes.

---

## 7. Accepted decisions (do not re-litigate)

Cooperator 2026-08-23, Orchestrator-reconciled:

- Auto-NIM after X Save: **administrator requesters only**, when
  `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` is true. Flag stays default
  false. This Worker lands the code path; it does **not** enable the flag.
- G2, S1, badge, `alarms`, review overlay, 0031, companion review routes: **accepted
  architecture, later Workers**. Write ADRs 0067–0071 now; do not implement them.
- Notifications permission: **out**.
- Generic NIM tags: **1–5**, quality over quantity, most significant for
  GIF/image/video. Prompt-version bump to v4.
- Companion does **not** concern movie. Do not change movie-identification
  prompt, genres, or `MAX_TAG_COUNT = 12` there.
- Tags ✅ is **replace**, not union — later apply slice. Do not implement apply.
- NUC deploy: **out**.
- Ingest Save overlay: **frozen**.
- `companion_mutation` stays two POSTs **in code** until W04. ADR-0067 records
  the successor contract.
- Ordinary identities must not gain `analysis.run`,
  `metadata.canonical.write`, or `media.content.publish`.
- No auto-apply of NIM at catalog. Enqueue is not apply.
- No second suggestion store.
- Parent wholes remain not-closed.

---

## 8. Orchestrator binding reconciliations

These win over Planner prose if a later implementation Worker would otherwise
guess:

1. **Identity mapping before coordinator.** Today `identity_mapping` is built
   near Tailscale middleware, **after** `UploadCatalogCoordinator` is
   constructed. Build `build_identity_mapping(resolved_settings.identity_map)`
   **before** `_combined_analysis_allowed` / catalog-coordinator wiring, and
   reuse that same mapping object for Tailscale ingress when ingress is
   enabled. Do not resolve identity from HTTP request context at catalog time.
2. **X helper law.** Refactor
   `x_acquisition.automatic_analysis_allowed_for_upload`; do not delete the
   function. Effective law:
   - No linked X asset (`find_asset_by_upload_id` is `None`): return `True`
     (not an X upload; YouTube helper still runs next).
   - Linked X asset: load `find_post_by_upload_id`. If missing, mapping miss,
     `created_by_login_key` is `None`, unmapped login, or `role != ROLE_ADMIN`:
     return `False`.
   - Linked X asset whose normalized login maps to `ROLE_ADMIN`: return `True`.
   - Repository/identity errors: **fail closed** (`False`) so cataloging still
     succeeds and analysis is not enqueued. Do not raise into the catalog
     transaction.
3. **Do not expand ordinary capabilities.** Admin eligibility is current
   `identity_map` role at catalog time, not `x.request`. Demotion before
   catalog prevents enqueue. No retroactive backfill when the flag later
   turns on.
4. **Scheduler `enabled` remains the final enqueue gate.** Policy `True` with
   flag false must not create a run. Existing
   `ScheduleAutomaticMediaAnalysis.enabled` / coordinator behavior stays.
5. **YouTube helper signature and fail-closed behavior stay.** Do not “unify”
   YouTube into the admin-X path.
6. **v4 prompt instruction** must include this meaning (English, professional;
   you may tighten wording but not weaken the cap):

   > Return 1 to 5 concise English display tags that are most significant for
   storing this GIF, image, or video. Quality matters more than quantity.
   Prefer 3 to 5 only when supported by visual evidence. Prioritize important
   subjects, actions, emotions, and context; omit weak, redundant,
   speculative, or filename-derived tags. Never return more than five.

   Keep anti-injection, JSON-only, and the rest of the current prompt
   contract. Result schema version stays `framenest-media-suggestion-result-v1`
   if that identifier already exists; do not invent a parallel result schema.
7. **Historical v3 codec is W03.** This Worker changes the **live** validator
   and prompt. Do not add `companion_review_*` tables, inbox queries, or a
   stored-result codec. Leave durable historical JSON in the database readable
   as stored text. Tests that are **historical fixtures** (migration SQL,
   populated 0015→0017, analysis-run history rows) must **keep** the v3
   string. Tests that assert the **live** constant must move to v4 /
   `PROMPT_VERSION`.
8. **Active v3 pins outside the allowlist.** If the focused suite in Section 13
   fails because a file outside Section 11 still asserts live `PROMPT_VERSION`
   is v3, stop `PARTIAL` and name the path. Do not silently expand into W03
   migration tests or companion UI. Do not “fix” movie-identification tests.
9. **`app.js` fallback** currently
   `aiCapability.prompt_version || "framenest-media-suggestion-v3"`. Update
   the fallback string to v4. Do not rewrite Analyze-by-AI UX.
10. **ADRs 0066–0071 are Accepted**, decision date `2026-08-23`, because the
    Cooperator accepted the plan. They are new files. Prior ADR bodies stay
    untouched. `docs/adr/README.md` gains six index rows and may annotate
    superseded **statements** the way 0062/0064 already do (e.g. 0061 “exactly
    two companion mutations” superseded by 0067; 0049 explicit-only
    publication superseded **narrowly** by 0068; 0016 prompt contract
    successor 0069; 0044 X carve-out successor 0066; 0063 iframe-only chrome
    successor 0071; 0045 supplemented by 0070). Do not mark entire prior ADRs
    `Superseded`.
11. **Missing provider** remains existing lifecycle truth (`PROVIDER_NOT_CONFIGURED`
    / failed run). Do not add a new provider client. Do not call NVIDIA.
12. **Loopback / empty mapping.** If `identity_map` is empty, every X-linked
    upload is denied for automatic analysis. That is correct fail-closed.

---

## 9. Positive behavior and invariants

### 9.1 ADRs

Create, in the existing ADR house style (Status, Decision Date, Context,
Decision numbered, Consequences, References; Superseded statements where
needed):

| File | Title |
|---|---|
| `docs/adr/0066-administrator-owned-x-automatic-generic-analysis.md` | Administrator-Owned X Automatic Generic Analysis |
| `docs/adr/0067-administrator-companion-review-inbox-and-mutation-trust.md` | Administrator Companion Review Inbox and Mutation Trust |
| `docs/adr/0068-companion-review-save-and-readiness-triggered-publication.md` | Companion Review Save and Readiness-Triggered Publication |
| `docs/adr/0069-five-tag-generic-media-suggestion-contract.md` | Five-Tag Generic Media Suggestion Contract |
| `docs/adr/0070-companion-exclusion-of-movie-workflows.md` | Companion Exclusion of Movie Workflows |
| `docs/adr/0071-native-side-panel-review-inbox-chrome.md` | Native Side-Panel Review Inbox Chrome |

Decision bullets must match `01_report_00.md` Sections 7–12 (admin X + flag;
new review routes later; G2 after review Save only; v4 1–5 tags; movie out;
S1 + badge + `alarms` later, no `notifications`). State clearly that W02
implements 0066+0069 in code and that 0067/0068/0070/0071 are accepted
contracts for later slices.

### 9.2 Prompt / validator

- `PROMPT_VERSION = "framenest-media-suggestion-v4"`
- `TAG_MAX_COUNT = 5` (keep `TAG_MIN_COUNT = 1`)
- New provider output with 0 or 6+ tags is invalid.
- NVIDIA prompt text contains the v4 version id and the five-tag instruction.
- Movie identification files are not modified.

### 9.3 X policy

Prove with tests (fake repository + mapping; no live Tailscale):

- Flag is **not** read inside the X helper. The helper answers “may this X
  upload be analyzed if the scheduler is enabled?”
- Admin X + mapping hit → `True`.
- Ordinary mapped user, unmapped login, `None` owner, missing post row →
  `False`.
- No X asset → `True`.
- YouTube helper still `False` when a YouTube claim is linked.
- `_combined_analysis_allowed` uses the new X signature with the pre-built
  mapping.

Do not add an Analyze control to ingest Save. Do not enqueue from the
extension.

---

## 10. Causal slices (this Worker only)

### Slice 1 — ADRs and README

Write 0066–0071 and update `docs/adr/README.md`. Do not edit 0016/0020/0044/
0045/0049/0061/0063/0065 bodies.

Gate: files exist; index rows present; no in-place accepted-ADR rewrite.

### Slice 2 — Prompt v4

Bump version, tag bounds, prompt text, live test pins, `app.js` fallback.

Gate: Section 13 prompt/provider tests.

### Slice 3 — Admin X policy + wiring

Refactor X helper, coordinator identity-mapping order, combined policy, new
unit tests. YouTube tests still pass.

Gate: Section 13 policy/YouTube/privacy tests.

A failed gate stops the sequence. After slice 3, `ap project check` on the
final candidate SHA.

You may use one or two local commits (for example `docs:` then `feat:`, or
one combined `feat:` with ADR files included). At most two. No push.

---

## 11. Changed-path allowlist

You may create or modify **only**:

**ADRs**

- `docs/adr/README.md`
- `docs/adr/0066-administrator-owned-x-automatic-generic-analysis.md`
- `docs/adr/0067-administrator-companion-review-inbox-and-mutation-trust.md`
- `docs/adr/0068-companion-review-save-and-readiness-triggered-publication.md`
- `docs/adr/0069-five-tag-generic-media-suggestion-contract.md`
- `docs/adr/0070-companion-exclusion-of-movie-workflows.md`
- `docs/adr/0071-native-side-panel-review-inbox-chrome.md`

**Policy, prompt, wiring**

- `src/framenest/application/media_suggestion.py`
- `src/framenest/infrastructure/ai/prompts.py`
- `src/framenest/application/x_acquisition.py`
- `src/framenest/adapters/api/application.py`
- `src/framenest/adapters/api/web/app.js`

**Tests**

- `tests/unit/application/test_media_suggestion.py`
- `tests/unit/application/test_media_analysis_lifecycle.py`
- `tests/unit/application/test_x_automatic_analysis_policy.py` (create)
- `tests/unit/infrastructure/ai/test_nvidia_nim.py`
- `tests/unit/infrastructure/ai/test_vercel_gateway.py`
- `tests/unit/test_configuration.py` (only if a live assertion requires it)
- `tests/integration/test_youtube_acquisition_lifecycle.py` (only if the
  import/signature of the **YouTube** helper would otherwise break; prefer
  zero edits)
- `tests/contract/test_media_suggestion_api.py`
- `tests/contract/test_automatic_analysis_privacy_contract.py` (only if a live
  assertion requires it; do not rewrite PRODUCT.md here)
- `tests/contract/test_local_web_application.py` (only if it asserts the
  `app.js` fallback string)

**Meta (report only)**

- `/home/agile/meta/projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/02_report_00.md`

Any other path is forbidden. Do not “while here” edit ingest Save, picker,
Attach, Alembic, `tailscale_ingress.py`, `youtube_acquisition.py` helper body,
movie identification, `PRODUCT.md`, `SPEC.md`, `docs/X_COMPANION.md`,
companion review API, or extension badge/alarms.

If `nvidia_nim.py` embeds a copied prompt string that would desync from
`prompts.py`, you may edit `src/framenest/infrastructure/ai/nvidia_nim.py`
**only** to keep it importing `MEDIA_SUGGESTION_PROMPT` / `PROMPT_VERSION`
rather than duplicating v3 text. If it already imports `prompts.py`, do not
touch it. Record the choice.

---

## 12. Git, network, secret, and side-effect authority

```text
Git authority: local commits only, at most two, on feat/x-meme-browser-companion; no amend of c581c0e or earlier; no rebase, reset, stash, clean, fetch-that-rewrites, or push; do not update git config; do not skip hooks
Network authority: git ls-remote to the two public refs above; no provider APIs; no FrameNest/NUC endpoints; no signed-in X
Secret authority: none
Filesystem authority: read FrameNest and pinned .ap; write only Section 11 paths plus the Meta report
Side-effect authority: reversible local source/tests/docs/commits
Dependency authority: none
Browser authority: none
```

Commit subjects follow this branch (`feat:` / `docs:`). Example shapes:

- `docs: record companion AI review inbox successor ADRs`
- `feat: cap generic NIM tags at five and allow admin X auto-analysis`

Pass the message via HEREDOC. Do not commit secrets. Do not commit Meta.

If pre-commit hooks modify files, create a **new** commit rather than amending
a predecessor commit you did not create. You may amend only your own
not-yet-pushed commit from this session, and only if a hook auto-modified
files after that commit succeeded.

---

## 13. Tests

Start each candidate SHA with:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline <SHA>
```

Then:

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline <SHA> --operation test-focus -- tests/unit/application/test_media_suggestion.py tests/unit/application/test_media_analysis_lifecycle.py tests/unit/application/test_x_automatic_analysis_policy.py tests/unit/infrastructure/ai/test_nvidia_nim.py tests/unit/infrastructure/ai/test_vercel_gateway.py tests/unit/test_configuration.py tests/integration/test_youtube_acquisition_lifecycle.py tests/contract/test_media_suggestion_api.py tests/contract/test_automatic_analysis_privacy_contract.py tests/contract/test_local_web_application.py -q -p no:cacheprovider
```

Required new cases (in `test_x_automatic_analysis_policy.py` unless an existing
owner is a strictly smaller fit):

- Flag-off is not the X helper’s job; document that scheduler `enabled` still
  gates enqueue (existing lifecycle tests must keep proving flag-off creates
  no pending run).
- Administrator-mapped X-linked upload → allowed.
- Ordinary-mapped / null / unmapped X-linked upload → denied.
- Missing X post for a linked asset → denied.
- No X asset → allowed.
- YouTube remains denied via the existing YouTube lifecycle test.
- Prompt/version/cap are exact; zero and six tags fail live validation.
- Movie prompt/version remains unchanged (do not add movie tests unless an
  imported constant would otherwise break; default: do not touch movie tests).
- Deliberate historical v3 fixtures in files you **are** allowed to edit stay
  v3 when they represent stored history, not the live constant.

Do not run `tests/browser_companion_evidence.test.js`. Do not run a full
Python suite. Do not call a live provider. Do not run JS companion tests
unless you edited extension files (you must not).

---

## 14. Negative authority

- Native Plan Mode
- Max
- Internal delegation / sub-agents
- Push, fetch-that-rewrites, submodule update, hard reset
- NUC, SSH, sudo, origins, `x_acquisition_root`, `framenest-release`,
  `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED=true` as a production/NUC act
- Provider calls, signed-in X/YouTube, Reload-unpacked
- Alembic 0031, companion review routes, overlay, badge, `alarms`, G2 apply
- Editing accepted ADR bodies in place
- CORS, `all_urls`, content-script FrameNest fetch, create-tag
- Granting ordinary users analysis/canonical/publish
- Auto-apply NIM at catalog
- YouTube automatic analysis
- Movie companion / genre UI
- Closing any logical whole
- `PRODUCT.md` / `SPEC.md` / `docs/X_COMPANION.md` (W07)
- AP upgrade ledger edits

---

## 15. INFOSEC R1 (inline, non-independent)

- Assets: catalog-time analysis allow decision; prompt text sent to NIM later;
  identity map.
- Trust: X-linked uploads must not enqueue for ordinary logins even when the
  global flag is on.
- Fail closed on missing mapping, missing claim, and repository errors.
- Do not log logins alongside media titles, suggestion bodies, or credentials.
- Prompt remains anti-injection; do not weaken it.
- Residual risk: enabling the flag later costs real NIM calls for each new
  admin X catalog event. Cooperator owns that later grant. This Worker must
  leave the flag default false.

---

## 16. Required terminal deliverable

Return one professional English report beginning **exactly** with:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Immediately after the heading, echo:

```text
Logical whole identity: framenest-companion-ai-review-inbox-mvp
Worker session ordinal: 02
Worker exchange ordinal: 01
```

Then include:

1. Terminal status (`PASS` / `PARTIAL` / `BLOCKED`);
   `Phase-qualified result: implementation-PASS` (or PARTIAL/BLOCKED);
   `Logical-whole closure: not-closed`;
   report justification `new-mutation`;
   authority expired.
2. Capability handshake.
3. Baseline ledger (start/end commit, parent, tree, public refs).
4. Changed paths and purpose.
5. Proof of the Section 9 invariants (policy matrix, v4 cap, YouTube
   unchanged, ADRs present, ingest Save untouched).
6. Commands and exit codes (`ap project check`, `ap exec test-focus`).
7. Git result (SHAs, no push).
8. INFOSEC R1 residual.
9. `Resolved Execution Issues / Near-Misses` and
   `Pre-Existing Failure Classification` (`none` is valid).
10. Smallest next Orchestrator action: issue W03 (0031 + inbox GET) only after
    verifying this candidate — do not self-issue it.

Write that report only to the Meta path in Section 1.

---

## 17. Quality bar

`PASS` only if:

- HEAD is a descendant of `c581c0e` created by this Worker, working tree
  clean of FrameNest allowlist remainder;
- six Accepted ADRs and README rows exist; no in-place ADR rewrite;
- live generic prompt/validator are v4 with max five tags;
- X admin mapping allows, ordinary/YouTube deny, flag still default false;
- identity mapping is constructed before catalog-coordinator wiring;
- no 0031, no new companion routes, no overlay/badge/alarms;
- focused tests in Section 13 exit 0 via `ap exec`;
- no ambient Python;
- no push, NUC, or provider call.

`PARTIAL` if one named evidence gap remains but the candidate is otherwise
bounded. `BLOCKED` if baseline, Plan Mode, or allowlist contradiction makes
the work unsafe.

---

## 18. Final stop rule

After writing the terminal report, stop. Do not start W03, implement inbox
UI, enable the analysis flag, deploy, or wait for Plan UI approval. Prior
authority is expired.
