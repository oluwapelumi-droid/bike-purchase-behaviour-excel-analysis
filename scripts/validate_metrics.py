"""Validate key figures from the cleaned Bike Buyers CSV."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "cleaned_bike_buyers.csv"

with DATA.open(newline="", encoding="utf-8-sig") as stream:
    rows = list(csv.DictReader(stream))

assert len(rows) == 1000, f"Expected 1,000 customers, got {len(rows)}"
purchase_col = next((c for c in rows[0] if c.lower().strip() in {"purchased bike", "purchased_bike"}), None)
assert purchase_col is not None, f"Could not locate purchase column: {list(rows[0])}"
buyers = sum(r[purchase_col].strip().lower() == "yes" for r in rows)
assert buyers == 481, f"Expected 481 buyers, got {buyers}"
print(f"OK: customers={len(rows)}, buyers={buyers}, nonbuyers={len(rows) - buyers}, purchase_rate={buyers/len(rows):.1%}")
