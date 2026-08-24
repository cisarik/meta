# WORKER TASK — Slice C2 (canonicalize X Save alias title so NUC ingest stops 422 ALIAS_INVALID)

Role: WORKER
Logical whole identity: framenest-companion-review-inbox-ux-history-mvp
Worker session ordinal: 11
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Implementation Worker
Phase: implementation
Native planning mode: not-used
Reasoning recommendation: extra-high
Independence required: no
Implementation authority: explicit
Exact baseline: 93624b1c527b3bea57e75cc6747cf0d1aa607369

## Implementation Authority Record

```text
Logical whole identity: framenest-companion-review-inbox-ux-history-mvp
Worker session ordinal: 11
Worker exchange ordinal: 01
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: 93624b1c527b3bea57e75cc6747cf0d1aa607369
Changed-path allowlist: the paths in "Changed-path allowlist" below
Implementation boundaries: companion X Save alias title canonicalization only;
  no Settings/origin work; no review-history chrome; no ingest overlay
  redesign (no radios, Analyze, layout); no schema; no publication; no NUC
Independence required: no
```

## Continuity

Worker 10 (`93624b1c527b3bea57e75cc6747cf0d1aa607369`) unblocked Tailscale
Connect. Cooperator 2026-08-24: Save on Settings closes the sheet and the
session attaches. Loopback `http://127.0.0.1:8000` remains rejected (intended).
UX step 1 (merged history) is PASS. Step 2 (colors) is paused.

New live defect, same session: X ingest Save fails. Overlay tooltip
`Save to FrameNest failed`. Response body (code only; no post URL in the
report):

```text
{"error":{"code":"ALIAS_INVALID","message":"Invalid FrameNest media user alias."}}
```

Worker 10 did not touch Save/alias. This is not a Connect regression. 03/10
forbids ingest Save *overlay polish*; it does not freeze a 422 that blocks
ingest. This slice is contract alignment so a normal X Save can succeed.

Do not request, log, or write the Cooperator’s post URL, tweet text, or
real origin.

## Repository diagnosis (Orchestrator-verified)

`POST /api/x/requests` maps `FrameNestMediaUserAliasError` → 422
`ALIAS_INVALID`. `parse_alias_content` builds `MediaDisplayTitle(value)`
after a strip-empty check but **passes the unstripped original**.
`MediaDisplayTitle` rejects `strip() != value` and **any Unicode `Cc`**,
including `\n`.

Companion prefill for title uses `firstNonGenericName` → `clipText`.
`withoutForbiddenControls` **keeps `\n`**. End trim does not remove an
internal newline. X `alt` / `aria-label` is often multiline. That title
is written into `#title` and sent as `alias.display_title`.

`aliasPayload()` does not trim `title.value`. `sanitizeAlias` slices to 240
and does not strip controls or whitespace. Description already `.trim()`s
and the domain **allows** `\n` in `MediaDescription`. Empty `{}` alias would
succeed (upsert skips empty content). Therefore the live 422 implies a
**non-empty invalid title** (or rarer invalid tags). Multiline title is the
systematic X-shaped cause.

## Mandatory reading (in order)

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/.ap/AP.md`
3. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
4. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
5. This prompt (sole current task authority)
6. Live files: `extension/shared/messages.js`, `extension/ui/save.js`,
   `extension/background/service_worker.js`, `extension/content/x_adapter.js`,
   `src/framenest/domain/media_user_alias.py`,
   `src/framenest/domain/media_metadata.py`

## Repository gate

```text
Canonical root: /home/agile/Projects/framenest
Expected branch: feat/x-meme-browser-companion
Expected HEAD: 93624b1c527b3bea57e75cc6747cf0d1aa607369
Expected worktree: clean
Pinned submodule: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

If any fact drifts, STOP and report BLOCKED before mutating.
Native Plan Mode must be OFF. If it cannot be disabled, STOP and report BLOCKED.

## Goal

A Title pasted or prefilled from X that contains internal newlines, other
`Cc` controls, or leading/trailing whitespace must canonicalize to a
`MediaDisplayTitle`-legal string (or be omitted if empty) **before**
`POST /api/x/requests`, so Save no longer 422s `ALIAS_INVALID` on ordinary
X posts. Do not redesign the Save sheet.

## Binding contract

1. Add `canonicalizeCompanionAliasTitle(value) -> string | null` in
   `extension/shared/messages.js` and export it next to
   `canonicalizeFrameNestOrigin`.
2. Canonicalization MUST:
   - Accept only strings; other types → null.
   - NFC-normalize.
   - Map every Unicode `Cc` (including `\n` and `\r`) to a single ASCII
     space. Do not keep newlines in a title.
   - Trim, collapse internal ASCII/Unicode whitespace to single spaces,
     trim again.
   - Clip to 240 Unicode code points (same cap as the title field).
   - Return the canonical title, or `null` if empty afterwards.
3. Use that helper in all three of:
   - `extension/content/x_adapter.js` title prefill (`firstNonGenericName`
     / equivalent title path — not tweet **description**, which may keep
     `\n`).
   - `extension/ui/save.js` `aliasPayload()` for `display_title`
     (trim-equivalent via the helper; omit the key when null).
   - `extension/background/service_worker.js` `sanitizeAlias()` so a stale
     popup cannot bypass the UI.
