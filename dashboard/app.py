"""Streamlit dashboard: Sanctions against Iran, 1979–2025 (English / Deutsch).

Reads only the aggregated tables exported by iran_sanctions_analysis.ipynb (section 9),
so no individual GSDB sanction cases are included. Start with:

    streamlit run dashboard/app.py
"""

import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

DATA_DIR = Path(__file__).parent / "data"

# Colours (same as in the notebook)
COLOR_MAIN = "#1f4e79"    # Iran / main series
COLOR_LIGHT = "#6fa8dc"   # secondary series
COLOR_WORLD = "#9e9e9e"   # comparison: all sanctions worldwide
COLOR_DARK = "#5f6368"    # tertiary series / secondary text
COLOR_NEW = "#c0392b"     # highlight: new cases
MAP_REDS = ["#fcae91", "#fb6a4a", "#de2d26", "#a50f15"]       # same reds on both maps
MAP_CLASS_COLORS = ["#d9d9d9"] + MAP_REDS                      # world map: grey for 1–5 cases
LAND_COLOR = "#f0f0f0"                                         # countries without cases

st.set_page_config(page_title="Sanctions against Iran / Sanktionen gegen den Iran", layout="wide")


# ---------------------------------------------------------------- texts (EN / DE)
TEXT = {
    "en": {
        "title": "Sanctions against Iran, 1979–2025",
        "intro": "All recorded sanction cases against Iran and their place in global sanction activity.",
        "source_r5": "Data: Global Sanctions Data Base, Release 5 (Felbermayr et al., 2020).",
        "source_fs": "Data: Global Sanctions Data Base – Financial Sanctions (Yotov et al., 2026).",
        "no_data": "No data found. Run iran_sanctions_analysis.ipynb first (section 9 exports the tables to dashboard/data).",
        "show_data": "Show data",
        "kpi_cases": "Sanction cases against Iran",
        "kpi_cases_help": "{share}% of all {total:,} cases worldwide",
        "kpi_rank": "Rank among sanctioned countries",
        "kpi_rank_help": "After Russia",
        "kpi_force": "Cases in force, end of 2025",
        "kpi_us": "Imposed by the US",
        "kpi_eu": "Imposed by the EU",
        "tabs": ["Over time", "Who sanctions Iran", "Instruments", "Objectives & outcomes", "Global context", "About the data"],
        # over time
        "show_events": "Show key events",
        "t_timeline": "Sanction cases against Iran in force per year",
        "cases_in_force": "Cases in force",
        "years_new": "Years with new cases",
        "cap_timeline": "Line: cases in force in each year (ongoing cases counted up to 2025). Red points: years with new cases; the label shows how many. Case counts reflect recorded episodes, not the severity of sanctions.",
        "t_new_cont": "New vs. continuing cases per year",
        "continuing": "Continuing from earlier years",
        "new": "New in this year",
        "cap_new_cont": "No case was in force in 1982–1983.",
        "txt_time": (
            "- **1979–2005:** mostly 1–3 cases in force, none in 1982–1983; all imposed by the US.\n"
            "- **2006–2016:** strong increase during the nuclear dispute, peak of 25 cases in 2016.\n"
            "- **2017:** drop to 8 cases after the JCPOA was implemented.\n"
            "- **2018–2025:** new increase after the US withdrawal, highest level of 36 cases in 2025."
        ),
        # senders
        "t_iran_map": "Countries imposing sanctions on Iran, number of cases 1979–2025",
        "cap_iran_map": "Dark grey: Iran. EU cases are assigned to all EU member states at the time of imposition. UN cases (7) are not shown.",
        "t_actors": "Top 10 sanctioning actors against Iran (EU and UN as single actors)",
        "cap_actors": "A case imposed jointly by several actors counts for each of them.",
        "data_actors": "All sanctioning actors against Iran",
        "data_map_countries": "Countries on the map (EU cases counted for each member state)",
        # instruments
        "t_instr": "Instruments: Iran vs. all sanctions",
        "x_instr": "Share of cases using the instrument (%)",
        "cap_instr": "A case can use several instruments, so shares add up to more than 100%.",
        "t_fin": "Financial measures: Iran vs. all financial sanctions",
        "x_fin": "Share of financial cases using the measure (%)",
        "select_instr": "Instrument over time",
        "t_instr_time": "{instr}: share of cases in force using the instrument, 2006–2025",
        "y_share": "Share (%)",
        "cap_instr_time": "Starts in 2006: before that only 1–3 Iran cases were in force, too few for meaningful shares. Dotted lines: JCPOA implemented (2016), US withdrawal (2018).",
        "jcpoa": "JCPOA implemented",
        "us_exit": "US leaves JCPOA",
        "data_instr_period": "Instruments by period (share of new cases)",
        "data_fin_period": "Financial measures by period (number of new financial cases)",
        "txt_instr": (
            "- **Trade** sanctions are far more common against Iran than worldwide (71% vs. 41%).\n"
            "- **Financial** sanctions rose from one in three new cases (1979–2005) to almost nine in ten (2017–2025).\n"
            "- **Asset freezes** (86%) and **bans on financial services** (81%) dominate; SWIFT exclusion was used twice, both by the EU (2012, 2025)."
        ),
        # outcomes
        "kpi_ended": "Cases ended / still in force (end of 2025)",
        "t_outcomes": "Outcomes of ended cases by objective",
        "x_objectives": "Number of objectives",
        "cap_outcomes": "Outcomes are assessed per objective when a case ends, based on government statements and press reports.",
        "t_outcome_comp": "Share of outcomes: Iran vs. all sanctions worldwide",
        "txt_outcomes": (
            "- **Terrorism and human rights:** all 10 assessed objectives failed.\n"
            "- **Nuclear:** 14 of 17 objectives are coded as full success. These are almost all sanctions lifted under the JCPOA "
            "in 2016, which were reimposed by the US (2018) and the UN (2025); the rating should be read with caution."
        ),
        # global
        "h_targets": "Most sanctioned countries",
        "t_targets": "Top 10 sanctioned countries, 1949–2025",
        "other_countries": "Other countries",
        "data_targets": "Top 15 sanctioned countries by objective",
        "h_world": "Who sanctions the world?",
        "t_world_map": "Number of sanction cases imposed per country, 1949–2025",
        "cap_world_map": "Grey: countries with only 1–5 cases. EU cases are assigned to all EU member states at the time of imposition. Cases by the UN and other organisations are not shown.",
        "h_sender_countries": "Top 15 sanctioning countries",
        "cap_senders": "Cases = own cases + cases imposed as an EU member. Not countries and therefore listed separately: EU {eu} cases, UN {un} cases. Germany includes one case of the former GDR; without it, Germany and France share rank 3 (226 cases each).",
        "h_eu": "The EU as a sanctioning actor",
        "kpi_eu_cases": "EU cases",
        "kpi_eu_rank_help": "Rank {rank} after the US",
        "kpi_eu_force": "Still in force",
        "kpi_eu_iran": "Against Iran",
        "t_eu_decades": "New EU cases per decade",
        "cap_eu_decades": "The 2020s cover only 2020–2025.",
        "t_eu_targets": "Main targets of EU sanctions",
        "t_eu_instr": "EU instruments vs. all sanctions worldwide",
        "txt_germany": (
            "- **Germany** ranks #{rank} worldwide ({cases} cases incl. EU sanctions) and has {own} national cases of its own. "
            "Against Iran it acts through the EU and the E3 (France, Germany, UK), which triggered the return of the UN sanctions in 2025."
        ),
        "h_compare": "Non-Western senders compared",
        "cap_compare": "None of these countries appears as a sender of a case against Iran; UN cases are counted separately. Russia includes the Soviet Union.",
        "cases": "Cases",
        "new_cases": "New cases",
        "lang_note": "Country names are shown as in the source data (English).",
        "about": """
**Data**
- GSDB Release 5: 1,794 sanction cases worldwide, 1949–2025.
- GSDB Financial Sanctions: financial subtypes for the 1,072 cases with a financial component.
- This dashboard uses only aggregated tables (counts and shares). The raw data is available on request at
  [globalsanctionsdatabase.com/data](https://www.globalsanctionsdatabase.com/data/) and may not be redistributed.

**Limitations**
- Case counts are not a measure of severity: a comprehensive embargo counts as one case, a step-by-step escalation as several.
- Outcome ratings are assessments made when a case ends, not measured effects.
- The data records which measures were imposed, not their economic or humanitarian impact.
- Coverage for Iran starts in 1979.
- On the maps, EU cases are assigned to all member states; the UN and other organisations are not shown.

**Sources**
- Felbermayr, G., A. Kirilakha, C. Syropoulos, E. Yalcin, and Y. V. Yotov (2020), "The Global Sanctions Data Base,"
  *European Economic Review*, 129, 103561.
- Yotov, Y. V., G. Felbermayr, H. Kariem, A. Kirilakha, O. Kwon, C. Syropoulos, and E. Yalcin (2026),
  "Financial Sanctions and International Trade: Evidence from a New Database," Working Paper 2026014,
  Center for Global Policy Analysis, LeBow College of Business, Drexel University.

Full analysis: `iran_sanctions_analysis.ipynb`
""",
    },
    "de": {
        "title": "Sanktionen gegen den Iran, 1979–2025",
        "intro": "Alle erfassten Sanktionsfälle gegen den Iran und ihre Einordnung in das weltweite Sanktionsgeschehen.",
        "source_r5": "Daten: Global Sanctions Data Base, Release 5 (Felbermayr et al., 2020).",
        "source_fs": "Daten: Global Sanctions Data Base – Financial Sanctions (Yotov et al., 2026).",
        "no_data": "Keine Daten gefunden. Zuerst iran_sanctions_analysis.ipynb ausführen (Abschnitt 9 exportiert die Tabellen nach dashboard/data).",
        "show_data": "Daten anzeigen",
        "kpi_cases": "Sanktionsfälle gegen den Iran",
        "kpi_cases_help": "{share} % aller {total:,} Fälle weltweit",
        "kpi_rank": "Rang unter den sanktionierten Ländern",
        "kpi_rank_help": "Nach Russland",
        "kpi_force": "Fälle in Kraft, Ende 2025",
        "kpi_us": "Von den USA verhängt",
        "kpi_eu": "Von der EU verhängt",
        "tabs": ["Zeitverlauf", "Wer sanktioniert den Iran", "Instrumente", "Ziele & Ergebnisse", "Weltweiter Vergleich", "Über die Daten"],
        "show_events": "Wichtige Ereignisse anzeigen",
        "t_timeline": "Sanktionsfälle gegen den Iran in Kraft pro Jahr",
        "cases_in_force": "Fälle in Kraft",
        "years_new": "Jahre mit neuen Fällen",
        "cap_timeline": "Linie: Fälle in Kraft pro Jahr (laufende Fälle bis 2025 gezählt). Rote Punkte: Jahre mit neuen Fällen; die Zahl zeigt, wie viele. Fallzahlen zeigen erfasste Episoden, nicht die Härte der Sanktionen.",
        "t_new_cont": "Neue und fortlaufende Fälle pro Jahr",
        "continuing": "Fortlaufend aus früheren Jahren",
        "new": "Neu in diesem Jahr",
        "cap_new_cont": "1982–1983 war kein Fall in Kraft.",
        "txt_time": (
            "- **1979–2005:** meist 1–3 Fälle in Kraft, keiner 1982–1983; alle von den USA.\n"
            "- **2006–2016:** starker Anstieg im Atomstreit, Höchststand von 25 Fällen 2016.\n"
            "- **2017:** Rückgang auf 8 Fälle nach Umsetzung des Atomabkommens (JCPOA).\n"
            "- **2018–2025:** erneuter Anstieg nach dem US-Ausstieg, Höchststand von 36 Fällen 2025."
        ),
        "t_iran_map": "Länder mit Sanktionen gegen den Iran, Anzahl der Fälle 1979–2025",
        "cap_iran_map": "Dunkelgrau: Iran. EU-Fälle zählen für alle Länder, die bei Verhängung EU-Mitglied waren. UN-Fälle (7) sind nicht dargestellt.",
        "t_actors": "Top 10 der Sanktionsakteure gegen den Iran (EU und UN als je ein Akteur)",
        "cap_actors": "Ein Fall mehrerer Akteure zählt für jeden von ihnen.",
        "data_actors": "Alle Sanktionsakteure gegen den Iran",
        "data_map_countries": "Länder auf der Karte (EU-Fälle für jedes Mitglied gezählt)",
        "t_instr": "Instrumente: Iran im Vergleich zu allen Sanktionen",
        "x_instr": "Anteil der Fälle mit diesem Instrument (%)",
        "cap_instr": "Ein Fall kann mehrere Instrumente nutzen; die Anteile ergeben zusammen mehr als 100 %.",
        "t_fin": "Finanzmaßnahmen: Iran im Vergleich zu allen Finanzsanktionen",
        "x_fin": "Anteil der Finanzsanktionsfälle mit dieser Maßnahme (%)",
        "select_instr": "Instrument im Zeitverlauf",
        "t_instr_time": "{instr}: Anteil der laufenden Fälle mit diesem Instrument, 2006–2025",
        "y_share": "Anteil (%)",
        "cap_instr_time": "Beginnt 2006: Davor liefen nur 1–3 Iran-Fälle, zu wenige für aussagekräftige Anteile. Gepunktete Linien: Umsetzung des JCPOA (2016), US-Ausstieg (2018).",
        "jcpoa": "JCPOA umgesetzt",
        "us_exit": "US-Ausstieg aus dem JCPOA",
        "data_instr_period": "Instrumente nach Zeitraum (Anteil der neuen Fälle)",
        "data_fin_period": "Finanzmaßnahmen nach Zeitraum (Anzahl neuer Finanzsanktionsfälle)",
        "txt_instr": (
            "- **Handelssanktionen** sind gegen den Iran viel häufiger als weltweit (71 % gegenüber 41 %).\n"
            "- **Finanzsanktionen** stiegen von jedem dritten neuen Fall (1979–2005) auf fast neun von zehn (2017–2025).\n"
            "- **Vermögenssperren** (86 %) und **Verbote von Finanzdienstleistungen** (81 %) dominieren; einen SWIFT-Ausschluss gab es zweimal, beide Male durch die EU (2012, 2025)."
        ),
        "kpi_ended": "Fälle beendet / noch in Kraft (Ende 2025)",
        "t_outcomes": "Ergebnisse beendeter Fälle nach Begründung",
        "x_objectives": "Anzahl der Ziele",
        "cap_outcomes": "Ergebnisse werden pro Ziel bei Ende eines Falls bewertet, auf Grundlage von Regierungsangaben und Presseberichten.",
        "t_outcome_comp": "Anteil der Ergebnisse: Iran im Vergleich zu allen Sanktionen weltweit",
        "txt_outcomes": (
            "- **Terrorismus und Menschenrechte:** alle 10 bewerteten Ziele gescheitert.\n"
            "- **Atomprogramm:** 14 von 17 Zielen gelten als voller Erfolg. Das sind fast nur die 2016 durch das JCPOA aufgehobenen "
            "Sanktionen, die die USA (2018) und die UN (2025) wieder verhängt haben; die Bewertung ist mit Vorsicht zu lesen."
        ),
        "h_targets": "Die meistsanktionierten Länder",
        "t_targets": "Top 10 der sanktionierten Länder, 1949–2025",
        "other_countries": "Andere Länder",
        "data_targets": "Top 15 der sanktionierten Länder nach Begründung",
        "h_world": "Wer sanktioniert die Welt?",
        "t_world_map": "Anzahl der verhängten Sanktionsfälle pro Land, 1949–2025",
        "cap_world_map": "Grau: Länder mit nur 1–5 Fällen. EU-Fälle zählen für alle Länder, die bei Verhängung EU-Mitglied waren. Fälle der UN und anderer Organisationen sind nicht dargestellt.",
        "h_sender_countries": "Top 15 der sanktionierenden Länder",
        "cap_senders": "Fälle = eigene Fälle + Fälle als EU-Mitglied. Keine Länder und daher getrennt aufgeführt: EU {eu} Fälle, UN {un} Fälle. Deutschland enthält einen Fall der ehemaligen DDR; ohne ihn teilen sich Deutschland und Frankreich Rang 3 (je 226 Fälle).",
        "h_eu": "Die EU als Sanktionsakteur",
        "kpi_eu_cases": "EU-Fälle",
        "kpi_eu_rank_help": "Rang {rank} nach den USA",
        "kpi_eu_force": "Noch in Kraft",
        "kpi_eu_iran": "Gegen den Iran",
        "t_eu_decades": "Neue EU-Fälle pro Jahrzehnt",
        "cap_eu_decades": "Die 2020er umfassen nur 2020–2025.",
        "t_eu_targets": "Hauptziele der EU-Sanktionen",
        "t_eu_instr": "EU-Instrumente im Vergleich zu allen Sanktionen weltweit",
        "txt_germany": (
            "- **Deutschland** steht weltweit auf Rang {rank} ({cases} Fälle einschließlich EU-Sanktionen) und hat {own} eigene nationale Fälle. "
            "Gegen den Iran handelt es über die EU und die E3 (Frankreich, Deutschland, Großbritannien), die 2025 die Rückkehr der UN-Sanktionen ausgelöst haben."
        ),
        "h_compare": "Nicht-westliche Sender im Vergleich",
        "cap_compare": "Keines dieser Länder ist als Sender eines Falls gegen den Iran erfasst; UN-Fälle werden getrennt gezählt. Russland einschließlich Sowjetunion.",
        "cases": "Fälle",
        "new_cases": "Neue Fälle",
        "lang_note": "Ländernamen wie in den Quelldaten (Englisch).",
        "about": """
**Daten**
- GSDB Release 5: 1.794 Sanktionsfälle weltweit, 1949–2025.
- GSDB Financial Sanctions: Unterarten der Finanzsanktionen für die 1.072 Fälle mit Finanzkomponente.
- Dieses Dashboard nutzt nur aggregierte Tabellen (Zählungen und Anteile). Die Rohdaten gibt es auf Anfrage unter
  [globalsanctionsdatabase.com/data](https://www.globalsanctionsdatabase.com/data/); sie dürfen nicht weitergegeben werden.

**Grenzen der Analyse**
- Fallzahlen messen nicht die Härte: Ein umfassendes Embargo zählt als ein Fall, eine schrittweise Verschärfung als mehrere.
- Die Ergebnisse sind Bewertungen bei Ende eines Falls, keine gemessenen Wirkungen.
- Die Daten erfassen, welche Maßnahmen verhängt wurden, nicht ihre wirtschaftlichen oder humanitären Folgen.
- Für den Iran beginnen die Daten 1979.
- Auf den Karten zählen EU-Fälle für alle Mitgliedsstaaten; die UN und andere Organisationen sind nicht dargestellt.

**Quellen**
- Felbermayr, G., A. Kirilakha, C. Syropoulos, E. Yalcin, and Y. V. Yotov (2020), "The Global Sanctions Data Base,"
  *European Economic Review*, 129, 103561.
- Yotov, Y. V., G. Felbermayr, H. Kariem, A. Kirilakha, O. Kwon, C. Syropoulos, and E. Yalcin (2026),
  "Financial Sanctions and International Trade: Evidence from a New Database," Working Paper 2026014,
  Center for Global Policy Analysis, LeBow College of Business, Drexel University.

Vollständige Analyse: `iran_sanctions_analysis.ipynb`
""",
    },
}

