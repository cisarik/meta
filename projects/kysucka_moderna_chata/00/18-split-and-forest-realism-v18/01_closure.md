# Poučenia a podklad k uzavretiu V18

**24. 11. 2026 · Podklad pre Orchestrátora celku**

Michal po sérii denných porovnaní požiadal exteriér nateraz odložiť po poslednom doladení lúky a chodníka. Výsledkom je lokálny pracovný kandidát s kompletnou dennou sadou a s otvoreným západom slnka z ďalšieho uhla. Stav technického overenia, Michalovo rozhodnutie o prestávke a posúdenie celku sú samostatné. Formálne rozhodnutie o uzavretí patrí Orchestrátorovi.

```text
Logical whole identity: kysucka-moderna-chata-split-and-forest-realism-v18
Logical-whole closure: not-closed
```

## Čo odovzdať

Posledný denný exteriér je [kysucka_chata_exterier_doladeny.blend](/home/agile/Projects/kysucka_moderna_chata/work/v18/recovery/kysucka_chata_exterier_doladeny.blend). V Meta k nemu patrí [12 obrázkov](renders/2026-11-24_150201_727305_doladenie-exterieru/), [porovnanie pred a po](renders/2026-11-24_150201_727305_doladenie-exterieru/porovnanie.jpg), [manifest](renders/2026-11-24_150201_727305_doladenie-exterieru/manifest.json) a [správa k doladeniu](renders/2026-11-24_150201_727305_doladenie-exterieru/sprava.md). Pri tomto odovzdaní som overila digest súboru voči manifestu, dekódovala páry všetkých dvanástich PNG a porovnala konfiguráciu kamier a renderu s predchádzajúcou sériou.

| Artefakt | Úloha | SHA-256 |
|---|---|---|
| `work/v18/recovery/kysucka_chata_exterier_doladeny.blend` | Posledný lokálny denný kandidát | `5e8ada70e99c70a3be0a7eea9b18306b422e4ef3a141a63b51b237b7957e3a24` |
| `work/v18/recovery/kysucka_chata_exterier_jar.blend` | Predchodca posledného doladenia a základ priameho A/B | `34d3d55200ce0d257e3c950303b589df7c2f0d268eee7a4f49b318d96875a158` |
| `work/v18/recovery/kysucka_chata_exterier_pracovny.blend` | Obnovovací checkpoint s ľahším štartovacím pohľadom | `a1629449399da47cdef4ca8754033109e8e1801bdc3dd53c7d40fd4440f0d322` |
| `blender/kysucka_chata_exterier.blend` | Verzovaný predchodca z výmeny 01/06 s ťažkým štartovacím pohľadom | `a0a153c66e25015b60781537097200dcba09a8423be0d21b0a23dddab93f8b56` |
| `blender/kysucka_chata_interier.blend` | Samostatná interiérová verzia z výmeny 01/06 | `c607cb21fbdb289b49f05596004b403e7dd5f96a64e900ce42ed8485f6a30449` |
| `model/review_cameras_v18.json` | Zdroj transformácií a rozlíšení pre pravidelnú dávku | `9d4731214ea68720a2b40626cce74b3d361d73d9b5c8f00c9ded949a37647d07` |
| `scripts/render_v18_review.py` | Zostavenie a archivácia porovnávacej dávky | `a51778d150b0a438027fa75c3cc7edcfcca758268f6f616c246b2f808492e0df` |

Projektový Git bol pri odovzdaní na `f600c7a8e69a23a029559872652302ac299c2aea` s AP pinom `d7023cf037f6d17885c3ede5c04812c61640da50`. Meta bolo na `9af60f367be3bf9e413b1a1bd2c9f129b22cd992`. Posledný denný balík bol v Meta lokálne mimo indexu. Priečinok `work/` je ignorovaný. Pri obnove z nového checkoutu alebo na inom stroji treba preniesť konkrétny checkpoint a overiť jeho hash. Procedurálny zdroj V18 pokrýva formálnu vetvu cez 01/06. Neskoršie opravy sú uložené v odvodených súboroch Blenderu a ich renderových manifestoch. Výber vstupu pre ďalší grant musí výslovne uviesť, na ktorú vetvu nadväzuje.

## Poučenia z rozdelenia a vývoja krajiny

