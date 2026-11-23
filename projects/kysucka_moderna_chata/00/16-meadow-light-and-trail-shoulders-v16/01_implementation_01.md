# V16 implementation — golden meadow accents, readable forest shadows, and irregular gravel-trail shoulders

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-meadow-light-and-trail-shoulders-v16
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker (same-session continuation of Planner 01/01)
Phase: implementation
Task identity: MEADOW-LIGHT-TRAIL-V16-IMPL — build, validate, and render one bounded V16 candidate from V15 C
Delivery route: manual Cooperator delivery
Continuity anchor: terminal planning report `01_report_00.md` (SHA-256 `e4c962ea5984d9e54cb5c568475f9b3344231578b12c32d871ced9da6627c341`) for MEADOW-LIGHT-TRAIL-V16-PLAN, exchange 01/01, accepted by this whole's ORCHESTRATOR on 2026-11-19 (record in `00_notes.md`)
Authority renewal: prior planning authority expired at that terminal report; this prompt grants complete new bounded implementation authority. Retained context is convenience, not authority. Re-gate repository, input hashes, and process state yourself; stop on any conflict between retained context and current evidence.
Evidence posture: non-independent
Implementation authority: explicit
Independence required: no
Reasoning recommendation: High — named risks: coordinated shader/attribute/mask construction across three terrain meshes, closed trail mesh, 48 linked meadow masters, and up to 6,000 support-verified shoulder tufts inside a 433.6 MiB packed scene under strict isolated CPU4 resource guards
Recommended context capacity: approximately 250k tokens

## Binding specification and goal

Your accepted plan `01_report_00.md` (SHA-256
`e4c962ea5984d9e54cb5c568475f9b3344231578b12c32d871ced9da6627c341`) is the
binding technical specification; implement its §§2–5 within the exact
authority boundaries below. Where this prompt specifies a boundary, this prompt
governs.

Deliver one editable V16 candidate
`work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend` and one
matched native Cycles CPU4 `960 × 540` render
`work/v16/meadow_trail_01/renders/B_v16_960.png` starting from immutable V15 C
(`work/v15/reference_01/checkpoints/candidate_exterior_v15_tonal.blend`), with
complete staged preservation, fresh-input source replay, cold reopen, actual
basal support and hull clearance proofs, `_working_branch` verification, and
fixed-crop comparison metrics against V15 C, V15 B, and reference `01.png`.
After producing `B_v16_960.png` and its proofs, write your terminal report and
stop so the Orchestrator and Michal can inspect the actual rendered pixels
before any optional `c01` visual correction or 4K render is considered.

## Repository gate and exact immutable baseline

Working directory: `R = /home/agile/Projects/kysucka_moderna_chata`
Trace directory: `T = /home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16`

Project repository gate:
- Local backup origin: `/home/agile/backups/git/kysucka_moderna_chata.git`
- Canonical GitHub URL: `https://github.com/cisarik/kysucka_moderna_chata.git`
- Branch `main`, expected HEAD `78534bd46020bb2bfc97eef69b05e583cba5a5e5`,
  clean tracked working tree and empty index (`git status --porcelain=v1`
  empty).
- Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `.ap`
  (gitlink = submodule HEAD, clean detached HEAD).

Re-verify these immutable input hashes before and after execution:

| Input | SHA-256 |
|---|---|
| `work/v15/reference_01/checkpoints/candidate_exterior_v15_tonal.blend` (sole scene input) | `15870b192662714a40ae7772a120e554acd9c3317e6ebfa1be54d4ac907d5bf2` |
| `work/v15/reference_01/renders/C_tonal960.png` (matched C control) | `3110941602665c563dfbe9bfe4ce9f118fb4d11dcb2fbc14ffeff15b3b8704d2` |
| `work/v15/reference_01/renders/B_reference960.png` (matched B reference) | `1315bb7a50528ca7d77b41527dbf080e3a30bb93805569f351e9ae09751c9cb5` |
| `work/v14/native_02/renders/B_final960.png` (matched A reference) | `334bc640d65490dfee64cfe7768daaf85d2bcdbf64f70264420537cadeb72c05` |
| `/home/agile/Projects/chata/chatgpt/01.png` (target look reference) | `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d` |
| `work/v12/profile_03/isolated_config/userpref.blend` (MCP-disabled prefs) | `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561` |

Mandatory reading: governing WORKER spine (`.ap/AP.md` Semantic Authority +
WORKER row, RF-03/RF-06/RF-12/RF-18, §8, §18); `.ap/AP_WORKER.md` Worker
Session Target + Reporting; `.ap/PROMPT_CONTRACTS.md` Worker Report Header,
Implementation Authority Record, Mutation Axes, Delivery Record; project
`AGENTS.md`; `/home/agile/meta/README.md`; your accepted plan `T/01_report_00.md`;
and `T/00_notes.md`.

