# Poznámky orchestrátorky — interiér hlavného obytného priestoru, celok 10

Autor: ORCHESTRATOR tohto celku
Access profile: Orchestrator
Orchestrator session scope: logical-whole
Development run identity: kysucka-moderna-chata-reference-visualization
Logical whole identity: kysucka-moderna-chata-interior-living-space
Dátum otvorenia: 2026-11-17, Europe/Bratislava
Životný cyklus: prevádzkové poznámky tohto celku; historická evidencia, nie task authority; pri uzavretí zmraziť, čistenie vlastní COOPERATOR pod osobitným grantom.

## 2026-11-17 20:00 — otvorenie bez handoutu

Michal priamo v tejto session vybral cieľ: „Riešim v tomto projekte teraz
interiér, poďme začať.“ Určil ma za Orchestrátorku, ktorá si Workerov deleguje
ako vlastných subagentov, a výslovne rozhodol, že všetko do Meta zapisujem ja
a konám autonómne. Provisional handout pre interiér neexistuje, preto nie je
čo revalidovať; tento celok otvára `00_notes.md` podľa Meta README.

Rozhodnutia Cooperatora platné pre celok:

- delivery: subagent dispatch z tejto session (nie manuálny prenos);
- persistencia: prompty, reporty, poznámky aj closure zapisujem ja do
  lokálneho Meta checkoutu; reporty ukladám bajtovo presne z návratovej
  hodnoty dispatchu;
- Meta Git (stage/commit/push) nebol výslovne spomenutý. Projektové pravidlo
  ho necháva Cooperatorovi a v Meta je nesúvisiaca rozpracovaná práca
  (`projects/kronika/`, celky 05–07, zmenený run map). Git preto nemením a
  Michalovi to pri prvej príležitosti oznámim.

## Stage 1 — obnovený stav (read-only)

- Projekt: fyzický koreň `/home/agile/Projects/kysucka_moderna_chata`, origin
  `https://github.com/cisarik/kysucka_moderna_chata.git`, `main`, HEAD
  `f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c` = priamo čítaný verejný
  `refs/heads/main` (ls-remote 20:01). Verejný main je v04; v05–v08 a pilot
  V09 sú zámerná lokálna nepublikovaná práca. Nič neresetujem.
- AP: gitlink aj checkout `.ap` `d7023cf037f6d17885c3ede5c04812c61640da50`.
- Meta: origin `https://github.com/cisarik/meta.git`, HEAD = verejný main
  `bb274bdd179e1038da0d3679fea214dd81128fe4`; celky 05–07 sú lokálne
  untracked.
- Prečítané: `AGENTS.md`, `.ap/AP_ORCHESTRATOR.md`, z `.ap/AP.md` spine,
  RF-01–RF-08, RF-19, Finite Convergence, §3 po Communication Routing, §14
  vrátane Run-Level Handouts a Continuation Bootstrap; z
  `.ap/PROMPT_CONTRACTS.md` report header, Planning Record, Common Worker
  Task Fields, Mutation Axes, delivery record, routing a Plan-to-Execution.
  Neprečítané časti AP (§5–§13, §15–§19 v plnom znení) dočítam pred
  implementačným grantom.
- Upgrade ledger: v projektovom `AGENTS.md` nie je deklarovaný; nehľadám ho.

Namerané hashe (20:05): `scripts/build_scene.py` c83e2bd2…6176cc369,
`scripts/design.py` 60b65d8b…, seed 9fcea3fc…, referencia 05bc3e72…,
v08 1ba638c7…, v08_view 07146b03…, `scripts/vegetation_v08.py` cd3137ed…,
`AGENTS.md` 005321eb…. Hashe v08, v08_view a modulu V08 súhlasia s
`AGENTS.md`. `model/parameters.json` a `scripts/build_scene.py` sa od tabuľky
V07 líšia, čo zodpovedá doplnenej sekcii a hooku V08; `AGENTS.md` ich nové
hashe neuvádza.

## Zistenie: súbežne beží celok V09

`work/v09/TASK_STATE.md` (19:56) opisuje aktívny celok
`kysucka-moderna-chata-reference-environment-pilot-v09` v inej agentskej
session: prvá nízkorozlišovacia štúdia prostredia podľa novej referencie
`reference/environment_valley_00.png`. Stav je živý, nie historický:

- `scripts/nature_study_v09.py` a `model/parameters.json` boli zapísané
  20:02:23, teda počas môjho čítania; pribudla sekcia `nature_study_v09`,
  ostatných 20 sekcií je zhodných s `work/v09/baseline/model/parameters.json`
  (e567d8cc…);
- dostupná RAM klesla z 14 GiB (20:01) na 7 GiB (20:05), čiže beží jeho
  CPU úloha;
