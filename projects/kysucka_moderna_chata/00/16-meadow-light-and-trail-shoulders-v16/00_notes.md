# Poznámky orchestrátorky — V16 · zlaté akcenty lúky, tieň stromov a nepravidelné krajnice chodníka

Autor: ORCHESTRATOR tohto celku
Access profile: Orchestrator
Orchestrator session scope: logical-whole
Development run identity: kysucka-moderna-chata-reference-visualization
Logical whole identity: kysucka-moderna-chata-meadow-light-and-trail-shoulders-v16
Dátum otvorenia: 2026-11-19, Europe/Bratislava
Životný cyklus: prevádzkové poznámky tohto celku; historická evidencia, nie task authority; pri uzavretí zmraziť, prípadné čistenie vlastní COOPERATOR pod osobitným grantom.

## 2026-11-19 — Continuation Bootstrap a výber nového celku V16

Michal doručil uzáver predchádzajúceho celku
`/home/agile/meta/projects/kysucka_moderna_chata/00/15-reference-light-v15/01_closure.md`
do tejto orchestrátorskej session a po read-only rekonciliácii (Continuation
Bootstrap Stage 1 & 2) vybral otvorenie nového logického celku **V16**
(`kysucka-moderna-chata-meadow-light-and-trail-shoulders-v16`) v tejto session
(záznam odchýlky od fresh-instance defaultu podľa AP §3 / Run-Scoped
Orchestration: pokračovanie v aktuálnej orchestrátorskej session po priamom
vizuálnom porovnaní A/B/C/01.png šetrí rekonštrukciu kontextu; predchádzajúce
celky V07–V15 zostávajú uzavreté/zmrazené a ich expirované granty sa
neotvárajú).

### Michalove explicitné rozhodnutia pre V16 (Stage 2)

1. **Vybraný koherentný výsledok (Rozsah V16):**
   - **Zlaté akcenty a členitosť lúky/svahov oproti referencii `01.png`:**
     zvýrazniť teplé zlatisto-zelené bočné slnečné akcenty na zvlnených svahoch
     a lokálny mikrokontrast / členitosť porastu lúky (bez rozbitia súvislého
     pokrytia 29 000 exteriérových trsov z V13).
   - **Čitateľnejší detail v tieni stromov:** zachovať teplé oblaky, bočné
     nasvietenie chaty a kratší tieň z V15 C, ale vrátiť čitateľnejšiu kresbu
     vetiev a kmeňov v tieni lesa (ktorá bola v B viditeľnejšia než v C).
   - **Nepravidelná šírka a mäkké trávnaté krajnice štrkového chodníka
     (`0.45–0.75 m`):** vyriešiť odložený bod z V07/V13/V15 — nahradiť ostrý,
     geometricky rovnomerný okraj štrkového chodníka prirodzene nepravidelnou
     šírkou a mäkkými, trávou prerastajúcimi krajnicami podľa `01.png`
     so skutočnou podporou na teréne.
   - *(Mimo rozsahu V16: samostatná oprava bledo-sivobieleho vonkajšieho terénu
     v pracovnom režime Material Preview ostáva oddelená, pokiaľ úprava
     materiálu terénu v rámci V16 tento stav priamo nezlepší; interiér V10,
     architektúra chaty a kamera `CAM_V11_VALLEY_REVIEW` sa nemenia.)*
2. **Východisková scéna:** **V15 C · tonal**
   (`work/v15/reference_01/checkpoints/candidate_exterior_v15_tonal.blend`,
   433 603 200 B, SHA-256
   `15870b192662714a40ae7772a120e554acd9c3317e6ebfa1be54d4ac907d5bf2`).
3. **Doručovanie Worker úloh:** **Manuálne doručenie (COOPERATOR)**; všetky
   Blender operácie Workera bežia výhradne v izolovanom natívnom CLI procese
   (`/home/agile/Applications/Blender/blender --background --disable-autoexec --threads 4`,
   nice +10, izolovaný config/temp s MCP-disabled `userpref.blend`) mimo
   Michalovho živého GUI okna (aktuálne PID 2452, start_ticks 12233). Live MCP
   sa v exteriérovej linke V16 nepoužíva.

### Priamo overený stav repozitárov, hardvéru a vstupných SHA-256

