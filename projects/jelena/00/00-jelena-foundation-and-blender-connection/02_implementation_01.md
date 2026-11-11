# Implementation — Jelena repository foundation (AP pin, README, ignore policy)

Persistent role identity: WORKER
Logical whole identity: jelena-foundation-and-blender-connection
Worker session ordinal: 02
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker
Phase: implementation
Task identity: JELENA-FOUNDATION-IMPL-001
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — exact-pin AP integration, managed-block integrity, Git candidate preparation and repository hygiene justify more than ordinary Medium care.
Recommended context capacity: approximately 250k tokens (recommendation, not observed capacity)
Requested model: Grok 4.7 High, or the Cooperator-selected Cursor model. Report the observed model if exposed, otherwise unknown.
Independence required: no

Continuity anchor: session 02 exchange 01 Fresh Evidence Probe report `02_report_00.md`, SHA-256 `9cc59b2c596a0559db49d8f9903e7c18e73bc56ddd8d29231c29ed8e9b19b829`, which confirmed the actual Cursor MCP route to live Blender. Prior authority expired at that terminal report. This is a new complete grant; retained context is convenience, not authority.

## Goal

Produce one coherent repository-foundation candidate in `/Users/agile/Projects/jelena`:

- adopt the exact-pinned stable AP submodule;
- add the minimal project-owned rules outside the managed block;
- add a minimal Slovak README;
- add `.gitignore` and remove the tracked root `.DS_Store`;
- create one local reviewable commit.

This exchange does **not** include a baseline render, a Blender checkpoint, a scene change, MCP configuration changes, or vegetation work.

## Accepted decisions and constraints

- Governing AP pin: `d7023cf037f6d17885c3ede5c04812c61640da50`.
- The local read-only AP checkout `/Users/agile/Projects/ap` is the transport source. It is clean at the pin.
- The project must use the stable AP integration tuple: canonical repository identity, `.ap` submodule, containing-project gitlink, matching checkout, and exact managed `AGENTS.md` block.
- Do not copy universal AP files into the project root. Do not update AP. Do not modify `cisarik/ap` or `cisarik/meta`.
- Slovak README, minimal. Do not add `docs/foundation.md` in this slice; the Cooperator selected a README-only entrypoint. A later slice may add focused docs.
- No Git LFS. No build system. No asset-management service.
- No project-local `.cursor/mcp.json` in this slice. The global Cursor MCP configuration already works; the project-local decision remains open.
- No baseline render, checkpoint copy or `evidence/` directory in this slice. That is a later bounded exchange after the Cooperator decides how to treat the pre-probe unsaved work.
- Do not touch Blender. Do not use the MCP tools. This is a repository-only exchange.
- Standing Cooperator authorization covers one ordinary local commit. Publication is separate: do not push in this exchange.

## Repository gate

Repository identity: https://github.com/cisarik/jelena (origin https://github.com/cisarik/jelena)
Working directory: /Users/agile/Projects/jelena
Repository checkout topology: standalone checkout
Expected branch: main
Expected HEAD: 1919647c837d069dcb0064a963bbe7aafe6396a4
Expected worktree and index: clean
Baseline parent: 73036d97b7e19b019b8520895250a7c0af4b6a6d
Baseline tree: 7296d4428adc9e9a02188cbb766e0727c82ef5f7

Before mutation, verify the physical root, canonical origin, branch, HEAD, clean index/worktree and absence of unexpected untracked paths. If the baseline differs or owner work is present, stop and report; preserve it.

Verify `/Users/agile/Projects/ap` is clean and its HEAD is exactly `d7023cf037f6d17885c3ede5c04812c61640da50`. Do not fetch, pull or switch the AP checkout. If it differs, stop.

## Exact allowlist

Create or change only:

- `.ap` — submodule gitlink at the exact AP pin
- `.gitmodules` — canonical AP URL
- `AGENTS.md` — generated managed block plus the exact project-owned text below
- `README.md` — minimal Slovak entrypoint
- `.gitignore` — exact content below
- `.DS_Store` — deletion of the tracked root file only

Do not change `Jelena/`, any `.blend`, the reference images, `Jelena_Studia.pdf`, `Jelena/Zacni_tu.md`, `.cursor/`, AP or Meta.

## AP adoption sequence

Use fish-compatible commands and the already verified local AP checkout as transport. The URL substitution and file-protocol allowance are bounded to this single submodule command; do not make them permanent Git configuration.

```fish
git -c 'url./Users/agile/Projects/ap.insteadOf=https://github.com/cisarik/ap.git' -c protocol.file.allow=always submodule add https://github.com/cisarik/ap.git .ap
git -C .ap checkout --detach d7023cf037f6d17885c3ede5c04812c61640da50
git add .gitmodules .ap
./.ap/ap init
```

Before continuing, verify:

