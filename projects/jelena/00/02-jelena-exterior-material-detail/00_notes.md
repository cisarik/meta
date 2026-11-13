# Jelena — `jelena-exterior-material-detail` — Notes

Orchestrator-authored. Not task authority.

## 2026-11-13 — Whole opened; restoration and handout revalidation

- Logical whole identity: `jelena-exterior-material-detail`
- Development run identity: `jelena-detail-development-00`
- Orchestrator session scope: `logical-whole`
- Orchestrator access profile: `ChatOrchestrator`
- Phase: Restoration
- Handout: `/Users/agile/meta/projects/jelena/00/02-jelena-exterior-material-detail/00_handout.md`
  - SHA-256 `10979578f3f2e7b6b50073b0072f227ec6d0f59f36d8f0d4104490fea0dc4f2e`
  - Received `provisional`; frozen on open; not edited in place.
  - Author: Master ChatOrchestrator. Persister: Michal, manually. Handout is untracked in the Meta worktree; Meta public `main` was `57768dc341ed0dd3301c6079aa00e088b66f6b88` at inspection, so the handout itself is not in the public Meta tree.
- Predecessor: `jelena-vegetation-detail`; authoritative closure
  `/Users/agile/meta/projects/jelena/00/01-jelena-vegetation-detail/00_closure.md`.
  The predecessor is closed, including publication. Its historical withheld-acceptance entries are not reopened.
- Selected whole: exterior material and craft detail of the existing cabin and terrace. This is the Cooperator-delegated selection; it is not re-asked.

### Continuity verified read-only

- Canonical repository: `https://github.com/cisarik/jelena`
- Working directory: `/Users/agile/Projects/jelena`
- Branch: `main`; `HEAD` `918d3db6b421048c85b25a7712bd40da6afb0660`; the accepted `v003` deliverable was published at `9d75587e39a97e4f26b106ef2d48a141515401dd`, which is HEAD's parent.
- Index/worktree: clean.
- Local `origin/main` and directly observed public `refs/heads/main`: `918d3db6b421048c85b25a7712bd40da6afb0660` (`git ls-remote`, 2026-11-13).
- Governing AP: `https://github.com/cisarik/ap` at `d7023cf037f6d17885c3ede5c04812c61640da50`; `.ap` gitlink equal, detached checkout clean; `./.ap/ap doctor` PASS, variant `stable`.
- Accepted starting file: `Jelena/Jelena_Realistic_v003.blend`
  - SHA-256 `e97fe7d745e2b5b0f8ce69ab85d8fc449dbd929e277ebc0bd566582844fedf3b`
  - 46,815,428 bytes; present on disk.
- Accepted visual: `.local/renders/smreky-camera-a.png`
  - SHA-256 `3956952b86a6b6a2246a13426949245aa9f6555c06901b148f356781881799e3`
  - 840 × 560; PNG metadata records frame 1, 16 samples, scene and camera `A • Chata pri lese`, file `Jelena_Realistic_v003.blend`.
- Accepted evidence: `evidence/vegetation-003/manifest.json`
  - SHA-256 `3251b5daca9395be4738f08c5eb11b1872904f5b65ba9d76e3ddb2c8f55c00b8`.
- Protected baselines unchanged:
  - `Jelena/Jelena.blend` `d2ed50aea93dfc00201be1def6db0b0b353be7eb473a799225c8a6f1386eb06f`
  - `Jelena/Jelena_Realistic_v001.blend` `b8304e7c585c36bec8e93b94868e143c42be00be6e5b3686cb0d05804304001b`
- Foundation evidence unchanged:
  - `evidence/foundation-001/camera-a.png` `db1386a24a00765c976eb8c216f1936f91ccbeb6eb4c8b9bb7da5b7b24a5cd8f`
  - `evidence/foundation-001/manifest.json` `f45b53d0c8a73f059f0b457d6ac8c0c4de9f02dd9ffe6b329e3ac62cf8b28fae`
- `README.md` SHA-256 `9130f50a439fba34ac39b087e72e1eed8528f01aa51097fa750534a173fb5f22` names `v003` as accepted, but its Quick Start step 1 still instructs opening `v001`. The contradiction is confirmed; a narrow Quick Start correction may be part of the implementation grant.
- The run map `/Users/agile/meta/projects/jelena/00/00_RUN_MAP.md` is absent. Master owns run-level status; this whole does not create or claim it.
- `.local` tracked checkpoints and renders remain tracked by the predecessor's explicit Cooperator decision. No untracking, LFS or history rewrite.

### Live Blender state — direct read-only observation

Observed 2026-11-13 04:22 CET through the local addon socket on `127.0.0.1:9876` using read-only property queries (no assignment, no operator, no render, no save, no scene switch):