## Execution route and resource/process guards

Canonical execution route: **isolated native Blender 5.3.0 CLI route**
(`/home/agile/Applications/Blender/blender --background --disable-autoexec --threads 4`),
explicitly activated for this isolated exterior task because Michal owns the
live Blender GUI (`PID 2452`, `start_ticks 12233`) and live MCP is prohibited.

- Run at most **one** owned background Blender child at a time, serialized in
  order: (1) build & save, (2) fresh-input replay without saving, (3) cold
  reopen & native 960×540 render.
- Launch with `nice -n 10` (plus the V14/V15 owned-thread priority keeper
  restoring `+10` if the scheduler adjusts to `+9`), `PYTHONDONTWRITEBYTECODE=1`,
  and process-local `BLENDER_USER_CONFIG`, `TMPDIR`, `TMP`, `TEMP` under
  `R/work/v16/meadow_trail_01/runtime/` using a copy of the MCP-disabled
  `work/v12/profile_03/isolated_config/userpref.blend` (save/remember/autosave
  disabled, zero owned TCP listeners).
- Before every child launch, verify: no foreign background Blender exists,
  owner GUI `PID 2452` (`start_ticks 12233`) is untouched, and system available
  RAM is **≥12 GiB**.
- Sample resources every ~1 s during execution: stop only your own child if own
  RSS exceeds **8 GiB** (early-stop guard at **7 GiB**), if system available
  RAM falls below **6 GiB** on two consecutive samples, or if a foreign
  background job starts and causes contention; apply the **240 s** whole-child
  watchdog on the cold/render job (native render target **<157.5 s**).
- Verify before and after every child that global Blender user preference,
  startup, and recovery file stat/SHA witnesses and owner GUI PID 2452 are
  unchanged.

## Authority and mutation axes

Positive authority / exact changed-path allowlist:
- New `R/work/v16/meadow_trail_01/source/meadow_trail_v16.py`
- New `R/work/v16/meadow_trail_01/source/meadow_trail_v16.json`
- New `R/work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend`
- New `R/work/v16/meadow_trail_01/renders/B_v16_960.png`
- New `R/work/v16/meadow_trail_01/worker/**` (isolated build, replay,
  cold/render, support, and crop-metric drivers/supervisors)
- New `R/work/v16/meadow_trail_01/proofs/**` (preservation, replay, support,
  portability, working-branch, resource, and crop-comparison JSON receipts)
- New `R/work/v16/meadow_trail_01/runtime/**` (isolated config/temp runtime
  files)
- Direct-write terminal report `T/01_report_01.md` (if your client permits the
  exact write; otherwise return the complete report in session output for the
  named ORCHESTRATOR exact-content relay).

Negative authority:
- No edits to any tracked repository file, `model/`, `scripts/`, `assets/`,
  `docs/`, `AGENTS.md`, `README*`, or any prior `work/v05`–`work/v15` file.
- Do not create `c01` correction files or UHD/4K renders in this exchange (stop
  after `B_v16_960.png` for Orchestrator/Cooperator visual inspection; one
  causal driver/harness retry is permitted only if a script fails before
  completing the candidate/render, with raw failure evidence preserved).
- No live MCP calls (`tools.blender.*` prohibited), no GUI window launch, no
  network access or asset downloads, no package/runtime installation, no Git
  writes in any repository, no image retouch/compositing/backplate/AI repair,
  and never emit the literal project closure signal.

Repository mutation: only new `R/work/v16/meadow_trail_01/**` paths listed above
Host/remote mutation: only owned isolated headless Blender child processes using `R/work/v16/meadow_trail_01/runtime/**`; zero persistent host or remote mutation
Trace persistence: direct-write `/home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16/01_report_01.md`

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 16-meadow-light-and-trail-shoulders-v16
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_implementation_01.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16
Report filename: 01_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

## Binding technical parameters (from accepted plan §3)

