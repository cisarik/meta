# Poznámky orchestrátorky — V20 · Pivnica s dvoma vstupmi

Autor: ORCHESTRATOR tohto celku
Capability profile: Orchestrator
Orchestrator session scope: logical-whole
Development run identity: kysucka-moderna-chata-reference-visualization
Logical whole identity: kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20
Dátum otvorenia: 2026-11-24, Europe/Bratislava
Životný cyklus: prevádzkové poznámky tohto celku; historická evidencia, nie task authority; pri uzavretí zmraziť, prípadné čistenie a Git archiváciu v Meta vlastní COOPERATOR.

## 2026-11-24 — Continuation Bootstrap Stage 1 a revalidácia handoutu V20

Prevzala som celok **V20** (`kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20`) z provizórneho handoutu na deklarovanom lokátore `/home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20/00_handout.md` (10 676 B, SHA-256 `a3f9938d4c85bf7c566fdaffb7293c03eee6820a79bb71b8c9bb905a0d4cd625`). Otvorením celku sa tento handout zmrazuje. Bajtovo zhodnú kópiu v `/home/agile/meta/projects/kysucka_moderna_chata/00/19-pivnica/01_handout.md` (rovnaký SHA-256) nechávam nedotknutú ako Michalovo lokálne prichystanie (`unrelated-owner-work`).

Michal schválil V20 a pridal samostatný vonkajší vstup do prijatého B1 s futuristickým osvetlením. Výber celku je tým daný. Realizačný grant vydám až po plánovacom reporte a po schválení konkrétneho vizualizačného zásahu do dosky, sokla a terénu podľa rezu.

### 1. Priamo overený stav repozitárov, AP pinu a stanice

- **Projektový repozitár:** `/home/agile/Projects/kysucka_moderna_chata`, branch `main` (`main...origin/main`), HEAD `f600c7a8e69a23a029559872652302ac299c2aea`. Lokálny origin `/home/agile/backups/git/kysucka_moderna_chata.git` je na tom istom commite. Sledovaný working tree aj index sú čisté.
- **Verejný produktový `main`:** priamo cez GitHub API, `cisarik/kysucka_moderna_chata`, SHA `8218cb3a27a247cc73de940462d21f3bebc27f8a`. Spoločný predok s lokálnym HEAD je `e7a925b98a8a4ef6da16746746d4d96bca25a118`. Verejný `8218cb3a` leží na inej línii (`codex/readme-public-20261119`) a nie je predkom lokálneho HEAD. Autorita scén je v overených lokálnych súboroch; `work/` je ignorovaný.
- **AP submodule:** gitlink aj checkout `d7023cf037f6d17885c3ede5c04812c61640da50`. `./.ap/ap doctor` → `PASS`, variant `stable`. V `AGENTS.md` mimo riadeného bloku nie je deklarovaný AP upgrade ledger.
- **Meta:** `/home/agile/meta`, branch `main`, HEAD aj `origin/main` `ce9d740e8cbf9be96d301a2fe8388c08881eda9c`. Nesledované sú len uvedené prichystanie handoutu a tento priečinok V20.
- **Blender:** `/home/agile/Applications/Blender/blender` `5.3.0`, build hash `02f0899d78e3`. Živé GUI nebeží. Päť procesov `[blender] <defunct>` a nečinné wrappery `mcp-for-blender` som nespájala so scénou. Globálne preferencie `/home/agile/.config/blender/5.3/config/userpref.blend` majú SHA-256 `ae7a8626c3f41081ac7dde07f2ddcf2ab7d09c807a16ae2bdd5f6d233f88a9c0` pred sondou aj po nej. Dostupné RAM pri sondách bolo približne 20 GiB.
- **Izolovaná sonda:** dve samostatné relácie `--background --factory-startup --disable-autoexec` s `BLENDER_USER_CONFIG=/tmp/v20_stage1/config`. Súbory scén sa neukladali. Po sonde ostali tri pripnuté SHA-256 scén nezmenené.

### 2. Identita vstupných súborov

