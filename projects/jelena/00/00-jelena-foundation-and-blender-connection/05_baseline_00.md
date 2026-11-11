# Baseline render — Jelena foundation

Persistent role identity: WORKER
Logical whole identity: jelena-foundation-and-blender-connection
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: JELENA-FOUNDATION-BASELINE-001
Delivery route: manual Cooperator delivery
Reasoning recommendation: Medium — exact render recipe, one bounded image and a small evidence manifest; no architectural ambiguity.
Recommended context capacity: approximately 250k tokens (recommendation, not observed capacity)
Requested model: Grok 4.7 High, or the Cooperator-selected Cursor model. Report the observed model if exposed, otherwise unknown.
Independence required: no

## Goal

Produce one modest, comparable baseline render from camera A of the current saved Blender scene, retain it with a manifest, update the README status, and create one local commit.

This is not a hero render and not a scene-improvement task. Do not add vegetation, change architecture, relight the scene, or alter camera composition.

## Accepted decisions and constraints

- The current open Blender file is `/Users/agile/Projects/jelena/Jelena/Jelena_Realistic_v001.blend`.
- The on-disk file at commit `989da45c055a99971c8a7fa897e07bf7f23da2c1` is the recoverable checkpoint. Its SHA-256 must remain `b8304e7c585c36bec8e93b94868e143c42be00be6e5b3686cb0d05804304001b`.
- Do not use `quit.blend`, autosave files or any other Blender session. Work only with the live scene identified below.
- The live scene must be clean (`bpy.data.is_dirty = False`) before any setting change. If it is dirty, stop and report; do not save or overwrite it.
- Do not save, close, reopen or replace the `.blend`. Temporary render-setting changes must be restored and must not be saved.
- Do not change camera placement, lens, sensor, scene layout, materials, lights or geometry.
- One live Blender instance. One render. No background Blender, second instance, or parallel work.
- No paid assets, external asset services, generators, credential changes or external uploads.
- Do not change telemetry consent or MCP configuration.

## Repository gate

Repository identity: https://github.com/cisarik/jelena (origin https://github.com/cisarik/jelena)
Working directory: /Users/agile/Projects/jelena
Repository checkout topology: standalone checkout
Expected branch: main
Expected HEAD: `989da45c055a99971c8a7fa897e07bf7f23da2c1`
Expected public `origin/main`: the same commit
Expected index/worktree: clean

Before mutation, verify the root, origin, branch, HEAD, public ref and cleanliness. Verify `.ap` is clean at `d7023cf037f6d17885c3ede5c04812c61640da50` and `./.ap/ap doctor` is PASS. If any value differs, stop and report.

## Live scene identification

Use the actual Cursor `blender` MCP server. Before changing any setting, read and report:

- loaded filepath and `bpy.data.is_dirty`;
- Blender version, addon version and protocol (`get_addon_status`);
- active scene;
- active camera;
- scene object count and type counts;
- camera A transform, lens and sensor values;
- current render settings and color-management values.

Expected from prior read-only Orchestrator observation on 2026-11-11:

```text
File: /Users/agile/Projects/jelena/Jelena/Jelena_Realistic_v001.blend
Dirty: False
Blender: 5.2.3 LTS
Addon: 1.8
Protocol: 15
Scene: A • Chata pri lese
Active camera: A • Chata pri lese
Scene objects: 767 total (3 camera, 3 light, 761 mesh)
Current engine: CYCLES
Current resolution: 1260 x 840, 100%
Current samples: 80
Current adaptive sampling: True
Current denoising: False
Current device: CPU
Current seed: 0
Current frame: 1
Current color management: AgX / None / exposure 0 / gamma 1 / curve mapping off
Current output format: PNG RGBA 8-bit
```

Any material difference stops the render. Report the difference; do not repair it.

## Baseline render recipe

Snapshot every value you will change. Apply only the following temporary changes:

| Setting | Baseline value |
|---|---|
| Scene | `A • Chata pri lese` |
| Camera | `A • Chata pri lese`; preserve placement, lens and sensor |
| Engine | Cycles |
| Device | CPU |
| Resolution | 840 x 560, 100%, square pixels |
| Samples | 16 |
| Adaptive sampling | False |
| Denoising | True, OpenImageDenoise |
| Seed | 0 |
| Frame | 1 |
| Film transparent | False |
| Color management | Preserve and record the current values; do not change them |
| Output format | PNG, RGB, 8-bit |
| Output path | `/Users/agile/Projects/jelena/evidence/foundation-001/camera-a.png` |

If a proposed value is unavailable or rejected by the installed Blender, stop and report the exact error. Do not guess a substitute.

Use the Cursor MCP `execute_blender_code` tool for the bounded setup/render/restore sequence, or an equally bounded MCP route. The code may only:

