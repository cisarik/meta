# Prostredie v04 — technické a obrazové porovnanie

Kandidát pre vizuálne posúdenie; celok zostáva otvorený. Dôkazy vytvoril rovnaký Worker, ktorý zmenu implementoval. Architektonické preverenie ani stavebná použiteľnosť sa netvrdia.

- [Pred: zachovaná v03](../renders/before.png)
- [Po: prostredie v04](../renders/after.png)
- [Výrezy v pôvodnej mierke](../renders/landscape_details.png)
- [Úplné merania a kontrolné súčty](../renders/render_metadata.json)

## Scéna a zachovanie

`blender/kysucka_chata_mcp_v04.blend`, SHA-256 `c19b37cf75037969d2608677d276880d46e9ae7afc31aa11a78c340241fa3d43`, 58,660,058 B (55.94 MiB). V živej relácii Blender 5.2.3 LTS je uložená, čistá a bez renderovacej úlohy.

Kamera zostala v polohe [21.5, -10.0, 1.25], so zameraním podľa pôvodnej v03, 35 mm, snímačom 36 mm, shift_y 0.105 a dosahom 500 m. Dom, strecha, otvory, interiér, komín/krb, sklo, chodník, schody, stĺpiky osvetlenia, svet a svetlá sa nezmenili. Materiály/UV/geometriu dreva a plota zachováva v03. Pôvodných 263 rastlinných náhrad je iba skrytých; ostatných 393 objektov zostáva zachovaných. Geometria terénu a záhona je rovnaká, zmenené sú iba dve povolené priradenia shaderov.

Predchádzajúce uloženie pohľadu bolo zachované v `work/mcp-v04-before.blend` s hashom `09a31edfae067b11969c197b9e89b2e2dee35172daa999d99eb7e73695aa8973`. Grant 01/03 osobitne povolil obnoviť sledovanú v03 na pôvodný hash `360c99a107f9bd819e273274e3cd449a5b7666a27fc69c6ee3a51dfa7e120248`. Neskoršie uloženia smerovali výlučne do v04.

## Modely, pôvod a skladba

Sedem normalizovaných knižníc obsahuje 16 master kolekcií. Prijaté archívy boli overené SHA-256; 20 súborov Poly Haven bolo overených publikovanou veľkosťou a MD5, potom SHA-256. Mapy a knižnice sú dostupné offline; 79 použitých súborových obrázkov je zabalených. Presný pôvod, rozmery, zásahy, licencie a súčty každého zachovaného súboru sú v projektovom `assets/ASSET_MANIFEST.md` a v metadátach vyššie.

