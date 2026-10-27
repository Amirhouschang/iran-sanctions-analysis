import csv
import json
import shutil
import urllib.request
from pathlib import Path

BASE = Path(__file__).parent
RAW = BASE / "data/raw/opensanctions_targets_nested_2026-10-27.json"
IRAN = BASE / "data/opensanctions_iran_2026-10-27.csv"
OUT = BASE / "data/opensanctions_iran_positionen_2026-10-27.csv"
URL = "https://data.opensanctions.org/datasets/latest/default/targets.nested.json"

# 1. Einmal herunterladen (große Datei, wird gestreamt)
if not RAW.exists():
    RAW.parent.mkdir(parents=True, exist_ok=True)
    print("Download läuft ...")
    with urllib.request.urlopen(URL) as r, open(RAW, "wb") as f:
        shutil.copyfileobj(r, f)

# 2. IDs der Iran-Einträge laden
with open(IRAN, encoding="utf-8") as f:
    iran_ids = {row["id"] for row in csv.DictReader(f)}

def erster(props, key):
    werte = props.get(key) or []
    return werte[0] if werte else ""

# 3. Datei Zeile für Zeile lesen, nur Iran-Personen auswerten
zeilen = []
with open(RAW, encoding="utf-8") as f:
    for line in f:
        e = json.loads(line)
        if e.get("id") not in iran_ids or e.get("schema") != "Person":
            continue
        props = e.get("properties", {})

        # a) Ämter mit Zeitraum (vor allem PEPs)
        for occ in props.get("positionOccupancies", []):
            op = occ.get("properties", {})
            for post in op.get("post", []):
                pp = post.get("properties", {}) if isinstance(post, dict) else {}
                zeilen.append({
                    "id": e["id"],
                    "position": erster(pp, "name"),
                    "start": erster(op, "startDate"),
                    "ende": erster(op, "endDate"),
                    "status": erster(op, "status"),
                    "quelle": "Occupancy",
                })

        # b) Positionen als Freitext (oft bei Sanktionierten)
        for pos in props.get("position", []):
            zeilen.append({
                "id": e["id"], "position": pos,
                "start": "", "ende": "", "status": "", "quelle": "Freitext",
            })

with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["id", "position", "start", "ende", "status", "quelle"])
    w.writeheader()
    w.writerows(zeilen)

print("Positionen:", len(zeilen))
print("Personen mit Position:", len({z["id"] for z in zeilen}))