- One Blender process (PID 3187) listening on `127.0.0.1:9876`; one `mcp-for-blender` bridge process. No second instance observed.
- Blender `5.2.3 LTS`; addon `MCP for Blender` 1.8; protocol 15.
- `bpy.data.filepath`: `/Users/agile/Projects/jelena/Jelena/Jelena_Realistic_v003.blend`
- `bpy.data.is_dirty`: `false`; `is_saved`: `true`.
- Active scene: `A • Chata pri lese`; active camera: `A • Chata pri lese`; lens 46 mm.
- Scene A: 870 objects. Scene B `B • Zariadená dispozícia`: 308 objects. Total unique objects: 1,031, so the scene counts overlap and some objects are shared; the exact shared set must be measured. 30 materials; 5 lights; 3 cameras; no image textures observed (only the `Render Result` viewer image).
- Saved render settings: Cycles, 1260 × 840, 80 samples, adaptive sampling on, denoising off, device CPU, AgX, look `None`, exposure 0.0, gamma 1.0, display device sRGB, film transparent off.
- The accepted PNG's 840 × 560 / 16-sample recipe is not the live saved recipe. The difference is consistent with a temporary comparison override, but the historical settings were not fully recorded. The implementation must create a fresh before render from `v003` under one explicitly recorded matched recipe; it must not present the historic PNG as the new before.
- Active mutation: none. No Worker is dispatched. No Blender save, close, reopen, render, load or scene mutation is authorized by this note.

### Handout Revalidation Record

```text
Handout revalidation: /Users/agile/meta/projects/jelena/00/02-jelena-exterior-material-detail/00_handout.md
Received handout status: provisional
Revalidated against: Jelena local main/HEAD/origin/main and directly observed public refs/heads/main 918d3db6b421048c85b25a7712bd40da6afb0660; clean index/worktree; AP gitlink and checkout d7023cf037f6d17885c3ede5c04812c61640da50 with ap doctor PASS and variant stable; v003 SHA-256 e97fe7d745e2b5b0f8ce69ab85d8fc449dbd929e277ebc0bd566582844fedf3b; accepted PNG SHA-256 3956952b86a6b6a2246a13426949245aa9f6555c06901b148f356781881799e3; evidence/vegetation-003/manifest.json SHA-256 3251b5daca9395be4738f08c5eb11b1872904f5b65ba9d76e3ddb2c8f55c00b8; predecessor closure; direct read-only live Blender identity query; Meta public main 57768dc341ed0dd3301c6079aa00e088b66f6b88
Usable facts: canonical repository and public HEAD 918d3db; accepted v003 and accepted PNG hashes; accepted evidence manifest; main scene and camera A; v003 loaded clean and saved in the live session; scene A 870 objects, scene B 308 objects, 30 materials; camera A 46 mm; Blender 5.2.3 LTS, addon 1.8/protocol 15; protected baselines and foundation evidence unchanged; README names v003 while Quick Start still opens v001; run map absent; tracked .local files public by Cooperator decision; predecessor closed and published
Stale facts and corrections: no handout fact was materially stale. Related corrections: the predecessor closure's "blank default startup scene" observation is superseded by today's measured v003 clean session, and the handout already treated it as non-current; the live saved 1260x840/80-sample settings do not match the accepted PNG's recorded 840x560/16-sample render, and no historical color-management or device setting is invented.
Not revalidated: effective Cursor model and reasoning enforcement in the intended Planner session; actual native Plan mode availability in that session; health of the Cursor MCP bridge path (the direct addon socket was observed, not the Cursor client path); scene-B shared-datablock ownership and exact material/UV/modifier inventory (deferred to the Planner's read-only inspection); peak memory and render duration for the new matched recipe; Meta public branch inclusion of this untracked handout and the new notes; full current bridge/process count beyond the single listener and bridge observed
Handout disposition: adopted
```

### Restoration classification

- Restoration readiness: **PASS** for read-only restoration and bounded planning.
- Live planning prerequisite: **PASS** — `v003`, scene A, camera A, clean and saved.
- Live execution readiness: **NOT YET GRANTED** — it requires the Planner's evidence-grounded plan, Orchestrator acceptance, and a separate complete implementation grant with checkpoint, render and Save As authority.

### Material observations and limits