1. **Recipe & ownership (`apply_v16(scene, config, ROOT) -> dict`, seed `13716`):**
   - Import-safe module; idempotent on repeated application with identical
     config hash.
   - Copy active terrain meshes (`V13_V11_TERRAIN_NEAR_MESH`,
     `V13_V11_TERRAIN_FAR_MESH`, `V13_V11_TERRAIN_EXTENSION_MESH`) and trail
     mesh (`V07_TRAIL_MESH`) into V16-owned derivatives preserving all original
     vertex coordinates, topology, UVs, normals, existing attributes
     (`v13_ecology`, `v13_exterior_weight`), face material indices, and
     transforms; add only V16 mask/coordinate attributes and rebind the owned
     V16 materials. Retain predecessor meshes/worlds with fake users where
     needed.
   - Create off-scene `V16_MASTER_MEADOW_RENDER` with 48 linked mesh objects
     and object-level overrides for 4 owned copies of
     `MAT_V09_MAT_V08_MAT_V06_{GREEN,OLIVE,THATCH,MEADOW_CARD}`. Clone the V13
     meadow GN group, rebind only its render-library reference to
     `V16_MASTER_MEADOW_RENDER`, and preserve its `IsViewport` TRUE arm
     (`V13_MASTER_MEADOW_WORK`, stride 8) and all 29,000 point placements.
2. **Golden accents and meadow texture:**
   - World XY noise lengths `18 m`, `3 m`, `0.28 m` (Detail `2`, Roughness
     `0.5`); warm-patch field `F = smoothstep(0.36, 0.68, 0.65*N18 + 0.35*N3)`;
     sun-facing factor `D = smoothstep(0.18, 0.62, dot(normalized_unbumped_normal, key_source_vector))`.
   - Terrain golden mix `0.38 * D * F` gated by `v13_exterior_weight`, golden
     linear RGB `[0.30, 0.255, 0.065]`; meadow golden mix
     `(0.08 + 0.22 * D) * F` on both diffuse and translucent branches, golden
     linear RGB `[0.38, 0.32, 0.075]`.
   - Shared 3 m brightness multiplier `0.86–1.14`; micro multiplier `0.88–1.14`
     (meadow) and `0.94–1.06` (terrain); meadow roughness `±0.04` clamped to
     `0.62–0.94`; exterior terrain micro-bump strength `0.15`, distance
     `0.008 m` chained with retained normal treatment; emission `0`, atlas
     alpha and 0.12 translucency mix preserved.
3. **Forest-shadow balance (`V16_WORLD_MEADOW_BALANCE`):**
   - Copy V15 C world (`V15_WORLD_REFERENCE_LIGHT`) to
     `V16_WORLD_MEADOW_BALANCE`; set fill strength to **`0.92`** and fill
     linear tint to **`[1.0, 0.94, 0.80, 1.0]`**. Retain fill saturation/cap/
     azimuth (`0.58` / `2.35` / `39.052734375°`), camera-cloud branch (`2.35`,
     `[1.0, 0.77, 0.49, 1.0]`), key light `V15_SUN_REFERENCE_KEY` (`2.8`,
     `[1.0, 0.88, 0.69]`, azimuth `285°`, elevation `17.6°`, diameter `2°`),
     forest materials, and interior lights unchanged.
4. **Irregular trail width and soft vegetated shoulders (`0.45–0.75 m` per side):**
   - Along the 1,105-station route (`L = 198.180813 m`), for each side
     `σ ∈ {0, 1}`: `h(s) = existing_width(s)/2`,
     `a(s) = smoothstep(1, 4, s) * (1 - smoothstep(L - 3, L, s))`, effective
     gravel edge `Eσ(s) = h(s) - a(s)*(0.02 + 0.04*Nedgeσ(s))` (wavelengths
     `2.7/8.5 m`, weights `0.65/0.35`), shoulder width
     `Wσ(s) = 0.45 + 0.30*Nwidthσ(s)` (wavelengths `4.5/13 m`, weights
     `0.70/0.30`), integer-lattice quintic 1D hash with salts
     `13716 + 100*side_index + 10*channel + octave`.
   - Store station, signed lateral coordinate, half-width, both edge values,
     both shoulder widths, and active/protection mask on derived terrain and
     trail meshes; compute `abs(lateral)` in the shader after interpolation.
   - Coordinated surface blend on gravel and terrain: `d = abs(lateral) - Eσ ≤ 0`
     retains gravel; `0–0.12 m` blends gravel into worn loam (`[0.115, 0.095, 0.040]`,
     roughness `0.96`); `0.12 m` to `Wσ` blends loam into local V16 substrate;
     bake matching 3 m route UVs onto the terrain halo; protect central
     travelled corridor `abs(lateral) ≤ h(s) - 0.08` (min width `0.96 m`) and
     apply `0.10 m` exclusion around the enclosed garden, paving,
     `V07_GATE_TRANSITION`, and gate geometry.
   - Add 8 source-derived low-tuft masters from complete connected components of
     V13 low forms (`0.06–0.14 m` height, ≤192 render triangles/master, ≤24
     working triangles/master, dedicated `IsViewport` switch with off-scene
     render/working collections and working stride 4 → ≤36,000 working
     triangles). Scatter on a jittered `0.20 m` lattice (`6 → 24 tufts/m²`
     across the shoulder, hard cap **6,000** by global deterministic rank).
   - Every full transformed tuft hull must clear the effective gravel edge by
     `≥0.02 m`, the travelled core, and all obstacle masks. Support roots on
     actual visible terrain/gravel triangles (max exposure `1 mm`, max burial
     `18 mm`, refine support spans `>5 mm`, scale refinements `0.75` then `0.5`
     before rejecting envelopes crossing an unresolved ~15 mm gravel-lip step).

