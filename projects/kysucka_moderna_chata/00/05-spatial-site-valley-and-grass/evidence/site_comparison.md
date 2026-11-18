# Priestorový pozemok, údolie, plot a tráva — v05

Kandidát `blender/kysucka_chata_mcp_v05.blend` obsahuje súvislý horský terén,
uzavretú záhradu s bránkou, krátky trávnik a vyššiu lúku. Je pripravený na tvoje
vizuálne posúdenie, Michal. Overenie vykonala tá istá Worker relácia (E2);
nejde o nezávislé prijatie ani zameranie skutočného pozemku.

## Pohľady

- [Pred v04](../renders/before.png) a [po v05](../renders/after.png): čerstvé natívne rendery 1448 × 1086 s rovnakou C1, svetlom a profilom.
- [Celý pozemok](../renders/site_overview.png): záhrada, pokračovanie plota a bránka pri chodníku.
- [Pohľad z interiéru do údolia](../renders/valley_from_inside.png): pôvodné sklo zostáva zachované a vzdialený obraz rozmazáva.
- [Štyri orbitálne pohľady](../renders/orbit_sheet.png): natívne dlaždice 724 × 543, bez preškálovania.
- [Porovnanie a detaily trávy](../renders/grass_details.png): horné výrezy pred/po sú `[0,770,1024,1086]`, dolné detaily `[0,0,1024,768]`, všetky 1 : 1.

## Priestor a zachovanie

Terén pokrýva `[-260,320] × [-220,260] m`, s uzavretým spodkom v −90 m.
Po súradnicovom zvarení má 129 279 hrán, každú s dvoma susednými plochami;
normály na šve majú minimálny skalárny súčin 0.999999613.
V chránenej terase zostalo presne 126 pôvodných vrcholov s odchýlkou 0,0 m.
Číslo 459 v zadaní sa meraním nepotvrdilo. Pôvodné súradnice a indexy sú zachované.
Kontrola 2 373 pôvodných objektov, UV, materiálov, sveta a svetiel nenašla
nepovolenú zmenu. Seed až v04, referencia, modelové knižnice a staršie generátory
zostali nezmenené podľa SHA-256.

Záhrada má 810,910 m² a obálku 34,70 × 25,12 m. Pôvodných 26 kolov a dve
priečky zostalo zachovaných. Doplnených je 286 kolov vrátane bránových a 100
priečok vrátane bránky, kovanie a štyri nadväzujúce betónové dosky. Rohové
podpery nie sú zdvojené. Spojenie priečok s kolmi je overené, maximálna
vzdialenosť osi konca od podpery je 20,01 mm.

Údolie pozdĺž +X klesá približne na −24,05 m pri X = 120 m a za ním stúpa
protiľahlý hrebeň. Osový lúč z interiéru prechádza `G01_lower_glass` a až po
X = 220 m nepretína terén ani pevnú prekážku. Tento konečný lúč dopĺňa
natívny interiérový render; nedokazuje priehľadnosť každej časti zorného poľa.
Približne 528,12 m² voľného trávnika zostáva po maskách a rozšírených korunách
stromov (vzorkovanie 0,20 m). Ďalší ovocný strom sa nepridal.

## Vegetácia a podklad

Pribudlo 1 200 zdieľaných smrekov (780 čiernych a 420 obyčajných), v sektoroch
300/350/300/250. Od záhrady majú odstup aspoň 8 m; otvorený údolný koridor
zostáva voľný. Spolu 2 402 starých/nových stromov je zvislo osadených na rovnaký
triangulovaný povrch. Chyba pätiek je najviac 0,009 mm.

Trávnik tvoria 4–10 cm procedurálne listy v 5 332 záplatách a 17 oblastiach
8 × 8 m. Lúka obsahuje 8 232 skupín vysokých 25–65 cm: 7 743 celých inštancií
a 489 skupín rozdelených na 6 726 samostatne osadených zdieľaných častí.
Kontrola 1 211 676 vzoriek skutočných pätiek nepotvrdila levitujúcu trávu;
najvyššia pätka je 2,021 mm pod podkladom. Masky kontrolujú celé premietnuté
obrysy pri dome, chodníkoch, záhone, koloch a v priestore bránky. Porušení je 0.
Pôvodné záhonové rastliny sa nemenili; 258 starých okrajových trsov je skrytých
a zachovaných, 54 vonkajších zostáva viditeľných.

