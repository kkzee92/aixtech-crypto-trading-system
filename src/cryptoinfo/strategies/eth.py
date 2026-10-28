"""Ethereum momentum + volume strategy (informational)."""
def rate_of_change(prices, period=5):
    if len(prices) < period + 1:
        return 0.0
    return (prices[-1] - prices[-period-1]) / prices[-period-1]

def signal(ohlcv):
    closes = [r["close"] for r in ohlcv]
    volumes = [r["volume"] for r in ohlcv]
    roc = rate_of_change(closes)
    avg_vol = sum(volumes[-5:]) / min(5, len(volumes)) if volumes else 0
    recent_vol = volumes[-1] if volumes else 0
    if roc > 0.02 and recent_vol > avg_vol * 1.2:
        return "LONG"
    if roc < -0.02 and recent_vol > avg_vol * 1.2:
        return "SHORT"
    return "HOLD"