- jeho Root vlastní živé MCP a GUI Blendera (PID 9404, socket 9876), CPU
  úlohy serializuje s RAM strážou (štart pri ≥ 12 GiB) a neuloženú prácu
  z GUI uložil do `work/v09/checkpoints/owner_before.blend`.

Dôsledok pre tento celok (moje orchestračné rozhodnutie, nie Plannerova
odpoveď): interiér musí mať disjunktnú mutačnú doménu. Žiadne živé MCP/GUI,
žiadny zápis do `model/parameters.json`, `scripts/build_scene.py`,
`scripts/nature_study_v09.py`, `AGENTS.md`, `README_SK.md`,
`docs/OPERATIONS.md` ani `work/v09/**`, kým V09 beží; žiadny GPU render bez
samostatného meraného grantu (história resetov); malé serializované CPU/RAM
nároky. Interiér sa má vyvíjať v ľahkej izolovanej scéne iba s chatou a do
plnej scény a zdieľaných súborov sa integruje neskorším samostatným krokom.
V tejto session som preto Blender MCP ani CLI Blender nepoužila.

Ďalšie nezrovnalosti, ktoré nepatria tomuto celku a iba ich evidujem:

- celok 07 nemá closure; `AGENTS.md` ho vedie ako PARTIAL s požiadavkou na
  dispozíciu Orchestrátorky (šírka krajníc), ktorú V08 výslovne odložil;
- V08 a V09 nemajú v Meta žiadny záznam; run map
  `00/00_RUN_MAP.md` končí celkom 07 v stave provisional a je neaktuálny.
  Run map vlastní run-scoped Orchestrator; nemením ho.

## Vymedzenie celku

Zdrojový stav interiéru: kolekcia `50_INTERIOR_PROXY` (kocky sedačky, stolík,
jedálenský stôl so stoličkami, kuchynský blok, „PARTITION_proposed“, krb,
prstencový záves), `FLOOR_interior`, vnútorné steny v `MAT_INTERIOR_PLASTER`
a jedno plošné svetlo `INTERIOR_warm`. V oficiálnom C1
(`previews/v08/after_C1.png`) je cez štít vidieť ploché béžové steny a
krabicový nábytok, rozmazané drsnosťou skla 0,07. Referencia ukazuje teplý
drevený obytný priestor so sedačkou, kamenným krbom s ohňom, jedálenským
stolom, prstencovým svietidlom a lampou.

Prvý ohraničený celok navrhujem takto: realistický, zariadený a nasvietený
priestor 07 (obývačka / jedáleň / kuchyňa, `[8.8, 0.3, 14.1, 8.1]` m,
otvorený do strechy), čitateľný cez presklený štít z C1 aj z nových
interiérových kamier. Miestnosti 01–06 sa iba zinventarizujú a zostanú na
ďalšie celky. Dispozícia, steny, otvory, komín a strecha sa nemenia; bez
podkrovia. Je to moje odporúčanie; rozsah a vkusové voľby potvrdí Michal na
plánovacej bráne pred akoukoľvek mutáciou.

Číslovanie priečinka: poradie 08 a 09 nechávam voľné pre celky V08 a V09,
ktoré reálne prebehli alebo bežia bez Meta záznamu, a aby som sa nezrazila so
súbežnou session, ak si stopu doplní. Doterajšia prax drží poradie priečinka
zhodné s verziou scény, interiér teda nesie 10 a pracovný prefix V10.

Evidence tier plánovania: E0. Pre implementáciu predpokladám E1/E2
(reverzibilné lokálne súbory, subjektívne prijatie vlastní Michal, nezávislé
prijatie netreba).

## Prompt 01/01 — Planner

`01_planning_00.md` je finálny. Routing: fresh-worker-session, Planner,
Native planning mode: required, plan approval-gated, implementácia v tej
istej session zakázaná, po pláne fresh-worker-session.

Odchýlka zaznamenaná pravdivo: nástroj na dispatch subagentov v tomto
klientovi nemá prepínač Plan Mode. Ako skutočný natívny režim som zvolila
klientom vynútený read-only typ subagenta (`explore`), nie promptovú náhradu
nad zapisovacím agentom. Read-only klient nevie zapísať report, preto je
menovaným persisterom ORCHESTRATOR (výslovná voľba Cooperatora), pravidlo P2.
Doručenie: subagent dostane presný lokátor súboru promptu a jeho SHA-256 a
prečíta ho celý; koordináty 01/01 sa spotrebujú dispatchom.

Kontrola splniteľnosti: všetky požadované kroky sú čítanie; žiadny krok
nevyžaduje zápis, Blender ani sieť (sieť je voliteľná, jej absencia má
v prompte pomenovanú náhradu); mutačné osi sú tri krát `none` a súhlasia
s delivery záznamom.

