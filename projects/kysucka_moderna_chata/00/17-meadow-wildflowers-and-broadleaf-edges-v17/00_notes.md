# Poznámky orchestrátorky — V17 · Lúčne kvety, listnaté stromy a živý okraj chodníka

Autor: ORCHESTRATOR tohto celku
Capability profile: Orchestrator
Orchestrator session scope: logical-whole
Development run identity: kysucka-moderna-chata-reference-visualization
Logical whole identity: kysucka-moderna-chata-meadow-wildflowers-and-broadleaf-edges-v17
Dátum otvorenia: 2026-11-19, Europe/Bratislava
Životný cyklus: prevádzkové poznámky tohto celku; historická evidencia, nie task authority; pri uzavretí zmraziť, prípadné čistenie a Git archiváciu v Meta vlastní COOPERATOR.

## 2026-11-19 — Continuation Bootstrap Stage 1 a revalidácia handoutu V17

Prevzala som celok **V17** (`kysucka-moderna-chata-meadow-wildflowers-and-broadleaf-edges-v17`) z provizórneho handoutu `/home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17/00_handout.md` (15 600 B, SHA-256 `0bb091c06c043fe32ca451294dc29f50d684011667ef7729340323868cfde33b`), ktorý sa otvorením celku zmrazuje.

### Priamo overený stav repozitárov, procesov a artefaktov

- **Projektový repozitár:** `/home/agile/Projects/kysucka_moderna_chata`, branch `main`, HEAD `78534bd46020bb2bfc97eef69b05e583cba5a5e5`, lokálny backup origin `/home/agile/backups/git/kysucka_moderna_chata.git`. Sledovaný working tree a index sú čisté; nesledovaný súbor `?? reference/01.png` (3 251 765 B, SHA-256 `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d`) je Michalom pridaná lokálna kópia referencie klasifikovaná podľa RF-12 ako `unrelated-owner-work` (zachovať bez dotknutia).
- **AP submodule:** `.ap` gitlink aj čistý checkout `d7023cf037f6d17885c3ede5c04812c61640da50` (`./.ap/ap doctor` → `PASS`, variant `stable`). V `AGENTS.md` nie je deklarovaný žiadny AP upgrade ledger.
- **Meta repozitár:** `/home/agile/meta`, branch `main`, HEAD `abfb0ea0226dab1db554abcd47b4cc0a3fc289c1`, nesledované lokálne celky `00/15-reference-light-v15/`, `00/16-meadow-light-and-trail-shoulders-v16/` a `00/17-meadow-wildflowers-and-broadleaf-edges-v17/`.
- **Hardvér a procesy:** CachyOS Linux, 31 GiB RAM (~19 GiB dostupných), NVIDIA GeForce RTX 3080 (10 240 MiB celkom, ~7 130 MiB voľných). Žiadny natívny render ani Worker proces nebeží; všetky granty V16 expirovali. Jediný bežiaci Blender 5.3.0 je Michalovo živé GUI (`PID 2452`, `start_ticks 12233`).