| Podklad | Overená cesta | Bajtov | SHA-256 |
|---|---|---:|---|
| Interiérový kandidát V19, východisko V20 | `work/v19/kysucka_chata_interier_pivnica_v19.blend` | 425 401 183 | `d9021ee49f63a6dc595214932485597b3b47186b6e26487065c87964dc5dcdf8` |
| Kanonický interiér pred povýšením | `blender/kysucka_chata_interier.blend` | 420 066 660 | `c607cb21fbdb289b49f05596004b403e7dd5f96a64e900ce42ed8485f6a30449` |
| Denný exteriér | `work/v18/recovery/kysucka_chata_exterier_doladeny.blend` | 435 436 722 | `5e8ada70e99c70a3be0a7eea9b18306b422e4ef3a141a63b51b237b7957e3a24` |
| Súbor obálky | `model/shared_envelope_v18.json` | 279 403 | `e58959a22b2d1879828fe87cff645ec3f7ed99a28ec12ae66bfce01c4f6045b8` |
| Agregát 289 objektov v súbore obálky | `aggregate_sha256` | — | `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50` |
| Priechod V19 | `work/v19/walk_clearance_v19.json` | 11 330 | `5cba280c8d164fcb7ec85eef85f4d70189364e24e07bd528505d3ba93f4a4f35` |
| Pôdorys prízemia V19 | `work/v19/podorys_prizemia_v19.svg` | 5 396 | `9e61f69a55a4bbf8111439c2140b1b02e2cef4b5e28c958f089f34f97ab59e61` |
| Pôdorys B1 V19 | `work/v19/podorys_b1_v19.svg` | 3 859 | `fd186e9e482b9b90387af5b5498167e9627a27d1c5d59977b77eda68a862d2b5` |
| Rez A–A V19 | `work/v19/rez_aa_v19.svg` | 3 505 | `24b4f8ab81e8583881aee979ead25ad622afbe75c778e51dabdc03875a9871eb` |
| Register náhrad obálky | `work/v19/slab_envelope_diff.json` | 131 536 | `aef9702d53f58638d6510732abc758598a94b6e7d006f1816e12ba955b03e837` |
| Izolované preferencie | `work/v12/profile_03/isolated_config/userpref.blend` | — | `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561` |

Súbor obálky má 289 objektov, osi `+X` od prístrešku k presklenému štítu, `+Y` od vstupu k severnej fasáde, `+Z` nahor, kóty dosky `+0,200 / +0,450 m` a podlahy `+0,451 m`. Register náhrad uvádza nezhodu agregátu `0` a skryté originály `BASE_slab`, `V10_FLOOR_oak`, `V11_TERRAIN_NEAR` a štyri priečky `PARTITION_proposed` až `.003`. V `walk_clearance_v19.json` je stav `PASS`, valec `0,700 × 2,100 m`, najmenšia hlásená bočná rezerva `0,015421 m`.

### 3. Zosúladenie svetových súradníc oboch vstupných scén

Obe scény sú `METRIC` so `scale_length = 1`. Interiér otvára snímku `181` na `Záber 07 | Obývačka a krb`. Exteriér otvára snímku `1` na `Záber 01 | Chata a údolie`.

Spoločné viditeľné svedecké objekty majú v oboch súboroch zhodný svetový posun aj svetový rám:

| Objekt | Svetový posun (m) | Svetový rám X, Y, Z (m) |
|---|---|---|
| `WALL_left_closed` | `(2,55; 4,20; 1,85)` | `2,40..2,70 × 0..8,40 × 0,45..3,25` |
| `D01_leaf` | `(7,875; −0,060; 1,600)` | `7,25..8,50 × −0,105..−0,015 × 0,45..2,75` |
| `WOOD_BAY_rack` | `(1,20; 0,55; 0,49)` | `0,25..2,15 × 0,05..1,05 × 0,45..0,53` |
| `GABLE_other_proposed` | `(0; 0; 0)` | `X = 2,40`, `Y 0..8,40`, `Z 3,25..7,45` |
| `WALL_front_0_0` | `(4,825; 0,15; 0,90)` | `2,40..7,25 × 0..0,30 × 0,45..1,35` |
| `WALL_rear_0_0` | `(8,40; 8,25; 0,90)` | `2,40..14,40 × 8,10..8,40 × 0,45..1,35` |
| `V10_FLOOR_oak` | `(0; 0; 0)` | `2,46..14,40 × 0..8,40 × 0,451` |
| `V11_TERRAIN_NEAR` | `(0; 0; 0)` | `−30,25..42,10 × −14,00..60,45 × −0,992..10,522`, 34 263 vrcholov |

