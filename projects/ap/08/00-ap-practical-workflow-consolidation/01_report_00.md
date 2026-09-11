### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: ap-practical-workflow-consolidation
Worker session ordinal: 01
Worker exchange ordinal: 01
Standard terminal status: PARTIAL
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence
```

**Toto je úplná finálna verzia plánovacieho reportu a plánu. Nahrádza predchádzajúci návrh v chate.**

**Požadovaný súbor som nezapísal.** Aktívny Native Plan Mode zakazuje zápis súborov aj pri výslovnom povolení Cooperatora. Vaše posledné povolenie zohľadňujem v presnom postupe opravy cieľového `01_report_00.md`; jeho vykonanie vyžaduje prostredie, v ktorom je zápis povolený. Status PARTIAL pravdivo označuje nedokončené súborové odovzdanie.

| Súčasť reportového jadra | Overený výsledok |
|---|---|
| AP, počiatočný a konečný commit | `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` |
| Meta, začiatok pôvodného plánovania | `6a5f3b421905f5a3fdb262024195a3d1c7897549` |
| Meta, konečný overený commit | `9c6733d4a116bf8cfa3ae28ffe34a9a6292b6e41` |
| Verejné referencie pri záverečnej kontrole | AP aj Meta `main` zodpovedajú uvedeným konečným lokálnym commitom |
| Moje zmeny súborov | Žiadne |
| Git operácie s mutáciou | Žiadny fetch, checkout, staging, commit ani push |
| Validácia | Cielené čítanie, Git porovnania, kontrola vlastníkov pravidiel, historických tvrdení, ciest, súradníc a obsahu cieľových súborov |
| Testovacie sady | Nespustené; táto úloha bola repository-grounded plánovanie |
| Delegovanie | Nepoužité |
| Zostávajúca prekážka odovzdania | Zápis nie je v aktívnom režime povolený; existujúci cieľ obsahuje nesprávny artefakt |
| Najmenší ďalší krok | Technicky uložiť tento zmrazený report podľa presného postupu v sekcii 6, bez nového plánovania |
| Zánik oprávnenia | Tento report končí plánovaciu úlohu. Neudeľuje implementačné, acceptance, publication ani closure oprávnenie |

# AP: finálny plán praktickej konsolidácie

## 1. Zhrnutie a overená diagnóza

Odporúčam **jednu súdržnú dokumentačnú zmenu existujúceho AP**, ktorá:

- zachová tri trvalé roly a jediného sémantického vlastníka;
- zavedie povinného prvého manuálneho Plannera v skutočnom Native Plan Mode;
- zachová raz vybranú následnú delivery trasu;
- oddelí autorstvo, uloženie, vyhodnotenie a Git publikovanie;
- skráti povinný základ pre bežného Workera;
- spojí nové testy s konkrétnou dôležitou medzerou v dôkazoch;
- sprevádzkuje špecialistov prostredníctvom existujúcich capability a routing kontraktov;
- posilní kontinuitu handoutov a povinnú stručnú orchestration critique.

Nevznikne ďalší protokolový manuál, nová trvalá rola, univerzálny workflow register ani nový vykonateľný validačný mechanizmus.

### Čo dnešné AP už rieši

Aktuálny pin obsahuje primeranú validáciu, konečný plánovací rozpočet, obnovovanie oprávnenia v zdravej relácii, nezávislé prijatie, minimum čítania podľa roly, restoration readiness review a kontrolu integrity reportového companionu. Tieto mechanizmy treba upraviť a prepojiť, nie zaviesť druhýkrát.

Podstatné zmeny majú jasných existujúcich vlastníkov:

| Oblasť | Aktuálny problém | Vlastník |
|---|---|---|
| Plánovanie | Risk-driven plánovanie nezaručuje prvého Plannera každého nového celku | [Orchestration Planning and Implementation Planning](/home/agile/Projects/ap/AP.md:872) |
| Doručovanie | Predvolený agentový dispatch nezodpovedá novému pravidlu manuálneho začiatku a jednorazovej voľby | [RF-02](/home/agile/Projects/ap/AP.md:152), §3 |
| Ukladanie | RF-19 všeobecne zakazuje Workerovi self-archival | [RF-19](/home/agile/Projects/ap/AP.md:339) |
| Plánovací report | Oprava chýbajúceho reportu nepokrýva presne autorizované uloženie | [Planner-Artifact Report Completion Repair](/home/agile/Projects/ap/PROMPT_CONTRACTS.md:123) |
| Čítanie | Worker spine existuje, ale stále vyžaduje rozsiahle čítanie | [Per-Role Minimum-Reading Spine](/home/agile/Projects/ap/AP.md:63) |
| Signály | Voliteľný projektový profil nezaručuje viditeľné informačné minimum | Communication Routing |
| Testy | Existujúce pravidlo treba spresniť pri nových testoch a aplikovateľnosti projektových brán | [Validation and Public Verification](/home/agile/Projects/ap/AP.md:2052) |
| Handouty | Overovanie existuje; slabým miestom je vykonanie, citácie a zachovanie prijatých rozhodnutí | [Session Rotation and Dynamic Prompts](/home/agile/Projects/ap/AP.md:2371) |

### Opravené historické premisy

- **Restoration readiness review existuje v starom aj aktuálnom AP.** Na starom pine `9c5cc44…` je príslušný odsek pri riadku 2308. D-13 preto nemožno implementovať ako doplnenie údajne chýbajúcej kontroly.
- **Veta „Your output is your REPORT, not a file“ sa v starom `PROMPT_CONTRACTS.md` nenachádza.** Skutočný zákaz Workerovho archivovania je však v RF-19 a jeho projekciách.
- Read-only acceptance môže potrebovať testy. Nulová zmena zdrojov sama neurčuje potrebný dôkaz.
- Aditívna zmena oprávnenia môže meniť predpoklady, spoločný stav aj riziko.
- Development alebo alpha status sám neudeľuje povolenie zmazať dáta.
- Workerovo interné delegovanie a Orchestrator-direct vykonávanie sú odlišné usporiadania.
- Rozdelenie práce podľa číselného rozdielu tierov alebo automatické vytvorenie testovacieho Workera nemá preukázanú úspornosť.

### Rozsah historickej kontroly

Prečítané boli celé koreňové Meta dokumenty `README.md`, `BRAINSTORMING.md`, `AP_DEFECTS.md` a `AP_DESTILLED.md`. AP archív 00–07 bol skontrolovaný inventárom a prehľadom nadpisov všetkých **135 Markdown súborov**, potom obsahovým čítaním relevantných plánov, reportov, opráv a uzavretí vo všetkých ôsmich skupinách.

Nešlo o úplné čítanie každého riadka celého archívu.

| Skupina | Podstatná historická skúsenosť |
|---|---|
| 00 | Opakované blokovanie na predpokladoch prostredia; formálne úspešné kontroly neskôr nezachytili chýbajúci požadovaný príklad. |
| 01 | Už existuje argumentácia pre kompaktné granty s citáciami a proti ďalším paralelným dokumentom. Identický pripravený prompt má precedens neblokujúceho rozpracovaného artefaktu. |
| 02 | Natívny plánovací artefakt bez štandardného reportu vyžadoval samostatné dokončenie. |
| 03 | Rovnaký problém sa zopakoval; [oprava zachovala pôvodný plán](/home/agile/meta/projects/ap/03/00-ap-cooperator-ergonomics-cost-proportional-execution-and-meta-trace-integration/01_report_01.md:24). |
| 04 | Oprava formátu bola potrebná aj pri acceptance reporte; samostatné historické statusové kroky pridávali ďalšie výmeny. |
| 05 | Delegovanie, Orchestrator-direct hranica a nezávislosť už majú rozdielne pravidlá. |
| 06 | Spine, detekovateľnosť pravidiel, prevod opakovaní na odkazy a notes už boli [prijaté](/home/agile/meta/projects/ap/06/05_closure.md:24). |
| 07 | Predvolený dispatch, integrita companionu a inicializačný signál sú aktuálne prijaté rozhodnutia, ktoré nová revízia musí explicitne zosúladiť. |

Libre Tiles bol skúmaný úzko pre konkrétne výhrady: [chyby allowlistov a inventárov](/home/agile/meta/projects/libretiles/13/00-multilingual-expansion-campaign/00_notes.md:1520), [neúplný vyhľadávací vzor](/home/agile/meta/projects/libretiles/13/00-multilingual-expansion-campaign/00_notes.md:1736), [chyby handoutu](/home/agile/meta/projects/libretiles/13/00-multilingual-expansion-campaign/00_notes.md:2209) a [explicitné clean-slate rozhodnutie](/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/00_notes.md:39). Stav aplikácie ani jej runtime výsledky som nezávisle netestoval.

## 2. Dispozičná matica

Klasifikácie: **A** už vyriešené; **S** stále relevantné; **P** čiastočne relevantné; **U** nepodložené alebo vyvrátené; **R** nahradené aktuálnou požiadavkou; **D** odložené s konkrétnym dôvodom.

### Trinásť aktuálnych požiadaviek

Všetkých trinásť požiadaviek tvorí záväzný smer tohto návrhu.

| Požiadavka | Stav na aktuálnom pine | Implementačné rozhodnutie |
|---|---|---|
| 1. Orchestrator / ChatOrchestrator | P | Pomenovať prístupové profily; schopnosti a vybranú trasu evidovať oddelene. |
| 2. Planner; tri trvalé roly | P | Používať `Planner`; zachovať COOPERATOR, ORCHESTRATOR a WORKER. |
| 3. Prvý Planner manuálne v Native Plan Mode | S | Povinný prvý Worker nového celku; raz vybrať následné doručovanie. |
| 4. Ďalší bounded Planner | P | Povoliť novú technickú otázku pri zachovaní prijatých rozhodnutí a rozpočtu opakovania. |
| 5. Spoľahlivé signály | P | Povinná krátka kapsula: emoji, adresát, relácia, delivery, reasoning, kontext a režim. |
| 6. Priame ukladanie Plannerom a Workermi | S | Povoliť presne autorizované uloženie podľa schopnosti klienta. |
| 7. Štyri zodpovednosti | P | Oddeliť autorstvo, persistence, reconciliation a Git publication. |
| 8. Meta mapovanie a artefakty | P | Zachovať mapovanie; doplniť notes, viac handoutov, closure a pokračovanie existujúceho celku. |
| 9. Kompaktné čítanie | P | Zúžiť normatívny Worker spine a ostatné čítanie aktivovať podľa úlohy. |
| 10. Kritické kauzálne testy | P | Každý nový test odôvodniť dôležitým správaním a medzerou v existujúcich dôkazoch. |
| 11. Špecialisti | S | Rozšíriť existujúce capability/routing kontrakty o použiteľné vstupy a výstupy. |
| 12. MEASURED / LEAD | S | Povinná stručná časť terminálneho reportu. |
| 13. Brainstorming a Continue | P | Interpretovať jasný kontext bez mikroapproval; nevytvárať tým nový Worker grant. |

### D-01 až D-18

| Defekt | Dispozícia | Rozhodnutie a hranica |
|---|---|---|
| D-01 | S | Zaviesť povinnú krátku orchestration critique. `none` je platný výsledok; netreba vyrábať nálezy. |
| D-02 | P | Kompaktné jadro už existuje. Rozsah reportu odvodzovať od rozhodovaného tvrdenia; nepridávať univerzálny limit slov ani neobmedzenú E3/E4 prílohu. |
| D-03 | P | Odstrániť neodôvodnenú rutinnú záťaž, ale neignorovať záväzné projektové brány. |
| D-03b | P | Pred vydaním promptu vyjasniť aplikovateľnosť brány na konkrétnu triedu práce. Nulová mutácia nie je automatická výnimka. |
| D-04 | P | Omission review existuje. Vyhľadávanie a inventár označiť podľa skutočného rozsahu; neúplný vzor nie je dôkaz absencie. |
| D-05 | P | Profily a Orchestrator-direct hranica už existujú. Prijať nové názvy; názov neudeľuje všeobecné implementačné oprávnenie. |
| D-06 | R | Staré tvrdenie o predvolenom zákaze Orchestrator dispatchu je zastarané. Nové pravidlo: prvý Planner manuálne, potom zachovaný výber Cooperatora. |
| D-07 | P | Spine a P19 už existujú. Zmenšiť povinný základ a umožniť citované granty aj čerstvým Workerom. |
| D-08 | P | Praktická výhrada voči ceremónii je použiteľná. Kauzálny vplyv názvu AP nie je preukázaný; názov sa nemení. |
| D-09 | P | AP už pracuje s cenou, kvótami, reasoning a kontextom. Nepotrebujeme paralelný povinný `Overhead budget`. |
| D-10 | U | Self-review a diagnostika môžu byť hodnotné. Neoznačujú sa za nezávislé prijatie; manuálna trasa nie je definíciou nezávislosti. |
| D-11 | D | Všeobecný dodatok s rovnakými súradnicami sa nezavádza: chýba bezpečné riešenie súbehu, zmeny predpokladov a už vykonaných účinkov. Použiť kompaktný úplný obnovený grant v zdravej relácii. |
| D-12 | P | Malé spoločné jadro zostáva. Rozsah príloh určuje claim a aktivované povrchy, nie rozsiahla všeobecná šablóna. |
| D-13 | P | Absencia readiness review je vyvrátená. Posilniť vykonanie existujúceho review: overené citácie, úplnosť prevzatých zoznamov a kontinuita. |
| D-14 | R | Absolútne „jednoslovná odpoveď nikdy nevyberá“ nahrádza aktuálna požiadavka. Jasné `A` môže vybrať možnosť; Continue pokračuje v existujúcom kroku. |
| D-15 | P | Viac handoutov už je dovolených. Doplniť lokálne názvy a explicitný vzťah k predchodcom; nepoužiť automatické latest-wins. |
| D-16 | U | Numerická tier-spread hranica nemá preukázanú optimálnosť. Deliť podľa oprávnenia, nezávislosti, spoločného stavu, schopností a ceny. |
| D-17 | P | Citovaná veta neexistuje, ale zákaz Workerovho archivovania áno. Nahradiť ho presne autorizovaným ukladaním vrátane Plannera. |
| D-18 | P | Skoro vyjasniť hodnotu dát a zachovať už prijaté rozhodnutie. Development status neudeľuje purge oprávnenie; percentuálne úspory nie sú overené. |

### Materiálne brainstormingové návrhy

| Návrh | Dispozícia | Rozhodnutie |
|---|---|---|
| Worker Orchestrator | P | Použiť existujúce explicitné interné delegovanie jedného zodpovedného WORKERa; žiadna ďalšia trvalá rola. |
| Šesť doplnkových reportových polí delegovania | P | Pri použitom delegovaní stručne uviesť podúlohy, dôvod rozdelenia, výsledky, rozpory, nedokončené úlohy a neoverené tvrdenia delegátov. Nevynucovať ich od ostatných Workerov. |
| Súbežné interné mutácie | A | Naďalej vyžadujú existujúcu bounded parallel výnimku a vlastníctvo ciest; samotné delegovanie nestačí. |
| Pilot delegovania na prekladovej úlohe | D | Neskorší experiment na aktuálnej vhodnej úlohe. Historický maďarský slice sa bez overenia dnešného stavu znovu neotvorí. |
| Viac handoutov | P | Prijať lokálnu konvenciu a kontinuitu. Nezavádzať univerzálny pás `9N` ani nový povinný integrity record. |
| Autonómny režim | P | Cooperator môže raz odložiť subjektívne prijatie na koniec. Technické a nezávislé dôkazy zostávajú podľa rozhodovaného tvrdenia. |
| Priame reporty bez Plannera | R | Aktuálna požiadavka zahŕňa aj Plannera. |
| Clean slate verzus migrácia | P | Rozhodnúť podľa hodnoty dát a konkrétneho oprávnenia; bez automatického purge defaultu. |
| Celý protokol má čítať iba Orchestrator | P | Orchestrator potrebuje širší prehľad, ale ani on nemusí rutinne čítať celý archív. Rozsah určuje konkrétna úloha. |
| Testy vždy ako samostatná výmena | U | Nezavádzať. Oddeľovať len pri konkrétnom prínose. |
| Nezávislosť vždy manuálne | U | Posudzovať skutočnú reláciu a vstupy. Manuálna trasa zostáva fallbackom. |
| Lacné priame Orchestrator vykonávanie | P | Zachovať už existujúcu RF-02 hranicu. Nerozšíriť ju na ľubovoľnú materiálnu implementáciu len pre zníženie počtu promptov. |

## 3. Odporúčaný protokolový dizajn

### A. Roly, prístup a dispatch

Zachovať tri roly:

- **Orchestrator:** ORCHESTRATOR s priamym prístupom k určenému pracovnému checkoutu projektu.
- **ChatOrchestrator:** ORCHESTRATOR pracujúci prostredníctvom Cooperatora a sprostredkovaných výsledkov; môže mať vlastné inšpekčné klony.
- **Planner, WebSearcher, DeepResearcher, ImageCreator:** WORKER profily alebo explicitne označené schopnosti.

Minimálne znenie vlastníka:

> “Orchestrator and ChatOrchestrator describe access profiles of the ORCHESTRATOR role. An inspection clone exposes its own checked-out and published state, not the Cooperator’s uncommitted working state. Profiles and capabilities never grant task authority.”

Existujúce pole `Capability profile` bude používať `Orchestrator | ChatOrchestrator`. Konkrétne schopnosti, oprávnenia a vybraná delivery trasa zostanú v existujúcich capability/routing poliach.

**Čerstvosť a nezávislosť sa posudzujú oddelene.**

> “Dispatch into a new concrete Worker session does not by itself prove independence. Execution inside a shared parent session is not a fresh Worker session; inherited parent conversation or reasoning disqualifies independent acceptance.”

Praktické dôsledky:

- Bežný dispatch doručí celý prompt do novej konkrétnej relácie; preferuje sa doručenie bez rodičovského transcriptu.
- Samotné vyvolanie dispatch nástroja Orchestratorom neznamená, že prijímateľ beží v tej istej relácii.
- Interný delegát v jednom Worker run nie je samostatným nezávislým AP auditorom.
- Nový ordinal, worktree ani iný model nepreukazuje nezávislosť.
- Pri požadovanej nezávislosti sa overí samostatná relácia, neprítomnosť implementačnej účasti a obmedzenie vstupov na určený acceptance balík a repository truth.
- Ak trasa tieto vlastnosti nevie splniť, použije sa vhodná manuálna čerstvá relácia.

### B. Prvý Planner, ďalšie technické otázky a konečné plánovanie

**Prvým Workerom každého nového celku bude Planner v relácii 01**, doručený manuálne so skutočne aktívnym `Native planning mode: required`.

Read-only príprava Orchestratora môže predchádzať vydaniu promptu. Nesmie sa však použiť na vykonanie prvého implementačného slice namiesto Plannera.

> “Every new logical whole begins with one manually delivered Planner task in the client’s actual native planning mode. Prompt-level read-only instructions do not substitute for this required initial mode.”

Ak klient natívny režim nemá, úvodný Planner sa cezň nespustí. Orchestrator odporučí vhodný klient; požiadavku potichu nezmení na `not-used`.

Okolo prvého dispatchu sa Cooperatora raz opýta na následné manuálne alebo subagentové doručovanie. Výber sa zachová po celý celok aj cez handouty. Kým výber nie je známy, následná trasa zostáva manuálna. Neotvára sa opakovane bez materiálnej zmeny.

**Ďalší Planner je dovolený pre novú relevantnú technickú otázku**, nie pre každý implementačný detail.

> “A bounded follow-up Planner task may resolve a newly relevant technical decision within the accepted objective. It preserves unaffected decisions. Renaming a task does not reset the revision budget for the same unresolved decision.”

Spresniť existujúci Planning Record bez pridania ďalšieho typu záznamu:

- Pri prvom plánovaní nového celku zostávajú dnešné počiatočné hodnoty `none`.
- Pri prvom cykle dodatočnej technickej úlohy sa môže použiť `Planning cycle: initial`, ale `Prior planning report`, `Changed decision boundary` a `Preserved unaffected decisions` uvedú skutočné odkazy a obsah. Nebudú vynucovať nepravdivé `none`.
- `Targeted revision basis: none` v takom prípade znamená, že nejde o revíziu toho istého plánovacieho problému.
- Revizný cyklus toho istého rozhodnutia použije `targeted-revision`, jednu z existujúcich dôvodových hodnôt a zachovaný počet použitých automatických revízií.
- Nový názov úlohy nevynuluje rozpočet tej istej nevyriešenej otázky.
- Materiálne zmenený cieľ vytvorí nový logický celok; samotná nová technická otázka v pôvodnom cieli nie.

Dodatočné plánovanie môže pri nevhodnom klientovi používať výslovne zvolený read-only grant s `not-used`. Táto možnosť neplatí pre povinného prvého Plannera nového celku.

Ak prvému Plannerovi chýba kritický dôkaz, vráti konkrétne obmedzenie. Následný výskum môže dodať nový vstup pre jednu odôvodnenú revíziu. Implementácia nezačne, kým nie je prijatý dostatočný plán.

Plan UI approval ani hotový plán neudeľujú implementačné oprávnenie. Implementácia potrebuje nový úplný grant; zdravá rovnaká Worker relácia sa môže zachovať.

### C. Viditeľné odovzdanie práce

Pri každom vydaní promptu alebo handoutu sa zobrazí krátka kapsula:

```text
🟡 Pripravené na doručenie
Adresát: Planner · nová relácia · manuálne
Odporúčanie: High · približne 1M kontext
Klient: Native Plan Mode ON
Prompt: 01_planning_00.md
Report: 01_report_00.md
Git archivácia: až po dokončení reportu
```

Povinné informačné minimum:

1. emoji spolu s textovým stavom;
2. adresát a profil;
3. konkrétna nová alebo aktuálna relácia;
4. vybraná delivery trasa;
5. reasoning odporúčanie;
6. približná kapacita `~250k` alebo `~1M`;
7. požadovaný stav Native Plan Mode;
8. pri aktivovanom ukladaní presné ciele a archival stav.

Pre vykonávací prompt sa explicitne uvedie `Native Plan Mode OFF`. Pri špecialistovi sa doplní požadovaná schopnosť alebo režim.

Emoji sú prezentačný signál, nie oprávnenie. Priebežné „pripravené“ alebo „čaká“ sa nezamieňa s terminálnym PASS. Projekt môže lokalizovať text a rozšíriť prezentáciu, ale nesmie vynechať povinné informácie.

`Recommended context capacity` je odporúčanie. Pozorovaná kapacita a využitie zostávajú oddelené; nedostupná telemetria sa nevymýšľa. Nezavádzajú sa pevné tokenové stropy ani automatická rotácia podľa percent.

### D. Autorstvo, uloženie, reconciliation a Git

Nahradiť univerzálny zákaz self-archival explicitne ohraničeným persistence oprávnením.

> “An explicitly authorized capable actor may persist finalized artifacts at the named destinations. Persistence does not transfer authorship or confer reconciliation, acceptance, Git publication, or closure authority.”

| Činnosť | Vlastník |
|---|---|
| Autorstvo promptu | Orchestrator |
| Autorstvo Worker reportu | Worker vrátane Plannera |
| Fyzické uloženie | Aktér pomenovaný v konkrétnom grante |
| Reconciliation a prijatie výsledku | Orchestrator; potrebné nezávislé prijatie ostáva samostatné |
| Git commit/push Meta pri ChatOrchestratorovi | Cooperator |

Prvý Planner pri aktivovanej Meta trase pripraví presný prijatý prompt a celý terminálny report obsahujúci plán, ak to klient a grant umožňujú. Ostatní schopní Workeri ukladajú vlastné reporty priamo.

Existujúci delivery record sa rozšíri, bez nového paralelného záznamu:

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: <exact prompt filename>
Destination path: <exact directory>
Report filename: <exact report filename>
Prompt persistence owner: <named actor>
Report persistence owner: <named actor>
Git publication owner: <named actor>
Archival: wait-for-report | allow-now
```

