# V19 · Pivnica v samostatnom interiéri

Handout status: provisional  
Capability profile: Orchestrator  
Orchestrator session scope: logical-whole  
Development run identity: kysucka-moderna-chata-reference-visualization  
Logical whole identity: kysucka-moderna-chata-basement-layout-study-v19  
Author: read-only Master Chat Orchestrator  
Prepared: 2026-11-24, Europe/Bratislava  
Destination: `projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/00_handout.md`  
Lifecycle: provisional handout, frozen on opening. Orchestrator consumes it. Michal owns Meta archival and retention.

## Obnova pre Fresh Orchestratora

Prevezmi V19 z presného lokátora vyššie. Pri Continuation Bootstrap Stage 1 over aktuálny checkout, AP pin, hash samostatného interiéru, zameranie V18 a stav práce v živej scéne. Výsledok ulož ako Handout Revalidation Record v `00_notes.md`. Otvor jeden plánovací cyklus v natívnom Plan Mode. Anglický prompt pre Plannera aj realizačný grant doruč samostatne. Worker report začína `### Report for ORCHESTRATOR_CHAT`. Ak klient v Plan Mode nevie zapisovať, urč Orchestrátorku ako vlastníčku uloženia reportu. Michalovi odpovedaj po slovensky v ženskom rode. Model vyberá Michal. Pre prvé zameranie a rozhodnutie o variante je vhodný High.

## Odovzdanie V18

