# 01_closure — kysucka-moderna-chata-spatial-site-valley-and-grass

Closure signal: CELOK UZAVRETÝ ORCHESTRÁTOROM
Closure status: closed — overená editovateľná a reprodukovateľná **technická priestorová základňa v05**; **nie prijatá finálna profesionálna vizualizácia**. Master Chat Orchestrator dostáva hardvérové spresnenie a kompletný zoznam zvyškových nedostatkov pre ďalšie celky.
Closed: 2026-11-16, Europe/Bratislava
Author: ORCHESTRATOR (this whole)
Access profile: Orchestrator
Orchestrator session scope: logical-whole
Development run identity: kysucka-moderna-chata-reference-visualization
Closed scope: spojitý svetový terén, údolie pozdĺž +X, uzavretá záhrada s bránkou, krátky trávnik, vysoká lúka, deterministické zdroje a zabalená scéna v05, natívne multi-view rendery, samostatné overenie zostavenia a Michalom požadovaná záverečná analýza.
Working candidate: `/home/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v05.blend`
Candidate SHA-256: `c3bd3d5e847c52d33a60f3f89cf4392da85a24df96fe7774a25a37bd39d8fafe`

```text
Phase-qualified result: implementation-PASS
Result artifact or commit: local blender/kysucka_chata_mcp_v05.blend (c3bd3d5e847c52d33a60f3f89cf4392da85a24df96fe7774a25a37bd39d8fafe); nový Git commit ani publikácia neboli povolené ani vykonané
Result evidence: Worker report 01/02, prečítanie všetkých Meta artefaktov celku okrem zmrazeného handoutu, priame prečítanie finálnych obrázkov, kontrola repozitárov a živého Blenderu 5.3.0/GPU, cielené kontroly skla, odrazu krbu, lesov a prístupu k bránke
Logical-whole closure: closed-by-ORCHESTRATOR
Required preceding results: satisfied for bounded technical delivery; finálne vizuálne prijatie sa nezískalo
Cooperator-owned decisions: satisfied — Michal požiadal o poslednú podrobnú rekapituláciu a odovzdanie zvyškových problémov Master Chat Orchestratorovi
Residual-risk disposition: satisfied — nedostatky sú zdokumentované a prenesené do ďalšieho rozhodovania, nie skryté uzavretím
Upgrade-ledger reconciliation: complete (nebol deklarovaný upgrade ledger)
Active mutation: no active Worker task or render; saved live scene idle; necommitnuté projektové/Meta zmeny čakajú na Cooperatora
Closure actor: ORCHESTRATOR
```

> **Dôležité ohraničenie:** Tento signál uzatvára jeden technický logický
> celok, nie celý vizualizačný projekt. Scéna `v05` je editovateľná základňa
> ďalšej práce, nie dokázaná fotorealistická vizualizácia podľa referencie.
> Technicky prepočítané inštancie, uzavretá topológia, balenie a reprodukcia
> nenahrádzajú vizuálne prijatie. Nové body tohto dokumentu sú usmernenie
> pre Mastera, nie nová implementačná alebo publikačná autorita.

## 1. Skutočne dodané a overené výsledky

### 1.1 Terén, lesy a chránené plochy

- Spoločná triangulovaná plocha **`SITE_terrain_proxy` + `V05_TERRAIN`** pokrýva
  **`[-260, 320] × [-220, 260] m`**, s obvodovým plášťom a spodkom pri `Z = -90 m`.
- Všetkých `129 279` zvarených hrán má dvoch susedov; otvorené chybné švy: `0`.
  Minimálny skalárny súčin normál na šve: `0.9999996128`.
- Všetkých **skutočných `126`** pôvodných vrcholov chránenej terasy
  `[-15, 19] × [-10, 11.5] m` má nulovú zmenu. Odhad `459` v prompte bol
  nahradený meraním, nie nesprávne použitý ako povinný počet.