Vydaný záznam obsahuje jednu skutočnú archival hodnotu. Povolenie zápisu musí byť zároveň súčasťou pozitívneho task scope; samotné uvedenie cesty oprávnenie neudeľuje.

**Pravidlá uloženia:**

- Overiť fyzickú cestu, symlinky a existujúce ciele.
- Identický pripravený prompt možno po overení použiť bez prepisu.
- Bežný Worker nesmie prepísať konfliktný report.
- Najprv dokončiť obsah; potom vykonať presný ohraničený zápis a readback.
- Nevytvárať prázdne placeholdery, ktoré sa neskôr prezentujú ako dokončené reporty.
- Úspešné uloženie potvrdiť až po overení.
- Uloženie vlastného reportu vykonať pred terminálnym odovzdaním. Po jeho odovzdaní Workerovo oprávnenie zaniká.
- Stage, commit a push zostávajú samostatne autorizované činnosti.

**Kontrola reportu musí overiť jeho význam, nielen rozdiel bajtov.**

Report musí obsahovať správny header, súradnice, kompaktné jadro a skutočný výsledok príslušnej úlohy. Cudzí handout, prompt, neúplný natívny plán ani interruption companion nie sú štandardným terminálnym reportom.

Štandardný header `### Report for ORCHESTRATOR_CHAT` sa nemení. Nové názvy profilov nevyvolajú zmenu tohto rozhrania.