# Category labels from the data (English) and their German translation
LABELS_DE = {
    # instruments
    "Trade": "Handel", "Financial": "Finanzen", "Travel": "Reisen", "Arms": "Waffen",
    "Military assistance": "Militärhilfe", "Other": "Sonstiges",
    # financial subtypes
    "Asset freeze": "Vermögenssperre", "Financial services": "Finanzdienstleistungen",
    "Investment restrictions": "Investitionsverbote", "Payment infrastructure (e.g. SWIFT)": "Zahlungsinfrastruktur (z. B. SWIFT)",
    "Aid": "Entwicklungshilfe",
    # outcomes
    "Full success": "Voller Erfolg", "Partial success": "Teilerfolg",
    "Negotiated settlement": "Verhandlungslösung", "Failed": "Gescheitert",
    # objectives
    "Nuclear / threat to peace": "Atomprogramm / Friedensbedrohung", "Terrorism": "Terrorismus",
    "Human rights": "Menschenrechte", "Policy change": "Politikwechsel", "End war": "Kriegsende",
    "Democracy": "Demokratie", "Destabilise regime": "Regimedestabilisierung",
    "Territorial conflict": "Territorialkonflikt",
    # groups
    "Iran": "Iran", "World": "Welt", "EU": "EU",
}

# Raw objective codes (used in the sender tables)
OBJECTIVE_CODES = {
    "en": {"policy_change": "Policy change", "human_rights": "Human rights", "democracy": "Democracy",
           "end_war": "End war", "terrorism": "Terrorism", "prevent_war": "Nuclear / threat to peace",
           "territorial_conflict": "Territorial conflict", "destab_regime": "Destabilise regime", "other": "Other"},
}
OBJECTIVE_CODES["de"] = {code: LABELS_DE[label] for code, label in OBJECTIVE_CODES["en"].items()}