- Štyri kamerou projektované pásy kopcov z v04 sú skryté a zachované.
  Súvislým terénom sa odstraňuje ich levitujúci oblúkový charakter pri orbitovaní.
  Všetkých `1 200` pôvodných lesných stromov a mladé smreky `V04_YOUNG_02/03`
  bolo výškovo dosadených na nový spoločný povrch. Spolu `2 402` stromov má
  maximálnu chybu osadenia `0.009 mm`.
- Údolie pozdĺž `+X` klesá približne k `-24.05 m` pri `X = 120 m` a potom stúpa
  k druhému hrebeňu. Spojitosť terénu je odlišná otázka od vizuálnej kvality
  vegetácie a optiky, ktoré môžeme vyhodnotiť len v obrázoch.

### 1.2 Záhrada, plot, bránka a kamery

- Konvexná záhrada: **`810.910 m²`**, rozmery **`34.70 × 25.12 m`**. Po maskách
  a rozšírených výrezoch okolo existujúcich stromov zostáva `528.12 m²`
  voľného trávnika pri vzorke `0.20 m`. Nové ovocné stromy sa nepridali.
- Pôvodných `26` kolov a `2` priečky sú nezmenené. Doplnených je `286` kolov
  vrátane bránových a `100` priečok vrátane bránky, bránka s paličkami,
  diagonálou, závesmi a západkou a štyri prístupové betónové dosky.
- Rohové posty nemajú duplicitné stĺpy. Koniec priečky je najviac `20.003 mm`
  od stredu podpory; chyba usadenia kolov je menšia ako `0.00005 mm`.
- `CAM_A_REFERENCE` ostáva `[21.5, -10, 1.25] → [8.5, 2.5, 1.25]`, `35 mm`,
  `36 mm sensor`, `shift 0/0.105`, `clip_end 500 m`. V uloženej scéne je aktívna
  s profilom `1448 × 1086 / 96 samples / Cycles CPU / OIDN`.
- Pomocné snímky obsahujú pohľad na celý pozemok, skutočný vnútorný pohľad cez
  sklo, štyri orbitálne strany a natívne detaily oboch druhov trávy.
  Výrezy sú 1 : 1 bez retuše a zmeny mierky.

### 1.3 Tráva, reprodukcia a aktíva

- Nových `1 200` zdieľaných smrekov, `5 332` záplat trávnika (`4–10 cm`)
  v `17` oblastiach a `8 232` lúčnych skupín (`25–65 cm`). Nerovný podklad
  rozdelil `489` lúčnych skupín na `6 726` samostatne usadených zdieľaných častí.
- Kontrola `1 211 676` pätiek nenašla levitujúcu trávu; najvyšší bod ostáva
  `2.02 mm` pod podkladom. Maska má nula porušení pre origin aj skutočné
  premietnuté obrysy pri dome, schodoch, chodníku, záhone, koloch a bránke.
- Scéna: `67 898 569 B` = **64.75 MiB**, `626 753` unikátnych vyhodnotených
  trojuholníkov a `85 906 914` trojuholníkov cez inštancie, nikdy plne
  nerealizovaných. Má `4 166` objektov, `82` zabalených obrazov a `19` fake-user
  master kolekcií.
- Chladné otvorenie prebehlo bez chýbajúcich knižníc/obrázkov. Samostatné
  `factory-startup` zostavenie porovnalo `9 612 774` číselných hodnôt so
  sémantickou odchýlkou `0`. Druhé `apply_v05` je idempotentné a globálne RNG
  ostáva zachované.
- Raw porovnanie zaznamenalo `117` odchýlok: `96` lokalizovaných názvov uzlov/
  odkazov a `21` neaktívnych hodnôt `Subsurface Scale` pri neprepojenej nulovej
  hmotnosti. Iba tieto overené polia sa normalizujú; aktívne shaderové
  nastavenia sa nemenili v záujme umelého splnenia testu.
- Zachované sú S00/v01/v02/v03/v04, referencia, `timber_fence_v03.py`,
  `landscape_v04.py`, sedem modelových knižníc a autorské CC BY/CC0 kredity.
  V projekte je `Grass005 1K` (PBRProcedural CC0). Pôvodná 2K ZIP a mapy
  zostávajú len v dočasnom `work/downloads/`, nie premenované za 1K.