## 2026-11-17 20:10 — report 01/01 prijatý na reconciliáciu

Dispatch: read-only subagent `explore`, concrete session
`da834268-4828-462a-a5e7-caec45f79aed`, spustený 20:06, ukončený 20:09.
Prompt doručený lokátorom a hashom
`db31e843fb3a98adb32660dea2ff2927ee760a6a486856e57195ac52a33f716e`; Worker
hash sám overil. Report som uložila bajtovo presne z prepisu subagenta
(posledná správa, od hlavičky po koniec) ako `01_report_00.md`, SHA-256
`a368dc7e8158ef11dfbd9881bbdbfa0b923e807f455a5d785b45c43487ff719c`, 408
riadkov. Identita: presná hlavička, koordináty 01/01 práve raz, compact core
prítomný, status PASS, closure not-closed, žiadny closure signál. Handshake:
čítanie, vyhľadávanie, obrázky a read-only shell pozorované; zápis
nepozorovaný; sieť nepoužitá.

Report je tvrdenie, nie prijatie. Moje overenie:

- **Viditeľnosť z C1 je v pláne nesprávne.** Plán radí krb a sedačku medzi
  prvky, ktoré C1 vidí cez štít (§2.3, priorita P1). Vlastný výpočet z
  kamery `[21.5, -10]` a roviny štítu X = 14.4: lúč ku krbu `(11.3, 3.2)`
  pretína rovinu štítu v Y = −0.81 a prednú stenu v X = 13.77, k sedačke
  v Y = −2.47 / X = 12.07. Oba prvky sú za plnou prednou stenou. Cez sklo
  štítu (Y 0.15–8.25) je v pôdoryse vidieť iba trojuholník pri zadnej stene:
  jedálenský stôl (Y = 2.97 v rovine štítu), kuchynskú linku okrem jej
  západného konca, zadnú stenu od X = 8.84 a podhľad strechy. Súhlasí to
  s `previews/v08/after_C1.png`. Plán sám uvádza, že presný klin neoveril.
- **Dôsledok pre referenciu.** Vonkajšia referencia ukazuje oheň a sedačku
  cez presklenie prednej steny pri nároží štítu. Model má na tom mieste plnú
  drevenú stenu (predné otvory sú iba D01 a W01). Krb sa z C1 nikdy neukáže,
  kým tam presklenie nebude. Je to zmena obálky, teda rozhodnutie Michala.
- Cesta k študijnej scéne je nedourčená (`build_scene.py` je skript, nie
  importovateľný modul; plán ponúka dve nerozhodnuté alternatívy).
- Identifikátory CC0 aktív sú neoverené návrhy; mechanizmus skla (voľba A)
  je opísaný neurčito.
- Použiteľné a overené: inventár proxy objektov a svetiel s riadkami zdroja,
  rozmery priestoru 07, zhoda siedmich JSON sekcií s kópiou V09, hranica
  disjunktnej domény voči V09, návrh povoleného zoznamu ciest.

Dispozícia: plán v tejto podobe neprijímam ako rozhodnutím úplný. Status
PASS z reportu nepotvrdzujem; hodnotím ho ako čiastočný podklad.

## 2026-11-17 20:10 — nová referencia od Michala

Počas behu Plannera poslal Michal bez textu obrázok interiéru. Uložila som ho
bajtovo zhodne ako `references/interior_concept_00.jpg` (1024 × 576, SHA-256
`9f7e4e9da1c654a72523d451b696391e29581fd83bbd7b9a766a4e4ee0336fc2`). Pôvod
(fotografia alebo AI koncept) nepoznám; beriem ho ako Michalov vizuálny smer,
nie ako rozmerový podklad.

Čo obrázok ukazuje: vysoký presklený štít s výhľadom do údolia, drevený
podhľad s trámami, galéria so zábradlím z tmavej ocele a lankami, drevené
schodisko s podsvietenými stupňami, krb s čiernym oceľovým plášťom, rohovým
preskleným ohniskom, kamennou lavicou a kamenným komínom, nika s polienkami
a policami, veľká svetlá rohová sedačka, masívny drevený stolík, koberec,
oblúková lampa, rastliny, dubová podlaha, teplé večerné svetlo.

Zrovnanie s modelom: pri pohľade od kuchyne k prednej stene je štít vľavo,
krb `(11.3, 3.2)` v strede a priečka X = 8.8 vpravo, čo kompozícii obrázka
zodpovedá. Dva prvky však menia samotnú stavbu a kolidujú s obmedzeniami,
ktoré som dala Plannerovi:

1. galéria a schodisko. Prompt 01/01 ich zakázal podľa `docs/VISUAL_BRIEF.md`
   („bez obytného podkrovia“), čo je však hodnota zo zoznamu Michalom zatiaľ
   neprijatých návrhov, nie jeho rozhodnutie. Geometricky je galéria nad
   miestnosťami 01–06 možná: pri podlahe galérie okolo +3.45 m je svetlá
   výška aspoň 2 m v páse širokom približne 4 m okolo hrebeňa;
2. presklenie prednej steny pri štíte (zhodne s vonkajšou referenciou).

Obe sú materiálne rozhodnutia Cooperatora. Pýtam sa na ne spolu s cestou
k aktívam a s Meta Gitom. Po odpovedi vydám jedinú cielenú revíziu plánu
(basis: new-repository-or-external-evidence — Michalova referencia a môj
výpočet viditeľnosti); druhá automatická revízia neexistuje.

## 2026-11-17 20:14 — rozhodnutia Michala

Michal odpovedal na štyri otázky:

1. **Galéria a schodisko: áno.** Galéria nad izbami a schodisko
   s podsvietenými stupňami patria do plánu. Tým padá obmedzenie „bez
   podkrovia“ z promptu 01/01.
2. **Presklenie prednej steny pri nároží štítu: áno**, zahrnúť do plánu; do
   plnej scény až pri integrácii po V09.
3. **Aktíva: bezplatné CC0** modely a textúry z Poly Haven / ambientCG,
   zvyšok procedurálne. Platené generovanie nie.
4. **Meta Git: commitovať a pushovať, výlučne priečinok tohto celku.**
   Stage iba explicitné cesty, push bez force na `origin main` po overení
   verejného rodiča. Nesúvisiacu prácu v Meta nechávam nedotknutú.

Cieľ celku zostáva ten istý (interiér hlavného obytného priestoru podľa
referencie), mení sa rozsah stavebných prvkov, ktoré k nemu patria. Identitu
celku preto nemením a nezačínam nový; zmenu zaznamenávam ako cielenú revíziu
plánu. Keďže ide o materiálnu zmenu predpokladov trasy, revíziu dostane
fresh Worker session 02, výmena 01. Rozpočet revízií sa rotáciou session
neobnovuje: toto je jediná automatická cielená revízia.

## 2026-11-17 20:17 — druhá referencia a príprava revízie

Michal poslal druhý obrázok, opäť bez textu: 360° panorámu celého priestoru
(`references/interior_concept_01_panorama.jpg`, 1024 × 512, SHA-256
`0c7c35ea817d802c8daab294d3f50ec9db2ecb86813576a3b491a6c6835800bc`). Meta
`.gitignore` archivuje iba `.md` a `.png`, preto oba obrázky archivujem ako
bezstratové PNG prevody a pôvodné JPG nechávam lokálne; hashe a pôvod sú
v `references/CONCEPT_PROVENANCE.md`.

Moje rozhodnutie o váhe referencií (oznámim ho Michalovi, môže ho zmeniť):
panoráma ukazuje celý priestor, preto je hlavnou referenciou rozloženia;
prvý obrázok je referenciou nálady a detailu. Obrázky sa líšia hlavne krbom
(čierna oceľ s rohovým ohniskom oproti sivému skladanému kameňu s TV
stenou); Planner navrhne jednu syntézu a alternatívu pomenuje ako Michalovo
rozhodnutie. Oblúkové trámy v panoráme pokladám za skreslenie projekcie.

Vlastná read-only príprava pre revíziu:

- overený výber z katalógu Poly Haven cez verejné API (522 modelov, 870
  textúr v odpovedi), uložený ako `evidence/polyhaven_catalogue_shortlist.md`,
  SHA-256 `658e606737ca6a56e9bba7b67ec0a6d3640ef1623652f12304e4a29ac771575e`.
  V katalógu chýba rohová sedačka, koberec, oblúková lampa, polienka, deka,
  kuchynská linka, schodisko a zábradlie; tie budú procedurálne;
- kandidát vstupu študijnej scény: zachovaná `blender/kysucka_chata_mcp_v03.blend`
  (15 MB, hash 360c99a1… súhlasí s `AGENTS.md`), chata s PBR drevom bez lesa.
  Voľbu a dôkaz zhody s `v08_view` nechávam na Plannera.

Prompt 02/01 (`02_planning_00.md`): fresh-worker-session, Planner,
Native planning mode: required (read-only subagent), `Planning cycle:
targeted-revision`, basis new-repository-or-external-evidence, použité
automatické revízie 1. Plán musí byť samostatný, lebo implementačný Worker
dostane iba ten. Git publication owner je odteraz ORCHESTRATOR pre tento
priečinok. Splniteľnosť: iba čítanie a aritmetika, tri mutačné osi `none`.

