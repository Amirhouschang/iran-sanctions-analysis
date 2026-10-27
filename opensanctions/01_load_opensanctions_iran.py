import pandas as pd
from pathlib import Path

RAW = Path("data/raw/opensanctions_targets_2026-10-27.csv")

# 1. Einmal komplett herunterladen (nur wenn noch nicht vorhanden)
if not RAW.exists():
    RAW.parent.mkdir(parents=True, exist_ok=True)
    url = "https://data.opensanctions.org/datasets/latest/default/targets.simple.csv"
    pd.read_csv(url, low_memory=False).to_csv(RAW, index=False)

# 2. Lokal laden und filtern
df = pd.read_csv(RAW, low_memory=False)
iran = df[df["countries"].fillna("").str.split(";").apply(lambda x: "ir" in x)]
iran.to_csv("data/opensanctions_iran_2026-10-27.csv", index=False)