- **Projektový repozitár:** `/home/agile/Projects/kysucka_moderna_chata`,
  branch `main`, čistý working tree (`git status --porcelain=v1` prázdny),
  HEAD `78534bd46020bb2bfc97eef69b05e583cba5a5e5`, lokálny backup origin
  `/home/agile/backups/git/kysucka_moderna_chata.git`.
- **AP submodule:** `.ap` gitlink aj čistý detached HEAD
  `d7023cf037f6d17885c3ede5c04812c61640da50`.
- **Meta repozitár:** `/home/agile/meta`, branch `main`, HEAD
  `abfb0ea`.
- **Hardvér a procesy pri otvorení:** CachyOS, Ryzen 5 3600, 31 GiB RAM total /
  ~19 GiB available; RTX 3080 10240 MiB total / 2278 MiB used / 7596 MiB free.
  Jediný bežiaci Blender je Michalovo GUI PID `2452` (`start_ticks 12233`).

| Artefakt | SHA-256 |
|---|---|
| `work/v15/reference_01/checkpoints/candidate_exterior_v15_tonal.blend` (V15 C · vstup) | `15870b192662714a40ae7772a120e554acd9c3317e6ebfa1be54d4ac907d5bf2` |
| `work/v15/reference_01/renders/C_tonal960.png` (V15 C · 960×540 control) | `3110941602665c563dfbe9bfe4ce9f118fb4d11dcb2fbc14ffeff15b3b8704d2` |
| `work/v15/reference_01/renders/B_reference960.png` (V15 B · 960×540 porovnanie) | `1315bb7a50528ca7d77b41527dbf080e3a30bb93805569f351e9ae09751c9cb5` |
| `work/v14/native_02/renders/B_final960.png` (V14 A · 960×540 porovnanie) | `334bc640d65490dfee64cfe7768daaf85d2bcdbf64f70264420537cadeb72c05` |
| `/home/agile/Projects/chata/chatgpt/01.png` (Michalova cieľová referencia) | `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d` |
| `work/v15/reference_01/source/reference_light_v15.py` | `40e71376d5b08490c5545eb15fd42c45887ce26714cf2e4ef06549becc5bd57c` |
| `work/v15/reference_01/source/tonal_reference_v15.py` | `72c1cea50d82d95f0a4384d8fe048fb9b19a4905edeff88c32c92c1c6ae52220` |
| `work/v13/meadow/correction_01/source/meadow_v13.py` | `6bf2b052b04101348dbc8167a86335391af7e26383e49bcdd8e348baefc79993` |
| `work/v12/profile_03/isolated_config/userpref.blend` (MCP-disabled prefs) | `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561` |

### Plán koordinácie celku V16

1. **Planner 01/01 (`01_planning_00.md` → `01_report_00.md`):**
   - `fresh-worker-session`, `Native planning mode: required`, manuálne
     doručenie.
   - Read-only inšpekcia zdrojov V11/V13/V14/V15, obrázkov A/B/C/`01.png` a
     jeden izolovaný read-only headless Blender prieskum scény V15 C
     (`candidate_exterior_v15_tonal.blend`) bez zápisu do `work/` a bez dotyku s
     GUI PID 2452.
   - Rozhodnutie-kompletný plán pre: (A) svetlo a shader/tónovanie svahov a
     lúky (zlaté slnečné akcenty + lokálny mikrokontrast trsov/terénu +
     zachovanie detailu v tieni stromov medzi B a C); (B) nepravidelnú šírku a
     mäkké trávnaté krajnice štrkového chodníka (`0.45–0.75 m`) s plynulým
     prechodom štrku do trávy a so skutočnou podporou na teréne; (C) presné
     hranice mutácie v `work/v16/meadow_trail_01/**`, zachovanie 87 zabalených
     obrázkov, kamery `CAM_V11_VALLEY_REVIEW` a P0 CPU4/96/960×540 profilu.
2. **Implementation 01/02 (`01_implementation_01.md` → `01_report_01.md`):**
   - Po prijatí plánu obnova autority v tej istej zdravej Worker session
     (`current-worker-session`, `Native planning mode: not-used`), jeden
     kandidát V16 + matched 960×540 render a nanajvýš jedna cielená korekcia po
     mojej priamej kontrole pixelov.

## 2026-11-19 — rekonciliácia plánu 01/01 a vydanie implementation grantu 01/02

