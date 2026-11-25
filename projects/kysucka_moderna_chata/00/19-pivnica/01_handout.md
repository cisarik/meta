# V20 · Pivnica s dvoma vstupmi a večerným osvetlením

Handout status: provisional  
Capability profile: Orchestrator  
Orchestrator session scope: logical-whole  
Development run identity: kysucka-moderna-chata-reference-visualization  
Logical whole identity: kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20  
Author: read-only Master Chat Orchestrator  
Prepared: 2026-11-24, Europe/Bratislava  
Destination: `projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20/00_handout.md`  
Lifecycle: advisory provisional handout; freeze on opening; Fresh Orchestrator consumes it. Meta archival, retention and cleanup belong to Michal.

## Obnova a zámer

Prevezmi V20 z tohto lokátora, obnov projektový kontext z aktuálneho `AGENTS.md`, AP pinu a lokálnych súborov. Zaznamenaj Handout Revalidation Record v `00_notes.md`. Zosúlaď súradnice a skutočnú identitu oboch vstupných scén. Priprav jeden anglický prompt pre fresh Plannera v natívnom Plan Mode a samostatný realizačný grant po prijatí riešenia. Výmeny V20 začínajú `01/01`. Workeri reportujú v angličtine od riadku `### Report for ORCHESTRATOR_CHAT`. Pri klientovi, ktorý v Plan Mode nevie zapisovať, vopred urči Orchestrátorku ako vlastníčku uloženia reportu. Michalovi odpovedaj po slovensky v ženskom rode. Odporúčam High pre priestorové rozhodnutie, model volí Michal.

Michal schválil V20 a pridal **samostatný vonkajší vstup do existujúcej pivnice B1, s futuristickým osvetlením**. Výsledkom je jedna pivnica s dvoma plnohodnotnými prístupmi, upraveným stropom a dverami a s jednotlivými prvkami zladenými v interiérovej a exteriérovej scéne. Rozsah V20 končí pri pivnici, jej prístupoch a priľahlom kúsku fasády a terénu. Kúpeľňa, izby a ostatné miestnosti patria do ďalších celkov. Samostatný západ slnka cez údolie ostáva položkou `R-V18-01`. Modrá hodina v tomto celku slúži na kontrolu osvetlenia nového vstupu.

## Východisko