**Dve samostatné scény potrebovali najprv kontrolu závislostí.** Po normalizácii 11 vstupov Stage 1 vytvoril samostatne prenosný exteriér a interiér. Oba spočiatku obsahovali 5 371 objektov a 289 zabalených obrázkov. Pôvodne skryté vegetačné objekty mali stále používateľov v scéne, preto sa ich čistenie odložilo až po skúške dosiahnuteľnosti. Spoločný súbor 289 prvkov obálky má kontrolný súčet `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50`. Ten je vhodnou kontrolou pri prípadnom prenose medzi scénami. Interiér má vlastnú verziu aj podklad pre budúcu štúdiu pivnice. Rozmery v podklade opisujú vizualizačný model. [Plán a spoločná obálka](01_report_00.md) · [Normalizácia a rozdelenie](01_report_01.md)

**Obrazová medzera chodníka sa musela najprv overiť v geometrii.** Pilot zachoval pôvodnú štrkovú plochu. Záber, nad ktorým vznikla pochybnosť, mal v dvoch úsekoch medzi kamerou a štrkom terénnu vlnu. Kontrola nad trasou a 1 105 staníc preukázali súvislosť povrchu. Skutočné predĺženie prišlo až s rozšíreným terénom. Napojenie pri `[42, 138.25, 1.157007]` m vedie k severnému okraju `[61, 340, 30.410757]` m. Výsledná trasa má približne 404 m v pôdoryse od brány. Podpora koreňov, trávy a štrku sa kontrolovala na skutočných trojuholníkoch terénu. [Pilotný dôkaz](01_report_01.md) · [Rozšírenie terénu a trasy](01_report_02.md)

**Nadhľad a pohľad od domu odhaľujú rôzne chyby.** Doplnenie svahov do rozsahu `[-320, 340] × [-220, 340]` m a výsadba po obvode opravili prvý jednostranný porast. Pri veľkom oddialení ostáva rozoznateľný fyzický okraj modelovaného terénu. Jarné koruny, podrasť a skupiny mladých stromov potrebovali samostatné zábery zblízka. Pri jemných farbách listov, štrku a koreňových nábehoch je detailový záber lepším svedkom než široká dioráma. [Rozšírené údolie](01_report_02.md) · [Jarné listnáče a podrasť](01_report_04.md)

**Počet stromov sám o sebe neukazuje viditeľnú zmes.** Pôvodných 11 535 stromov sa vo formálnej vetve postupne zredukovalo na 5 100. Pri jarnom modeli pôsobila aj časť stromov vedených ako smreky listnato, pretože tvar korún vychádzal z listnatých predlôh. Pomohli skutočné modely smreka obyčajného, šesť tvarových variantov a vyváženie aj v zóne viditeľných svahov pri chate. Pred skrytím mala celá scéna 2 550 smrekov a 2 550 listnáčov. Vo viditeľnej zóne bolo po vyvážení 592 stromov každého typu. Následný deterministický výber skryl 765 stromov, presne 15 %, a overených 4 335 zostalo aktívnych. Body zostali v súbore a obe mračná majú vratný prepínač `Skryť vybrané stromy`. [Formálne merania lesa](01_report_05.md) · [Vizuálne porovnanie zmiešaného lesa](/home/agile/Projects/kysucka_moderna_chata/work/v18/recovery/zmiesany_les_nahlady.png)

**Lúka potrebovala pracovať v niekoľkých mierkach naraz.** Pre prvý problém, schodovitý prechod materiálových slotov medzi trávou a lesom, pomohla jedna 4K RGB mapa s UV vo svetových súradniciach. Formálna iterácia 01/06 doplnila 82 225 trsov, 4 820 skupín kvetov, 3 010 skupín vysokej trávy, 68 kríkov a osem samostatných stromov. Šesť modelovaných druhov tráv vychádzalo z regionálnych podkladov a líšilo sa siluetou stebiel a súkvetí. Holé vzdialené plochy však ostali viditeľné aj po rozšírení detailnej vegetácie pri chate. [Prvá 4K mapa a botanické podklady](01_report_05.md)

Celé údolie potom dostalo fotografickú farebnú štruktúru a 105 180 trsov v troch pásmach detailu. V ďalšej iterácii sa táto vrstva zahustila o 30 % na 136 734 trsov. Michalov nadhľad odhalil ešte svetlé slamové škvrny, ktoré boli z úrovne očí menej rušivé. Selektívna jarná zeleň zachovala kresbu a posledná úprava doplnila jemnejšiu fotografickú štruktúru a 12 miest vlhkej zeminy pri chodníku a krajnici. Zdroje novej farebnej kresby a blata sú uvedené aj v správe a v zabalených dátach scény. [Lúka zhora aj z výšky očí](/home/agile/Projects/kysucka_moderna_chata/work/v18/recovery/luka_pred_a_po.png) · [Doladenie](renders/2026-11-24_150201_727305_doladenie-exterieru/sprava.md)