| Podklad | Autor | Licencia |
|---|---|---|
| [Realistic HD Norway spruce (3/43)](https://sketchfab.com/3d-models/realistic-hd-norway-spruce-343-bf500546e2874f9ea086ba6abb11357e) | PlantCatalog | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| [Realistic HD Black spruce (19/38)](https://sketchfab.com/3d-models/realistic-hd-black-spruce-1938-3232c3022f2947b7999de0941ede5653) | PlantCatalog | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| [Blossoming apple tree](https://sketchfab.com/3d-models/blossoming-apple-tree-7df0631398f443379fa4541e9efc2343) | Lassi Kaukonen (thesidekick) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| [Food Apple 01](https://polyhaven.com/a/food_apple_01) | Oliver Harries | [CC0](https://polyhaven.com/license) |
| [Grass Medium 01](https://polyhaven.com/a/grass_medium_01) | Rob Tuytel, Rico Cilliers | [CC0](https://polyhaven.com/license) |
| [Shrub 01](https://polyhaven.com/a/shrub_01) | Rico Cilliers | [CC0](https://polyhaven.com/license) |
| [Periwinkle Plant](https://polyhaven.com/a/periwinkle_plant) | Amal Kumar | [CC0](https://polyhaven.com/license) |

Čierny smrek Picea mariana je Michalom výslovne vybraný lesný podklad; nejde o tvrdenie o jeho pôvodnosti na Kysuciach. Pred rozmiestnením sa vykonal jeden skúšobný render: alfa ihličia/listov, OpenGL normály, zelené tónovanie, odstránený zemný lem jablone a jednotlivé rastliny boli vizuálne skontrolované. Rastliny boli na tejto pracovnej skúške zväčšené pre čitateľnosť shaderov; skutočné rozmery vlastní manifest.

Tri široké vrstvy kopcov a pravé nadviazanie vytvárajú terén v smere zamknutej kamery. Rozsah u presahuje oba okraje záberu. Les tvorí 1 200 zdieľaných sietí: 780 čiernych a 420 nórskych smrekov. Čierne smreky sú sústredené hlbšie; plnší okraj tvorí nórsky smrek. Minimálny odstup v rámci vrstvy je 2,20181 m. Úzke nepravidelné čistiny zostávajú medzi porastmi; konkrétne premietnuté body hrebeňov sú v metadátach.

Štyri mladé smreky používajú zúžený samostatný master pri ľavom a pravom okraji. Jabloň má 28 plodov s priemerom 6,5–9 cm na vybraných hnedých povrchoch vonkajšej koruny. Predná výsadba má 15 nízkych skupín kríkov, 24 trávových trsov a 12 kvetinových skupín (168 zdieľaných jednotlivých rastlín); pri trávniku/plote je 104 trsov (312 jednotlivých rastlín). Hlavný vstup a priestor lavičky ostávajú čitateľné.

Použili sa dva pracovné náhľady a jedna súvislá kompozičná korekcia: po prvom náhľade sa zmenil charakter bližšieho okraja lesa, jeho rozdelenie druhov a hustota rastlinných trsov. Kamera a existujúce svetlá sa nemenili.

## Overenie a výkon

| Kontrola | Výsledok |
|---|---|
| Unikátne zdrojové trojuholníky | 429,202; cieľ < 1,5 M, limit < 3 M |
| Vyhodnotené unikátne trojuholníky | 446,545 |
| Súčet po zohľadnení všetkých umiestnení | 27,828,482; siete zostávajú zdieľané |
| Objekty scény / databázy | 2 373 / 2 389 vrátane 16 nezobrazených masterov |
| Siete / materiály / súborové obrázky | 668 / 53 / 79 |
| Odhad dekódovaných obrázkov | 369,425,088 B |
| Fyzická RAM | 8 GiB |
| Najväčšie vzorkované RSS počas renderu | 1,338,474,496 B; vzorkovanie každé 2 s |
| Životné maximum RSS procesu po rendri | 1,530,462,208 B; odlišná veličina od vzorkovaného maxima |
| Pamäť hlásená rendererom | 611M |
| Finálny render | 218.994 s, Cycles CPU, 8 vlákien |
| Zachovanie dát v03 | najväčšia číselná odchýlka 0.0 |
| Cold otvorenie oproti živému stavu | odchýlka 0 |
| Zdrojový replay: geometria a hranice | 4.768371582e-07 m ≤ 1e-5 m |
| Zdrojový replay: rotácia | 2.384185956e-07 rad ≤ 1e-6 rad |
| Zdrojový replay: mierka | 1.168768247e-07 ≤ 1e-6 |
| Opakované apply_v04 po cold otvorení | odchýlka 0, počty dát sa nezmenili |
| Ukotvenie plodov | najväčšia odchýlka konca stopky 0.01498 m ≤ 0,02 m |
| Korene lesa | približne 0,012 m pod vlastným povrchom; bez plávajúcich koreňov |

Všetkých šesť samostatných záverečných kontrol skončilo kódom 0. Globálny RNG je nezmenený. Chladné otvorenie aj zdrojové zostavenie používajú `--disable-autoexec` v samostatných procesoch. Najväčší súbor kandidáta je pod 90 MiB. Nebola pridaná závislosť, runtime, doplnok ani sieťový cieľ mimo grantu.

Porovnanie shaderov používa typy uzlov, identifikátory socketov a väzby, nie lokalizované názvy. Skryté objekty sa porovnávajú z uložených TRS a matíc rodičov, pretože Blender po cold otvorení nemusí vyhodnotiť ich runtime matrix_world. Hranice sú odvodené z vrcholov sietí a uložených transformácií. Neaktívna Subsurface Scale sa neporovnáva pri nulovej váhe podpovrchového rozptylu. Aktívny Filter Width starých drevených shaderov je v zdrojovom generátore explicitne zachovaný na hodnote 1,0 a zostáva súčasťou kontroly.

Ukladanie pôvodne vynechalo nezobrazené master kolekcie a dva už nepoužívané materiály podkladu. Doplnilo sa ich trvalé uchovanie cez fake user; následné cold/replay kontroly prešli. Viditeľná geometria ani render sa touto opravou nezmenili.

## Obrazové dôkazy a obmedzenia

Pred/po majú zhodne 1448 × 1086, 100 %, 96 vzoriek, OIDN, snímku/seed 0, AgX/None, expozíciu 0 a gamma 1. Pred je byte-identická prijatá v03 s hashom `3c77ef772bb5578aa54227df98615356cc301c9542fffe982071bed62b0d69d1`. Výrezy kopírujú pôvodné RGBA pixely bez prevzorkovania; presné hranice sú v metadátach.

Finálny obraz a všetky výrezy boli vizuálne prečítané. Charakter čierneho smreka na hornom okraji zostáva riedky a koruna skenovanej jablone otvorená; nejde o tvrdenie, že už zodpovedajú hustote referencie. Z 28 plodov má 13 stred v zábere a štyri nemajú geometricky zakrytý stredový lúč; ostatné sú zakryté alebo mimo záberu. Plody sa nezväčšovali kvôli viditeľnosti. Zachovaná sivá obloha a osvetlenie ovplyvňujú výsledný dojem. Subjektívne prijatie Michalom a prijatie Orchestratorom zatiaľ nie sú vykonané.

Masterov run-map sa mechanicky zosúladil s dodaným snapshotom; novšie stavy sa neprepisovali a nový stav celku sa nevymýšľal. Nebolo vykonané staging, commit ani publikovanie. `renders/render_metadata.json` je podľa Meta pravidiel ignorovaný a vyžaduje explicitné `git add -f` vykonané Cooperatorom.
