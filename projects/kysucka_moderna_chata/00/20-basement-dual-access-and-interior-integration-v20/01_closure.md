# 01_closure — V20 · Pivnica s dvoma vstupmi

**CELOK UZAVRETÝ ORCHESTRÁTOROM**

**25. 11. 2026 · Orchestrátorka celku · `kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20`**

Celok **V20** je uzavretý. Michal schválil druhý, zvonka osvetlený vstup do prijatého B1, po plánovaní vybral smer Hypotézy 2 a po záberoch doplnil kamenný základ okolo celej chaty aj chodník od vchodu k schodisku. Štyri svetové strany a spojovací pohľad sú v Meta. Kanonický interiér ani Git sa v tomto celku nemenia.

Táto uzávierka neuzatvára celý vizuálny projekt. Západ slnka cez údolie ostáva `R-V18-01`. Kúpeľňa, izby a povýšenie do `blender/kysucka_chata_interier.blend` ostávajú ďalším celkom.

## 1. Čo je výsledok

Prijatá trasa je **Hypotéza 2**: priamy zostup na východ po osi `Y 5,015 m`, 13 výšok po `168,8 mm`, nášľap `280 mm`, sklon `31,1°`, čistá šírka `1,040 m`. Západná hrana dosky je prerezaná v páse `Y 4,305–5,725 m` do `X 1,040 m`. Vnútorné schodisko z V19 ostáva. Prvý regál ostáva plytší, `0,256 m`. Svetlo na strope B1 je zarovnané nadol a svetlá výška skladu ostáva `2,390 m`.

Okolo celej dosky je jeden rad `53` kameňov od terénu po spodok dosky `+0,200 m`. Chodník má `31` dosiek, dĺžku `27,28 m` a ide od južného nástupu okolo jablone k hornej podeste pivnice. Najtesnejšie miesto na chodníku je `0,170 m` pri existujúcom madle schodiska, nie pri novom kameni.

Aktuálne súbory na posúdenie:

| Súbor | SHA-256 |
|---|---|
| `work/v20/kysucka_chata_exterier_pivnica_v20_chodnik.blend` | `2121f6f46185c9914dce6944c792f6d032c8fdc7a17eb2728debfdc869881366` |
| `work/v20/kysucka_chata_interier_pivnica_v20_chodnik.blend` | `975e278c3bbd3a6b9e9ffe3d18194b2539c9f10fd25d79e386dfd44270cb62e0` |

Predchodcovia `blender/kysucka_chata_interier.blend` (`c607cb21…`), interiér V19 (`d9021ee4…`) a denný exteriér V18 (`5e8ada70…`) ostali nezmenené. Projektový `HEAD` je `f600c7a8e69a23a029559872652302ac299c2aea`.

## 2. Archív záberov

Priečinok `renders/2026-11-25_svetove-strany/` drží denné snímky `1440×810`, 96 vzoriek, CPU, OIDN, zo scény `2121f6f4…`.

| Súbor | Pohľad | SHA-256 |
|---|---|---|
| `zapad.png` | západ, schodisko a príchod chodníka | `6dbe739f1f4df74cefc8830b5e07978aced2009af7f2de4c9689aee4a02c6408` |
| `sever.png` | sever, kamenný základ | `2995a61ebd8fbcd92f3955c64d6d5ee357afd3b15a3e890b9ac29f0d21eaacd9` |
| `juh.png` | juh, vchod a odbočka | `b638d07cd8870d6984b47eda40275293baf6a43573deba580e7f5965d76f44f7` |
| `vychod.png` | východ, základ a odbočka | `0d919448a35ce9402ceb4ae26b75b19013065f95f3c65cc226b7fa61aec5c738` |
| `spojenie.png` | od vchodu po schodisko pivnice | `180e3ac82063d050e57be871869644a369c2f6e14ff89b948046b9a320ee1510` |

Východná kamera je len v tejto snímke. Do súboru `.blend` sa neukladala.

