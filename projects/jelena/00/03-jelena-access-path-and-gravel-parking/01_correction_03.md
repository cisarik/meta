# Implementation Correction 01/04 — Jelena paved access and gravel parking

Delivery marker: **TEN ISTÝ CHAT**
Actual client mode: **Cursor Agent mode; native Plan mode OFF** (`not-used`)
Persistent role identity: WORKER
Worker session profile: Implementation Worker (renewed after BLOCKED preflight)
Phase: Implementation
Task identity: `JELENA-ACCESS-PATH-GRAVEL-PARKING-IMPLEMENTATION-CORRECTION`
Delivery route: manual Cooperator delivery
Reasoning recommendation: **High** — the same scene-building and preservation risks remain, plus one reversible tree-hide scope correction; Medium cannot safely resolve the interacting constraints.
Recommended context capacity: approximately 250k tokens — a recommendation, not observed telemetry or a token cap.
Requested model: Michal's current Cursor model selection; routing is Cooperator-owned, and effective model identity and reasoning enforcement are unverified.

Continuity anchor: the BLOCKED report `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking/01_report_02.md`, the accepted plan `01_report_01.md`, and the prior implementation grant `01_implementation_02.md`, all from this same session.
Authority renewal: prior implementation authority expired at the terminal BLOCKED report; this exchange grants a complete renewed implementation authority with exactly one scope correction.
Why current-session reuse: the healthy same session holds the exact path-A vertex measurement, the accepted plan and the prior grant; independence is not required for this reversible visualization.
Retained context: convenience, not authority. Re-gate the repository and live scene from current evidence. Stop on conflict between retained context and current evidence.
Evidence posture: non-independent implementation evidence.

```text
Logical whole identity: jelena-access-path-and-gravel-parking
Worker session ordinal: 01
Worker exchange ordinal: 04
Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Exact baseline: commit b70f242169b8173d0af5b660dcf1c9f00181449a; Jelena/Jelena_Realistic_v004.blend SHA-256 00d1dbe65c15a7e86ae52480b4e8aa3cad5744cac9443a10e5a5b230ea9c76aa
Changed-path allowlist: Jelena/Jelena_Realistic_v005.blend; scripts/access_landscape_v005.py; evidence/access-005/camera-a-before.png; evidence/access-005/camera-a-after.png; evidence/access-005/overview.png; evidence/access-005/camera-a-detail.png; evidence/access-005/camera-a-terrace-detail.png; evidence/access-005/manifest.json; README.md; .local/checkpoints/Jelena_Realistic_v004-before-access.blend (untracked checkpoint, never staged)
Implementation boundaries: one coherent access landscape in scene A only; preserve the accepted cabin, terrace, furniture, steps, Camera A, lighting, scene B and all protected baselines; exactly one reversible tree hide is authorized below; no other tree moves or removals; no whole-scene vegetation regeneration; no external assets
Independence required: no
```

## Why this correction exists

`01_report_02.md` is a correct `BLOCKED` result. The path-A preflight measured `Smrek • stredný.021` with numpy/`foreach_get`: 27,051 vertices in the relevant z band, 10,024 inside the `0.90 m` paver footprint, minimum centreline distance `0.0001 m`, minimum signed edge distance `-0.4499 m`. The `0.15 m` shift does not clear the tree. No scene edit, checkpoint, Save As, render, script, evidence, commit or push occurred. The live file remains clean `v004`.

The Cooperator’s 2026-11-13 response accepts a pragmatic resolution and explicitly raises removing the blocking tree. This grant chooses the reversible version of that decision: **hide the single blocking tree, do not delete it**. This is a material scope change, recorded and reversible.

## The one authorized correction

Move `Smrek • stredný.021` from its current collection into a new scene-A collection:

```text
05c • Strom • odstránený pre prístup
```

Set that collection excluded in scene A’s view layer. The tree object, mesh, transform and materials must remain unchanged; only its collection membership and view-layer exclusion may change. Do not delete, apply modifiers destructively, or edit the mesh. Record the original collection and matrix in the terminal report. The tree remains restorable.

This correction authorizes hiding **only** `Smrek • stredný.021`. Do not hide, move or remove any other tree. If the path-A re-check finds another blocking tree or object, stop and report `BLOCKED` with the exact object, vertices and clearance; do not hide a second tree without a new decision.

After hiding the tree, re-run the full path-A clearance check against all remaining scene-A geometry in the same z band and expanded bounding box. The path may proceed only if no remaining vertex lies inside the paver footprint and the minimum horizontal distance from the paver edge to any remaining vertex is at least `0.10 m`. The same `0.70 m` trunk-to-edge checks remain for the road, parking and path B.

The final candidate will show a gap where the tree was. That is a known visual risk. Do not restore the tree automatically; report the candidate and let the Cooperator judge. If the gap is unacceptable, the tree can be restored and path A shortened in a later bounded decision.

## Authority, mutation axes and trace