- The Orchestrator inspected the accepted PNG directly. The cabin and terrace are readable; the façade reads as a fairly uniform orange-brown vertical timber surface, the roof as a uniform dark sheet, the glazing as washed-out transparent glass, and the terrace as a flat plank slab. These are framing observations for the Planner, not a substitute for its own material and geometry inspection.
- Deferred and out of scope: tree errors, floating foliage, foliage saturation, tree-generation improvements. They are known limitations of the accepted baseline and do not fail this whole.
- Excluded: interior redesign, new landscaping, building redesign, animation, additional buildings, broad repository cleanup, MCP replacement, AP changes, external asset services, paid services, credentials, uploads.
- Preserved: cabin footprint, roof silhouette, openings, terrace footprint and principal layout; camera A transform and lens; existing vegetation, ground cover and tree placement; scene B behavior; protected baselines; accepted v003 and historical evidence.
- `v004` is absent; it is the expected new deliverable path if the Planner confirms it remains unused.
- New artifact retention must be deliberate. Temporary renders and iteration checkpoints stay out of Git unless a later grant names an exact retained path and manifest.

### Next bounded step

- Fresh Planner, Worker session `01`, exchange `01`, Cursor native Plan mode **required**, recommended High reasoning.
- Prompt: `01_planning_00.md` in this directory, written directly by the ORCHESTRATOR under the preserved 2026-11-11 Cooperator delivery decision. SHA-256 `776c5881a8f52c88507d4a687a57143074d8c8d023609d955bb3b888fb3e7095`.
- Report: `01_report_00.md`, written by the assigned WORKER if the client permits; otherwise returned in-session for exact Orchestrator persistence.
- Planning is read-only. It grants no implementation, acceptance, publication, Git or Blender mutation authority.

## 2026-11-13 — Planner report received; plan accepted with corrections; implementation grant issued

- `01_report_00.md` received: 27,270 bytes, SHA-256 `b295a9fbf1ec4f4684414f538edb561bb5c6324ea5f7f3b98f2086adaafa14e4`; standard header; coordinates `01` / `01`; `status: PASS`; start and end commit `918d3db6b421048c85b25a7712bd40da6afb0660`; `Phase-qualified result: not-applicable`; `Logical-whole closure: not-closed`; `Report justification: new-evidence`; no repository, host, Blender or Git mutation.
- Delivery limitation: the report body records that native Plan mode blocked the granted write of `01_report_00.md`. The file is now present and complete at the exact path, so delivery was completed under the Planner-Artifact Report Completion Repair route. The body sentence "the report file was not written" describes the client limitation at generation time, not the current delivery state. The report is frozen evidence; do not edit it.
- The report's plan is accepted with the corrections recorded below. Planning authority expired at the terminal report.

### Orchestrator verification of the plan's material facts

The Orchestrator re-read the live scene read-only through the Cursor MCP/blender path on 2026-11-13. Key facts confirmed:

- Addon `MCP for Blender` 1.8, protocol 15; the installed server expects protocol 16 and reports fallback operation. The mismatch is recorded; do not update or reinstall inside this whole.
- Live file `Jelena_Realistic_v003.blend`, `is_dirty` false, scene `A • Chata pri lese`, camera A.
- Scene A 870 objects; scene B 308; 1,031 unique; 147 shared; 723 only A; 161 only B. Camera A is linked into both scenes. Vegetation collection `10 • Vegetácia scéna A` has 93 objects. World strengths and light energies match the report.
- `Fasáda • termodrevo`: 491 users; 335 scene-A objects (210 battens in collection 01 + 102 battens in collection 02 + 21 `Exterior_*` + 2 `Gable_*`) and 156 scene-B objects in collection 08. The material graph matches the report: Object coordinate multiplied by `(10, 10, 0.47)`, one noise at scale 1/detail 3.4, ramp `(0.115, 0.043, 0.018)` to `(0.37, 0.177, 0.074)`, bump strength 0.13/distance 0.028 m, roughness 0.5.
- `Sklo • priehľadné`: 10 users; nine collection-03 exterior panes plus shared `Sprchová zástena`. The plan's scene-A-only assignment to the nine panes is correct.
- `06 • Terasa`: 51 objects; no object is in another collection; all 51 are in both scenes. The duplication + scene-A view-layer exclude plan is structurally sound.
- `Terasa • smrekovec`: 25 users, all in `06 • Terasa`, all in both scenes: 16 `Terasová doska` planks, 2 `Schod terasy` steps, `Terasový stôl`, 4 table legs, 2 `Vstupný schod` entry steps.
- `Strecha • falcovaný plech`: 45 users, all in collection 02, scene A only. The in-place shader edit is scene-A-only.
- `Jelena/Jelena_Realistic_v004.blend`, `06b • Terasa • scéna A`, the checkpoint, the script and `evidence/exterior-004/` are all absent.

### Accepted corrections to the plan