EVENTS_DE = {
    1979: "Revolution, Geiselkrise",
    1984: "US-Terrorliste",
    1995: "US-Handelsembargo",
    2006: "Erste UN-Sanktionen",
    2012: "EU-Ölembargo, SWIFT",
    2016: "JCPOA umgesetzt",
    2018: "US-Ausstieg aus dem JCPOA",
    2022: "Proteste „Frau, Leben, Freiheit“",
    2025: "UN-Snapback",
}

COLUMN_NAMES = {
    "en": {
        "year": "Year", "cases_in_force": "Cases in force", "new_cases": "New cases", "continuing": "Continuing",
        "sender": "Actor", "cases": "Cases", "country": "Country", "iso3": "ISO3", "period": "Period",
        "financial_cases": "Financial cases", "outcome": "Outcome", "Iran": "Iran", "World": "World",
        "rank": "Rank", "target": "Country", "total_cases": "Total cases", "first_year": "First year",
        "last_year": "Last year", "peak_year": "Peak year", "peak_decade": "Peak decade",
        "cases_against_iran": "Cases against Iran", "world_rank": "World rank", "ongoing": "Ongoing",
        "against_iran": "Against Iran", "top_targets": "Main targets", "top_objectives": "Main objectives",
        "own_cases": "Own cases", "via_eu": "As EU member",
    },
    "de": {
        "year": "Jahr", "cases_in_force": "Fälle in Kraft", "new_cases": "Neue Fälle", "continuing": "Fortlaufend",
        "sender": "Akteur", "cases": "Fälle", "country": "Land", "iso3": "ISO3", "period": "Zeitraum",
        "financial_cases": "Finanzsanktionsfälle", "outcome": "Ergebnis", "Iran": "Iran", "World": "Welt",
        "rank": "Rang", "target": "Land", "total_cases": "Fälle gesamt", "first_year": "Erstes Jahr",
        "last_year": "Letztes Jahr", "peak_year": "Spitzenjahr", "peak_decade": "Stärkstes Jahrzehnt",
        "cases_against_iran": "Fälle gegen Iran", "world_rank": "Weltrang", "ongoing": "Laufend",
        "against_iran": "Gegen Iran", "top_targets": "Hauptziele", "top_objectives": "Hauptgründe",
        "own_cases": "Eigene Fälle", "via_eu": "Als EU-Mitglied",
    },
}


