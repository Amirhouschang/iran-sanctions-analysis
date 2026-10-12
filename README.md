# Sanctions against Iran, 1979–2025

🇩🇪 [Deutsche Version](README.de.md)

Analysis of all recorded sanction cases against Iran and their place in global sanction activity,
based on the Global Sanctions Data Base (GSDB): who imposed sanctions, with which instruments, for which reasons, and with what result.

## Interactive dashboard

**[Open the dashboard](https://iran-sanctions-analysis.streamlit.app/)**: all results interactively, in English and German.
To run it locally, see [How to run](#how-to-run).

## Questions and findings

### 1. How did sanctions against Iran develop, and who imposed them?

- Iran is the **second most sanctioned country** in the world: 62 cases since 1979, after Russia (75).
- 1979–2005: mostly 1–3 cases in force, none in 1982–1983; all imposed by the US.
- 2006–2015: strong increase during the nuclear dispute (UN, EU and others), up to 20 cases in force in 2012–2015.
- 2016: when the nuclear agreement (JCPOA) was implemented in January 2016, 13 cases ended; at the end of 2016 only 7 were still in force.
  The chart counts every case in force at any time during a year, so it shows 25 for 2016 and the drop only in 2017.
- 2018–2025: new increase after the US withdrawal, highest level of **36 cases in force in 2025**.
- The US imposed 25 of the 62 cases. China, Russia, India, Saudi Arabia and Turkey do not appear as senders of any case against Iran (UN cases are counted separately).

[![Sanction cases against Iran in force per year](images/timeline.png)](images/timeline.png)

### 2. Which instruments were used?

- Trade sanctions are far more common against Iran than worldwide (71% vs. 41% of cases).
- Financial sanctions rose from one in three new cases (1979–2005) to almost nine in ten (2017–2025).
- Among the 43 financial sanction cases, asset freezes (86%) and bans on financial services (81%) dominate. Restrictions on payment infrastructure (e.g. SWIFT) are recorded in only two cases, both by the EU (2012, 2025).

[![Sanction instruments: Iran vs. world](images/instruments.png)](images/instruments.png)
[![Financial measures: Iran vs. world](images/financial_measures.png)](images/financial_measures.png)

### 3. Why were sanctions imposed, and how did they end?

- Declared objectives (a case can have several): nuclear / threat to peace 24, policy change 16, human rights 15, terrorism 14, other objectives 8.
- At the end of 2025, 36 of 62 cases are still in force.
- All 10 assessed objectives on terrorism and human rights **failed**.
- Nuclear / threat to peace: 14 of 17 assessed objectives are coded as "full success", i.e. Iran fully accepted the demands.
  13 of them belong to cases that ended in January–May 2016, after the JCPOA was implemented; one ended in 2020.
  The rating is made when a case ends and should be read with caution: the dispute was not resolved,
  and the US (2018), the UN and the EU (both 2025) imposed sanctions again.

[![Outcomes of ended cases by objective](images/outcomes.png)](images/outcomes.png)

### 4. How does Iran compare globally?

| Rank | Most sanctioned countries | Cases |
|---|---|---|
| 1 | Russia | 75 |
| **2** | **Iran** | **62** |
| 3 | China | 57 |
| 4 | Belarus | 47 |
| 5 | Myanmar | 42 |

| Rank | Sanctioning countries | Cases | of which as EU/EEC member |
|---|---|---|---|
| 1 | United States | 686 | – |
| 2 | United Kingdom | 261 | 141 |
| **3** | **Germany** | **241** | **203** |
| 4 | France | 240 | 203 |
| 5 | Denmark, Netherlands | 222 each | 204 |

Cases of the EU and of its predecessor, the EEC, are assigned to the countries that were members when the case began.
The EU (190 cases) and the UN (88 cases) are not countries and are counted separately.
Germany's 241 cases include one case of the former GDR; without it, Germany and France share rank 3 with 240 cases each.

- Counted as a single actor, the **EU** is the second largest sanctioning actor after the US (190 vs. 686 cases; the UK has 120 cases of its own).
  Iran is among its most sanctioned targets: 8 cases, rank 3 together with Myanmar, after Belarus (12) and Russia (11).
- **Germany** ranks third worldwide (241 cases incl. EU and EEC sanctions). Against Iran it acts through the EU and the E3,
  which triggered the return of the UN sanctions in 2025.

**Case counts show recorded sanction episodes, not how severe the sanctions were.**

## Data sources

| Data | Source | Period |
|---|---|---|
| Sanction cases worldwide (GSDB-R5) | Felbermayr et al. (2020), *The Global Sanctions Data Base*, European Economic Review 129 | 1949–2025 |
| Financial sanction types (GSDB-FS) | Yotov et al. (2026), *Financial Sanctions and International Trade*, CGPA Working Paper 2026014, Drexel University | 1950–2025 |

The GSDB is available on request at [globalsanctionsdatabase.com/data](https://www.globalsanctionsdatabase.com/data/).
Commercial use and redistribution are not permitted, so the raw data is not included here. The dashboard uses only aggregated tables (counts and shares).

## Project structure

```
iran_sanctions_analysis.ipynb   analysis: data checks, charts, interpretation, limitations, sources
README.de.md                    German version of this README
dashboard/
    app.py                      Streamlit dashboard (English / German)
    data/                       aggregated tables exported by the notebook
images/                         charts for this README
.streamlit/config.toml          dashboard theme (light)
requirements.txt
```

## How to run

Request the GSDB data and save the files as `GSDB-R5/GSDB-R5.csv` and `GSDB-FS/GSDB-FS.csv` in the project folder. `requirements.txt` covers the dashboard;
the notebook additionally needs matplotlib, country_converter and Jupyter:

```
pip install -r requirements.txt matplotlib country_converter notebook
jupyter notebook iran_sanctions_analysis.ipynb    # run all cells; exports dashboard/data and images
streamlit run dashboard/app.py
```

## Limitations

- Case counts are not a measure of severity: a comprehensive embargo counts as one case, a step-by-step escalation as several.
- Outcome ratings are assessments made when a case ends, based on government statements and press reports.
- End dates are GSDB codings: an ended case does not always mean the sanctions ended. For example, the EU human-rights sanctions
  against Iran from 2011 are coded as ended in 2016, although the EU has extended this regime every year ([Council of the EU, 2026](https://www.consilium.europa.eu/en/press/press-releases/2026/03/30/human-rights-in-iran-council-extends-sanctions-regime-until-april-2027/)).
- The data records which measures were imposed, not their economic or humanitarian impact.
- For Iran, the data starts in 1979.

## How this project was made

I chose the questions, the data and the methods, and checked the results against the data and the GSDB codebooks.
AI (Claude) helped with writing code and texts. How I work with AI: [local-ai-workflow](https://github.com/Amirhouschang/local-ai-workflow)

## Rights

© 2026 Amirhoushang Rahmannejad. All rights reserved. Code, texts and charts may be viewed and checked, but not copied or reused.
Feedback is welcome via issues. The GSDB data belongs to the GSDB team at Drexel University.