## 2026-11-17 20:22–20:35 — zosúladenie reportu 02/01 a rozhodnutie Orchestrátorky

Planner 02/01 (read-only subagent) vrátil report so stavom PASS; uložila som
ho bajtovo presne z prepisu subagenta ako `02_report_00.md`, SHA-256
`52a23306ae0b5d394a2951e667e646345397da2d6e266d24cf32031d2c574bfb`.

Počas plánovania Michal sám commitol projekt (20:20:19, `ebfdf66f…`, v05 a
novšia práca). Planner odchýlku HEAD nahlásil a pokračoval, lebo sedem JSON
sekcií a hashe zdrojov sedeli. Je to vlastníkova práca, nie moja zmena; nový
základ je `ebfdf66f5afc0c05343adf4ed49dffb03eb874ef`.

PASS nepotvrdzujem. Report som preverila proti zdrojom a vlastnej aritmetike:

- galéria na +2,70 m pretína priečky vysoké do +3,05 m a nechala by izbám
  svetlú výšku 2,05 m; „pás ≥ 2,10 m v y 1,2–7,2“ je počtová chyba (v y 1,2
  vychádza 1,75 m);
- schodisko má os x = 8,45, teda v zádverí (miestnosť 01), nie v miestnosti
  07, a podestou vo výške +1,50 m zatarasí jediný vstup z chodby;
- presklenie x 10,05–14,01 by prekrylo lavicu a zrušilo kruhový ornament;
  exteriérová referencia má úzky presklený roh vedľa nich;
- tvrdenie, že krb ostane z C1 skrytý aj po presklení, je nesprávne: lúč na
  krb pretína prednú stenu v x = 13,77, teda v presklení;
- hero kamera 0,7 m od ohniska nemôže ukázať štít, krb a schody naraz.

Technická trasa plánu je použiteľná: študijná scéna z v03, modul
`scripts/interior_v10.py`, parametre `model/interior_v10.json`, seed 13710,
názvy `V10_`, skrývanie bez mazania, vlastné číre duplikáty skla, CPU,
tri rezy, identifikátory z katalógového výberu.

Rozpočet plánovania je vyčerpaný (úvodný cyklus + jedna cielená revízia),
tretí Planner podľa AP neexistuje. Prechod: `NEEDS_ORCHESTRATOR_DECISION`,
ktorý vyhlasujem sama pri zosúladení. Moje rozhodnutie: technickú trasu
prijímam, priestorové hodnoty plánu odmietam a nahrádzam ich vlastným
záväzným podkladom `evidence/design_basis_v10.md` (SHA-256
`e1a2165e06d1963067b363e20aa725f01f8d87f822d9970096abbf5621a21d86`),
odvodeným zo zdrojov a prepočítaným:

- galéria: doska x 2,7–8,8, vrch +3,25 (spodok 3,05 = vrch priečok), pás na
  státie y 2,2–6,2;
- schodisko: dvojramenné v SZ rohu miestnosti 07, 16 × 0,175 m, stupeň
  0,27 m, medzipodesta +1,325, horná plošina nad otvorom chodby so svetlou
  výškou 2,60 m;
- presklený roh prednej steny x 12,75–14,25, lavica a ornament ostávajú;
  z C1 cezeň vidno JV roh krbu, stolík a východný koniec sedenia;
- krb: kamenné teleso okolo komína s čiernou oceľovou rohovou vložkou v JV
  rohu, kamenná lavica s polienkami, nika na drevo;
- zóny: obývacia časť na juhu, jedáleň na SV, kuchyňa pri zadnej stene.

Vkusové otázky (charakter krbu, šírka presklenia, TV, pracovný kút, využitie
galérie) majú predvolené hodnoty a sú parametrami; Michal ich uvidí na
pilotných obrázkoch a môže ich zmeniť. Toto je odchýlka od čistej cesty
„prijať plán“: priestorový návrh je moje orchestračné rozhodnutie, nie
výstup Plannera, a jeho overenie v skutočnej scéne (lúče, kolízie, svetlé
výšky) ukladám implementačnému Workerovi.

Zvyšné časti AP potrebné pre implementačný grant som prečítala
(Implementation Authority, Mutation Axes, delivery record, profil Fresh
Implementation Worker, Planning Budget and Expiry).

Prompt 03/01 (`03_implementation_00.md`): fresh-worker-session, Native
planning mode: not-used, rez 1 — študijná scéna a pilot rozloženia. Mení
iba nové súbory `scripts/interior_v10.py`, `scripts/interior_v10_study.py`,
`model/interior_v10.json`, `work/v10/**`; report si Worker zapíše sám do
`03_report_00.md`. Bez MCP, GUI, GPU, siete a Gitu; jeden Blender proces
naraz, stráž RAM 9 GiB (12 GiB pre čítanie `v08_view`), 6 vlákien.
Splniteľnosť: vstupy existujú a majú overené hashe, povolené cesty zatiaľ
neexistujú, dostupná RAM pri vydaní 16 GiB.

