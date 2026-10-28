"""Altcoin volatility-adjusted mean reversion (informational)."""
def bollinger_signal(ohlcv, period=20, std_mult=2.0):
    closes = [r["close"] for r in ohlcv]
    if len(closes) < period:
        return "HOLD"
    window = closes[-period:]
    mean = sum(window) / period
    variance = sum((x - mean) ** 2 for x in window) / period
    std = variance ** 0.5
    upper = mean + std_mult * std
    lower = mean - std_mult * std
    last = closes[-1]
    if last < lower:
        return "LONG"  # mean reversion buy
    if last > upper:
        return "SHORT"
    return "HOLD"

signal = bollinger_signal
