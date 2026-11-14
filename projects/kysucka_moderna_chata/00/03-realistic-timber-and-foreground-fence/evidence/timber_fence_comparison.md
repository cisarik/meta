# V03 — porovnanie exteriérového dreva a predného plota

Logický celok: `kysucka-moderna-chata-realistic-timber-and-foreground-fence`
Vstupný commit projektu: `d67431d1678de511e06a8ad04cd632ae4899cdc4`
Výsledný publikovaný commit projektu: `623d12abe0c0eb2742cd02c9962c1712b53437e2`
AP pin: `d7023cf037f6d17885c3ede5c04812c61640da50`
Cesta: `blender-mcp-live-v1` + `blender-local-v1` (cold CLI kontrola a factory-startup source replay).

## 1. Materiály, PBR textúry a metrické UV

- **`MAT_TIMBER_EXTERIOR`** používa oficiálnu 2K CC0 sadu **`coated_pine_02`** ([Poly Haven](https://polyhaven.com/a/coated_pine_02), licencia [CC0](https://polyhaven.com/license)) na presne **89 exteriérových objektoch** (`CLADDING_front*` 35, `CLADDING_rear*` 33, `GABLE_timber*` 16, `SOFFIT_wood*` 2, `WOOD_BAY_post*` 2, `GABLE_other_proposed` 1).
- **`MAT_TIMBER_FENCE`** používa oficiálnu 2K CC0 sadu **`rough_wood`** ([Poly Haven](https://polyhaven.com/a/rough_wood), licencia [CC0](https://polyhaven.com/license)) na presne **28 objektoch plota** (`FENCE_post_proxy*` 26 stĺpikov, `FENCE_rail_proxy*` 2 priebežné priečky).
- Pôvodné materiály **`MAT_WOOD_H`** (32 objektov: jedálenský a konferenčný stôl, 6 sedákov stoličiek, kmeň a 23 konárov jablone) a **`MAT_WOOD_V`** (45 objektov: nástenná dekorácia, 6 operadiel stoličiek, 38 kmeňov ihličnanov) zostali **100 % nezmenené**.
- Šesť 2K JPG súborov (`10 577 778` bajtov spolu) má overené veľkosti, MD5 a SHA-256 v `assets/ASSET_MANIFEST.md`; originálne JPG súbory na disku sa nijako neupravovali.
- **Smer vlákien a metrické `UVMap`**:
  - V `coated_pine_02` vedú vlákna vodorovne po osi `U` (`tile_m = 1.05 m`); v `rough_wood` vedú vlákna zvisle po osi `V` (`tile_m = 0.50 m`), preto má plot zámenu `(u, v) -> (v, u)`.
  - Všetkých 89 exteriérových objektov (vrátane predtým neomapovaných `GABLE_timber*`, `GABLE_other_proposed` a `SOFFIT_wood*`) aj 28 objektov plota má explicitnú `UVMap` v reálnych metroch pozdĺž skutočnej dlhej osi prvku s deterministickým posunom `(du, dv)` zo `sha256(obj.name.encode())` a **0 degenerovaných UV plôch**.
  - Po prvom kontrolnom rendri bola aplikovaná jedna zameraná korekcia shaderu `MAT_TIMBER_EXTERIOR`: saturácia `0.85`, hodnota `0.68`, variácia jasu medzi doskami `0.94–1.06`, drsnosť `0.42–0.58`, plus pomalá neperiodická maska miešajúca dve posunuté fázy tých istých máp (`phase_offset_uv = (0.317, 0.419)`, `scale = 0.38`), ktorá odstránila opakovanie hrčí bez zmeny geometrie alebo pridania ďalších súborov.

## 2. Umiestnenie a geometria predného rustikálneho plota

- Zvolený **Trial 1** vedie po priamej 3D línii pred záhradou z **`(16.60, -8.62)` do `(18.25, 1.00)`** (dĺžka `9.761 m`) pri uzamknutej kamere `CAM_A_REFERENCE` (`[21.5, -10.0, 1.25]`, cieľ `[8.5, 2.5, 1.25]`, `35 mm`, `shift_y = 0.105`).
- Plot tvorí **26 stĺpikov** (25 štiepaných kolov s miernou variáciou výšky `Z_top = 0.58 ± 0.04 m`, šírky `0.085 ± 0.015 m`, hrúbky `0.065 ± 0.010 m` a náklonu `<= 2°` + 1 hrubší kotviaci stĺpik `FENCE_post_proxy.004` na `s = 0.14`, prierez `0.16 × 0.13 m`, `Z_top = 0.62 m`) a **2 priebežné vodorovné priečky** (`Z = 0.19 m` a `Z = 0.43 m`, prierez `0.055 × 0.065 m`, predsadené o `0.020 m` smerom ku kamere).
- **Ukotvenie v teréne a prepojenie**:
  - Všetky päty stĺpikov majú svetové `Z` v rozsahu `[-0.076718, -0.073282] m`, teda zapustené pod povrch terénu `SITE_terrain_proxy` (`Z = -0.055 m`).
  - Kontrola priesečníkov cez `BVHTree.overlap` potvrdila všetkých **52 priesečníkov** (každý z 26 stĺpikov fyzicky pretína spodnú aj hornú priečku).

| Kontrola priemetu v kamere `v03` (top-left UV) | `u` | `v` horného vodiaceho bodu (`Z = 0.58 m`) | `v` päty (`Z = -0.075 m`) | Pásmo podľa zadania |
|---|---:|---:|---:|---|
| Ľavý okraj záberu | `0.0000` | **`0.8315`** | `1.0187` | dolná pätina (`0.80–1.00`) — **PASS** |
| Kotviaci stĺpik (`FENCE_post_proxy.004`) | `0.2650` | `0.8031` | `0.9668` | výrazný rohový/kotviaci stĺpik vľavo — **PASS** |
| Stred pod vstupnými schodmi | `0.3400` | **`0.7978`** | `0.9521` | čisto pod schodmi (`v_step1 = 0.7329`) — **PASS** |
| Pravý okraj záberu | `1.0000` | **`0.7325`** | `0.8229` | dolných 20–40 % (`0.60–0.80`) — **PASS** |

## 3. Zhodné porovnávacie rendery a výrezy 1 : 1

- `renders/before.png` (`3774ee85acf9e553f377dc98d0e11d10939886c25a6e6831cc4e2bec445acda8`) je čerstvý render nezmenenej scény `v02`; `renders/after.png` (`3c77ef772bb5578aa54227df98615356cc301c9542fffe982071bed62b0d69d1`) je finálny render `v03`.
- Oba rendery boli vyhotovené s identickým profilom: **`1448 × 1086` (`100 %`), Cycles CPU, 96 vzoriek, `use_denoising = True` (`OPENIMAGEDENOISE`), frame `0`, seed `0`, `AgX`, look `None`, exposure `0.0`, gamma `1.0`, 8 vlákien**.
- `renders/timber_details.png` (`5071d753069f680615a2617abb127f06428b172947c7e00e6fe5bf5059ff3ae7`, `1580 × 1470`) zobrazuje 1 : 1 výrezy `Pred (v02)` a `Po (v03)` bez AI retuše zo súradníc:
  - Fasáda: `(550, 619, 1000, 804)`
  - Štít: `(1042, 130, 1448, 673)`
  - Podhľad: `(246, 550, 1000, 665)`
  - Plot: `(174, 793, 811, 1086)`

## 4. Zachovanie necieľových skupín, cold CLI kontrola a source replay (`work/v03_source_replay.blend`)

- **Preservation odtlačky medzi `v02`, živou `v03` a cold CLI otvorením `v03`**:
  - Kombinovaný SHA-256 odtlačok všetkých 539 vylúčených objektov, kamery, 89 exteriérových geometrií, pôvodných materiálov, svetiel, sveta a vegetácie je identický: `e895f2a01dd1746faa70a9c422f24ba78d2b361171a84cc8e0eed816e9cabd62`.
  - Cold CLI kontrola (`scripts/inspect_scene.py` s `--background --disable-autoexec` na `blender/kysucka_chata_mcp_v03.blend`) skončila s `exit 0` (`656` objektov, `13 568` vrcholov, 7 zabalených obrázkov vrátane referencie a 6 PBR máp).
- **Source replay (`work/v03_source_replay.blend`) a idempotencia**:
  - V `scripts/build_scene.py:321` bol doplnený kompatibilitný výber `sky.sky_type` (`'NISHITA'` ak je v `enum_items`, inak `'SINGLE_SCATTERING'` pre Blender 5.2.3 LTS, čo presne zodpovedá otvorenej scéne `v02`/`v03`).
  - Zostavenie od nuly (`--background --factory-startup --python scripts/build_scene.py -- --output work/v03_source_replay.blend`) skončilo s `exit 0` (SHA-256 `93f6ae577773ceba3b7cb96e985feb63d8c65524eb8ff6cfbab3f7e29e84a7ce`).
  - Kým hrubý RNA dump celého súboru v `01/03` zachytil nevizuálne rozdiely predvolených UI šírok uzlov (`150` v seedu z Blenderu 4.3.2 oproti `160` pri `--factory-startup` v 5.2.3 LTS), priame sémantické a tolerančné porovnanie uloženej `blender/kysucka_chata_mcp_v03.blend`, `work/v03_source_replay.blend` a druhého (idempotentného) zavolania `apply_v03` potvrdilo:
    - `object_count = 656`, identické zoznamy objektov a priradenia materiálov na všetkých 656 objektoch (`89` `MAT_TIMBER_EXTERIOR`, `28` `MAT_TIMBER_FENCE`, `32` `MAT_WOOD_H`, `45` `MAT_WOOD_V`),
    - identických 7 zabalených obrázkov, farebné priestory a relatívne cesty,
    - identické uzly a vstupy `MAT_TIMBER_EXTERIOR` a `MAT_TIMBER_FENCE`,
    - `max_pos_err_m = 0.0 m` (tolerancia `1e-5 m`),
    - `max_vert_err_m = 1.4901e-08 m` (tolerancia `1e-5 m`),
    - `max_uv_err = 0.0` (tolerancia `1e-6`),
    - `max_rot_err_rad = 0.0 rad` (tolerancia `1e-6 rad`),
    - `0` degenerovaných UV plôch a `0.0 m` odchýlka polôh všetkých stromov a kríkov (`global_rng_unchanged = True`).

## 5. Zaznamenané rezíduá a Michalov brainstorming pre ďalší celok (Master Chat Orchestrator)

1. **Zalesnené kopce so smrekovým lesom v pozadí, malé smreky pri chate, jabloň s jablkami a predné kríky (Michalova priorita pre ďalší celok)**:
   - Michal pri odovzdaní formuloval jasnú predstavu o nasledujúcom kroku pre Master Chat Orchestratora:
     - v pozadí chce viditeľné **kopce s realistickými smrekovými lesmi** (súčasných 38 kužeľových `CONIFER_proxy*` na vzdialenom svahu je riedkych, malých a geometricky umelých),
     - v blízkosti chaty chce **menšie realistické smreky**,
     - v záhrade vľavo chce **realistickú jabloň s jablkami** (namiesto guľového `APPLE_foliage_proxy*`),
     - pred domom chce nahradiť **nerealistické „videoherné“ guľové kríky** (`SHRUB_proxy*` / `FLOWER_proxy*`),
     - a navrhuje, aby **Master Chat Orchestrator vyhľadal na internete vhodné CC0 / kompatibilné 3D objekty a assety** pre smrekový les, malé smreky pri chate, jabloň s jablkami a záhradné kríky, aby výsledok pôsobil ako skutočná architektonická vizualizácia.
2. **Ostatné odložené pozorovania zo vstupného zadania**:
   - osvetlenie oblohy/denného svetla (štítové drevo a podhľad pod presahom strechy sú v tieni tmavšie než na referencii),
   - viditeľnosť krbu s ohňom cez rohové sklo a nadväznosť komína,
   - vnútorné priečky (`PARTITION_proposed*`) viditeľné cez presklenie.