`BASE_slab` v exteriéri a viditeľná `BASE_slab_V19_STUDY` v interiéri majú posun `(7,20; 4,20; 0,325)` a rám `0..14,40 × 0..8,40 × 0,20..0,45`. Skrytý originál `BASE_slab` v interiéri má v `location` uložené `(7,20; 4,20; 0,325)`. Kým má `hide_viewport` zapnuté, surové `matrix_world` bez obnovy view layer číta identitu a lokálny rám kocky. Po dočasnom odkrytí v pamäti a `view_layer.update()` je svetový rám zhodný s exteriérom. Súbor sa neukladal. Skrytý objekt preto nie je posunutý; pre V20 je smerodajná viditeľná študijná doska a exteriérový originál.

`V11_TERRAIN_NEAR` aj `V11_TERRAIN_NEAR_V19_STUDY` majú v boxoch `X −8..0`, `Y −2..9` (459 vrcholov), `X −3..0`, `Y 4..9` (84) a `X −1..1`, `Y 0..8,4` (100) výšku presne `−0,055 m`. Západná kamenná stena prijatého B1 je `V19_B1_West_Stone` s rámom `X 2,70..2,90`, `Y 2,48..5,70`, `Z −2,25..0,20`. Severný kameň `V19_B1_North_Stone` je `Y 5,50..5,70`. Hrubý objem teda končí na `Y 5,70 m`. Starý nepostavený otvor Variant B na `Y 5,940–6,980 m` leží mimo tohto objemu.

Dolná vnútorná podesta v `walk_clearance_v19.json` prechádza bodmi `(3,80; 2,925; −2,25)` a `(3,45; 2,925; −2,25)`, potom na sever k dverám skladu. Presklené krídlo v scéne siaha v otvorenej polohe približne po `Y 4,56` pri `X 3,90`. Západné ostenie dverí skladu je `V19_Store_Jamb_L` na `X 2,92..2,95`, `Y 3,46..3,60`.

### Handout Revalidation Record

