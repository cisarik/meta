# 01_closure — V19 · Pivnica v samostatnom interiéri

**CELOK UZAVRETÝ ORCHESTRÁTOROM**

**24. 11. 2026 · Orchestrátorka celku · `kysucka-moderna-chata-basement-layout-study-v19`**

Celok **V19** (`kysucka-moderna-chata-basement-layout-study-v19`) je dokončený, prijatý Michalom (**PASS** na všetkých akceptačných bodoch `V19-A1` až `V19-A4`) a formálne uzavretý Orchestrátorkou celku. Na základe porovnania zameraných variantov v natívnom Plan Mode (`01_report_01.md`) Michal vybral **Variant A — vnútorný vstup zo zázemia**, ktorý bol následne zrealizovaný a overený v samostatnej pracovnej kópii interiéru `work/v19/kysucka_chata_interier_pivnica_v19.blend` (`01_report_02.md`).

---

## 1. Zhrnutie rozhodnutia o variante a výslednej dispozície (Variant A)

| Parameter | Variant A · Vstup zvnútra zo zázemia *(Prijatý a zrealizovaný)* | Variant B · Vstup od západného prístrešku *(Porovnaný v pláne)* |
|---|---|---|
| **Nástupná → výstupná kóta** | **`+0,451 m → −2,250 m`** (prevýšenie **`2,701 m`**) | `−0,055 m → −2,250 m` (prevýšenie `2,195 m` z terénu) |
| **Prístupová trasa od vstupu D01** | Priamo zvnútra cez `01 Zádverie` / `04 Chodba`, horná podesta `1,100 × 0,900 m` (`X = 7,160–8,260; Y = 2,450–3,350 m`) | Vonkajšia obchádzka okolo koruny jablone (`34,17 m` od `D01`) |
| **Schodisko** | Priame jednoramenné schodisko na západ (os `Y = 2,925 m`): **14 výšok × `192,9 mm`**, 13 nášľapov × **`240 mm`** (`2h + g = 625,9 mm`), sklon **`38,8°`**, dĺžka **`3,120 m`**, čistá šírka **`0,810 m`** | Priame schodisko na sever v prístrešku (`13 × 168,8 mm / 285 mm`, sklon `30,6°`, šírka `1,050 m`) |
| **Otvor v doske `BASE_slab`** | Vnútorný výrez `X = 3,830–7,100 m`, `Y = 2,480–3,340 m` (**`3,270 × 0,860 m = 2,8122 m²`**) | Výrez v prístrešku `6,552 m²` vrátane prerušenia západnej hrany sokla o `1,200 m` |
| **Svetlá výška na najhoršom mieste** | **`2,180 m`** v oboch dverných nadpražiach; **`2,197 m`** pri západnej hrane otvoru dosky (`X = 3,830 m` s predklonom hlavy `0,350 m` zo stupňa č. 13); **`2,390 m`** v sklade B1 (`−2,250 → +0,140 m`) | `2,180 m` v podzemnom nadpraží; `2,281 m` pri hrane dosky (`1,939 m` pod existujúcim presahom strechy pri hlavnom vstupe) |
| **Priechodnosť chodby `04` a zázemie** | Posuvné dvere do puzdra (`0,790 × 2,180 m` na `X = 7,080 m`, posuv `0,920 m`) nechávajú celú chodbu `04` (**`1,150 m`**) aj portál zádveria `01` (**`1,100 m`**) plne voľné (odstup `0,2025 m`). Izby `05` (`10,18 m²`) a `06` (`9,83 m²`) sú bez zmeny; `02 Technická miestnosť` má **`2,81 m²`** a `03 Kúpeľňa / WC` **`2,94 m²`** (s bočnou prístupovou chodbičkou `1,050 / 0,800 m`) | `0,00 m²` úbytku v interiéri, úbytok `6,552 m²` krytej plochy západného prístrešku |
| **Pivnica B1** | Hrubý pôdorys `X = 2,700–7,400; Y = 2,280–5,700 m` (**`16,07 m²`**); dolná podesta **`1,080 × 0,980 m`**; čistý sklad **`4,300 × 1,900 m = 8,17 m²`** so svetlou výškou **`2,390 m`** | Hrubý pôdorys pod chatou `10,07 m²`, čistý sklad `3,300 × 2,250 m = 7,43 m²` |
| **Zásah do spoločnej obálky (289 častí) a viditeľného sokla** | **`0,00 m` zásahu do vonkajšieho obvodu `BASE_slab`**. Výrez aj podterénne steny v `0,255 m` medzere začínajú na `Y = 2,480 m` (`20,36 mm` za konzervatívnym dosahom lúča nízkej južnej kamery `Záber 03` pod 25 mm skosením dosky). Nulová viditeľná zmena z exteriérových kamier. | Prerušenie západnej hrany sokla o `1,200 m`, zmena pozadia `0,255 m` medzery na `3,600 m` a zábradlie viditeľné v `Záber 04` a `Záber 05` |