1. **Detail evidence order.** The detail crop must be rendered from the final selected after state, not from the first pass. Sequence: before, first after, up to two refinement afters, final detail, optional presentation. Maximum 6 renders remains: before, first after, refinement-1 after, refinement-2 after, final detail, optional presentation. No intermediate detail render is retained.
2. **Publication is a separate grant.** The implementation grant does not commit or push. The complete candidate, evidence and manifest are reported first; the Orchestrator inspects them and Michal gives subjective acceptance; only then does a separate publication grant commit the exact paths and perform one ordinary non-force push. This corrects the report's one-step "commit after acceptance" sequencing.
3. **Scene membership, not name alone.** New façade materials must be assigned by scene-A membership. The name pattern `Fasádna lata*` matches 453 objects; `Fasádna lata.312`–`.452` are the 141 scene-B objects in collection 08 and must keep the original material. The script must not select by name alone.
4. **Explicit scene-B readbacks.** Before Save As and before the report, verify: scene B still has 308 objects; scene B view layer includes `06 • Terasa`; scene A view layer excludes `06 • Terasa` and includes `06b`; `06b` has 51 duplicates linked only to `06b` and scene A; the original façade material still has its 156 scene-B users and no new-material user in scene B; the original terrace material still serves the 25 scene-B terrace objects; `Sprchová zástena` still uses `Sklo • priehľadné`; `Strecha • falcovaný plech` has no scene-B user; collection `10 • Vegetácia scéna A` still has 93 objects; camera A/B/C transforms, lights and worlds are unchanged.

### Implementation grant

- Worker session `01`, exchange `02`, `current-worker-session`, profile Implementation Worker, `Native planning mode: not-used`, recommended High reasoning.
- Continuity anchor: accepted `01_report_00.md`. Prior planning authority expired; this is a complete renewed grant.
- Prompt: `01_implementation_01.md`, written directly by the ORCHESTRATOR. SHA-256 `e256aaf24382230a9108f8a7c01cc0147c1445253b02a2fe475f403af392532e`.
- Report: `01_report_01.md`, written by the assigned WORKER.
- Exact scope: checkpoint copy, live-scene material pass, terrace duplicate set, Save As `Jelena/Jelena_Realistic_v004.blend`, evidence under `evidence/exterior-004/`, script `scripts/exterior_material_v004.py`, minimal README Quick Start correction. No Git commit or push in this grant.
- Active mutation: authorized by this grant; no Worker mutation observed at note time.

## 2026-11-13 — Implementation report received; technical validation PASS; acceptance requested

- `01_report_01.md` received: 11,284 bytes, SHA-256 `2bae4a9b15747630bf378345f8b90ceb93c709d8c9d139413f2a28385f2fbb9c`; standard header; coordinates `01` / `02`; `status: PASS`; `Phase-qualified result: implementation-PASS`; start and end commit `918d3db6b421048c85b25a7712bd40da6afb0660`; no Git commit or push; `Logical-whole closure: not-closed`.
- Result files and hashes verified by the ORCHESTRATOR:
  - `Jelena/Jelena_Realistic_v004.blend` — 46,850,325 bytes — `f02ad73ce879cd30ced6ab88dda01c6a4ecbfc7b03333b74b9036190712d5272`
  - `scripts/exterior_material_v004.py` — 19,211 bytes — `6c332d84e9580b31017ca198bf238d5423faa2766cd1a1795ef0e889889009e4`
  - `evidence/exterior-004/camera-a-before.png` — `55a13ccf97b87c2bd2af99c99de0cec5de16a27a497644403dc9acfb2626ae2c`
  - `evidence/exterior-004/camera-a-after.png` — `da56d8e671f8db64b42fdeafdc784ab8a4144a151861faec0dc3cf5c12a0dc72`
  - `evidence/exterior-004/camera-a-detail.png` — `8979d02f2d59f4e93727f9671102f545582ee667a22f7919fc4e9599d2031771`
  - `evidence/exterior-004/camera-a-presentation.png` — `81ea36d93a0968e2c9330e6b4f8c9fe6a27a858a81d8e2f651964a201c7ffde8`
  - `evidence/exterior-004/manifest.json` — `172183489883a9c34ecab5ac2ce4afca03dbee758d73cda562b0b0f12b871d5e`
  - `README.md` — `e4e8d95dff90656f0ed88e04e73758574ac172dfb0f6bb891054554d73e57035`
  - checkpoint — `e97fe7d745e2b5b0f8ce69ab85d8fc449dbd929e277ebc0bd566582844fedf3b`, equal to `v003`