```text
Handout revalidation: projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20/00_handout.md
Received handout status: provisional
Revalidated against: local project commit f600c7a8e69a23a029559872652302ac299c2aea; local origin /home/agile/backups/git/kysucka_moderna_chata.git at the same commit; directly observed GitHub main cisarik/kysucka_moderna_chata 8218cb3a27a247cc73de940462d21f3bebc27f8a with merge-base e7a925b98a8a4ef6da16746746d4d96bca25a118; AP pin d7023cf037f6d17885c3ede5c04812c61640da50 (ap doctor PASS, variant stable); Meta commit ce9d740e8cbf9be96d301a2fe8388c08881eda9c equal to origin/main; interior candidate work/v19/kysucka_chata_interier_pivnica_v19.blend d9021ee49f63a6dc595214932485597b3b47186b6e26487065c87964dc5dcdf8; predecessor blender/kysucka_chata_interier.blend c607cb21fbdb289b49f05596004b403e7dd5f96a64e900ce42ed8485f6a30449; exterior work/v18/recovery/kysucka_chata_exterier_doladeny.blend 5e8ada70e99c70a3be0a7eea9b18306b422e4ef3a141a63b51b237b7957e3a24; model/shared_envelope_v18.json e58959a22b2d1879828fe87cff645ec3f7ed99a28ec12ae66bfce01c4f6045b8 with 289-object aggregate 8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50; work/v19/walk_clearance_v19.json 5cba280c8d164fcb7ec85eef85f4d70189364e24e07bd528505d3ba93f4a4f35; podorys_prizemia_v19.svg 9e61f69a55a4bbf8111439c2140b1b02e2cef4b5e28c958f089f34f97ab59e61; podorys_b1_v19.svg fd186e9e482b9b90387af5b5498167e9627a27d1c5d59977b77eda68a862d2b5; rez_aa_v19.svg 24b4f8ab81e8583881aee979ead25ad622afbe75c778e51dabdc03875a9871eb; slab_envelope_diff.json aef9702d53f58638d6510732abc758598a94b6e7d006f1816e12ba955b03e837
Usable facts: both input scenes are METRIC with unit scale 1 and share the envelope axes; witness walls, D01, wood rack, floor and near terrain match between the V19 interior candidate and the V18 day exterior; visible BASE_slab_V19_STUDY matches exterior BASE_slab at translation (7.2, 4.2, 0.325) and bounds X 0..14.4, Y 0..8.4, Z 0.2..0.45; hidden interior BASE_slab stores the same location and matches after a view-layer update, while a stale identity matrix_world appears only before that update; west grade samples of V11_TERRAIN_NEAR and its V19 study copy are exactly Z -0.055 m in the three sampled boxes; V19_B1_West_Stone ends at Y 5.70 m, so the cited unbuilt Variant B opening Y 5.940–6.980 m falls outside the accepted gross volume; walk file reports PASS and minimum side margin 0.015421 m; no live Blender GUI was attached; global userpref ae7a8626c3f41081ac7dde07f2ddcf2ab7d09c807a16ae2bdd5f6d233f88a9c0 was unchanged
Stale facts and corrections: handout phrase "Priložená večerná vizualizácia" -> no image file is present in the V20 handout directory or in projects/kysucka_moderna_chata/00/19-pivnica/; the written material and light specification remains the reference
Not revalidated: unbuilt Variant B slab cut 6.552 m² and 34.17 m detour, cited from the V19 planning report and not reconstructed in a saved scene; orchard-tree world position; ground meshes other than V11_TERRAIN_NEAR along a future stair polyline; cause of the B1 ceiling seam; interactive viewport frame rate
Handout disposition: adopted-with-corrections
```

## 2026-11-24 — Vydanie plánovacieho promptu `01_planning_00.md` (01/01)

Otváram jeden plánovací cyklus v natívnom Plan Mode (`01/01`, `fresh-worker-session`, `Native planning mode: required`, manuálne doručenie). Plánovač v Plan Mode report nezapisuje. Vlastníčkou uloženia je Orchestrátorka: kompletný anglický report príde vo výstupe relácie a uložím ho na `01_report_00.md`. Realizačný grant vydám samostatne až po prijatí riešenia a po schválení konkrétneho zásahu do dosky, sokla a terénu.

Odporúčanie pre Michala: High, približne 250k tokenov kontextu. Model vyberá Michal. Pomenované riziko je priestorové napojenie nového zostupu na prijaté B1, oba dverné oblúky, prvý regál a viditeľný západný sokel.

## 2026-11-25 — Rekonciliácia `01_report_00.md` (01/01, BLOCKED pred plánom) a vydanie `02_planning_00.md` (02/01)

Terminálny záznam výmeny `01/01` je `/home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20/01_report_00.md` (30 riadkov, SHA-256 `40c55fdb6b27f8d9238ab81e3650044aa99802c07eece54dd68e4fdc0bce4121`). Začína presne `### Report for ORCHESTRATOR_CHAT`, súradnice sú `01/01`, `Status: BLOCKED`. Príčina: grant žiadal natívny Plan Mode a prijímací klient bol v Default mode. Scény sa neotvorili, plán nevznikol. Prompt `01_planning_00.md` ostáva SHA-256 `e397c38ed4c90a9e90bbcc980d2a588ad8e0c6ec0ec7a6c02e3af72a8e7f42b2`. Tento pár neprepisujem.

Neskoršie vloženie toho istého `01_planning_00.md` do inej relácie, už v Plan Mode, vrátilo odmietnutie spotrebovaných súradníc. Ten text nie je druhý výsledok výmeny `01/01` a neukladám ho ako report. Relácia `01` bola konkrétna Default-mode relácia a skončila. Ďalší grant preto ide do novej relácie.

