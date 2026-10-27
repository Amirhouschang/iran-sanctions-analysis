# Sanktionen gegen den Iran, 1979–2025

🇬🇧 [English version](README.en.md)

Analyse der Sanktionen gegen den Iran auf zwei Ebenen:

- **Sanktionsfälle (GSDB):** alle erfassten Sanktionsfälle gegen den Iran seit 1979 und ihre Einordnung in das weltweite Sanktionsgeschehen: wer Sanktionen verhängt hat, mit welchen Instrumenten, aus welchen Gründen und mit welchem Ergebnis.
- **Betroffene (OpenSanctions):** welche iranischen Firmen, Personen, Organisationen und Schiffe heute auf Sanktionslisten stehen, in welchen Sektoren und mit welchen Ämtern.

## Interaktives Dashboard

**[Dashboard öffnen](https://iran-sanctions-analysis.streamlit.app/)**: alle Ergebnisse interaktiv, auf Deutsch und Englisch, mit Suche und Filtern für die gelisteten Entitäten.
Zum lokalen Starten siehe [Ausführen](#ausführen).

## Teil 1: Sanktionsfälle (GSDB)

### 1. Wie haben sich die Sanktionen gegen den Iran entwickelt, und wer hat sie verhängt?

- Der Iran ist das **am zweithäufigsten sanktionierte Land** der Welt: 62 Fälle seit 1979, nach Russland (75).
- 1979–2005: meist 1–3 Fälle in Kraft, keiner 1982–1983; alle von den USA.
- 2006–2015: starker Anstieg im Atomstreit (UN, EU und andere), bis zu 20 Fälle in Kraft (2012–2015).
- 2016: Mit der Umsetzung des Atomabkommens (JCPOA) im Januar 2016 endeten 13 Fälle; Ende 2016 waren nur noch 7 in Kraft.
  Die Grafik zählt jeden Fall, der in einem Jahr zumindest zeitweise in Kraft war; deshalb zeigt sie für 2016 25 Fälle und den Rückgang erst 2017.
- 2018–2025: erneuter Anstieg nach dem US-Ausstieg, Höchststand von **36 Fällen in Kraft im Jahr 2025**.
- Die USA haben 25 der 62 Fälle verhängt. China, Russland, Indien, Saudi-Arabien und die Türkei sind nicht als Sender eines Falls gegen den Iran erfasst (UN-Fälle werden getrennt gezählt).

[![Sanktionsfälle gegen den Iran in Kraft pro Jahr](images/timeline_de.png)](images/timeline_de.png)

### 2. Welche Instrumente wurden eingesetzt?

- Handelssanktionen sind gegen den Iran viel häufiger als weltweit (71 % gegenüber 41 % der Fälle).
- Finanzsanktionen stiegen von jedem dritten neuen Fall (1979–2005) auf fast neun von zehn (2017–2025).
- Unter den 43 Fällen mit Finanzsanktionen dominieren Vermögenssperren (86 %) und Verbote von Finanzdienstleistungen (81 %). Beschränkungen der Zahlungsinfrastruktur (z. B. SWIFT) sind nur in zwei Fällen erfasst, beide durch die EU (2012, 2025).

[![Sanktionsinstrumente: Iran im Vergleich zur Welt](images/instruments_de.png)](images/instruments_de.png)
[![Finanzmaßnahmen: Iran im Vergleich zur Welt](images/financial_measures_de.png)](images/financial_measures_de.png)

### 3. Warum wurden Sanktionen verhängt, und wie endeten sie?

- Erklärte Ziele (ein Fall kann mehrere haben): Atomprogramm / Friedensbedrohung 24, Politikwechsel 16, Menschenrechte 15, Terrorismus 14, sonstige Ziele 8.
- Ende 2025 sind 36 der 62 Fälle noch in Kraft.
- Alle 10 bewerteten Ziele zu Terrorismus und Menschenrechten sind **gescheitert**.
- Atomprogramm / Friedensbedrohung: 14 von 17 bewerteten Zielen gelten als „voller Erfolg“, d. h. der Iran hat die Forderungen vollständig angenommen.
  13 davon gehören zu Fällen, die im Januar–Mai 2016 nach der Umsetzung des JCPOA endeten; einer endete 2020.
  Die Bewertung erfolgt bei Fallende und ist mit Vorsicht zu lesen: Der Streit war nicht gelöst,
  und die USA (2018), die UN und die EU (beide 2025) haben erneut Sanktionen verhängt.

[![Ergebnisse beendeter Fälle nach Ziel](images/outcomes_de.png)](images/outcomes_de.png)

### 4. Wie steht der Iran im weltweiten Vergleich da?

| Rang | Am häufigsten sanktionierte Länder | Fälle |
|---|---|---|
| 1 | Russland | 75 |
| **2** | **Iran** | **62** |
| 3 | China | 57 |
| 4 | Belarus | 47 |
| 5 | Myanmar | 42 |

| Rang | Sanktionierende Länder | Fälle | davon als EU-/EWG-Mitglied |
|---|---|---|---|
| 1 | USA | 686 | – |
| 2 | Großbritannien | 261 | 141 |
| **3** | **Deutschland** | **241** | **203** |
| 4 | Frankreich | 240 | 203 |
| 5 | Dänemark, Niederlande | je 222 | 204 |

Fälle der EU und ihrer Vorgängerin, der EWG, zählen für alle Länder, die bei Beginn des Falls Mitglied waren.
Die EU (190 Fälle) und die UN (88 Fälle) sind keine Länder und werden getrennt gezählt.
Die 241 Fälle Deutschlands enthalten einen Fall der ehemaligen DDR; ohne ihn teilen sich Deutschland und Frankreich mit je 240 Fällen Rang 3.

- Als ein Akteur gezählt, ist die **EU** nach den USA der zweitgrößte Sanktionsakteur (190 gegenüber 686 Fällen; Großbritannien hat 120 eigene Fälle).
  Der Iran gehört zu den Ländern, gegen die sie am häufigsten Sanktionen verhängt hat: 8 Fälle, Rang 3 gemeinsam mit Myanmar, nach Belarus (12) und Russland (11).
- **Deutschland** steht weltweit auf Rang 3 (241 Fälle einschließlich EU- und EWG-Sanktionen). Gegen den Iran handelt es über die EU und die E3,
  die 2025 die Rückkehr der UN-Sanktionen ausgelöst haben.

**Fallzahlen zeigen erfasste Sanktionsepisoden, nicht die Härte der Sanktionen.**

## Teil 2: Wer ist betroffen? (OpenSanctions)

Stand 27.10.2026, gefiltert auf den Ländercode `ir`. Hier werden einzelne gelistete Entitäten gezählt, keine Sanktionsfälle.

### 5. Wer sanktioniert iranische Entitäten?

- 4.972 iranische Einträge in OpenSanctions, davon **2.840 sanktioniert** (1.316 Personen, 1.323 Firmen und Organisationen, 201 Schiffe).
  Die übrigen sind vor allem politisch exponierte Personen (PEPs) ohne Sanktion.
- Die **USA** sanktionieren 2.242 der 2.840 Entitäten (79 %), danach folgen EU (728), Ukraine (608), Großbritannien (577) und Kanada (495).
- Nur 400 Entitäten stehen auf Listen der USA und der EU; 328 sanktioniert die EU ohne US-Gegenstück.
- Die USA listen fast alle Schiffe (199 von 201); EU, Ukraine und Großbritannien sanktionieren überwiegend Personen.

[![Sanktionierte iranische Entitäten je Akteur](opensanctions/images/opensanctions_akteure_de.png)](opensanctions/images/opensanctions_akteure_de.png)

### 6. Welche Bereiche und Ämter sind betroffen?

- Sektoren der sanktionierten Firmen, Organisationen und Schiffe: am häufigsten Schifffahrt (278), Energie (162, vor allem Öl und Petrochemie) und Banken/Finanzen (139).
  Nuklear (82), Rüstung (69) und IRGC (40) ergeben zusammen 191 Einträge.
- Ämter der Personen: Sanktioniert sind vor allem Militär und IRGC (226), Geheimdienst und Sicherheitskräfte (116) und Justiz (100), jeweils zu über 90 %.
  Parlamentsabgeordnete (4 %), Mitglieder des Expertenrats (7 %) und Diplomaten (8 %) sind kaum sanktioniert.
- Sanktionen treffen also gezielt den Sicherheits-, Justiz- und Rüstungsapparat und kaum die gewählten oder repräsentativen Institutionen.

## Datenquellen

| Daten | Quelle | Zeitraum |
|---|---|---|
| Sanktionsfälle weltweit (GSDB-R5) | Felbermayr et al. (2020), *The Global Sanctions Data Base*, European Economic Review 129 | 1949–2025 |
| Arten von Finanzsanktionen (GSDB-FS) | Yotov et al. (2026), *Financial Sanctions and International Trade*, CGPA Working Paper 2026014, Drexel University | 1950–2025 |
| Gelistete Entitäten und Ämter | OpenSanctions (2026), *Default Dataset* (`targets.simple.csv`, `targets.nested.json`), [opensanctions.org](https://www.opensanctions.org/), Lizenz CC BY-NC 4.0 | Stand 27.10.2026 |

Die GSDB ist auf Anfrage unter [globalsanctionsdatabase.com/data](https://www.globalsanctionsdatabase.com/data/) erhältlich.
Kommerzielle Nutzung und Weitergabe sind nicht erlaubt, deshalb sind die GSDB-Rohdaten hier nicht enthalten. Das Dashboard nutzt für die GSDB nur aggregierte Tabellen (Zählungen und Anteile).

OpenSanctions ist für nicht-kommerzielle Nutzung frei. Im Repository liegen nur die aufbereiteten Iran-Tabellen, ohne Geburtsdaten, Adressen, Telefonnummern, E-Mails und Ausweisnummern.

## Projektstruktur

```
iran_sanctions_analysis.ipynb          Teil 1 (GSDB): Datenprüfung, Diagramme, Interpretation, Limitations, Quellen
README.en.md                           englische Version dieses README
dashboard/
    app.py                             Streamlit-Dashboard (Deutsch / Englisch)
    data/                              vom GSDB-Notebook exportierte aggregierte Tabellen
images/                                Diagramme Teil 1: <name>.png (Englisch), <name>_de.png (Deutsch), Karten als .html
opensanctions/
    01_load_opensanctions_iran.py      lädt OpenSanctions und filtert auf den Iran
    02_opensanctions_iran_analysis.ipynb   Teil 2: Kategorien, Akteure, Sektoren, Ämter, Export
    03_load_opensanctions_positions.py lädt die Ämter aus targets.nested.json
    data/                              aufbereitete Tabellen für das Dashboard
    images/                            Diagramme Teil 2 (Deutsch und Englisch)
.streamlit/config.toml                 Dashboard-Design (hell)
requirements.txt
```

## Ausführen

**Teil 1 (GSDB):** GSDB-Daten anfragen und die Dateien als `GSDB-R5/GSDB-R5.csv` und `GSDB-FS/GSDB-FS.csv` im Projektordner speichern. `requirements.txt` enthält die Pakete für das Dashboard;
das Notebook braucht zusätzlich matplotlib, country_converter und Jupyter:

```
pip install -r requirements.txt matplotlib country_converter notebook
jupyter notebook iran_sanctions_analysis.ipynb    # alle Zellen ausführen; exportiert dashboard/data und images
```

**Teil 2 (OpenSanctions):** im Ordner `opensanctions/` (lädt die Daten direkt von OpenSanctions, mehrere GB):

```
python 01_load_opensanctions_iran.py
python 03_load_opensanctions_positions.py
jupyter notebook 02_opensanctions_iran_analysis.ipynb    # alle Zellen ausführen; exportiert opensanctions/data
```

**Dashboard:**

```
streamlit run dashboard/app.py
```

## Grenzen

**Teil 1 (GSDB)**
- Fallzahlen messen nicht die Härte: Ein umfassendes Embargo zählt als ein Fall, eine schrittweise Verschärfung als mehrere.
- Die Ergebnisse sind Bewertungen bei Ende eines Falls, auf Grundlage von Regierungsangaben und Presseberichten.
- Enddaten sind Kodierungen der GSDB: Ein beendeter Fall heißt nicht immer, dass die Sanktionen endeten. So gelten die EU-Menschenrechtssanktionen
  gegen den Iran von 2011 in den Daten als 2016 beendet, obwohl die EU dieses Regime jedes Jahr verlängert hat ([Rat der EU, 2026](https://www.consilium.europa.eu/en/press/press-releases/2026/03/30/human-rights-in-iran-council-extends-sanctions-regime-until-april-2027/)).
- Die Daten erfassen, welche Maßnahmen verhängt wurden, nicht ihre wirtschaftlichen oder humanitären Folgen.
- Für den Iran beginnen die Daten 1979.

**Teil 2 (OpenSanctions)**
- Momentaufnahme vom 27.10.2026; OpenSanctions wird mehrmals täglich aktualisiert. Ein Sanktionsdatum ist nicht enthalten, eine zeitliche Entwicklung lässt sich daher nicht ableiten.
- Gefiltert wurde auf den Ländercode `ir`. Entitäten mit Iran-Bezug, die nur einem anderen Land zugeordnet sind (z. B. Tarnfirmen in den VAE), fehlen.
- Kategorien, Sektoren und Amtsgruppen sind eine eigene Zuordnung über Schlüsselwörter, keine amtliche Branchen- oder Amtsangabe; einzelne Fehlzuordnungen sind möglich, 16 % der Firmen, Organisationen und Schiffe bleiben ohne Sektor.
- Die PEP-Daten aus Wikidata enthalten auch ehemalige Amtsträger.

## Wie dieses Projekt entstanden ist

Fragen, Daten und Methoden habe ich ausgewählt und die Ergebnisse an den Daten, den GSDB-Codebooks und der Dokumentation von OpenSanctions geprüft.
KI (Claude) hat beim Schreiben von Code und Texten geholfen. Wie ich mit KI arbeite: [local-ai-workflow](https://github.com/Amirhouschang/local-ai-workflow)

## Rechte

© 2026 Amirhoushang Rahmannejad. Alle Rechte vorbehalten. Code, Texte und Diagramme dürfen angesehen und geprüft, aber nicht kopiert oder weiterverwendet werden.
Feedback gern über Issues. Die GSDB-Daten gehören dem GSDB-Team der Drexel University.
Die OpenSanctions-Daten in `opensanctions/data/` stammen von OpenSanctions und stehen unter der Lizenz [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