### 1.4 Dôkazové súbory

| Artefakt | SHA-256 |
|---|---|
| `01_report_00.md` | `2b0ff52350ac3bbf905136af6faf3a6c93e4f9b45b13cfcca8237c82d2d30abc` |
| `01_report_01.md` | `71aac7c5b849073aa73e48ed69560979b7dd39e74d398b613e7fe258ca8ccc34` |
| `renders/before.png` | `87d0ba9dd7382aa765dee2eddac0ccbcc12adecaa5dcbc8f6e8ff744757fdcc0` |
| `renders/after.png` | `3050eeb56a678cd8af32ee30bd3fa91444256dcd278d54f3b2c7782bd8142844` |
| `renders/site_overview.png` | `30145b29417b6b0d4276fe51cdec41be2698e86d57cfed8ca1feaf8bedc4490e` |
| `renders/valley_from_inside.png` | `16cccb403dac71436b885c804080a1c27da0e844e1921b3941a8dd36f05c540b` |
| `renders/orbit_sheet.png` | `c0e7ebc5664348cffe932feb5a0aa12560b72d1c728660b8e6663bb1bbb5d695` |
| `renders/grass_details.png` | `5579a6a2f648b4f68798221a0874354732803ed1f0421a9f60b0db4c826d44ee` |
| `AGENTS.md` po záverečnom doplnení CachyOS/vizuálnych kritérií | `0d63847340460344825cc9b1104322706f01a678dded780f1e06f7219f810393` |
| `README_SK.md` po doplnení CachyOS/vizuálnych kritérií | `e4e58a52f41b40edcba1035a0cc51d38b31ea2581a8dda6d560d59eabea40ee8` |
| `docs/OPERATIONS.md` po doplnení CachyOS/vizuálnych kritérií | `29d23d3a432d47e9910eb48fdf9abed680d99fb03a2a5c03d01865ad176ef6c9` |

`renders/render_metadata.json` (2 801 riadkov) obsahuje zdrojové a obrazové
hashy, kamery/matice, masky, korene, geometrické kontroly, merané trianguly,
časovanie, RSS a úplné replay dôkazy.

## 2. CachyOS a koniec automatického limitu 3 GiB

### 2.1 Aktuálny jediný pracovný kontext

Michal rozhodol, že ďalšia práca projektu bude prebiehať **výhradne na PC s CachyOS Linuxom**.
Historické záznamy o macOS/8 GiB M1 zachovávame, ale nesmú už riadiť hustotu ani
LOD nových kandidátov. Overená/hlásená aktuálna konfigurácia:

| Súčasť | Stav |
|---|---|
| Systém | `CachyOS`, `ID=cachyos`, `ID_LIKE=arch` |
| Procesor | `AMD Ryzen 5 3600`, 6 jadier / 12 vlákien |
| Systémová RAM | `32 GiB`; Michal hlási **približne 20 GiB dostupných** aj s bežiacimi dev nástrojmi, Blenderom a browserom |
| GPU | `NVIDIA GeForce RTX 3080`, **10 240 MiB VRAM** |
| Ovládač | `nvidia-smi 620.70.06`, CUDA UMD `13.5` |
| GPU zaťaženie pri kontrole | `4434 MiB / 10240 MiB`; proces Blenderu `2987 MiB` |
| Blender | `/home/agile/Applications/Blender/blender`, `5.3.0`, MCP `127.0.0.1:9876` |
| Cycles zariadenia cez MCP | `OPTIX` aj `CUDA` s `use=True`; CPU v zozname `use=False` |
| GUI pri kontrole | v05 otvorená, `is_saved=True`, `is_dirty=False`, `render_running=False`, C1 aktívna |
| AP | gitlink/checkout `d7023cf037f6d17885c3ede5c04812c61640da50`, `./.ap/ap doctor: PASS` |