Plánovací cyklus sa nespotreboval. Opravený úvodný grant je `02_planning_00.md`: `Worker session ordinal: 02`, `Worker exchange ordinal: 01`, `Worker session target: fresh-worker-session`, `Native planning mode: required`, `Planning cycle: initial`, `Prior planning report: 01_report_00.md`, `Automatic targeted revisions used: 0`. Report uložím ja na `02_report_00.md`. Piny projektu, Meta, AP, scén aj globálnych preferencií som pred vydaním znovu čítala a sedia. Živé GUI Blenderu nebeží.

Odporúčanie ostáva High. Michal vloží celý `02_planning_00.md` do novej relácie Plannera až po zapnutí Plan Mode. Opätovné vloženie `01_planning_00.md` nie je tento grant.

## 2026-11-25 — Rekonciliácia `02_report_00.md` (02/01, druhý BLOCKED na tom istom režime)

Terminálny záznam výmeny `02/01` je `02_report_00.md`, SHA-256 `c7efe146ff52c926ce1345908f9cd590c4d5eb883ea98817b3b1c431bca1b15c`. Text doručený v tomto rozhovore je s tým súborom zhodný. Prompt `02_planning_00.md` ostáva SHA-256 `8bdc39829c5a0898709dab8058957751e54adb6b610fe8349c96ff928ec72862`. Pár neprepisujem.

`Status: BLOCKED`. Klient opäť hlásil Default mode, scény sa neotvorili a plán nevznikol. Plánovací cyklus ostáva nespotrebovaný. Súradnice `02/01` sú spotrebované. Je to druhý po sebe idúci terminálny `BLOCKED` na nezmenenej príčine: grant žiada natívny Plan Mode a cieľový klient je v Default mode. `Closure decision required: identify-missing-evidence`.

Chýbajúci dôkaz je overený natívny Plan Mode v cieľovej relácii ešte pred vydaním ďalšieho promptu. Ďalší čerstvý grant teraz nevydávam. Tretie opakovanie toho istého vloženia by nebolo nový dôkaz. Keď Michal potvrdí, že nová relácia je v režime Plan, vydám `03/01` s `Planning cycle: initial` a predchodcom `02_report_00.md`.

## 2026-11-25 — Michal potvrdil Plan Mode a vydanie `03_planning_00.md` (03/01)

Michal v tomto rozhovore výslovne potvrdil, že cieľová relácia je v Plan Mode, a požiadal o vydanie plánu. Beriem to ako Cooperatorom dodaný chýbajúci dôkaz o režime doručenia. Samotný klient Plannera som priamo nevidela.

Piny pred vydaním sedia: projekt `f600c7a8e69a23a029559872652302ac299c2aea`, AP `d7023cf037f6d17885c3ede5c04812c61640da50`, Meta `ce9d740e8cbf9be96d301a2fe8388c08881eda9c`, obe scény aj globálne preferencie `ae7a8626c3f41081ac7dde07f2ddcf2ab7d09c807a16ae2bdd5f6d233f88a9c0`. Živé GUI Blenderu nebeží. Dostupné RAM je približne 20 GiB.

Vydávam `03_planning_00.md`: `03/01`, `fresh-worker-session`, `Native planning mode: required`, `Planning cycle: initial`, `Prior planning report: 02_report_00.md`, `Automatic targeted revisions used: 0`. Report uložím na `03_report_00.md`. Súbory `01_*` a `02_*` ostávajú spotrebované.

## 2026-11-25 — Rekonciliácia `03_report_00.md` (03/01, BLOCKED na živom GUI) a vydanie `03_planning_01.md` (03/02)

Terminálny záznam `03/01` je `03_report_00.md`, SHA-256 `4942d1762ab9aa9cb9cc48f910f703bddfc72e358121191e06875b924ff55511`. Text z tohto rozhovoru som doň uložila. Prompt `03_planning_00.md` ostáva SHA-256 `b5d53fe84af1deadff01e63753a2276f94a8aa17866467e2ad589b3cba631b7c`. Plan Mode v tejto relácii bol aktívny. Zastavenie spôsobila moja brána: živé GUI `/home/agile/Applications/Blender/blender`, PID `96634`, používateľ `agile`, stav `SNsl`, štart `2026-11-25 08:48:32`, pripojenie na `wayland-1`. Scény sa neotvorili. Plánovací cyklus ostáva nespotrebovaný.

