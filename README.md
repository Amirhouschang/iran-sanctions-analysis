# Sanctions against Iran, 1979–2025

🇩🇪 [Deutsche Version](README.de.md)

Analysis of all recorded sanction cases against Iran and their place in global sanction activity,
based on the Global Sanctions Data Base (GSDB): who imposed sanctions, with which instruments, for which reasons, and with what result.

## Interactive dashboard

The Streamlit dashboard shows all results interactively, in English and German.
To run it locally, see [How to run](#how-to-run).

## Questions and findings

### 1. How did sanctions against Iran develop, and who imposed them?

- Iran is the **second most sanctioned country** in the world: 62 cases since 1979, after Russia (75).
- 1979–2005: mostly 1–3 cases in force, none in 1982–1983; all imposed by the US.
- 2006–2016: strong increase during the nuclear dispute (UN, EU and others), peak of 25 cases in 2016; drop to 8 after the JCPOA.
- 2018–2025: new increase after the US withdrawal, highest level of **36 cases in force in 2025**.
- The US imposed 25 of the 62 cases. China, Russia, India, Saudi Arabia and Turkey do not appear as senders of any case against Iran (UN cases are counted separately).

[![Sanction cases against Iran in force per year](images/timeline.png)](images/timeline.png)

### 2. Which instruments were used?

- Trade sanctions are far more common against Iran than worldwide (71% vs. 41% of cases).
- Financial sanctions rose from one in three new cases (1979–2005) to almost nine in ten (2017–2025).
- Asset freezes (86%) and bans on financial services (81%) dominate. SWIFT exclusion was used twice, both times by the EU (2012, 2025).

[![Sanction instruments: Iran vs. world](images/instruments.png)](images/instruments.png)
[![Financial measures: Iran vs. world](images/financial_measures.png)](images/financial_measures.png)

### 3. Why were sanctions imposed, and how did they end?

- At the end of 2025, 36 of 62 cases are still in force.
- All 10 assessed objectives on terrorism and human rights **failed**.
- 14 of 17 nuclear objectives are coded as "full success". These are almost all sanctions lifted under the JCPOA in 2016,
  which were reimposed by the US (2018) and the UN (2025).

[![Outcomes of ended cases by objective](images/outcomes.png)](images/outcomes.png)

### 4. How does Iran compare globally?

| Rank | Most sanctioned countries | Cases |
|---|---|---|
| 1 | Russia | 75 |
| **2** | **Iran** | **62** |
| 3 | China | 57 |
| 4 | Belarus | 47 |
| 5 | Myanmar | 42 |

| Rank | Sanctioning countries | Cases | of which as EU member |
|---|---|---|---|
| 1 | United States | 686 | – |
| 2 | United Kingdom | 247 | 127 |
| **3** | **Germany** | **227** | **189** |
| 4 | France | 226 | 189 |
| 5 | Denmark, Netherlands | 208 each | 190 |

The EU (190 cases) and the UN (88 cases) are not countries and are counted separately.

- The **EU** is the second largest sanctioning actor; Iran is among its most sanctioned targets (8 cases).
- **Germany** ranks third worldwide (227 cases incl. EU sanctions). Against Iran it acts through the EU and the E3,
  which triggered the return of the UN sanctions in 2025.

**Case counts show recorded sanction episodes, not how severe the sanctions were.**

## Data sources

| Data | Source | Period |
|---|---|---|
| Sanction cases worldwide (GSDB-R5) | Felbermayr et al. (2020), *The Global Sanctions Data Base*, European Economic Review 129 | 1949–2025 |
| Financial sanction types (GSDB-FS) | Yotov et al. (2026), *Financial Sanctions and International Trade*, CGPA Working Paper 2026014, Drexel University | 1950–2025 |

The GSDB is available free of charge on request at [globalsanctionsdatabase.com/data](https://www.globalsanctionsdatabase.com/data/).
Redistribution is not permitted, so the raw data is not included here. The dashboard uses only aggregated tables (counts and shares).

## Project structure

```
iran_sanctions_analysis.ipynb   analysis: data checks, charts, interpretation, limitations, sources
dashboard/
    app.py                      Streamlit dashboard (English / German)
    data/                       aggregated tables exported by the notebook
images/                         charts for this README
requirements.txt
```

## How to run

Request the GSDB data and place the files in `GSDB-R5/` and `GSDB-FS/`, then:

```
jupyter notebook iran_sanctions_analysis.ipynb    # run all cells; exports dashboard/data and images
streamlit run dashboard/app.py
```

## Limitations

- Case counts are not a measure of severity: a comprehensive embargo counts as one case, a step-by-step escalation as several.
- Outcome ratings are assessments made when a case ends, based on government statements and press reports.
- The data records which measures were imposed, not their economic or humanitarian impact.
- For Iran, the data starts in 1979.

## How this project was made

I chose the questions, the data and the methods, and checked the results against the data and the GSDB codebooks.
AI (Claude) helped with writing code and texts. How I work with AI: [local-ai-workflow](https://github.com/Amirhouschang/local-ai-workflow)

## Rights

© 2026 Amirhoushang Rahmannejad. All rights reserved. Code, texts and charts may be viewed and checked, but not copied or reused.
Feedback is welcome via issues. The GSDB data belongs to the GSDB team at Drexel University.