| Artefakt | Overený SHA-256 | Poznámka |
|---|---|---|
| `work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend` | `5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1` | Vybraný východiskový kandidát V16 B (446 495 489 B) |
| `work/v16/meadow_trail_01/source/meadow_trail_v16.py` | `16bde4cf14182b99ae4467cdf4f052ab9067c7a2b46613648140775a4f09266e` | Zdrojový recept V16 B |
| `work/v16/meadow_trail_01/source/meadow_trail_v16.json` | `1298218692c8fe88f27008df9eab287b2f5c3e7bb62866f762df883e748243fb` | Konfigurácia V16 B |
| `work/v16/meadow_trail_01/renders/B_v16_960.png` | `92f865ec1e04190a9d28aed213a93f85a2eac58f32ce2a2961872ddc2f0dece6` | Priamy obrazový základ V16 B (960 × 540) |
| `work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16_c01.blend` | `2b39665905a65db860bc8f21159fbfb7e93ee3e39ab8051b12b15a64b07b8214` | Porovnávací variant V16 c01 (len pre metódu okraja chodníka) |
| `work/v16/meadow_trail_01/source/meadow_trail_v16_c01.py` | `4e1645e6f7b74ba1295ff357208c842fc4c6fdfd3e0c7812a496a4baa565fd11` | Zdrojový recept V16 c01 |
| `work/v16/meadow_trail_01/renders/C_v16_c01_960.png` | `62f4f5afc34f246f125c4da7d22bdb331fde96ac7713b59e6d31420aa196b317` | Render V16 c01 (960 × 540) |
| `/home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16/references/00.png` = `reference/01.png` = `/home/agile/Projects/chata/chatgpt/01.png` | `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d` | Lokálny 1672 × 941 PNG koncept (3 251 765 B); v chate Master Orchestratora mal re-enkódovaný kontajnerový hash `4a898a93...` pod názvom `00(1).png` |
| `work/v12/profile_03/isolated_config/userpref.blend` | `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561` | Izolované MCP-disabled preferencie pre CLI Blender 5.3.0 |

### Priame vizuálne porovnanie `B_v16_960.png` a lokálneho konceptu `00.png` / `reference/01.png`

Otvorila som a skontrolovala `work/v16/meadow_trail_01/renders/B_v16_960.png` oproti `reference/01.png` (`7cbc9890...`):
1. **Dolná štvrtina záberu a lúka:** V16 B má pokojný, prirodzený olivovo-zelený tón bez fľakatosti c01, ale porast v popredí tvoria len rovnomerné trávne trsy z V13. Chýba mu čitateľná botanická hierarchia: prízemné listové ružice/ďatelinový podrast, vyššie ohnuté steblá s teplými hnedastými/zlatistými semeniskami a klasmi zachytávajúcimi bočné slnko a nepravidelne roztrúsené drobné biele súkvetia a striedme žlté kvety.
2. **Predná slučka chodníka pod záhradou:** V `B_v16_960.png` pôsobí predný oblúk chodníka pred plotom stále ako hladko vyrezaná svetlá stuha, pretože efektívny okraj v `meadow_trail_v16.py` bol posunutý dovnútra len o `0,02–0,06 m`, trávny substrát na `V07_TRAIL_MESH` začínal až za fyzickou hranou (`d = 0,12 m`) a nízke trsy krajníc (`0,06–0,14 m`) nesmeli prekryť 15 mm hranu štrku. Naopak, v `meadow_trail_v16_c01.py` hlbší nepravidelný posun okraja + 3D šum + zjednotenie substrátu na hrane `V07_TRAIL_MESH` + osadenie trsov na zazelenaný okraj hornej plochy štrku zjemnili horný chodník, no na prednej slučke treba výraznejšiu obojstranne nesúmernú prácu (kompaktný štrk v strede → drvina a ušliapaná hlina → nízke listy, tráva a ojedinelé kamienky/steblá prerastajúce cez hranu).
3. **Prechod lúky do lesa a listnaté stromy:** Všetkých 6 200 lesných stromov vo V16 B sú smreky (`Picea mariana` a `Picea abies`) s kužeľovitou siluetou. Doplnenie alebo lokálna náhrada vybraných okrajových smrekov niekoľkými nesúmernými skupinami listnáčov (širšie vrstvené koruny buka a vzdušnejšia breza) v presvetlených okrajoch lesa a prípadne jednou skupinou/solitérom na otvorenejšom svahu zmäkčí prechod medzi lúkou a smrečinou v duchu kysuckej mozaiky.

### Handout Revalidation Record

