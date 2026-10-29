"""Ethereum momentum + volume / network activity proxy strategy (informational signals only)."""

def rate_of_change(prices, period=5):
    if len(prices) < period + 1:
        return 0.0
    return (prices[-1] - prices[-period - 1]) / prices[-period - 1]

def signal(ohlcv):
    """Momentum confirmed by volume spike (proxy for network activity)."""
    closes = [r["close"] for r in ohlcv]
    volumes = [r.get("volume", 0) for r in ohlcv]
    roc = rate_of_change(closes)
    if len(volumes) < 5:
        return "HOLD"
    avg_vol = sum(volumes[-5:]) / 5
    recent_vol = volumes[-1]
    vol_confirm = recent_vol > avg_vol * 1.3  # stronger confirmation threshold
    if roc > 0.025 and vol_confirm:
        return "LONG"
    if roc < -0.025 and vol_confirm:
        return "SHORT"
    return "HOLD"