### 2.2 Ako zachovať Rozpočet pri profesionálnej práci

- Hodnota `target_render_rss_bytes = 3221225472` pochádza z opatrného plánovania
  spojeného so starším 8 GiB M1. **Nie je to technická požiadavka aktuálneho
  CachyOS PC, ani trvalý projektový limit.**
- Pôvodné výkonové opatrenia viedli k 1K `Grass005`, `meadow_density_scale_far = 0.5`
  a oblastiam lúky 32 m. Bola to dovolená volba v realizanom grante, nie dôkaz
  vizuálnej výhodnosti 1K alebo polovičnej hustoty.
- Svieži proces jedného C1 renderu nameral `168.05 s` a konzervatívnu OS/high-water
  pamäťou `2.927 GiB`. Dlhodobé GUI udávalo `5.67–5.70 GiB` vďaka alokačnej
  histórii. To sú odlišné merania, nie protirečenie.
- Každý nový grant má zaznamenať oddelene GUI/CLI, RAM, VRAM a skutočné použitie
  CPU/CUDA/OPTIX. Dostupnosť zariadení v preferenciách nie je dôkaz ich použitia
  vo výslednom renderi.
- Zachovaná Cycles CPU+OIDN C1 kontrola ostáva pre before/after. Rýchlejšia
  OPTIX/CUDA cesta musí patriť samostatnému zdokumentovanému profilu.
- Kvalita a hustota sa majú vybrať priamym natívnym A/B dôkazom, nie automaticky
  znížovaním z minulého rozpočtu. Rozdiel 1K/2K a hustoty sa hodnotí vizuálne.
- Tento hardvérový kontext je doplnený do `AGENTS.md`, `README_SK.md` a
  `docs/OPERATIONS.md`. Managed AP block a sekcia **Closure and Git gates**
  ostali byte-identické. Scéna, `model/parameters.json`, generátor a modul
  `site_v05.py` sa touto zmenou dokumentácie nezmenili.

## 3. Úplný zoznam nedostatkov pre Master Chat Orchestratora

Nálezy vychádzajú z obrázkov, referencie, zdrojov a MCP. Nie každý je chyba
Workera: niektoré plochy boli v tomto grante zámerne chránené (sklo, svetlo,
interiér, drevo, strecha, základ domu). Sú však stále otvorenými úlohami pre
profesionálny vizuálny výsledok.

### A. Les a hĺbka krajiny

**D01 — Vzdialený hrebeň za údolím nemá stromy.** V `valley_from_inside.png`
dominuje prázdna hladká gaussianska zeleň. Sektory nového `V05_FOREST_*` zaberajú
najviac `X = 35..230`, zatiaľ čo hrebeň `X = 240..320` ostáva bez stromov.
**Ďalší cieľ:** hustý vrstvený les na vzdialenom hrebeni tam, kde sa výhľad
má najviac podobať na diaľku.

**D02 — Nové sektory lesa sú príliš riedke.** Kandidátske obdĺžniky predstavujú
približne `111 m²/strom` na západe a juhu a `91 m²/strom` na severovýchode,
ešte pred gládami/filtrami. `spacing_m = 3` je len minimálny odstup dvoch stromov,
nie priemerná hustota lesa. Prehľad a orbity ukazujú hladké plochy.
**Ďalší cieľ:** hustota podľa šírky korún a ich prekrytia, nie len množstvo inštancií.

**D03 — Okraje lesov pôsobia jednotvárne a vypreparovane.** Viac stromov má podobnú
výšku a pravidelné medzery; chýba organický prechod z lúky cez kroviny/mladé
stromy k plným korunám. **Ďalší cieľ:** zóny podrastu a redších okrajov,
lokálne zhluky a glády, nie prstenec rovnakých smrekov okolo chaty.

**D04 — Časť stromov vyzerá skôr ako suché ihly.** `Picea mariana` je vhodná
na hustú vzdialenú zástavbu, jej úzka koruna však na popredí a vláčnych okrajoch
údolia nestačí. **Ďalší cieľ:** viac plného `Picea abies` v predných vrstvách,
radiálne/výškové variácie, podrast a prirodzená štruktúra bez tvrdenia natívnej
botaniky.