- Live readback on `v004`: clean and saved; scene A 921 objects, scene B 308; `06b • Terasa • scéna A` has 51 duplicates; scene A excludes `06 • Terasa` and includes `06b`; scene B includes `06` and has no `06b`; original façade material 156 scene-B users and 0 scene-A; new façade materials 312 and 23 scene-A users; original terrace material 25 scene-B users; new terrace material 25 scene-A users; original glass on `Sprchová zástena`; nine exterior panes on the new glass; roof 45 scene-A users; vegetation 93; cameras, lights and worlds unchanged; only `Render Result` image datablock; no libraries. `v004` opens with the working recipe 1260×840, 80 samples, denoise off, PNG RGBA, output `/tmp/`.
- The ORCHESTRATOR inspected the four images directly. The after is visibly richer than the before: darker batten gaps and grain, glass that reads as glass with reflected interior, deck grain and gaps, and unchanged roof seams. The detail crop shows the façade, three terrace doors and deck. No new intersection, floating piece, doubled terrace or broken silhouette was seen. Roof roughness remains subtle. Tree defects are unchanged and deferred.
- Technical validation: **PASS**. Matched before/after settings are recorded; four retained renders; no refinement; no batten bevel; render time 162.285 s; highest sampled RSS 989,264 KiB (0.943 GiB), labelled sampled, not peak.
- Disclosed deviation accepted: the backing bump uses a broad object-space noise as height for the specified strength/distance; it is not a second color pattern.
- No Git commit or push. The worktree contains only the expected new files, checkpoint and README edit.
- Acceptance is requested from Michal with the four numbered questions. Publication is a separate grant after his explicit visual acceptance.

## 2026-11-13 — Michal's feedback: façade rejected; one bounded correction authorized

- Michal answered the four questions:
  1. **Façade: not accepted.** He sees no difference in the façade and wants its appearance closer to the attached reference image (traditional natural-wood cabin with visible grain, varied board tones and deep shadow lines).
  2. **Glass: yes**, it must look like glass that shines.
  3. **Roof: corrected by Michal.** He initially said OK, then corrected himself: the roof is **not** OK. He wants it in the shingle style of the reference image, but the original dark roof colour must remain. This supersedes the earlier roof-OK answer.
  4. **Yes**, we remain in the fourth logical whole and `v004`.
- Disposition: acceptance is withheld for the façade and the roof. The glass must remain shiny; the terrace, architecture, scene B, vegetation, camera and lighting are not reopened. One smallest coherent correction is authorized for the façade material and the roof surface.
- Interpretation: preserve the contemporary cabin and the existing roof silhouette, ridge, eaves, chimney and dark colour. The reference is material art direction — natural wood character for the façade and a shingle-row roof surface — not a redesign into the reference's log cabin. The roof keeps the original dark anthracite colour while gaining a visible shingle pattern and relief. A light wood-coloured roof is not requested.
- Correction route: same healthy Worker session `01`, exchange `03`, profile `Bounded Correction Worker`, `Native planning mode: not-used`, recommended High reasoning.
- Correction prompt: `01_correction_02.md`, written directly by the ORCHESTRATOR. SHA-256 `b684ac2291147daf5adf20c3cff629b299f895f4c2d17c1c596ea05a5eb5b0d1`. Report: `01_report_02.md`.
- Correction scope: only `Fasáda • lata • A`, `Fasáda • podklad • A`, the roof surface and one optional small batten bevel; new per-board tonal variation, stronger visible grain, natural warm-brown palette, soft sheen, deeper gaps; a shingle-style roof surface in the original dark colour, with the standing-seam ribs preserved but hidden and a new editable shingle layer/material. No glass, terrace, architecture silhouette, scene B, vegetation, camera or light change. No image textures, external assets, network or Git commit/push.
- Recovery and evidence: checkpoint the current first-pass `v004` to `.local/checkpoints/Jelena_Realistic_v004-before-facade-correction.blend`; overwrite `v004` only after the checkpoint. Preserve `evidence/exterior-004/` as the first-pass history; write the corrected evidence to `evidence/exterior-004-correction-01/` with the matched after, façade detail, roof detail and manifest. The README points at the final evidence only in the later publication grant.
- No commit or push in the correction grant. The first-pass `v004` remains preserved in the checkpoint; `v003` remains untouched.
- Active mutation: authorized by the correction grant; no Worker mutation observed at note time.

## 2026-11-13 — Correction report received; technical validation PASS; acceptance requested