---

## 2. Technické a vizuálne overenie realizovanej štúdie (`01/03`)

1. **Kolekcia `56_BASEMENT_V19` a označené študijné kópie (`slab_envelope_diff.json`):**
   - V pracovnej kópii `work/v19/kysucka_chata_interier_pivnica_v19.blend` (`425 401 183 B`, SHA-256 `d9021ee49f63a6dc595214932485597b3b47186b6e26487065c87964dc5dcdf8`) vlastní kolekcia `56_BASEMENT_V19` 557 objektov štúdie.
   - Všetkých 289 pôvodných objektov spoločnej obálky (`model/shared_envelope_v18.json`) si zachovalo presný súhrnný digest `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50` (`0` odchýlok); 8 nahradených originálov je skrytých a evidovaných vo `v19_hide_registry`.
   - Študijné kópie `BASE_slab_V19_STUDY` (`56 → 64` vrcholov, `108 → 128` trojuholníkov), `V10_FLOOR_oak_V19_STUDY` (`4 → 8` vrcholov, `2 → 8` trojuholníkov) a `V11_TERRAIN_NEAR_V19_STUDY` (`34 263 → 34 270` vrcholov, `67 918 → 67 854` trojuholníkov) majú mimo vnútorného výrezu nulovú odchýlku vrcholov, normálov aj UV.
2. **Dôkaz spojitého 3D priechodu (`walk_clearance_v19.json`):**
   - Kontrolný valec postavy (`priemer 0,700 m × výška 2,100 m`, `792` vzoriek s krokom `≤ 0,045 m` proti `518 815` trojuholníkom) prešiel všetkými 6 trasami (zostup do B1 a obídenie otvoreného krídla dverí do skladu, súbežný priechod zo zádveria cez hlavnú chodbu do dennej zóny pri zatvorených, otvorených aj posúvaných dverách, odbočky do izieb `05` a `06` a bočná chodbička do `03 Kúpeľňa / WC` a `02 Technická miestnosť`) s **`0` kolíziami** a minimálnou bočnou rezervou `15,42 mm`.
3. **Offline prenosnosť a idempotencia (`cold_portability_v19.json`):**
   - Kópia scény sa otvorila za studena v izolovanom `bwrap --unshare-net` sandboxe s `0` externými knižnicami, `0` linkovanými ID, `262` dekódovanými zabalenými obrázkami, otváracou snímkou `181` na kamere `Záber 07 | Obývačka a krb` a zachovaným podkladom `56_BASEMENT_V18` / `V18 | Podklad pre pivnicu`. Opätovné spustenie `work/v19/build_basement_v19.py` je idempotentné.
4. **Prezentačné zábery a kontrola fixných kamier (`renders/`):**
   - `zaber_nastupu_v19.png` (`1920 × 1080`, 128 vzoriek, Cycles OptiX + OIDN Accurate/High, AgX/None) zobrazuje nástup z prízemia cez otvorený portál posuvných dverí po 14 dubových stupňoch s madlom a prechodom omietky do kamenného muriva B1.
   - `zaber_b1_pivnica_v19.png` (`1920 × 1080`, 128 vzoriek) zobrazuje kamennú pivnicu B1 s dreveným stropom, veľkoformátovou dlažbou, podschodiskovými dubovými skrinkami, podsvietenými dubovo-oceľovými regálmi s fľašami vína, nádobami, prúteným košom a debničkami s jablkami a vpravo priehľad cez otvorené presklené dvere na podsvietené dubové stupne schodiska.
   - `porovnanie_fixnych_kamier_v19.png` (`2040 × 2603`) dokladá zachovanie obývačky (`Záber 07`), galérie (`Záber 08`), vstupného pohľadu (`CAM_V10_ENTRY`) a priehľadu oknom do údolia (`CAM_V05_VALLEY_INSIDE`) bez geometrickej regresie a bez úniku svetla z pivnice.

