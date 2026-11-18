# V07 – les a súvislý štrkový chodník

Stav implementácie: **PARTIAL**. Uložený technický kandidát, opora, prenosnosť,
zdrojový replay a idempotencia sú overené. Parameter krajníc 0,45–0,75 m zatiaľ
nemá samostatné vynútenie; kód používa konštantný test pôdneho pásu 0,85 m a
obnovný porast do 1,15 m plus hraničné náhrady. Tieto obnovné zóny nie sú dôkazom
splnenia cieľovej šírky krajnice. Povolená jedna oprava je využitá. Ďalší zásah
potrebuje rozhodnutie orchestrátorky a nový grant.

## Uložený výsledok a zdroje

`/home/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v07.blend` – 194344710 bajtov, SHA-256 `99c4f239040e880d0d8c5e9fc761954690b707c84ce746a33ac356a86d72e384`.
Novú sekciu `forest_trail_v07` vlastní JSON; modul `scripts/forest_trail_v07.py`
je spoločný pre MCP aj builder. Starších 18 sekcií a v03/v04/v05/v06 moduly
ostali nezmenené. Referencia a staršie scény sú zachované. Pracovné checkpointy
a replay sú dočasné dôkazy, nie zdrojová autorita.

## Les a register

| Položka | Overený výsledok |
|---|---:|
| Celkový les | 12 977 = 12 833 + 144 |
| Náhrady s mierkou 0,5 na každej osi | 649; 5,001156 % |
| Staršia mladá trieda s faktorom 1 | 378 |
| Povolené existujúce posuny XY | presne 11 |
| Okrajové výmeny MARIANA → ABIES | 337 |
| Nové lokálne trávne trsy | 60 552, z toho 3 297 hraničných náhrad |
| Maskované pôvodné lúčne body | 41 215 |
| Kamene / ihličie | 300 / 600 inštancií |

Úplný register je natívny Text `V07_FOREST_REGISTRY.json` v `.blend`.
Metadáta obsahujú hash celého registra, všetkých 649 výberov s nemennými
predlohami, 144 doplnení a presné ID výmen/mladej triedy. Výber je deterministický
seed 13707, osem sektorov a tri vzdialenostné pásma. Doplnenia rešpektujú polygon,
rozstupy a dve eliptické oblasti bez nových koreňov; blízke údolie zostáva otvorené.
Nové stromové siete ani materiály sa nezaviedli.

## Trasa, opora a ochrana scény

Trasa má 1 105 bodov, XY dĺžku 198,180813 m, priestorovú dĺžku 200,616798 m,
maximálny rozstup 0,199972 m a maximálny pozdĺžny sklon 30 %. Úprava profilu je
najviac 87,401 mm. Skutočný výstup je [42;138,25;1,142006468] m, povrch štrku
Z = 1,157006468 m. Bod mimo hranice Y = 138,251 správne zlyhá. Žiadny nový
štrkový vrchol ani celý pôdorys nového trsu nepresahuje terén.

Štrková vrstva je uzavretá, spodok 2 mm v teréne, povrch 15 mm nad ním;
kontrola nenašla otvorené hrany ani vynechanú stredovú stanicu. Skosenie pri
bránke má 27,55–35,13°; svetlosť pod zachovaným krídlom je 5,000 mm.
Je to krátky vizuálny prechod, nie bezbariérová podesta.

Pôvodné terény zostávajú zachované. Najväčší posun pôvodného vrcholu v odvodenom
teréne je 0,291433 m; mimo koridoru je nulový. UV a normály mimo koridoru sa
zhodujú presne, projektované pokrytie pôvodných trojuholníkov nemá výpadok.
Opora všetkých nových koreňov a 7 633 ponechaných trsov v dotknutej oblasti bola
premeraná. Zvyšok používa identické pôvodné buffery a dôkaz nedotknutej podpory.
Medzi maskovanými prípadmi je 3 422 trsov so stredom mimo jadra, ale geometriou
zasahujúcou do jadra. Ponechané body majú nula zásahov do jadra/úprav/koreňov.
Najväčšie vystúpenie ponechaného koreňového obalu je 0,916 mm; zahrnutie 18,654 mm.
Nové trsy majú maximálne zahrnutie 18,993 mm a sú aspoň približne 2 mm zapustené.
Konzervatívny obal bázy stromov má maximálne zahrnutie 830,671 mm na svahu;
vystúpenie je záporné, približne −6 mm. Tento široký obal sa vykazuje samostatne.

