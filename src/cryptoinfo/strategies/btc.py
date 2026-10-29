"""Bitcoin trend-following strategy with volatility filter (informational signals only)."""

def sma(prices, period):
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period

def atr_proxy(ohlcv, period=14):
    """Simple high-low range as ATR proxy for volatility filter."""
    if len(ohlcv) < period:
        return None
    ranges = [abs(r["high"] - r["low"]) for r in ohlcv[-period:]]
    return sum(ranges) / period

def signal(ohlcv):
    """Return LONG / SHORT / HOLD based on SMA crossover + volatility filter."""
    closes = [r["close"] for r in ohlcv]
    short = sma(closes, 5)
    long = sma(closes, 20)
    vol = atr_proxy(ohlcv)
    if short is None or long is None or vol is None:
        return "HOLD"
    # Simple volatility filter: only signal if recent range is not extreme
    avg_price = sum(closes[-20:]) / 20 if len(closes) >= 20 else closes[-1]
    vol_ratio = vol / avg_price if avg_price else 0
    if vol_ratio > 0.05:  # high volatility — reduce confidence, default HOLD
        return "HOLD"
    if short > long * 1.002:  # small buffer to reduce noise
        return "LONG"
    elif short < long * 0.998:
        return "SHORT"
    return "HOLD"