- `.ap` is a `160000` gitlink at `d7023cf037f6d17885c3ede5c04812c61640da50`;
- `.ap` checkout HEAD equals that gitlink and is clean;
- the `.ap` origin is canonical `https://github.com/cisarik/ap.git`;
- `.gitmodules` records the canonical AP URL, not the local filesystem path;
- `AGENTS.md` contains exactly one canonical managed AP block created by `init`;
- no universal AP files were copied into the project root.

If any check fails, stop and report. Do not repair by hand, do not fetch a newer AP, and do not substitute a different pin.

## Project-owned `AGENTS.md` text

After `./.ap/ap init`, append the following text **outside** the managed block, separated by one blank line. Do not edit the managed block.

```markdown
# Project-local rules

## Communication

- The Cooperator is Michal. Speak to him in Slovak and use feminine grammatical gender for the assistant's self-reference.
- Worker prompts and formal Worker reports are in English. Formal reports begin exactly `### Report for ORCHESTRATOR_CHAT`.
- The Cooperator's Blender UI is Slovak. Owner UI steps use verified Slovak Blender labels and recognizable English addon labels.
- Shell examples are fish-compatible.
- Manual Cooperator delivery is the selected route. The Cooperator persists prompts, reports and notes; Meta Git operations belong to the Cooperator.

## Environment

- Verified on 2026-11-11: macOS Apple silicon, 8 GB RAM; Blender 5.2.3 LTS; Cursor 3.29.15; local MCP server `blender` via `uvx --python 3.11 mcp-for-blender`; Blender addon `MCP for Blender` 1.8, protocol 15; loopback `127.0.0.1:9876`.
- MCP remains local. Optional paid generators and external asset services remain disabled. `MCP_DISABLE_TELEMETRY=1` is set in the Cooperator's MCP configuration.
- One live Blender instance. No background Blender, second instance, or file replacement without an exact grant.
- No paid assets, paid generation services, credential changes, or external uploads without a specific Cooperator decision.

## Blender safety

- No scene mutation, save, close, reopen or render without an explicit task grant and a recoverable checkpoint.
- A server listed in Cursor is not proof of the correct scene. Require direct MCP evidence of the live file and scene.
- Preserve `Jelena/Jelena.blend` and `Jelena/Jelena_Realistic_v001.blend` as baselines. Do not overwrite them without a Cooperator decision.
- Judge visible quality through inspected images, not object counts or successful script execution alone.

## Assets, binaries and renders

- Use ordinary Git for the current small binaries. Do not add Git LFS without a concrete measured need.
- Keep backups, local checkpoints, caches and temporary renders out of Git via `.gitignore`.
- Commit retained render evidence only when a task grant names the exact path and manifest.
- Preserve original deliverables and their hashes; no history rewriting.
- Record external asset source, license and acquisition date before use.

## Protocol

- The governing AP source is the pinned `.ap` submodule. `AP.md` alone owns protocol meaning.
- Do not copy universal AP files into the project root.
- Do not silently update AP or use a newer public revision.
- Project-local rules extend but do not override universal AP.

## Closure

- The only authoritative closure signal is `JELENA — LOGICKÝ CELOK UZAVRETÝ ORCHESTRÁTOROM`.
- Only the ORCHESTRATOR emits it. Workers signal completion through their terminal report status.
```

## `README.md` content

Write this minimal Slovak README, preserving the content and structure. You may fix a broken relative link only if the repository path genuinely differs; report any such correction.

```markdown
# Jelena — chata pri lese

Cvičný projekt vizualizácie chaty pri lese. Cieľom je ukázať, ako AI-assisted Blender práca dokáže postupne vylepšiť existujúci editovateľný 3D model — od základnej scény k detailnejšiemu exteriéru a interiéru.

## Súbory

- `Jelena/Jelena.blend` — pôvodná scéna.
- `Jelena/Jelena_Realistic_v001.blend` — pracovná kópia.
- `Jelena/Jelena_3D.obj`, `Jelena/Jelena_Model.step`, `Jelena/Jelena_Podorys.dxf` — geometrické podklady.
- `Jelena/Jelena_Exterier.png`, `Jelena/Jelena_Dispozicia.png`, `Jelena/Jelena_Interier.png` — referenčné rendery.
- `Jelena_Studia.pdf` — architektonická štúdia.
- `Jelena/Zacni_tu.md` — pôvodný návod.

## Rýchly štart

1. Otvor `Jelena/Jelena_Realistic_v001.blend` v Blenderi 5.2.3 LTS.
2. Scéna **A • Chata pri lese** je hlavná; aktívna kamera je **A • Chata pri lese**.
3. Interiérová kamera je **C • Interiér pri terase**.
4. Render spustíš cez **Render → Render Image**.

## MCP

Lokálne spojenie Cursor → Blender cez `mcp-for-blender` a addon **MCP for Blender** na `127.0.0.1:9876`. Cursor MCP server sa volá `blender`.

## Projektové pravidlá