```text
Handout revalidation: projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17/00_handout.md
Received handout status: provisional
Revalidated against: repository commit 78534bd46020bb2bfc97eef69b05e583cba5a5e5; AP pin d7023cf037f6d17885c3ede5c04812c61640da50; Meta commit abfb0ea0226dab1db554abcd47b4cc0a3fc289c1; V16 closure projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16/01_closure.md; V16 B scene work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend (5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1); V16 B recipe work/v16/meadow_trail_01/source/meadow_trail_v16.py (16bde4cf14182b99ae4467cdf4f052ab9067c7a2b46613648140775a4f09266e); V16 B render work/v16/meadow_trail_01/renders/B_v16_960.png (92f865ec1e04190a9d28aed213a93f85a2eac58f32ce2a2961872ddc2f0dece6)
Usable facts: project HEAD 78534bd46020bb2bfc97eef69b05e583cba5a5e5 clean tracked tree; AP pin d7023cf037f6d17885c3ede5c04812c61640da50 (ap doctor PASS); Meta HEAD abfb0ea0226dab1db554abcd47b4cc0a3fc289c1; V16 closed visual PARTIAL with Michal selecting V16 B as baseline and V16 c01 retained for trail-edge comparison only; V16 B blend/recipe/render hashes exact; V16 c01 blend (2b39665905a65db860bc8f21159fbfb7e93ee3e39ab8051b12b15a64b07b8214) and recipe (4e1645e6f7b74ba1295ff357208c842fc4c6fdfd3e0c7812a496a4baa565fd11) present; all prior Worker grants expired and no render running; owner GUI Blender 5.3.0 active at PID 2452 (start_ticks 12233); MCP-disabled userpref.blend (d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561) present; local normalized models in assets/models/ (periwinkle_plant, grass_medium_01, shrub_01, food_apple_01, Norway spruce, Black spruce, Blossoming apple tree) present
Stale facts and corrections: chat-attached reference 00(1).png (1672x941, remote chat-container re-encoded SHA-256 4a898a93960c227954bcb478eadf3bb1d1c9ef4633e5e4566528ca7589f7c2ed) -> local byte-identical 1672x941 reference image is stored at /home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16/references/00.png, /home/agile/Projects/kysucka_moderna_chata/reference/01.png, and /home/agile/Projects/chata/chatgpt/01.png (3,251,765 bytes, SHA-256 7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d); project git status clean at V16 closure -> tracked tree remains clean at 78534bd46020bb2bfc97eef69b05e583cba5a5e5 with untracked owner file reference/01.png (7cbc9890...) classified under RF-12 as unrelated-owner-work and preserved read-only
Not revalidated: external web assets (tevy Wildflower Patch v1, tevy European Beech v1, tevy Silver Birch v1, Poly Haven Dandelion 01, Sketchfab evolveduk Beech tree) and their glTF meshopt/KTX2 import behavior in isolated Blender 5.3.0 (not fetched during Stage 1 read-only bootstrap; assigned to bounded Planner probe / Stage-0 implementation gate); public GitHub API reachability (not required for local checkout verification)
Handout disposition: adopted-with-corrections
```

### Podklad pre zosúladenie Master run map (`00/00_RUN_MAP.md`)

Podľa pokynu v handoute evidujem presné riadky pre zosúladenie V16 (`closed`) a V17 (`provisional` / otvorený celok) v `projects/kysucka_moderna_chata/00/00_RUN_MAP.md` (sledovaný súbor v `/home/agile/meta` nemutujem priamo mimo autority run-scoped Orchestratora / Michala):

```text
Run entry: 16 | kysucka-moderna-chata-meadow-light-and-trail-shoulders-v16 | closed | depends on: kysucka-moderna-chata-reference-light-v15 | handout: not-written | evidence: local V16 B 5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1 and B_v16_960.png 92f865ec1e04190a9d28aed213a93f85a2eac58f32ce2a2961872ddc2f0dece6; closed visual PARTIAL in 00/16-meadow-light-and-trail-shoulders-v16/01_closure.md; Michal selected natural V16 B over blotchy V16 c01
Run entry: 17 | kysucka-moderna-chata-meadow-wildflowers-and-broadleaf-edges-v17 | provisional | depends on: kysucka-moderna-chata-meadow-light-and-trail-shoulders-v16 | handout: projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17/00_handout.md | evidence: Michal requests realistic nature with wildflowers and broadleaf trees; Master proposes local meadow and foreground trail edge refinement on V16 B
```