Prvé Git pridanie nového správneho prompt/report páru zostáva spoločné a nastáva až po existencii reportu. Príprava súborov nie je Git archivácia.

Historické chyby sa riešia výslovne a prospektívne so zachovaním pôvodu. Konkrétne povolená oprava chybne umiestneného artefaktu nezakladá všeobecné oprávnenie prepisovať reporty.

### E. Uloženie pri obmedzeniach natívneho klienta

Použiť existujúci report-completion mechanizmus a rozlíšiť dve situácie:

1. **Plán existuje, štandardný report chýba.** Treba vytvoriť chýbajúci report nad nezmeneným plánom.
2. **Plán aj report existujú, súborové odovzdanie chýba.** Treba iba uložiť hotový obsah.

> “When client restrictions prevent authorized persistence, preserve the completed result through the available output mechanism. Persistence of an existing complete report does not require a new planning cycle.”

Predvolený najmenší postup:

- Ak už existuje schopný a autorizovaný persister, uloží hotový report bez nového Planner tasku.
- Ak treba nový Worker grant na rendering alebo uloženie, ide o presnú completion výmenu s novými súradnicami podľa skutočnej relácie.
- `Native planning mode: not-used` v completion výmene neudeľuje implementačné oprávnenie.
- Zmena zmrazeného plánu, implementácia, acceptance a publication zostávajú zakázané.
- Pôvodný report ani jeho status sa spätne neprepisujú preto, aby vyzeralo, že uloženie prebehlo skôr.
- Ak presný pôvodný obsah nie je dostupný, nesmie sa rekonštruovať z pamäti pod označením „exact“.