**D05 — Kopce sú stále príliš hladké a gaussianske.** Vyššia triangulácia terénu
nerieši samu formu/zakrytie. Oblé svahy v interiéri a v orbitoch potrebujú
lepší terénny tvar a viacvrstvové pokrytie lesom a lúkami.

**D06 — Údolie je geometricky voľné, ale opticky ešte nepôsobí dostatočne hlboko.**
Stredový lúč prechádza cez sklo až po `X = 220 m` bez pevnej prekážky. To je
dobrá kontrola osi, nie celková kompozícia. Potrebujeme ustupujúce lesné boky
a horizonty s meniacim sa detailom/farbou/atmosférickou hĺbkou.

### B. Lúka a trávnik

**D07 — Lúka je plocha s izolovanými tmavými trsmi, nie súvislá vegetácia.**
Pravý detail v `grass_details.png` ukazuje veľké holé medzery medzi trsmi;
na orbitoch vidno malé tmavé body na hladkom zeleno podklade.
**Ďalší cieľ:** plná spodná a stredná geometrická pokryvnosť, nie iba viac vysokých
trsov v rovnakých medzerách.

**D08 — Opakovanie lúčnych masterov je zrejmé z výšky.** Štyri kompozície,
málo farieb a kruhové zoskupenia vytvárajú pravidelnosť. Potrebné sú viac variantov,
stochastická poloha/rotácia/šírka, tenšie trsy a vrstvenie suchých a zelených častí.

**D09 — Lúka má umelé pásy a kruhové hranice.** Funkcia `_meadow()` používa pásma
hustoty `2 / 0.5 / 0.12` od stredu `(7.2, 4.2)`, masku a `far_scale = 0.5`.
Obvodový pás trsov napodobňuje hranicu parcely, nie vegetačný prechod.
**Ďalší cieľ:** svetovo zašumené gradienty prechádzajúce k lesným okrajom a svahom.

**D10 — Krátky trávnik má príliš ploché a málo prehnuté listy.** V `_lawn_masters()`
je list z piatich bodov/troch trojuholníkov a ohyb len `0.004–0.020 m`.
Pri výške `0.04–0.10 m` pôsobia listy ako rovné úzke pásky, nie prirodzená tráva.
**Ďalší cieľ:** viacbodové 3D prierezy, rebro, skrútenie, vodorovné zložky
a rozličné rastové polohy namiesto plochých vertikálnych pásikov.

**D11 — Podklad a farba trávy sú príliš rovnomerné.** `MAT_V05_LAWN_*` má len
konštantné farby a zem 1K PBR. Treba preskúmať thatch/spodnú slamu,
zeleno-olivové odstíny, konkrétny prierez a mikrotiene a mierku 1 m.
Nechceme "cartoon" rovnaký zelený náter pod inštanciami.

**D12 — Počet bodov nezaručuje prirodzenosť.** Natívna snímka ukazuje medzery
aj napriek presným výškam a nulovej chybe osadenia. Akceptovanie má zahŕňať
C1, detail z nízkej polohy očí a všetky orbitálne pohľady s rovnako dôležitou
vizuálnou váhou, nie iba štatistické podmienky.

**D13 — Citlivý prechod medzi trávou a záhonom treba posúdiť aj vizuálne.** Nulová
kolízia s chodníkmi/záhonom je dobrá, no strih pri dome by mal byť miestami
mäkší a prirodzenejší, nie ako jeden umelo hranatý zelený okraj.

### C. Sklo a interiérový výhľad

**D14 — Sklo má skutočnú optickú chybu pre účel jasného výhľadu.**
MCP overil `MAT_GLASS`: `Transmission Weight = 1.0`, `IOR = 1.45`,
**`Roughness = 0.07`**, `Alpha = 1.0`. To zodpovedá rozmazaniu detailov terénu
aj plota v `valley_from_inside.png`. Sklo je visual stand-in, nie finálne čisté
presklenie. **Ďalší celok:** fyzické nastavenie hrúbky, IOR/roughness,
odrazov a kontrolu jasného pohľadu bez skrytia `G01/G02`.

