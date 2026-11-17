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