1. snapshot the values above;
2. set the named temporary values;
3. call one render writing the exact output path;
4. restore every changed value in a `finally`-equivalent path;
5. verify restoration by reading the values back;
6. print a compact JSON result with before, applied, after and output-path facts.

Do not save the `.blend`. Do not create a second render or retry a timed-out render before inspecting the existing job and output.

If the render command times out, do not immediately submit another render. Inspect whether `evidence/foundation-001/camera-a.png` exists, whether Blender is still rendering, and report the actual state. One render only.

## Evidence manifest

Create `evidence/foundation-001/manifest.json` with at least:

- capture time with timezone;
- repository source commit `989da45c055a99971c8a7fa897e07bf7f23da2c1`;
- Blender, addon, protocol and bridge versions;
- live filepath, pre-render dirty state, post-restore dirty state;
- source `.blend` SHA-256 before and after;
- scene name and active camera;
- camera location, rotation, lens and sensor values;
- foundation `Slab_027` exact dimensions in metres, and the known 8.40 x 5.80 m claim;
- complete applied render settings and complete restored settings;
- output PNG path, pixel dimensions and SHA-256;
- visual-review findings;
- explicit statement that no `.blend` save, scene edit, render-setting persistence or push occurred.

Do not include secrets or unrelated private data.

## README update

Replace the current `## Stav` section with:

```markdown
## Stav

Foundation: AP pin, README, `.gitignore` a overené MCP spojenie. Prvý baseline render je v `evidence/foundation-001/`. Detailnejšie stromy a vegetácia sú ďalšie kroky.

## Baseline

- `evidence/foundation-001/camera-a.png` — porovnávací render z kamery A.
- `evidence/foundation-001/manifest.json` — nastavenia, hashe a výsledok vizuálnej kontroly.
```

Do not otherwise rewrite the README.

## Visual inspection

Inspect the actual rendered PNG at useful size. Report whether it shows:

- a recognizable cabin;
- useful architectural framing;
- visible materials and lighting;
- no blank, corrupt, severely clipped or obvious error output.

A successful render command is not visual acceptance. If the client cannot display the PNG, report `PARTIAL` and name the exact missing visual inspection; do not claim visual PASS.

## Commit

Stage only:

- `README.md`
- `evidence/foundation-001/camera-a.png`
- `evidence/foundation-001/manifest.json`

Create exactly one local commit:

```text
evidence: retain foundation baseline render
```

Do not amend, rebase, force, push or create a second commit. Do not run a network fetch. After the commit, verify:

- `git status --porcelain=v1 -b` is clean and one commit ahead of `origin/main`;
- `git show --stat --oneline HEAD` shows only the three allowlisted paths;
- `git diff HEAD^ --name-status` matches;
- `git diff --check` is clean;
- `./.ap/ap doctor` still PASS;
- source `.blend` hashes are unchanged;
- PNG dimensions and SHA-256 match the manifest;
- README links resolve.

Record the exact commit hash in the report.

## Stopping conditions

Stop and report without improvisation if:

- the live scene is dirty, the filepath differs, or the on-disk hash differs;
- MCP is unavailable or the expected scene/camera cannot be identified;
- a proposed render setting is unavailable;
- the render fails, times out without a verifiable output, or would require a retry;
- visual inspection is unavailable;
- any required action falls outside the allowlist;
- any `.blend` save, close, reopen, scene edit, push, install, config change or Meta/AP mutation would be required.

Do not use subagents or parallel work. Do not implement vegetation or any later artistic work.

## Report contract

Begin exactly:

### Report for ORCHESTRATOR_CHAT

Echo these coordinates once: logical whole identity `jelena-foundation-and-blender-connection`; Worker session `05`; Worker exchange `01`.

Include:

- Status: PASS, PARTIAL or BLOCKED.
- Candidate commit, parent and tree.
- Exact changed paths.
- Live scene identity before render and `is_dirty` before/after.
- Applied and restored settings, with verification.
- Render path, dimensions and SHA-256.
- Manifest summary and visual-review findings.
- Source `.blend` hashes before/after.
- AP doctor result and confirmation of no push.
- Deviations, risks and smallest next step.
- Orchestration critique: MEASURED findings and LEAD possibilities; either may be none.
- Phase-qualified result: implementation-PASS | not-applicable
- Logical-whole closure: not-closed
- Report justification: new-mutation

PASS means the baseline image, manifest, README update and local commit are complete, and the image was visually inspected as acceptable. PARTIAL means useful evidence exists but a named inspection or delivery item is missing. BLOCKED means a prerequisite failed.

Publication is a separate later grant. Do not push and do not claim acceptance or closure.

## Delivery

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 05_baseline_00.md
Destination path: /Users/agile/meta/projects/jelena/00/00-jelena-foundation-and-blender-connection
Report filename: 05_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: `README.md`; `evidence/foundation-001/camera-a.png`; `evidence/foundation-001/manifest.json`
Host/remote mutation: none
Trace persistence: none