Pri prevzatí reportu PID `96634` stále beží. Je to Michalova otvorená práca. Neukončujem ju a nežiadam jej zatvorenie. Ďalší grant ide do tej istej Plan Mode relácie ako `03/02`, `current-worker-session`. Izolovaná headless sonda smie bežať vedľa GUI a nesmie sa ho dotknúť. Súbor je `03_planning_01.md`, report uložím na `03_report_01.md`.

## 2026-11-25 — Plán z `03/02` je zmrazený, štandardný report chýba

Súbor `03_report_01.md` má 298 riadkov a SHA-256 `9c3a1fbbed6af812f02d68b0ee7e4ab4de860c0643988bcb8812eecf15bca118`. Je to rozhodovací plán Hypotézy 2, nie terminálny report: prvý riadok je nadpis plánu a pole `Status` v ňom nie je. Súbor neprepisujem. Prompt `03_planning_01.md` má SHA-256 `f1598032497eacba9c5084b7cc5352974d67202b7a53ded9eb90d1a9826ced33`.

Priamo som overila, že obe vstupné scény, kanonický interiér aj globálne preferencie majú nezmenené SHA-256, projekt je na `f600c7a8e69a23a029559872652302ac299c2aea`, dočasný adresár sondy chýba a PID `96634` stále beží. Plán tým nie je prijatý a realizačný grant nevydávam. Dokončovací grant `03/03` je `03_completion_02.md`, `Native planning mode: not-used`, iba na vyhotovenie štandardného reportu do `03_report_02.md`.

## 2026-11-25 — `03_report_02.md` je bajtová kópia plánu

`03_report_02.md` má SHA-256 `9c3a1fbbed6af812f02d68b0ee7e4ab4de860c0643988bcb8812eecf15bca118`, zhodný s `03_report_01.md`, 35 450 bajtov. Prvý riadok je nadpis plánu. Súradnice `03/03`, hlavička `### Report for ORCHESTRATOR_CHAT` ani `Status` v ňom nie sú. Nie je to terminálny report dokončovacej výmeny a plán ním neprijímam. Súbor nechávam ako kópiu, zmrazený plán neprepisujem. Ďalší grant nevydávam, kým cieľová relácia nie je mimo Plan Mode.

## 2026-11-25 11:31 — nové hlásenie bez nového súboru

Michal znova oznámil, že report je vygenerovaný. V stope V20 ani v okolitých textových súboroch od `03_report_02.md` (10:44, rovnaký SHA ako plán) nepribudol žiadny nový report. Posledný súbor ostáva táto kópia. Termínálny report `03/03` stále chýba.

## 2026-11-25 — Prijatie reportu `03/03` a schválenie výrezu H2

`03_report_02.md` je teraz terminálny report, SHA-256 `a9e4e7b3381bbbf2918da8261e3bbce440b7e582772f92e49d907a658ca1c952`, súradnice `03/03`, `Status: PASS`, `Phase-qualified result: not-applicable`, `Planning cycle effect: none`. Zmrazený plán `03_report_01.md` ostáva `9c3a1fbbed6af812f02d68b0ee7e4ab4de860c0643988bcb8812eecf15bca118`. Michalova kópia plánu je `x_03_report_02.md` s rovnakým odtlačkom. Rodičovské scény aj kanonický interiér majú nezmenené SHA-256. PID `96634` stále beží.

Prijímam plán a schvaľujem výrez Hypotézy 2: doska `Y 4,305–5,725` po `X 1,040`, kamenný otvor a terénny výrez podľa `03_report_01.md`. Hypotézu 1 nerealizujem. Vydávam `03_implementation_03.md` ako `03/04`, `current-worker-session`, `Native planning mode: not-used`, `Implementation authority: explicit`. Report zapíše Worker do `03_report_03.md`.

## 2026-11-25 — Realizácia H2 je technicky PASS, Michal odmieta levitujúcu dosku