- `01_report_02.md` received: 8,809 bytes, SHA-256 `347a7ffc23ce432d1c5625909b619679841dfc7ccfc97c3f100f7c0d77f178fa`; standard header; coordinates `01` / `03`; `status: PASS`; `Phase-qualified result: implementation-PASS`; start and end commit `918d3db6b421048c85b25a7712bd40da6afb0660`; no Git commit or push; `Logical-whole closure: not-closed`.
- Corrected result hashes verified:
  - `Jelena/Jelena_Realistic_v004.blend` — 46,888,090 bytes — `24927e9ae55ba45287578ff1cb3e999ea6f45da806fcb3ccdec5b98c64500095`
  - `scripts/exterior_material_v004_correction.py` — 21,700 bytes — `536184f2c76934334352c5b02202afc08d2dbc81111fb349e096b4b242ec80b8`
  - `evidence/exterior-004-correction-01/camera-a-before.png` — `55a13ccf97b87c2bd2af99c99de0cec5de16a27a497644403dc9acfb2626ae2c`
  - `camera-a-after.png` — `7447be3b8057284d422298097c8c2e144849802d2e5c5ec0ae256a83ae0f13e1`
  - `camera-a-detail.png` — `2ef368ca4ecb89420faaf07231f0c082d5ee5df6e6a2a1452d6316302c57f829`
  - `camera-a-roof-detail.png` — `085cbacc5c80fb9ad300c8237c59b58770dcc00ac9b09a926fdd0518642b3ffe`
  - `camera-a-presentation.png` — `e46c54e3d88cd0d4a64f8ae9542fa38ad2635af51a2c307abee69dcc863887e2`
  - `manifest.json` — `8417fe35329b52695e7225a77b90e9f8490d4e37c9726e6b129670709feff58b`
  - checkpoint — `f02ad73ce879cd30ced6ab88dda01c6a4ecbfc7b03333b74b9036190712d5272`, equal to the first-pass v004
- Live readback on corrected `v004`: clean and saved; scene A 922 objects, scene B 308; `02a • Strecha • pôvodné falce` has 38 ribs and is excluded on scene A; `02b • Strecha • šindeľ` has one 740-quad shingle mesh, scene A only; `06b` has 51 duplicates; scene A excludes `06`, scene B includes it; façade material counts 156 B / 312 A / 23 A; terrace 25 B / 25 A; glass 1 original / 9 new; roof metal 45 A; shingle material 1 A; vegetation 93; cameras/lights/worlds unchanged; only `Render Result`; working recipe 1260×840, 80 samples, denoise off, PNG RGBA, `/tmp/`.
- The ORCHESTRATOR inspected the corrected after, façade detail, roof detail and presentation directly. The façade now has clear board-to-board tone variation, visible grain, dark gaps and no black outline; the roof reads as horizontal staggered dark shingles, not standing-seam metal; ridge, eaves, chimney and silhouette remain; the glass is glossy; the terrace is unchanged. No z-fighting, light-wood drift, new intersection or doubled terrace was seen.
- The Worker reports that the reference image file was not present in its session; the correction followed the written art-direction text. The visual result matches that text, but Michal's direct comparison with the reference remains the acceptance test. If he wants a tighter match, one further bounded pass can use the actual image.
- Technical validation: **PASS**. Render time 142.744 s; highest sampled RSS 1,065,952 KiB (1.016 GiB), sampled not peak. No internal adjustment was used. No commit or push.
- Acceptance is requested from Michal with the four questions. Publication remains a separate grant after his explicit visual acceptance.

## 2026-11-13 — Michal's second feedback: roof and glass accepted; façade still needs a closer match

- Michal answered the correction questions:
  1. **Façade: still not accepted.** He wants it to resemble the reference image more.
  2. **Roof: accepted.** The shingle character is there.
  3. **Glass: accepted**, glossy.
  4. **Continue** — we remain in the fourth logical whole and `v004`.
- Interpretation: the remaining gap is the cladding direction. The reference has horizontal timber log walls with a vertical-board gable; the current cabin has vertical battens across the whole façade. The next correction changes the **main-wall cladding to horizontal timber** while keeping the gable vertical, the shingle roof, the glossy glass, the terrace, the openings and the cabin silhouette.
- This is **refinement 2 of 2** within the handout's envelope. If it still does not match, stop and report PARTIAL for an Orchestrator/Cooperator decision; do not loop.
- Correction route: same healthy Worker session `01`, exchange `04`, profile `Bounded Correction Worker`, `Native planning mode: not-used`, recommended High reasoning.
- Correction prompt: `01_correction_03.md`, written directly by the ORCHESTRATOR. SHA-256 `c1c5481465a5d80f1a8d05a1f526fbaf7b06691e8a361dde9b853d6299ef838c`. Report: `01_report_03.md`.
- Correction scope: hide and preserve the 210 scene-A main-wall vertical battens in `01a • Fasáda • pôvodné latky`, excluded on scene A; keep the 102 gable battens visible with `Fasáda • lata • A`; add a new horizontal timber cladding material/layer to the 21 scene-A `Exterior_*` wall panels (`Fasáda • zrub • A` or equivalent); keep the roof shingles, glass, terrace, plinth, walls, openings, frames, cameras, lights, worlds, vegetation and scene B unchanged. No stone base or new props in this pass.
- Recovery and evidence: checkpoint the current corrected `v004` `24927e9ae55ba45287578ff1cb3e999ea6f45da806fcb3ccdec5b98c64500095` to `.local/checkpoints/Jelena_Realistic_v004-before-facade-cladding-correction.blend`; preserve `evidence/exterior-004/` and `evidence/exterior-004-correction-01/`; write the new evidence to `evidence/exterior-004-correction-02/` with the copied original before, the new after, façade detail, optional presentation and manifest. The README is updated only in the later publication grant.
- The reference image must be visible in the Cursor chat. The previous correction session did not receive the image file; this prompt requires the Cooperator to attach it. If the image is not visible, the Worker must stop.
- No commit or push. `v003` remains untouched; the first two candidates remain in their checkpoints/evidence.