## Plynulosť, GPU a druhy overenia

Výmena 01/06 prešla studeným otvorením a izolovanými Workbench a Cycles testami. Úplný model korún v pracovnej vetve dosahoval približne 35–38 tisíc trojuholníkov na hlavný prototyp. Na Michalovom stroji Blender 24. 11. o 12:01:47 zapísal načítanie súboru a o 12:01:56 NVIDIA zaznamenala pre ten istý proces `Xid 109 / CTX SWITCH TIMEOUT`. Kontrolný súčet súboru sedel. Presná príčina chyby ovládača zostala neurčená. Pre budúce prevzatie má preto studené načítanie, prvý obraz v grafickom okne a plynulé otáčanie na cieľovom stroji vlastnú hodnotu dôkazu. [Izolované GPU testy z 01/06](01_report_05.md) · [Katalóg chýb NVIDIA Xid](https://docs.nvidia.com/deploy/xid-errors/620/analyzing-xid-catalog.html)

Obnovovací súbor dostal ľahšie modely korún len do pracovných vetiev a štart v Solid Texture s vypnutými tieňmi a cavity. Pri cielenej kontrole mal kontrolný Cycles render 360 × 203 pixelov presnú zhodu s predchodcom. Otvorenie a náhľad sa podarili v izolovanom grafickom Blenderi cez llvmpipe. Michal následne potvrdil, že pracovnú kópiu otvoril. Pri ďalšej lúčnej úprave sa pre pracovný pohľad vyplo 52 ťažkých modifikátorov V16. Detailný porast V16 ostal k dispozícii pre Cycles. Plynulosť finálnej scény pri interaktívnom otáčaní na RTX zostala nezmeraná.

| Sada | Meraný kontext | Celková špička VRAM |
|---|---|---:|
| Lúka pred zahustením | RTX 3080, 6 obrázkov | 7 839 MiB |
| Hustejšia lúka a skrytie 15 % lesa | RTX 3080, 6 obrázkov | 7 878 MiB |
| Jarná farba lúky | Meranie obnoveného úseku dávky | 7 877 MiB |
| Posledné doladenie | RTX 3080, 12 obrázkov v dvoch dávkach | 7 945 MiB |

Prvé dve sady ukazujú podobnú celkovú pamäť pri súbežnej zmene trávy aj lesa. Z týchto údajov sa nedá oddeliť samostatný prínos skrytých stromov. Skorší plný EEVEE pokus narazil na limit RAM a na počet atribútov zdedeného štrkového shaderu. Po zjednodušení shaderu prešiel skúšobný EEVEE náhľad pri 60 % rozlíšení s vypnutým ray tracingom a architektonickými svetlami. Táto skúška namerala 9 148 MiB celkovej VRAM. Budúce merania majú vždy uviesť režim, konkrétnu scénu, stavy pracovných vetiev a odlíšiť pamäť celého zariadenia od pamäte procesu. [Formálne merania](01_report_05.md) · [Merania poslednej dávky](renders/2026-11-24_150201_727305_doladenie-exterieru/manifest.json)

## Porovnávací workflow a obnova po chybe

- **Zachytiť uhol pri spätnej väzbe.** Pri `Zábere 09 | Vlastný nadhľad údolia` sme zo snímky odhadli pozíciu podľa chaty, chodníka, okrajov terénu a smeru osí. Zhodu v ďalších dávkach určuje už uložená kamera a jej registrovaná matica. Pri novom pohľade je presnejšie uložiť aktuálnu kameru priamo zo scény, kým je referenčný pohľad k dispozícii. Každá nová kompozícia dostane vlastné ID. [Register kamier](/home/agile/Projects/kysucka_moderna_chata/model/review_cameras_v18.json)
- **Rovnaké uhly a rovnaký profil držať spolu.** Štandardná dávka používa SZ, SV, JZ, JV a vlastný nadhľad. Nadhľad má aj verziu Solid Texture. Dve posledné rozšírené sady pridali šesť uložených prezentačných kamier exteriéru, takže máme 11 uhlov a 12 obrázkov. Presnú rozšírenú sadu určuje pole `cameras` v jej manifeste. Bežné kamery majú 960 × 540, nadhľad 1536 × 638. Uzamknutý profil Cycles je RTX 3080 OptiX, 32 vzoriek, snímka 1, seed 0, AgX a textúry do 2K. Solid Texture ukazuje plnú farebnú mapu. Automatické uloženie do Meta beží pri použití dávkového skriptu. [Postup dávky](/home/agile/Projects/kysucka_moderna_chata/docs/OPERATIONS.md:6) · [Manifest celej sady](renders/2026-11-24_150201_727305_doladenie-exterieru/manifest.json)
- **Kontrolovať výsledok po načítaní, nielen deklarované nastavenie.** V skorších dôkazoch časová značka pri nastavení snímky zmenila aktívnu kameru. Dávka odstraňuje väzby markerov iba v pracovnom procese a nastavuje kameru z registra. Pri vratnom skrytí lesa sa v Blenderi 5.3 hodnota na rozhraní uzlov neprejavila v existujúcich modifikátoroch, kým sa nezapísala skutočná hodnota v `modifier.properties.inputs`. Správanie sa potom overilo počtom vyhodnotených inštancií so zapnutým aj vypnutým prepínačom. [Prvý problém s markermi](01_report_01.md)
- **Hotové obrázky sa dajú zachrániť aj pri prerušenej dávke.** Jarná sada skončila kódom 143 po desiatich hotových obrázkoch. Príčina prerušenia zostala neurčená. Zvyšné dva výstupy boli dopočítané z rovnakého súboru a s totožnými nastaveniami, potom sa skontroloval celý manifest. Záverečná dávka bola rozdelená na dve časti s časmi 66,44 a 70,52 s a zlúčená podľa ID a kontrolných súčtov. Pri rozpočte renderu pomáha vopred zvoliť veľkosť časti a overiť kompletnosť archívu podľa deklarovaného zoznamu. [Jarný manifest](renders/2026-11-24_143809_887942_jarna-luka-final/manifest.json) · [Záverečný manifest](renders/2026-11-24_150201_727305_doladenie-exterieru/manifest.json)
- **Kontinuitu treba odčítať z fyzického artefaktu.** Výmenu 01/04 zastavil rozdiel medzi hashom reportu v grante a jeho uloženými bajtmi. Skutočný hash `01_report_02.md` je `d75f710d3664868c3b0ea76520ee453bde91e22961e385543ff26417089d10a2` a zhodoval sa s pôvodnou potvrdenkou. Obnovenie umožnil nový úplný grant so správnou kotvou. Pri ďalšom odovzdaní sa oplatí prepočítať digest priamo z lokálneho súboru, ktorý bude vstupom. [Záznam o zablokovanej výmene](01_report_03.md)

## Otvorené body pre rozhodnutie

- **R-V18-01 · Západ slnka z opačného pohľadu cez údolie.** Michal ho výslovne žiada evidovať ako residual. Referenciou je jeho posledná snímka s chatou blízko stredu, chodníkom prichádzajúcim zľava a sedlom za chatou. Pri návrate k tejto úlohe treba uložiť samostatný uhol a doručiť z neho večerný render v Cycles. Overenie má ukázať čitateľný západ a teplý obzor pri sedle, pričom zostane vidieť chatu aj prednú lúku. Stav je otvorený. [Pôvodný zápis residualu](renders/2026-11-24_150201_727305_doladenie-exterieru/sprava.md#otvorený-residual-r-v18-01)
- **Vizuálny limit dennej scény.** Michal potvrdil postupné zlepšenie a vybral prestávku po úzkych korekciách. Miera fotorealizmu celej lúky ostáva otvorenou vizuálnou otázkou. Hranicu terénu možno vidieť v najširších orbitách. Rozhodnutie o prípadnej ďalšej práci vychádza z posledného schváleného rozsahu a konkrétneho záberu, ktorý problém ukáže.
- **Prenos a prevádzka.** Posledný kandidát prešiel otvorením bez siete a so skrytým zdrojovým projektom. Reprodukovateľnosť všetkých jeho materiálov je v zabalenom súbore. Prechod na iné PC alebo obnova z Gitu vyžaduje dostupný checkpoint z ignorovaného `work/`. Interaktívna plynulosť finálnej verzie na RTX ostáva samostatným meraním. 

Tento zápis slúži na zosúladenie dôkazov a výber presného východiska. Kontroly vykonané v tejto session patria k implementačným dôkazom tej istej session. Michalovi zostáva rozhodnutie o vizuálnom prijatí, ďalšom rozsahu a archivácii v Gite. Orchestrátor môže týmto bodom priradiť konečnú dispozíciu podľa pravidiel projektu.
