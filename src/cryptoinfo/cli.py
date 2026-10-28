"""CLI entry point."""
from cryptoinfo.data import load_ohlcv
from cryptoinfo.strategies.btc import signal as btc_signal
from cryptoinfo.strategies.eth import signal as eth_signal
from cryptoinfo.strategies.alts import signal as alts_signal
from cryptoinfo.security import audit_log, validate_ohlcv
from cryptoinfo.risk import position_size_hint

def demo():
    print("=== Crypto Trading Information System Demo ===")
    print("Synthetic data only. Not financial advice. No live trading.\n")
    # Demo with minimal synthetic series
    sample = [
        {"timestamp": "2024-01-01", "open": 100, "high": 105, "low": 98, "close": 102, "volume": 1000},
        {"timestamp": "2024-01-02", "open": 102, "high": 110, "low": 101, "close": 108, "volume": 1500},
    ] * 15  # pad for indicators
    validate_ohlcv(sample)
    btc = btc_signal(sample)
    eth = eth_signal(sample)
    alt = alts_signal(sample)
    print(f"BTC trend signal: {btc}")
    print(f"ETH momentum signal: {eth}")
    print(f"Alts mean-reversion signal: {alt}")
    print(position_size_hint(btc))
    audit_log("demo_run", {"btc": btc, "eth": eth, "alt": alt})
    print("\nSee docs/architecture.md, docs/security-architecture.md, docs/strategies-per-asset.md")

if __name__ == "__main__":
    demo()