---

## 3. Nápady na budúce doladenie (Final Touch / kandidáti pre ďalšie interiérové celky)

Pri záverečnej vizuálnej inšpekcii záberov `zaber_b1_pivnica_v19.png` a `zaber_nastupu_v19.png` som spísala päť konkrétnych návrhov, ktoré možno využiť pri budúcom povýšení pivnice do hlavného interiérového súboru alebo v ďalšom interiérovom celku (tieto body sú zaznamenané ako neautorizujúce návrhy na ďalší rozvoj a neotvárajú novú mutáciu v uzavretom celku V19):

1. **FT-V19-01 · Otočenie pántov presklených dverí B1 k západnej stene (`X = 2,950 m`):**
   - V aktuálnej štúdii majú dvere do skladu B1 (`X = 2,950–3,890 m, Y = 3,600 m`) pánt na východnej strane `(3,910; 3,600)`, takže pri otvorení o 90° dovnútra skladu stojí zvislý dubový rám krídla v priestore na `X = 3,91 m` (v ľavej tretine záberu `zaber_b1_pivnica_v19.png`). Premiestnenie pántu na západné ostenie `(2,950; 3,600)` s otváraním krídla k západnej kamennej stene (`X = 2,900 m`) úplne vyčistí priehľad do pivnice, sprístupní celý severný regál priamo od prahu dverí a umožní vrátiť prvému regálovému modulu plnú hĺbku `0,381 m`.
2. **FT-V19-02 · Odstránenie uhlopriečneho UV švu na drevenom strope B1 a priznané 3D stropné trámy:**
   - Na podhľade stropu B1 (`+0,140 m`) v `zaber_b1_pivnica_v19.png` je viditeľný uhlopriečny prechod textúry/normálovej mapy medzi dvoma trojuholníkmi stropného obdĺžnika. Nahradenie jednej plochy jednotlivými 3D stropnými doskami s priebežným mapovaním vlákien a priznanými profilovanými dubovými trámami s teplým LED podsvietením v škárach pri kamennej stene výrazne zvýši kvalitu hornej časti obrazu.
3. **FT-V19-03 · Tretí kamerový uhol z úrovne očí v chodbe/zádverí a teplejšie nasvietenie horného nástupu:**
   - Kamera `CAM_V19_STAIR_ENTRY` sa pozerá strmo dole do šachty (medián luma `31,32`), takže dubová podlaha `+0,451 m` v popredí je tmavšia. Pridanie teplého nástenného svietidla pri hornej podeste, zvýraznenie teplých LED pásikov pod nosmi všetkých horných stupňov a doplnenie tretej kamery z úrovne očí v chodbe `04` (ukazujúcej otvorené puzdrové dvere do pivnice v kontexte zádveria a priehľadu do obývačky) vizuálne prepojí prízemie so zostupom do B1.
4. **FT-V19-04 · Bohatší mikro-detail vínnej a komorovej výbavy v B1:**
   - Nahradenie jednoduchých valcových nádob na ľavých policiach tvarovo pestrejšími sklenenými pohármi s indexom lomu a odleskami, doplnenie etikiet a korkov na fľašiach vína, jemného plamienka v drevenom lampáši na východnom pulte a tkaného behúňa na kamennej dlažbe posunie pivnicu na úroveň špičkovej horskej vinotéky a komory.
5. **FT-V19-05 · Povýšenie do kanonického `blender/kysucka_chata_interier.blend` a detailné stvárnenie kúpeľne `03` a spální `05/06`:**
   - Kanonický súbor `blender/kysucka_chata_interier.blend` (`c607cb21...`) zostal v tomto celku zámerne nedotknutý a štúdia je uložená v `work/v19/kysucka_chata_interier_pivnica_v19.blend` (`d9021ee4...`). V nadväznom interiérovom celku možno schválenú pivnicu povýšiť do `blender/kysucka_chata_interier.blend` a detailne vymodelovať aj interiér kompaktnej kúpeľne `03` (`2,94 m²`), technickej miestnosti `02` (`2,81 m²`) a oboch severných izieb `05` (`10,18 m²`) a `06` (`9,83 m²`).

---

## 4. Identita kľúčových artefaktov a záznam uzavretia

