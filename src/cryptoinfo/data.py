"""Data loading and validation. Synthetic only."""
import csv
from pathlib import Path

def load_ohlcv(path: str):
    """Load synthetic OHLCV. Returns list of dicts."""
    records = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append({
                "timestamp": row["timestamp"],
                "open": float(row["open"]),
                "high": float(row["high"]),
                "low": float(row["low"]),
                "close": float(row["close"]),
                "volume": float(row["volume"]),
            })
    return records