`03_report_03.md` má SHA-256 `6610ed4db1de002fddbb72f3069c74bda7e57e5f2030c762dfc697d0494ac9e8`, súradnice `03/04`, `Status: PASS`, `Phase-qualified result: implementation-PASS`. Kandidáti sedia: interiér `7114bd8e946180db565d475c88ed5ed2b48c51628c63199ecf382c3c7f7867ed`, exteriér `9d5f9399e266783688bb067219cb7e06e76163d2a554569528b5e271a71c6d6e`. Rodičia sú nezmenení. PID `96634` stále beží.

Michal na záberoch vidí chatu vo vzduchu. Chce, aby pivnica bola čitateľná na celej chate, kamenným základom okolo celého obvodu. Je to jeho nové vizuálne rozhodnutie a mení zachovanú prázdnu medzeru pod doskou. Technický výsledok H2 ostáva základom. Vydávam korekciu `03_implementation_04.md`, výmena `03/05`, nové súbory `*_v20_zaklad.blend`. Pôvodné kandidáty H2 sa neprepisujú.

## 2026-11-25 — Čerstvý Worker namiesto pokazenej relácie 03

Relácia, ktorá mala vložiť `03_implementation_04.md`, nepokračuje. Ten súbor nie je autorita pre novú reláciu. V `work/v20/foundation/` ostal nedokončený pokus: meranie, štyri before PNG a skripty, bez súborov `*_zaklad.blend`. Kandidáti H2 majú stále SHA-256 `9d5f9399…` a `7114bd8e…`. PID `96634` beží. Vydávam `04_implementation_00.md` pre `fresh-worker-session`, súradnice `04/01`, `Native planning mode: not-used`. Report je `04_report_00.md`.

## 2026-11-25 — Základ je PASS, Michal chce ešte chodník od vchodu

`04_report_00.md` má SHA-256 `549f2d46cb9b66123dbd0b14647934526274f38d501302e1869142b4302ad243`, súradnice `04/01`, `Status: PASS`. Zaklad súbory sedia: exteriér `394a818c…`, interiér `e9458c7a…`. Kameň je na západnom, severnom aj južnom zábere. Chodník od hlavného vchodu k schodisku pivnice na záberoch nie je; pred dverami ostáva len pôvodný rovný nástup a pivnica ústi do trávy.

Michal chce z exteriéru vidieť kamenný základ okolo chaty a kreatívny chodník od vchodu do pivnice. Základ nechávam. Vydávam `05_implementation_00.md`, čerstvá relácia `05/01`, Plan Mode vypnutý. Nové súbory sú `*_v20_chodnik.blend`.

## 2026-11-25 — Štyri svetové strany v Meta

`05_report_00.md` má SHA-256 `549f2d46cb9b66123dbd0b14647934526274f38d501302e1869142b4302ad243`, súradnice `05/01`, `Status: PASS`. Chodník je v oboch kandidátoch. Exteriér `2121f6f4…` som po východnom zábere znova overila, súbor sa neukladal. Preferencie ostali `ae7a8626…`.

Archív je `renders/2026-11-25_svetove-strany/`: `zapad.png` `6dbe739f…`, `sever.png` `2995a61e…`, `juh.png` `b638d07c…`, `vychod.png` `0d919448…`. Západ, sever a juh sú dôkazové snímky z reportu. Východ je nový záber z `(33,4; 4,2; 5,1)` na stred chaty, 37 mm, 1440×810, 96 vzoriek, CPU. Git commit nerobím.

## 2026-11-25 — Uzávierka celku

Michal požiadal dokončiť posledné body, prípadný finálny dotyk a `01_closure.md` pre Master. Novú scénu už nespúšťam. Do archívu svetových strán pribúda `spojenie.png`, SHA-256 `180e3ac82063d050e57be871869644a369c2f6e14ff89b948046b9a320ee1510`, pohľad od vchodu po schodisko. Drobnosti na okraji trávy, `15 mm` schod na prahu a tenký tieň pod fasciou sú v uzávierke ako `FT-V20-01` až `FT-V20-03`, nie ako otvorený grant.

Vydávam `01_closure.md`. Celok V20 je uzavretý signálom `CELOK UZAVRETÝ ORCHESTRÁTOROM`. Tieto poznámky sa tým zmrazujú. Git archiváciu v Meta vlastní Michal. PID `96634` pri uzávierke ešte bežal a ostáva jeho práca.
