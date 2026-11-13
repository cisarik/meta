# Implementation Correction 01/05 — Jelena paved access and gravel parking

Delivery marker: **TEN ISTÝ CHAT**
Actual client mode: **Cursor Agent mode; native Plan mode OFF** (`not-used`)
Persistent role identity: WORKER
Worker session profile: Implementation Worker (renewed after second BLOCKED preflight)
Phase: Implementation
Task identity: `JELENA-ACCESS-PATH-GRAVEL-PARKING-IMPLEMENTATION-CORRECTION-02`
Delivery route: manual Cooperator delivery
Reasoning recommendation: **High** — the same scene-building and preservation risks remain, plus the expanded three-object reversible hide; Medium cannot safely resolve the interacting constraints.
Recommended context capacity: approximately 250k tokens — a recommendation, not observed telemetry or a token cap.
Requested model: Michal's current Cursor model selection; routing is Cooperator-owned, and effective model identity and reasoning enforcement are unverified.

Continuity anchor: the two BLOCKED reports `01_report_02.md` and `01_report_03.md`, the accepted plan `01_report_01.md`, and the prior grants `01_implementation_02.md` and `01_correction_03.md`, all from this same session.
Authority renewal: prior implementation authority expired at the terminal `01_report_03.md`; this exchange grants complete renewed implementation authority with the Cooperator-authorized three-object hide.
Why current-session reuse: the healthy same session holds the exact path-A vertex measurements, the accepted plan and the prior grants; independence is not required for this reversible visualization.
Retained context: convenience, not authority. Re-gate the repository and live scene from current evidence. Stop on conflict between retained context and current evidence.
Evidence posture: non-independent implementation evidence.

```text
Logical whole identity: jelena-access-path-and-gravel-parking
Worker session ordinal: 01
Worker exchange ordinal: 05
Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Exact baseline: commit b70f242169b8173d0af5b660dcf1c9f00181449a; Jelena/Jelena_Realistic_v004.blend SHA-256 00d1dbe65c15a7e86ae52480b4e8aa3cad5744cac9443a10e5a5b230ea9c76aa
Changed-path allowlist: Jelena/Jelena_Realistic_v005.blend; scripts/access_landscape_v005.py; evidence/access-005/camera-a-before.png; evidence/access-005/camera-a-after.png; evidence/access-005/overview.png; evidence/access-005/camera-a-detail.png; evidence/access-005/camera-a-terrace-detail.png; evidence/access-005/manifest.json; README.md; .local/checkpoints/Jelena_Realistic_v004-before-access.blend (untracked checkpoint, never staged)
Implementation boundaries: one coherent access landscape in scene A only; preserve the accepted cabin, terrace, furniture, steps, Camera A, lighting, scene B and all protected baselines; exactly three reversible vegetation hides are authorized below; no other tree, shrub or plant moves or removals; no whole-scene vegetation regeneration; no external assets
Independence required: no
```

## Why this second correction exists

`01_report_02.md` found `Smrek • stredný.021` blocking path A. `01_report_03.md` then tested the path with that tree excluded and found two further blockers:

- `Smrek • vysoký.015`, location `(12.6358, -1.9822, -0.2148)`, scale `0.72`: 6,956 vertices in the path-A z band, 4,129 inside the `0.90 m` footprint, minimum signed edge distance `-0.4500 m`.
- `Ker.003`, location `(13.2, -1.0, -0.237)`: 4 vertices inside, minimum signed edge distance `-0.1687 m`.

The single-hide grant was correctly stopped. The Cooperator has now explicitly authorized hiding **all three** objects on 2026-11-13. This grant is the complete renewed implementation authority for that decision.

## The authorized correction

Move these three objects into one new scene-A collection:

```text
05c • Vegetácia • odstránená pre prístup
```

- `Smrek • stredný.021`
- `Smrek • vysoký.015`
- `Ker.003`

Set the collection excluded in scene A’s view layer. The objects, meshes, transforms and materials must remain unchanged; only collection membership and view-layer exclusion may change. Do not delete, apply modifiers destructively, or edit meshes. Record each object’s original collection and transform in the terminal report. All three remain restorable.