| Artefakt | Overená alebo hlásená identita |
|---|---|
| Verejný Meta V19 | `ce9d740e8cbf9be96d301a2fe8388c08881eda9c`. Uzávierka je PASS pre vnútorný variant A. Master skontrolovala tri uložené PNG a ich hashe. [Uzávierka V19](https://github.com/cisarik/meta/blob/ce9d740e8cbf9be96d301a2fe8388c08881eda9c/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/01_closure.md) |
| Schválený interiérový kandidát V19 | `work/v19/kysucka_chata_interier_pivnica_v19.blend` · SHA-256 `d9021ee49f63a6dc595214932485597b3b47186b6e26487065c87964dc5dcdf8` · východisko pre nový interiérový kandidát |
| Hlavný interiér pred povýšením | `blender/kysucka_chata_interier.blend` · SHA-256 `c607cb21fbdb289b49f05596004b403e7dd5f96a64e900ce42ed8485f6a30449` · referenčný predchodca a cieľ lokálneho povýšenia po akceptácii |
| Denný exteriér na modelovanie západného okolia | `work/v18/recovery/kysucka_chata_exterier_doladeny.blend` · SHA-256 `5e8ada70e99c70a3be0a7eea9b18306b422e4ef3a141a63b51b237b7957e3a24` · aktuálny lokálny exteriérový predobraz |
| Protokol obálky | `model/shared_envelope_v18.json` · 289 pôvodných objektov · agregát `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50`. Pri V20 sa posudzuje aj aktívna renderová geometria a všetky viditeľné náhrady. |

Lokálne hashe sú z uzávierok a revaliduje ich Orchestrátorka. Verejný produktový repozitár je na `8218cb3a27a247cc73de940462d21f3bebc27f8a`. Lokálny checkout pri uzávierke V19 bol `f600c7a8e69a23a029559872652302ac299c2aea`, AP pin `d7023cf037f6d17885c3ede5c04812c61640da50`. `work/` je ignorovaný. Pri obnove má prioritu skutočný súbor s overeným hashom a jeho lokálnymi dôkazmi. Z V19 použi aj `walk_clearance_v19.json`, výkres B1, rez A–A a register náhrad obálky. Ak dôkazy nie sú v novom checkoute, odčítaj merania z overenej scény. [Realizačný report V19](https://github.com/cisarik/meta/blob/ce9d740e8cbf9be96d301a2fe8388c08881eda9c/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/01_report_02.md)

## Nový vonkajší vstup

**Vonkajší zostup navrhni k prijatému B1.** Starý alternatívny variant B mal iný pôdorys a otvor vo fasádnej línii na `Y 5.940–6.980 m`. Schválený hrubý objem V19 končí už pri `Y 5.700 m`, takže pôvodný otvor ústi mimo neho. Použi starý variant na porovnanie dĺžky, záberov a veľkosti zásahu do dosky. Jeho výrez `6.552 m²` a obchádzka `34.17 m` od D01 sú meraným porovnávacím základom. [Pôvodné porovnanie V19](https://github.com/cisarik/meta/blob/ce9d740e8cbf9be96d301a2fe8388c08881eda9c/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/01_report_01.md)

1. **Prvá hypotéza pre zameranie.** Zostup pri severnej časti západného prístrešku, prevažne mimo dosky `X < 0`, s krátkou podestou a obratom smerom k zapusteným dverám do B1. Presný smer ramena a polohu prahu určí rez. Hrubý B1 má `X 2.700–7.400 m` a `Y 2.280–5.700 m`. Čistý sklad má `X 2.900–7.200 m`, `Y 3.600–5.500 m` a podlahu `−2.250 m`. Zameraný terén pri západe je okolo `−0.055 m`, takže zostup prekonáva zhruba `2.195 m`. Zmeraj vyhodnotený terén v celej navrhovanej trase. Skús dosiahnuť západnú stenu skladu severne od existujúcej dolnej podesty. V preverovaní zahrň oba dverné oblúky a miesto, kde možno lokálne upraviť prvý regálový modul.
2. **Druhá hypotéza.** Ak riešenie mimo dosky vyžaduje príliš dlhý podzemný prechod alebo súperí s priechodom v B1, prever posunuté alebo otočené rameno čiastočne pri prístrešku. Porovnaj dĺžku pešej odbočky z existujúceho prístupu, zásah do západnej hrany dosky, objem výkopu, zachovanie prístrešku na drevo a odstup od jablone. Pre obe možnosti zakresli pôdorys a rez. Odporuč jedno riešenie podľa meraní a pohľadov zo západu a severu.
3. **Trasa a napojenie.** Odbočka musí začínať na skutočne dosiahnuteľnej časti existujúceho prístupu alebo dvora a viesť po zemnom povrchu až na hornú podestu. Zostup má mať terénne návraty, súvislé madlo, ochranu pri otvorenom okraji, protišmykový povrch, dolnú podestu a presvedčivú škáru pri prahu. V reze ukáž výšky, styk terénu s novými stenami a priestor na vizuálne čitateľné zachytenie vody pred dverami. Posúdenie konštrukcie, odvodnenia a hydroizolácie patrí do samostatného stavebného návrhu. Orchestrátorka schváli konkrétny vizualizačný zásah do dosky, sokla a terénu podľa rezu.

## Vzhľad a dokončenie pivnice

- **Vstup cez deň aj po zotmení.** Zapustený kamenný zostup so svetlosivým betónom, bridlicovými stupňami a tenkým grafitovým kovom. Teplá súvislá línia pod madlom (návrh 2700–3000 K) smeruje na stupne a kresbu kameňa. Pri tmavých dverách nech jedna jemná zvislá línia v ostení ukáže prah. V kontrolnom pohľade od plota a z lúky sleduj priamu viditeľnosť zdrojov, vypálené plochy a rozliatie svetla. Použi matné materiály a tlmené opakované odrazy. Priložená večerná vizualizácia je referencia materiálov a svetla. Geometriu určuje meranie a lokálny Blender rez. [Zámer exteriérovej svetelnej orientácie](https://www.erco.com/en/knowledge/culture/welcoming/)
- **Strop B1.** Odstráň diagonálny šev na strope v rovnakom pohľade ako `zaber_b1_pivnica_v19.png` (plánovaná kamera `CAM_V19_B1_CELLAR`). Najprv over príčinu vo vláknach, UV, normálach alebo osvetlení a zvoľ najmenšiu opravu. Ak dosky alebo tenké priznané trámy pridajú vizuálnu hodnotu, porovnaj profil s nameranou čistou výškou `2.390 m` a pohybovým priestorom.
- **Presklené dvere medzi vnútornými schodmi a skladom.** Prever presun pántu na západné ostenie. Skontroluj celý oblúk krídla aj kľučky pri stene, regáli a prístupe zvonka. V19 namerala na svojom testovacom telese minimálnu bočnú rezervu len `15.42 mm`. Obnovenie plnej hĺbky prvého regálu schváľ až po novom teste oboch trás. Záber z výšky očí v chodbe má ukázať puzdrové dvere a smer zostupu. Lokálne pridaj mäkké svetlo pri prahu podľa porovnania rovnakého záberu.

## Dva kandidáty, jeden spoločný vstup

- Použi zmrazený interiér V19 a denný exteriér V18. Vlastnú V20 kolekciu vstupu normalizuj v spoločných svetových súradniciach. Oba súbory používajú totožné stupne, nástup, múriky, dvere, terénny výrez v ich okolí a svetlá v rozsahu potrebnom v každej scéne. Pôvodné referenčné objekty zachovaj a eviduj ich viditeľné náhrady. Pri zdieľaných častiach porovnaj objem, transformácie, prah oboch trás a stav dverí. V exteriéri zastúp len potrebnú časť B1 pre pohľad či svetlo cez otvorené dvere. Zachovaj samostatné offline otvorenie oboch produktov.
- Prevezmi V19 kontrolný profil postavy `Ø 0.700 × 2.100 m` s krokom najviac `0.045 m` pre porovnanie. Prejdi pôvodné trasy aj novú súvislú trasu **dvor → B1 → chodba** v oboch smeroch, so skúškou otočenia na podestách. Dvere otestuj v zatvorenej, otvorenej a priebežnej polohe pri bežných trasách. Zaznamenaj najtesnejšie miesto, hodnoty a príslušnú polohu. Over výsledok aj po otvorení súborov v čistej izolovanej Blender relácii.
- Odovzdaj jeden čitateľný pôdorys a jeden rez napojením na B1, **západný záber deň/modrá hodina z rovnakej kamery**, nočný detail zostupu, pohľad zvnútra chodby a B1. Zopakuj fixné západné a severné pohľady na obálku a štyri referenčné interiérové uhly V19. Denné a nočné nastavenia majú vlastné reprodukovateľné scény, vrstvy alebo profily. Na záver uveď aj hash oboch kandidátov a všetky povolené rozdiely voči V18/V19.
- Po akceptácii povýš presný kandidát do hlavného interiéru podľa samostatného lokálneho kroku s overenou obnovou predchodcu. Exteriérový kandidát odovzdaj na posúdenie s jasným rodičom `kysucka_chata_exterier_doladeny.blend`. Archívnu politiku projektových `.blend` a Git rozhodnutia prevezme Michal. Pracovné dôkazy ponechaj do potvrdenia obnovy a akceptácie oboch scén. Report uvedie kolízne testy, checkpointy, denné a večerné páry a presný stav integrácie.

```text
Run entry: 20 | kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20 | provisional | depends on: kysucka-moderna-chata-basement-layout-study-v19 | handout: projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20/00_handout.md | evidence: Cooperator approves V20 and adds a separately lit second access from outside to the accepted B1
```