## 2026-11-19 — Vydanie plánovacieho promptu `01_planning_00.md` (01/01)

Vydávam prvý anglický prompt `01_planning_00.md` pre fresh Plannera (`01/01`, `fresh-worker-session`, `Native planning mode: required`, manuálne doručenie). Pre prípad klientského obmedzenia priameho zápisu v Native Plan Mode je `Report persistence owner` nastavený na `ORCHESTRATOR` (`Trace persistence: none` podľa `PROMPT_CONTRACTS.md` P2): Planner vráti kompletný text `01_report_00.md` začínajúci `### Report for ORCHESTRATOR_CHAT` vo výstupe relácie a Orchestrátorka ho uloží na `/home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17/01_report_00.md`.

## 2026-11-19 — Rekonciliácia `01_report_00.md` (01/01) a vydanie `01_planning_01.md` (01/02)

Report `01_report_00.md` bol prevzatý z `/home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17/01_report_00.md` (73 riadkov, 10 794 B, SHA-256 `d66746fc408fc21ad52a69815ef0c894202c18bf422dbca8b41ab5757e92dd02`, začína na riadku 1 presne `### Report for ORCHESTRATOR_CHAT`, koordináty `01` / `01`, `Status: BLOCKED`).

### Overenie stavu po výmene 01/01 a rekonciliácia zistení

- **Čistota a zachovanie:** `/tmp/opencode/v17_plan_inspect` je úplne odstránený (`TMP_CLEAN`). Východisková scéna `candidate_exterior_v16.blend` má nezmenený SHA-256 `5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1`, globálny `userpref.blend` má nezmenený SHA-256 `8c52b5cf0d5ac23a35c9496e442a37c69399203b47b32842dd76d05653c29c02`, projektový working tree je čistý (len deklarovaný `?? reference/01.png`) a Michalovo živé GUI `PID 2452` (`start_ticks 12233`) ostalo nedotknuté.
- **Potvrdené a prijaté zistenia z `01_report_00.md` (neopakovať sťahovanie v 01/02):**
  1. **Overený import CC0 aktív tevy a Poly Haven v izolovanom Blenderi 5.3.0 (`02f0899d78e3`):**
     - Priamy import GLB s vnoreným KTX2 v Blenderi 5.3.0 dekóduje `meshopt` geometriu, ale zlyhá na vnorenom KTX2 (`IMB_load_image_from_memory: unknown file-format (<packed data>)`, `0 × 0`).
     - **Riešenie potvrdené testom a kontrolným renderom (600 × 360, CPU4, 16 vzoriek, 4,52 s, 1,77 GiB peak RSS):** externalizácia každého KTX2 obrázka podľa `bufferView` offsetu a dĺžky popri lokálnom `.gltf` (so zachovaným BIN chunkom a `meshopt`) a import s `import_ktx_texture=True, import_pack_images=True` v štandardnom Blenderi 5.3.0 bez úpravy importéra vytvorí platné zabalené OpenEXR textúry, farby, non-color normály a alfu 0–1.
     - Zmerané rozmery aktív:
       - `tevy Wildflower Patch v1 LOD0`: `3 860` trojuholníkov, `118,9 × 114,3 × 53,5 cm`; 8 bielych kvetných hlávok (`5,1–7,4 cm`) a žlté hlávky (`3,1–4,0 cm`) možno extrahovať ako samostatné komponenty bez opakovania celej štvorcovej záplaty.
       - `tevy European Beech v1`: `LOD1` `17 674` trojuholníkov (`16,14 × 18,30 m` koruna pred škálovaním), `LOD2` `5 708` trojuholníkov.
       - `tevy Silver Birch v1`: `LOD1` `11 108` trojuholníkov (`10,97 × 11,07 m` koruna pred škálovaním), `LOD2` `5 446` trojuholníkov.
       - `Poly Haven Dandelion 01` (1K Blend): `dandelion_01_a_LOD2` (`15,9 cm`, `629` trojuholníkov) a `dandelion_01_b_LOD2` (`11,3 cm`, `619` trojuholníkov).
       - Lokálne normalizované modely v `assets/models/`: `Grass Medium 01` (`14,5–32,3 cm`), `Shrub 01` (`29,4–37,2 cm`), `Periwinkle Plant` (`20,6–39,7 cm`).
     - Záložný Sketchfab listing `evolveduk Beech tree` vrátil HTTP 403 a nie je potrebný, keďže CC0 `tevy European Beech v1` a `Silver Birch v1` fungujú cez KTX2-externalizovaný `.gltf` import.
  2. **Zmerané vekové rozvrstvenie V11 ihličnanov vo V16 B (6 200 bodov v 126 chunkoch):**
     - `Young`: `1 220` (`1,504 / 4,006 / 6,491 m`, zvislá mierka `0,157 / 0,417 / 0,676`)
     - `Middle`: `1 717` (`7,005 / 11,297 / 16,000 m`, zvislá mierka `0,637 / 1,163 / 1,666`)
     - `Mature`: `3 263` (`13,000 / 18,341 / 23,997 m`, zvislá mierka `1,169 / 1,898 / 2,498`)