| Artefakt | Úloha | SHA-256 |
|---|---|---|
| `blender/kysucka_chata_interier.blend` | Zachovaný kanonický predchodca interiéru z V18 (01/06) | `c607cb21fbdb289b49f05596004b403e7dd5f96a64e900ce42ed8485f6a30449` |
| `work/v18/recovery/kysucka_chata_exterier_doladeny.blend` | Zachovaný denný exteriérový checkpoint (referencia pri fasáde) | `5e8ada70e99c70a3be0a7eea9b18306b422e4ef3a141a63b51b237b7957e3a24` |
| `model/shared_envelope_v18.json` | Spoločná obálka 289 častí (`aggregate_sha256` `87288303...`) | `e58959a22b2d1879828fe87cff645ec3f7ed99a28ec12ae66bfce01c4f6045b8` |
| `work/v19/kysucka_chata_interier_pivnica_v19.blend` | Pracovný kandidát interiéru s pivnicou V19 (Variant A, 557 objektov v `56_BASEMENT_V19`) | `d9021ee49f63a6dc595214932485597b3b47186b6e26487065c87964dc5dcdf8` |
| `work/v19/build_basement_v19.py` | Deterministický a idempotentný zostavovací skript V19 | `44a08a32b324cf6d33ebb45d5b852c36b352bb23536cf7bce0e8cc6a6ad87df4` |
| `Meta/renders/zaber_nastupu_v19.png` | Prezentačný render nástupu schodiska (`1920 × 1080`) | `5c6674b112fb5c2ba589fe974e61ba23f90fa23852b4fd6a9f53802eefd92a8e` |
| `Meta/renders/zaber_b1_pivnica_v19.png` | Prezentačný render pivnice B1 (`1920 × 1080`) | `257e93059aa0667b3ebd3d6061fb57431f20627efd9a8726581b2fc844f62334` |
| `Meta/renders/porovnanie_fixnych_kamier_v19.png` | Kontaktné porovnanie 4 fixných kamier Pred V18 vs Po V19 (`2040 × 2603`) | `87e4db557e1558c28501da674086ee256eb6df9f12fd7f9f43ea10e12e9ab56d` |
| `Meta/evidence/podorys_prizemia_v19.svg` | Aktualizovaný pôdorys prízemia zo zostaveného 3D modelu | `9e61f69a55a4bbf8111439c2140b1b02e2cef4b5e28c958f089f34f97ab59e61` |
| `Meta/evidence/podorys_b1_v19.svg` | Aktualizovaný pôdorys B1 zo zostaveného 3D modelu | `fd186e9e482b9b90387af5b5498167e9627a27d1c5d59977b77eda68a862d2b5` |
| `Meta/evidence/rez_aa_v19.svg` | Aktualizovaný rez A–A cez schodisko, dosku a terén | `24b4f8ab81e8583881aee979ead25ad622afbe75c778e51dabdc03875a9871eb` |
| `Meta/evidence/slab_envelope_diff.json` | Presný diff študijných kópií dosky/podlahy/terénu a 289 prvkov obálky | `aef9702d53f58638d6510732abc758598a94b6e7d006f1816e12ba955b03e837` |
| `Meta/evidence/walk_clearance_v19.json` | Dôkaz spojitého priechodu `0,700 × 2,100 m` cez 6 trás (`792` vzoriek, `0` kolízií) | `5cba280c8d164fcb7ec85eef85f4d70189364e24e07bd528505d3ba93f4a4f35` |
| `Meta/evidence/cold_portability_v19.json` | Dôkaz offline studeného otvorenia v `bwrap --unshare-net` a idempotencie | `d0bcd94733a072cb705f66b5ff2b26d18b74a738454743f52c0924934634a3d6` |
| `Meta/00_handout.md` | Zmrazený provizórny handout V19 | `b499e05fdcd799b3510117104f0c2a490e7a81d6431f054a2507d76837ab28f7` |
| `Meta/01_planning_00.md` + `Meta/01_report_00.md` | Prvá výmena `01/01` (BLOCKED na preflight environment pinoch) | `4e317d1acca9383bc3d2677b0fb24b8eb86d727136c75a2ec254cd6228c690e5` / `73ef1865dbca0aebfefe857b191b2b9549894ab213d268f7b72b407e6b05ec25` |
| `Meta/01_planning_01.md` + `Meta/01_report_01.md` | Opravený úvodný plánovací cyklus `01/02` (PASS, porovnanie Variantov A a B + 8 SVG schém) | `90c5752ce5c5c0802befcc55a0aae8be720cc917a03cf808bf2d8ce35081263c` / `8f1f7f5766b591ad4ce24ecc3a9406773b6b9d61e21c3fd657cc46add44d04d5` |
| `Meta/01_implementation_02.md` + `Meta/01_report_02.md` | Realizačná výmena `01/03` (implementation-PASS, Variant A v pracovnej kópii interiéru) | `21b0998c5ad960f0d6bb0b42954c0a607f493c88a872cd593347f1b3776209a3` / `fbca525872b916e74b507ffda1f68dada872a1b4217a0a2ff9b9a43169af59d5` |