## Validation and required evidence

Evidence tier: E2
Evidence tier basis: reversible isolated candidate build and native render in `work/v16/meadow_trail_01/` with exhaustive preservation, replay, cold, support, and portability checks
Combined implementation envelope: allowed
Authorized implementation stages: (1) pre-launch repository/hash/process/RAM gate; (2) isolated build & save of `candidate_exterior_v16.blend` + idempotence check + staged preservation, basal support, full-hull clearance, and `_working_branch` proofs; (3) isolated fresh-input replay from V15 C without saving, proving semantic fixed-point equality; (4) isolated cold reopen of `candidate_exterior_v16.blend`, 87-image portability check, and matched native CPU4/96 960×540 render `B_v16_960.png`; (5) full PNG decode, fixed-crop metrics against C, B, and `01.png`, direct visual inspection of `B_v16_960.png`, and terminal report persistence/readback
Implementation stage gates: every failed gate stops the sequence; at most one causal driver/harness retry in a distinct proof label if a script fails before completing candidate/render, preserving raw failure logs
Independent acceptance: not-required
Rollback or recovery checkpoint: immutable V15 C (`15870b19…`) and all prior `work/` directories remain untouched; any failed V16 output stays isolated in `work/v16/meadow_trail_01/`
Terminal implementation report point: one, after stage 5

Verify and record in `proofs/` and your report:
- Unchanged V15 C input hash, 87 packed image byte hashes/colorspaces/relative
  paths/resolved targets (including `//../../../v14/assets/qwantani_sunset_puresky_2k.hdr`),
  29,000 meadow points, 6,200 forest points, cottage/interior/garden/camera,
  and all six `_working_branch` checks (5 existing + 1 new shoulder library).
- Exhaustive basal support (`exposure ≤ 1 mm`, `burial ≤ 18 mm`) and full-hull
  clearance (`≥0.02 m` from effective gravel edge, zero core/paving/garden/gate/
  post/trunk intersections, shoulder-width bounds within `2 μm`) for all
  accepted shoulder tufts, with accepted/rejected counts.
- Exact semantic agreement across build, second-apply idempotence, fresh-input
  replay, and cold reopen.
- Native render time (`<157.5 s`), whole-child durations, peak RSS, min
  available system RAM, card-wide free VRAM, and unchanged owner GUI PID 2452 +
  global preference witnesses across all three children.
- Fixed crop metrics table (`Front meadow`, `Left / right slopes`,
  `Shaded left forest`, `Cottage shadow / adjacent lit grass`, `Sky`, and
  `Front / right / upper trail`) comparing V16 `B_v16_960.png` against V15 C,
  V15 B, and `01.png` against the §4 review thresholds, plus your honest visual
  assessment after directly viewing `B_v16_960.png`.

## Completion and report contract

- **Critical formatting requirement:** Line 1 of `T/01_report_01.md` must be
  **exactly** `### Report for ORCHESTRATOR_CHAT` with no leading blank line or
  markdown title above it.
- Echo the three coordinates
  (`kysucka-moderna-chata-meadow-light-and-trail-shoulders-v16`, `01`, `02`)
  once, followed by the compact core (`Status: PASS | PARTIAL | BLOCKED`,
  `Phase-qualified result: implementation-PASS | not-applicable`,
  `Start commit` / `End commit`, deliverables with byte sizes and SHA-256
  hashes, validation summary, crop metrics and visual observations, Git result =
  no writes, deviations/risks/limitations, one smallest next step,
  `Report justification: new-mutation`, authority-expiry statement, compact
  `Orchestration critique` `MEASURED` / `LEAD`,
  `Resolved Execution Issues / Near-Misses`, and
  `Pre-Existing Failure Classification`). `Logical-whole closure: not-closed`.
- Save `T/01_report_01.md`, read it back in full to verify line 1, coordinates,
  and SHA-256 (or return the complete report text in session output if client
  controls block the write), then send a short completion notice and stop.

Authority expiry: this terminal report, cancellation, or supersession ends the
grant; no autonomous continuation, correction, UHD render, publication, or
closure follows.