## 2026-11-13 — Cladding correction report received; technical validation PASS; acceptance requested

- `01_report_03.md` received: 7,747 bytes, SHA-256 `01efd543d100f5ad6e67bac452a7793b2dcd3e458b902b7ead5fd1af2ef895f5`; standard header; coordinates `01` / `04`; `status: PASS`; `Phase-qualified result: implementation-PASS`; start and end commit `918d3db6b421048c85b25a7712bd40da6afb0660`; no Git commit or push; `Logical-whole closure: not-closed`.
- Result hashes verified:
  - `Jelena/Jelena_Realistic_v004.blend` — 46,923,160 bytes — `00d1dbe65c15a7e86ae52480b4e8aa3cad5744cac9443a10e5a5b230ea9c76aa`
  - `scripts/exterior_material_v004_correction_02.py` — 16,550 bytes — `bd71caf9d7956a97f5d63e004323ca10a947a1cfbb8811c3e08bb4a567223f24`
  - `evidence/exterior-004-correction-02/camera-a-before.png` — `55a13ccf97b87c2bd2af99c99de0cec5de16a27a497644403dc9acfb2626ae2c`
  - `camera-a-after.png` — `da2035b5088ae9242ac4901172d28a16a66b6149d07cc6f6d51937b6cc2f89e5`
  - `camera-a-detail.png` — `db14282c3d315f1597f75fbd27f90d3fd111b301090b576d491b1e51801bef35`
  - `camera-a-presentation.png` — `668bda523029f3eab3eef02e8233e5357dcaa9861f151484bebf37267282c6a7`
  - `manifest.json` — `848d3f2e2bb3966a4ac3fad3da09aa0062e4fdc85e53c386a8249b3d0f6dedfc`
  - checkpoint — `24927e9ae55ba45287578ff1cb3e999ea6f45da806fcb3ccdec5b98c64500095`, equal to the previous corrected v004
- Live readback on the new `v004`: clean and saved; scene A 923 objects, scene B 308; `01a • Fasáda • pôvodné latky` has 210 battens and is excluded on scene A; `01b • Fasáda • zrub • A` has one 1,020-face / 2,040-triangle log mesh, scene A only; `02a` has 38 ribs, excluded; `02b` has the 740-quad shingle mesh; `06b` has 51 duplicates; scene A excludes `06`, scene B includes it. Original façade 156 B / 0 A; batten material 312 A total (210 hidden + 102 visible gable); backing 2 A (gable slabs); new log material 1 A; seam material 21 A; terrace 25 A/B original + 25 A new; glass 1 original + 9 new; roof metal 45 A; shingle 1 A. Vegetation 93, cameras/lights/worlds unchanged, only `Render Result`, no libraries, working recipe 1260×840 / 80 samples / denoise off / PNG RGBA / `/tmp/`.
- The ORCHESTRATOR inspected the new after, façade detail and presentation directly. The main walls now read as horizontal stacked timber with dark seams, a warm medium-brown tone and a shallow rounded profile; the gable remains vertical boards; the dark shingle roof, glossy glass, terrace and frames are unchanged. The logs stop at the openings and do not cover glass. No black outline, new intersection or doubled terrace was seen. The façade is substantially closer to the reference composition than the vertical-batten version.
- Known limits: the 210 vertical battens are hidden by scene-A view-layer exclude, not deleted; a new view layer would reveal them. Log ends are inset 4 mm at panel joints, so a hairline vertical break is possible. The reference's stone base and props were intentionally not added in this pass.
- Technical validation: **PASS**. Render time 133.777 s; highest sampled RSS 946,448 KiB (0.903 GiB), sampled not peak. No internal adjustment was used. No commit or push.
- Acceptance is requested from Michal with the four questions. This was refinement 2 of 2; if the façade is still not accepted, the next step is an Orchestrator/Cooperator decision, not another automatic pass. Publication remains a separate grant after explicit visual acceptance.