## 2026-11-17 20:41–20:50 — hlásené zastavenie Workera 03/01; session v skutočnosti beží

Michal napísal (správa s časom 20:41), že Workera 03/01 zastavil, lebo sa
zasekol na git príkaze. Pozorovania, ktoré s tým nesedia:

- prepis session obsahuje dva dokončené read-only git príkazy a žiadny
  neskorší;
- session po správe pracovala ďalej: 20:42:28 zapísala `work/v10/run_job.py`,
  20:43:15 `scripts/interior_v10_study.py`, 20:43:21 a 20:43:30 spustila dva
  background Blender joby (oba exit 0; 0,8 s / 459 MiB a 1,1 s / 551 MiB),
  ktoré vytvorili `work/v10/study/interior_study_base.blend` a inventár;
  posledný záznam v prepise je z 20:43:52;
- od 20:43:52 do 20:49 sa nemenil prepis ani disk;
- pokus poslať session nadväzujúcu správu o 20:48 klient odmietol s tým, že
  subagent stále beží. Prerušenie som nevynútila.

Záver: session 03 nie je zastavená. Ticho zodpovedá aj písaniu veľkého
súboru (modul `interior_v10.py`), aj čakaniu na niečo; príčinu neviem.

Moja chyba v postupe: na základe Michalovej správy som najprv pripravila
záznam prerušenia, nový grant (najprv ako 04/01, potom ako 03/02) a Dodatok 1
k `evidence/design_basis_v10.md`, hoci som ešte neoverila, že session
naozaj skončila. Nič z toho nebolo vydané ani commitnuté. Koncepty som
stiahla (ležia mimo repozitára v `/tmp/v10_drafts/`), súradnice 03/02 ani
04/01 nie sú spotrebované. Podklad som vrátila na commitnuté bajty
(e1a2165e…), lebo bežiaci Worker má v grante práve tento hash; súbor bol
zmenený dvakrát na krátko (asi 20:44–20:45 a 20:48), čo pri zosúladení
reportu zohľadním.

Vecné zistenie session, ktoré platí bez ohľadu na ďalší postup: hotová
podlaha je na +0,494 (`FLOOR_interior`, `build_scene.py` L120), nie +0,45.
Schodisko má teda výšku 2,756 m = 16 × 0,17225 m, medzipodesta +1,355.
Dodatok k podkladu pridám až po reporte alebo pri novom grante.

Ďalšie zistenia: HEAD projektu je `0f5f84579d88ee67bc0bacee74826ef02bea7452`
(Michalov commit 20:27, README_SK.md → README.md), strážené hashe sedia;
`/usr/bin/time` na stroji nie je; V09 vytvoril nesledovaný
`blender/kysucka_chata_mcp_v09_study.blend`.

Rozhodnutie, či session nechať dobehnúť alebo ju prerušiť a vydať nový
grant, patrí Michalovi; pýtam sa ho.

## 2026-11-17 20:50–21:10 — Michalovo rozhodnutie, prerušenie 03/01, grant 04/01

Michal na otázku odpovedal: prerušiť Workera 03/01 a vydať grant novému
Workerovi bez git príkazov. Prerušenie som poslala cez klienta okolo 21:03.
Session potvrdila zastavenie a uviedla, že žiadny jej príkaz nikdy
neuviazol a git použila iba dvakrát na čítanie (obe volania pod 0,5 s).
Čo Michal videl ako zaseknutie, ostáva nezistené. Session medzitým
pracovala až do 21:03:18.

Na disku po nej ostalo (všetko v allowliste, nič neprijaté): modul
`scripts/interior_v10.py` (1 345 riadkov), nástroj
`scripts/interior_v10_study.py` (743 riadkov, kontroly nedokončené),
`model/interior_v10.json`, launcher, základná aj prvá V10 študijná scéna a
JSON evidencia. Tri Blender joby, každý pod 2 s a 0,6 GiB, žiadny render.
Presné hashe sú v `03_interruption_00.md`, ktorý som napísala ja ako záznam
prerušenia (nie report Workera). Súradnice 03/01 sú spotrebované.