**D15 — Oranžový vertikálny prvok je kompatibilný s odrazom krbu v skle,
nie stromom v údolí.** Zrkadlenie šiestich `FIRE_proxy*` okolo roviny
`X = 14.412 m` premieta prvky do `u ≈ 0.556–0.582` a `v_top ≈ 0.643–0.730`
v `CAM_V05_VALLEY_INSIDE`. To zodpovedá nálezu v obraze. Okolité reálne
lúče cez sklo trafili len sklo/terén/lúčne clumpy.
**Interpretácia:** dominantný vnútorný odraz skutočného emisného krbu.
**Riešenie:** fyzikou odrazu a kompozíciou interiéru, nie vymazaním
nesprávne identifikovaného exteriérového stromu. Chránený krb a osvetlenie
v tomto celku ostávajú nezmenené.

**D16 — Vnútorný odraz a rozostrenie zatiaľ oslabujú dôkaz do diaľky.**
Po optickom vyčistení skla a doplnení lesa má kontrola zahŕňať celý zorný rozsah,
normálnu výšku očí a detail vzdialeného horizontu, nie iba jeden voľný lúč.

### D. Kamery a prístup k bránke

**D17 — NW/SZ orbitálna kamera je v existujúcom lese.** V pravom hornom
obrázku `orbit_sheet.png` prekrýva les takmer celý dom.
**Ďalší cieľ:** nová vyššia/vzdialenejšia NW/SZ poloha s čitateľným domom,
plotom a krajinou, bez skrýtia lesov a zmeny C1.

**D18 — Presná maska a veľa inštancií nemôže zastúpiť vizuálnu kontrolu.**
Worker čestne zaznamenal opakované trsy a zlé NW prekrytie; tieto body sú v tomto
registri. Ďalšie prijatie má kontrolovať každý podstatný obrazový odsek,
nie iba výsledky replay/count/mask.

**D19 — Prístup k bránke je krátky asi o 18–22 cm.** Posledná povolená doska
má stred `Y = -7.90` a hranu `Y = -8.175`; os bránky je `Y = -8.393591772`.
Podľa hrúbky listu ostáva medzera asi `0.18–0.22 m`.
**Ďalší cieľ:** malá pristávacia doska/plošina s aktualizovanou trávovou maskou,
bez presunu pôvodných dosiek a uzavretá priamo ku bránke v novom grante.

**D20 — Základ domu má nevyriešené tmavé medzery a chýba detail prechodu zo
schodiska a terasy k zemi.** Referencia má plnú kamennú podstavu a drobný štrkový lem.
Súčasný zjednodušený betónový základ potrebuje osobitnú revíziu sokla,
podpery a prechodu betón–štrk–tráva. Nezachádza sa stavebno-staticky.

### E. Ďalšia architektúra, materiály a osvetlenie

**D21 — Strecha pôsobí ako pravidelná škridla, nie ako kovové pásy referencie.**
Panelový tvar, stojaté drážky, rozmer, odtieň, hrúbka a okraje treba osobitne
referenčne prepracovať namiesto súčasnej dlaždicovitej mriežky.

**D22 — Komín nemá kamennú/murovanú faktúru referencie.** Je stále hladký svetlý blok
s dekoratívnymi liniami, nie finálny kameň. Poloha komína voči krbu a viditeľnosť
ohňa ostáva v neskoršej architektonickej revízii.

**D23 — Obloha a osvetlenie nedosahujú referenčné fotografické prostredie.**
Sivá obloha a mäkké hypotetické svetlá ostávajú príliš ploché/chladné.
Budúci svetelný celok má koordinovať sklo (jas), slnko, odraz/bounce, drevo,
podhľad a interiér bez náhodného lokálneho zosvetlenia.