- **Rekonciliácia `MEASURED` a `LEAD` critique z `01_report_00.md`:**
  - `MEASURED`: Samotné `PYTHONDONTWRITEBYTECODE=1` nezabránilo vstavanému Pythonu Blenderu vytvoriť 46 `.pyc` súborov v `/home/agile/Applications/Blender/5.3/scripts/addons_core/io_scene_gltf2/**/__pycache__/`, keď sa spustil glTF importér, a v diagnostickom skripte scény zlyhala záverečná JSON serializácia NumPy typov po exporte lesa.
  - **Rozhodnutie Orchestrátorky:** Existujúce `.pyc` bytecode cache súbory v inštalácii Blenderu sú neškodná interná cache interpretu; v grante `01/02` výslovne povoľujem prípadnú Python `__pycache__` tvorbu pri behu Blenderu a zároveň predpisujem `PYTHONPYCACHEPREFIX=/tmp/opencode/v17_plan_inspect/pycache` + `sys.dont_write_bytecode = True` pred prvým importom. Keďže test externých aktív je už v `01_report_00.md` hotový a prijatý, výmena `01/02` (`01_planning_01.md` → `01_report_01.md`, `current-worker-session`, `Planning cycle: targeted-revision`, `Automatic targeted revisions used: 1`) vykoná už iba rýchly read-only audit scény `candidate_exterior_v16.blend` (bez sťahovania a bez glTF importu) a dokončí rozhodnutie-kompletný plán V17.
  - Po prijatí plánu `01_report_01.md` bude nasledovať implementačný grant na súradniciach `01/03` (`01_implementation_02.md` → `01_report_02.md`) v tej istej relácii (alebo `02/01` pri fresh relácii).

## 2026-11-19 — Rekonciliácia a prijatie plánu `01_report_01.md` (01/02) a vydanie `01_implementation_02.md` (01/03)

Plán `01_report_01.md` bol prevzatý z `/home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17/01_report_01.md` (216 riadkov).
- **Poznámka k formátu a RF-19 integrite:** Súbor `01_report_01.md` na disku obsahuje kompletný, zmrazený výstup natívneho Plan Mode (`# V17 implementation plan — meadow plants, broadleaf margins, and front-loop gravel`, §§1–6) z výmeny `01/02` bez obalovej hlavičky `### Report for ORCHESTRATOR_CHAT` (ktorá bola plne prítomná v `01_report_00.md` z výmeny `01/01`). Podľa RF-19 existujúci súbor `01_report_01.md` na disku neprepisujem ani nevytváram ceremoniálnu medzivýmenu iba na doplnenie hlavičky; plán v `01_report_01.md` (spolu s podkladovým reportom `01_report_00.md`) prijímam ako rozhodnutie-kompletnú technickú špecifikáciu V17 a v implementačnom grante `01_implementation_02.md` (`01/03`) vyžadujem, aby terminálny report `01_report_02.md` začínal na prvom riadku presne `### Report for ORCHESTRATOR_CHAT`.