Rozhodnutie o podlahe (Dodatok 1 v `evidence/design_basis_v10.md`, nový
SHA-256 `520db73c4d162e52b6dca916c7f65ab371cea20f4fce94dad07f257bf25c8960`):
proxy `FLOOR_interior` má vrch na +0,494, ale deklarovaná úroveň podlahy
(prahy, vstupné schody, spodná hrana skla) je +0,45. Platí +0,45: proxy
podlaha sa skryje a ponechá, vlastná podlaha ju nahradí v rovnakom
pôdoryse. Všetky úrovne podkladu ostávajú, schodisko 16 × 0,175 m. Pôvodne
som zvažovala opačné riešenie (ponechať +0,494); prerušená session došla
k tomuto a je konzistentnejšie s budovou.

Grant 04/01 (`04_implementation_00.md`): fresh-worker-session, rovnaký rez
a allowlist. Rozdiely oproti 03/01: žiadny git (identitu repozitára som
overila sama: HEAD `0f5f84579d88ee67bc0bacee74826ef02bea7452`, strážené
hashe a JSON sekcie sedia); podklad s Dodatkom 1; zvyšky po session 03 sú
v bráne s hashmi a nový Worker ich má najprv celé prečítať a potom prevziať,
opraviť alebo prepísať; report do `04_report_00.md`. Koncept 03/02 nebol
vydaný a jeho súradnice nie sú spotrebované.

## 2026-11-17 22:13–22:25 — zosúladenie reportu 04/01 (rez 1, pilot rozloženia)

Worker 04/01 dokončil prácu a report si zapísal sám: `04_report_00.md`,
SHA-256 `c8a9763e5ed80ddefce270963058f434c9aefc2147a0fa415f12da2cbe7c1d5c`,
stav PARTIAL.

Čo som overila sama:

- hashe modulu, nástroja, parametrov, oboch študijných scén, `checks.json`
  a všetkých deviatich PNG sa zhodujú s reportom;
- chránené vstupy majú pôvodné hashe (`build_scene.py`, `design.py`, v03,
  v08_view); v projekte sú nové iba tri nesledované zdrojové súbory V10
  a ignorovaný `work/v10/`; HEAD ostal `0f5f8457…`;
- `jobs.jsonl`: 58 záznamov, 35 renderov, všetky exit 0, najviac 1,88 GiB
  RSS a 80,6 s;
- `checks.json`: všetky kontroly `pass` okrem `cold_open`;
- všetkých deväť obrázkov som si pozrela.

Odchýlky a moje rozhodnutia:

- **Strop 30 renderov prekročený na 35.** Podľa Workera klient dve dávky
  spustil dvakrát; príčinu som neoverovala. Joby boli sériové, na CPU, za
  strážou RAM, bez viditeľnej škody. Beriem to ako zaznamenanú odchýlku;
  do ďalšieho grantu dám poistku v launcheri (odmietnuť už zapísaný label).
- **Chýba malý snímok kontroly cold open.** Počítacia časť prešla v novom
  procese a osem finálnych renderov bežalo každý v novom procese nad
  uloženou scénou. Na účel tohto rezu (podklad pre Michalovo posúdenie
  rozloženia) to stačí; samostatnú opravnú výmenu nevydávam. Stav rezu
  ostáva PARTIAL, nie PASS.
- **Krokvy a svetlá výška galérie.** Pod priznanými krokvami je na okraji
  pásu 1,887 m; 2,0 m platí medzi krokvami, pod krokvami v y 2,31–6,09.
  Krokvy ponechávam a pás na státie zúžim na y 2,31–6,09 (dodatok k podkladu
  pri ďalšom grante). Moja rezerva 0,20 m vychádzala zo `SOFFIT_wood`, nie
  zo spodku strešnej škrupiny; chybu v podklade priznávam.
- Ostatné konflikty (1 mm od povrchu podlahy, hlava otvoru v hrúbke strechy,
  koniec okrajového trámu, voľný pás pri nástupe 1,05 m) prijímam, ako sú
  postavené.

Vlastný pohľad na obrázky: rozloženie je čitateľné a z C1 je cez presklený
roh vidno krb s ohňom a niku na drevo, cez štít schodisko a luster. Slabé
miesta: krbové teleso pôsobí ako tehlový stĺp uprostred miestnosti a z hero
pohľadu oheň takmer nevidno; nábytok je hmotový; za oknami je zástupná
krajina. Nič z toho nie je vizuálne prijatie; to patrí Michalovi.

Obrázky som skopírovala do `evidence/slice1/` (bajtovo zhodné s
`work/v10/evidence/`).

## 2026-11-17 22:30–22:45 — Michalove rozhodnutia k pilotu a grant 05/01

Michal po pozretí pilotných obrázkov rozhodol: rozloženie sedí a mám
pokračovať rezom 2; krb si ponechá tvar a dostane skutočný sivý skladaný
kameň; presklený roh ostáva široký 1,5 m s lavicou a ornamentom. Je to
prijatie rozloženia, nie vizuálne prijatie interiéru.