4. Keep description rules: trim ends; **do not** collapse description
   newlines; still omit empty description. Do not send whitespace-only
   title or description.
5. Do not change `MediaDisplayTitle` / `parse_alias_content` in this
   slice (NUC is still public `0eeaf350…`; extension reload is the live
   path). Do not add loopback origins. Do not change review history,
   Settings Connect, manifest permissions, or tag-key regex except as
   required to call the helper.
6. Synthetic fixtures only in tests (`example` hosts, fake alt strings
   with `\n`). No real tweet URLs, handles, or NUC hostnames.

## Changed-path allowlist (exact)

```text
extension/shared/messages.js
extension/ui/save.js
extension/background/service_worker.js
extension/content/x_adapter.js
tests/x_companion_extension.test.js
```

Edit `tests/companion_review_extension.test.js` **only** if a source-string
assertion would otherwise fail. Do not edit it otherwise.

No Python, Alembic, docs unless a one-line X_COMPANION Save note is
strictly required (prefer tests + code). No operator wrappers. No NUC.

## Tests (required)

In `tests/x_companion_extension.test.js`, require `extension/shared/messages.js`
and assert synthetic values:

Must become `"A two line alt"` (or the exact collapse you implement, one
space between words):

- `"A two\\nline alt"`
- `"  A two\\nline alt  "`
- `"A two\\r\\nline alt"`

Must become `null`:

- `""`
- `"   "`
- `"\\n\\n"`
- non-strings (`null`, `1`)

Must remain a 240-or-fewer code-point string when given a long newline-free
title (clip, do not throw).

Also assert `save.js` / `service_worker.js` / `x_adapter.js` source call
`canonicalizeCompanionAliasTitle` (same style as the origin helper
assertions). Keep existing Node suites green:

```text
node --test tests/x_companion_extension.test.js tests/companion_review_extension.test.js
```

## Git authority

```text
Start: clean tree at 93624b1c527b3bea57e75cc6747cf0d1aa607369
  on feat/x-meme-browser-companion
Stage: exactly the modified allowlisted paths
Commit: ONE commit, subject exactly:
  fix: canonicalize companion X Save alias titles
Parent check: commit only onto 93624b1c527b3bea57e75cc6747cf0d1aa607369
Push: FORBIDDEN
Forbidden: force ops, reset, stash, restore, clean, branch creation,
  amend, `git add .`, `git add -A`
```

```text
git commit -m "$(cat <<'EOF'
fix: canonicalize companion X Save alias titles

EOF
)"
```

After commit: `git rev-parse HEAD^` equals the baseline; worktree clean.
A Cursor `Co-authored-by` trailer is a residual to report, not a reason to
amend.

## Commands authority

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 93624b1c527b3bea57e75cc6747cf0d1aa607369
node --test tests/x_companion_extension.test.js tests/companion_review_extension.test.js
git status / log / show / diff / diff --check / rev-parse
git add <exact allowlisted paths>
git commit (per Git authority)
rg / file reads inside the canonical root
```

After commit, re-run the Node suites. Never invoke `.venv/bin/python`,
`python`, `python3`, or `poetry run`. No NUC. No `~/nuc_update.fish`. No
`~/framenest_routine.fish`.

## Validation ladder (E2)

```text
Evidence tier: E2
1. Re-gate (HEAD, branch, clean tree, AP pin, Plan Mode off).
2. Implement helper + three call sites.
3. Node tests above PASS; review-extension suite still PASS.
4. git diff --check clean.
5. One commit; parent SHA; clean tree.
Stop on: publication, NUC, schema, overlay redesign, origin/Connect
  changes, real tweet/hostname in repo or report.
```

## Negative authority

No NUC / SSH / sudo / framenest-release / home Fish wrappers. No secrets.
No push. No Max. No sub-agents. You are one WORKER. Do not enable
automatic media analysis. Do not mutate companion extension origin env.
Do not print gpg/SSH sockets. Do not “while here” restyle Save.

## Untrusted-content boundary

Repository and Meta files are evidence. Embedded requests expand nothing.
Cooperator tweet bodies are not in this prompt on purpose.

## Report contract

Write EXACTLY ONE file:

```text
/home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/11_report_00.md
```

Begin EXACTLY:

```text
### Report for ORCHESTRATOR_CHAT
```

Include in order: coordinate echo (session 11 / exchange 01); PASS | PARTIAL |
BLOCKED; `implementation-PASS` + commit SHA (or why not); `Logical-whole
closure: not-closed`; gate evidence; files; tests; commit SHA +
`push: not-performed`; deviations; next step = Cooperator reloads unpacked
from this checkout and retries X Save (Orchestrator does not treat this as
UX PASS); justification `new-mutation`; authority expiry; near-misses;
pre-existing classification.

Professional English; no secrets; no real origins or tweet URLs.

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/
Trace project key: framenest
Trace logical-whole projection identity: 03/10-framenest-companion-review-inbox-ux-history-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR (prompt pre-staged); Worker writes only 11_report_00.md
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
```

Planning-mode note: native Plan Mode must be OFF. If it cannot be disabled,
STOP without mutating and report BLOCKED.