This correction authorizes hiding **only** these three objects. Do not hide, move or remove any other tree, shrub or plant. If the renewed path-A clearance check finds another blocking object, stop and report `BLOCKED` with the exact object, vertices and clearance; do not hide a fourth object without a new Cooperator decision.

After hiding the three, re-run the full path-A clearance check against all remaining scene-A geometry in the same z band and expanded bounding box. The path may proceed only if no remaining vertex lies inside the paver footprint and the minimum horizontal distance from the paver edge to any remaining vertex is at least `0.10 m`. The same `0.70 m` trunk-to-edge checks remain for the road, parking and path B.

The final candidate will show a wider gap on the east side where the three objects were. That is a known visual risk. Do not restore them automatically; report the candidate and let the Cooperator judge. If the gap is unacceptable, the objects can be restored and path A shortened or redesigned in a later bounded decision.

## Renewed implementation scope

The full implementation scope, accepted layout, five original corrections, exact paths, render recipe, evidence set, preservation checks, budget, Git authority and report contract from `01_implementation_02.md` and `01_correction_03.md` are renewed unchanged, except for the three-object hide and the new collection name above.

The accepted plan remains `01_report_01.md`. The mandatory layout and settings remain:

- Candidate `Jelena/Jelena_Realistic_v005.blend`; checkpoint `.local/checkpoints/Jelena_Realistic_v004-before-access.blend`; script `scripts/access_landscape_v005.py`; evidence `evidence/access-005/`.
- Road centerline `(-6.3,-10.0)`, `(-3.0,-13.1)`, `(1.0,-13.3)`, `(15.0,-13.3)`, `(17.0,-10.5)`; width `3.0 m`; tips taper to `1.0 m`.
- Parking gravel x `5.60..10.60`, y `-11.80..-9.20`; tapers x `3.20..5.60` and `10.60..13.00`; proxy car `(8.30,-10.65)`, yaw `0`, `4.50 × 1.80 × 1.50 m`; north strip `0.55 m`, south `0.25 m`; wheel strips `1.50 m` centres.
- Path B width `1.20 m`, control points `(6.20,-2.63)`, `(6.20,-5.70)`, `(6.75,-6.60)`, `(6.40,-8.20)`, `(5.40,-9.20)`; rock clearance `>=0.35 m`; last `0.60 m` eases to `12 mm`.
- Path A width `0.90 m`, replaces the entire run A in place, shifted `0.15 m` southeast at `.006`–`.009`, ends at the last stone; three-object hide per this grant.
- Pavers `0.198 × 0.098 × 0.060 m`, running bond `0.200 × 0.100 m`, about `670` instances; trim/border the curved edges; no gaps or overlaps.
- `Lôžko • chodník` flush edge, `Obruba • betón`; materials `Dlažba • betón`, `Obruba • betón`, `Štrk • prístup`; procedural only.
- Collections `11 • Prístup • A`, `11a • Pomocné • A`, `05b • Nášľap • ponechané`, `05c • Vegetácia • odstránená pre prístup`, `10a • Vegetácia • mimo prístup`, `07d • Kamera prístup • A`.
- Camera D `D • Prístup zhora`, `(7.0,-23.5,15.5)`, lens `28 mm`, aim `(6.5,-8.0,-0.4)`; at most `2 m` / `5 mm` framing adjustment. Camera A never moves.
- Grass mask `Maska prístupu` expanded `0.12 m`; modify `Pokryv lesa` only; no vegetation generator rerun.
- Matched before/after `840 × 560`, 32 samples, adaptive, OIDN, seed 0, AgX, look None, exposure 0, gamma 1, sRGB, PNG RGB 8-bit. Overview `840 × 560`. Side detail `1260 × 840` border `(0.64,0.995,0.00,0.28)`. Terrace detail `1260 × 840` border `(0.28,0.72,0.00,0.38)`. Restore saved `1260 × 840 / 80 / denoise off / RGBA` before final save.
- Budget: first pass at most six stills including the optional 16-sample overview test; one correction at most two more; hard cap eight; `15` minutes cumulative; stop/simplify at `4.5 GiB` sampled RSS, never past `6.0 GiB`.
- Manifest must include SHA-256 for each image, candidate, checkpoint and script, all settings, actual borders/dimensions, scene-B count, Camera A, `Kameň` users, remaining tree transforms, proxy exclusion, visual review, limitations and sampled RSS in KiB (not peak).
- README: one minimal line under `## Súbory` naming `v005` as the access candidate and `v004` as the accepted exterior until acceptance.