## 2026-11-13 — Michal accepted the final candidate; publication authorized as a separate grant

- Michal answered **PASS** to the final acceptance request. The corrected `v004` with horizontal timber main walls, vertical gable, dark shingle roof, glossy glass and unchanged terrace is accepted as the visual result.
- Accepted candidate: `Jelena/Jelena_Realistic_v004.blend`, SHA-256 `00d1dbe65c15a7e86ae52480b4e8aa3cad5744cac9443a10e5a5b230ea9c76aa`, 46,923,160 bytes.
- Accepted final evidence: `evidence/exterior-004-correction-02/` — `camera-a-after.png` `da2035b5088ae9242ac4901172d28a16a66b6149d07cc6f6d51937b6cc2f89e5`, `camera-a-detail.png` `db14282c3d315f1597f75fbd27f90d3fd111b301090b576d491b1e51801bef35`, `camera-a-presentation.png` `668bda523029f3eab3eef02e8233e5357dcaa9861f151484bebf37267282c6a7`, `manifest.json` `848d3f2e2bb3966a4ac3fad3da09aa0062e4fdc85e53c386a8249b3d0f6dedfc`, and the copied before image `55a13ccf97b87c2bd2af99c99de0cec5de16a27a497644403dc9acfb2626ae2c`.
- The accepted final candidate includes the accepted roof shingle surface and the accepted glossy glass from correction-01; the final evidence set shows both. The first-pass and correction-01 evidence remain history.
- Publication route: same healthy Worker session `01`, exchange `05`, profile `Implementation Worker`, `Native planning mode: not-used`, Phase Publication. Prompt `01_publication_04.md`; report `01_report_04.md`.
- Publication scope: update the README final evidence sentence, stage only the exact accepted paths, one ordinary local commit, one ordinary non-force push to `origin/main`, verify the public ref. No checkpoint, no LFS, no history rewrite, no unrelated files.
- Publication grant: `01_publication_04.md`, written directly by the ORCHESTRATOR. SHA-256 `786558449d2af2cd5a2d9f28900c0daa434d89e84557153bd8dd2b9fcdc6c914`. Report: `01_report_04.md`.
- No publication or closure is claimed until the Worker report and the Orchestrator's independent public-ref verification.

## 2026-11-13 — Publication report received; public ref verified; closure prepared

- `01_report_04.md` received: 4,812 bytes, SHA-256 `3ce282faa76a359d88edd90bc36a50ae97c9a33d81c1456c47698525a5e5272a`; standard header; coordinates `01` / `05`; `status: PASS`; `Phase-qualified result: publication-PASS`; start commit `918d3db`; end commit `b70f242169b8173d0af5b660dcf1c9f00181449a`; `Logical-whole closure: not-closed`.
- Independent Orchestrator verification:
  - Local `HEAD` and public `refs/heads/main` are both `b70f242169b8173d0af5b660dcf1c9f00181449a` (`git ls-remote`).
  - Parent `918d3db6b421048c85b25a7712bd40da6afb0660`; tree `5a66a19b06d2ae7cdca190314ca524dbca42f715`; subject `add exterior material detail and final v004`.
  - GitHub API for the exact commit returned the same SHA, parent, tree and 21 changed files; the public tree equals the local tree, so the public content is the exact accepted tree.
  - The published `Jelena/Jelena_Realistic_v004.blend` blob hashes to `00d1dbe65c15a7e86ae52480b4e8aa3cad5744cac9443a10e5a5b230ea9c76aa`; correction-02 before/after/detail/presentation/manifest hashes match the accepted values; first-pass and correction-01 evidence hashes match their reports.
  - No `.local/checkpoints/` path, temporary render, AP/Meta file or unrelated path is in the commit. No LFS, no `.gitattributes`, no force, no amend/rebase/reset, no history rewrite. The push was a fast-forward from `918d3db`.
  - README final state: v004 current, Quick Start v004, accepted exterior visual at `evidence/exterior-004-correction-02/camera-a-after.png`, prior vegetation and exterior history preserved.
  - Worktree after publication: clean except the three intentionally untracked local checkpoints; no uncommitted tracked changes.
- Publication is **publication-PASS**. Michal's prior **PASS** is the acceptance record. No open residual; tree defects remain deferred. Closure artifact prepared in `00_closure.md`; run map remains Master-owned and absent.
- Recommended next bounded opportunity (not started): foreground terrace furniture and entrance-path craft detail; sky/atmosphere may be an alternative. Tree defects remain deferred.