Report `01_report_00.md` bol prevzatý z
`/home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16/01_report_00.md`
(236 riadkov, SHA-256
`e4c962ea5984d9e54cb5c568475f9b3344231578b12c32d871ced9da6627c341`).
Overenie po behu Plannera:
- `/tmp/opencode/v16_plan_inspect` je úplne odstránený (`TMP_CLEAN`).
- Východisková scéna `candidate_exterior_v15_tonal.blend` má nezmenený SHA-256
  `15870b192662714a40ae7772a120e554acd9c3317e6ebfa1be54d4ac907d5bf2`.
- Projektový working tree a AP submodule sú čisté; Michalovo GUI PID 2452
  (`start_ticks 12233`) zostalo nedotknuté (inšpekcia trvala 8,70 s, peak RSS
  2,00 GiB, min. dostupná RAM 16,44 GiB, 0 uložení, 0 renderov).
- Poznámka k formátu: pri uložení relayovaného reportu na disk je riadok 1
  prázdny a chýba na ňom literal `### Report for ORCHESTRATOR_CHAT`, hoci
  koordináty `01` / `01`, `Status: PASS`, `Phase-qualified result: not-applicable`,
  `Logical-whole closure: not-closed` a celý compact core sú prítomné. Podľa
  RF-19 existujúci terminálny report na disku neprepisujem; v grante 01/02 ho
  viažem presným SHA-256 `e4c962ea…` a vyžadujem, aby `01_report_01.md` začínal
  presne `### Report for ORCHESTRATOR_CHAT` na prvom riadku.

### Rekonciliácia MEASURED critique a prijatie plánu

- **MEASURED critique od Plannera potvrdený:** aktívne terénne siete
  (`V11_TERRAIN_NEAR/FAR/EXTENSION` → `V13_V11_TERRAIN_*_MESH`) nepoužívajú
  slot `MAT_V07_SHOULDER` na žiadnej ploche a pôvodný `V07_SHOULDER_POINTS`
  (60 552 bodov do 1,15 m) je skrytý vo viewporte aj renderi. V16 preto musí
  riešiť aktívny terén, štrkový chodník a populáciu nízkych trsov krajníc
  spoločne.
- **Prijatý technický návrh V16 (`apply_v16(scene, config, ROOT) -> dict`, seed `13716`):**
  1. **Vlastníctvo a zachovanie:** vlastné deriváty 3 terénnych sietí a siete
     chodníka (`V07_TRAIL_MESH`), `V16_MASTER_MEADOW_RENDER` so 48 linkovanými
     objektmi a 4 kópiami materiálov lúky, klonovaná GN skupina so zachovaným
     `IsViewport` TRUE ramenom (`V13_MASTER_MEADOW_WORK`, stride 8), 29 000
     lúčnych a 6 200 lesných umiestnení nezmenených, 87 zabalených obrázkov so
     zachovanou hĺbkou ciest (vrátane Qwantani `//../../../v14/assets/qwantani_sunset_puresky_2k.hdr`).
  2. **Zlaté akcenty a mikro-textúra lúky/svahov:** svetové XY šumové pole
     (`18 m`, `3 m`, `0.28 m`; Detail 2, Roughness 0.5),
     `F = smoothstep(0.36, 0.68, 0.65*N18 + 0.35*N3)`,
     `D = smoothstep(0.18, 0.62, dot(unbumped_normal, key_source_vector))`;
     terénny zlatý mix `0.38*D*F` (`[0.30, 0.255, 0.065]`, vážený
     `v13_exterior_weight`), lúčny zlatý mix `(0.08 + 0.22*D)*F`
     (`[0.38, 0.32, 0.075]` do difúznej aj priesvitnej vetvy), 3 m jasový
     multiplikátor `0.86–1.14`, mikro-multiplikátor `0.88–1.14` (lúka) /
     `0.94–1.06` (terén), drsnosť lúky `±0.04` (`0.62–0.94`), exteriérový
     mikro-bump terénu `0.15` / `0.008 m`.
  3. **Tieň stromov (`V16_WORLD_MEADOW_BALANCE`):** kópia sveta V15 C so zmenou
     iba fill strength na **`0.92`** a fill linear tint na **`[1.0, 0.94, 0.80]`**;
     oblaky a kľúčové slnko (`V15_SUN_REFERENCE_KEY`) ostávajú presne ako v C.
  4. **Nepravidelný chodník a mäkké krajnice (`0.45–0.75 m` na každej strane):**
     efektívny okraj `Eσ(s) = h(s) - a(s)*(0.02 + 0.04*Nedgeσ(s))` (vlny
     `2.7/8.5 m`), šírka krajnice `Wσ(s) = 0.45 + 0.30*Nwidthσ(s)` (vlny
     `4.5/13 m`), chránený pojazdný stred `abs(lateral) ≤ h(s) - 0.08` (min.
     `0.96 m`), 0.10 m ochrana záhrady/prechodu/bránky; spoločný prechod
     štrk → `0–0.12 m` ušliapaná hlina (`[0.115, 0.095, 0.040]`, roughness
     `0.96`) → `0.12 m až Wσ` lokálny V16 substrát; 8 nízkych trsových predlôh
     z V13 nízkych foriem (`0.06–0.14 m`, ≤192 render / ≤24 working trojuholníkov,
     vlastný `IsViewport` prepínač s working stride 4 → max. +36 000 working
     trojuholníkov), jitterovaná `0.20 m` mriežka (`6 → 24 trsov/m²`, strop
     **6 000**), odstup od efektívneho okraja štrku ≥0.02 m, vyčnievanie koreňov
     ≤1 mm, zanorenie ≤18 mm, zjemnenie pri rozpätí >5 mm, ošetrenie 15 mm
     hrany štrku so škálovaním `0.75`/`0.5` pred zamietnutím.
  5. **Overenie a výstupy:** tri sériové CPU4 úlohy (build/save → fresh replay
     bez uloženia → cold reopen/render 960×540/96 OIDN Accurate/High pod 157,5 s)
     v `work/v16/meadow_trail_01/` + pevné výrezy a metriky oproti C, B a `01.png`.