## Authority, mutation axes and trace

Positive authority: read-only inspection of the repository, AP and Meta evidence, the live scene; exact local filesystem writes in the changed-path allowlist; scene-A mutation exactly as specified; checkpoint copy, Save As `v005`, script execution, renders, evidence writes, manifest and the minimal README edit; one commit and one ordinary non-force push; direct write of the terminal report.

Negative authority: no writes outside the changed-path allowlist; no scene-B edits; no shared collection `04`, `06`, `07`, `07b` edits; no `Kameň` edit; no cabin, terrace, furniture, steps, Camera A, light, world or colour-management changes; no vegetation change except the three authorized hides; no whole-scene vegetation regeneration; no external assets, paid services, network except the authorized Git push/readback, uploads, credentials, accounts or host configuration; no addon update, reinstall, second Blender instance, background Blender or process termination; no Meta Git operation; no acceptance, publication PASS or closure; no subagents or parallel work.

Commands: read-only shell, `cp`, `shasum`, the exact script, Blender MCP calls, `git add` with explicit paths, `git commit`, `git push origin HEAD`, `git ls-remote origin refs/heads/main`, `git status`, `shasum`, `stat`, `rg`, `cat`. Fish-compatible presentation for owner steps.

Repository mutation: `Jelena/Jelena_Realistic_v005.blend`; `scripts/access_landscape_v005.py`; `evidence/access-005/camera-a-before.png`; `evidence/access-005/camera-a-after.png`; `evidence/access-005/overview.png`; `evidence/access-005/camera-a-detail.png`; `evidence/access-005/camera-a-terrace-detail.png`; `evidence/access-005/manifest.json`; `README.md`; `.local/checkpoints/Jelena_Realistic_v004-before-access.blend` (untracked, never staged)
Host/remote mutation: ordinary non-force push to `origin` `refs/heads/main` at `https://github.com/cisarik/jelena`; no other host/remote effect
Trace persistence: direct-write `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking/01_report_04.md`

Cooperator delivery / trace destination: configured
Downloadable prompt filename: `01_correction_04.md`
Destination path: `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking`
Report filename: `01_report_04.md`
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR (Meta Git); project Git push is separately authorized below
Archival: wait-for-report

External trace disposition: configured
Trace discovery: `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking`
Trace project key: `jelena`
Trace logical-whole projection identity: `jelena-access-path-and-gravel-parking`
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

## Preflight and sequence

The prior attempts left no candidate, checkpoint, script, evidence or commit. Start from the clean live `v004` and re-verify:

1. Repository identity, branch `main`, HEAD `b70f242169b8173d0af5b660dcf1c9f00181449a`, AP pin `d7023cf037f6d17885c3ede5c04812c61640da50`, clean tracked worktree apart from the three known untracked checkpoints.
2. `v004` SHA-256 `00d1dbe65c15a7e86ae52480b4e8aa3cad5744cac9443a10e5a5b230ea9c76aa`; `v005`, checkpoint, script, evidence directory and `01_report_04.md` absent.
3. Live filepath exactly `Jelena_Realistic_v004.blend`, `is_dirty false`, scene `A • Chata pri lese`, camera `A • Chata pri lese`, frame 1, scene A 923 objects, scene B 308.
4. Create the checkpoint copy and hash both files; both must equal the baseline hash. Do not stage the checkpoint.
5. Write `scripts/access_landscape_v005.py` with the full build and the three-object hide. It must refuse unless the open filepath ends with `v005`, scene and camera are A, scene B has 308 objects, Camera A matches, and the new collections are absent.
6. Render the fresh before from `v004` with the matched recipe; restore saved settings; do not save `v004`.
7. Save As `Jelena/Jelena_Realistic_v005.blend`; verify the filepath.
8. Run the script through MCP. It must hide only the three authorized objects, re-measure path A against all remaining geometry, and assert all other clearances, scene-B preservation, `Kameň` users, Camera A and remaining-tree transforms.
9. Save `v005`; render after, overview, side detail and terrace detail. Inspect the actual images.
10. One bounded correction at most: mask margin, edge blend/border, material variation or detail framing. No layout, Camera A, vegetation or scope change. Re-render at most two stills.
11. Restore saved render settings; save `v005`; hash it.
12. Write the manifest and the one README line.
13. Re-hash `v004`, verify scene B, Camera A, `Kameň`, stones, remaining vegetation, collections, proxy exclusion and the three hidden objects’ preserved data.
14. Stage only the exact commit paths, one commit, one ordinary non-force push, verify the public ref.
15. Write `01_report_04.md`.

If any assertion fails, stop without saving a failed candidate. If the path-A re-check finds another blocker, stop and report it; do not hide a fourth object.

## Preservation and acceptance

Preserve all accepted cabin, terrace, furniture, steps, Camera A, lighting, world, colour management, scene B, protected baselines and all vegetation except the three authorized hides. The hidden objects must remain in the file with unchanged object/mesh data and transforms. The original 20 stones remain in `05b`, excluded. The new collections remain scene-A-only. `Kameň` remains 25 users and untouched. No whole-scene vegetation generator runs.

Journal the three hides as a scope deviation in the terminal report, including:

- objects `Smrek • stredný.021`, `Smrek • vysoký.015`, `Ker.003`;
- new collection `05c • Vegetácia • odstránená pre prístup`;
- each original collection and transform;
- why the path-A clearance failed for each;
- the reversible-hide decision and the 2026-11-13 Cooperator authorization;
- the visual risk of the wider east-side gap;
- confirmation that the object/mesh data was not deleted.

The owner’s subjective acceptance remains separate. The report must provide a short numbered acceptance request covering both paths, the overview, the parking approach, the terrace junction and the wider vegetation gap.

## Git, report and stop rules

Git authority, commit message, staging rules and non-force push are exactly those in `01_implementation_02.md`:

```text
Jelena/Jelena_Realistic_v005.blend
scripts/access_landscape_v005.py
evidence/access-005/camera-a-before.png
evidence/access-005/camera-a-after.png
evidence/access-005/overview.png
evidence/access-005/camera-a-detail.png
evidence/access-005/camera-a-terrace-detail.png
evidence/access-005/manifest.json
README.md
```

One commit with the same message; one ordinary non-force `git push origin HEAD`; verify `git ls-remote origin refs/heads/main`. Never stage `.local` checkpoints or the Meta report. No LFS, force push or history rewrite.

Report path: `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking/01_report_04.md`
Report coordinates: session `01`, exchange `05`.
The report must begin exactly `### Report for ORCHESTRATOR_CHAT`, use `Phase-qualified result: implementation-PASS | not-applicable`, `Logical-whole closure: not-closed`, `Report justification: new-mutation`, and include the standard core, three-hide deviation, image hashes, performance, Git result, critique, resolved issues and authority expiry.

Stop and report `BLOCKED`/`PARTIAL` for the same conditions as `01_implementation_02.md`, plus:

- the three-object hide would require deleting or editing a mesh;
- another object blocks path A after the three hides;
- the final images show the wider vegetation gap is visually catastrophic and cannot be judged as a candidate;
- any request to hide a fourth object, move Camera A, change the layout or expand the allowlist.

Do not claim acceptance, publication PASS or closure. Do not emit the project closure signal. Authority expires at the terminal report, cancellation or supersession.