Positive authority: read-only inspection of the repository, AP and Meta evidence, the live scene; exact local filesystem writes in the changed-path allowlist; scene-A mutation exactly as specified; checkpoint copy, Save As `v005`, script execution, renders, evidence writes, manifest and the minimal README edit; one commit and one ordinary non-force push; direct write of the terminal report.

Negative authority: no writes outside the changed-path allowlist; no scene-B edits; no shared collection `04`, `06`, `07`, `07b` edits; no `Kameň` edit; no cabin, terrace, furniture, steps, Camera A, light, world or colour-management changes; no tree change except the one authorized hide; no whole-scene vegetation regeneration; no external assets, paid services, network except the authorized Git push/readback, uploads, credentials, accounts or host configuration; no addon update, reinstall, second Blender instance, background Blender or process termination; no Meta Git operation; no acceptance, publication PASS or closure; no subagents or parallel work.

Commands: read-only shell, `cp`, `shasum`, the exact script, Blender MCP calls, `git add` with explicit paths, `git commit`, `git push origin HEAD`, `git ls-remote origin refs/heads/main`, `git status`, `shasum`, `stat`, `rg`, `cat`. Fish-compatible presentation for owner steps.

Repository mutation: `Jelena/Jelena_Realistic_v005.blend`; `scripts/access_landscape_v005.py`; `evidence/access-005/camera-a-before.png`; `evidence/access-005/camera-a-after.png`; `evidence/access-005/overview.png`; `evidence/access-005/camera-a-detail.png`; `evidence/access-005/camera-a-terrace-detail.png`; `evidence/access-005/manifest.json`; `README.md`; `.local/checkpoints/Jelena_Realistic_v004-before-access.blend` (untracked, never staged)
Host/remote mutation: ordinary non-force push to `origin` `refs/heads/main` at `https://github.com/cisarik/jelena`; no other host/remote effect
Trace persistence: direct-write `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking/01_report_03.md`

Cooperator delivery / trace destination: configured
Downloadable prompt filename: `01_correction_03.md`
Destination path: `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking`
Report filename: `01_report_03.md`
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

## Renewed implementation scope

The full implementation scope, accepted layout, five corrections, exact paths, render recipe, evidence set, preservation checks, budget, Git authority and report contract from `01_implementation_02.md` are renewed unchanged, except for the tree-hide correction above and the new report coordinates.

The accepted plan remains `01_report_01.md`. The mandatory layout and settings remain:

- Candidate `Jelena/Jelena_Realistic_v005.blend`; checkpoint `.local/checkpoints/Jelena_Realistic_v004-before-access.blend`; script `scripts/access_landscape_v005.py`; evidence `evidence/access-005/`.
- Road centerline `(-6.3,-10.0)`, `(-3.0,-13.1)`, `(1.0,-13.3)`, `(15.0,-13.3)`, `(17.0,-10.5)`; width `3.0 m`; tips taper to `1.0 m`.
- Parking gravel x `5.60..10.60`, y `-11.80..-9.20`; tapers x `3.20..5.60` and `10.60..13.00`; proxy car `(8.30,-10.65)`, yaw `0`, `4.50 × 1.80 × 1.50 m`; north strip `0.55 m`, south `0.25 m`; wheel strips `1.50 m` centres.
- Path B width `1.20 m`, control points `(6.20,-2.63)`, `(6.20,-5.70)`, `(6.75,-6.60)`, `(6.40,-8.20)`, `(5.40,-9.20)`; rock clearance `>=0.35 m`; last `0.60 m` eases to `12 mm`.
- Path A width `0.90 m`, replaces the entire run A in place, shifted `0.15 m` southeast at `.006`–`.009`, ends at the last stone; tree hide per this grant.
- Pavers `0.198 × 0.098 × 0.060 m`, running bond `0.200 × 0.100 m`, about `670` instances; trim/border the curved edges; no gaps or overlaps.
- `Lôžko • chodník` flush edge, `Obruba • betón`; materials `Dlažba • betón`, `Obruba • betón`, `Štrk • prístup`; procedural only.
- Collections `11 • Prístup • A`, `11a • Pomocné • A`, `05b • Nášľap • ponechané`, `05c • Strom • odstránený pre prístup`, `10a • Vegetácia • mimo prístup`, `07d • Kamera prístup • A`.
- Camera D `D • Prístup zhora`, `(7.0,-23.5,15.5)`, lens `28 mm`, aim `(6.5,-8.0,-0.4)`; at most `2 m` / `5 mm` framing adjustment. Camera A never moves.
- Grass mask `Maska prístupu` expanded `0.12 m`; modify `Pokryv lesa` only; no vegetation generator rerun.
- Matched before/after `840 × 560`, 32 samples, adaptive, OIDN, seed 0, AgX, look None, exposure 0, gamma 1, sRGB, PNG RGB 8-bit. Overview `840 × 560`. Side detail `1260 × 840` border `(0.64,0.995,0.00,0.28)`. Terrace detail `1260 × 840` border `(0.28,0.72,0.00,0.38)`. Restore saved `1260 × 840 / 80 / denoise off / RGBA` before final save.
- Budget: first pass at most six stills including the optional 16-sample overview test; one correction at most two more; hard cap eight; `15` minutes cumulative; stop/simplify at `4.5 GiB` sampled RSS, never past `6.0 GiB`.
- Manifest must include SHA-256 for each image, candidate, checkpoint and script, all settings, actual borders/dimensions, scene-B count, Camera A, `Kameň` users, tree transforms, proxy exclusion, visual review, limitations and sampled RSS in KiB (not peak).
- README: one minimal line under `## Súbory` naming `v005` as the access candidate and `v004` as the accepted exterior until acceptance.