### Prijatý technický návrh V17 (`apply_v17(scene, config, project_root, *, stage)`, seed `13717`)

1. **Audit scény V16 B a ochrana 6 `IsViewport` vetiev:**
   - Východisko `candidate_exterior_v16.blend` (`5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1`): 5 084 linkovaných objektov, 87 zabalených obrázkov, 0 externých knižníc, 126 aktívnych `V11_FOREST` mračien (6 200 bodov: `Young` 1 220, `Middle` 1 717, `Mature` 3 263 + samostatné `V04_YOUNG_00/01/02` viditeľné a `03` skrytý), 52 `V13_MEADOW_CLOUD_*` mračien (29 000 bodov), 2 903 `V16_SHOULDER_POINTS` (558 v úseku prednej slučky `5 ≤ s ≤ 44 m`), všetkých 6 existujúcich `IsViewport` working knižníc (`V12_WORK_CORE_LAWN`, `V12_WORK_CORE_MEADOW`, `V12_WORK_EXTERIOR_MEADOW`, `V12_WORK_FOREST`, `V13_MASTER_MEADOW_WORK`, `V16_MASTER_SHOULDER_WORK`) overených.
   - Na prednej slučke (`5 ≤ s ≤ 44 m`) má všetkých 795 hraničných vrcholov `V07_TRAIL` presnú XY zhodu s terénom (`560` na `V11_TERRAIN_NEAR`, `235` na `V11_TERRAIN_FAR`) s výškou hrany `14,999986–15,000015 mm` a hustotou `87,98–116,39 trojuholníkov/m²`.
2. **Tri cieľové zóny, pilot a nízka kamera `CAM_V17_LOW_DETAIL`:**
   - **Zóna A (blízky svah v popredí):** konvexný obal 5 zameraných lúčov hlavnej kamery (`u = 0,16–0,86`, `v = 0,75–0,985`, hĺbka `≤ 22 m`) zjednotený s `.65 m` obalom pilota.
   - **Zóna B (lúčna strana prednej slučky pod plotom):** `7,5 ≤ s ≤ 42 m`, `-(h + 1,35) ≤ lateral ≤ -(h + 0,12)`.
   - **Zóna C (okraje lesa):** k lúke otočená polovica 5 m obalu okolo koreňov skupín `R`, `L`, `D` (iba prízemný kryt a steblá so semeniskami, bez jednotlivých kvetných hlávok).
   - **Pilot (`stage="pilot"`):** `.65 m` obal 4 zameraných kotiev v popredí (vynútené 2 biele hlávky na kotvách 1 a 3, 1 žltá hlávka na kotve 2, 1 ohnuté steblo so semeniskom na kotve 4) + Zóna B a obe krajnice chodníka na `21 ≤ s ≤ 36 m` + pravá listnatá skupina `R` (`R1, R2, R3`) s podrastom Zóny C.
   - **Fixná nízka kamera `CAM_V17_LOW_DETAIL`:** poloha `(48; -21,75; 8,070608535)` (`0,680 m` nad vyhodnoteným terénom `7,390608535 m`), cieľ `(33,871910472; -7,882651524; 5,225659935)` cez `to_track_quat('-Z','Y')`, `28 mm`, senzor `36 × 24 mm`, 16:9, nulový shift, clip `0,03–450 m`, DOF vypnuté.