Podklad používa [ambientCG Grass005](https://ambientcg.com/view?id=Grass005),
[CC0](https://docs.ambientcg.com/license/), `PBRProcedural`. Finálne sú tri
neupravené 1K JPG mapy Color/Roughness/NormalGL. Mierka 1 m je vizuálny
predpoklad, drsnosť 0,80–0,98, intenzita normály 0,35; displacement sa nepoužíva.
Pôvodné kredity PlantCatalog a Lassi Kaukonen (CC BY 4.0), Rob Tuytel a Rico
Cilliers (CC0) sú zachované v `assets/ASSET_MANIFEST.md` vrátane odkazov.

## Rozpočet a reprodukcia

Samostatný finálny proces Blender 5.3.0 nameral pri C1/96 vzorkách čas
168.05 s a konzervatívnu pamäťovú špičku 2.927 GiB
(3,142,590,464 B). Maximum zahŕňa aj OS high-water údaj, nielen pravidelné vzorkovanie.
Súbor má 67,898,569 B (64.75 MiB), pod limitom 90 MiB.
Jedinečná vyhodnotená geometria má 626 753 trojuholníkov; inštančne rozvinutý
počet je 85 906 914. Rozptyl sa úplne nerealizoval.

Malý pilot obsahoval 8 × 8 m trávnik, 20 × 20 m lúku a 100 stromov; mal 599 091
jedinečných vyhodnotených trojuholníkov, 30 735 918 po rozvinutí a súbor
82 133 823 B. Jeho krátky render spotreboval približne 1,80 GiB. Plný 2K render
prekročil cieľ 3 GiB, preto sa použili dovolené 1K mapy, polovičná hustota
vzdialenej lúky a 32 m lúčne oblasti, ktoré znižujú réžiu objektov. Blízka lúka
a 8 m oblasti záhradného trávnika sú zachované. Dlhšie bežiace GUI má vyššiu
spotrebu (5.67 GiB počas finálnych renderov);
čerstvý proces sa meral samostatne. Nie je tvrdené, že GUI zostalo pod 3 GiB.

Studené otvorenie overilo 82 zabalených obrazových súborov, 19 uchovaných
master kolekcií, nulové chýbajúce knižnice/obrazy a nezmenené chránené svedkyne.
Zostavenie z factory-startup porovnalo 9,612,774 číselných hodnôt;
maximálna sémantická odchýlka je 0. Druhé `apply_v05` má presne zhodný podpis.
Surové porovnanie zaznamenalo 117 rozdielov: 96 v lokalizovaných názvoch uzlov/
odkazov a 21 v neaktívnom `Subsurface Scale` (nulová neprepojená váha).
Porovnanie ich pomenúva a normalizuje, aktívne shaderové hodnoty nemení.
Rozsah tolerancií, matice kamier, čas každého renderu, SHA-256 a presné výrezy
sú v [metadátach](../renders/render_metadata.json).

SHA-256 finálnej scény: `c3bd3d5e847c52d33a60f3f89cf4392da85a24df96fe7774a25a37bd39d8fafe`.

## Hranice a odovzdanie

Vysoké orbitálne pohľady ukazujú opakovanie lúčnych skupín; severozápadný pohľad
čiastočne prekrýva zachovaný les. Celkový vzhľad, rozmery domu, poloha kamery
a podoba pozemku stále čakajú na tvoje prijatie. Stavebné ani pozemkové overenie
sa netvrdí.

HEAD zostáva `f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c`; v oboch repozitároch
sa nič nezaradilo, necommitovalo ani nepublikovalo. Run-map má 04 uzavretý
podľa jeho prijatého záznamu a 05 stále provisional. Manuálne archivovanie patrí
tebe; JSON metadát vyžaduje explicitné vynútené zaradenie na ceste
`projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/renders/render_metadata.json`.