Ak je súborové odovzdanie podmienkou task PASS a ešte nie je overené, výsledok zostáva PARTIAL. Následné potvrdenie uloženia je nový dôkaz; nie dôvod opakovane vytvárať technický plán.

### F. Meta mapovanie, notes, handouty a closure

Meta README zostane vlastníkom lokálneho názvoslovia. AP vlastní význam súradníc a životného cyklu.

Zachovať:

```text
meta_exchange_index = Worker exchange ordinal - 1

relácia 01, prvá výmena:
01_planning_00.md + 01_report_00.md

rovnaká relácia, druhá výmena:
01_implementation_01.md + 01_report_01.md

nová relácia 02, prvá výmena:
02_acceptance_00.md + 02_report_00.md
```

Fáza nemení reláciu ani nevynuluje výmenu. Podporovať `planning`, `implementation`, `correction`, `acceptance`, `audit`, `diagnostic`, `publication` a odôvodnené opravné/pokračovacie fázy vrátane `re-*`. Prefix `re-` neobnovuje oprávnenie ani rozpočet automatických opráv.

Pre nové aktivované AP/Meta celky:

- `00_notes.md` vznikne pri otvorení celku.
- Úvodný `00_handout.md` je voliteľný.
- Neskoršie `xx_handout.md` a `xx_closure.md` používajú samostatnú Orchestratorovu postupnosť.
- Ďalší Orchestrator artifact ordinal je o jeden vyšší než najvyšší použitý ordinal handoutu alebo closure v danom celku; Worker prefixy sa do tejto postupnosti nepočítajú.
- Handout ani closure nespotrebuje Worker session ordinal.
- Existujúce historické názvy a medzery sa nemenia.
- Profil nástupcu je explicitný v obsahu; nededukuje sa len z názvu súboru.