Vydávam implementačný grant `01_implementation_01.md` (koordináty `01/02`,
`current-worker-session`, `Native planning mode: not-used`).

## 2026-11-19 — rekonciliácia 01/02 (`B_v16_960.png`) a vydanie jedinej korekcie `c01` (01/03)

Report `01_report_01.md` bol prevzatý a overený (136 riadkov, SHA-256
`07e55c077a9306b9f972af6f78770ea3fcc2c40aa6e689acba5bd057df8f8a00`, začína
presne `### Report for ORCHESTRATOR_CHAT` na riadku 1).
Overené artefakty z výmeny 01/02 (`work/v16/meadow_trail_01/`):
- `checkpoints/candidate_exterior_v16.blend` — 446 495 489 B, SHA-256
  `5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1`
- `renders/B_v16_960.png` — 910 647 B, SHA-256
  `92f865ec1e04190a9d28aed213a93f85a2eac58f32ce2a2961872ddc2f0dece6`
- `source/meadow_trail_v16.py` — SHA-256
  `16bde4cf14182b99ae4467cdf4f052ab9067c7a2b46613648140775a4f09266e`
- `source/meadow_trail_v16.json` — SHA-256
  `1298218692c8fe88f27008df9eab287b2f5c3e7bb62866f762df883e748243fb`
- Východisková scéna V15 C (`15870b19…`), čistý projektový working tree a
  Michalovo GUI PID 2452 (`start_ticks 12233`) zostali nedotknuté.
- Všetky technické brány prešli: idempotencia, fresh-input replay a cold reopen
  majú zhodný sémantický hash
  `4249dbeece0841283190e47815d9718181d18f6cda9001d0ccd883d26887cfb0`;
  87 zabalených obrázkov a všetkých 6 `_working_branch` kontrol prešlo;
  2 903 trsov krajníc prešlo kontrolou 205 680 bazálnych vrcholov
  (`exposure ≤ -1.999 mm`, `burial ≤ 8.116 mm`); natívny render trval
  118,83 s (peak RSS 4,38 GiB, min. dostupná RAM 15,72 GiB).

### Priama vizuálna kontrola `B_v16_960.png` a diagnostika príčin PARTIAL stavu