# ---------------------------------------------------------------- language
lang_choice = st.radio("Sprache / Language", ["English", "Deutsch"], horizontal=True, label_visibility="collapsed")
LANG = "de" if lang_choice == "Deutsch" else "en"
T = TEXT[LANG]


def lab(value):
    """Translate a category label from the data into the selected language."""
    return LABELS_DE.get(value, value) if LANG == "de" else value


def cols(df):
    """Rename table columns (and objective-code columns) into the selected language."""
    names = dict(COLUMN_NAMES[LANG])
    names.update(OBJECTIVE_CODES[LANG])
    return df.rename(columns={c: names.get(c, lab(c)) for c in df.columns})


def translate_objective_codes(text):
    """Replace raw objective codes in strings such as 'policy_change (20)'."""
    for code, label in OBJECTIVE_CODES[LANG].items():
        text = text.replace(code, label)
    return text


# ---------------------------------------------------------------- data
@st.cache_data
def load_csv(name):
    """Load one exported table from the dashboard data folder."""
    return pd.read_csv(DATA_DIR / name)


@st.cache_data
def load_kpis():
    """Load the headline figures exported by the notebook."""
    return json.loads((DATA_DIR / "kpis.json").read_text())


if not (DATA_DIR / "kpis.json").exists():
    st.error(T["no_data"])
    st.stop()