```text
Declared closure signal: CELOK UZAVRETÝ ORCHESTRÁTOROM
Signal owner: orchestrator
Worker emission of closure signal: prohibited
Phase-qualified result: acceptance-PASS
Result artifact or commit: work/v19/kysucka_chata_interier_pivnica_v19.blend (SHA-256 d9021ee49f63a6dc595214932485597b3b47186b6e26487065c87964dc5dcdf8) at project commit f600c7a8e69a23a029559872652302ac299c2aea
Result evidence: 01_report_01.md (8f1f7f57...), 01_report_02.md (fbca5258...), zaber_nastupu_v19.png (5c6674b1...), zaber_b1_pivnica_v19.png (257e9305...), porovnanie_fixnych_kamier_v19.png (87e4db55...), podorys_prizemia_v19.svg (9e61f69a...), podorys_b1_v19.svg (fd186e9e...), rez_aa_v19.svg (24b4f8ab...), slab_envelope_diff.json (aef9702d...), walk_clearance_v19.json (5cba280c...), cold_portability_v19.json (d0bcd947...)
Accepted evidence: porovnávacia štúdia Variantov A a B (01/02 PASS), 3D realizácia Variantu A v work/v19/kysucka_chata_interier_pivnica_v19.blend (01/03 implementation-PASS), diff študijnej kópie dosky so zachovaním 289 objektov spoločnej obálky (87288303...), 6-trasový 3D dôkaz priechodu 0,700 x 2,100 m (0 kolízií), offline studené otvorenie, porovnanie 4 fixných kamier a dva 1920x1080 prezentačné rendery prijaté Michalom ako PASS
Required preceding results: satisfied
Cooperator-owned decisions: satisfied — Michal vybral Variant A, prijal výsledok ako PASS a udelil pokyn na uzavretie celku V19
Residual-risk disposition: satisfied — návrhy na budúce vizuálne a dispozičné doladenie (FT-V19-01 až FT-V19-05) sú zdokumentované vyššie; kanonický blender/kysucka_chata_interier.blend (c607cb21...) ostáva zachovaný
Upgrade-ledger reconciliation: complete (v AGENTS.md nie je deklarovaný žiadny AP upgrade ledger)
Active-context reconciliation: complete
Active mutation: none (všetky Worker granty expirovali, žiadny Blender proces nebeží, projektový Git strom je čistý na f600c7a8e69a23a029559872652302ac299c2aea)
Closure authority: present
Implementation completion: implementation-PASS
Audit completion: not-required (E2 lokálna vizualizačná štúdia v pracovnej kópii s kompletným diffom, walk-envelope, cold-open a regresným dôkazom)
Publication: not-applicable (mimo rozsahu celku; Git archiváciu v Meta vlastní COOPERATOR)
Public Git equality: not-applicable
Orchestrator acceptance: acceptance-PASS
Closure actor: ORCHESTRATOR
Logical-whole closure: closed-by-ORCHESTRATOR
```

### Podklad pre zosúladenie Master run map (`projects/kysucka_moderna_chata/00/00_RUN_MAP.md`)

```text
Run entry: 19 | kysucka-moderna-chata-basement-layout-study-v19 | closed | depends on: kysucka-moderna-chata-split-and-forest-realism-v18 | handout: projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/00_handout.md | evidence: Variant A interior service-zone basement study accepted PASS in work/v19/kysucka_chata_interier_pivnica_v19.blend d9021ee49f63a6dc595214932485597b3b47186b6e26487065c87964dc5dcdf8 with 289-part envelope intact, 0-collision walk proof, updated SVGs, and 1920x1080 showcase renders archived in 00/19-basement-layout-study-v19/01_closure.md
```