Pozrela som si `B_v16_960.png` vlastnými očami a porovnala ho s V15 C, V15 B,
`01.png` a zdrojovým kódom `meadow_trail_v16.py`:
1. **Svetelný balans a tieň stromov (`V16_WORLD_MEADOW_BALANCE`) — PASS (zachovať):**
   Fill `0.92` / `[1.0, 0.94, 0.80, 1.0]` trafil cieľové pásmo: medián luma v
   tieni ľavého lesa stúpol z C `24.633` na **`29.095`** (p5 `18.637`), pomer
   tieňa chaty k osvetlenej tráve je **`0.6481`** (cieľ `0.60–0.71`) a obloha
   je zhodná s C (`5.936`). Tento svetelný balans sa v `c01` nemení.
2. **Prečo sú zlaté akcenty svahov a kontrast lúky v `B_v16_960.png` ešte
   príliš slabé (`Front meadow std 9.816` vs `≥10.2`, `RMS 6.259` vs `≥6.3`,
   `Left/Right slope std 5.303/7.356` vs `≥5.5/7.8`, `Left slope golden 0%`):**
   - V `meadow_trail_v16.py` r. 76–77 je `D = smoothstep(0.18, 0.62, dot(N, sun))`
     viazané na azimut slnka `285°`, takže ľavý svah má `dot < 0.18` (`D ≈ 0`)
     a nedostal žiadnu zlatú moduláciu.
   - `ShaderNodeTexNoise` má hodnoty sústredené blízko `0.5`, takže
     `F = smoothstep(0.36, 0.68, …)` má nízky kontrast a farby
     `terrain_gold [0.30, 0.255, 0.065]` / `meadow_gold [0.38, 0.32, 0.075]`
     majú takmer rovnakú luminanciu ako pôvodná olivová tráva.
3. **Prečo okraj štrkového chodníka stále pôsobí ako ostrá stuha (`edge ratio
   0.9948` vs `≥1.25`):**
   - V `meadow_trail_v16.py` r. 147 sa efektívny okraj `Eσ(s)` posunul dovnútra
     od fyzickej hrany `V07_TRAIL_MESH` (`h(s)`) len o `0.02–0.06 m` (2–6 cm),
      pričom na samotnom `MAT_V16_V07_GRAVEL` sa trávnatý substrát `Grass`
     začínal až od `d = 0.12 m` (teda až mimo telesa `V07_TRAIL_MESH`), takže
     celá fyzická šírka `V07_TRAIL_MESH` s 15 mm schodíkom zostala vykreslená
     ako štrk/hlina s ostrou hranou.
   - Navyše trsy krajníc mali výšku len `0.06–0.14 m` (polomer `0.075 m`) a
     podmienka `if gravel.hits(box): reject` + `d >= 0.022 m` ich odsunula
     ďalej od okraja štrku, takže pri 960×540 neprekryli okraj chodníka.

### Autorizácia jedinej vyhradenej korekcie `c01` (`01_correction_02.md`, 01/03)

Podľa plánu §5 a AP Finite Convergence autorizujem jednu cielenú korekciu
`c01` v tej istej zdravej Worker session (`01/03`, `current-worker-session`,
`Bounded Correction Worker`), ktorá zachová zmrazený `candidate_exterior_v16.blend`
aj `B_v16_960.png` a vytvorí `source/meadow_trail_v16_c01.{py,json}`,
`checkpoints/candidate_exterior_v16_c01.blend`, `renders/C_v16_c01_960.png` a
`01_report_02.md`.

## 2026-11-19 — rekonciliácia korekcie 01/03 (`C_v16_c01_960.png`) a eskalácia na Cooperatora

Report `01_report_02.md` bol prevzatý a overený (114 riadkov, SHA-256
`19dd5108c3b6cc4988ac24430a531c2ebacfda8343843629cbd2be71ac042dbf`, začína
presne `### Report for ORCHESTRATOR_CHAT` na riadku 1).
Overené artefakty z výmeny 01/03 (`work/v16/meadow_trail_01/`):
- `checkpoints/candidate_exterior_v16_c01.blend` — 446 287 190 B, SHA-256
  `2b39665905a65db860bc8f21159fbfb7e93ee3e39ab8051b12b15a64b07b8214`
- `renders/C_v16_c01_960.png` — 1 000 628 B, SHA-256
  `62f4f5afc34f246f125c4da7d22bdb331fde96ac7713b59e6d31420aa196b317`