kpis = load_kpis()


# ---------------------------------------------------------------- chart helpers
def chart_title(text):
    """Chart title as text above the chart (keeps titles and legends apart)."""
    st.markdown(f"**{text}**")


def show_chart(fig, height=420):
    """Common layout for all charts: white background, recessive grid, legend above the plot."""
    fig.update_layout(
        template="plotly_white",
        height=height,
        margin=dict(l=10, r=10, t=30, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.0, x=0, title_text=""),
        hoverlabel=dict(bgcolor="white"),
        font=dict(size=12, color="#31333f"),
        paper_bgcolor="white",   # fixed light background, independent of dark mode
        plot_bgcolor="white",
    )
    fig.update_xaxes(showgrid=False, linecolor="#cccccc")
    fig.update_yaxes(gridcolor="#eeeeee", zeroline=False)
    st.plotly_chart(fig, use_container_width=True, theme=None)


def show_map(fig, height=520):
    """Common layout for maps: land in neutral grey, no Antarctica."""
    fig.update_geos(
        showframe=False, showcoastlines=False, projection_type="natural earth",
        showland=True, landcolor=LAND_COLOR, showcountries=True, countrycolor="white",
        lataxis_range=[-58, 90],
    )
    fig.update_layout(
        template="plotly_white", height=height, margin=dict(l=0, r=0, t=10, b=0),
        paper_bgcolor="white", font=dict(color="#31333f"),  # fixed light background, independent of dark mode
    )
    fig.update_geos(bgcolor="white")
    st.plotly_chart(fig, use_container_width=True, theme=None)