**D24 — Drevo, veranda a interiér sú stále skráteným zástupným modelom.**
Drevo má oproti referencii hrubší/oranžovejší tón; chýbajú kvetináče,
bohatšie trvalky/levanduľa, boulder, sedák/lavička a drobné vonkajšie detaily.
Interiér má boxy/stoličky/svetelný kruh a nejednoznačnú partíciu/slab namiesto
referenčného zariadenia. Možné „druhé dvere“ sa nemajú mazať: exteriérový D01
existuje iba jeden. Otázka patrí do ďalšieho interiérového celku.

**D25 — Všetky rozmery a architektonické vlastnosti zostávajú hypotézami.**
Pôdorys 14.4 × 8.4 m, sklon 45°, poschodie, dispozícia, zadné fasády,
kamera C1 a pozemok nie sú zamerané ani stavebne potvrdené. Ani tento dokument
netvrdí statiku, povolenie, energetickú certifikáciu alebo geodéziu reálneho miesta.

### F. Publikovanie a archivácia

**D26 — Projektový commit/push v tomto celku neexistuje.** `HEAD` ostáva
`f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c`, projektový index je prázdny.
Povolená bola iba inicializácia `.ap`. Táto dokumentačná rekapitulácia
ani uloženie v05 nie je novým publikačným grantom. Publikovanie potrebuje
Michalovo samostatné rozhodnutie a recheck exact parentu.

**D27 — Meta archival je lokálna a nedokončená.** Výstupy celkov 04 a 05 sú
untracked/nezaradené. `00_RUN_MAP.md` má mechanický snapshot so 04 `closed`
a 05 `provisional`; toto uzavretie ho nepovažuje za verejne potvrdenú novú mapu.
Archivácia patrí COOPERATOROVI a Master Chat Orchestratorovi, nie samotnej scéne.

Pri archivovaní Meta:
1. Pridať každý reálny prompt/report pár spoločne, až keď report existuje.
2. Vynútiť tento ignorovaný súbor explicitne:
   `git add -f projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/renders/render_metadata.json`.
3. Skontrolovať prípadne príslušný starší JSON celku 04 podľa skutočných súborov.
4. Nesúvisiace untracked `projects/kronika/` nezaradiť a neupravovať.
5. Nikdy `git add .`; explicitné cesty, samostatný nový grant a overenie verejného
   commitu priamo.

## 4. Návrhy ďalších logických celkov

Toto sú odporúčania, nie grant na nový kód alebo na novú publikáciu. Každý nový
celok má začať z overenej v05 s novým výstupným súborom (nie prepisovaním v05)
a samostatným implementačným grantom.

### 4.1 Prvý navrhovaný celok: hustý les a súvislá lúka/tráva

Identifikátor: **`kysucka-moderna-chata-dense-forest-and-continuous-meadow`**

- Hustý les na vzdialenom hrebeni `X ≈ 200..320`, s dochovaným otvoreným
  koridorom z preskleného štítu.
- Hustejšie vrstvy v celom okolí podľa skutočnej šírky korún a ich prekrytia,
  nie podľa jedného oblúkového prstenca. Plnokorunné predné smreky, variácia
  šírky/výšky, mladé stromy a podrast.
- Súvislá spodná a stredná pokryvnosť lúky, ktorá odstráni efekt tmavých trsov
  na prázdnom zelenom podklade a umelého obvodového pásu.
- Skutočné 3D listy trávnika s viac segmentmi, ohybom, skrútením, thatch a
  prirodzenou farebnou variáciou.
- Sektorové overenie v C1/low-eye/detail a následne vo všetkých orbitoch.
- Nová NW/SZ kamera mimo lesov s čitateľným domom, plotom a prechodmi.
- Rozpočet vyvodiť z RTX 3080/32 GiB a hlásených ~20 GiB voľných, nie z historického
  3 GiB cieľa. Zachovať zdieľané inštancie, replay a idempotenciu.

### 4.2 Nasledujúci celok: čisté sklo a detail prístupu