Notes obsahujú dátované rozhodnutia, vybranú trasu, reconciliation, materiálne povolenia, zistenia a presnú ďalšiu výmenu. Neobsahujú rutinný transcript. Pri closure sa uzavrú.

Orchestrator zostáva autorom notes a handoutov. Poverený persister môže uložiť jeho presný obsah, ale nesmie ho svojvoľne vytvárať alebo meniť.

Každý ďalší handout uvedie:

- predchodcov;
- zachované prijaté rozhodnutia a obmedzenia;
- explicitne nahradené tvrdenia a dôvod;
- overený commit a hranicu lokálneho/verejného pozorovania;
- aktívne Worker relácie a rozpracované mutácie;
- presný ďalší krok;
- skutočný rozsah readiness review.

Novší handout automaticky neruší staršie rozhodnutie. Rozpor sa rieši autoritou a dôkazmi, nie časom súboru.

Implementation-first continuation znamená obnovenie už naplánovaného celku. Rotácia Orchestratora ani nová Worker relácia samy osebe nezačínajú nový logický celok.

### G. Kompaktný Worker základ

Zúžiť WORKER riadok existujúceho spine na:

- sémantickú autoritu a vlastný riadok spine;
- krátke kapsuly RF-03, RF-06, RF-12 a RF-18;
- §8 Worker Responsibilities a §18 Stopping Conditions;
- v `AP_WORKER.md` iba Worker Session Target a Reporting;
- Worker Report Header v `PROMPT_CONTRACTS.md`;
- aplikovateľné projektové a adresárové pravidlá.

Ostatné kapitoly aktivovať podľa konkrétnej úlohy: plánovanie, trace persistence, Git mutácia, provider, browser, privilégium, INFOSEC alebo nezávislé prijatie.

> “Document entrypoints identify where applicable rules are found; they do not require cover-to-cover reading. A Worker reads the common foundation and verified task-relevant anchors for the current grant.”

Toto vysvetlenie sa vzťahuje aj na existujúce dokumentové odkazy v generovanom managed blocku. **Executable `ap` a managed-block template sa nemenia.**

Materiálna citácia obsahuje vlastníka a nadpis; pri závislosti od verzie aj pin alebo baseline. Číslo riadka je pomocná navigácia.

Worker môže nájsť posunutý odkaz podľa nadpisu na správnom pine. Pri významovom konflikte alebo chýbajúcom potrebnom pravidle sa zastaví a pomenuje problém. Bežný posun riadka nevynucuje nový prompt.

P19 sa rozšíri aj na čerstvé relácie s úplným grantom a dostupnými overenými citáciami. Archív sa nebude čítať ako všeobecná onboarding povinnosť.

Kompaktnosť nesmie vynechať materiálny scope, zákaz, potrebný dôkaz ani explicitnú výnimku udelenú Cooperatorom.

### H. Testy, validácia a dáta

Spresniť existujúce pravidlo:

> “Add a test only for a named important behavior or uncovered regression when existing evidence is insufficient. State the gap the test closes. Select validation by the claim being decided, including read-only acceptance.”

Existujúci `New causal regression` riadok uvedie:

- `none` s primeraným stručným dôvodom, alebo
- dôležité správanie/regresiu, chýbajúci dôkaz a dôvod, prečo test túto medzeru pokrýva.

Uprednostniť vhodný existujúci test alebo jeho rozšírenie. Nový test nemá iba kopírovať aktuálnu implementáciu.

Dokumentačná zmena môže mať nula nových automatizovaných testov a napriek tomu potrebovať sémantické, odkazové a scenárové overenie.

Projektové brány sa vyhodnotia pred vydaním promptu. Záväzná aplikovateľná brána sa nesmie ticho vynechať. Nejasný materiálny rozsah sa vyjasní; neodvodí sa výnimka len z nulovej mutácie.

Široká kontrola sa neopakuje bez relevantnej zmeny kandidáta, prostredia alebo nového dôvodu. Samostatný testovací Worker sa vyberie iba pri konkrétnom prínose.

Pri dátach Planner najprv overí existujúce rozhodnutie o zachovaní alebo zmazaní. Ak je už konkrétne oprávnenie známe, znovu sa nepýta. Ak hodnota dát materiálne mení návrh a nie je známa, vyjasní ju pred návrhom zložitej kompatibility alebo purge. Chýbajúca historická informácia sa nesmie vydávať za rekonštruovaný fakt.

### I. WebSearcher, DeepResearcher a ImageCreator

Použiť existujúci capability handshake a surface routing.

| Profil | Spúšťač | Vstup | Výstup |
|---|---|---|---|
| WebSearcher | Ohraničená otázka vyžadujúca externé alebo aktuálne zdroje | Otázka, rozhodnutie, časový rozsah a zdrojové obmedzenia | Stručná citovaná odpoveď, dátumy, rozpory, neistoty a oddelené odporúčanie |
| DeepResearcher | Potrebná širšia syntéza výslovne zvolená Cooperatorom | Research brief, hranice, otázky a požadovaný artefakt | Citovaný súhrnný artefakt, porovnanie alternatív a medzery v dôkazoch |
| ImageCreator | Nový alebo upravený obrazový asset | Účel, rozmery, formát, zadanie, dostupné referencie a cieľ odovzdania | Skutočný asset a kontrola jeho požadovaných vlastností |

Pravidlá:

- Deep Research manuálne zapne Cooperator. Bežné browsing nástroje ho nenahrádzajú.
- Native Plan Mode a Deep Research sú rozdielne požiadavky; jedna nepreukazuje druhú.
- Nedostupná schopnosť sa uvedie ako obmedzenie. Odlišný výstup sa nevydáva za splnený pôvodný kontrakt.
- Externému povrchu sa odovzdajú iba potrebné a povolené vstupy.
- Externý povrch bez filesystem prístupu vráti text, odkaz alebo asset; uloženie vykoná pomenovaný schopný persister.
- Generátor obrázka alebo výskumná služba je nástroj. Zodpovedný AP Worker dodá terminálny report, ak ide o Worker výmenu.
- Samotný obrázok alebo download nie je Worker report.
- Výskumný záver je vstup do rozhodnutia, nie implementačné oprávnenie.

Nie je potrebné zavádzať osobitný špecialistický register, nový provider adapter ani nový reportový header.

### J. Kritika, brainstorming a Continue

Do existujúceho reportového jadra doplniť:

```text
Orchestration critique:
MEASURED: none | <overené zistenie; dôkaz; dôsledok; najmenšia oprava>
LEAD: none | <neoverená možnosť; najmenšie užitočné overenie>
```

Kritika sa týka promptu, predpokladov, rozsahu, poradia práce a zbytočných nákladov. Nemá nútiť Workera vymýšľať nálezy.

> “Every terminal report separates measured orchestration findings from unverified leads. Findings may justify correction or further evidence; they do not expand mutation authority.”

Orchestrator kritiku vyhodnotí spolu s výsledkom. Materiálnu dispozíciu zapíše do existujúcich notes; nová povinná výmena iba na kritiku nevznikne.

Pre konverzáciu:

> “A response may select a clearly bounded option in the established context. Continue resumes a clearly established next step within existing authority; it does not renew an expired Worker grant or create unexpressed scope.”

Brainstorming môže prebiehať medzi výsledkami. Nezávislá autorizovaná práca môže pokračovať, pokiaľ ju nová otázka nemení. Závislá činnosť počká na materiálne rozhodnutie. Už udelené konkrétne povolenie sa nepýta znovu.

## 4. Vlastníci, rozhrania a detekcia

`AP.md` ostáva jediným sémantickým vlastníkom. `PROMPT_CONTRACTS.md` vlastní presné štrukturálne spellings. Projekcie použijú odkaz a najviac jednu orientačnú vetu namiesto ďalšieho nezávislého prepisu pravidla.

Každé nové alebo materiálne zmenené pravidlo dostane **jednu** detekčnú triedu podľa aktuálneho AP. Nasledujúca tabuľka oddeľuje štruktúru od skutočného správania tam, kde ide o dve rozdielne povinnosti.

| Pravidlo | Vlastník v AP.md | Aplikovateľné projekcie | Trieda a pozorovateľný povrch |
|---|---|---|---|
| Názvy profilov a hranica pozorovaného checkoutu | §2, §3, RF-06, §4 | Orchestrator handbook, kontrakty, glossary, intuition | **Artifact-detectable:** metadata, cesty a evidencia pozorovaného stavu |
| Celý prompt a konkrétna Worker relácia | RF-05, RF-19, §3 | Session routing, oba handbooks, P14 | **Artifact-detectable:** vydaný prompt, identita relácie a deklarovaná kontinuita |
| Skutočný prvý manuálny Planner a aktívny natívny režim | §3, Plan-to-Execution Gate | Projekcie iba odkazujú; kontrakt nesie požadované hodnoty | **Behavioral-normative:** pozorovateľné spustenie na hranici klienta |
| Zachovaná delivery voľba | RF-02, provider-neutral routing | Delivery/routing kontrakty, Orchestrator handbook | **Artifact-detectable:** vybraná trasa, nasledujúce prompty a handout |
| Bounded planning a rozpočet tej istej otázky | Planning Budget and Expiry | Planning Record, handbooks, FAQ | **Artifact-detectable:** scope, predchádzajúci plán, zmenená hranica a revízne metadáta |
| Povinná odovzdávacia kapsula | Communication Routing | Delivery kontrakt, INTEGRATION, UPDATING | **Artifact-detectable:** vydaná kapsula a súlad s promptom |
| Autorstvo, persistence a Git hranice | RF-02, RF-14, RF-19 | Kontrakty, handbooks, artifact lifecycle | **Artifact-detectable:** grant, uložené artefakty, readback, reconciliation a Git výsledok |
| Úplnosť a identita reportu | RF-19, §17 | Report Header, exchange projection | **Artifact-detectable:** skutočný obsah reportu a matching prompt |
| Report completion bez replánovania | Planning Budget and Expiry, RF-19 | Existujúci completion kontrakt | **Artifact-detectable:** pôvodný obsah, nový scope, diff plánu a uložený výsledok |
| Meta mapovanie a kontinuita | RF-19, §14, Continuation Bootstrap | Meta README, Orchestrator handbook, artifact lifecycle | **Artifact-detectable:** názvy, súradnice, notes a odkazy medzi handoutmi |
| Výber Worker čítania | Per-Role Minimum-Reading Spine, §7, §17 | Worker handbook, Common Fields, P19, README | **Artifact-detectable:** povinný základ a relevantné citácie v prompte |
| Skutočné vykonanie požadovaného čítania | §8 | Projekcie iba odkazujú | **Behavioral-normative:** pozorovateľný postup pri práci; bez predstieranej mechanickej atestácie |
| Kauzálne testy a aplikovateľnosť brán | RF-07, §12 | Validation Ladder, handbooks, FAQ | **Artifact-detectable:** claim, medzera, vybraná kontrola a výsledok |
| Špecialistický vstup a výstup | §3, §4, provider-neutral routing | Existujúce capability/routing kontrakty | **Artifact-detectable:** brief, schopnosti, výstup a delivery cesta |
| Manuálne zapnutie Deep Research | Provider-neutral routing | Projekcie iba odkazujú | **Behavioral-normative:** skutočný režim klienta |
| MEASURED / LEAD | §8, §17 | Report Header a Worker reporting | **Artifact-detectable:** dve oddelené položky reportu |
| Kontextové Continue a bounded option selection | RF-01, Communication Routing | Projekcie iba odkazujú | **Behavioral-normative:** kontext rozhodnutia a následná činnosť |
| Konkrétna dátová autorita | §5, plánovacia hranica | Cielený plánovací prompt | **Artifact-detectable:** rozhodnutie o dátach, pomenovaný cieľ a rozsah oprávnenia |

**Zmeny verejných štruktúr sú obmedzené na:**

- nové hodnoty existujúceho `Capability profile`;
- profil `Planner` a špecialistické profily/schopnosti;
- `Recommended context capacity`;
- doplnenia existujúceho delivery recordu;
- `Orchestration critique` s MEASURED a LEAD;
- pravdivé počiatočné hodnoty existujúceho Planning Record pri novej bounded follow-up otázke;
- rozšírenie existujúceho completion kontraktu o presne autorizovanú persistence.