def show_data(df, label=None):
    """Table view of the data behind a chart."""
    with st.expander(label or T["show_data"]):
        st.dataframe(cols(df), use_container_width=True, hide_index=True)


def comparison_bars(df, label_col, share_col, group_name, x_title):
    """Horizontal bars comparing a group (Iran or EU) with the world; shares 0–1, largest on top."""
    data = df.sort_values(share_col).copy()
    data["label"] = data[label_col].map(lab)
    fig = go.Figure()
    # World first, group second: in grouped horizontal bars the later trace is drawn on top
    for col, name, color in (("world_share", lab("World"), COLOR_WORLD), (share_col, lab(group_name), COLOR_MAIN)):
        values = data[col] * 100
        fig.add_bar(
            y=data["label"], x=values, orientation="h", name=name, marker_color=color,
            text=values.round(0).astype(int).astype(str) + "%", textposition="outside",
            hovertemplate="%{y}: %{x:.0f}% (" + name + ")<extra></extra>",
        )
    fig.update_layout(barmode="group", xaxis_title=x_title, xaxis_range=[0, 108], yaxis_title="",
                      legend_traceorder="reversed")
    return fig


def ranked_bars(df, label_col, value_col, highlight=None, x_title=None):
    """Horizontal bars sorted from largest (top) to smallest, optional highlight of one entry."""
    data = df.sort_values(value_col).copy()
    colors = [COLOR_MAIN if (highlight is None or v == highlight) else COLOR_WORLD for v in data[label_col]]
    fig = go.Figure(go.Bar(
        y=data[label_col], x=data[value_col], orientation="h", marker_color=colors,
        text=data[value_col], textposition="outside", hovertemplate="%{y}: %{x}<extra></extra>",
    ))
    fig.update_layout(xaxis_title=x_title or T["cases"], yaxis_title="", showlegend=False)
    return fig


# ---------------------------------------------------------------- header
st.title(T["title"])
st.caption(T["intro"] + " " + T["source_r5"])

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric(T["kpi_cases"], kpis["cases_iran"],
          help=T["kpi_cases_help"].format(share=kpis["share_iran"], total=kpis["cases_world"]))
c2.metric(T["kpi_rank"], f"#{kpis['iran_rank_target']}", help=T["kpi_rank_help"])
c3.metric(T["kpi_force"], kpis["iran_cases_in_force_2025"])
c4.metric(T["kpi_us"], kpis["iran_cases_by_us"])
c5.metric(T["kpi_eu"], kpis["iran_cases_by_eu"])

tab_time, tab_senders, tab_instr, tab_outcomes, tab_global, tab_about = st.tabs(T["tabs"])


# ---------------------------------------------------------------- tab: over time
with tab_time:
    timeline = load_csv("iran_timeline.csv")
    events = load_csv("key_events.csv")
    if LANG == "de":
        events["event"] = events["year"].map(EVENTS_DE)

    show_events = st.toggle(T["show_events"], value=True)

    chart_title(T["t_timeline"])
    fig = go.Figure()
    fig.add_scatter(
        x=timeline["year"], y=timeline["cases_in_force"], mode="lines", name=T["cases_in_force"],
        line=dict(color=COLOR_MAIN, width=2), fill="tozeroy", fillcolor="rgba(31,78,121,0.12)",
        hovertemplate="%{x}: %{y}<extra></extra>",
    )
    new = timeline[timeline["new_cases"] > 0]
    fig.add_scatter(
        x=new["year"], y=new["cases_in_force"], mode="markers+text", name=T["years_new"],
        marker=dict(color=COLOR_NEW, size=8), text="+" + new["new_cases"].astype(str),
        textposition="top left", textfont=dict(size=10, color=COLOR_DARK),
        customdata=new["new_cases"], hovertemplate="%{x}: +%{customdata}<extra></extra>",
    )
    if show_events:
        for _, row in events.iterrows():
            fig.add_vline(x=row["year"], line=dict(color="#bbbbbb", dash="dot", width=1))
            fig.add_annotation(
                x=row["year"], y=1, yref="paper", text=f"{row['year']} {row['event']}", textangle=-90,
                showarrow=False, xanchor="right", yanchor="top", font=dict(size=10, color=COLOR_DARK),
            )
    fig.update_xaxes(dtick=5, range=[1977, 2027])
    fig.update_yaxes(title_text=T["cases_in_force"], range=[0, timeline["cases_in_force"].max() * 1.55])
    show_chart(fig, height=540)
    st.caption(T["cap_timeline"] + " " + T["source_r5"])

    timeline["continuing"] = timeline["cases_in_force"] - timeline["new_cases"]
    chart_title(T["t_new_cont"])
    fig = go.Figure()
    fig.add_bar(x=timeline["year"], y=timeline["continuing"], name=T["continuing"], marker_color=COLOR_MAIN,
                hovertemplate="%{x}: %{y}<extra></extra>")
    fig.add_bar(x=timeline["year"], y=timeline["new_cases"], name=T["new"], marker_color=COLOR_NEW,
                hovertemplate="%{x}: %{y}<extra></extra>")
    fig.update_layout(barmode="stack", bargap=0.15, legend_traceorder="normal")
    fig.update_xaxes(dtick=5, range=[1977, 2027])
    fig.update_yaxes(title_text=T["cases_in_force"])
    show_chart(fig)
    st.caption(T["cap_new_cont"] + " " + T["source_r5"])
    show_data(timeline[["year", "cases_in_force", "new_cases", "continuing"]].sort_values("year", ascending=False))

    st.markdown(T["txt_time"])