## Preflight and sequence

The prior attempt left no candidate, checkpoint, script, evidence or commit. Start from the clean live `v004` and re-verify:

1. Repository identity, branch `main`, HEAD `b70f242169b8173d0af5b660dcf1c9f00181449a`, AP pin `d7023cf037f6d17885c3ede5c04812c61640da50`, clean tracked worktree apart from the three known untracked checkpoints.
2. `v004` SHA-256 `00d1dbe65c15a7e86ae52480b4e8aa3cad5744cac9443a10e5a5b230ea9c76aa`; `v005`, checkpoint, script, evidence directory and `01_report_03.md` absent.
3. Live filepath exactly `Jelena_Realistic_v004.blend`, `is_dirty false`, scene `A • Chata pri lese`, camera `A • Chata pri lese`, frame 1, scene A 923 objects, scene B 308.
4. Create the checkpoint copy and hash both files; both must equal the baseline hash. Do not stage the checkpoint.
5. Write `scripts/access_landscape_v005.py` with the full build and the tree-hide correction. It must refuse unless the open filepath ends with `v005`, scene and camera are A, scene B has 308 objects, Camera A matches, and the new collections are absent.
6. Render the fresh before from `v004` with the matched recipe; restore saved settings; do not save `v004`.
7. Save As `Jelena/Jelena_Realistic_v005.blend`; verify the filepath.
8. Run the script through MCP. It must hide only `Smrek • stredný.021`, re-measure path A against all remaining geometry, and assert all other clearances, scene-B preservation, `Kameň` users, Camera A and tree transforms.
9. Save `v005`; render after, overview, side detail and terrace detail. Inspect the actual images.
10. One bounded correction at most: mask margin, edge blend/border, material variation or detail framing. No layout, Camera A, tree or scope change. Re-render at most two stills.
11. Restore saved render settings; save `v005`; hash it.
12. Write the manifest and the one README line.
13. Re-hash `v004`, verify scene B, Camera A, `Kameň`, stones, remaining trees, collections, proxy exclusion and the hidden tree’s preserved data.
14. Stage only the exact commit paths, one commit, one ordinary non-force push, verify the public ref.
15. Write `01_report_03.md`.

If any assertion fails, stop without saving a failed candidate. If the path-A re-check finds another blocker, stop and report it; do not hide a second tree.

## Preservation and acceptance

Preserve all accepted cabin, terrace, furniture, steps, Camera A, lighting, world, colour management, scene B, protected baselines and all trees except the single authorized hide. The hidden tree must remain in the file with unchanged object/mesh data and transform. The original 20 stones remain in `05b`, excluded. The new collections remain scene-A-only. `Kameň` remains 25 users and untouched. No whole-scene vegetation generator runs.

Journal the tree hide as a scope deviation in the terminal report, including:

- object `Smrek • stredný.021`;
- new collection `05c • Strom • odstránený pre prístup`;
- original collection and transform;
- why the path-A clearance failed;
- the reversible-hide decision and the 2026-11-13 Cooperator direction;
- the visual risk of the resulting gap;
- confirmation that the tree data was not deleted.

The owner’s subjective acceptance remains separate. The report must provide a short numbered acceptance request covering both paths, the overview, the parking approach, the terrace junction and the tree-gap trade-off.

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

Report path: `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking/01_report_03.md`
Report coordinates: session `01`, exchange `04`.
The report must begin exactly `### Report for ORCHESTRATOR_CHAT`, use `Phase-qualified result: implementation-PASS | not-applicable`, `Logical-whole closure: not-closed`, `Report justification: new-mutation`, and include the standard core, tree-hide deviation, image hashes, performance, Git result, critique, resolved issues and authority expiry.

Stop and report `BLOCKED`/`PARTIAL` for the same conditions as `01_implementation_02.md`, plus:

- the tree-hide correction would require deleting or editing the tree mesh;
- another tree or object blocks path A after the authorized hide;
- the final images show the tree gap is visually catastrophic and cannot be judged as a candidate;
- any request to hide a second tree, move Camera A, change the layout or expand the allowlist.

Do not claim acceptance, publication PASS or closure. Do not emit the project closure signal. Authority expires at the terminal report, cancellation or supersession.