- AP: `.ap/AP.md`; projektové pravidlá: `AGENTS.md`.

## Stav

Foundation: AP pin, README, `.gitignore` a overené MCP spojenie. Baseline render a detailnejšie stromy/vegetácia sú ďalšie kroky.

## Poznámka

Fotorealizmus nie je cieľom prvého prechodu. Dôležitá je viditeľná kvalita, zachovaný layout a postupné, overiteľné zlepšovanie.
```

## `.gitignore` content

Write exactly:

```gitignore
.DS_Store
*.blend[0-9]*
*.blend@
*.blend.tmp
/.local/
/.cache/
/renders/tmp/
**/blendcache_*/
__pycache__/
*.py[cod]
```

## `.DS_Store`

Remove only the tracked root `.DS_Store` with `git rm .DS_Store`. Do not remove any other `.DS_Store` or unrelated file. The new `.gitignore` must cover it going forward.

## Commit

Stage only the allowlisted paths. Create exactly one local commit:

```text
docs: adopt pinned AP foundation
```

Do not amend, rebase, force, push or create a second commit. Do not run a network fetch. After the commit, verify:

- `git status --porcelain=v1 -b` is clean;
- `git show --stat --oneline HEAD` shows only the allowlisted paths;
- `git diff HEAD^ --name-status` matches the allowlist;
- `git diff --check` is clean;
- `./.ap/ap doctor` passes strict validation;
- `.ap` is clean and at `d7023cf`;
- `.gitmodules` has the canonical URL;
- `AGENTS.md` has one managed block plus the project-owned text;
- `README.md` links resolve and the text is Slovak;
- `.DS_Store` is absent from the index;
- original `.blend` hashes are unchanged.

Record the exact commit hash in the report.

## Cooperator delivery

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_implementation_01.md
Destination path: /Users/agile/meta/projects/jelena/00/00-jelena-foundation-and-blender-connection
Report filename: 02_report_01.md
Prompt persistence owner: COOPERATOR
Report persistence owner: COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: .ap; .gitmodules; AGENTS.md; README.md; .gitignore; deletion of .DS_Store
Host/remote mutation: none
Trace persistence: none

## Validation and evidence

Required focused validation:

```fish
git status --porcelain=v1 -b
git rev-parse HEAD
git show --stat --oneline HEAD
git diff HEAD^ --name-status
git diff --check
git submodule status
git -C .ap rev-parse HEAD
git -C .ap status --porcelain=v1
git config -f .gitmodules --get-regexp '^submodule\.'
./.ap/ap doctor
shasum -a 256 Jelena/Jelena.blend Jelena/Jelena_Realistic_v001.blend
git ls-files .DS_Store
```

If `ap doctor` fails, stop and report the exact failure and the smallest correction. Do not hand-edit generated files to make it pass.

## Stopping conditions

Stop and report without improvisation if:

- the current session is not the exact session 02 that produced `02_report_00.md`, or the continuity anchor does not match;
- repository identity, branch, HEAD, cleanliness or baseline differs;
- `/Users/agile/Projects/ap` is not clean at `d7023cf`;
- the submodule command would require network access or the canonical `.gitmodules` URL cannot be established;
- the generated managed block is missing, duplicated, modified, or `ap doctor` fails;
- any required action falls outside the allowlist;
- any Blender, MCP, Cursor-config, Meta or AP mutation would be required;
- publication would be required; it is not authorized in this exchange.

Do not use subagents or parallel work. Do not implement the baseline render, checkpoint, project-local MCP config, README expansion or vegetation work in this exchange.

## Report contract

Begin exactly:

### Report for ORCHESTRATOR_CHAT

Echo these coordinates once: logical whole identity `jelena-foundation-and-blender-connection`; Worker session `02`; Worker exchange `02`.

Include:

- Status: PASS, PARTIAL or BLOCKED.
- Start commit `1919647...` and the new candidate commit hash.
- Exact changed paths and commit subject.
- AP pin, `.ap` HEAD, `.gitmodules` URL, strict `ap doctor` result and managed-block review.
- README and `.gitignore` review.
- Confirmation that `.DS_Store` is deleted from the index and ignored.
- Confirmation that original `.blend` hashes are unchanged.
- Validation commands and actual results.
- Git result: local commit only; no push.
- Deviations, risks and the smallest next step.
- Orchestration critique: MEASURED findings and LEAD possibilities; either may be none.
- Phase-qualified result: implementation-PASS | not-applicable
- Logical-whole closure: not-closed
- Report justification: new-mutation

PASS means the exact local candidate is produced, validated and committed as specified. PARTIAL means useful work exists but a named validation or delivery item is incomplete. BLOCKED means a prerequisite failed.

The next exchange after this report is a separate fresh independent acceptance of the exact candidate. Publication is a later separate grant. Do not push and do not claim acceptance or closure.

Authority expires at the terminal report, cancellation or supersession.