# ---------------------------------------------------------------- tab: who sanctions Iran
with tab_senders:
    iran_senders = load_csv("iran_senders.csv").sort_values("cases", ascending=False)
    actors = load_csv("iran_sender_actors.csv").sort_values("cases", ascending=False)

    chart_title(T["t_iran_map"])
    fig = px.choropleth(
        iran_senders, locations="iso3", color="cases", hover_name="country",
        color_continuous_scale=MAP_REDS, hover_data={"iso3": False, "cases": True},
        labels={"cases": T["cases"]},
    )
    fig.add_trace(go.Choropleth(
        locations=["IRN"], z=[1], colorscale=[[0, COLOR_DARK], [1, COLOR_DARK]],
        showscale=False, hovertemplate="Iran<extra></extra>",
    ))
    fig.update_layout(coloraxis_colorbar=dict(title=T["cases"]))
    show_map(fig)
    st.caption(T["cap_iran_map"] + " " + T["source_r5"])

    chart_title(T["t_actors"])
    show_chart(ranked_bars(actors.head(10), "sender", "cases"), height=440)
    st.caption(T["cap_actors"] + " " + T["source_r5"])
    show_data(actors, T["data_actors"])
    show_data(iran_senders[["country", "iso3", "cases"]], T["data_map_countries"])
    st.caption(T["lang_note"])


# ---------------------------------------------------------------- tab: instruments
with tab_instr:
    instruments = load_csv("iran_instruments.csv")
    by_period = load_csv("iran_instruments_by_period.csv")
    shares = load_csv("instrument_shares_over_time.csv")
    subtypes = load_csv("financial_subtypes.csv")
    subtypes_period = load_csv("financial_subtypes_by_period.csv")

    left, right = st.columns(2)
    with left:
        chart_title(T["t_instr"])
        show_chart(comparison_bars(instruments, "instrument", "iran_share", "Iran", T["x_instr"]))
        st.caption(T["cap_instr"] + " " + T["source_r5"])
    with right:
        chart_title(T["t_fin"])
        show_chart(comparison_bars(subtypes, "subtype", "iran_share", "Iran", T["x_fin"]))
        st.caption(T["source_fs"])

    instrument_order = instruments.sort_values("iran_cases", ascending=False)["instrument"].tolist()
    instrument_choice = st.selectbox(T["select_instr"], instrument_order, index=1, format_func=lab)
    data = shares[shares["instrument"] == instrument_choice].copy()
    data["group"] = data["group"].map(lab)

    chart_title(T["t_instr_time"].format(instr=lab(instrument_choice)))
    fig = px.line(data, x="year", y="share", color="group",
                  color_discrete_map={lab("Iran"): COLOR_MAIN, lab("World"): COLOR_WORLD})
    fig.update_traces(line_width=2, hovertemplate="%{x}: %{y:.0f}%<extra></extra>")
    for year, key in ((2016, "jcpoa"), (2018, "us_exit")):
        fig.add_vline(x=year, line=dict(color="#bbbbbb", dash="dot", width=1))
        fig.add_annotation(x=year, y=1, yref="paper", text=T[key], showarrow=False, xanchor="left",
                           yanchor="top", font=dict(size=10, color=COLOR_DARK))
    fig.update_layout(xaxis_title="", yaxis_title=T["y_share"], yaxis_range=[0, 105])
    show_chart(fig)
    st.caption(T["cap_instr_time"] + " " + T["source_r5"])

    show_data(by_period, T["data_instr_period"])
    show_data(subtypes_period, T["data_fin_period"])
    st.markdown(T["txt_instr"])