Nemenia sa tri súradnice, štandardný reportový header, terminálne statusy ani univerzálna Git/Markdown exchange gramatika. Nezavádza sa nový `planning-PASS` status; pre tento typ plánovacieho reportu zostáva phase-qualified result `not-applicable`.

## 5. Implementácia a prijatie

### Presný budúci allowlist

AP:

```text
AP.md
PROMPT_CONTRACTS.md
AP_ORCHESTRATOR.md
AP_WORKER.md
ARTIFACT_LIFECYCLE.md
PROMPT_ENGINEERING_PATTERNS.md
INTEGRATION.md
UPDATING.md
GLOSSARY.md
FAQ.md
INTUITION.md
README.md
CHANGELOG.md
docs/adr/README.md
docs/adr/0023-practical-workflow-consolidation.md
```

Meta, iba pod budúcim explicitným implementačným grantom:

```text
/home/agile/meta/README.md
```

Bez zmien zostanú executable `ap`, `ap.project.conf`, managed block, schema, CI, vyradená testovacia sada, spotrebiteľské piny, aplikačné repozitáre a ich dáta. Historické Meta analýzy a reporty nie sú implementačným povrchom tejto protokolovej zmeny.

### Sekvencia

**1. Jeden koherentný implementačný task.**

Odporúčanie: High reasoning, približne 250k kontext, `Native planning mode: not-used`. High odôvodňuje súbeh authority, routing, persistence a compatibility zmien.

Poradie práce:

1. upraviť sémantických vlastníkov;
2. upraviť existujúce štrukturálne kontrakty;
3. zosúladiť handbooks, P14/P19, príklady a vstupné dokumenty;
4. doplniť lokálnu Meta konvenciu;
5. pridať ADR a indexové vzťahy;
6. skontrolovať kandidáta ako celok.

Nevydávať na prijatie polovičný kandidát s novým vlastníkom a starými protichodnými projekciami.

ADR zachytí prijaté rozhodnutie, dôvody, odmietnuté alternatívy a čiastočné nahradenie starších rozhodnutí. Historické telá starších ADR sa neprepisujú. Status prijatého architektonického rozhodnutia sa výslovne odlíši od acceptance-PASS implementačného kandidáta, publikovania a closure; samotné historické označenie nesmie vytvoriť ďalšiu povinnú ceremoniálnu výmenu.

**2. Jedno čerstvé nezávislé prijatie presného kandidáta.**

Auditor dostane AP commit, presný Meta README kandidát alebo jeho obsahový hash, allowlist, vlastnícku mapu, požadované výstupy prijatého plánu a kontrolné scenáre. Implementačný report zostáva tvrdením na overenie.

Odporúčanie: High, približne 250k, read-only acceptance. Bez rodičovského transcriptu alebo implementačného reasoning.

Jedna primárna kontrola. Jedna konkrétna oprava a re-acceptance iba pri pomenovanom nedostatku. Pri zmene sémantiky, autority, routing, presného štrukturálneho poľa alebo nezávislosti sa použije existujúca hranica pre plné fresh acceptance; drobná prípustná oprava môže mať scoped re-acceptance.

**3. Publikovanie a closure podľa existujúcich oprávnení.**

Po prijatí overiť presný publikovaný AP commit. Meta commit/push zostáva Cooperatorovi. Publikovanie AP automaticky nemení spotrebiteľské piny ani neuzatvára celok.

### Prijímacie scenáre

| Scenár | Očakávaný výsledok |
|---|---|
| Nový celok, následná trasa subagent | Prvý Planner je napriek tomu manuálny a natívny. |
| Prvý Planner bez dostupného natívneho režimu | Nespustí sa cez tichý `not-used` fallback. |
| Dodatočná nová Planner otázka | Počiatočný cyklus môže pravdivo odkázať na predchádzajúci plán a zachované rozhodnutia. |
| Opakovaná stará otázka pod novým názvom | Revizný rozpočet sa nevynuluje. |
| Plánovanie potrebuje ďalší výskum | Chýbajúci dôkaz sa pomenuje; implementácia nezačne; neskorší dôkaz použije bounded pokračovanie. |
| Native Plan Mode blokuje zápis | Hotový obsah zostane zachovaný; persister alebo completion výmena ho uloží bez replánovania. |
| Zdravá rovnaká relácia | Zachová sa session ordinal, zvýši sa exchange a Meta suffix zodpovedá vzorcu. |
| Nový samostatný dispatch | Dostane celý prompt a skutočne novú reláciu; samotné vyvolanie nástroja sa nezamieňa so spoločnou rodičovskou reláciou. |
| Nezávislý audit | Implementer, zdieľaná relácia alebo zdedený rodičovský transcript nezískajú nezávislosť premenovaním profilu. |
| Priamy Worker zápis | Mení iba pomenované artefakty; nevykoná Git publication ani closure. |
| Identický pripravený prompt | Overí sa a použije bez zbytočného blokovania alebo prepisu. |
| Konfliktný cieľ alebo symlink mimo rozsahu | Bežné uloženie sa zastaví; nesúvisiaci dirty stav sa zachová. |
| Cudzí handout na reportovej ceste | Neprijme sa ako report ani vtedy, keď sa líši od promptu. |
| Neúplný natívny plán alebo interruption companion | Neoznačí sa za štandardný terminálny report. |
| ChatOrchestrator dostane „report je commitnutý“ | Načíta očakávanú cestu z overeného verejného commitu; netvrdí znalosť nepozorovaného lokálneho stavu. |
| Bežný čerstvý Worker | Začne zo spoločného základu a overených relevantných odkazov bez povinného celého archívu. |
| Posunutá citácia | Nájde sa správny nadpis na správnom pine; významový konflikt sa nevyrieši domnienkou. |
| Dokumentačná zmena | Môže mať nula nových automatizovaných testov a cielené sémantické overenie. |
| Read-only acceptance správania | Spustí potrebné testy napriek nulovej mutácii. |
| Nový test | Pomenuje dôležité správanie a nedostatok existujúceho dôkazu; nekopíruje iba implementáciu. |
| Špecialisti | Použijú skutočné schopnosti a pravdivú delivery cestu; browsing nie je Deep Research a asset nie je report. |
| Viac handoutov | Zachovajú trasu, prijaté rozhodnutia, aktívnych Workerov a explicitné zmeny voči predchodcom. |
| Continue a výber A | Jasná odpoveď sa správne použije; neobnoví sa ňou expirovaný Worker grant. |
| MEASURED / LEAD | Pozorovanie a hypotéza zostanú oddelené; nález neaktivuje ďalšiu mutáciu. |
| Vývojové dáta | Konkrétny už udelený súhlas sa rešpektuje; samotné development označenie purge nepovolí. |
| Nový prompt/report pár | Prvý Git add nastane spoločne až po dokončení reportu. |
| Staré piny a názvy | Historické artefakty zostanú interpretovateľné podľa pôvodnej revízie. |