- `source/meadow_trail_v16_c01.py` — SHA-256
  `4e1645e6f7b74ba1295ff357208c842fc4c6fdfd3e0c7812a496a4baa565fd11`
- `source/meadow_trail_v16_c01.json` — SHA-256
  `0af5b0a9ff1cd6bf9707d408787398e0daeb7ec58ab609bd256346035091a2a9`
- Predchádzajúci kandidát V16 B (`5d82ecf4…`), jeho render `B_v16_960.png`
  (`92f865ec…`), východisková scéna V15 C (`15870b19…`), čistý projektový
  working tree a Michalovo GUI PID 2452 (`start_ticks 12233`) sú nezmenené.
- Technické kontroly `c01` prešli: idempotencia, fresh-input replay a cold
  reopen sa zhodujú na sémantickom hashi
  `17f7d56416a0236e88cef8258b8c29e208f5cba5a050ef89771db9b7d3fc22c9`;
  87 zabalených obrázkov a všetkých 6 `_working_branch` kontrol prešlo;
  2 159 trsov krajníc (2 056 na teréne + 103 na hornej ploche štrku, 153 120
  bazálnych vrcholov) prešlo kontrolou podpory (`exposure ≤ -2.000 mm`,
  `burial ≤ 9.020 mm`); natívny render trval 126,65 s (peak RSS 4,49 GiB,
  min. dostupná RAM 15,46 GiB).

### Priama vizuálna kontrola `C_v16_c01_960.png` vs `B_v16_960.png`

- **`C_v16_c01_960.png` (`c01`):**
  - Dosiahol 11 z 13 numerických kritérií (vrátane `Front high-pass RMS 6.643 ≥ 6.3`,
    `Left/Right slope std 20.966 / 21.631`, tieňa lesa `29.990 / 19.279` a
    tieňa chaty `0.6337`) a v strednej/hornej časti chodníka zjemnil okraj
    (doplnková znamienková šírka prechodu `4.234 px` = `1.66x` V15 C).
  - Avšak **18 m / 3 m zlatisto-žlté fľaky prestrelili**: `Front meadow luma std
    16.339 > 16.0`, zlatá frakcia vyskočila na `96.93 %` v popredí a `62.54 %`
    na ľavom svahu, čo pri priamom pohľade vytvára neprirodzený žlto-zelený
    fľakatý („kamuflážny“) vzor na svahoch namiesto prirodzeného bočného
    slnečného lesku terénnych vĺn ako na `01.png`.
- **`B_v16_960.png` (01/02):**
  - Má oveľa prirodzenejšiu, nenásilnú farebnosť svahov a lúky bez žltých
    fľakov, pričom už obsahuje opravený tieň lesa (`29.095`), teplé oblaky,
    kontrastný tieň chaty (`0.6481`) a overené `0.465–0.733 m` krajnice s
    2 903 podporovanými trsmi.

Rozpočet jednej automatickej korekcie v celku V16 je vyčerpaný
(`Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`). Predkladám Michalovi
porovnanie **V16 B** a **V16 c01** na výber východiskového kandidáta a spôsob
uzavretia celku V16.

## 2026-11-19 — Michalovo rozhodnutie a uzavretie celku V16 (`01_closure.md`)

Michal po porovnaní výsledkov vybral: **„Uzavrieť V16 · vybrať V16 B (Recommended)“**.
- Východiskovým kandidátom pre ďalšiu prácu je **V16 B**
  (`work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend`,
  SHA-256 `5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1`,
  render `B_v16_960.png` SHA-256
  `92f865ec1e04190a9d28aed213a93f85a2eac58f32ce2a2961872ddc2f0dece6`).
- Kontrastnejší kandidát **V16 c01** (`2b396659…`, render `C_v16_c01_960.png`
  `62f4f5af…`) zostáva zachovaný ako porovnávacia evidencia.
- Všetky oprávnenia Workerov (`01/01`, `01/02`, `01/03`) expirovali, žiadny
  natívny Blender proces Workera nebeží, projektový repozitár je čistý na
  `78534bd46020bb2bfc97eef69b05e583cba5a5e5` s AP pinom
  `d7023cf037f6d17885c3ede5c04812c61640da50`.
- Zapisujem `01_closure.md` a tieto prevádzkové poznámky `00_notes.md` pri
  uzavretí celku zamŕzajú.
