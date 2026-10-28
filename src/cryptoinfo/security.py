"""Security helpers: audit logging, basic validation."""
import json
from datetime import datetime, timezone

def audit_log(event: str, details: dict):
    """Structured audit entry (stdout for demo; in prod -> secure store)."""
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "event": event,
        "details": details,
        "synthetic": True,
    }
    print(json.dumps(entry))
    return entry

def validate_ohlcv(records):
    """Basic sanity checks."""
    for r in records:
        if not (r["low"] <= r["open"] <= r["high"] and r["low"] <= r["close"] <= r["high"]):
            raise ValueError("Invalid OHLC")
        if r["volume"] < 0:
            raise ValueError("Negative volume")
    return True