Identifikátor: **`kysucka-moderna-chata-clear-valley-optics-and-entry-detail`**

- Fyzicky preveriť a upraviť `MAT_GLASS` pre čistý výhľad namiesto skrytia `G01/G02`.
- Riešiť dominantný odraz krbu v rámci skutočnej optiky a kompozície.
- Doplniť pristávaciu plochu k bránke a uzavrieť zvyšných 18–22 cm medzery
  s novou clearance maskou.
- Preveriť sokel/schodisko a štrkový lem v rovnakom alebo blízko súvislom
  detailnom grante.

### 4.3 Následný celok: referenčná architektúra, svetlo a interiér

Identifikátor: **`kysucka-moderna-chata-reference-architecture-light-and-interior`**

Treba ho koordinovať s prijatou krajinou: panelová strecha, komínový kameň,
obloha/slnko/bounce, drevo, podhľad, kvetináče/lavička/kameň/záhony,
finálny interiér a partícia/slab. Ovocné stromy sa majú individuálne vybrať
až pre voľný priestor tejto záhrady, nie vkladať ich automaticky. Každý import
si ponecháva autorov, licencie a overené cesty v manifeste.

### 4.4 Kritérium skutočného vizuálneho prijatia

1. Hlavný C1 vyzerá presvedčivo v 1448 × 1086 a v natívnom detaile.
2. Orbitovanie neodhaľuje prázdne/riedke plochy ani pravidelné kopce trsov.
3. Vnútorný výhľad má jasný detail vzdialeného údolia a horizontu bez dominancie
   optického rozostrenia a rušivého svetelného odrazu.
4. Krátky trávnik a vysoká lúka majú rozličiteľné, ale prirodzené, súvislé porasty.
5. Architektúra, materiály a atmosféra smerujú k referencii, nie len k zjednodušenej
   všeobecnému pojmu „drevená chata so zeleňou“.
6. Offline reopen, source replay, idempotencia a CC BY/CC0 kredity zostávajú
   zachované; publikácia a archivácia prebiehajú len s výslovným grantom.

## 5. Granty, stav procesu a zdrojová pravda

- `01/01` Planner: terminálny `PASS`, plánovacia autorita skončená.
- `01/02` Implementation: terminálny `PASS` = `implementation-PASS`;
  nezávislé prijatie sa netvrdí, autorita skončená.
- Táto rekapitulácia neposkytuje nový realizačný ani publikačný grant.
- GUI má uloženú v05, C1, `is_dirty=False`, `render_running=False`.
  Čítacie kontroly skla a projekcie odrazu nezmenili súbor.
- V projektovom repozitári ani Meta nebol vykonaný commit ani push. Untracked
  `projects/kronika/` a ostatná cudzia práca zostali zachované.
- `work/` checkpointy a `work/v05_source_replay.blend` sú dočasné.
  Zdrojové verzie, `model/parameters.json`, moduly, knižnice a manifest
  zostávajú referenčným offline vstupom pre ďalšiu prácu.
- Architektonická/stavebná revízia je odložená až po skutočnom vizuálnom prijatí.
  Nové hardvérové možnosti nezískavajú automaticky autoritu ani povolenie ďalších zmien.

## Closure Statement

CELOK UZAVRETÝ ORCHESTRÁTOROM

Logický celok `kysucka-moderna-chata-spatial-site-valley-and-grass` sa uzatvára
na overenej editovateľnej a reprodukovateľnej scéne
`blender/kysucka_chata_mcp_v05.blend`. Odovzdáva sa CachyOS hardvérový kontext,
rozobratie starého cieľa 3 GiB, detailný zoznam vizuálnych nedostatkov plus
konkrétne nasledovné logické celky. Finálna profesionálna vizualizácia sa týmto
neprehlasuje za hotovú; táto scéna je zachovaným technickým štartovacím bodom
pre hustý les, prirodzenú trávu, lepšiu optiku, detail prístupu a nasledovné
architektúru/svetlo/interiér.