## 3. Čo ostáva mimo tohto celku

Ďalší zásah do scén tento celok už nerobí. Nasledujúce body sú register, nie nový grant.

1. **FT-V20-01.** Okraj chodníka ešte miestami prekrývajú trsy trávnika. Maska končí `0,36 m` od dosiek.
2. **FT-V20-02.** Posledný betónový stupeň chodníka je `15 mm` nad bridlicovým prahom schodiska.
3. **FT-V20-03.** Pod bielou hranou dosky ostáva tenký tieň skosenia. Kamene siahajú najviac `20 mm` na fasciu.
4. **FT-V20-04.** Povýšenie interiérového kandidáta do `blender/kysucka_chata_interier.blend` je samostatný krok po vizuálnom prijatí. V tomto celku sa nerobil.
5. **FT-V20-05.** Kúpeľňa, izby a západ slnka cez údolie (`R-V18-01`) patria iným celkom.
6. **FT-V20-06.** Git záznam v Meta aj v projektovom repozitári ostáva Michalovi. Pracovné `.blend` sú v ignorovanom `work/`.

## 4. Záznam uzavretia

```text
Declared closure signal: CELOK UZAVRETÝ ORCHESTRÁTOROM
Signal owner: orchestrator
Worker emission of closure signal: prohibited
Phase-qualified result: acceptance-PASS
Result artifact or commit: work/v20/kysucka_chata_exterier_pivnica_v20_chodnik.blend SHA-256 2121f6f46185c9914dce6944c792f6d032c8fdc7a17eb2728debfdc869881366 and work/v20/kysucka_chata_interier_pivnica_v20_chodnik.blend SHA-256 975e278c3bbd3a6b9e9ffe3d18194b2539c9f10fd25d79e386dfd44270cb62e0 at project commit f600c7a8e69a23a029559872652302ac299c2aea
Result evidence: 03_report_03.md 6610ed4db1de002fddbb72f3069c74bda7e57e5f2030c762dfc697d0494ac9e8; 04_report_00.md 549f2d46cb9b66123dbd0b14647934526274f38d501302e1869142b4302ad243; 05_report_00.md cd975d6aa1dae40af19bd6d6db98384304ba5c8bfe1e44c654b203fd7a6da977; compass archive renders/2026-11-25_svetove-strany/
Accepted evidence: H2 entrance built and cleared; 53-stone foundation around the slab; 27.28 m walk from the south entrance to the basement landing; four compass frames plus the link frame archived in Meta
Required preceding results: satisfied
Cooperator-owned decisions: satisfied — Michal approved V20, directed the foundation and the entrance path, asked for the compass archive, and asked for this closure
Residual-risk disposition: satisfied — FT-V20-01 through FT-V20-06 are recorded above and are not open grants
Upgrade-ledger reconciliation: complete (AGENTS.md declares no AP upgrade ledger)
Active-context reconciliation: complete
Active mutation: none
Closure authority: present
Implementation completion: implementation-PASS
Audit completion: not-required
Publication: not-applicable
Public Git equality: not-applicable
Orchestrator acceptance: acceptance-PASS
Closure actor: ORCHESTRATOR
Logical-whole closure: closed-by-ORCHESTRATOR
```

Michalov Blender PID `96634` pri uzávierke ešte bežal. Žiadny grant sa ho nedotkol a žiadna ďalšia mutácia z tohto celku nebeží.

### Podklad pre Master

```text
Run entry: 20 | kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20 | closed | depends on: kysucka-moderna-chata-basement-layout-study-v19 | handout: projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20/00_handout.md | evidence: H2 exterior stair, 53-stone perimeter foundation and 27.28 m entrance walk saved in work/v20/*_chodnik.blend (exterior 2121f6f4…, interior 975e278c…); four compass frames and the link frame archived in renders/2026-11-25_svetove-strany/; canonical interior and Git publication remain with the Cooperator; R-V18-01 stays open
```
