"""Bitcoin trend-following strategy (informational signals only)."""
def sma(prices, period):
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period

def signal(ohlcv):
    closes = [r["close"] for r in ohlcv]
    short = sma(closes, 5)
    long = sma(closes, 20)
    if short is None or long is None:
        return "HOLD"
    if short > long:
        return "LONG"
    elif short < long:
        return "SHORT"
    return "HOLD"