Do `evidence/design_basis_v10.md` som pridala Dodatok 2 (tieto rozhodnutia,
pás na státie y 2,31–6,09, prijaté odchýlky stavby); nový SHA-256
`23d06f085df0f831731adecf552b75129d9251fc770f5626d16624ce918c822e`.

Grant 05/01 (`05_implementation_00.md`): fresh-worker-session, rez 2 —
CC0 PBR textúry a modely z Poly Haven, dopracované procedurálne kusy tam,
kde katalóg nič nemá (rohová sedačka, koberec, oblúková lampa, polienka,
kuchyňa), vierohodný oheň, rovnaká sada kamier znovu vyrenderovaná plus
C1 za súmraku a tri porovnania so rezom 1. Novú session som zvolila preto,
lebo session 04 má za sebou dlhý beh; kontext získa z kódu a reportu.

Rozdiely oproti rezu 1: povolená sieť iba na `api.polyhaven.com` a jeho
sťahovací host, rozpočet 700 MB, nové súbory v `assets/interior_v10/`
s vlastným slovenským manifestom (existujúci `assets/ASSET_MANIFEST.md`
ostáva nedotknutý, lebo na projekte bežia ďalšie session); launcher musí
najprv dostať poistku proti dvojitému spusteniu a tvrdý strop 30 renderov;
rez 1 sa pred zmenami zachová v `work/v10/slice1/`; kontrola cold open
vrátane snímky je povinná. Bez gitu, MCP, GUI a GPU. Na stroji teraz
bežia aj exteriérové joby V11 (`work/v11/`), stráž RAM a sériovosti ich
zohľadňuje. Splniteľnosť: vstupy majú overené hashe, `assets/interior_v10/`
neexistuje, dostupná RAM pri vydaní asi 12 GiB.

## 2026-11-17 22:20 — oprava časových údajov v poznámkach

Niektoré časy v nadpisoch vyššie som odhadla, namiesto aby som ich
odčítala z hodín, a dva sú preukázateľne nesprávne (ležia v budúcnosti
voči commitom). Staršie zápisy neprepisujem; platí táto oprava podľa časov
commitov v Meta a hodín stroja:

| Zápis | Uvedené | Skutočnosť |
|---|---|---|
| zosúladenie reportu 02/01 | 20:22–20:35 | hotové pred commitom `dd9e992` o 20:32:21 |
| prerušenie 03/01 a grant 04/01 | 20:50–21:10 | hotové pred commitom `199a8cf` o 21:05:20 |
| zosúladenie reportu 04/01 | 22:13–22:25 | 22:13–22:15 (commit `e07a95f` o 22:14:49) |
| rozhodnutia k pilotu a grant 05/01 | 22:30–22:45 | 22:15–22:19 (commit `a568b2f` o 22:18:47) |

Rovnako Dodatok 2 v `evidence/design_basis_v10.md` nesie čas 22:35;
vznikol okolo 22:17. Súbor teraz nemením, lebo bežiaci grant 05/01
odkazuje na jeho hash; opravím to pri najbližšej zmene podkladu.

Worker 05/01 bol vydaný okolo 22:19 a o 22:19:42 preukázateľne pracuje
(prepis rastie); na disku zatiaľ nič nové.

## 2026-11-17 23:08 — pád session 05/01 a grant 06/01

Session 05/01 klient ukončil o 22:47 chybou `Other Models usage limit
reached`. Report neexistuje. Záznam som napísala ja ako
`05_interruption_00.md`. Súradnice 05/01 sú spotrebované.

Stihla: CC0 aktíva (293 MB, `assets/interior_v10/`, slovenský manifest),
modul s materiálmi a nábytkom, apply a kontroly. Geometria, idempotencia,
svedkovia a textúry prešli. Tri kontroly nie: lúč z C1 na medzipodestu
schodov trafí kreslo; tri rastliny na galérii sú vnútri otomanu; kuchynská
linka zasahuje do uličky o 4 mm. Žiadny render rezu 2. Rez 1 je zachovaný
v `work/v10/slice1/` s pôvodnými hashmi.

V Dodatku 2 podkladu som opravila nesprávny čas 22:35 na „okolo 22:17“.
Rozhodnutia sa nezmenili. Nový SHA-256
`4901cdc0da78c5cb7b64992ee3eaa76bc5d3885d7b90f1e730b2be3bc40a2870`.

Grant 06/01: fresh session, rovnaký rez. Žiadne sťahovanie. Opraví tri
namerané zlyhania najmenším posunom, doženie cold open a vyrenderuje sadu
pohľadov. Strop 30 renderov ostáva, doteraz sa minulo 0. Bez gitu, siete,
MCP a GPU.