Implementer vykoná jeden cielený prechod cez diff, vlastníctvo významu, staré protichodné formulácie, odkazy a vykreslené príklady. `git diff --check` doplní obsahové posúdenie. Kontroly sa opakujú po relevantnej zmene alebo zlyhaní, nie ako rituál.

**Kritérium prijatia:** všetkých trinásť požiadaviek má jednoznačné pravidlo, vlastnenú štruktúru a správne projekcie; scenáre nemajú materiálny rozpor; nevznikla skrytá autorita ani druhý sémantický vlastník.

To preukáže kvalitu dokumentačného kandidáta. Nepreukáže ešte reálne tokenové úspory alebo úspech v budúcom projekte.

### Kompatibilita a rollback

- Nové pravidlá sa uplatnia prospektívne pri vydaní promptu pod novou revíziou.
- Už naplánovaný rozpracovaný celok sa nebude nútiť do ďalšieho úvodného Plannera.
- Chýbajúci plán sa nesmie predstierať ako historicky splnený.
- Staré názvy profilov, súborov a pôvodné piny sa neprepisujú.
- Rollback vráti koherentnú AP dokumentačnú zmenu vrátane projekcií.
- Meta README sa vráti samostatným bežným commitom Cooperatora; historické reporty sa nemažú.
- Spotrebiteľská adopcia alebo rollback pinu je samostatne autorizovaný krok.

## 6. Presné odovzdanie, uzamknuté rozhodnutia a kritika

### Požadované uloženie tohto reportu

Požadovaný cieľ:

```text
/home/agile/meta/projects/ap/08/00-ap-practical-workflow-consolidation/01_report_00.md
```

Pri poslednej kontrole:

- fyzická cesta zodpovedá zadanej ceste;
- žiadna jej komponenta nebola symlink;
- súbor má 10 619 bajtov;
- jeho SHA-256 je:

```text
e56e3d1c819404426218fc08b21f9230045173bb919a01b8ef7d9982a0b1b75d
```

- obsahuje handout ContextDecku;
- nesprávny obsah je zachovaný vo verejnom Meta commite:

```text
9c6733d4a116bf8cfa3ae28ffe34a9a6292b6e41
```

Vaše posledné explicitné povolenie chápem ako súhlas s opravou **tohto konkrétneho známeho cieľa**. Nejde o všeobecné oprávnenie prepisovať históriu alebo iné reporty.

Presný technický postup po umožnení zápisu:

1. Znovu overiť fyzickú cestu, neprítomnosť presmerovania a aktuálny obsah.
2. Ak cieľ už presne obsahuje tento finálny report, iba overiť úspešné odovzdanie.
3. Ak stále obsahuje uvedený známy chybný obsah, nahradiť ho týmto kompletným Markdown reportom. Starý obsah zostane dostupný v uvedenom Git commite.
4. Ak sa objavil iný obsah, neprepísať ho bez vyhodnotenia novej zmeny.
5. Pri uložení vynechať iba prezentačný obal, ktorým klient zobrazuje plán. Vlastný súbor musí začínať štandardným reportovým headerom a obsahovať celý tento report.
6. Overiť uložené bajty, header, jediné metadáta výmeny a celý plán.
7. Nemeniť `01_planning_00.md`, notes, handouty ani iné Meta súbory.
8. Nevykonať stage, commit alebo push.

Existujúci plánovací prompt má 12 730 bajtov a SHA-256:

```text
370e0ec9698f489304173ad7879f40b4a66fdbb8c15bc29f05d7d5582e912bb4
```

Presne zodpovedá pôvodnej prílohe.

Prompt a nesprávny report boli historicky pridané v rozdielnych commitoch. Oprava obsahu nemôže spätne vytvoriť spoločný first-add commit. Tento nesúlad sa zachová ako známa história; nebude sa zakrývať prepisovaním Git histórie.

Neskoršie uloženie tiež nemení pravdivosť tohto reportového statusu v čase jeho autorstva. Potvrdenie persistence bude samostatným novým dôkazom.

### Uzamknuté rozhodnutia

Implementer nemusí vyberať nový dizajn. Platí:

- jeden sémantický vlastník a tri trvalé roly;
- prvý Planner manuálne v skutočnom natívnom režime;
- zachovaná následná delivery voľba;
- autorizovaná persistence oddelená od ostatných práv;
- Cooperatorov Meta commit/push pri ChatOrchestratorovi;
- kompaktný Worker základ;
- kauzálne nové testy a claim-driven validácia;
- existujúce capability/routing kontrakty pre špecialistov;
- povinné MEASURED/LEAD;
- jeden koherentný kandidát a jedno primerané čerstvé nezávislé prijatie.

**Žiadna nevyriešená produktová alebo architektonická voľba nebráni implementovateľnosti plánu.** Budúci grant musí určiť aktuálny baseline, skutočne dostupný klient a konkrétne oprávnenia; tieto hodnoty sa nemajú vymýšľať vopred.

Jedna neskoršia praktická skúška na aktuálnom ohraničenom projekte je odporúčaná na meranie administratívnych nákladov a chýb. Nie je predstieraným výsledkom tejto práce ani dôvodom znovu otvárať historické Libre Tiles úlohy.

### Orchestration critique

**MEASURED**

- D-13 nesprávne tvrdí absenciu restoration readiness review; D-17 používa neexistujúcu citáciu. Finálny návrh opravuje skutočných vlastníkov.
- Archívy 02–04 opakovane ukazujú rozdiel medzi hotovým výsledkom a úplným terminálnym reportom. Persistence nesmie vytvárať ďalšie technické plánovanie.
- Cieľový report tejto úlohy obsahuje cudzí handout. Je to konkrétny negatívny prípad pre kontrolu identity a obsahu reportu.
- Moja skoršia reakcia na identický pripravený prompt bola príliš prísna. Identická rozpracovaná kópia sa musí odlíšiť od skutočnej obsahovej kolízie.
- Predchádzajúci návrh nešpecifikoval dostatočne počiatočné polia dodatočného Plannera. Finálna verzia umožňuje pravdivé odkazy na existujúci plán bez vymýšľania nového typu záznamu.
- Finálna verzia tiež odstraňuje zbytočnú požiadavku na novú plánovaciu výmenu tam, kde už existuje celý report a schopný autorizovaný persister.

**LEAD**

- Menší základ čítania, zachovaná delivery voľba a priame reporty by mali znížiť administratívne výmeny. Rozsah úspory nebol zmeraný.
- Povinný prvý Planner môže byť citeľný pri veľmi malých nových celkoch. Ide o výslovne vybraný kompromis; plán má byť úmerne krátky.
- Praktický pilot môže odhaliť rozdiely medzi deklarovanými a skutočnými vlastnosťami agentových relácií alebo externých špecialistov. Overovať ich konkrétnym odovzdaním a dôkazom, nie názvom nástroja.

**Finálny stav:** plán je dokončený; zápis `01_report_00.md` v aktívnom Plan Mode vykonaný nebol. Preto zostáva tento report **PARTIAL**, bez tvrdenia o úspešnom uložení, implementácii alebo closure.