Master prečítala priložený report a overila verejný Meta commit `240b4472fca3613fac6b56b3482593c30a15a5a5`. Report je bajtovo zhodný s `01_closure.md` (SHA-256 `5450f531c30967bf6b8de715e0da4f9159ab8aa618ed78a34d6b403059c70d96`). Text obsahuje `Logical-whole closure: not-closed`. Formálnu dispozíciu zapisuje Orchestrátorka V18. Verejne dostupných je všetkých 12 finálnych PNG a `sprava.md`. Manifest a kontaktný prehľad odkazované v reporte v tomto commite chýbajú. Pri revalidácii využi ich lokálne kópie, ak sú dostupné. [Podklad k uzavretiu V18](https://github.com/cisarik/meta/blob/240b4472fca3613fac6b56b3482593c30a15a5a5/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/01_closure.md) · [Finálne denné zábery](https://github.com/cisarik/meta/tree/240b4472fca3613fac6b56b3482593c30a15a5a5/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/renders/2026-11-24_150201_727305_doladenie-exterieru)

- Denné zábery preukazujú lepší prechod z lúky do lesa, rôzne výšky drevín a čitateľne modelované kvety v popredí. V JV a SZ je odstránenie svetlých slamových plôch z jarnej úpravy výraznejšie než posledné doladenie. V `kopce-a-lesy` priťahujú pozornosť opakujúce sa svetlé listnaté koruny. Široké orbity ukazujú konečnú hranu modelovaného terénu. Užitočný je nízky záber `luka-od-chodnika`, kde sú viditeľné steblá, kvety aj rôzne vrstvy porastu. Posledný denný checkpoint odporúčam zachovať a exteriér ponechať na prestávke podľa Michalovho rozhodnutia.
- Chodník je v reporte geometricky preukázaný až po nový severný okraj, približne 404 m v pôdoryse od brány. Skoršiu obrazovú medzeru spôsobovala terénna vlna. Formálna vetva 01/06 doložila 255 mladých stromov z 5 100 pri pomeroch výšok 0,479–0,521. Po neskoršom skrytí 15 % lesa ostalo podľa reportu 4 335 aktívnych stromov. Zverejnené podklady nepotvrdzujú presný pomer mladých medzi týmito 4 335.
- Pri uzávierke V18 zosúlaď presný denný checkpoint a Michalovu prestávku. `R-V18-01` zostáva otvorený pre západ slnka z opačnej strany údolia. Zachovaj Michalov referenčný záber a jeho popis. Interaktívna plynulosť finálnej scény na RTX zostáva nezmeraná. Záverečné denné súbory sú lokálne. Priečinok `work/` preto treba pri obnove pokryť prenosom checkpointu. V19 potrebuje samostatný interiér a zameranie V18.

## Presné východisko pre V19

| Podklad | Identita podľa V18 |
|---|---|
| Samostatný interiér, výmena 01/06 | `blender/kysucka_chata_interier.blend` · SHA-256 `c607cb21fbdb289b49f05596004b403e7dd5f96a64e900ce42ed8485f6a30449` |
| Posledný denný exteriér, referencia pri fasáde | `work/v18/recovery/kysucka_chata_exterier_doladeny.blend` · SHA-256 `5e8ada70e99c70a3be0a7eea9b18306b422e4ef3a141a63b51b237b7957e3a24` |
| Spoločná obálka | `model/shared_envelope_v18.json` · digest geometrie a transformácií 289 častí `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50` |
| Zameranie | `56_BASEMENT_V18`, vložený text `V18 \| Podklad pre pivnicu` a lokálne `work/v18/stage1/{basement.json,basement_plan.svg,cross_sections.csv,cross_sections.svg}` |
| Checkout pri odovzdaní V18 | lokálne `f600c7a8e69a23a029559872652302ac299c2aea`, AP `d7023cf037f6d17885c3ede5c04812c61640da50`. Verejný projektový commit, ktorý mala Master k dispozícii, je starší. |

Najprv over kóty a spoločnú obálku na presnom lokálnom interiérovom súbore. Stage 1 nameral hotovú podlahu **+0,451 m**, dosku **+0,200 až +0,450 m**, okolitý terén pri fasádach **−0,055 m** a otvorenú medzeru pod doskou **0,255 m**. Na západe je prístrešok `X=0–2,40 m`, za ním uzavretá stena `X=2,40–2,70 m`. Chodba má čistú šírku **1,15 m**. Schody na galériu, skrinka pod nimi a krb majú v podklade vlastné kolízne objemy. [Merania v §3 plánovacieho reportu](https://github.com/cisarik/meta/blob/240b4472fca3613fac6b56b3482593c30a15a5a5/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/01_report_00.md) · [Readback rozdelenia](https://github.com/cisarik/meta/blob/240b4472fca3613fac6b56b3482593c30a15a5a5/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/01_report_01.md)

## Prvá úloha · kadiaľ sa do pivnice skutočne dostaneme

Pracovná hypotéza je malá skladová pivnica pod západnou časťou uzavretej chaty. Rozsah pivnice a účel zaznamenaj ako predpoklady, ktoré možno zmeniť po prezretí variantov.

| Variant | Čo preukázať |
|---|---|
| A · Vstup zvnútra zo zázemia | Nakresli nástup z chodby, schody v bočnom priestore zázemia, otvor v doske a dolný výstup. Otvorenie dverí a prejdenie trasy do dennej zóny vyskúšaj naraz. Označ, či variant uberá z technickej miestnosti, kúpeľne alebo izby a koľko. Priechodná chodba je podmienka. |
| B · Vstup od západného prístrešku | Odmeraj voľný priestor okolo dreva a nástup od existujúceho vstupu. Modeluj celé klesanie od rovného terénu a zakresli otvor, dvere, výstup aj zásah do dosky či viditeľného sokla. Na reze skontroluj, či sa schody dajú osadiť v pôdoryse prístrešku. Pri zásahu do spoločnej obálky ukáž západný a severný pohľad. |

V Plan Mode použi existujúce zameranie. Pre oba varianty priprav schematický pôdorys prízemia, pôdorys B1 a jeden rez cez schody, dosku a terén s čitateľnou mierkou. Uveď nástupnú a výstupnú kótu, čistý priestor na státie, rozmery a geometriu schodov, svetlú výšku na najhoršom mieste, otváranie dverí a kolízie s vybavením, stenami či krbom. Navrhni jeden variant na základe konkrétnych rozdielov. Vnútorný variant má prednosť, ak ponechá pohodlný priechod a funkciu zázemia. Použi úroveň vizualizačnej štúdie. Skutočná stavebná realizácia má vlastný konštrukčný návrh.

## Realizácia až po výbere dispozície

- Vytvor jednu funkčnú štúdiu v projektovej kópii interiéru. Pivničná kolekcia vlastní skúšobné schody, podlahu, obvodový objem, strop a otvor s dverami. Ak prístup vyžaduje otvor v geometrii spoločnej dosky, použi označenú študijnú kópiu a vráť presný diff. Predchodcu over podľa hashu.
- Odovzdaj aktualizovaný pôdorys a rez, jeden záber nástupu a jeden záber z B1. Dolož spojitý priechod z prízemia po posledný stupeň. Porovnaj pôvodnú obývačku, galériu a priehľad oknom vo fixných kamerách. Prípadná zmena viditeľného sokla sa vyhodnotí v spoločnej revízii obálky po prijatí riešenia. Denný exteriérový checkpoint slúži ako referenčný predobraz.
- Zachovaj pracovný `.blend` a podklady s hashmi a cestami. Dôkazy uloží Orchestrátorka podľa aktivovanej Meta stopy. Dočasné kópie možno upratať po prijatí vybraného variantu a potvrdení samostatného otvorenia. Vizuálne schválenie pivnice patrí Michalovi.

```text
Run entry: 19 | kysucka-moderna-chata-basement-layout-study-v19 | provisional | depends on: kysucka-moderna-chata-split-and-forest-realism-v18 | handout: projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/00_handout.md | evidence: separate V18 interior and measured basement context; Master recommends layout and access study
```