# ---------------------------------------------------------------- tab: objectives & outcomes
with tab_outcomes:
    outcomes = load_csv("iran_outcomes.csv")
    comparison = load_csv("outcome_comparison.csv")

    st.metric(T["kpi_ended"], f"{kpis['iran_ended']} / {kpis['iran_ongoing']}")

    order = ["Full success", "Partial success", "Negotiated settlement", "Failed"]
    colors = {"Full success": COLOR_MAIN, "Partial success": COLOR_LIGHT,
              "Negotiated settlement": "#bdbdbd", "Failed": COLOR_DARK}
    objective_order = outcomes.groupby("objective")["count"].sum().sort_values().index.tolist()

    chart_title(T["t_outcomes"])
    fig = go.Figure()
    for outcome in order:
        part = outcomes[outcomes["outcome"] == outcome].set_index("objective").reindex(objective_order)
        fig.add_bar(
            y=[lab(o) for o in objective_order], x=part["count"], orientation="h", name=lab(outcome),
            marker_color=colors[outcome], text=part["count"], textposition="inside",
            insidetextanchor="middle", textfont_color="white",
            hovertemplate="%{y}: %{x}<extra>" + lab(outcome) + "</extra>",
        )
    fig.update_layout(barmode="stack", xaxis_title=T["x_objectives"], yaxis_title="", legend_traceorder="normal")
    show_chart(fig)
    st.caption(T["cap_outcomes"] + " " + T["source_r5"])

    chart_title(T["t_outcome_comp"])
    comp = comparison.set_index("outcome").reindex(order).reset_index()
    fig = go.Figure()
    for group, color in (("Iran", COLOR_MAIN), ("World", COLOR_WORLD)):
        values = comp[group] * 100
        fig.add_bar(x=[lab(o) for o in comp["outcome"]], y=values, name=lab(group), marker_color=color,
                    text=values.round(0).astype(int).astype(str) + "%", textposition="outside",
                    hovertemplate="%{x}: %{y:.0f}%<extra></extra>")
    fig.update_layout(barmode="group", yaxis_title=T["y_share"], yaxis_range=[0, 70], legend_traceorder="normal")
    show_chart(fig)
    show_data(comp)
    st.markdown(T["txt_outcomes"])


# ---------------------------------------------------------------- tab: global context
with tab_global:
    top_targets = load_csv("top_targets.csv").sort_values("rank")
    world = load_csv("world_senders.csv").sort_values("cases", ascending=False)
    eu_decades = load_csv("eu_per_decade.csv")
    eu_targets = load_csv("eu_top_targets.csv").sort_values("cases", ascending=False)
    eu_instruments = load_csv("eu_instruments.csv")
    sender_comparison = load_csv("sender_comparison.csv").sort_values("world_rank")

    st.subheader(T["h_targets"])
    chart_title(T["t_targets"])
    show_chart(ranked_bars(top_targets.head(10), "target", "total_cases", highlight="Iran"))
    show_data(top_targets, T["data_targets"])

    st.subheader(T["h_world"])
    chart_title(T["t_world_map"])
    class_order = ["1–5", "6–20", "21–50", "51–100", "100+"]
    fig = px.choropleth(
        world.sort_values("cases"), locations="iso3", color="class", hover_name="country",
        hover_data={"cases": True, "iso3": False, "class": False}, labels={"cases": T["cases"]},
        category_orders={"class": class_order}, color_discrete_sequence=MAP_CLASS_COLORS,
    )
    fig.update_layout(legend_title_text=T["cases"])
    show_map(fig)
    st.caption(T["cap_world_map"] + " " + T["source_r5"])
    chart_title(T["h_sender_countries"])
    sender_countries = load_csv("top_sender_countries.csv").sort_values("rank")
    st.dataframe(cols(sender_countries[["rank", "country", "cases", "own_cases", "via_eu", "against_iran"]]),
                 use_container_width=True, hide_index=True)
    st.caption(T["cap_senders"].format(eu=kpis["eu_cases"], un=kpis["un_cases"]) + " " + T["source_r5"])

    st.subheader(T["h_eu"])
    e1, e2, e3 = st.columns(3)
    e1.metric(T["kpi_eu_cases"], kpis["eu_cases"], help=T["kpi_eu_rank_help"].format(rank=kpis["eu_rank"]))
    e2.metric(T["kpi_eu_force"], kpis["eu_ongoing"])
    e3.metric(T["kpi_eu_iran"], kpis["iran_cases_by_eu"])

    left, right = st.columns(2)
    with left:
        chart_title(T["t_eu_decades"])
        decades = eu_decades.copy()
        if LANG == "de":
            decades["decade"] = decades["decade"].str.replace("s", "er", regex=False)
        fig = go.Figure(go.Bar(x=decades["decade"], y=decades["new_cases"], marker_color=COLOR_MAIN,
                               text=decades["new_cases"], textposition="outside",
                               hovertemplate="%{x}: %{y}<extra></extra>"))
        fig.update_layout(yaxis_title=T["new_cases"], yaxis_range=[0, decades["new_cases"].max() * 1.2])
        show_chart(fig)
        st.caption(T["cap_eu_decades"] + " " + T["source_r5"])
    with right:
        chart_title(T["t_eu_targets"])
        show_chart(ranked_bars(eu_targets, "target", "cases", highlight="Iran"))

    chart_title(T["t_eu_instr"])
    show_chart(comparison_bars(eu_instruments, "instrument", "eu_share", "EU", T["x_instr"]))

    st.markdown(T["txt_germany"].format(rank=kpis["germany_rank"], cases=kpis["germany_cases_incl_eu"],
                                        own=kpis["germany_own_cases"]))

    st.subheader(T["h_compare"])
    sender_comparison["top_objectives"] = sender_comparison["top_objectives"].map(translate_objective_codes)
    st.dataframe(cols(sender_comparison), use_container_width=True, hide_index=True)
    st.caption(T["cap_compare"] + " " + T["source_r5"] + " " + T["lang_note"])


# ---------------------------------------------------------------- tab: about
with tab_about:
    st.markdown(T["about"])
