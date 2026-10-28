"""Simple risk notes (informational only)."""
def position_size_hint(signal: str, volatility: float = 0.05) -> str:
    if signal == "HOLD":
        return "No position"
    # Demo: fixed fractional with vol adjustment
    base = 0.01  # 1%
    adjusted = base / (1 + volatility * 10)
    return f"Suggested size ~{adjusted:.2%} of portfolio (demo only, not advice)"