1 539 pôvodných sietí, 4 477 objektov, 82 pôvodných obrázkov a svetlá/world/staré
kamery prešli ochranou. Všetkých 85 obrázkov je zabalených a má platný externý
súbor s rovnakým hashom. Tri mapy [Gravel Ground 01](https://polyhaven.com/a/gravel_ground_01)
sú 2K JPG, [CC0](https://polyhaven.com/license), metrická mierka 3 m; licencie,
bajty a hashe sú v manifeste aktív a v metadátach.

## Replay a natívne snímky

Jediný normálny builder v03→v04→v05→v06→v07 uložil replay. V tom istom procese
prebehla vynútená opakovaná aplikácia v07 bez druhého v06: presná zhoda, RNG
nezmenený. Uložený replay a uložený MCP kandidát majú presne zhodných 80 vlastných
sietí a 89 objektov. Nepoužitá lawn skupina bez používateľov prirodzene chýba v
oboch uložených súboroch. Zdanlivý rozdiel šiestich svetiel bol len poradie dvoch
uzlov; úplné uzly/spojenia aj fyzické parametre a viditeľnosť sú presne zhodné.
Žiadne svetlá sa neupravovali. Skutočný produkt bol otvorený v ďalšom čistom
procese a jeho C1 vyrenderovaný pod P0.

P0: CPU, 8 vlákien, 96 vzoriek, CPU OIDN Accurate/High, AgX/None, frame/seed 0,
expozícia 0, gamma 1. Dokončené samostatné ťažké procesy majú zachytený skutočný
návratový kód a záznam RSS/RAM/VRAM. Pri prerušenej prvej renderovacej dávke je
známy kód obalového procesu 143; konečný kód jej Blender procesu sa nezachytil.
Najväčšie doterajšie namerané RSS je 9,004 GiB.
NVML je spoločná obsadenosť GPU desktopom; nepredstavuje GPU render. GPU/P1 ani
zmena preferencií neprebehli.

Čerstvé [v06 pred](../renders/before.png) a [skutočné v07 po](../renders/after.png)
majú rovnakú C1. [Vekové porovnanie](../renders/forest_age_comparison.png) obsahuje
celé snímky tej istej kamery a nezväčšené výrezy 1:1; faktor 0,5 označuje geometriu,
pričom porovnávaná náhrada je jedným z 11 povolených posunov XY.
[Celková trasa](../renders/trail_overview.png), [bránka](../renders/trail_gate_detail.png),
[pohľad chodca](../renders/trail_eye_level.png), [orbitálny hárok](../renders/orbit_sheet.png)
a [vonkajšie údolie](../renders/valley_exterior_diagnostic.png) používajú úplnú scénu.
Všetky originály sú v `renders/native/`; skladanie iba kopíruje natívne pixely.

## Zostávajúce limity a doručenie

Okrem nevynútenej šírky krajníc zostávajú nízke vetvy zakrývajúce pohľad chodca,
okraje konečného sveta v pevnom celkovom zábere, pôvodné smerové/bodkované textúry
lúky, morfológia trávnika a optické/architektonické obmedzenia. Sklon skosenia a
veľkosť produktu sú výslovne vykázané. Profesionálne vizuálne, architektonické ani
prijatie návrhu pre skutočnú lokalitu sa netvrdí.

Zachované logy vysvetľujú prerušený prvý zápis obrovského riadka registra,
Michalom povolený reštart/jedno opakovanie, prerušenú prvú renderovaciu dávku,
opravy pomocných kontrol a jedinú sústredenú opravu podpory trasy. Žiadny Git zápis
sa nevykonal. Neskoršie vynútené pridanie ignorovaného `renders/render_metadata.json`
do Meta patrí Michalovi. Úplná evidencia: [render_metadata.json](../renders/render_metadata.json).
