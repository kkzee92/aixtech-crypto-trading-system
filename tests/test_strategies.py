from cryptoinfo.strategies.btc import signal as btc_signal
from cryptoinfo.strategies.eth import signal as eth_signal

def test_btc_hold_short_data():
    ohlcv = [{"close": 100}] * 10
    assert btc_signal(ohlcv) == "HOLD"

def test_eth_hold():
    ohlcv = [{"close": 100, "volume": 10}] * 10
    assert eth_signal(ohlcv) == "HOLD"