3. **Botanická vrstva lúky a kvety (`V17_BOTANICAL_IsViewport`):**
   - `tevy Wildflower Patch v1 LOD0` (`8fd2262d...`): 8 bielych hlávok (`5,1–7,4 cm`, ID `2380..2772`) na zakrivených 5-bokých stonkách (`0,27–0,39 m`), 8 žltých hlávok (`3,1–4,0 cm`, ID `2828..3178`, RGB `× 0,82`) na stonkách (`0,18–0,30 m`) a 6 prízemných trojlistových/ďatelinových trsov (`≤ 0,15 m`).
   - `Poly Haven Dandelion 01 1K Blend` (`9751bb96...`): prízemné listové ružice z `dandelion_01_a_LOD2` a `dandelion_01_b_LOD2` (`≤ 0,075 m`) na každom 8. prízemnom osadení.
   - Fyzické kubicky prehnuté steblá so semeniskami (`H = 0,26; 0,34; 0,42; 0,48 m`, 3 šesťkláskové poschodia na koncových `4–7 cm`, teplé lineárne RGB `(0,102; 0,078; 0,035)` steblo a `(0,240; 0,145; 0,054)` semenisko, 3 jasové varianty `0,88; 1,00; 1,09` pod existujúcim svetlom `V16_WORLD_MEADOW_BALANCE`).
   - Elipsové zhluky so seedom `13717` (stropy `500` prízemných ružíc/trsov, `350` stebiel so semeniskami, `52` bielych a `24` žltých kvetov) s vlastným `V17_BOTANICAL_IsViewport` (`≤ 32` trojuholníkov/proxy).
4. **Listnaté skupiny pri okrajoch smrečín (`V17_BROADLEAF_IsViewport`):**
   - 8 osadení (`R1, R2, R3` vpravo, `L1, L2` vľavo, `D1, D2` vzdialenejší pravý okraj, `O1` solitér brezy na otvorenejšom svahu `(-33; 93)`) z `tevy European Beech v1` (`LOD1` `17 674` trojuholníkov render / `LOD2` `5 708` working proxy) a `tevy Silver Birch v1` (`LOD1` `11 108` render / `LOD2` `5 446` working proxy).
   - Lokálna náhrada 4 konkrétnych okrajových smrekov (`V11_TREE_01610`, `02456`, `01307`, `03274` → `6 196` zachovaných V11 ihličnanov, všetkých `1 220` mladých stromov nedotknutých) a doplnenie 4 briez, s preukázanými odstupmi od chaty (`≥ 85,76 m`), plota/záhrady (`≥ 74,44 m`), jablone (`≥ 92,01 m`), chodníka (`≥ 34,24 m`), osi doliny a výhľadu z presklenia.
5. **Predná slučka chodníka a živé okraje (`5 ≤ s ≤ 44 m`):**
   - Spoločné pole uložené na `V07_TRAIL` a `V11_TERRAIN_NEAR/FAR` so zachovaným pojazdným stredom `|lateral| ≤ 0,480 m` (`0,96 m` čistá stopa) a nesúmernými vlnami `I-`, `I+`, `Eσ`, `W-`, `W+`, `F`, `G`, `K`. Na hrane `p = 0` oba povrchy prechádzajú cez jemnú drvinu/hlinu (`F`) do zhodného ekologického substrátu V16 B (`G`) bez fľakov c01.
   - Z toho istého poľa sú osadené terénne trsy/nízke listy (strop `420`), previsnuté steblá zakorenené `≥ 6 mm` vo vnútri hornej plochy štrku (strop `100`, svetlosť `≥ 1 mm` nad hranou) a drobné kamienky `1,8–4,0 cm` z `V07_STONES_MASTER_0..2` (strop `140`) s oporou `exposure ≤ 1 mm`, `burial ≤ 18 mm` a vlastnou `IsViewport` working vetvou (stride 4, `≤ 24` trojuholníkov/proxy).

Vydávam samostatný realizačný prompt `01_implementation_02.md` (`01/03`, `current-worker-session`, `Native planning mode: not-used`).


